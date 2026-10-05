# Mécaniques du Jeu B, chapitre 1 : la chasse et le combat

Rédigé le 2026-10-05. Domaine : la Boucle de Chasse, le combat en temps réel tactile, le modèle de dégâts, les monstres en combat, la Traque, la Poursuite, les armes et armures, le score de fin de chasse, et la chasse complète du premier boss de la démo (Dorgane, id `cro02`).

Sources lues : Livre I ch. 2, 4, 7, 8, 10 ; Livre II ch. 6 (Poursuite) ; Livre III (fiches du chef de meute et de son éclaireur, lignes 28 et 227 : voir `donnees/monstres/correspondance.json`) ; Livre VI ch. 2, 3, 4, 8 ; Livre IX ch. 6, 7, 11 ; Livre X ch. 1 à 4, 6, 11, 13 ; `docs/audit/*`, `docs/livres-crs-vers-jeu-b.md`, `docs/cours-godot/07, 08, 12, 13`, `donnees/monstres/*.json`.

Convention : tout chiffre marqué **(à tester)** est une valeur de départ, pas une décision. Les conflits entre livres sont signalés « conflit résolu par l'option N » (options provisoires du brief). Le pixel de référence est celui du Jeu B : écran 360 px de haut (logique 800 × 360), héros 64 px pour 1,75 m, soit **36,6 px par mètre**.

## 0. Résumé en douze lignes

