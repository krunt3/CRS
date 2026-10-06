#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
simu_combat.py : essais d'équilibrage du combat du Jeu B (CRS), par simulation Monte-Carlo.

Python 3.8+, bibliothèque standard seulement. Reproductible : toutes les tirages dérivent de
SEED (une graine par cellule de résultat, obtenue par CRC32 de l'étiquette de la cellule).

Usage
    python3 outils/simu_combat.py                      # rapport complet (Markdown) sur la sortie standard
    python3 outils/simu_combat.py --sections echelle,K # seulement certaines sections
    python3 outils/simu_combat.py --n 500 --seed 7     # moins de tirages, autre graine
    sections : echelle, livre, jeu, K, tank, leviers, variantes, competence

Ce que la simulation fait (voir docs/trame/07-essais-equilibrage.md pour les limites)
    * temps abstrait : 1 round = 4 s ; les héros agissent par ordre d'initiative, puis les monstres ;
    * trois modèles de dégâts reçus par le héros (docs/mecaniques/01-chasse-et-combat.md §4.5) :
        A = Livre I : l'Endurance absorbe d'abord, le reste va à la Vitalité ;
        B = Livres II / IX : dégâts directs sur la Vitalité, chaque attaque coûte de l'Endurance ;
        C = deux barres séparées : Vitalité = vie, Endurance = carburant (esquive, garde) ;
    * deux « échelles » (PRESETS) : "livre" (tour par tour, d20 contre Défense, chiffres bruts des Livres III/IX)
      et "jeu" (temps réel tactile : conversions de docs/mecaniques/01 §4 : facteur 0,65, armure 5 % par CA,
      esquive du joueur, garde du bouclier, K sur la Vitalité des monstres).
Tout ce qui est INVENTÉ (non tiré des livres ni des documents) est signalé « INVENTÉ » dans les commentaires.
"""
import argparse
import math
import random
import statistics
import sys
import zlib

# =====================================================================================
# PARAMÈTRES GLOBAUX (modifiables)
# =====================================================================================
SEED = 20261006                 # graine de base (date de la décision de krunt)
N_DEFAUT = 1500                 # tirages par cellule de résultat
DUREE_ROUND_S = 4.0             # un round = 4 secondes (consigne)
ROUNDS_MAX = 150                # 10 minutes : au-delà, combat compté comme non gagné (« abandon »)

# Deux jeux de règles d'échelle. Les valeurs "jeu" viennent de docs/mecaniques/01 §3.2, §4.3, §12 ; les autres INVENTÉES.
PRESETS = {
    "livre": dict(
        nom="livre",
        touches=1.0,             # 1 Acte d'attaque par héros et par round (Livre I ch. 7)
        cad_boss=1.0, cad_escorte=1.0,
        f_recu=1.0,              # dégâts du Livre III pris tels quels, en cases de Vitalité (1 point = 1 case)
        armure_pct=False,        # l'armure ne fait que monter la Défense (Livre I)
        regen_end=0.0,           # pas de régénération d'Endurance en combat (Livre I)
        b_cout_end=1.0,          # modèle B : Endurance par Acte d'attaque (INVENTÉ : 1, comme la Riposte du Livre I)
        perseverer=1.0,          # cases de Vitalité perdues quand on agit à Endurance 0 (docs/mecaniques/01 §3.2)
        busy_potion=1.0, busy_tech=0.0, busy_soin=1.0, techs_round=1,
        stun_frac=1.0,           # renversé : perd l'Acte suivant
        esquive_skill=False, hit_monstre="d20",
    ),
    "jeu": dict(
        nom="jeu",
        touches=2.4,             # 0,6 touche utile par seconde x 4 s (docs/mecaniques/01 §12)
        cad_boss=1.6,            # une attaque toutes les 2,5 s (docs/mecaniques/01 §12)
        cad_escorte=0.6,         # INVENTÉ : les éclaireurs attaquent « en alternance »
        f_recu=0.65 / 4.0,       # facteur 0,65 puis conversion point de coup -> case (1 case = 4 PC), §4.1-4.2
        armure_pct=True,         # PC reçus x (1 - min(0,35 ; 0,05 x CA)), §4.3
        regen_end=4.0,           # INVENTÉ : 2 /s après 0,8 s (§3.2) ramené à ~1 /s utile (garde, roulades, coups)
        b_cout_end=0.4,          # modèle B : Endurance par touche (INVENTÉ)
        perseverer=1.0,          # 4 PC = 1 case par round d'action à Endurance 0 (§3.2)
        busy_potion=0.3, busy_tech=0.12, busy_soin=0.35, techs_round=2,
        stun_frac=0.35,          # renversé : 1 s au sol + 0,4 s de relevé sur un round de 4 s (§5.1)
        esquive_skill=True, hit_monstre="auto",
    ),
}
ESQUIVE_BASE = 0.55             # 55 % de touches évitées par un joueur moyen (docs/mecaniques/01 §12)
ESQUIVE_PAR_AGI = 0.02          # INVENTÉ : +/- 2 points par point d'AGI autour de 8
COUT_ESQUIVE = 2.0              # roulade = 2 Endurance (§3.2)
GARDE_REDUC = 0.60              # la garde (bouclier) retire 60 % des dégâts (§3.2)
GARDE_P = 0.70                  # INVENTÉ : part des coups parés à temps par un joueur moyen
GARDE_COUT_PAR_PC = 0.5         # 1 Endurance par 2 PC bloqués (§3.2)
P_PROVOC = 0.80                 # INVENTÉ : un monstre cible le provocateur avec cette probabilité (Livre VI : « en priorité »)
P_INTERPO = 0.50                # INVENTÉ : part des attaques sur un allié qu'Interposition peut capter (positionnement)
RESERVE_END = 2.0               # Endurance gardée en réserve avant une Technique de Posture (INVENTÉ)
PTS_ATTR = [0, 2, 4, 4, 7]      # points d'attribut cumulés par palier d'histoire (docs/trame/04 §5.3)

# Statistiques des quatre fiches équilibrées (docs/trame/04 §4.1 à 4.5, §6.3), avec les corrections de krunt.
HEROS = {
    "Krunt3": dict(FOR=9, AGI=8, END=9, atk=13, dice=(2, 6), dmg_attr=9, ca=2, defense=19, init=15,
                   mana=6, mode="flux", melee=True, bouclier=False, arme="tranchant", poids_cible=1.0),
    "Taranis": dict(FOR=5, AGI=12, END=5, atk=16, dice=(1, 8), dmg_attr=12, ca=2, defense=19, init=18,
                    mana=6, mode="rituel", melee=False, bouclier=False, arme="perçant", poids_cible=0.5),
    "Cyril": dict(FOR=5, AGI=6, END=6, atk=9, dice=(1, 8), dmg_attr=5, ca=1, defense=13, init=15,
                  mana=8, mode="flux", melee=True, bouclier=False, arme="tranchant", poids_cible=0.8),
    "Pascal": dict(FOR=7, AGI=6, END=8, atk=10, dice=(1, 6), dmg_attr=7, ca=5, defense=19, init=12,
                   mana=6, mode="ancrage", melee=True, bouclier=True, arme="tranchant", poids_cible=1.0),
}

# Options de simulation par défaut (modifiables par expérience)
OPTS_DEFAUT = dict(
    tank=True,                  # Krunt3 joue Provocation / Mur de Chair / Interposition
    flanc_limite=True,          # Flanc Coordonné : au plus un bonus par cible et par round (docs/trame/04 §7.3)
    bagage_taranis=True,        # correction de krunt : Taranis part avec un bagage (contenu INVENTÉ ci-dessous)
    pascal="base",              # "base" = attaque de base seule (correction de krunt) ; "soutien" ; "bombe"
    souffle=False,              # Souffle du Réceptacle de Krunt3 (docs/trame/04 §5.4, INVENTÉ)
    ouverture=True,             # Provocation : « les alliés bénéficient d'une Ouverture gratuite » (Livre VI)
    esquive=ESQUIVE_BASE,       # compétence du joueur (esquive_base)
    kd=1.0,                     # coefficient de réglage des DÉGÂTS des monstres (en plus du facteur 0,65) ; INVENTÉ
    prio_escorte=True,          # les héros tuent les éclaireurs d'abord
    phases=True,                # phases et agonie des fiches
    terrain=None,               # {"feu_p":.., "instable_p":..} (INVENTÉ)
    potions=None,               # surcharge du nombre de Potions de Soin par héros
)
# Bagage de départ de Taranis (INVENTÉ ; krunt : « il part avec un bagage de départ »)
BAGAGE_TARANIS = dict(potions=4, piege_colle=1, huile_feu=1)
POTIONS_BASE = dict(Krunt3=2, Taranis=2, Cyril=2, Pascal=3)   # INVENTÉ ; Pascal alchimiste : 3 potions mineures


# =====================================================================================
# OUTILS
# =====================================================================================
def seed_de(etiquette, base=None):
    return (SEED if base is None else base) ^ zlib.crc32(etiquette.encode("utf-8"))


def de(rng, n, f):
    return sum(rng.randint(1, f) for _ in range(n))


def stoch(rng, x):
    i = int(x)
    return i + (1 if rng.random() < x - i else 0)


def moy_de(n, f):
    return n * (f + 1) / 2.0


def evolue(c, palier):
    """Héros évolué : palier 0 = début ; 1..4 = 25 %, 50 %, 75 %, 100 % de l'histoire (docs/trame/04 §5.3). INVENTÉ en détail."""
    c = dict(c)
    if palier == 0:
        c["qual"] = 0
        return c
    pts = PTS_ATTR[palier]
    gain_end, gain_att = (pts + 1) // 2, pts // 2
    c["END"] += gain_end
    c["dmg_attr"] += gain_att
    c["atk"] += palier + gain_att // 2          # rang d'École (+1 par rang au-dessus de I) + attribut
    c["ca"] += palier // 2                       # armure de meilleure série
    c["defense"] += gain_end + palier // 2
    c["qual"] = palier // 2                      # qualité de l'arme (Supérieure +1, Rare/Signature +1...)
    return c


# =====================================================================================
# MONSTRES (Livre III, section V ; stats copiées, attaques simplifiées)
# =====================================================================================
def A(nom, nd, df, flat, w, hits=1, atk=None, dot=None, renv=None, aoe=0, special=None, pen_def=0, pen_second=0):
    return dict(nom=nom, nd=nd, df=df, flat=flat, w=w, hits=hits, atk=atk, dot=dot, renv=renv, aoe=aoe,
                special=special, pen_def=pen_def, pen_second=pen_second)


# Chef de meute de la démo (id cro02, nom de travail du roster : Dorgane ; nom du Livre III : Velodrak). CR 4, 2 phases.
CHEF_P1 = [
    A("Morsure déchirante", 2, 6, 7, 0.40, dot=(1, 3, 0.5)),
    A("Frappe de queue", 1, 8, 7, 0.20, aoe=2, renv=("AGI", 13)),
    A("Charge déstabilisatrice", 2, 8, 7, 0.20, renv="auto"),
    A("Vocalisation de commandement", 0, 0, 0, 0.20, special="vocal"),
]
CHEF_P2 = [
    A("Déluge de crocs", 1, 6, 7, 0.30, hits=3),
    A("Rugissement de dominance", 0, 0, 0, 0.15, special="secoue"),
    A("Morsure renforcée", 3, 6, 7, 0.30, dot=(1, 3, 1.0)),
    A("Charge aveugle", 2, 8, 7, 0.25, hits=2, pen_second=2, renv="auto"),
]
# Éclaireur (id cro01 ; Velokrak). CR 1, Vitalité 6, Défense 7.
ECL = [
    A("Morsure en passant", 1, 4, 3, 0.40, atk=3),
    A("Griffes aux jarrets", 1, 4, 5, 0.30, atk=5),
    A("Charge en coin", 2, 4, 3, 0.30, atk=3, renv=("FOR", 12), special="coin"),
]
# Élite : Garuvorn, CR 12 (Vitalité 58, Défense 19, FOR 13, AGI 9), 3 phases à 65 % et 30 %.
GAR_P1 = [
    A("Charge explosive", 3, 8, 13, 0.30, renv=("AGI", 16)),
    A("Morsure venimeuse", 2, 8, 13, 0.40, dot=(3, 10, 0.6)),
    A("Coup de queue latéral", 2, 6, 13, 0.20, aoe=2, renv=("AGI", 14)),
    A("Cri de territoire", 0, 0, 0, 0.10, special="cri"),
]
GAR_P2 = [
    A("Morsure venimeuse", 2, 8, 13, 0.30, dot=(3, 10, 0.6)),
    A("Charge explosive", 3, 8, 13, 0.15, renv=("AGI", 16)),
    A("Crachat envenimé", 2, 6, 0, 0.15, dot=(3, 10, 1.0)),
    A("Saut de flanquement", 2, 8, 13, 0.20, pen_def=3),
    A("Morsure de maintien", 2, 8, 13, 0.20, dot=(3, 10, 1.0)),
]
GAR_P3 = [
    A("Frénésie de crocs", 1, 8, 13, 0.40, hits=4),
    A("Impact de crête", 3, 8, 13, 0.30, pen_def=3),
    A("Morsure venimeuse", 2, 8, 13, 0.30, dot=(3, 10, 0.6)),
]
GAR_AGONIE = [A("Dernier impact", 3, 8, 13, 1.0)]
# Légendaire : Garuvorn Sourd, CR 18 (Vitalité 79, Défense 21, FOR 16), 2 phases (40 %), 2 attaques par action.
SOU_P12 = [
    A("Charge explosive", 3, 8, 16, 0.30, renv=("AGI", 16)),
    A("Morsure venimeuse", 2, 8, 16, 0.35, dot=(4, 10, 0.7)),
    A("Coup de queue latéral", 2, 6, 16, 0.20, aoe=2, renv=("AGI", 14)),
    A("Crachat envenimé", 2, 6, 0, 0.15, dot=(4, 10, 1.0)),
]
SOU_P3 = [
    A("Frénésie totale", 1, 8, 16, 0.60, hits=4),
    A("Morsure venimeuse", 2, 8, 16, 0.40, dot=(4, 10, 0.7)),
]


class Mon:
    def __init__(self, nom, vit_livre, K, defense, atk, role, seuils, listes, res=None, faibl=None,
                 cad=1.0, cad_p2=1.0, att_par_action=1, agonie=None, agonie_att=None, regen=0.0, cr=1):
        self.nom, self.role, self.defense, self.atk, self.cr = nom, role, defense, atk, cr
        self.vitmax = vit_livre * K
        self.vit = self.vitmax
        self.seuils, self.listes = seuils, listes        # phase i active tant que vit/vitmax > seuils[i]
        self.res = res or {}                             # {"tranchant": 0.75, ...}
        self.faibl = faibl or {}                         # {"feu": 1.5}
        self.cad, self.cad_p2 = cad, cad_p2
        self.att_par_action = att_par_action
        self.agonie, self.agonie_att = agonie, agonie_att
        self.regen = regen * K
        self.expose = 0
        self.immob = 0.0
        self.mort = False
        self.agonie_restante = None
        self.declenche = False
        self.cri_fait = False
        self.hit_par = set()

    def ratio(self):
        return max(0.0, self.vit) / self.vitmax

    def phase(self, trig_force=0.30):
        r = self.ratio()
        if self.role == "chef":
            if r <= 0.5 and (self.declenche or r <= trig_force):
                return 1
            return 0
        idx = 0
        for i, s in enumerate(self.seuils):
            if r <= s:
                idx = i + 1
        return min(idx, len(self.listes) - 1)


def construit(scenario, Kb, Km, phases=True):
    """Retourne (boss ou None, escortes, palier par défaut du scénario)."""
    def chef():
        listes = [CHEF_P1, CHEF_P2] if phases else [CHEF_P1, CHEF_P1]
        return Mon("Chef de meute (cro02)", 27, Kb, 11, 9, "chef", [0.5], listes,
                   res={"dorsal": 0.95}, faibl={"feu": 1.5, "foudre": 1.25}, cad="boss", cad_p2=1.25,
                   agonie=(2 if phases else 0), agonie_att=CHEF_P2, cr=4)

    def eclaireur(i):
        return Mon("Éclaireur %d (cro01)" % (i + 1), 6, Km, 7, 3, "escorte", [], [ECL], cad="escorte", cr=1)

    if scenario == "eclaireurs":
        return None, [eclaireur(i) for i in range(4)], 0
    if scenario == "chef_seul":
        return chef(), [], 0
    if scenario == "chef_meute":
        return chef(), [eclaireur(i) for i in range(4)], 0
    if scenario == "elite":
        listes = [GAR_P1, GAR_P2, GAR_P3] if phases else [GAR_P1] * 3
        b = Mon("Élite CR 12 (Garuvorn)", 58, Kb, 19, 19, "elite", [0.65, 0.30], listes,
                res={"tranchant": 0.75}, faibl={"glace": 1.5}, cad=1.5, cad_p2=1.0,
                agonie=(1 if phases else 0), agonie_att=GAR_AGONIE, cr=12)
        b.resist_feu = 0.5
        return b, [], 2
    if scenario == "legende":
        listes = [SOU_P12, SOU_P3] if phases else [SOU_P12, SOU_P12]
        b = Mon("Légendaire CR 18 (Garuvorn Sourd)", 79, Kb, 21, 25, "legende", [0.40], listes,
                res={"tranchant": 0.75, "contondant": 0.75}, cad=1.7, cad_p2=1.0, att_par_action=2,
                agonie=(3.5 if phases else 0), agonie_att=SOU_P3, regen=3.0, cr=18)
        b.resist_feu = 0.5
        return b, [], 4
    raise ValueError(scenario)


SCENARIOS = ["eclaireurs", "chef_seul", "chef_meute", "elite", "legende"]
NOM_SCEN = {"eclaireurs": "4 éclaireurs (cro01)", "chef_seul": "chef de meute seul (cro02)",
            "chef_meute": "chef + 4 éclaireurs (démo)", "elite": "élite CR 12", "legende": "légendaire CR 18"}


# =====================================================================================
# HÉROS
# =====================================================================================
class Hero:
    def __init__(self, nom, palier, P, o):
        c = evolue(HEROS[nom], palier)
        self.nom, self.c = nom, c
        self.vitmax = float(4 + c["END"])
        self.vit = self.vitmax
        self.endmax = 10.0
        self.end = 10.0
        self.mana = float(c["mana"])
        self.alive = True
        self.taunt = False
        self.mur = False
        self.garde = False
        self.stun = 0.0
        self.secoue = 0
        self.ebranle = 0
        self.fracture = 0
        self.dots = []
        self.riposte_ok = True
        pot = (o.get("potions") if o.get("potions") is not None else POTIONS_BASE[nom])
        self.piege = 0
        self.huile = 0
        self.huile_r = 22                                  # 90 s de durée (docs/mecaniques/01 §9.3)
        if nom == "Taranis" and o["bagage_taranis"] and o.get("potions") is None:
            pot = BAGAGE_TARANIS["potions"]
            self.piege, self.huile = BAGAGE_TARANIS["piege_colle"], BAGAGE_TARANIS["huile_feu"]
        self.potions = pot
        self.herbes = 3 if (nom == "Pascal" and o["pascal"] == "soutien") else 0
        self.bombes = 3 if (nom == "Pascal" and o["pascal"] == "bombe") else 0
        self.souffle_dispo = (nom == "Krunt3" and o["souffle"])
        self.souffle_rounds = 0
        # statistiques
        self.dmg = 0.0
        self.end_use = 0.0
        self.vit_perdue = 0.0
        self.coups = 0
        self.potions_utilisees = 0
        self.premier_tombe_round = None

    def p_esquive(self, base):
        p = base + ESQUIVE_PAR_AGI * (self.c["AGI"] - 8)
        return min(0.90, max(0.10, p))


# =====================================================================================
# COMBAT
# =====================================================================================
class Combat:
    def __init__(self, P, modele, noms, scenario, Kb, Km, o, rng, palier=None):
        self.P, self.m, self.rng, self.o = P, modele, rng, o
        boss, escortes, pal = construit(scenario, Kb, Km, o["phases"])
        pal = pal if palier is None else palier
        self.boss, self.escortes = boss, escortes
        self.heros = [Hero(n, pal, P, o) for n in noms]
        self.solo = len(noms) == 1
        self.round = 0
        self.tension = 0
        self.log_provoc_tenue = 0
        self.hits_par_nom = {h.nom: 0 for h in self.heros}
        # bagage de Taranis : piège à colle posé avant le combat
        for h in self.heros:
            if h.piege and self.boss is not None:
                dur = 0.75 if P["nom"] == "jeu" else 1.0
                if self.boss.cr >= 10:
                    dur /= 2.0                        # un boss de CR 10 ou plus divise les durées par 2 (§5.1)
                self.boss.immob = dur

    # -------- aides --------
    def vivants(self):
        return [h for h in self.heros if h.alive]

    def monstres(self):
        l = [m for m in self.escortes if m.vit > 0]
        if self.boss is not None and not self.boss.mort:
            l = [self.boss] + l
        return l

    def cadence(self, m):
        P = self.P
        if m.cad == "boss":
            c = P["cad_boss"]
        elif m.cad == "escorte":
            c = P["cad_escorte"]
        else:
            c = m.cad if P["nom"] == "jeu" else 1.0
        if P["nom"] == "jeu" and m.cad == "boss" and m.phase() == 1:
            c *= m.cad_p2
        return c

    def payer_end(self, h, x):
        x = min(x, h.end)
        h.end -= x
        h.end_use += x

    # -------- dégâts subis par un héros --------
    def subit(self, h, d_cases):
        if d_cases <= 0 or not h.alive:
            return
        h.coups += 1
        self.hits_par_nom[h.nom] += 1
        if self.m == "A":
            tampon = min(h.end, d_cases)
            h.end -= tampon
            h.end_use += tampon
            d_cases -= tampon
        h.vit -= d_cases
        h.vit_perdue += d_cases
        if h.vit <= 0:
            h.vit = 0
            h.alive = False
            h.premier_tombe_round = self.round

    def convertir(self, h, dmg_livre):
        """Dégâts du Livre -> cases de Vitalité du héros, selon l'échelle."""
        P = self.P
        d = dmg_livre
        if h.nom != "Krunt3":
            k = next((x for x in self.heros if x.nom == "Krunt3" and x.alive and x.mur), None)
            if k is not None and h.c["melee"]:
                d -= 2                                  # Mur de Chair : -2 aux alliés au contact (Livre VI)
        if h.garde:
            d -= 3                                      # Garde Haute : -3 aux dégâts reçus (Livre VI)
        d = max(0.0, d) * self.o["kd"]
        if P["armure_pct"]:
            d = d * P["f_recu"] * (1 - min(0.35, 0.05 * h.c["ca"]))
        else:
            d = d * P["f_recu"]
        return d

    def toucher_heros(self, h, m, a, hit_index=0, premiere=True):
        """Une attaque (un coup) de m contre h. Retourne les cases perdues (déjà appliquées)."""
        P, rng = self.P, self.rng
        if not h.alive:
            return
        # test de touche
        nd, df, flat = a["nd"], a["df"], a["flat"]
        crit = False
        if P["hit_monstre"] == "d20":
            defense = h.c["defense"] - (3 if h.fracture else 0) - a["pen_def"]
            if h.riposte_ok and h.end >= 1 and h.stun == 0:
                self.payer_end(h, 1)
                defense += h.c["AGI"]                  # Riposte : esquiver (+AGI à la Défense), 1 Endurance
                h.riposte_ok = False
            atk = (a["atk"] if a["atk"] is not None else m.atk) - a["pen_second"] * (1 if hit_index else 0)
            if h.ebranle:
                atk += 0
            roll = rng.randint(1, 20)
            if roll == 1 or (roll != 20 and roll + atk < defense):
                return
            crit = roll == 20
        else:
            # temps réel : toute attaque non évitée touche ; esquive minutée ou garde du bouclier
            if h.c["bouclier"]:
                if h.end > 0 and rng.random() < GARDE_P:
                    brut = (de(rng, nd, df) + flat)
                    d = self.convertir(h, brut)
                    bloque = d * GARDE_REDUC
                    self.payer_end(h, bloque * 4 * GARDE_COUT_PAR_PC)
                    self.subit(h, d - bloque)
                    if a["dot"] and rng.random() < a["dot"][2]:
                        self.ajoute_dot(h, a["dot"])
                    return
            elif h.end >= COUT_ESQUIVE:
                self.payer_end(h, COUT_ESQUIVE)
                p = h.p_esquive(self.o["esquive"])
                if h.secoue:
                    p *= 0.5
                if rng.random() < p:
                    return
        brut = de(rng, nd, df) * (2 if crit else 1) + flat
        if a["renv"] is not None:
            echec = True
            if a["renv"] != "auto" and P["nom"] == "livre":
                attr, dd = a["renv"]
                echec = rng.randint(1, 20) + h.c.get(attr, 8) < dd
            elif a["renv"] != "auto":
                echec = rng.random() < 0.5
            if echec:
                h.stun = max(h.stun, P["stun_frac"])
        d = self.convertir(h, brut)
        self.subit(h, d)
        if a["dot"] and h.alive and rng.random() < a["dot"][2]:
            self.ajoute_dot(h, a["dot"])
        if a["pen_def"] and a["nom"] == "Impact de crête" and h.alive:
            h.fracture = 99

    def ajoute_dot(self, h, dot):
        dmg, dur, _ = dot
        h.dots.append([dmg, dur])                          # saignée : 3 rounds ; venin : 2d6+3 ~ 10 rounds (Livre III)

    # -------- choix de cible des monstres --------
    def choisir_cible(self, m):
        vivants = self.vivants()
        if not vivants:
            return None
        krunt = next((h for h in vivants if h.nom == "Krunt3"), None)
        if krunt and krunt.taunt and self.rng.random() < P_PROVOC:
            return krunt
        poids = []
        for h in vivants:
            w = h.c["poids_cible"]
            if m.role in ("elite", "legende") and m.phase() >= 1:
                w *= h.c["AGI"] / 8.0                     # « cible la plus dangereuse et la plus mobile »
            poids.append(w)
        r = self.rng.random() * sum(poids)
        for h, w in zip(vivants, poids):
            r -= w
            if r <= 0:
                return h
        return vivants[-1]

    def interposition(self, cible):
        """Krunt3 prend le coup à la place d'un allié (réaction, 2 Endurance)."""
        if not self.o["tank"] or self.solo:
            return cible
        k = next((h for h in self.vivants() if h.nom == "Krunt3"), None)
        if k is None or k is cible or k.end < COUT_ESQUIVE + 0.0 or k.stun:
            return cible
        if self.rng.random() < P_INTERPO:
            self.payer_end(k, COUT_ESQUIVE)
            return k
        return cible

    # -------- action d'un monstre --------
    def liste_attaques(self, m):
        ph = m.phase()
        if m.agonie_restante is not None and m.agonie_att is not None:
            return m.agonie_att if m.role != "chef" else CHEF_P2
        return m.listes[min(ph, len(m.listes) - 1)]

    def agit(self, m):
        P, rng = self.P, self.rng
        if m.immob > 0:                                    # piège à colle : le monstre perd son action
            if m.immob >= 1:
                m.immob -= 1
                return
            saut = rng.random() < m.immob
            m.immob = 0.0
            if saut:
                return
        n_act = stoch(rng, self.cadence(m))
        for _ in range(n_act):
            if not self.vivants():
                return
            for _k in range(m.att_par_action):
                if not self.vivants():
                    return
                self.une_attaque(m)

    def une_attaque(self, m):
        rng = self.rng
        liste = self.liste_attaques(m)
        # pondération ; contraintes spéciales
        choix, poids = [], []
        scouts = [e for e in self.escortes if e.vit > 0]
        for a in liste:
            w = a["w"]
            if a["special"] == "vocal" and not scouts:
                w = 0
            if a["special"] == "coin" and len(scouts) < 3:
                w = 0
            if a["special"] == "cri" and m.cri_fait:
                w = 0
            if a["w"] <= 0 or w <= 0:
                continue
            choix.append(a)
            poids.append(w)
        if not choix:
            choix, poids = [liste[0]], [1.0]
        r = rng.random() * sum(poids)
        a = choix[-1]
        for x, w in zip(choix, poids):
            r -= w
            if r <= 0:
                a = x
                break
        cible = self.choisir_cible(m)
        if cible is None:
            return
        if a["special"] == "vocal":
            for e in scouts:
                self.toucher_heros(cible, e, ECL[0])
            return
        if a["special"] == "secoue":
            for h in self.vivants():
                h.secoue = 2
            return
        if a["special"] == "cri":
            m.cri_fait = True
            for h in self.vivants():
                h.ebranle = 2
            return
        cible = self.interposition(cible)
        cibles = [cible]
        if a["aoe"]:
            autres = [h for h in self.vivants() if h is not cible and h.c["melee"]]
            rng.shuffle(autres)
            cibles += autres[:a["aoe"] - 1]
        for c in cibles:
            for i in range(a["hits"]):
                self.toucher_heros(c, m, a, hit_index=i)
        if a["special"] == "coin":
            pass

    # -------- action d'un héros --------
    def facteur_arme_vs(self, h, m):
        """Résistances du monstre au type de dégâts de l'arme."""
        f = 1.0
        if "dorsal" in m.res:
            f *= m.res["dorsal"]
        if h.c["arme"] == "tranchant" and "tranchant" in m.res:
            f *= m.res["tranchant"]
        if "contondant" in m.res and h.c["arme"] == "tranchant":
            pass
        return f

    def cible_heros(self):
        ms = self.monstres()
        if not ms:
            return None
        if self.o["prio_escorte"]:
            es = [m for m in ms if m.role == "escorte"]
            if es:
                return min(es, key=lambda x: x.vit)
        return ms[0]

    def besoin_potion(self, h):
        if h.potions <= 0:
            return False
        if self.m == "A":
            return h.end <= 2.0 and (h.vit <= 0.7 * h.vitmax or h.end <= 1.0)
        return h.end <= 1.0

    def hero_agit(self, h):
        P, rng, o = self.P, self.rng, self.o
        jeu = P["nom"] == "jeu"
        ms = self.monstres()
        if not ms:
            return
        busy = 0.0
        techs = P["techs_round"]
        alliés = [x for x in self.vivants() if x is not h]
        flanc_utilisable = o["flanc_limite"]
        # états
        perdu = 0.0
        if h.stun:
            perdu = h.stun if jeu else 1.0
            h.stun = 0.0
        ebr = 1 if h.ebranle else 0
        if h.ebranle:
            h.ebranle -= 1
        if h.secoue:
            h.secoue -= 1
        # Souffle du Réceptacle (INVENTÉ)
        if h.souffle_dispo and (h.vit <= 0.5 * h.vitmax):
            h.souffle_dispo = False
            h.end = h.endmax
            h.souffle_rounds = 3
            self.tension += 1
        # potion
        if self.besoin_potion(h):
            h.potions -= 1
            h.potions_utilisees += 1
            h.end = min(h.endmax, h.end + 7.0)
            busy += P["busy_potion"]
        # techniques de Posture / métiers
        if h.nom == "Krunt3" and o["tank"] and not self.solo:
            h.taunt = False
            h.mur = False
            if techs >= 1 and h.end >= 2 + RESERVE_END:
                self.payer_end(h, 2)
                h.taunt = True
                techs -= 1
                busy += P["busy_tech"]
            if techs >= 1 and h.end >= 2 + RESERVE_END and any(x.c["melee"] for x in alliés):
                self.payer_end(h, 2)
                h.mur = True
                techs -= 1
                busy += P["busy_tech"]
        if h.nom == "Cyril":
            blesses = [x for x in self.vivants() if x.vit <= 0.6 * x.vitmax]
            malades = [x for x in self.vivants() if x.dots]
            if malades and h.end >= 2:
                self.payer_end(h, 2)                       # Présence Rassurante : retire un état, 2 Endurance
                for x in malades:
                    x.dots = []
                busy += P["busy_tech"]
            if blesses and h.mana >= 2 and busy < 0.9:
                cible = min(blesses, key=lambda x: x.vit / x.vitmax)
                h.mana -= 2
                cible.vit = min(cible.vitmax, cible.vit + 1.0)
                busy += P["busy_soin"]
        if h.nom == "Pascal":
            mode = o["pascal"]
            h.garde = False
            if mode == "soutien":
                if h.herbes > 0 and h.vit <= 0.5 * h.vitmax and busy < 0.9:
                    h.herbes -= 1
                    h.vit = min(h.vitmax, h.vit + 2.0)
                    busy += P["busy_soin"]
                elif h.vit <= 0.4 * h.vitmax and h.mana >= 2 and busy < 0.9:
                    h.mana -= 2
                    h.garde = True
                    busy += P["busy_tech"]
        # attaque
        frac = max(0.0, 1.0 - busy - (perdu if jeu else 0.0))
        if not jeu and (busy >= 1.0 or perdu):
            frac = 0.0
        touches = P["touches"] * (frac if jeu else 1.0)
        if jeu and h.end <= 0:
            touches *= 0.8                                 # Épuisé : coups à 80 % de vitesse
        n = stoch(rng, touches) if jeu else (1 if frac > 0 else 0)
        # coût du modèle B
        if self.m == "B" and n > 0:
            cout = P["b_cout_end"] * n
            if h.end >= cout:
                self.payer_end(h, cout)
            else:
                self.payer_end(h, h.end)
                h.vit -= P["perseverer"]
                h.vit_perdue += P["perseverer"]
                if h.vit <= 0:
                    h.vit = 0
                    h.alive = False
                    h.premier_tombe_round = self.round
                    return
        for _ in range(n):
            cible = self.cible_heros()
            if cible is None:
                break
            self.touche(h, cible, ebr)

    def touche(self, h, m, ebranle):
        P, rng, o = self.P, self.rng, self.o
        jeu = P["nom"] == "jeu"
        c = h.c
        nd, df = c["dice"]
        base = de(rng, nd, df)
        # bombe de Pascal (Livre X : rang 5 ; ici seulement en variante)
        elem = 0.0
        if h.bombes > 0 and m.role != "escorte":
            h.bombes -= 1
            base = de(rng, 2, 6)
            elem = 0.0
            if "feu" in m.faibl:
                base *= m.faibl["feu"]
            elif getattr(m, "resist_feu", None):
                base *= m.resist_feu
        elif h.huile and h.nom == "Taranis":
            e = 2.5
            if "feu" in m.faibl:
                e *= m.faibl["feu"]
            elif getattr(m, "resist_feu", None):
                e *= m.resist_feu
            elem = e
        # touche
        if not jeu:
            bonus = c["atk"] + (3 if m.expose else 0) + (3 if (o["ouverture"] and self.ouverture_active(h)) else 0) - (2 if ebranle else 0)
            roll = rng.randint(1, 20)
            if roll == 1 or (roll != 20 and roll + bonus < m.defense):
                return
            if roll == 20:
                base += de(rng, nd, df)
            dmg = (base + c["qual"] + elem) * self.facteur_arme_vs(h, m)
        else:
            durete = min(1.3, max(0.35, 1.0 + (10 - m.defense) * 0.04))
            mult = durete * (1.25 if m.expose else 1.0)
            if o["ouverture"] and self.ouverture_active(h):
                mult *= 1.25
            dmg = ((base + c["qual"] + c["dmg_attr"] // 4) * mult + elem * 1.0) * self.facteur_arme_vs(h, m)
        if h.souffle_rounds > 0:
            dmg += rng.randint(1, 6)
        # Flanc Coordonné (Loup) : +d6 si un allié a attaqué la même cible ce round
        if h.nom != "Krunt3" and h.end >= 2 + RESERVE_END and m.hit_par and (h.nom not in m.hit_par):
            if not (o["flanc_limite"] and getattr(m, "_flanc_pris", False)):
                self.payer_end(h, 2)
                dmg += rng.randint(1, 6)
                m._flanc_pris = True
        # Tir Ciblé (Taranis) : Exposé
        if h.nom == "Taranis" and h.mana >= 2 and not m.expose:
            h.mana -= 2
            m.expose = 1
        # application
        reel = min(dmg, max(0.0, m.vit)) if not m.mort else 0.0
        if m.agonie_restante is not None or m.mort:
            reel = 0.0
        m.vit -= dmg if m.agonie_restante is None else 0.0
        h.dmg += reel
        m.hit_par.add(h.nom)
        if c["mana"] and h.c["mode"] == "flux":
            h.mana = min(c["mana"], h.mana + 1)
        # mort / agonie
        if m.vit <= 0 and m.agonie_restante is None and not m.mort:
            if m.role in ("escorte",):
                m.mort = True
            elif m.agonie:
                m.agonie_restante = float(stoch(rng, m.agonie)) if m.role != "legende" else float(rng.randint(1, 6))
                if m.role == "elite":
                    m.agonie_restante = 1.0
                m.vit = 0.0
            else:
                m.mort = True

    def ouverture_active(self, h):
        k = next((x for x in self.heros if x.nom == "Krunt3" and x.alive and x.taunt), None)
        return k is not None and h.nom != "Krunt3"

    # -------- boucle --------
    def termine(self):
        if not self.vivants():
            return "defaite"
        if self.boss is not None:
            if self.boss.mort:
                return "victoire"
        else:
            morts = sum(1 for e in self.escortes if e.vit <= 0)
            if morts >= (len(self.escortes) + 1) // 2:   # la meute fuit quand la moitié est hors combat (Livre III)
                return "victoire"
        return None

    def run(self):
        P, rng, o = self.P, self.rng, self.o
        res = None
        while self.round < ROUNDS_MAX:
            self.round += 1
            for h in self.vivants():
                h.riposte_ok = True
                h.end = min(h.endmax, h.end + P["regen_end"])
                if h.huile:
                    h.huile_r -= 1
                    if h.huile_r <= 0:
                        h.huile = 0
                if h.c["mode"] == "ancrage":
                    h.mana = min(h.c["mana"], h.mana + 1)
                if h.souffle_rounds:
                    h.souffle_rounds -= 1
                # DoT
                if h.dots:
                    tot = sum(d[0] for d in h.dots)
                    d_cases = tot * (P["f_recu"] if P["nom"] == "jeu" else 1.0) * o["kd"]
                    self.subit(h, d_cases)
                    h.coups -= 1
                    self.hits_par_nom[h.nom] -= 1
                    for d in h.dots:
                        d[1] -= 1
                    h.dots = [d for d in h.dots if d[1] > 0]
                    if h.nom != "Cyril" and rng.random() < 0.0:
                        pass
                # terrain
                t = o["terrain"]
                if t and h.alive:
                    if rng.random() < t.get("feu_p", 0):
                        self.subit(h, de(rng, 1, 6) * (P["f_recu"] if P["nom"] == "jeu" else 1.0))
                        h.coups -= 1
                        self.hits_par_nom[h.nom] -= 1
                    if rng.random() < t.get("instable_p", 0):
                        h.stun = max(h.stun, 0.5 if P["nom"] == "jeu" else 1.0)
            for m in self.monstres():
                m.hit_par = set()
                m._flanc_pris = False
                if m.regen and m.agonie_restante is None and m.vit > 0 and m.vit < m.vitmax:
                    m.vit = min(m.vitmax, m.vit + m.regen)
            # déclencheur de phase 2 du chef
            if self.boss is not None and self.boss.role == "chef" and not self.boss.declenche:
                morts = sum(1 for e in self.escortes if e.vit <= 0)
                if morts >= 3 or not self.escortes or rng.random() < 0.12:
                    self.boss.declenche = True
            for h in sorted(self.vivants(), key=lambda x: -x.c["init"]):
                if h.alive:
                    self.hero_agit(h)
                res = self.termine()
                if res:
                    break
            if res == "defaite" or (res == "victoire" and not self.agonie_en_cours()):
                break
            res = None
            # monstres
            for m in self.monstres():
                if m.role == "escorte" and self.boss is not None and self.boss.agonie_restante is not None:
                    continue
                self.agit(m)
            for m in self.monstres():
                if m.expose:
                    m.expose -= 1
            if self.boss is not None and self.boss.agonie_restante is not None and not self.boss.mort:
                self.boss.agonie_restante -= 1
                if self.boss.agonie_restante <= 0:
                    self.boss.mort = True
            res = self.termine()
            if res:
                break
        if res is None:
            res = "abandon"
        return res

    def agonie_en_cours(self):
        return self.boss is not None and self.boss.agonie_restante is not None and not self.boss.mort


# =====================================================================================
# ENSEMBLES DE TIRAGES ET STATISTIQUES
# =====================================================================================
def une_cellule(etiquette, preset, modele, noms, scenario, Kb, Km, n, opts=None, palier=None, base_seed=None):
    o = dict(OPTS_DEFAUT)
    if opts:
        o.update(opts)
    P = PRESETS[preset]
    rng = random.Random(seed_de(etiquette, base_seed))
    out = dict(n=n, vic=0, defaite=0, abandon=0, rounds_v=[], rounds_all=[], tombe_un=0, tombe_k=0, tombe_autre=0,
               vit={h: [] for h in noms}, end={h: [] for h in noms}, dmg={h: 0.0 for h in noms},
               coups={h: 0 for h in noms}, pots=0, vit_v=[], tension=0)
    for _ in range(n):
        c = Combat(P, modele, noms, scenario, Kb, Km, o, rng, palier)
        r = c.run()
        out["rounds_all"].append(c.round)
        if r == "victoire":
            out["vic"] += 1
            out["rounds_v"].append(c.round)
        elif r == "defaite":
            out["defaite"] += 1
        else:
            out["abandon"] += 1
        tot_dmg = sum(h.dmg for h in c.heros) or 1.0
        un = False
        vit_tot = 0.0
        for h in c.heros:
            out["vit"][h.nom].append(min(h.vit_perdue, h.vitmax))
            out["end"][h.nom].append(h.end_use)
            out["dmg"][h.nom] += h.dmg / tot_dmg
            out["coups"][h.nom] += c.hits_par_nom[h.nom]
            out["pots"] += h.potions_utilisees
            if not h.alive:
                un = True
                if h.nom == "Krunt3":
                    out["tombe_k"] += 1
                else:
                    out["tombe_autre"] += 1
            vit_tot += min(h.vit_perdue, h.vitmax)
        if un:
            out["tombe_un"] += 1
        if r == "victoire":
            out["vit_v"].append(vit_tot / len(c.heros))
        out["tension"] += c.tension
    return out


def pct(x, n):
    return "%.0f %%" % (100.0 * x / n)


def mediane(l):
    return statistics.median(l) if l else float("nan")


def fmt_s(rounds):
    if rounds != rounds:
        return "n/a"
    s = rounds * DUREE_ROUND_S
    if s >= 120:
        return "%d min %02d s" % (int(s // 60), int(s % 60))
    return "%d s" % round(s)


def table(entetes, lignes):
    out = ["| " + " | ".join(entetes) + " |", "|" + "|".join(["---"] * len(entetes)) + "|"]
    for l in lignes:
        out.append("| " + " | ".join(str(x) for x in l) + " |")
    return "\n".join(out)


def moy(l):
    return sum(l) / len(l) if l else 0.0


def moy_ou_na(l):
    return "%.1f" % moy(l) if l else "n/a"


# =====================================================================================
# EXPÉRIENCES
# =====================================================================================
TOUS = ["Krunt3", "Taranis", "Cyril", "Pascal"]
DUO = ["Krunt3", "Cyril"]


def config_nom(noms):
    return {1: "solo ", 2: "duo ", 4: "table "}.get(len(noms), "") + "+".join(noms) if len(noms) < 4 else "table (4)"


def section_echelle():
    print("### E0. Le problème d'échelle en chiffres (calcul direct, sans tirage)\n")
    lignes = []
    for nom in TOUS:
        c = evolue(HEROS[nom], 0)
        nd, df = c["dice"]
        de_moy = moy_de(nd, df)
        att_livre = de_moy
        att_jeu = de_moy + c["dmg_attr"] // 4
        lignes.append([nom, "%dd%d (%.1f)" % (nd, df, de_moy), "%.1f" % att_jeu, "%.1f" % (att_jeu * 2.4)])
    print(table(["Héros", "Arme (dé moyen, Livre IX)", "Dégâts par touche (formule §4.3)", "Dégâts par round de 4 s (2,4 touches)"], lignes))
    print()
    print("Combien de touches pour abattre la créature, aux chiffres bruts du Livre III (K = 1) ?\n")
    lignes = []
    for sc in ["eclaireurs", "chef_seul", "elite", "legende"]:
        b, esc, _ = construit(sc, 1, 1)
        m = b if b is not None else esc[0]
        v = m.vitmax
        dureté = min(1.3, max(0.35, 1.0 + (10 - m.defense) * 0.04))
        ligne = [NOM_SCEN[sc].replace("4 éclaireurs", "un éclaireur"), "%d" % v, m.defense, "%.2f" % dureté]
        for nom in ["Krunt3", "Taranis", "Cyril", "Pascal"]:
            c = evolue(HEROS[nom], 0 if sc in ("eclaireurs", "chef_seul") else 2)
            nd, df = c["dice"]
            dmg_t = (moy_de(nd, df) + c["qual"] + c["dmg_attr"] // 4) * dureté
            ligne.append("%.0f" % math.ceil(v / dmg_t))
        lignes.append(ligne)
    print(table(["Cible", "Vitalité du livre", "Défense", "Dureté", "Touches Krunt3", "Touches Taranis", "Touches Cyril", "Touches Pascal"], lignes))
    print()
    print("(Héros au palier 0 pour les éclaireurs et le chef ; palier 2 pour l'élite ; au palier 2 aussi pour le légendaire dans ce calcul seulement.)\n")


def ligne_standard(r, noms, scen_nom, extra=None):
    n = r["n"]
    return [scen_nom, pct(r["vic"], n), pct(r["defaite"], n), pct(r["tombe_un"], n),
            fmt_s(mediane(r["rounds_all"])),
            " / ".join("%.1f" % moy(r["vit"][h]) for h in noms),
            " / ".join("%.1f" % moy(r["end"][h]) for h in noms)] + (extra or [])


def section_livre(n):
    print("### E1. Échelle « Livre » (tour par tour, d20 contre Défense, K = 1) : les trois modèles\n")
    print("Colonnes : victoire / défaite (tous les héros à 0) / au moins un héros à 0 / durée médiane / Vitalité perdue (cases) / Endurance dépensée, par héros dans l'ordre listé.\n")
    for (titre, noms) in [("Un héros seul", None), ("Deux héros (Krunt3 + Cyril)", DUO), ("La table (quatre héros)", TOUS)]:
        print("**%s**\n" % titre)
        lignes = []
        configs = [[h] for h in TOUS] if noms is None else [noms]
        for cfg in configs:
            for sc in ["chef_meute", "elite", "legende"]:
                for mod in "ABC":
                    r = une_cellule("livre|%s|%s|%s" % (mod, "+".join(cfg), sc), "livre", mod, cfg, sc, 1, 1, n)
                    lignes.append([("+".join(cfg) if len(cfg) < 4 else "4 héros"), mod] + ligne_standard(r, cfg, NOM_SCEN[sc]))
        print(table(["Héros", "Modèle", "Scénario", "Victoire", "Défaite", "≥ 1 à terre", "Durée méd.", "Vit. perdue", "End. dépensée"], lignes))
        print()


def section_jeu(n):
    print("### E2. Échelle « jeu » (temps réel tactile), K = 1 : la démo sans correction\n")
    lignes = []
    for cfg in [["Krunt3"], ["Taranis"], ["Cyril"], ["Pascal"], DUO, TOUS]:
        for sc in ["chef_seul", "chef_meute"]:
            r = une_cellule("jeu1|C|%s|%s" % ("+".join(cfg), sc), "jeu", "C", cfg, sc, 1, 1, n)
            lignes.append([("+".join(cfg) if len(cfg) < 4 else "4 héros"), NOM_SCEN[sc], pct(r["vic"], n), fmt_s(mediane(r["rounds_v"] or r["rounds_all"])),
                           "%.1f" % moy(r["vit_v"]) if r["vit_v"] else "n/a"])
    print(table(["Héros", "Scénario", "Victoire", "Durée médiane", "Vit. perdue / héros (victoires)"], lignes))
    print()


def section_K(n):
    print("### E3. Coefficient K sur la Vitalité du chef de meute (échelle jeu, modèle C, héros seul, chef + éclaireurs)\n")
    print("K_meute = max(1, K_boss / 5) (le document 01 donne K = 20 et K = 4). Le tableau donne : victoire / durée médiane des victoires / Vitalité perdue (cases) par victoire / Potions de Soin utilisées par combat.\n")
    Ks = [1, 2, 4, 6, 8, 10, 15, 20, 30]
    for mod in "CAB":
        print("**Modèle %s**\n" % mod)
        lignes = []
        for K in Ks:
            ligne = [K]
            for h in TOUS:
                r = une_cellule("K|%s|%s|%d" % (mod, h, K), "jeu", mod, [h], "chef_meute", K, max(1, K // 5), n)
                ligne.append("%s / %s / %s" % (pct(r["vic"], n), fmt_s(mediane(r["rounds_v"])), moy_ou_na(r["vit_v"])))
            lignes.append(ligne)
        print(table(["K"] + TOUS, lignes))
        print()
    print("**Table (quatre héros), modèle C, chef + éclaireurs**\n")
    lignes = []
    for K in [1, 5, 10, 20, 40, 60, 80, 100]:
        r = une_cellule("Kt|C|%d" % K, "jeu", "C", TOUS, "chef_meute", K, max(1, K // 5), n)
        lignes.append([K, pct(r["vic"], n), fmt_s(mediane(r["rounds_v"])), pct(r["tombe_un"], n), moy_ou_na(r["vit_v"])])
    print(table(["K", "Victoire", "Durée médiane", "≥ 1 à terre", "Vit. perdue / héros"], lignes))
    print()


def section_tank(n):
    print("### E4. Le rôle de tank de Krunt3 (échelle jeu et échelle livre, quatre héros)\n")
    print("Colonnes : part des coups subis par Krunt3 / Krunt3 à terre / un autre héros à terre / victoire / Vitalité perdue Krunt3 vs moyenne des trois autres. « sans tank » : Krunt3 attaque seulement.\n")
    lignes = []
    for preset, K, scen in [("livre", 1, "chef_meute"), ("jeu", 10, "chef_meute"), ("livre", 1, "elite"), ("jeu", 10, "elite")]:
        for mod in "ABC":
            for tank in (True, False):
                r = une_cellule("tank|%s|%s|%s|%s" % (preset, mod, scen, tank), preset, mod, TOUS, scen, K, max(1, K // 5), n, opts=dict(tank=tank))
                coups = sum(r["coups"].values()) or 1
                autres = [moy(r["vit"][h]) for h in TOUS if h != "Krunt3"]
                lignes.append([preset, NOM_SCEN[scen], "K=%d" % K, mod, "oui" if tank else "non",
                               pct(r["coups"]["Krunt3"], coups), pct(r["tombe_k"], n),
                               pct(r["tombe_autre"], n * 3), pct(r["vic"], n),
                               "%.1f vs %.1f" % (moy(r["vit"]["Krunt3"]), moy(autres))])
    print(table(["Échelle", "Scénario", "K", "Modèle", "Tank joué", "Part des coups", "Krunt3 à terre", "Autre à terre (par héros)", "Victoire", "Vit. perdue K3 vs autres"], lignes))
    print()
    print("**Krunt3 seul en première ligne dans un duo (Krunt3 + Cyril), échelle jeu, K = 5, chef + éclaireurs**\n")
    lignes = []
    for mod in "ABC":
        r = une_cellule("duo|%s" % mod, "jeu", mod, DUO, "chef_meute", 5, 1, n)
        lignes.append([mod, pct(r["vic"], n), fmt_s(mediane(r["rounds_v"])), pct(r["tombe_k"], n), pct(r["tombe_autre"], n),
                       moy_ou_na(r["vit"]["Krunt3"]), moy_ou_na(r["vit"]["Cyril"])])
    print(table(["Modèle", "Victoire", "Durée", "Krunt3 à terre", "Cyril à terre", "Vit. perdue Krunt3", "Vit. perdue Cyril"], lignes))
    print()


def section_leviers(n):
    print("### E5. Les leviers de réglage, un par un (échelle jeu, modèle C, Krunt3 seul, démo)\n")
    lignes = []
    cas = [
        ("L0 chef seul, K = 1", "chef_seul", 1, 1, {}),
        ("L1 chef seul, K = 8", "chef_seul", 8, 1, {}),
        ("L2 chef + éclaireurs, K = 8, K_meute = 2", "chef_meute", 8, 2, {}),
        ("L3 L2 sans phases ni agonie (une seule phase)", "chef_meute", 8, 2, dict(phases=False)),
        ("L4 L2 + terrain (feu 25 %/round, sol instable 20 %/round)", "chef_meute", 8, 2, dict(terrain=dict(feu_p=0.25, instable_p=0.20))),
        ("L5 K = 12 chef seul (K seul, sans meute)", "chef_seul", 12, 1, {}),
        ("L6 K = 12 + éclaireurs K_meute = 2 + terrain", "chef_meute", 12, 2, dict(terrain=dict(feu_p=0.25, instable_p=0.20))),
    ]
    for (nom, sc, K, Km, o) in cas:
        r = une_cellule("lev|%s" % nom, "jeu", "C", ["Krunt3"], sc, K, Km, n, opts=o)
        lignes.append([nom, pct(r["vic"], n), fmt_s(mediane(r["rounds_v"])), moy_ou_na(r["vit_v"]), "%.1f" % (r["pots"] / n)])
    print(table(["Configuration", "Victoire", "Durée médiane", "Vit. perdue (victoires)", "Potions / combat"], lignes))
    print()


def section_variantes(n):
    print("### E6. Variantes de fiches (échelle jeu, modèle C, K = 5 : chef + éclaireurs)\n")
    print("Part des dégâts infligés à la table (quatre héros) et durée solo, avec et sans le bagage de Taranis ; trois versions de Pascal.\n")
    lignes = []
    for nom, o in [("référence (bagage Taranis ; Pascal « base »)", {}),
                   ("sans bagage de Taranis", dict(bagage_taranis=False)),
                   ("Pascal « soutien » (Garde Haute, Herbes)", dict(pascal="soutien")),
                   ("Pascal « bombe » (3 bombes de feu, niveau 5)", dict(pascal="bombe")),
                   ("Flanc Coordonné cumulable", dict(flanc_limite=False)),
                   ("Krunt3 avec Souffle du Réceptacle", dict(souffle=True))]:
        r = une_cellule("var|%s" % nom, "jeu", "C", TOUS, "chef_meute", 5, 1, n, opts=o)
        parts = " / ".join("%.0f %%" % (100 * r["dmg"][h] / n) for h in TOUS)
        r2 = une_cellule("var1|%s" % nom, "jeu", "C", ["Taranis"], "chef_meute", 5, 1, n, opts=o)
        r3 = une_cellule("var1p|%s" % nom, "jeu", "C", ["Pascal"], "chef_meute", 5, 1, n, opts=o)
        lignes.append([nom, parts, fmt_s(mediane(r["rounds_v"])), pct(r["tombe_un"], n), pct(r2["vic"], n), pct(r3["vic"], n)])
    print(table(["Variante", "Part des dégâts K3 / Tar / Cyr / Pas", "Durée table", "≥ 1 à terre", "Taranis seul : victoire", "Pascal seul : victoire"], lignes))
    print()
    print("**Parts de dégâts de référence, échelle livre (K = 1) et jeu (K = 5), quatre héros, par scénario**\n")
    lignes = []
    for preset, K in [("livre", 1), ("jeu", 5)]:
        for sc in ["chef_meute", "elite", "legende"]:
            r = une_cellule("parts|%s|%s" % (preset, sc), preset, "C", TOUS, sc, K, max(1, K // 5), n)
            lignes.append([preset, NOM_SCEN[sc], " / ".join("%.0f %%" % (100 * r["dmg"][h] / n) for h in TOUS)])
    print(table(["Échelle", "Scénario", "Part des dégâts K3 / Tar / Cyr / Pas"], lignes))
    print()


def section_competence(n):
    print("### E7. Sensibilité à l'habileté du joueur (échelle jeu, modèle C, héros seul, chef + éclaireurs)\n")
    lignes = []
    for K in [4, 6, 8, 10]:
        ligne = [K]
        for esq in (0.40, 0.55, 0.70):
            r = une_cellule("sk|%d|%.2f" % (K, esq), "jeu", "C", ["Krunt3"], "chef_meute", K, max(1, K // 5), n, opts=dict(esquive=esq))
            ligne.append("%s / %s" % (pct(r["vic"], n), fmt_s(mediane(r["rounds_v"]))))
        lignes.append(ligne)
    print(table(["K (Krunt3)", "Novice (esquive 40 %)", "Moyen (55 %)", "Bon (70 %)"], lignes))
    print()
    print("**Élite et légendaire, échelle jeu, héros évolués (palier 2 et 4), quatre héros, modèle C, selon K et facteur de dégâts reçus**\n")
    lignes = []
    for sc, K in [("elite", 5), ("elite", 10), ("elite", 20), ("legende", 5), ("legende", 10), ("legende", 20), ("legende", 40)]:
        r = une_cellule("el|%s|%d" % (sc, K), "jeu", "C", TOUS, sc, K, 1, n)
        lignes.append([NOM_SCEN[sc], K, pct(r["vic"], n), fmt_s(mediane(r["rounds_v"])), pct(r["tombe_un"], n), moy_ou_na(r["vit_v"])])
    print(table(["Scénario", "K", "Victoire", "Durée médiane", "≥ 1 à terre", "Vit. perdue / héros"], lignes))
    print()
    print("**Même chose, héros seul (Krunt3), échelle jeu**\n")
    lignes = []
    for sc, K in [("elite", 2), ("elite", 4), ("elite", 8), ("legende", 2), ("legende", 4), ("legende", 8)]:
        r = une_cellule("el1|%s|%d" % (sc, K), "jeu", "C", ["Krunt3"], sc, K, 1, n)
        lignes.append([NOM_SCEN[sc], K, pct(r["vic"], n), fmt_s(mediane(r["rounds_v"])), moy_ou_na(r["vit_v"])])
    print(table(["Scénario", "K", "Victoire", "Durée médiane", "Vit. perdue"], lignes))
    print()


SECTIONS = {"echelle": lambda n: section_echelle(), "livre": section_livre, "jeu": section_jeu, "K": section_K,
            "tank": section_tank, "leviers": section_leviers, "variantes": section_variantes, "competence": section_competence}


def main():
    global SEED
    ap = argparse.ArgumentParser(description="Essais d'équilibrage du combat du Jeu B (CRS)")
    ap.add_argument("--n", type=int, default=N_DEFAUT, help="tirages par cellule (défaut %d)" % N_DEFAUT)
    ap.add_argument("--seed", type=int, default=SEED)
    ap.add_argument("--sections", default="echelle,livre,jeu,K,tank,leviers,variantes,competence")
    a = ap.parse_args()
    SEED = a.seed
    print("<!-- simu_combat.py : graine %d, %d tirages par cellule, 1 round = %d s -->\n" % (SEED, a.n, DUREE_ROUND_S))
    for s in a.sections.split(","):
        SECTIONS[s.strip()](a.n)
        sys.stdout.flush()


if __name__ == "__main__":
    main()
