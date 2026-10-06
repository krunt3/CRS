#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
simu_combat.py : essais d'équilibrage du combat du Jeu B (CRS), par simulation Monte-Carlo.

Python 3.8+, bibliothèque standard seulement. Reproductible : tous les tirages dérivent de
SEED (une graine par cellule de résultat, obtenue par CRC32 de l'étiquette de la cellule).

Usage
    python3 outils/simu_combat.py                      # rapport complet (Markdown) sur la sortie standard
    python3 outils/simu_combat.py --sections echelle,K # seulement certaines sections
    python3 outils/simu_combat.py --n 500 --seed 7     # moins de tirages, autre graine
    sections : echelle, livre, jeu, K, tank, leviers, variantes, competence, equiv, modeles

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
        regen_end=5.0,           # 2 /s après 0,8 s sans dépense (§3.2) : environ 5 par round de 4 s si l'on dépense toutes les 2,5 s (dérivé)
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
    tank=True,                  # Krunt3 : True = Provocation + Mur de Chair + Interposition ; "provoc" = Provocation seule ; False = aucun
    krunt_kit="base",           # "base" (cuir, Double Lame) ; "plaques" (CA 4) ; "bouclier" (Épée et Bouclier, maille : kit de Pascal) ; INVENTÉ
    flanc_limite=True,          # Flanc Coordonné : au plus un bonus par cible et par round (docs/trame/04 §7.3)
    bagage_taranis=True,        # correction de krunt : Taranis part avec un bagage (contenu INVENTÉ ci-dessous)
    pascal="base",              # "base" = attaque de base seule (correction de krunt) ; "soutien" ; "bombe"
    souffle=False,              # Souffle du Réceptacle de Krunt3 (docs/trame/04 §5.4, INVENTÉ)
    ouverture=True,             # Provocation : « les alliés bénéficient d'une Ouverture gratuite » (Livre VI)
    esquive=ESQUIVE_BASE,       # compétence du joueur (esquive_base)
    soin_mana=2,                # coût en Mana du soin de Vitalité de Cyril (Livre VII : soins mineurs ; INVENTÉ : 2)
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
                agonie=(3.5 if phases else 0), agonie_att=SOU_P3, regen=0.0, cr=18)
        b.regen_frac = 0.01 if phases else 0.0           # Régénération de rage (phase 3) : 3 Vitalité du livre par round = ~4 % ; ramenée à 1 % (INVENTÉ)
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
        if nom == "Krunt3" and o.get("krunt_kit") == "plaques":
            c["ca"] += 2
            c["defense"] += 2
        elif nom == "Krunt3" and o.get("krunt_kit") == "bouclier":
            c.update(bouclier=True, dice=(1, 8), ca=c["ca"] + 3, defense=c["defense"] + 3)
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
        self.end_fatal = None
        self.rounds_end_bas = 0

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
        reel = min(d_cases, h.vit)
        pre_end = h.end + (tampon if self.m == "A" else 0.0)
        h.vit -= d_cases
        h.vit_perdue += reel
        if h.vit <= 0:
            h.vit = 0
            h.alive = False
            h.premier_tombe_round = self.round
            h.end_fatal = pre_end

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
        if self.o["tank"] is not True or self.solo:
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
            if o["tank"] is True and techs >= 1 and h.end >= 2 + RESERVE_END and any(x.c["melee"] for x in alliés):
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
            if blesses and h.mana >= o["soin_mana"] and busy < 0.9:
                cible = min(blesses, key=lambda x: x.vit / x.vitmax)
                h.mana -= o["soin_mana"]
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
                if h.end < COUT_ESQUIVE:
                    h.rounds_end_bas += 1
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
                        self.subit(h, de(rng, 1, 6) * (P["f_recu"] if P["nom"] == "jeu" else 1.0) * o["kd"])
                        h.coups -= 1
                        self.hits_par_nom[h.nom] -= 1
                    if rng.random() < t.get("instable_p", 0):
                        h.stun = max(h.stun, 0.5 if P["nom"] == "jeu" else 1.0)
            for m in self.monstres():
                m.hit_par = set()
                m._flanc_pris = False
                rf = getattr(m, "regen_frac", 0.0)
                if rf and m.phase() >= 1 and m.agonie_restante is None and m.vit > 0:
                    m.vit = min(m.vitmax, m.vit + rf * m.vitmax)
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
    P = dict(PRESETS[preset])
    for k in ("cad_boss", "cad_escorte", "touches", "regen_end", "f_recu", "b_cout_end"):
        if k in o:
            P[k] = o[k]                                    # surcharge d'un paramètre d'échelle pour une expérience
    rng = random.Random(seed_de(etiquette, base_seed))
    out = dict(spir=0, mort_solo=0, end_bas=0.0, n=n, vic=0, defaite=0, abandon=0, rounds_v=[], rounds_all=[], tombe_un=0, tombe_k=0, tombe_autre=0,
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
            out["vit"][h.nom].append(h.vit_perdue)
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
            vit_tot += h.vit_perdue
        for h in c.heros:
            out["end_bas"] += h.rounds_end_bas / max(1, c.round) / len(c.heros)
            if not h.alive and h.end_fatal is not None:
                out["mort_solo"] += 1
                if h.end_fatal < COUT_ESQUIVE:
                    out["spir"] += 1
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

# Réglage recommandé pour le prototype (résultat des essais E3 à E7 ; voir le document 07)
RECO = dict(K=20, K_meute=4, kd=0.15, cad_boss=1.2, cad_escorte=0.4)
# Population de joueurs à la première tentative (esquive moyenne, poids) : INVENTÉ, pour simuler 35 à 50 % de victoires
POP = [(0.35, 0.15), (0.45, 0.30), (0.55, 0.30), (0.65, 0.20), (0.75, 0.05)]
DECALAGE_JETONS = 0.07          # INVENTÉ : trois Jetons de Connaissance élargissent la fenêtre d'esquive (docs/mecaniques/01 §3.2)


def opts_reco(**kw):
    o = dict(kd=RECO["kd"], cad_boss=RECO["cad_boss"], cad_escorte=RECO["cad_escorte"])
    o.update(kw)
    return o


def population(etiquette, noms, scenario, K, Km, n, opts, modele="C", decalage=0.0, palier=None):
    """Victoire pondérée sur la population de joueurs POP ; durée médiane des victoires ; cases perdues par minute."""
    n_e = max(100, n // 3)
    w, durees, vit_v, perdu_min = 0.0, [], [], []
    for esq, p in POP:
        o = dict(opts)
        o["esquive"] = min(0.95, esq + decalage)
        r = une_cellule("%s|e%.2f|d%.2f" % (etiquette, esq, decalage), "jeu", modele, noms, scenario, K, Km, n_e, opts=o, palier=palier)
        w += p * r["vic"] / n_e
        durees += r["rounds_v"]
        vit_v += r["vit_v"]
        tot_vit = sum(sum(r["vit"][h]) for h in noms) / n_e
        tot_t = sum(r["rounds_all"]) / n_e * DUREE_ROUND_S / 60.0
        perdu_min.append(p * tot_vit / max(tot_t, 1e-9) / len(noms))
    return dict(win=w, dur=mediane(durees), vit_v=moy(vit_v), par_min=sum(perdu_min))


def calibre(modele, noms, scenario, K, Km, cible, n, opts, palier=None, par_population=False, etiquette="cal"):
    """Cherche par dichotomie (échelle log) le kd qui donne la victoire visée. Retourne kd."""
    lo, hi = math.log(0.003), math.log(1.5)
    for it in range(9):
        mid = (lo + hi) / 2
        kd = math.exp(mid)
        o = dict(opts)
        o["kd"] = kd
        if par_population:
            v = population("%s|%d" % (etiquette, it), noms, scenario, K, Km, n, o, modele=modele, palier=palier)["win"]
        else:
            r = une_cellule("%s|%d" % (etiquette, it), "jeu", modele, noms, scenario, K, Km, n, opts=o, palier=palier)
            v = r["vic"] / n
        if v > cible:
            lo = mid                                       # trop facile : on peut monter les dégâts
        else:
            hi = mid
    return math.exp((lo + hi) / 2)


def config_nom(noms):
    return "+".join(noms) if len(noms) < 4 else "4 héros"


def section_echelle(n=0):
    print("### E0. Le problème d'échelle en chiffres (calcul direct, sans tirage)\n")
    lignes = []
    for nom in TOUS:
        c = evolue(HEROS[nom], 0)
        nd, df = c["dice"]
        de_moy = moy_de(nd, df)
        att_jeu = de_moy + c["dmg_attr"] // 4
        lignes.append([nom, "%dd%d (%.1f)" % (nd, df, de_moy), "%.1f" % att_jeu, "%.1f" % (att_jeu * 2.4), "%.1f" % (att_jeu * 2.4 / DUREE_ROUND_S),
                       "%d cases = %d PC" % (4 + c["END"], 4 * (4 + c["END"]))])
    print(table(["Héros", "Arme (dé moyen, Livre IX)", "Dégâts par touche (formule §4.3)", "Par round de 4 s (2,4 touches)", "Par seconde", "Vitalité"], lignes))
    print()
    print("Touches nécessaires pour abattre la créature aux chiffres bruts du Livre III (K = 1), dureté de zone incluse ; héros au palier 0 (éclaireur, chef) ou 2 (élite, légendaire).\n")
    lignes = []
    for sc in ["eclaireurs", "chef_seul", "elite", "legende"]:
        b, esc, pal = construit(sc, 1, 1)
        m = b if b is not None else esc[0]
        v = m.vitmax
        durete = min(1.3, max(0.35, 1.0 + (10 - m.defense) * 0.04))
        ligne = [NOM_SCEN[sc].replace("4 éclaireurs", "un éclaireur"), "%d" % v, m.defense, "%.2f" % durete]
        for nom in TOUS:
            c = evolue(HEROS[nom], 2 if sc in ("elite", "legende") else 0)
            nd, df = c["dice"]
            dmg_t = (moy_de(nd, df) + c["qual"] + c["dmg_attr"] // 4) * durete
            ligne.append("%d" % math.ceil(v / dmg_t))
        lignes.append(ligne)
    print(table(["Cible", "Vitalité du livre", "Défense", "Dureté", "Krunt3", "Taranis", "Cyril", "Pascal"], lignes))
    print()
    print("Temps pour abattre le chef de meute seul (27 Vitalité) à 2,4 touches par round : table de quatre héros = %.1f s ; héros seul = %.1f à %.1f s."
          % (27 / (sum((moy_de(*HEROS[h]["dice"]) + HEROS[h]["dmg_attr"] // 4) * 0.96 for h in TOUS) * 2.4 / DUREE_ROUND_S),
             27 / ((moy_de(*HEROS["Krunt3"]["dice"]) + HEROS["Krunt3"]["dmg_attr"] // 4) * 0.96 * 2.4 / DUREE_ROUND_S),
             27 / ((moy_de(*HEROS["Pascal"]["dice"]) + HEROS["Pascal"]["dmg_attr"] // 4) * 0.96 * 2.4 / DUREE_ROUND_S)))
    print()
    print("Vitalité effective à viser pour une durée cible T : PV_chasse = T x DPS_héros x rendement (rendement mesuré ~ 0,8). Exemple pour T = 150 s :\n")
    lignes = []
    for sc, cible_nom in [("chef_seul", "chef (27, Déf. 11)"), ("elite", "élite (58, Déf. 19)"), ("legende", "légendaire (79, Déf. 21)")]:
        b, _, pal = construit(sc, 1, 1)
        durete = min(1.3, max(0.35, 1.0 + (10 - b.defense) * 0.04))
        ligne = [cible_nom]
        for nom in TOUS:
            c = evolue(HEROS[nom], 0 if sc == "chef_seul" else (2 if sc == "elite" else 4))
            nd, df = c["dice"]
            dps = (moy_de(nd, df) + c["qual"] + c["dmg_attr"] // 4) * durete * 2.4 / DUREE_ROUND_S * facteur_res(c, b)
            pv = 150 * dps * 0.8
            ligne.append("%.0f PV (K = %.0f)" % (pv, pv / b.vitmax))
        lignes.append(ligne)
    print(table(["Cible", "Krunt3", "Taranis", "Cyril", "Pascal"], lignes))
    print()


def facteur_res(c, m):
    f = 1.0
    if "dorsal" in m.res:
        f *= m.res["dorsal"]
    if c["arme"] == "tranchant" and "tranchant" in m.res:
        f *= m.res["tranchant"]
    return f


def ligne_standard(r, noms, scen_nom):
    n = r["n"]
    return [scen_nom, pct(r["vic"], n), pct(r["defaite"], n), pct(r["tombe_un"], n),
            fmt_s(mediane(r["rounds_all"])),
            " / ".join("%.1f" % moy(r["vit"][h]) for h in noms),
            " / ".join("%.1f" % moy(r["end"][h]) for h in noms)]


def section_livre(n):
    print("### E1. Échelle « Livre » (tour par tour, d20 contre Défense, K = 1) : les trois modèles\n")
    print("Colonnes : victoire, défaite (tous les héros à 0), au moins un héros à 0, durée médiane (1 round = 4 s), Vitalité perdue (cases) et Endurance dépensée par héros (ordre : Krunt3 / Taranis / Cyril / Pascal pour la table).\n")
    plan = [("Un héros seul", [[h] for h in TOUS], ["chef_meute"]),
            ("Un héros seul (Krunt3 uniquement)", [["Krunt3"]], ["elite", "legende"]),
            ("Deux héros (Krunt3 + Cyril)", [DUO], ["chef_meute", "elite"]),
            ("La table (quatre héros)", [TOUS], ["chef_seul", "chef_meute", "elite", "legende"])]
    for titre, configs, scs in plan:
        print("**%s**\n" % titre)
        lignes = []
        for cfg in configs:
            for sc in scs:
                for mod in "ABC":
                    r = une_cellule("livre|%s|%s|%s" % (mod, "+".join(cfg), sc), "livre", mod, cfg, sc, 1, 1, n)
                    lignes.append([config_nom(cfg), mod] + ligne_standard(r, cfg, NOM_SCEN[sc]))
        print(table(["Héros", "Modèle", "Scénario", "Victoire", "Défaite", "≥ 1 à terre", "Durée méd.", "Vit. perdue", "End. dépensée"], lignes))
        print()
    print("**Réconciliation avec le document 04 §6.2 (chef seul, quatre héros, échelle Livre, K = 1, modèle A)**\n")
    lignes = []
    for nom, o in [("tank joué, agonie 2 rounds (cas par défaut ici)", dict()), ("sans tank, agonie 2 rounds", dict(tank=False)),
                   ("sans tank, sans agonie ni phases (proche du document 04)", dict(tank=False, phases=False))]:
        r = une_cellule("rec04|%s" % nom, "livre", "A", TOUS, "chef_seul", 1, 1, n, opts=o)
        lignes.append([nom, pct(r["vic"], n), "%.1f rounds (%s)" % (moy(r["rounds_all"]), fmt_s(moy(r["rounds_all"]))), pct(r["tombe_un"], n)])
    print(table(["Cas", "Victoire", "Durée moyenne", "≥ 1 à terre"], lignes))
    print()
    print("**Combien de K pour que la table dure ? (échelle Livre, modèle A, quatre héros, chef + éclaireurs ; K_meute = 1)**\n")
    lignes = []
    for K in [1, 2, 3, 4, 6, 8]:
        for sc in ["chef_meute", "elite"]:
            r = une_cellule("livreK|%s|%d" % (sc, K), "livre", "A", TOUS, sc, K, 1, n)
            lignes.append([NOM_SCEN[sc], K, pct(r["vic"], n), fmt_s(mediane(r["rounds_all"])), pct(r["tombe_un"], n), pct(r["defaite"], n)])
    print(table(["Scénario", "K", "Victoire", "Durée méd.", "≥ 1 à terre", "Défaite"], lignes))
    print()


def section_jeu(n):
    print("### E2. Échelle « jeu » (temps réel tactile), K = 1, facteur 0,65 du document 01 : la démo sans correction\n")
    lignes = []
    for cfg in [["Krunt3"], ["Taranis"], ["Cyril"], ["Pascal"], DUO, TOUS]:
        for sc in ["chef_seul", "chef_meute"]:
            r = une_cellule("jeu1|C|%s|%s" % ("+".join(cfg), sc), "jeu", "C", cfg, sc, 1, 1, n)
            lignes.append([config_nom(cfg), NOM_SCEN[sc], pct(r["vic"], n), fmt_s(mediane(r["rounds_all"])),
                           "%.1f" % (sum(sum(r["vit"][h]) for h in cfg) / n / len(cfg))])
    print(table(["Héros", "Scénario", "Victoire", "Durée médiane", "Vit. perdue / héros (cases)"], lignes))
    print()


def section_K(n):
    print("### E3. Le coefficient K sur la Vitalité du chef de meute\n")
    print("**E3a. K seul, sans toucher aux dégâts reçus (échelle jeu, document 01 : facteur 0,65, une attaque toutes les 2,5 s), modèle C, héros seul, chef + éclaireurs (K_meute = max(1, K/5)), joueur moyen (esquive 55 %)**\n")
    lignes = []
    for K in [1, 2, 4, 6, 8, 10, 15, 20, 30]:
        ligne = [K]
        for h in TOUS:
            r = une_cellule("K|%s|%d" % (h, K), "jeu", "C", [h], "chef_meute", K, max(1, K // 5), n)
            ligne.append("%s / %s" % (pct(r["vic"], n), fmt_s(mediane(r["rounds_all"]))))
        lignes.append(ligne)
    print(table(["K"] + TOUS + [], lignes))
    print("\nLecture : victoire / durée médiane. Quand K monte, la durée monte mais la victoire disparaît : le chef frappe trop longtemps.\n")
    print("**E3b. K et coefficient de dégâts reçus kd (en plus du 0,65), tempo du chef 1,2 action par round (une toutes les 3,3 s), éclaireurs 0,4 : victoire à la première tentative (population de joueurs) / durée médiane d'une victoire, Krunt3 seul**\n")
    lignes = []
    for K in [8, 12, 16, 20, 25, 30]:
        ligne = [K]
        for kd in [0.08, 0.10, 0.12, 0.15, 0.20]:
            p = population("K3b|K3|%d|%.2f" % (K, kd), ["Krunt3"], "chef_meute", K, max(1, K // 5), n, opts_reco(kd=kd))
            ligne.append("%.0f %% / %s" % (100 * p["win"], fmt_s(p["dur"])))
        lignes.append(ligne)
    print(table(["K", "kd 0,08", "kd 0,10", "kd 0,12", "kd 0,15", "kd 0,20"], lignes))
    print()
    print("**E3c. Réglage recommandé (K_meute = %d, kd = %.2f, tempo %.1f et %.1f), héros seul, chef + éclaireurs, modèle C ; population de joueurs. K propre à chaque personnage (voir E3d)**\n" % (RECO["K_meute"], RECO["kd"], RECO["cad_boss"], RECO["cad_escorte"]))
    lignes = []
    for nom, K, o in [("Krunt3", 20, {}), ("Taranis", 20, {}), ("Taranis", 18, {}), ("Cyril (soin 2 Mana)", 20, {}), ("Cyril (soin 4 Mana)", 16, dict(soin_mana=4)),
                      ("Pascal « base »", 10, dict(pascal="base")), ("Pascal « soutien »", 14, dict(pascal="soutien")), ("Pascal « bombe »", 12, dict(pascal="bombe"))]:
        h = nom.split(" ")[0]
        a = population("K3c|%s|%d|0" % (nom, K), [h], "chef_meute", K, max(1, K // 5), n, opts_reco(**o))
        b = population("K3c|%s|%d|j" % (nom, K), [h], "chef_meute", K, max(1, K // 5), n, opts_reco(**o), decalage=DECALAGE_JETONS)
        lignes.append([nom, K, "%.0f %%" % (100 * a["win"]), "%.0f %%" % (100 * b["win"]), fmt_s(a["dur"]),
                       "%.1f" % a["vit_v"], "%.1f" % a["par_min"]])
    print(table(["Héros seul", "K", "1re tentative", "avec 3 Jetons", "Durée médiane (victoire)", "Vit. perdue par victoire (cases)", "Vit. perdue par minute"], lignes))
    print()
    print("**E3d. K nécessaire pour Cyril et Pascal « base » (même kd) : victoire 1re tentative / durée médiane**\n")
    lignes = []
    for h, Ks, o in [("Pascal", [6, 8, 10, 14], dict(pascal="base")), ("Pascal", [8, 10, 14, 20], dict(pascal="soutien")), ("Cyril", [20, 28, 36], {})]:
        for K in Ks:
            p = population("K3d|%s|%s|%d" % (h, o.get("pascal"), K), [h], "chef_meute", K, max(1, K // 5), n, opts_reco(**o))
            lignes.append([h + (" (%s)" % o["pascal"] if o else ""), K, "%.0f %%" % (100 * p["win"]), fmt_s(p["dur"])])
    print(table(["Héros", "K", "Victoire 1re tentative", "Durée médiane (victoire)"], lignes))
    print()
    print("**E3e. La table, modèle C, échelle jeu (pour mémoire : le jeu est solo ; pour le prototype à plusieurs ou la table avec un dé), kd = %.2f, chef + éclaireurs**\n" % RECO["kd"])
    lignes = []
    for K in [20, 40, 60, 80, 100]:
        r = une_cellule("Kt|C|%d" % K, "jeu", "C", TOUS, "chef_meute", K, max(1, K // 5), n, opts=opts_reco())
        lignes.append([K, pct(r["vic"], n), fmt_s(mediane(r["rounds_v"])), pct(r["tombe_un"], n)])
    print(table(["K", "Victoire", "Durée médiane", "≥ 1 à terre"], lignes))
    print()


def section_tank(n):
    print("### E4. Le rôle de tank de Krunt3 (quatre héros)\n")
    print("« Tank joué » : Krunt3 utilise Provocation, Mur de Chair et Interposition (Livre VI : 2 Endurance chacune). Part des coups : part des coups reçus par Krunt3 (25 % = pas de rôle). « Autre à terre » : probabilité qu'un des trois autres héros tombe.\n")
    print("**E4a. Échelle Livre, K = 1 (chiffres bruts)**\n")
    lignes = []
    for scen in ["chef_meute", "elite"]:
        for mod in "ABC":
            for tank in (True, False):
                r = une_cellule("tank|livre|%s|%s|%s" % (mod, scen, tank), "livre", mod, TOUS, scen, 1, 1, n, opts=dict(tank=tank))
                coups = sum(r["coups"].values()) or 1
                autres = [moy(r["vit"][h]) for h in TOUS if h != "Krunt3"]
                lignes.append([NOM_SCEN[scen], mod, "oui" if tank else "non", pct(r["coups"]["Krunt3"], coups), pct(r["tombe_k"], n),
                               pct(r["tombe_autre"], n * 3), pct(r["tombe_un"], n), pct(r["vic"], n),
                               "%.1f vs %.1f" % (moy(r["vit"]["Krunt3"]), moy(autres))])
    print(table(["Scénario", "Modèle", "Tank joué", "Part des coups", "Krunt3 à terre", "Autre à terre (par héros)", "≥ 1 à terre", "Victoire", "Vit. perdue K3 vs autres"], lignes))
    print()
    print("**E4b. Échelle jeu, à difficulté égale : kd calibré par modèle pour que les quatre héros (joueurs moyens) gagnent 75 % du temps SANS tank (Krunt3 attaque seulement), K = 60, chef + éclaireurs ; puis on joue le tank à trois niveaux. « provoc » = Provocation seule ; « complet » = Provocation + Mur de Chair + Interposition**\n")
    lignes = []
    for mod in "ABC":
        kd = calibre(mod, TOUS, "chef_meute", 60, 12, 0.75, max(300, n // 2), dict(cad_boss=RECO["cad_boss"], cad_escorte=RECO["cad_escorte"], tank=False),
                     etiquette="cal4|%s" % mod)
        kits = ["base"] if mod != "C" else ["base", "plaques", "bouclier"]
        for kit in kits:
            for tank in (False, "provoc", True):
                o = opts_reco(kd=kd, tank=tank, krunt_kit=kit)
                r = une_cellule("tankj|%s|%s|%s" % (mod, kit, tank), "jeu", mod, TOUS, "chef_meute", 60, 12, n, opts=o)
                coups = sum(r["coups"].values()) or 1
                autres = [moy(r["vit"][h]) for h in TOUS if h != "Krunt3"]
                lignes.append([mod, "%.3f" % kd, kit, {False: "aucun", "provoc": "provoc", True: "complet"}[tank], pct(r["coups"]["Krunt3"], coups), pct(r["tombe_k"], n),
                               pct(r["tombe_autre"], n * 3), pct(r["tombe_un"], n), pct(r["vic"], n), fmt_s(mediane(r["rounds_all"])),
                               "%.1f vs %.1f" % (moy(r["vit"]["Krunt3"]), moy(autres))])
    print(table(["Modèle", "kd calibré", "Kit de Krunt3", "Tank", "Part des coups", "Krunt3 à terre", "Autre à terre (par héros)", "≥ 1 à terre", "Victoire", "Durée méd.", "Vit. perdue K3 vs autres"], lignes))
    print()
    print("**E4c. Élite (K = 40, héros au palier 2), modèle C, même méthode (kd calibré sans tank pour 75 %)**\n")
    lignes = []
    kd = calibre("C", TOUS, "elite", 40, 1, 0.75, max(300, n // 2), dict(cad_boss=RECO["cad_boss"], tank=False), etiquette="cal4e")
    for kit in ["base", "plaques", "bouclier"]:
        for tank in (False, "provoc", True):
            o = opts_reco(kd=kd, tank=tank, krunt_kit=kit)
            r = une_cellule("tankje|%s|%s" % (kit, tank), "jeu", "C", TOUS, "elite", 40, 1, n, opts=o)
            coups = sum(r["coups"].values()) or 1
            autres = [moy(r["vit"][h]) for h in TOUS if h != "Krunt3"]
            lignes.append(["C", "%.3f" % kd, kit, {False: "aucun", "provoc": "provoc", True: "complet"}[tank], pct(r["coups"]["Krunt3"], coups), pct(r["tombe_k"], n),
                           pct(r["tombe_autre"], n * 3), pct(r["tombe_un"], n), pct(r["vic"], n), fmt_s(mediane(r["rounds_all"])),
                           "%.1f vs %.1f" % (moy(r["vit"]["Krunt3"]), moy(autres))])
    print(table(["Modèle", "kd calibré", "Kit de Krunt3", "Tank", "Part des coups", "Krunt3 à terre", "Autre à terre (par héros)", "≥ 1 à terre", "Victoire", "Durée méd.", "Vit. perdue K3 vs autres"], lignes))
    print()
    print("**E4d. Duo Krunt3 + Cyril, échelle jeu, K = 40, kd calibré sans tank pour 75 %, modèle C, selon le kit de Krunt3**\n")
    lignes = []
    kd = calibre("C", DUO, "chef_meute", 40, 8, 0.75, max(300, n // 2), dict(cad_boss=RECO["cad_boss"], cad_escorte=RECO["cad_escorte"], tank=False), etiquette="cal2")
    for kit in ["base", "bouclier"]:
        r = une_cellule("duo|%s" % kit, "jeu", "C", DUO, "chef_meute", 40, 8, n, opts=opts_reco(kd=kd, krunt_kit=kit))
        lignes.append([kit, "%.3f" % kd, pct(r["vic"], n), fmt_s(mediane(r["rounds_all"])), pct(r["tombe_k"], n), pct(r["tombe_autre"], n),
                       moy_ou_na(r["vit"]["Krunt3"]), moy_ou_na(r["vit"]["Cyril"])])
    print(table(["Kit de Krunt3", "kd calibré", "Victoire", "Durée", "Krunt3 à terre", "Cyril à terre", "Vit. perdue Krunt3", "Vit. perdue Cyril"], lignes))
    print()


def section_leviers(n):
    print("### E5. Les leviers de réglage, un par un (échelle jeu, modèle C, Krunt3 seul, joueur moyen)\n")
    print("Tous les essais gardent le facteur de dégâts reçus de l'essai considéré ; « brut » = facteur 0,65 du document 01 (kd = 1, une attaque toutes les 2,5 s).\n")
    lignes = []
    brut = dict(kd=1.0, cad_boss=1.6, cad_escorte=0.6)
    cas = [
        ("L0 brut : chef seul, K = 1", "chef_seul", 1, 1, brut),
        ("L1 brut : chef seul, K = 6", "chef_seul", 6, 1, brut),
        ("L2 brut : chef + éclaireurs, K = 6, K_meute = 1", "chef_meute", 6, 1, brut),
        ("L3 K = 20 seul, brut (chef seul)", "chef_seul", 20, 1, brut),
        ("L4 K = 20, dégâts kd = 0,15, tempo 1,2 (chef seul)", "chef_seul", 20, 1, opts_reco()),
        ("L5 L4 + éclaireurs (K_meute = 4)", "chef_meute", 20, 4, opts_reco()),
        ("L6 L5 sans phases ni agonie", "chef_meute", 20, 4, opts_reco(phases=False)),
        ("L7 L5 + terrain (feu 25 % par round, sol instable 20 %)", "chef_meute", 20, 4, opts_reco(terrain=dict(feu_p=0.25, instable_p=0.20))),
        ("L8 L5 + terrain, avec kd = 0,12 pour compenser", "chef_meute", 20, 4, opts_reco(kd=0.12, terrain=dict(feu_p=0.25, instable_p=0.20))),
    ]
    for (nom, sc, K, Km, o) in cas:
        r = une_cellule("lev|%s" % nom, "jeu", "C", ["Krunt3"], sc, K, Km, n, opts=o)
        tot_min = sum(r["rounds_all"]) / n * DUREE_ROUND_S / 60.0
        lignes.append([nom, pct(r["vic"], n), fmt_s(mediane(r["rounds_all"])), moy_ou_na(r["vit_v"]), "%.1f" % (moy(r["vit"]["Krunt3"]) / tot_min)])
    print(table(["Configuration", "Victoire", "Durée médiane", "Vit. perdue (victoires)", "Vit. perdue par minute"], lignes))
    print()


def section_variantes(n):
    print("### E6. Variantes de fiches\n")
    print("**Part des dégâts infligés et risque, table de quatre héros, échelle Livre K = 1 puis K = 3 (modèle A)**\n")
    lignes = []
    refs = [("livre", dict(), 1, "A"), ("livre", dict(), 3, "A")]
    variantes = [("référence (bagage Taranis ; Pascal « base » ; Flanc limité)", {}),
                 ("sans bagage de Taranis", dict(bagage_taranis=False)),
                 ("Pascal « soutien » (Garde Haute, Herbes)", dict(pascal="soutien")),
                 ("Pascal « bombe » (3 bombes de feu, niveau 5)", dict(pascal="bombe")),
                 ("Flanc Coordonné cumulable", dict(flanc_limite=False)),
                 ("Krunt3 avec Souffle du Réceptacle", dict(souffle=True))]
    for preset, base, K, mod in refs:
        for nom, o in variantes:
            oo = dict(base)
            oo.update(o)
            r = une_cellule("var|%s|%d|%s" % (preset, K, nom), preset, mod, TOUS, "chef_meute", K, max(1, K // 5) if preset == "jeu" else 1, n, opts=oo)
            parts = " / ".join("%.0f %%" % (100 * r["dmg"][h] / n) for h in TOUS)
            lignes.append(["%s K=%d" % (preset, K), nom, parts, fmt_s(mediane(r["rounds_all"])), pct(r["tombe_un"], n), pct(r["vic"], n)])
    print(table(["Échelle", "Variante", "Part des dégâts K3 / Tar / Cyr / Pas", "Durée méd.", "≥ 1 à terre", "Victoire"], lignes))
    print()
    print("**Parts des dégâts à la table en temps réel (échelle jeu, modèle C, K = 60, kd = %.2f, chef + éclaireurs)**\n" % RECO["kd"])
    lignes = []
    for nom, o in [("référence", {}), ("sans bagage de Taranis", dict(bagage_taranis=False)), ("Pascal « bombe »", dict(pascal="bombe")), ("Pascal « soutien »", dict(pascal="soutien"))]:
        r = une_cellule("varj|%s" % nom, "jeu", "C", TOUS, "chef_meute", 60, 12, n, opts=opts_reco(**o))
        lignes.append([nom, " / ".join("%.0f %%" % (100 * r["dmg"][h] / n) for h in TOUS), fmt_s(mediane(r["rounds_all"]))])
    print(table(["Variante", "Part des dégâts K3 / Tar / Cyr / Pas", "Durée méd."], lignes))
    print()
    print("**Taranis seul, avec et sans bagage ; Cyril avec soin limité (4 Mana au lieu de 2), kd = %.2f, K = %d, 1re tentative**\n" % (RECO["kd"], RECO["K"]))
    lignes = []
    for nom, h, o in [("Taranis avec bagage", "Taranis", {}), ("Taranis sans bagage", "Taranis", dict(bagage_taranis=False)),
                      ("Cyril soin 2 Mana", "Cyril", {}), ("Cyril soin 4 Mana", "Cyril", dict(soin_mana=4))]:
        p = population("var1|%s" % nom, [h], "chef_meute", RECO["K"], RECO["K_meute"], n, opts_reco(**o))
        lignes.append([nom, "%.0f %%" % (100 * p["win"]), fmt_s(p["dur"]), "%.1f" % p["par_min"]])
    print(table(["Cas", "Victoire 1re tentative", "Durée médiane", "Vit. perdue par minute"], lignes))
    print()


def section_competence(n):
    print("### E7. Sensibilité à l'habileté du joueur, et rangs supérieurs\n")
    print("**Victoire / durée médiane selon l'esquive du joueur (réglage recommandé, héros seul, chef + éclaireurs, modèle C)**\n")
    lignes = []
    for h in ["Krunt3", "Taranis"]:
        for esq in (0.35, 0.45, 0.55, 0.65, 0.75):
            r = une_cellule("sk|%s|%.2f" % (h, esq), "jeu", "C", [h], "chef_meute", RECO["K"], RECO["K_meute"], n, opts=opts_reco(esquive=esq))
            lignes.append([h, "%.0f %%" % (100 * esq), pct(r["vic"], n), fmt_s(mediane(r["rounds_all"])), moy_ou_na(r["vit_v"])])
    print(table(["Héros", "Esquive du joueur", "Victoire", "Durée médiane", "Vit. perdue (victoires)"], lignes))
    print()
    print("**Rangs supérieurs : kd calibré pour 45 % de victoires à la première tentative (population), Krunt3 seul, modèle C**\n")
    lignes = []
    for sc, K, pal in [("chef_meute", 20, 0), ("elite", 8, 2), ("elite", 10, 2), ("elite", 12, 2), ("legende", 4, 4), ("legende", 5, 4), ("legende", 6, 4)]:
        base = dict(cad_boss=RECO["cad_boss"], cad_escorte=RECO["cad_escorte"])
        Km = RECO["K_meute"] if sc == "chef_meute" else 1
        kd = calibre("C", ["Krunt3"], sc, K, Km, 0.45, n, base, palier=pal, par_population=True, etiquette="rang|%s|%d" % (sc, K))
        p = population("rangv|%s|%d" % (sc, K), ["Krunt3"], sc, K, Km, n, opts_reco(kd=kd), palier=pal)
        p2 = population("rangj|%s|%d" % (sc, K), ["Krunt3"], sc, K, Km, n, opts_reco(kd=kd), palier=pal, decalage=DECALAGE_JETONS)
        lignes.append([NOM_SCEN[sc], K, pal, "%.3f" % kd, "%.0f %%" % (100 * p["win"]), "%.0f %%" % (100 * p2["win"]), fmt_s(p["dur"]), "%.1f" % p["par_min"]])
    print(table(["Scénario", "K", "Palier des héros", "kd calibré", "1re tentative", "avec 3 Jetons", "Durée médiane", "Vit. perdue par minute"], lignes))
    print()
    print("**Quatre héros contre l'élite et le légendaire (échelle jeu, modèle C), K de table, kd du tableau précédent**\n")
    lignes = []
    for sc, kd, Ks in [("elite", 0.06, [30, 40, 50]), ("legende", 0.02, [12, 16, 20])]:
        for K in Ks:
            r = une_cellule("el4|%s|%d" % (sc, K), "jeu", "C", TOUS, sc, K, 1, n, opts=opts_reco(kd=kd))
            lignes.append([NOM_SCEN[sc], K, kd, pct(r["vic"], n), fmt_s(mediane(r["rounds_all"])), pct(r["tombe_un"], n)])
    print(table(["Scénario", "K", "kd", "Victoire", "Durée médiane", "≥ 1 à terre"], lignes))
    print()


def section_modeles(n):
    print("### E9. Les trois modèles à difficulté égale, héros seul (Krunt3, K = 20, chef + éclaireurs, échelle jeu)\n")
    print("kd calibré par modèle pour 45 % de victoires à la première tentative (population). « Spirale » : part des Hors Combat survenus quand l'Endurance était sous 2 (plus d'esquive possible), critère du document 01 §4.6 (seuil : moins de 25 % des échecs). « Temps sans esquive » : part des rounds passés avec moins de 2 Endurance.\n")
    lignes = []
    for mod in "ABC":
        base = dict(cad_boss=RECO["cad_boss"], cad_escorte=RECO["cad_escorte"])
        kd = calibre(mod, ["Krunt3"], "chef_meute", 20, 4, 0.45, n, base, par_population=True, etiquette="mod|%s" % mod)
        o = dict(base)
        o["kd"] = kd
        p = population("modv|%s" % mod, ["Krunt3"], "chef_meute", 20, 4, n, o, modele=mod)
        p2 = population("modj|%s" % mod, ["Krunt3"], "chef_meute", 20, 4, n, o, modele=mod, decalage=DECALAGE_JETONS)
        r = une_cellule("modr|%s" % mod, "jeu", mod, ["Krunt3"], "chef_meute", 20, 4, n, opts=o)
        spir = 100.0 * r["spir"] / r["mort_solo"] if r["mort_solo"] else 0.0
        lignes.append([mod, "%.3f" % kd, "%.0f %%" % (100 * p["win"]), "%.0f %%" % (100 * p2["win"]), fmt_s(p["dur"]), "%.1f" % p["par_min"],
                       "%.0f %%" % spir, "%.0f %%" % (100 * r["end_bas"] / n), "%.1f" % moy(r["end"]["Krunt3"])])
    print(table(["Modèle", "kd calibré", "1re tentative", "avec 3 Jetons", "Durée médiane", "Vit. perdue par minute", "Spirale", "Temps sans esquive", "Endurance dépensée"], lignes))
    print()
    print("**Modèle C : effet de la régénération d'Endurance (par round de 4 s) sur la spirale, même méthode**\n")
    lignes = []
    for regen in [3.0, 5.0, 6.5, 8.0]:
        base = dict(cad_boss=RECO["cad_boss"], cad_escorte=RECO["cad_escorte"], regen_end=regen)
        kd = calibre("C", ["Krunt3"], "chef_meute", 20, 4, 0.45, n, base, par_population=True, etiquette="reg|%.1f" % regen)
        o = dict(base)
        o["kd"] = kd
        r = une_cellule("regr|%.1f" % regen, "jeu", "C", ["Krunt3"], "chef_meute", 20, 4, n, opts=o)
        spir = 100.0 * r["spir"] / r["mort_solo"] if r["mort_solo"] else 0.0
        lignes.append(["%.1f (%.2f /s)" % (regen, regen / DUREE_ROUND_S), "%.3f" % kd, "%.0f %%" % spir, "%.0f %%" % (100 * r["end_bas"] / n)])
    print(table(["Régénération par round", "kd calibré", "Spirale", "Temps sans esquive"], lignes))
    print()


def section_equiv(n):
    print("### E8. Équivalence tempo / dégâts par coup (Krunt3 seul, K = 20, chef + éclaireurs, modèle C ; kd calibré pour 45 % de victoires à la première tentative)\n")
    print("Le prototype peut choisir : beaucoup de petits coups ou peu de gros coups, à pression égale. PC = points de coup (1 case = 4 PC). Morsure déchirante = 2d6+7, 14 en moyenne dans le Livre III ; armure de Krunt3 = cuir (-10 %).\n")
    lignes = []
    for cad in [0.4, 0.6, 0.8, 1.2, 1.6]:
        base = dict(cad_boss=cad, cad_escorte=cad / 3)
        kd = calibre("C", ["Krunt3"], "chef_meute", 20, 4, 0.45, n, base, par_population=True, etiquette="eq|%.1f" % cad)
        p = population("eqv|%.1f" % cad, ["Krunt3"], "chef_meute", 20, 4, n, dict(kd=kd, **base))
        pc = 14 * 0.65 * kd * 0.9
        lignes.append(["%.1f" % cad, "toutes les %.1f s" % (DUREE_ROUND_S / cad), "%.3f" % kd, "%.2f PC (%.1f %% de la Vitalité)" % (pc, 100 * pc / 52.0),
                       "%.0f %%" % (100 * p["win"]), fmt_s(p["dur"]), "%.1f" % p["par_min"]])
    print(table(["Actions du chef par round", "Cadence", "kd calibré", "Morsure déchirante, PC après armure", "1re tentative", "Durée médiane", "Vit. perdue par minute"], lignes))
    print()


SECTIONS = {"modeles": section_modeles, "equiv": section_equiv, "echelle": section_echelle, "livre": section_livre, "jeu": section_jeu, "K": section_K,
            "tank": section_tank, "leviers": section_leviers, "variantes": section_variantes, "competence": section_competence}


def main():
    global SEED
    ap = argparse.ArgumentParser(description="Essais d'équilibrage du combat du Jeu B (CRS)")
    ap.add_argument("--n", type=int, default=N_DEFAUT, help="tirages par cellule (défaut %d)" % N_DEFAUT)
    ap.add_argument("--seed", type=int, default=SEED)
    ap.add_argument("--sections", default="echelle,livre,jeu,K,tank,leviers,variantes,competence,equiv,modeles")
    a = ap.parse_args()
    SEED = a.seed
    print("<!-- simu_combat.py : graine %d, %d tirages par cellule, 1 round = %d s -->\n" % (SEED, a.n, DUREE_ROUND_S))
    for s in a.sections.split(","):
        SECTIONS[s.strip()](a.n)
        sys.stdout.flush()


if __name__ == "__main__":
    main()