1. Une chasse = 4 temps : Désignation (interface), Traque (vue 3/4), Affrontement (arène latérale), Retour (interface, autre chapitre).
2. Les 3 modes s'enchaînent dans une chasse : 3/4 pour la Traque, plateforme pour la Poursuite (si le monstre ou le héros fuit), arène latérale pour l'Affrontement.
3. Le combat est en temps réel, sans d20 : le jet de touche est remplacé par la hitbox, le jet de défense par l'esquive minutée.
4. Deux barres, deux rôles : Vitalité (la vie, en cases du livre, 4 quarts par case) et Endurance (le carburant, 10 points). Le glissement Endurance vers Vitalité du Livre I est gardé comme règle de « persévérance ».
5. Dégâts : la formule joue sur des tableaux du livre (dé moyen de l'arme, Défense du monstre devenue dureté, faiblesses des fiches), avec un coefficient de chasse K = 20 sur la Vitalité du monstre (à tester).
6. Trois modèles de dégâts sont comparés (Livre I, Livres II/IX, proposition C) ; un protocole de prototype de 3 builds les départage.
7. Les Jetons de Connaissance (max 3) ne donnent pas un bonus de jet : ils révèlent et télégraphient (icône d'alerte, ligne de charge, seuil de phase sur la barre) et élargissent la fenêtre d'esquive parfaite.
8. Les monstres suivent les seuils de leurs fiches (50 % pour Dorgane), pas les 60/30 du Livre I ; les 5 états du Livre I sont une couche d'« humeur » optionnelle.
9. La manière de vaincre fixe la qualité des matériaux (5 cas du livre) par des indicateurs mesurés pendant le combat.
10. Familiers : un ordre, une jauge de vigueur, K.O. sans mort.
11. Démo : 1 arène, 1 chef de meute et 4 à 6 éclaireurs, 1 famille d'armes (une main + bouclier) plus l'arc, 3 jetons, 3 pièges, la météo des Forêts Totémiques.
12. Les 15 questions ouvertes (section 15) portent surtout sur la solitude du héros face à un boss écrit pour 4 joueurs, la taille de Dorgane (70 px) et la durée cible.

---

## 1. Ce que disent les livres

### 1.1 La Boucle de Chasse (Livre I ch. 4)

| Temps | Contenu des livres | Chiffres et règles |
|---|---|---|
| 1 Désignation | « La créature est désignée par le monde, pas par les joueurs ». 4 questions : quelle créature, qui désigne, pourquoi maintenant, quelles contraintes | 3 formes : Nécessité (honneur neutre, pas de Traque formelle), Contrat (mandant, conditions), Prestige (±2 Honneur, public) |
| 2 Traque | Préparation active ; chaque réussite significative = 1 Jeton de Connaissance | Maximum **3** par créature (4 avec la Bibliothèque de Terrain, ch. 4 §Traque et ch. 6) ; jetons non conservés d'une expédition à l'autre ; chercher un 4e fait monter la Tension |
| 3 Affrontement | « Comment la créature est vaincue » fixe la qualité des matériaux | Rapidement = Standard ; long combat d'usure = Supérieure ; faiblesse élémentaire = Élémentaire ; parties rares préservées = Rare ; fuite = rien + Tension +2 |
| 4 Retour | Récolte, Récit, Rituel ; principal mouvement de l'Honneur | Traité dans un autre chapitre |
| Trinité | Chaque chasse produit un Acte, une Trace, une Conséquence | À écrire dans le journal PocketBase |
| Défense du Bastion | La Boucle s'inverse : la proie vient au groupe | Défense réussie : Ancrage +2, Honneur collectif +1 ; avec pertes : Tension +1 ; échec : Ancrage −5, Tension +3 |

### 1.2 Les jauges (Livre I ch. 2)

| Jauge | Règle du livre | Valeurs |
|---|---|---|
| Vitalité | Blessures graves ; 0 = Hors Combat ; la mort n'est jamais mécanique | Max = 4 + END (7 à 16 cases à la création). Livre X ch. 13 §5 donne 12 au niveau 1 et 26 au niveau 30 (**conflit résolu par l'option 1** : Livre I) |
| Endurance | Carburant ; Techniques de Posture 2 End ; à 0 : plus d'action physique intense, l'action puise dans la Vitalité | Max 10 (+2 avec le Ceinturon Crochue) ; repos court : moitié ; repos long : pleine |
| Mana | Séparé de l'Endurance ; Techniques d'École 2 à 5 Mana ; à 0 : la technique part, coûte de l'Endurance et déclenche un jet de Tension | Max 8 au niveau 1 (Livre X §5) |
| Honneur | 0 à 10, 5 seuils (Paria 0–1, Suspect 2–3, Reconnu 4–6, Estimé 7–8, Légendaire 9–10) ; valeur connue du MJ seulement | Départ 4 à 6 |
| Tension | Collective, 1 à 10 ; monte par les actions bruyantes et le temps, baisse par la discrétion | Combat bruyant en zone habitée +2, Mana vide + sort +1 |
| Forge | Hors du périmètre de ce chapitre | 0 à 40 (option 5) |
| Corruption | **Pas de jauge définie** dans les livres (Livre I : jet VOL DD 15 par étape en zone corrompue ; Onguent de Purge −2 ; Livre IX : fiole −1) | Proposition en 3.6 |

Jauges croisées (ch. 2 §10) : Endurance vide + action physique = perte de Vitalité ; Mana vide + sort = Endurance + Tension ; tout vide = effondrement (hors de combat, pas la mort).

### 1.3 Le combat (Livre I ch. 7)

| Règle | Valeur du livre |
|---|---|
| Round | environ 6 secondes ; Initiative d20 + AGI + VOL, fixe pour tout le combat |
| Tour | 1 Pas + 1 Acte + 1 Riposte (1 Endurance). Sacrifier le Pas = un second Acte |
| Zones | Contact, Proche, Lointain ; une zone = 3 à 4 cases (CELL = 37 px dans l'application de combat) |
| Attaque | d20 + attribut (FOR lourdes, AGI légères) + Rang d'École (0 à +5) contre Défense = AGI + bonus d'armure |
| 5 résultats | Échec critique (1), échec, réussite tendue (= Défense ou +1), réussite (> Défense + 1), critique (20 = Ouverture) |
| Dégâts | Endurance d'abord, puis Vitalité ; dé unique : léger d6, standard d8, lourd d12, jet d6 ; *Ciblage Vital* d6 et *Coup Briseur* d8 visent la Vitalité directement |
| Riposte | Esquiver (+AGI à la Défense), bloquer, protéger un allié, contre-attaque (rang III+), rompre |
| Fatigue | À 0 Endurance : perte du Pas et de la Riposte, 1 Acte par round |
| 8 états | Concentré, Protégé, Déséquilibré, Étourdi, Épuisé, Immobilisé, Exposé, Enragé |
| Blessures persistantes | Dégâts de Vitalité sans soins entre deux scènes : une case cochée ; 3 cases = séquelle permanente |
| Soins en combat | Soin simple d6 Endurance ; Vitalité +1 (technique + Mana ou matériaux) ; stabilisation à 0 Vitalité |
| Créatures | 3 phases à 100/60, 59/30, 29/0 %, 5 états comportementaux, tour de créature = 1 action de phase + 1 réaction éventuelle |
| Terrain (VIII.c) | Sol instable (AGI DD 12 sinon Déséquilibré) ; hauteur (Avantage) ; obscurité partielle (Désavantage à distance) ; zone de feu ou d'acide 1d6 par round ; espace contraint (d12 traité comme d8) |

### 1.4 Les deux autres modèles de dégâts

| Source | Modèle |
|---|---|
| Livre II ch. 2 §6 | Après un critique, un d12 retire de la Vitalité à la créature et un d10 coûte de l'Endurance à l'attaquant ; les dégâts n'entament pas d'abord l'Endurance |
| Livre IX ch. 6 | 14 armes avec dés propres : Grande Lame 1d10, Épée Longue 1d8, Épée & Bouclier 1d6 + bouclier, Double Lame 1d6+1d6, Marteau 1d10, Lance 1d8, Arbalète-Lance 1d10, Hache-Épée 1d8 ou 1d6+1d4, Lame Chargée 1d6 + charge, Glaive-Insecte 1d8, Arc 1d8, Arbalète Légère 1d6, Arbalète Lourde 1d12, Cor de Chasse sans dégâts. Qualités : Basique −1, Standard 0, Supérieure +1, Rare +1 + propriété, Signature +1 + élément, Légendaire. Armures en « CA » : cuir +2, maille +3, plaques +4 (**la CA n'existe pas dans le Livre I** : conflit résolu en la lisant comme « bonus de Défense ») |

### 1.5 Les monstres (Livre III, fiche section V)

Une fiche donne : 6 attributs, Vitalité, Défense, Initiative, Résistance mentale, faiblesses élémentaires (multiplicateurs ×1,25 à ×1,5), résistances, points faibles anatomiques, immunités, phases (1 à 4) avec seuils propres, 3 à 4 attaques par phase, comportement de fuite, matériaux avec brisures, capture vivante. Échelle : Vitalité 6 (CR 1), 25 à 30 (CR 4), 65 (CR 12), 150 à 200 (Dragons). Les « Indices de Traque » sont écrits en trois paliers de compétence (0–1, 2–3, 4–5). Le mot « Jeton » n'apparaît jamais dans le Bestiaire (compatible : palier = jetons obtenus).

### 1.6 Traque, survie, poursuite

| Source | Règle |
|---|---|
| Livre I ch. 8 §IV | Traque en 3 phases : Repérage (Perception, Bestiaire, Survie), Approche (AGI, Exploration, Artisanat pour un piège), Connaissance (jetons). Avantages : position avantageuse, jeton, piège actif (la créature commence avec un état), surprise (20 naturel) |
| Livre I ch. 8 §I à V | Voyage en étapes (4 rôles), fatigue persistante (3 étapes sans repos long : End max −2 par étape), météo en 7 conditions, 5 environnements dangereux, provisions (1 portion et 2 eaux par étape), campement (sommaire, défensif +1 End, abri construit : Vitalité doublée) |
| Livre I ch. 10 | Pièges : Piège à Colle (DD 12, IMMOBILISÉE 2 rounds, FOR DD 14), Piège Tonnerre (DD 16, +1d8), Appât (1 h), Répulsif (4 h) ; bombes (Fumée, Tonnerre ÉTOURDI, Feu 2d6, Glace 2d6, Poison, Flash) ; huiles (+1 attaque, +1d4 élément) ; 1 consommable = 1 Acte, 10 par type maximum |
| Livre II ch. 6 | Poursuite par segments : jet opposé, Écart de −2 (rattrapé) à +3 (rupture) ; sprint 1 End (+3), terrain choisi 1 End, obstacle, appel d'allié, embuscade préparée (piège : −2 d'Écart), lecture anticipée (+2) ; 5 fins ; l'Endurance dépensée reste dépensée |
| Livre X ch. 11 | Météo : 6 terrains × tables 1d12 ; 4 saisons |
| Livre X ch. 1 à 4 | 8 familles d'armes et d'armures (14 armes × 8 = 112 armes ; 5 pièces × 8 = 40 armures) ; bonus de série à 3 et 5 pièces ; alchimie de combat (12 grenades, 8 huiles, 5 protections) |

### 1.7 Écoles et Mana (Livre VI)

14 Écoles martiales (une par arme), 5 Techniques par École (rangs I à V), coût 2, 2, 2, 3, 4 à 5 Mana. Technique de Posture : 2 Endurance, 4 (naturelles) ou 5 (légendaires). Les effets d'une Posture et d'une École sur la même action se cumulent (coûts compris, l'Avantage ne se double pas). Quatre modes de récupération du Mana : Flux (+1 par attaque réussie, +1 par déplacement significatif, +2 par manœuvre réussie), Ancrage (+1 par round immobile, +2 par tour défensif, +1 par dégât absorbé sans reculer), Rituel (complet au repos court avec acte rituel, rien en combat), Sacrifice (+2 par Vitalité perdue volontairement, +1 par état négatif accepté, +3 pour une mise en danger extrême).

### 1.8 Contradictions rencontrées dans ce domaine

| Conflit | Résolution adoptée |
|---|---|
| Phases 100/60/30 (Livre I) contre seuils des fiches (50 % pour le chef de meute) | **Option 7** : seuils des fiches ; 1 à 4 phases |
| Jetons : Avantage (L1 ch. 4), information (L1 ch. 7/8), −2 DD (L2) | Information et télégraphie, plus une fenêtre d'esquive (4.5) ; le −2 DD devient le temps de lecture réduit en Traque |
| États : 8 états du Livre I contre 6 états du Livre VI et du Livre IX (Exposé = Avantage ; Déséquilibré = pas de Techniques) | Effets du Livre I adaptés ; les états du Livre VI deviennent des effets de technique (5.1) |
| Réussite tendue : DD..DD+1 (L1) contre DD..DD+4 (L2) | **Option 8** : DD..DD+4 pour les jets hors combat ; en combat, la « tendue » devient l'esquive limite (3.2) |
| Soin : Endurance (L1, 2d4+2) contre Vitalité (+2, +5, +8, +12 au Livre IX) | Livre I (Potion de Soin = Endurance ; Potion de Vitalité = 1 case) |
| Dé de la Grande Lame d12 (L1) contre d10 (L9) | Tableau du Livre IX (14 armes) |
| Vitalité de base 4 + END (L1) contre 12 au niveau 1 (L10) | **Option 1** |

---

## 2. La Boucle de Chasse en jeu

### 2.1 Les quatre temps et les trois modes

| Temps | Mode de jeu | Ce que le joueur fait | Durée visée (à tester) | Sortie |
|---|---|---|---|---|
| 1 Désignation | Interface (+ scène de dialogue) | Lit le mandat, accepte, règle contraintes et équipe | 1 à 2 min | `chasse` créée, contraintes, mandant |
| 2 Traque | **Vue 3/4** | Explore la zone de territoire, lit des indices (jetons), pose des pièges, choisit la position d'entrée, campe | 6 à 10 min | 0 à 3 jetons, pièges posés, position, météo |
| 3 Affrontement | **Arène latérale** (type Metal Slug) | Combat en temps réel contre le monstre et sa meute | 5 à 8 min (◆◆) | issue, indicateurs de manière, brisures |
| 3b Poursuite (conditionnel) | **Plateforme de profil** | Course derrière ou devant le monstre qui fuit | 1 à 3 min | rattrapé (retour en arène), rupture (fuite) |
| 4 Retour au Clan | Interface (autre chapitre) | Récolte, Récit, Rituel | 3 à 5 min | Honneur, Tension, Forge, journal |

Durée totale d'une chasse ◆◆ : 15 à 25 minutes, compatible avec une session mobile. Les ◆◆◆ et ◆◆◆◆ peuvent aller à 10 à 15 minutes d'Affrontement.

**Règle d'enchaînement.** On ne passe jamais directement à l'Affrontement sans Désignation (livre). Une chasse de Nécessité n'a pas de Traque : l'écran de Désignation envoie directement à l'arène avec 0 jeton, mais un début de combat à la surprise du monstre (round 1 sans parade, soit 1,5 s de verrouillage des boutons d'esquive, pour éviter un coup injuste) **(à tester)**. Les quêtes de plateforme pures (cueillette, minage, ruines) ne sont pas des chasses et ne passent pas par cette machine.

### 2.2 Machine d'états de la chasse

```
DESIGNATION -> PREPARATION -> TRAQUE <-> CAMP
TRAQUE -> ENTREE_ARENE -> AFFRONTEMENT
AFFRONTEMENT -> POURSUITE -> AFFRONTEMENT   (monstre rattrapé)
AFFRONTEMENT -> BILAN                       (victoire)
AFFRONTEMENT -> REPLI -> TRAQUE ou CAMP     (héros Hors Combat ou fuite du héros)
POURSUITE -> BILAN_FUITE                    (rupture d'écart)
BILAN / BILAN_FUITE -> RETOUR_AU_CLAN       (autre chapitre)
```

Le héros à 0 Vitalité est **Hors Combat**, jamais mort (livre : la mort n'est jamais mécanique). Conséquences : écran de repli, case de Blessure Persistante, Tension +1, matériaux perdus. Le monstre garde 50 % des dégâts subis et ses brisures, mais récupère un état de Territoire à la tentative suivante **(à tester)**.

### 2.3 Les types de chasse

| Type | Traque | Contraintes | Effet sur le bilan |
|---|---|---|---|
| Nécessité | Absente ou réduite (1 indice max) | Aucune | Honneur neutre ; Tension déjà haute au départ |
| Contrat | Complète | 1 à 3 contraintes affichées (tête intacte, pas de feu, zone préservée, vivant) | Chaque contrainte respectée ou rompue pèse dans le Récit |
| Prestige | Complète | Public, journal visible | Honneur ±2 selon la manière |
| Défense du Bastion | Remplacée par une préparation défensive (bâtiments actifs) | Bastion à défendre | Résultats du Livre I ch. 4 §8 (Ancrage +2 ou −5) |

---

## 3. Le combat en temps réel tactile

### 3.1 Contrôles (écran 800 × 360 logique, paysage)

Cibles tactiles : 48 px minimum, 56 px recommandé (environ 9 à 10 mm sur un téléphone de 6,5 pouces) **(à tester sur 3 tailles d'écran)**.

| Zone | Contrôle | Action |
|---|---|---|
| Gauche (x < 40 %) | Stick flottant horizontal (apparaît sous le pouce) | Marcher, courir (seuil à 80 % d'inclinaison) |
| Gauche | Glissé vers le haut sur le stick | Sauter (option : bouton Saut dédié, accessibilité) |
| Gauche | Glissé vers le bas | S'accroupir, traverser une plateforme fine |
| Droite, bas | **Attaque** (64 px) | Toucher = enchaînement ; maintenir = coup chargé ou tir visé |
| Droite | **Esquive** (56 px) | Roulade avec invincibilité ; maintenir après une garde = parade (armes à bouclier) |
| Droite | **Technique** (56 px) | Lance l'emplacement actif ; glisser vers un des 3 emplacements pour changer |
| Droite | **Saut** (56 px, optionnel) | Remplace le glissé |
| Centre bas | **Objet** (48 px) | Utilise l'objet actif ; toucher la pastille pour faire défiler (3 emplacements rapides) |
| Haut droite | **Ordre** (44 px, si familier) | Commande le familier (1 ordre contextuel, recharge 20 s) |
| Haut droite | Pause | Pause avec les écrans Bestiaire et Journal |

Règles d'ergonomie : tout se joue avec deux pouces, jamais de geste à trois doigts ; aucune action vitale sur le bord de l'écran (zone de capture du système) ; mémoire tampon d'entrée de 120 ms (une pression 120 ms avant la fin d'une animation est jouée à la fin) ; aide à la visée à l'arc (verrouillage de hauteur sur la hurtbox la plus proche, désactivable).

### 3.2 Esquive, garde, endurance

| Action | Coût en Endurance | Détails (à tester) |
|---|---|---|
| Marcher | 0 | Vitesse 150 px/s |
| Courir | 1 par 2 s | 230 px/s |
| Roulade (Esquive) | 2 | 400 ms, invincible 0 à 250 ms, 90 px de déplacement, reprise de 150 ms |
| Garde (armes à bouclier) | 1 par 2 PC bloqués | Réduit les dégâts de 60 % ; garde cassée si End = 0 (Étourdi 1 s) |
| Parade (Esquive maintenue en garde) | 1 | Fenêtre de 150 ms ; si réussie : Ouverture, +2 Mana (Ancrage) |
| Coup lourd chargé | 1 à 2 | Selon la famille d'arme |
| Technique de Posture | 2 (livre) | Idem livre |
| Persévérer (action à End 0) | 0 End, **4 PC de Vitalité** (1 case) | Règle du Livre I : « le corps se consume lui-même » ; rendue visible par un flash rouge |

Régénération : 2 points par seconde après 0,8 s sans dépense ; arrêt pendant la garde. À End 0 : le héros est **Épuisé** : pas de roulade ni de course (livre : perte du Pas et de la Riposte), marche à 70 %, coups à 80 % de vitesse, 2 s de « souffle coupé » avant que la régénération reprenne.

**Esquive minutée (traduction du jet de défense).** Le moment où la roulade commence, mesuré avant l'impact :

| Fenêtre avant l'impact | Résultat | Équivalent du livre |
|---|---|---|
| 0 à 150 ms | **Esquive parfaite** : pas de dégât, une Ouverture (1 s, prochain coup x1,5), +2 Mana en mode Flux | Réussite |
| 150 à 350 ms | **Esquive limite** : pas de dégât mais 1 Endurance en plus et recul de 20 px | Réussite tendue (la cible « se repositionne ou subit une complication ») |
| Plus tôt ou plus tard | Touché | Échec |

La fenêtre « parfaite » vaut 6 images à 30 i/s ; chaque Jeton de Connaissance la porte plus loin (+2 images par jeton, soit 8, 10, 12) **(à tester)**.

### 3.3 Armes : 14 types, 6 familles d'animation

Portées du livre compressées au quart pour tenir à l'écran (l'écran fait 21,8 m de large) ; 1 m = 36,6 px.

| Famille d'animation | Armes (Livre IX) | Dé (moyenne) | Portée en jeu | Rythme | Spécificité jeu (à tester) |
|---|---|---|---|---|---|
| A. Une main + bouclier | Épée Longue (1d8, 4,5), Épée & Bouclier (1d6, 3,5, bouclier), Hache-Épée (1d8 ou 1d6+1d4) | 3,5 à 4,5 | 45 à 55 px | Rapide (combo 3 coups) | Garde et parade ; la Hache-Épée change de forme par pression longue |
| B. Deux mains lourdes | Grande Lame (1d10, 5,5), Marteau (1d10, 5,5), Lame Chargée (1d6+charge) | 5,5 | 60 à 75 px | Lent, long coup chargé | Grande vulnérabilité en préparation ; le Marteau étourdit (accumulation d'état) ; la charge de la Lame Chargée est une jauge d'arme |
| C. Deux armes | Double Lame (1d6+1d6, 7) | 7 en deux touches | 40 px | Très rapide, End intensive | Danse (état En Transe) : dégâts élevés, esquive coûteuse |
| D. Perche | Lance (1d8, 4,5, +2 de portée), Glaive-Insecte (1d8, aérien) | 4,5 | 90 à 100 px | Moyen, coups droits | La Lance garde à longue distance ; le Glaive gère un compagnon-insecte lié (nom d'origine à franciser) et le saut |
| E. Tir | Arc (1d8, 80 m devient 20 m), Arbalète Légère (1d6, 3 tirs/round à −2), Arbalète Lourde (1d12, immobile pour les dés max), Arbalète-Lance (1d10, 30 m devient 7,5 m) | 3,5 à 6,5 | 275 à 730 px | Tir, visée, rechargement | Désavantage au contact (arc) ; déplacement figé pour dégâts maximaux (lourde) |
| F. Soutien | Cor de Chasse (aucun dégât direct) | 0 | Zone 220 px | Mélodies | Techniques seulement ; mode Rituel ; l'unique arme sans bouton Attaque classique (le bouton lance la mélodie courante) |

Les familles sont les budgets d'animation : 6 jeux d'images au lieu de 14. Le héros a **2 emplacements d'arme** par chasse (changement au camp seulement) pour limiter les cas. Les noms anglais des armes du Livre X doivent être francisés (la Hache-Épée et la Lame Chargée existent déjà dans le Livre IX).

### 3.4 Techniques d'École : des boutons

| Élément | Règle de jeu |
|---|---|
| Emplacements | **3 techniques équipées** au camp ou à la Préparation ; 1 bouton Technique, 3 pastilles au-dessus. Le livre donne 5 techniques par École, une par rang |
| Coût | Mana : 2, 2, 2, 3, 4 à 5 selon le rang (livre) |
| Recharge | 1,5 s partagée (évite le spam) ; pas de recharge longue (le Mana régule seul, livre) |
| Techniques de Posture | 4 techniques (Loup, Faucon, Ours, Félin), 2 Endurance, partagent les emplacements |
| Combinaison | Posture et École sur la même action : coûts cumulés, effets cumulés, Avantage non doublé (livre VI ch. 2 §3) ; en jeu : lancer la seconde dans les 0,5 s déclenche la combinaison |
| Exemple | *Posture Lourde* (Coup Final rang I, 2 Mana) : prochain coup Avantage (x1,5 dégâts), immobile 0,8 s ; *Charge Profonde* (rang II, 2 Mana) : coup d12 avec télégraphie visible d'un round (1,2 s, dégât x1,5 par rapport au d10) ; *Coup Briseur* (rang IV, 3 Mana) : dégâts directs ignorant la dureté de zone |
| Tabou d'école | Chaque École a un tabou (« frapper sans intention de conclure ») : mécaniquement, un effet de **Retour** (Honneur), pas un malus en combat |

Mode « Avantage » du livre : une attaque avec Avantage inflige x1,5 ; un Désavantage inflige x0,75 et réduit la fenêtre parfaite de moitié. « Se déplacer » dans le texte des techniques se lit comme « sprint ou roulade ».

### 3.5 Le Mana en quatre modes

| Mode | Gain en combat (valeurs de jeu, à tester) | Pénalité | Comportement attendu |
|---|---|---|---|
| Flux | +1 par touche réussie (maximum 1 par 0,5 s) ; +1 par 4 m parcourus (hors sprint) ; +2 par esquive parfaite | Aucun gain si immobile 3 s ; une jauge de « rythme » se vide | Mobilité constante |
| Ancrage | +1 par 3 s sans se déplacer ; +2 par parade ou blocage réussi ; +1 par 6 PC absorbés sans reculer | Aucun gain en roulant | Tenir sa place, garde |
| Rituel | Aucun gain en combat ; **plein** au camp après un geste rituel (maintenir 5 s) ; +1 par action hors combat liée à l'école (Livre VI) | Mana à zéro pour tout combat enchaîné | Gérer le Mana comme une ressource |
| Sacrifice | +2 par case de Vitalité perdue volontairement (bouton de sacrifice dans les menus de technique) ; +1 par état négatif accepté (3 s sans soigner) ; +3 si 0 Vitalité évité | Vitalité vide et réserve de soins consommée | Risque permanent |

Mana à 0 : la technique part en consommant de l'Endurance (équivalent) et ajoute +1 Tension (livre : jet de Tension remplacé par un compteur). La table du Livre IX ch. 11 §5 est plus simple que celle du Livre VI ; le jeu suit le Livre VI pour les gains détaillés et reprend le Livre IX pour les récupérations courtes.

### 3.6 Les jauges dans le HUD

| Jauge | Affichage | Visible quand |
|---|---|---|
| Vitalité | Rangée de cases (14 px ; 16 cases = 224 px) en haut à gauche, chaque case remplie par quarts de 4 PC ; une case définitivement vide (Blessure Persistante) est dessinée avec un trait | Toujours |
| Endurance | Barre fine sous la Vitalité, 10 crans (12 avec le Ceinturon) | Toujours ; clignote sous 3 |
| Mana | Barre fine bleue sous l'Endurance ; icône de mode (Flux, Ancrage, Rituel, Sacrifice) | Si le héros a une École |
| Tension | Petit thermomètre vertical en haut à droite | Seulement à partir de 3 ou en Affrontement si une action la fait bouger |
| Honneur | Glyphe de seuil (5 niveaux) près du portrait ; valeur numérique **jamais affichée** (livre : valeur connue du MJ) | Dans le menu pause et au Retour |
| Corruption | Anneau violet autour du portrait, 0 à 10 | Seulement en zone corrompue (proposition : voir plus bas) |

**Corruption (proposition, hors démo).** Jauge individuelle 0 à 10 ; +1 par minute en zone corrompue moins 1 si Résistance mentale ≥ 12 ; effets : ≥ 3 Mana récupéré −25 % ; ≥ 6 techniques +1 Mana ; 10 événement de crise ; réduction : Onguent de Purge −2, Fiole anti-corruption −1. À valider par krunt (question 10).

Autres éléments du HUD : portrait et état des 8 pastilles d'états (icône 16 px, minuterie en cercle), barre du boss en haut au centre, 3 losanges de jetons à gauche de la barre du boss, **bande de progression de l'arène** (fine ligne de 400 px de long en haut au centre : héros, monstre, sortie), indicateurs de brisures (4 pastilles sous la barre du boss), vigueur du familier en bas à gauche.

---

## 4. Le modèle de dégâts

### 4.1 Pourquoi les chiffres du livre ne tiennent pas tels quels

Les fiches sont écrites pour une table de **4 joueurs** au tour par tour : un chef de meute de CR 4 a 27 de Vitalité ; quatre personnages à 4,5 de dégâts moyens et 60 % de touche l'abattent en 3 rounds (18 secondes de fiction). Un héros seul, en temps réel, doit tenir 4 à 6 minutes de combat actif. Il faut donc un **coefficient de chasse K** sur la Vitalité du monstre. Dans l'autre sens, la morsure moyenne du chef de meute (14) dépasse l'Endurance du héros (10) : sans réduction, un coup suffit. D'où un **facteur de dégâts reçus** de 0,65 (en points de coup).

### 4.2 Unités

| Unité | Définition |
|---|---|
| Point de coup (PC) | 1 case de Vitalité du livre = 4 PC ; Vitalité héros en PC = 4 x (4 + END) (END 6 : 40 PC) |
| PV de chasse du monstre | Vitalité du livre x K ; **K = 20** pour boss, mini-boss et chef de meute ; **K = 4** pour membres de meute (à tester) |
| Round de livre | 6 s ; **1 round de jeu = 3 s** (durées d'état et recharges) |

### 4.3 Formules (proposition C)

**Dégâts infligés au monstre :**

`dégâts = (dé_moyen + qualité + floor(attribut / 4)) x M_mouvement x M_dureté x M_zone x M_élément x M_état`

| Terme | Valeur |
|---|---|
| dé_moyen | Moyenne du dé de l'arme (Livre IX) |
| qualité | Basique −1, Standard 0, Supérieure +1, Rare +1, Signature +1 |
| attribut | FOR (familles A lourdes, B, D) ou AGI (A légères, C, E) |
| M_mouvement | 0,8 premier coup de combo, 1,0 deuxième, 1,25 troisième, 1,5 coup chargé, 2,0 coup lourd à immobilité (à tester) |
| M_dureté | `clamp(1,0 + (10 − Défense_zone) x 0,04 ; 0,35 ; 1,3)` ; la **Défense du Livre III devient la dureté** (Défense 11 : 0,96 ; ventre de Défense 8 : 1,08 ; Défense 36 : 0,35) |
| M_zone | Fiche : dos écailleux x0,75 (« physique mineur »), yeux x2, ventre et tête voir fiche, tête x1,5 pour les membres de meute |
| M_élément | Faiblesse de la fiche (x1,25 à x1,5) appliquée à la part élémentaire seulement (huile : +1d4) ; résistance x0,75 |
| M_état | Exposé : x1,25 (le livre le donnait comme « ignore l'armure ») ; Avantage x1,5 ; Désavantage x0,75 |

Exemple : Épée Longue Rare (4,5 + 1), FOR 7 (floor = 1), coup 2 sur le flanc de Dorgane : 6,5 x 1,0 x 0,96 x 0,75 = 4,7 PV. Même coup sur le ventre (Défense 8) : 6,5 x 1,08 = 7,0 PV. Avec une Huile de Feu (+2,5 x 1,5 = 3,75) : 10,8 PV.

**Dégâts reçus par le héros :**

`PC reçus = round(dégât_moyen_livre x 0,65 x (1 − min(0,35 ; 0,05 x CA)))`

Avec CA = somme du bonus de Défense des pièces (Crochue complète : 1+2+1+1+1 = 6, soit −30 %). Les dégâts bloqués sont payés en Endurance (voir 3.2). Une attaque qui inflige un état l'inflige à la touche, sauf garde.

### 4.4 Table de conversion des attaques de Dorgane et de son éclaireur

| Attaque (fiches) | Dégâts du livre (moy.) | PC (avant armure) | Cases |
|---|---|---|---|
| Éclaireur : Morsure en passant 1d4+FOR 3 | 5,5 | 4 | 1 |
| Éclaireur : Griffes aux jarrets 1d4+AGI 5 (+ Ralenti) | 7,5 | 5 | 1,25 |
| Éclaireur : Charge en coin 2d4+FOR 3 (3 ou plus) | 8 | 5 | 1,25 |
| Chef : Morsure déchirante 2d6+7 (+ Saignée) | 14 | 9 | 2,25 |
| Chef : Frappe de queue 1d8+7 | 11,5 | 7 | 1,75 |
| Chef : Charge déstabilisatrice 2d8+7 (renverse) | 16 | 10 | 2,5 |
| Chef, phase 2 : Déluge de crocs, 3 x 1d6+7 | 10,5 par morsure | 7 x 3 | 5,25 |
| Chef, phase 2 : Morsure renforcée 3d6+7 (Saignée auto) | 17,5 | 11 | 2,75 |

### 4.5 Les trois modèles comparés

| Critère | A. Livre I fidèle | B. Livres II / IX | **C. Proposition** |
|---|---|---|---|
| Principe | Dégâts sur l'Endurance (tampon et carburant), débordement en Vitalité | Dégâts directs sur la Vitalité ; l'attaque coûte de l'Endurance à l'attaquant | Deux barres séparées : Vitalité = vie ; Endurance = carburant (blocage, esquive, coups lourds) ; dégâts bloqués payés en End ; End vide = Persévérer (coûte de la Vitalité) |
| Points forts | Fidèle au texte, 20 « points » de héros, soins peu chers | Simple à comprendre ; jauges lisibles | Lisible à l'écran, cohérent avec l'esquive minutée, garde l'esprit du glissement End vers Vit |
| Points faibles | Spirale de mort en temps réel : être touché vide la ressource qui sert à esquiver ; Endurance à 10 est avalée par un seul coup du chef | Perd la jauge d'Endurance tactique ; frustrant si chaque coup coûte aussi de l'End | Plus de réglages ; Endurance qui ne sert que de carburant : il faut une règle de blocage |
| Héros solo contre un chef (nombre de morsures avant Hors Combat, END 6, CA 6) | environ 2 | environ 4 à 5 | environ 5 à 6 |
| Compatible Potion de Soin (Endurance) | Oui (soin de santé) | Non | Oui (soin de carburant) ; la santé vient de la Potion de Vitalité et de l'Infirmerie |

### 4.6 Test de prototype (à exécuter avant la fin de la phase 1)

**Matériel.** Une arène de 3 écrans, le chef de meute (phase 1 seulement), un héros avec l'Épée Longue, 3 builds du même prototype (A, B, C), même K.

**Protocole.** 6 testeurs (dont krunt et 2 joueurs de jeux d'action), 5 essais par build, ordre des builds tournant. Mesures automatiques : durée, coups subis, causes de Hors Combat, Endurance moyenne au moment du coup, nombre de roulades, nombre de potions. Mesures déclarées : lisibilité (1 à 5), équité (1 à 5), envie de rejouer (1 à 5).

**Critères de réussite du modèle retenu :**

| Critère | Seuil |
|---|---|
| Durée du combat de phase 1 au premier essai | 2 à 4 min |
| Coups subis par victoire d'un joueur moyen | 3 à 7 cases perdues |
| Victoire au premier essai sans jeton | 35 à 50 % |
| Victoire au premier essai avec 3 jetons | 60 à 75 % |
| « Mort » avec Endurance à 0 (spirale) | moins de 25 % des échecs |
| Équité moyenne | 3,5 ou plus |

Si le modèle C échoue sur la durée, on ajuste K (15 à 30) avant de changer de modèle ; s'il échoue sur l'équité, on bascule vers A avec Endurance tampon régénérante.

---

## 5. Monstres : états, brisures, phases, jetons, pièges, fuite

### 5.1 États (héros et monstres)

Durées en secondes de jeu (1 round de livre = 3 s). Les états du Livre I sont conservés ; les effets des Livres VI et IX deviennent des effets de technique ; les états infligés par le roster (Paralysie, Sommeil, Poison, Éblouissement, Saignée) sont ajoutés.

| État | Effet de jeu | Durée | Source type |
|---|---|---|---|
| Concentré | Fenêtre d'esquive +50 %, +2 Mana (Flux) | 3 s | Technique de préparation, parade |
| Protégé | Dégâts reçus −20 % | Jusqu'au prochain coup reçu | Garde active |
| Déséquilibré | Pas de technique, cadence −30 % | 1 à 2 s | Terrain instable, brisure |
| Étourdi | Perd les contrôles, une Ouverture est offerte | 1,5 s | Bombe de Tonnerre, coup à la tête |
| Épuisé | End = 0 : voir 3.2 | Jusqu'à End > 2 | Effort |
| Immobilisé | Ne peut pas se déplacer ; roulade impossible | 6 s (colle) | Piège à Colle |
| Exposé | Dégâts reçus x1,25 | 3 s | Armure brisée, brisure de partie |
| Enragé | Dégâts infligés +20 %, reçus +20 % | Jusqu'à la fin de la phase | Seuil de phase |
| Renversé | Au sol 1 s + 0,4 s de relevé | | Charge, queue |
| Ralenti | Vitesse −50 % | 3 s | Griffes aux jarrets |
| Saignée | 1 PC par 3 s | 15 s ; l'action Panser (2 s) l'arrête | Morsure déchirante |
| Secoué | Dégâts infligés x0,75, fenêtre parfaite −50 % | 6 s | Rugissement de dominance |
| Aveuglé | Le monstre perd la cible 2 s (coup sur les yeux) | 2 s | Yeux x2 |
| Paralysie, Sommeil, Poison, Éblouissement | Immobile 2 s, sommeil 3 s (réveil au premier coup), 1 PC par 2 s pendant 10 s, désorienté 2 s | | États infligés par les fiches |

**Résistance d'un monstre à un état.** Jauge d'état par type : seuil = 20 + 5 x Résistance mentale de la fiche (Dorgane, 7 : 55). Chaque source ajoute des points (colle 30, tonnerre 25, flash 25, coup à la tête 3). Au seuil : l'état s'applique, la jauge repart à 0 et le seuil monte de 50 % **(à tester)**. Un boss de CR 10 ou plus divise les durées par 2.

### 5.2 Brisures de parties

Chaque partie brisable de la fiche est une hurtbox avec une **jauge de partie** (fraction des PV de chasse). Un coup sur la partie réduit la jauge et les PV principaux avec ses multiplicateurs. Brisure : le monstre est Déséquilibré 2 s, la partie tombe (matériau garanti, qualité « Brisée » si la fiche dit « fragile »), un effet de combat s'applique.

| Partie (Dorgane) | Jauge (K = 20, PV 540) | Effet de la brisure (fiche) | Matériau |
|---|---|---|---|
| Cornes spiralées (ex-crête) | 12 % = 65 | Désactive la Vocalisation de commandement | Corne spiralée (fragile, rare si intacte) |
| Queue | 12 % = 65 | Supprime la Frappe de queue | Queue musclée |
| Pattes arrière | 15 % = 81 | Réduit la mobilité de la phase 2 (une seule charge par round) | Peau épaisse |
| Épaule | 10 % = 54 | Matériau d'épaule (rareté ◆◆◆) | Écaille d'épaule |

Les parties « rares à préserver » d'un contrat ne sont pas brisées : le choix entre briser (pour désactiver une attaque) et préserver (pour le contrat) est le cœur de la décision tactique.

### 5.3 Phases (machine à états du monstre)

Deux niveaux : la **phase** (de la fiche, sur seuil de Vitalité et déclencheur) et le **comportement** (micro-états).

**Phases.** Les seuils viennent des fiches ; le Livre I (100/60/30) est abandonné (**option 7**). Pour Dorgane : phase 1 de 100 % à 50 % ; phase 2 de 50 % à 0. Passage en phase 2 : Vitalité à 50 % **et** un déclencheur (3 membres de la meute morts, blessure sur un point faible anatomique, ou héros qui lui tourne le dos pour fuir). Trou de la fiche : sans déclencheur, le monstre resterait en phase 1 jusqu'à la mort. **Proposition : passage forcé à 30 %** (question 5).

**Comportements (micro-états, repris du module 8 du cours).**

| État | Contenu |
|---|---|
| IDLE / Territoire | Marque, repousse, patrouille |
| TRAQUE | Se rapproche du héros |
| TÉLÉGRAPHIE | Attitude et icône d'alerte avant le coup |
| ATTAQUE | Hitbox active |
| RÉCUPÉRATION | Fenêtre de punition (0,5 à 1,2 s) |
| DÉSÉQUILIBRÉ / ASSOMMÉ | Après brisure ou jauge d'état |
| FUITE | Si la fiche en prévoit une : voir 5.6 |
| AGONIE | Phase finale de Dorgane après 0 PV (5.7) |

**Les 5 états optionnels du Livre I** (couche d'« humeur », jamais exposés au joueur sauf par l'attitude du monstre) :

| Humeur | Règle de jeu |
|---|---|
| Territoire | Début de combat : le monstre défend ; l'adversaire est toléré 15 à 25 s si le héros ne frappe pas |
| Menacée | Réponse directe, attaques prévisibles (phase 1) |
| Blessée | Sous 50 % : motifs d'attaque changent, les jetons de phase 1 ne s'appliquent plus |
| Désespérée | Dernier quart : attaques maximales, endurance ignorée |
| Effondrée | 0 PV : plus de défense ; qualité des matériaux fixée à ce moment |

### 5.4 Les adversaires secondaires (meutes)

Règle du Livre I : combat de masse regroupé en entité de groupe (3 actes par round, réduits selon l'Endurance collective). **Traduction :** au plus **4 membres de meute actifs en même temps** à l'écran (lisibilité sur 360 px) ; les autres arrivent en renfort par la droite ou la gauche toutes les 20 s si le chef est vivant. Une meute dont la moitié est hors combat **fuit en zigzag** (fiche) et revient 1d4 heures plus tard : en jeu, elle quitte l'arène sans conséquence mais ne revient pas dans cet affrontement. L'éclaireur seul fuit au lieu de combattre ; à deux ou plus, il attaque en alternance ; à 3 ou plus, la Charge en coin se déclenche.

### 5.5 Les Jetons de Connaissance : télégraphier les attaques

Nombre : 0 à 3 (4 avec la Bibliothèque de Terrain). Un jeton = **une information** (action standard de phase 1, action spéciale de phase 1, déclencheur de phase, faiblesse élémentaire, comportement de la phase finale). Dans le livre, les jetons se dépensent ; en jeu, ils sont **consommés à la Désignation du combat** (ils déterminent ce que le HUD affiche) et ne se conservent pas d'une expédition à l'autre.

| Niveau de lecture | Ce que le HUD affiche |
|---|---|
| 0 jeton | Aucune aide : alerte visuelle minimale (le monstre prend la pose) |
| 1 jeton (action standard) | Icône d'alerte sur l'attaque standard de phase 1, 400 ms avant l'impact |
| 2 jetons | Idem pour l'action spéciale, **ligne de charge au sol** (zone dangereuse), seuil de phase marqué sur la barre du boss |
| 3 jetons | Comportement de la phase 2 télégraphié, faiblesse élémentaire révélée (icône sur la barre), déclencheur de phase listé |
| Tous niveaux | La **fenêtre d'esquive parfaite** s'élargit de 2 images par jeton |

Une information peut être **rendue fausse** : si le monstre change de comportement (blessé, piège, météo extrême), l'icône de ce jeton devient grise (le livre dit : « les patterns changent, les jetons peuvent ne plus s'appliquer »).

### 5.6 Fuite du monstre

Le texte de chaque fiche indique si et quand le monstre fuit (Dorgane : jamais en phase 2, mais combat 1d4 rounds après 0 PV). Pour les monstres qui fuient :

| Condition | Résultat |
|---|---|
| PV sous le seuil de la fiche, humeur Blessée, 3 s sans coup | Le monstre choisit une sortie de l'arène et s'y dirige |
| Le joueur coupe la route (piège, bombe, familier) | Retour au combat avec une humeur Désespérée |
| Il atteint la sortie | **Fuite** : Poursuite possible (plateforme) ; si rupture : aucun matériau, Tension +2 (livre), conséquence « la créature reviendra » |

### 5.7 L'agonie de Dorgane

Fiche : à 0 PV, il combat pendant 1d4 rounds à pleine capacité avant de s'effondrer. **Proposition : durée fixe de 8 s** (à tester), avec compte à rebours en anneau autour de la barre du boss, musique qui change, aucune nouvelle brisure possible. La qualité des matériaux est fixée à 0 PV ; le héros qui est mis Hors Combat pendant l'agonie remporte la victoire avec une Blessure Persistante.

### 5.8 Les pièges

| Piège (Livre I) | Fabrication | Effet de jeu | Limites |
|---|---|---|---|
| Piège à Colle | DD 12 | Immobilisé 6 s (diminué de 30 % à chaque réutilisation en 30 s) | 2 sur le terrain |
| Piège Tonnerre | DD 16 | Idem + 1d8 de dégâts (jauge d'état tonnerre : 25) | 1 |
| Bombe de Tonnerre | DD 13 | Étourdi par jauge d'état | Lancer (10 m) |
| Bombe de Feu et de Glace | DD 15 | 2d6 de dégâts élémentaires (faiblesse du monstre appliquée), terrain en feu 3 s | Lancer |
| Bombe Flash | DD 13 | Éblouissement 2 s, utile contre la Vocalisation | Lancer |
| Appât olfactif | DD 10 | Attire le monstre vers un point à la Traque (position en arène) | 1 à la Traque |
| Répulsif | DD 11 | Éloigne les créatures d'un camp pour la Traque | Camp |

Pose : 1,2 s d'animation, 3 pièges maximum sur le terrain ; ils se placent soit en Traque (en vue 3/4, ils deviennent des « points d'ancrage » dans l'arène), soit en direct dans l'arène. Un **piège actif posé en Traque** donne un état au monstre au début du combat (livre). Le jet d'alchimie d20 + ESP + Artisanat est remplacé par un taux de réussite affiché à l'établi (calculé sur la même formule) avec « préparation ratée » qui ne perd que la moitié des matériaux (anti-frustration).

---

## 6. Matériaux, score de fin de chasse, transition vers le Retour

### 6.1 Qualité des matériaux selon la manière de vaincre

Indicateurs mesurés pendant l'Affrontement. Résolution par priorité **Rare > Élémentaire > Supérieure > Standard** ; un second critère rempli ajoute une pièce bonus.

| Qualité | Condition mesurée (à tester) |
|---|---|
| Standard | Victoire sans autre critère rempli, ou en moins de 0,6 x t_ref (« rapidement ») |
| Supérieure | Victoire en 1,4 x t_ref ou plus (combat d'usure), sans 3 Hors Combat successifs |
| Élémentaire | Au moins 35 % des dégâts infligés sont élémentaires de faiblesse, et le coup fatal l'est aussi |
| Rare | Au moins une **zone rare** (définie par le contrat ou la fiche) est restée intacte (aucun coup, ou aucune brisure) |
| Aucun + Tension +2 | Le monstre quitte l'arène vivant (fuite) |

Pour Dorgane : t_ref = 5 min ; zones rares : glande à musc (cou, matériau signature, Compétence Dépeceur 2), œil (rareté ◆◆◆, Compétence 3), cornes intactes (la fiche les dit fragiles).

### 6.2 Le score de fin de chasse (Bilan)

Le livre refuse le farming et un tableau de progression : le score est **interne** et se montre sous forme qualitative (mention + 5 pastilles). Pondération (à tester) :

| Axe | Poids | Mesure |
|---|---|---|
| Manière | 30 | Qualité de matériau (Standard 10, Supérieure 18, Élémentaire 24, Rare 30) |
| Contrat | 25 | Contraintes respectées (proportion) ; 25 sans contrat si l'objectif de Nécessité est atteint |
| Maîtrise | 20 | Brisures utiles, esquives parfaites (par paliers de 5), pièges utilisés |
| Cohésion | 15 | 15 − 5 par Hors Combat du héros, − 3 par K.O. du familier ; bonus pour avoir protégé un allié |
| Rythme | 10 | Temps proche de t_ref |

Mentions : Exemplaire (≥ 85), Propre (65 à 84), Honorable (40 à 64), Brouillonne (< 40), Fuite (échec). Aucun classement en ligne, aucune répétition récompensée (une même créature n'a pas de bonus de re-chasse).

### 6.3 Interface de transition vers le Retour (le Retour est dans un autre chapitre)

À la fin de l'Affrontement, l'écran de Bilan expose : qualité de matériau, parties obtenues (liste), brisures, contraintes respectées ou non, mention, jetons utilisés. Il produit un objet `bilan_chasse` remis tel quel au chapitre du Retour (Récolte, Récit, Rituel). Valeurs proposées au Retour : Honneur de départ du Récit (Exemplaire +1, Propre +1, Honorable 0, Brouillonne −1 ; Prestige x2), Tension (Fuite +2 ; chasse sans bruit −1). Le Retour calcule la valeur finale.

---

## 7. Les familiers en combat

Le roster (272 entrées) compte 106 familiers possibles ; rôles recensés : éclaireur 39, assistant de combat 33, garde 31, récolte 30, signal 28, pisteur 22, bête de somme 19, monture terre 15, soin 8. 40 fiches mentionnent le K.O. par fatigue suivi de soins.

| Règle | Valeur (à tester) |
|---|---|
| Relation | Trois états : Sauvage (aucune aide), Habituée (pisteur et éclaireur en Traque, pas de combat), Dressée (peut combattre) |
| Commande | **Un seul bouton « Ordre »** : l'ordre dépend du contexte (attaquer la cible, défendre, rallier) ; recharge 20 s |
| Vigueur | Jauge propre, 20 PC x taille ; **à 0 : K.O. (jamais la mort)**, couché ; peut être relevé en 10 s avec une ration (30 %) ; K.O. répété 3 fois = fatigue, indisponible jusqu'au camp |
| Dégâts | Les dégâts du familier sont plafonnés à 25 % des PV de chasse infligés (il aide, il ne joue pas à la place du joueur) |
| Rôles en combat | Assistant de combat : charge, ouvre une Ouverture ; garde : attire l'attention 3 s ; signal : télégraphie +0,3 s ; soin : 1 case toutes les 30 s |
| Dorgane dressé | Fiche : charge la cible principale, brise sa garde d'un coup de cornes (**état Exposé 3 s**), rallie les petits coureurs. Lien « affectif », long à bâtir, redevient dominant si le dresseur faiblit |
| Éclaireur (Alizade) | Habituée : en Traque, révèle un point d'intérêt supplémentaire (pisteur, éclaireur) ; ne combat pas |
| Compétences de l'Armure Crochue complète | *Instinct de Meute* : l'ordre du familier est gratuit une fois par chasse |

---

## 8. Météo, terrain, survie, exploration et Poursuite

### 8.1 Météo de l'arène et de la Traque

La météo se tire **au début de la Traque** (d12 de la table du Livre X ch. 11) et reste pour toute la chasse. Pour la démo : table des Forêts Totémiques.

| d12 | Météo (Livre X) | Traque | Arène (traduction proposée, à tester) |
|---|---|---|---|
| 1–2 | Pluie dense | Piste à Avantage (−30 % de temps de lecture), torches inutiles | Sol glissant en zone sous-bois (Déséquilibré sur esquive ratée), huiles de feu à moitié efficaces |
| 3–5 | Humidité forte | Aucun effet sur la Traque | Usure des cuirs : −1 durabilité d'armure après la chasse |
| 6–8 | Conditions normales | Aucun | Aucun |
| 9–10 | Brouillard matinal | Visibilité 15 m les 2 premières minutes (les indices s'affichent plus tard) | Visibilité réduite en début de combat (le monstre apparaît à 8 m) |
| 11 | Orage violent | Le bruit couvre les sons | Éclairs en clairière (dégâts de décor 2 PC, Étourdi 0,5 s, **ligne d'alerte de 1 s au sol**) ; les dégâts de foudre du décor touchent aussi le monstre (2 % des PV, x1,25 sur faiblesse Foudre) |
| 12 | Pluie de sève éthérique | Aucun | Mana récupéré +50 % pendant toute la chasse |

Les cinq autres tables (Hautes Terres Claniques, Déserts Rouges, Royaumes Marins, Terres Ravagées, Failles du Monde) s'ajoutent en phase suivante.

### 8.2 Terrain et arène

Traduction du terrain du Livre I (VIII.c) en dalles de décor :

| Terrain du livre | Dalle de jeu |
|---|---|
| Sol instable (boue, glace) | Sol glissant : accélération −50 %, risque de Déséquilibré à la roulade |
| Hauteur | Plateforme : Avantage (x1,5) pour le premier coup en retombant |
| Obscurité partielle | Sous-bois : tir à distance −25 % de dégâts, visibilité 6 m |
| Zone de feu ou d'acide | Zone dangereuse : 2 PC par 1,5 s |
| Espace contraint | Armes lourdes : coups chargés réduits d'un cran (d12 traité d8) |

**Arène type, 5 400 px (environ 148 m)** : lisière d'entrée (0–1 400), clairière centrale (1 400–3 400), sous-bois dense (3 400–5 400), sortie à l'extrémité droite. Trois zones, trois contraintes. Les points d'ancrage de pièges sont placés dans la clairière.

### 8.3 Survie et exploration utiles à la Traque

Le voyage est abstrait en **étapes** (Livre I). Pour la chasse, le jeu retient :

| Règle du livre | Traduction |
|---|---|
| Fatigue persistante (3 étapes sans repos long : End max −2 par étape) | Conservée : compteur affiché à la carte de Traque ; au-delà de 3 zones traversées sans camp, End max −2 ; levée au camp |
| Provisions (1 portion/étape) et eau (2/étape) | 2 slots de sac (ration, gourde) ; sans eau, End max −2 par zone traversée, sans nourriture −1 ; on peut chasser et cueillir en vue 3/4 (mini-interaction) |
| Campement | 3 qualités : sommaire (repos standard), défensif (+1 End max), abri construit (Vitalité récupérée x2) ; le camp est le point de sauvegarde et de changement d'équipement |
| Repos | Court : moitié de l'End perdue (action de 10 s en jeu) ; long : tout (passe le temps, **Tension −1**, mais la créature se déplace) |
| Rôles du voyage (navigateur, guetteur, intendant, médecin) | Compétences passives des 4 personnages jouables (question 2) |
| Météo (7 conditions) | Voir 8.1 |
| Pièges de ruines (détecter, désamorcer, éviter) | Appartiennent aux quêtes de plateforme, non à la chasse |

### 8.4 La Traque en jeu

La **carte de Traque** (vue 3/4) représente le territoire du monstre (15 à 30 km² dans la fiche, abstrait en 6 à 8 écrans). Éléments :

- **Points d'intérêt** (5 pour Dorgane) : chacun révèle une des cinq informations jetables, conditionnée par une compétence (paliers 0–1, 2–3, 4–5 des « Indices de Traque » de la fiche).
- **Lecture** : maintenir le doigt sur l'indice pendant 2 à 6 s ; le temps dépend de la compétence du personnage et de la météo (remplace le jet d20 : le DD devient une durée).
- **Horloge** : 4 créneaux (aube, matin, midi, soir) ; chaque lecture et chaque déplacement long consomme du temps ; au-delà du dernier créneau, la **Tension** monte (le monde réagit : la meute migre, le mandant s'impatiente).
- **Furtivité** : approche silencieuse (jauge de bruit, AGI) ; un échec donne la surprise inversée au monstre ; un « 20 naturel » devient un approche parfaite avec 1,5 s de surprise pour le héros.
- **Position** : si l'approche réussit, le héros choisit sa porte d'entrée dans l'arène (gauche, ou une plateforme du centre).

### 8.5 La Poursuite (Livre II)

La Poursuite est la **seule apparition du mode plateforme dans une chasse**. Elle s'ouvre quand : (a) le monstre atteint la sortie de l'arène, (b) le héros choisit de fuir, (c) le monstre a détecté le groupe en Traque.

| Règle du livre | Traduction en jeu |
|---|---|
| Écart de −2 (rattrapé) à +3 (rupture) | Jauge d'Écart à 7 crans affichée entre deux silhouettes ; départ à 0 (ou +1 si le monstre avait de l'avance) |
| Jet opposé par segment | Un **segment** = un tronçon de 2 à 3 écrans de plateforme avec obstacles ; franchir sans heurt : +1 d'Écart pour le héros ; heurt : −1 |
| Terrain du segment annoncé (AGI, END, ESP) | Trois itinéraires à choisir (ouvert vite, difficile endurant, détour) |
| Sprint 1 End (+3) | Bouton Sprint : 1 End, +1 d'Écart d'élan ; deux sprints consécutifs : 2 End |
| Changer de terrain, obstacle, appel d'allié, lecture anticipée | Respectivement : bifurcation, renverser un tronc (le monstre perd 1 d'Écart), le familier coupe la route, indice affiché 2 s à l'avance |
| Embuscade préparée (piège posé en Traque) | Le piège se déclenche automatiquement : −2 d'Écart pour le monstre |
| Fins | Rupture (+3) : fuite ; rattrapé (−2) : retour en arène, monstre « acculé » (combat à mort, humeur Désespérée) ; épuisement (End 0) ; obstacle infranchissable ; décision narrative |
| « L'Endurance dépensée reste dépensée » | L'Endurance ne se régénère pas pendant la Poursuite |

---

## 9. Armes, armures, alchimie de combat

### 9.1 Armes

Voir 3.3 pour les familles. Qualités (Livre IX) : Basique −1 ; Standard 0 ; Supérieure +1 ; Rare +1 et propriété ; Signature +1 et élément ; Légendaire. Propriétés de l'exemple Crochue (Livre X ch. 2) : Grande Lame de Griffes : sur critique, saignée (+1 par round, 3 rounds) ; Épée Longue de Meute : +1d4 si un allié a frappé la même cible. En jeu : un **critique** devient un coup de **Ouverture** (esquive parfaite ou coup à la tête).

Usure (Livre IX §3) : Intact, Endommagé (−1 dégâts), Brisé ; passe à Endommagé après 3 combats intenses sans entretien. Proposition : l'usure se règle au camp (entretien : 10 s) ; un seul état « Endommagé » dans la démo.

### 9.2 Armures

| Type (Livre IX) | CA | Mobilité | Effet de jeu |
|---|---|---|---|
| Vêtements renforcés | +1 | Totale | −5 % dégâts reçus |
| Cuir | +2 | Bonne | −10 % |
| Maille | +3 | Correcte | −15 %, vitesse −3 % |
| Plaques | +4 | Réduite | −20 %, vitesse −8 %, roulade +1 End |
| Hybride organique | +3 | Bonne | −15 % + résistance de la créature d'origine |
| Éthérique | +3 + résistance | Bonne | −15 % + résistance d'effets non physiques |

Résistances élémentaires : −2 dégâts par élément (Livre X) devient −25 % sur les dégâts élémentaires. Faiblesse : l'élément ignore la résistance.

**Bonus de série** (Livre X ch. 3 et 4). Exemple Crochue (5 pièces : Heaume, Dossard, Brassards, Ceinturon, Grèves ; CA 1, 2, 1, 1, 1) : propriétés passives (Perception de Meute, Mobilité Rapide, Griffes Secondaires +1d4 sur critique, Endurance de Meute **End max +2**, Déplacement Aigu +1 m par round) ; **3 pièces : +1d4 d'initiative** (en jeu : +10 % de vitesse de déplacement, l'initiative n'existe plus) ; **5 pièces : Instinct de Meute** (1 fois par chasse, l'effet *Appel de Meute* de la Posture Loup sans Posture : une Ouverture pour le familier). Les 8 familles ont leurs bonus de série (Draconides : Résistance Feu +3 ; Léviathans : immunité Ralenti ; etc., liste dans le Livre X).

### 9.3 Alchimie de combat

| Objet | Livre | Jeu |
|---|---|---|
| Potion de Soin (DD 10) | +2d4+2 Endurance | +7 End instantanés, 1,2 s |
| Potion de Vitalité (DD 18) | +1 Vitalité | +1 case (4 PC), 1,5 s, rare |
| Antidote, Remède de Réveil | Retire EMPOISONNÉ / ÉTOURDI | Retire l'état, 1 s |
| Huile d'Aiguisage (DD 11) | +1 attaque 1 h | +1 aux dégâts de base 5 min |
| Huile de Feu ou de Glace (DD 15) | +1d4 élémentaire 10 min | +2,5 dégâts élémentaires par coup (faiblesse applicable), 90 s |
| Huile Perforante, Saignante (Livre X) | Ignore 2 d'armure ; saignée | Dureté de zone −0,15 ; saignée du monstre 1 % PV par 3 s |
| Bombe de Fumée (DD 10) | Zone obscurcie 2 rounds | Les monstres perdent la cible 3 s |
| Ciment d'Armure (DD 12) | +1 armure temporaire | +1 CA jusqu'à la fin de la chasse |

Limites : 10 consommables par type (livre) ; **6 emplacements** de sacoche en combat, 3 emplacements rapides (UI). Les recettes sont couvertes par le chapitre de l'artisanat.

---

## 10. Modèle de données

Tous les exemples sont exportables en JSON et utilisent des valeurs des livres ou du roster. Les enregistrements `chasse*` sont des collections PocketBase.

### 10.1 Bloc de combat d'un monstre (extension de `donnees/monstres/*.json`, id `cro02`)

```json
{
  "id": "cro02",
  "combat": {
    "fiche_livre3_ligne": 227,
    "attributs": {"FOR": 7, "AGI": 6, "END": 5, "ESP": 3, "VOL": 4, "PRE": 3},
    "vitalite_livre": 27,
    "k_chasse": 20,
    "pv_chasse": 540,
    "defense": 11,
    "initiative": 10,
    "resistance_mentale": 7,
    "faiblesses": [{"element": "Feu", "mult": 1.5}, {"element": "Foudre", "mult": 1.25}],
    "resistances": [{"zone": "dos", "type": "physique", "mult": 0.75}],
    "zones": [
      {"id": "tete", "mult": 1.0, "hauteur_px": 62},
      {"id": "yeux", "mult": 2.0, "etat": "Aveuglé", "zone_rare": true},
      {"id": "cou", "mult": 1.0, "zone_rare": true, "materiau": "glande_musc"},
      {"id": "ventre", "defense": 8, "mult": 1.0},
      {"id": "dos", "mult": 0.75}
    ],
    "parties": [
      {"id": "cornes", "pv_pct": 12, "effet": "desactive:cri_commandement", "materiau": "corne_spiralee", "fragile": true},
      {"id": "queue", "pv_pct": 12, "effet": "desactive:frappe_queue", "materiau": "queue_musclee"},
      {"id": "pattes_arriere", "pv_pct": 15, "effet": "limite:charge_par_round=1", "materiau": "peau_epaisse"},
      {"id": "epaule", "pv_pct": 10, "effet": "materiau", "materiau": "ecaille_epaule"}
    ],
    "phases": [
      {"id": 1, "nom": "L'Autorité", "de_pct": 100, "a_pct": 50,
       "transition": {"a_pct": 50, "ou": ["meute_morts>=3", "point_faible_touche", "heros_tourne_le_dos"], "force_a_pct": 30},
       "attaques": ["morsure", "queue", "cri_commandement", "charge"]},
      {"id": 2, "nom": "La Rage du Dominant", "de_pct": 50, "a_pct": 0,
       "attaques": ["deluge_crocs", "rugissement", "morsure_renforcee", "charge_aveugle"],
       "agonie_s": 8}
    ],
    "attaques": {
      "morsure": {"degats_livre": "2d6+FOR", "moy": 14, "pc": 9, "tele_ms": 500, "actif_ms": 150, "recup_ms": 700, "etat": "Saignée"},
      "charge": {"degats_livre": "2d8+FOR", "moy": 16, "pc": 10, "tele_ms": 700, "portee_px": 439, "etat": "Renversé"}
    },
    "jetons": [
      {"info": "action_standard_p1", "poi": "empreintes", "palier": "0-1"},
      {"info": "action_speciale_p1", "poi": "marquages", "palier": "2-3"},
      {"info": "declencheur_phase", "poi": "territoire_nerveux", "palier": "4-5"},
      {"info": "faiblesse", "poi": "archives_ou_bestiaire", "palier": "bibliotheque"},
      {"info": "comportement_p2", "poi": "perchoir", "palier": "4-5"}
    ],
    "matieres": [
      {"id": "ecaille_dorsale", "rarete": 1, "source": "carnage"},
      {"id": "corne_spiralee", "rarete": 2, "source": "carnage", "fragile": true},
      {"id": "glande_musc", "rarete": 2, "source": "carnage+depeceur2", "zone_rare": "cou"},
      {"id": "ecaille_epaule", "rarete": 3, "source": "brisure:epaule"},
      {"id": "oeil", "rarete": 3, "source": "carnage+depeceur3", "zone_rare": "yeux"}
    ],
    "capture_vivante": {"possible": true, "condition": "meute_morte && pv_pct<20"}
  }
}
```

### 10.2 Arme

```json
{"id": "epee_longue", "nom": "Épée Longue", "ecole": "flux_tranchant", "famille_anim": "A",
 "de": "1d8", "de_moyen": 4.5, "portee_px": 50, "mode_mana": "flux", "attribut": "AGI",
 "combo": [{"mult": 0.8, "ms": 380}, {"mult": 1.0, "ms": 420}, {"mult": 1.25, "ms": 620}],
 "qualite": "rare", "mod_qualite": 1, "usure": "intact"}
```

### 10.3 Chasse (collection `chasse`) et événements

```json
{"id": "ch_0001", "monstre": "cro02", "type": "contrat", "mandant": "clan_forestier",
 "contraintes": [{"id": "glande_intacte", "zone": "cou"}],
 "etat": "affrontement", "meteo": {"table": "forets_totemiques", "d12": 11},
 "jetons": [{"info": "action_standard_p1"}, {"info": "action_speciale_p1"}],
 "pieges_poses": [{"type": "colle", "ancre": "rocher_2"}],
 "position": "plateforme_centre", "tension_depart": 3}
```

```json
{"id": "ev_0001", "chasse": "ch_0001", "acte": "Chef de meute vaincu en 6 min 12 s",
 "trace": "Corne spiralée intacte, cicatrice à l'épaule",
 "consequence": "La meute orpheline cherche un nouveau chef ; le clan reconnaît la dette",
 "bilan": {"qualite": "rare", "score": 88, "mention": "Exemplaire", "brisures": ["queue"],
           "contraintes_respectees": ["glande_intacte"], "hors_combat": 0, "tension_delta": -1}}
```

### 10.4 États, jetons, familier

```json
{"id": "saignee", "nom": "Saignée", "duree_s": 15, "pc_par_3s": 1, "retire_par": ["panser", "potion_soin"]}
{"id": "jeton", "info": "action_standard_p1", "effet_hud": "icone_alerte_ms=400", "fenetre_parfaite_images": 2}
{"id": "fam_cro02", "monstre": "cro02", "relation": "dressee", "vigueur_pc": 40, "ordre_recharge_s": 20, "ko": "fatigue"}
```

Les champs sont conçus pour être lisibles dans CharForge (chaînes, nombres, listes courtes) et ne dépendent d'aucun type propre à Godot.

---

## 11. Interfaces et flux

| # | Écran | Mode | Contenu | Entrées / sorties |
|---|---|---|---|---|
| E1 | Panneau de Mandat | Interface | Les 4 questions du livre (créature avec fiabilité de la source, mandant, urgence, contraintes) ; boutons Accepter, Refuser, Négocier | `chasse` créée |
| E2 | Préparation | Interface | Équipement (2 armes, armure, 3 techniques, sacoche 6 slots), familier ; recommandations selon contrats | Équipement figé pour la Traque (modifiable au camp) |
| E3 | Carte de Traque | 3/4 | Carte, horloge de 4 créneaux, jauges de fatigue et de Tension, points d'intérêt, pose de pièges | Jetons (max 3), météo, position |
| E4 | Lecture d'un indice | 3/4 (modale) | Maintenir 2 à 6 s ; résultat : un jeton | Jeton consommé en E6 |
| E5 | Camp | 3/4 | Repos court ou long, entretien, changement d'équipement, sauvegarde | Tension, fatigue |
| E6 | Entrée d'arène | Interface (transition) | Résumé « Ce que vous savez » : jetons (icônes), pièges, météo, contraintes ; bouton Entrer | Arène chargée |
| E7 | HUD d'Affrontement | Arène latérale | Voir 3.6 | |
| E8 | Pause | Interface | Journal, Bestiaire (informations débloquées par jetons), options (aide à la visée, bouton Saut) | |
| E9 | Poursuite | Plateforme | Jauge d'Écart, 3 itinéraires, bouton Sprint | Rattrapé, rupture |
| E10 | Repli | Interface | Résumé de la blessure, Tension +1, matériaux perdus ; option de revenir | |
| E11 | Bilan de chasse | Interface | Mention, qualité, pastilles des 5 axes, parties obtenues, brisures, contraintes | `bilan_chasse` |
| E12 | Passage au Retour | Interface | Aperçu Acte, Trace, Conséquence ; bouton « Rentrer au clan » | Chapitre du Retour |

Transitions : tout retour de E7 vers E3 ou E5 (repli) est autorisé ; **le combat ne se sauvegarde jamais en cours** (reprise au camp). Le héros peut quitter l'arène à tout moment par la sortie gauche (fuite volontaire, Poursuite en sens inverse sans le monstre qui chasse s'il ne l'a pas repéré).

---

## 12. Chiffres d'équilibrage de départ (tous à tester)

| Paramètre | Valeur |
|---|---|
| Écran / héros | 800 x 360 / 64 px ; 36,6 px par mètre |
| Vitalité du héros | 4 + END cases, 4 PC par case (END 6 : 40 PC) |
| Endurance | 10 (+2 Ceinturon), régénération 2 /s après 0,8 s |
| Mana | 8 au départ, rang IV 3, rang V 4 à 5 |
| Coefficients | K boss 20 ; K meute 4 ; facteur de dégâts reçus 0,65 ; armure 5 % par CA, plafond 35 % |
| Roulade | 2 End, 250 ms d'invincibilité, fenêtre parfaite 150 ms (+2 images par jeton), limite 350 ms |
| Round de jeu | 3 s |
| Durée du combat | ◆ 1 à 2 min ; ◆◆ 5 à 8 min ; ◆◆◆ 8 à 12 min ; ◆◆◆◆ 10 à 15 min |
| Familier | Plafond de dégâts 25 % ; ordre 20 s ; K.O. à vigueur 0 |
| Pièges | 3 sur le terrain ; Colle 6 s |
| Jetons | Max 3 (4 avec la Bibliothèque de Terrain) |
| Tension de Traque | +1 au dernier créneau dépassé |
| Phases | Seuils des fiches ; passage forcé à 30 % si déclencheur absent |
| Agonie (Dorgane) | 8 s |
| Qualité | t_ref 5 min ; Standard < 3 min ; Supérieure ≥ 7 min ; Élémentaire 35 % ; Rare : zone intacte |
| Poursuite | Écart −2 à +3 ; sprint 1 End |
| Armes | Portées : arc 730 px, arbalète légère 366, lourde 550, lance 95, épée 50 |

**Budget de combat de Dorgane (calcul de contrôle).** 540 PV de chasse ; coup moyen avec huile de feu 8,5 : environ 64 touches ; à 0,6 touche par seconde utile, 107 s d'attaque pure ; plus esquives, adds, déplacements : 4 à 6 min. Dégâts reçus : une attaque toutes les 2,5 s, 55 % de touches évitées (joueur moyen) : 1,1 coups de 8 PC par 5 s, soit environ 90 PC en 5 min ; avec 40 PC de Vitalité (et armure −30 %), il faut des soins (Potion de Soin pour l'End, Potion de Vitalité) ou une bonne esquive. Le test 4.6 confirmera si cela mène à la cible « 3 à 7 cases perdues ».

---

## 13. Premier boss de la démo : Dorgane (`cro02`), chef de meute ◆◆, CR 4, 2 phases

### 13.1 Fiche de jeu

| Champ | Valeur | Source |
|---|---|---|
| Nom | Dorgane, « Le Maître des Trotteurs » | `crochues.json` |
| Rang, CR | ◆◆ Rare, CR 4 | `crochues.json` |
| Taille | 1,9 m au garrot, 3,2 m de long, hauteur de sprite 70 px (longueur environ 117 px) | roster + fiche Livre III |
| Élément | Neutre ; faiblesses Feu x1,5 et Foudre x1,25 | fiche |
| Terrain | Forêts mixtes, sous-bois denses | roster |
| Trait distinctif | Deux cornes torsadées en spirale d'ivoire | roster |
| Vitalité | 27 (PV de chasse 540) ; Défense 11 ; Initiative 10 ; Résistance mentale 7 | fiche |
| Meute | Alizade (id `cro01`) : CR 1, Vitalité 6 (24 PV de chasse), Défense 7, hauteur 44 px, faiblesses Feu et Foudre, ventre Défense −2, tête x1,5 | fiche + roster |
| Familier | Possible (lien « affectif »), rôles assistant de combat et monture terre | roster |

**Remarque honnête sur la taille.** À 70 px de haut, Dorgane est à peine plus haut que le héros (64 px) : c'est un prédateur de la taille d'un grand cervidé, pas une silhouette de boss. Ce n'est pas un problème de règles (la fiche fixe 1,9 m), mais de lisibilité à 360 px : voir question 4.

### 13.2 Pas à pas

**Étape 1. Désignation (E1), 1 à 2 minutes.** Un clan forestier désigne la créature (formes : Contrat). Contenu du panneau : créature (« un grand dominant de meute, vu pour la dernière fois à la lisière nord »), source à fiabilité moyenne (silhouette partiellement obscurcie), mandant (le clan, attentes : préserver la glande à musc pour les pisteurs, qui s'en servent comme sauf-conduit dans les territoires de meute), urgence (une route de pisteurs coupée depuis trois jours : Tension de départ 3), contraintes affichées : **Glande à musc intacte** (zone rare : le cou). Choix : accepter ou négocier (contrat plus court, moins bien payé).

**Étape 2. Préparation (E2).** Le joueur choisit : une arme (Épée Longue, ou Arc pour viser la tête depuis les plateformes), l'armure, 3 techniques, la sacoche (conseil : 2 Huiles de Feu, 2 Potions de Soin, 1 Piège à Colle, 1 Bombe Flash contre la Vocalisation). Le Feu est la faiblesse à ×1,5.

**Étape 3. Traque (E3), 6 à 10 minutes, vue 3/4.** Carte de 6 écrans. Météo tirée à l'ouverture (table des Forêts Totémiques). Cinq points d'intérêt, chacun associé à un palier de compétence de la fiche :

| Point d'intérêt | Palier | Information (jeton) | Interaction |
|---|---|---|---|
| Empreintes de 12 cm à la foulée de 1,4 m | 0–1 | Action standard de phase 1 (morsure, charge) | Maintenir 2 s |
| Griffades à 2 m de hauteur, 5 griffes parallèles | 0–1 | Zone de territoire | Maintenir 2 s (pas de jeton, informe la position d'entrée) |
| Empreintes distinctes, zones de repos, meute qui converge | 2–3 | Action spéciale de phase 1 (Vocalisation) | Maintenir 4 s |
| Marquages nerveux et denses | 4–5 | Déclencheur de phase (3 membres morts, point faible touché, fuite) | Maintenir 6 s |
| Perchoir de repos préféré | 4–5 | Comportement de phase 2, et **position avantageuse** | Maintenir 6 s |

Le maximum est 3 jetons : le joueur choisit lesquels lire (et la Salle des Archives donnerait la faiblesse sans jeton). Un éclaireur Alizade dressé, s'il existe, révèle un point supplémentaire. La Traque est aussi l'occasion de poser un Piège à Colle en point d'ancrage de la clairière (le monstre commencera le combat Immobilisé 3 s s'il passe dessus) et d'utiliser un Appât olfactif pour fixer le chef dans la clairière. Si le héros se fait détecter (jauge de bruit), la meute attaque en premier et la Poursuite est envisageable (rare ici : le chef ne fuit pas).

**Étape 4. Camp (E5).** Repos court, entretien, dernier changement d'équipement ; la Tension baisse de 1 si le repos est long mais la météo avance.

**Étape 5. Entrée d'arène (E6).** Écran « Ce que vous savez » : 0 à 3 icônes de jetons, pièges posés, météo, contrainte du contrat. Le héros choisit sa porte d'entrée (gauche, ou plateforme centrale si l'approche a réussi).

**Étape 6. Affrontement (E7), 5 à 8 minutes.** L'arène fait 5 400 px (lisière, clairière, sous-bois, sortie à droite). Chronologie type :

| Moment | Événement |
|---|---|
| 0:00 | **Territoire.** Dorgane se tient au centre de la clairière, 4 Alizades se déploient et attaquent en alternance (un frontal, un par les jambes). Le chef ne frappe pas encore (la fiche : « il positionne sa meute, attend qu'elle engage ») |
| 0:00 à 0:30 | Le joueur apprend le rythme des éclaireurs : Morsure en passant (4 PC), Griffes aux jarrets (Ralenti 3 s), Charge en coin quand 3 ou plus attaquent la même cible (renversé). 4 coups d'épée tuent un éclaireur. À 3 éclaireurs morts : **déclencheur de phase 2** satisfait |
| 0:30 | Dorgane entre en action : Vocalisation de commandement (icône d'alerte de 800 ms au-dessus de la tête, les Alizades dans 60 m (2 200 px) attaquent la cible simultanément). Parades : Bombe Flash, briser les cornes, tuer vite les éclaireurs |
| 0:30 à 3:00 | Phase 1 : Morsure déchirante (télégraphie de 500 ms, Saignée), Frappe de queue (arc de 180° vers l'arrière, il faut sauter, 400 ms), Charge déstabilisatrice (12 m, 439 px, sabot qui gratte 700 ms, le héros doit passer au-dessus ou rouler à la fin de la course) |
| ≈ 3:00 | Dorgane à 50 % **et** déclencheur actif : **transition de phase.** Crête et regard virent au rouge (fiche : « la crête vire au rouge, les yeux s'enflamment »), cri continu |
| 3:00 à 5:30 | Phase 2 : Déluge de crocs (3 morsures de 7 PC en un enchaînement), Rugissement de dominance (Secoué 6 s dans 15 m = 550 px, éclaireurs +2), Morsure déchirante renforcée (11 PC, Saignée sans jet), Charge aveugle (deux charges par round, la seconde moins précise mais perce l'armure légère). La fiche note que la rage le rend plus prévisible |
| 5:30 | **0 PV : agonie de 8 s**, anneau de compte à rebours ; aucune brisure ne compte |
| 5:38 | **Effondrée.** Qualité de matériau fixée à 0 PV ; fin |

Décisions tactiques : tuer les éclaireurs d'abord (stoppe les attaques coordonnées) ou viser les cornes (stoppe la Vocalisation), frapper la tête haute en sautant ou à l'arc (hauteur de la tête : 62 px, la tête baisse pendant la morsure et la charge), éviter les yeux si le contrat demande l'œil intact, éviter le cou si le contrat demande la glande intacte, tirer parti du Feu x1,5, utiliser la colle avant une phase dangereuse.

**Étape 7. Variantes d'issue.**
- *Héros Hors Combat avant la victoire* : repli (E10), Blessure Persistante, Tension +1 ; le chef garde 50 % des dégâts et ses brisures, retrouve l'humeur Territoire.
- *Fuite du héros* (sortie gauche) : le chef se lance dans une Poursuite courte (le Livre III note que la fuite du héros déclenche la rage) ; passage forcé en phase 2.
- *Capture vivante* (fiche) : la meute morte et Dorgane sous 20 % de Vitalité, avec filets (Compétence 3 et plus) ; chasse annexe pour les éleveurs, dressage possible avec le lien « affectif ».

**Étape 8. Bilan (E11) : exemple de calcul.** Victoire en 6 min 12 s (supérieure à 1,4 x 5 min : critère « Supérieure » rempli) ; la glande à musc est intacte (zone rare respectée : Rare) ; la queue a été brisée ; contrainte respectée (25) ; 1 Hors Combat évité de justesse ; 12 esquives parfaites : Manière 30 (Rare) ; Contrat 25 ; Maîtrise 12 (1 brisure, 12 esquives parfaites, 1 piège) ; Cohésion 15 ; Rythme 6 : **score interne 88, mention Exemplaire**. Qualité Rare : une pièce bonus. Acte : le chef de meute vaincu ; Trace : glande à musc intacte et cicatrice à l'épaule ; Conséquence : la meute orpheline cherche un chef, la route est rouverte, le clan est redevable.

**Étape 9. Transition (E12) vers le Retour.** L'objet `bilan_chasse` passe au chapitre du Retour (Récolte avec Dépeceur, Récit, Rituel).

---

## 14. Portée de la démo (16 mars 2028) et feuille de route

### 14.1 Sous-ensemble minimal (démo)

| Domaine | Inclus | Exclu |
|---|---|---|
| Chasse | Un contrat (E1 à E12), Traque courte (5 points d'intérêt), 1 arène, Retour (stub) | Nécessité, Prestige, Défense du Bastion |
| Monstres | Dorgane et 4 à 6 Alizades, 2 phases, 4 brisures, agonie | Autres monstres, fuite générique |
| Armes | Famille A (Épée Longue, Épée & Bouclier) et E (Arc) | 11 autres armes |
| Techniques | 3 techniques de l'École Flux Tranchant (rangs I à III) ; mode Flux seul | 13 autres Écoles, 3 autres modes |
| Jauges | Vitalité, Endurance, Mana, Tension | Honneur affiché, Corruption |
| États | 8 du livre + Saignée, Renversé, Ralenti, Secoué | États du roster (poison, sommeil, etc.) |
| Pièges | Colle, Bombe Flash, Bombe de Feu (via sacoche) | Piège Tonnerre, Appât |
| Météo | Table des Forêts Totémiques | 5 autres tables |
| Familier | Un seul, en commande simple, ou aucun | Dressage complet |
| Poursuite | Optionnelle (coupe possible) | |

### 14.2 Feuille de route par versions

| Version | Contenu |
|---|---|
| v0.1 Prototype | Héros, arène de 3 écrans, Dorgane phase 1, 3 builds de dégâts (test 4.6), commandes tactiles |
| v0.2 | Phase 2, brisures, agonie, états, pièges |
| v0.3 | Traque en vue 3/4 (5 points d'intérêt, jetons, horloge, météo) |
| v0.4 | E1, E2, E11, E12, qualité des matériaux, score |
| v0.5 Démo | Polish, 3 techniques, balance, test sur 3 appareils |
| v1.0 | Les 6 familles d'armes, les 4 modes de Mana, 5 ou 6 monstres supplémentaires, Poursuite, Nécessité et Prestige |
| v1.1 | Défense du Bastion, Corruption, 6 tables de météo, familiers complets |
| v2.0 | Chasses ◆◆◆◆ (monstres hors format, cinématiques de Dragons Anciens) |

---

## 15. Questions ouvertes pour krunt

1. **Modèle de dégâts (A, B ou C).** Recommandation : C (deux barres séparées) à confirmer par le test 4.6. Le modèle du Livre I (A) est fidèle mais crée une spirale de mort en temps réel.
2. **Quatre « joueurs » : coopération ou un seul héros ?** Le brief parle d'un jeu solo tactile ; le combat suppose **un héros et un familier**. Recommandation : les trois autres personnages deviennent des soutiens de camp (jetons, bonus) et non des combattants ; une vraie coopération à quatre doublerait le budget.
3. **Les fiches sont écrites pour 4 joueurs.** Recommandation : K = 20 comme point de départ et un mode « difficulté » (K de 15 à 30) ; ne pas modifier les livres.
4. **Dorgane mesure 70 px (hauteur).** Pour un premier boss, c'est très petit à côté d'un héros de 64 px. Recommandation : accepter 70 px comme « boss d'apprentissage » et jouer sur la meute et les cornes, ou adopter un facteur de lisibilité de 1,3 (91 px) pour tous les monstres.
5. **Phase 2 conditionnelle.** La fiche exige 50 % **et** un déclencheur. Recommandation : passage forcé à 30 %.
6. **Agonie de 1d4 rounds.** Recommandation : durée fixe de 8 s, pour que ce soit lisible et équitable.
7. **Endurance à 0 : « Persévérer » coûte une case de Vitalité.** Recommandation : oui, c'est la règle du livre, mais avec un feedback très visible.
8. **Jetons : information et fenêtre d'esquive.** Recommandation : oui ; l'Avantage de jet du Livre I n'a pas de sens sans d20.
9. **Score visible ou caché.** Recommandation : mention et 5 pastilles visibles, nombre caché ; l'Honneur numérique reste caché (livre) avec un glyphe de seuil.
10. **Corruption.** Aucune jauge définie. Recommandation : jauge 0 à 10 proposée en 3.6, reportée à la v1.1.
11. **Hors Combat et Blessures Persistantes.** Le livre dit que la mort n'est jamais mécanique et que trois cases non soignées donnent une séquelle permanente. Sur mobile, une perte permanente est frustrante. Recommandation : cicatrice cosmétique et case grise réparable à l'Infirmerie, pas de perte définitive.
12. **Noms anglais des armes (Livre X) et du compagnon-insecte du Glaive.** Recommandation : franciser (Hache-Épée, Lame Chargée existent déjà) et trouver un nom pour le compagnon.
13. **14 armes, 6 familles.** Recommandation : 3 armes dans la démo, 6 familles en v1.0 ; la famille F (Cor de Chasse) en dernier (animation, audio, interface différentes).
14. **Poursuite.** Précieuse (seule apparition de la plateforme dans une chasse) mais coûteuse. Recommandation : séquence scriptée de 2 segments en v1.0, hors démo.
15. **Techniques d'École.** 14 Écoles × 5 rangs = 70 techniques. Recommandation : jamais plus de 3 équipées, 1 mode de Mana dans la démo, les 14 Écoles échelonnées sur les versions.

---

## 16. Ponts avec les autres domaines

- **Retour au Clan** : reçoit `bilan_chasse` (qualité, brisures, contraintes, mention) ; calcule Honneur final, Récolte (Dépeceur), Récit, Rituel ; écrit Acte, Trace, Conséquence.
- **Bestiaire et roster** : exige un bloc `combat` par monstre (10.1) : stats du Livre III, zones, parties, seuils, jetons ; les JSON du roster n'en ont pas encore (le roster dit : « les statistiques de combat restent celles du Livre III »).
- **Écoles, Postures, Métiers, progression** : fournissent les techniques équipables, les paliers de compétence de Traque (lecture), les valeurs de jauges par niveau.
- **Forge, alchimie, équipement** : qualité des matériaux, bonus de série, recettes de combat, usure.
- **Bastion** : bâtiments qui agissent sur la Traque (Bibliothèque : 4e jeton ; Archives : faiblesse sans jeton ; Tour de Guet : pas de surprise) et sur la Défense du Bastion.
- **Dressage et familiers** : états Sauvage, Habituée, Dressée, vigueur, K.O.
- **Monde et exploration 3/4** : cartes de territoire, points d'intérêt, météo, Poursuite en plateforme, quêtes de plateforme.
- **Interface, audio, journal PocketBase** : HUD tactile, musique d'agonie, collections `chasse` et `evenement`.
