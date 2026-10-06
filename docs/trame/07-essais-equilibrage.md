# Essais d'équilibrage du combat : trois modèles de dégâts, quatre fiches, cinq adversaires

> **Rejeu v3 (2026-10-06).** La revalidation (`09`) relevait que ce document simulait le Taranis de `04` (AGI 12, Vitalité 9, bagage de 4 potions, piège et huile) et le Pascal en maille (Défense 19), alors que `08` a changé les attributs, la Vitalité, le bagage et l'armure. Le script `outils/simu_combat.py` a été mis à jour avec les fiches v2 (Taranis AGI 11 / END 6 / Vitalité 10, bagage de `08` ; Pascal cuir + bouclier, Défense 18) et **rejoué : voir §12**. Les tableaux des §3, §4 et §7 (Krunt3 seul, calibrage de K et de kd) ne dépendent pas de Taranis ni de Pascal et restent valables ; les tableaux qui les concernent (§1.2, §5 pour le kit « maille », §6) sont **corrigés ou annotés** ci-dessous, et les nouveaux chiffres sont au §12.

Rédigé le 2026-10-06 (Claude). Domaine : mesurer, par simulation réelle (Monte-Carlo, graine fixée), ce que valent les trois modèles de dégâts du chapitre `docs/mecaniques/01-chasse-et-combat.md` §4.5, si Krunt3 peut tenir la première ligne, pourquoi le chef de meute de la démo est « trivial » pour des fiches équilibrées, et avec quels réglages on obtient un combat de boss de 2 à 4 minutes en solo.

**Légende.** `LIVRE` = ce que disent les livres (numéro). `DOC` = ce que disent les documents du dépôt. `MESURÉ` = résultat de `outils/simu_combat.py` (reproductible). `INVENTÉ` = valeur d'équilibrage sans appui dans les livres, à confirmer au prototype. Aucun commit n'a été fait.

**Fichiers.** Script : `outils/simu_combat.py` (Python 3, bibliothèque standard, graine 20261006, paramètres en tête de fichier). Relancer : `python3 outils/simu_combat.py` (rapport complet ; 10 à 20 minutes à 600 tirages par cellule, les calibrations de kd en prennent la moitié ; `--n 150` : environ 4 minutes) ou `--sections echelle,livre,jeu,K,tank,leviers,variantes,competence,equiv,modeles`, `--n 300`, `--seed 7`. Tous les tableaux ci-dessous viennent d'une exécution à 600 tirages (1 000 pour la réconciliation du §3.3) ; les écarts statistiques sont de l'ordre de ± 4 points sur un pourcentage.

---

## 0. En bref

1. **Le chef de meute n'est pas « trivial » pour tout le monde : il l'est pour la table, mortel pour un héros seul, et K seul ne répare rien.** Aux chiffres bruts du Livre III, quatre héros l'abattent en 10 à 12 secondes avec 100 % de victoires ; un héros seul le perd dans 95 à 100 % des cas à l'échelle du Livre, et dure 12 à 20 s à l'échelle du jeu. Monter K (la Vitalité du monstre) allonge le combat mais le chef frappe plus longtemps : à K = 4 un héros seul ne gagne plus (1 à 2 %), à K = 20 plus jamais (§3.4).
2. **Il faut deux leviers, pas un** : K ≈ 20 sur la Vitalité (durée) **et** un coefficient de dégâts reçus kd ≈ 0,17 par-dessus le 0,65 du document 01, à tempo d'attaque égal (une action du chef toutes les 3,3 s). Autrement dit les dégâts reçus tombent à 0,11 PC par point de dégât du livre, soit une morsure déchirante de 1,4 PC (2,7 % de la Vitalité) au lieu de 9 PC. À pression égale on peut choisir moins de coups plus lourds : 5 s entre deux actions et 2,4 PC par morsure (§7.3, la table d'équivalence).
3. **La grandeur qui compte est la pression** : environ **5,3 cases (21 PC) de Vitalité perdues par minute** pour un joueur moyen (esquive 55 %) donnent 45 % de victoires à la première tentative et 2 min 24 s de combat, quel que soit le tempo choisi (E8). Cette valeur est le vrai paramètre de réglage, K et kd n'en sont que deux écritures.
4. **Les trois modèles à difficulté égale** (kd recalibré pour que Krunt3 seul gagne 45 % des premières tentatives) : le modèle A (Livre I) est une spirale par construction (100 % des défaites à Endurance sous 2) et récompense peu le savoir (3 Jetons : + 6 points) ; B (Livres II / IX) : spirale 56 %, + 14 points ; **C (deux barres) : spirale 35 à 39 % à 5 d'Endurance par round, 8 % à 8 (2 /s, la valeur du document 01), + 19 points**. C est le meilleur sur les trois critères ; A reste jouable seulement avec un tampon d'Endurance qui se régénère (kd 4 fois plus haut).
5. **Krunt3 ne peut pas tenir la première ligne** avec la Double Lame et le cuir, dans aucun des trois modèles : avec Provocation il encaisse 26 à 58 % des coups (au lieu de 22 à 25 %) mais tombe dans 95 à 100 % des combats de 2 minutes, et la victoire de l'équipe baisse (75 % sans tank, 64 % avec Provocation, 43 % avec Provocation, Mur de Chair et Interposition, modèle C). **Avec Épée et Bouclier et maille (garde de 60 %), il tient** : en duo avec Cyril, 94 % de victoires contre 12 % (§5). *(Rejeu v3, §12 : la maille n'est pas disponible à la création ; avec cuir + bouclier, 85 % contre 12 %. Le kit de tank est celui de Pascal, `04` §4.5.)*
6. **Les fiches équilibrées diffèrent d'un facteur 2 en dégâts** (21,6 contre 10,8 par round) : avec un K unique de 20, Krunt3 gagne un combat de 2 min 24 s à 44 à 63 % et Pascal « attaque de base seule » ne gagne jamais (0 %). Il faut un K propre à chaque personnage en solo (Krunt3 20, Taranis 18, Cyril 16, Pascal 10), ou un kit offensif pour Pascal.
7. **Deux déséquilibres que les essais mettent au jour** : le **soin de Cyril** (Vitalité + 1 case pour 2 Mana, Mana gagné en frappant) la rend quasi invulnérable en solo (100 % de victoires à K = 20) ; à 4 Mana, 77 %. **Taranis** (fiche d'origine) infligeait 35 à 38 % des dégâts de la table (parts Krunt3 / Taranis / Cyril / Pascal : 24 / 35 / 23 / 18 % à K = 1), grâce à *Tir Ciblé* (Exposé), au *Flanc Coordonné* et à l'huile de son bagage ; **avec la fiche v2 (rejeu v3, §12), il tombe à 29 à 30 % et n'est plus le premier des dégâts** ; en solo, 41 % de victoires avec le bagage v3 contre 12 % sans les Herbes.
8. **Le seuil « 3 à 7 cases perdues par victoire » du document 01 §4.6 est incompatible avec 35 à 50 % de victoires** : un combat qui se gagne à 45 % se gagne avec 1 à 3 cases restantes (10 à 12 cases perdues sur 13). À proposer : mesurer à la place **la Vitalité restante** et **les cases perdues par minute**.
9. **Rien ici n'est une preuve** : ce sont des simulations en temps abstrait, avec une IA de héros simple et un joueur « moyen » à probabilité d'esquive constante. Elles donnent l'ordre de grandeur de K, kd et du tempo, et classent les modèles ; les valeurs finales viendront des tests à la main (§9). Limites au §10.

---

## 1. Méthode

### 1.1 Ce qui est simulé

| Élément | Règle | Source |
|---|---|---|
| Temps | 1 round = 4 s ; les héros agissent par ordre d'Initiative (18, 15, 15, 12), puis les monstres ; plafond de 150 rounds (10 min) | consigne ; l'ordre d'Initiative du monstre n'est pas simulé |
| Touche des héros, échelle « Livre » | d20 + bonus d'attaque (13, 16, 9, 10, soit `04` §6.3) contre la Défense du monstre ; 1 naturel = échec, 20 = critique (dés doublés) ; dégâts = dé de l'arme (Livre IX) ; 1 Acte par round | LIVRE I ch. 7 |
| Touche des héros, échelle « jeu » | 2,4 touches utiles par round (0,6 /s) ; dégâts = (dé moyen + qualité + FOR ou AGI / 4) x dureté `clamp(1 + (10 − Défense) x 0,04 ; 0,35 ; 1,3)` ; Exposé x 1,25 | DOC 01 §4.3, §12 |
| Touche des monstres, échelle « Livre » | d20 + (attribut principal + CR / 2) contre Défense avec armure ; la Riposte (1 End, une par round) ajoute l'AGI à la Défense | LIVRE I ; `+ CR / 2` INVENTÉ |
| Touche des monstres, échelle « jeu » | toute attaque non évitée touche ; esquive minutée : 2 End, réussite de probabilité 0,55 + 0,02 x (AGI − 8) pour un joueur moyen ; Pascal pare avec son bouclier (70 % des coups, − 60 %, 1 End par 2 PC bloqués) ; dégâts du livre x 0,65 x kd, puis / 4 (cases), armure − 5 % par CA (max 35 %) | DOC 01 §3.2, §4.3, §12 ; kd INVENTÉ |
| Endurance | 10 ; régénération 5 par round (≈ 1,25 /s) en jeu, 0 en échelle Livre ; Techniques de Posture 2 End ; potion de soin + 7 | DOC 01 §3.2 (2 /s après 0,8 s, ramené à 5 par round : dérivé prudent) |
| Modèle A | l'Endurance absorbe d'abord, le reste va à la Vitalité | LIVRE I ch. 2 et 7 |
| Modèle B | dégâts directs sur la Vitalité ; chaque touche coûte de l'Endurance (1 par Acte en échelle Livre, 0,4 par touche en jeu, INVENTÉ) ; à Endurance 0, l'action coûte 1 case de Vitalité | LIVRE II ch. 2 §6, IX ; DOC 01 §3.2 |
| Modèle C | dégâts directs sur la Vitalité ; l'Endurance ne sert que d'esquive, de garde et de techniques ; à 0, plus d'esquive | DOC 01 §4.3 |
| Monstres | Vitalité, Défense, attributs, phases et attaques du Livre III (copiés) ; poids de choix des attaques INVENTÉS ; agonie du chef 2 rounds (DOC 01 §5.7 : 8 s ; LIVRE III : 1d4 rounds) | LIVRE III section V |
| Tank | Provocation (cible prioritaire avec une probabilité de 0,8, INVENTÉ), Mur de Chair (− 2 dégâts aux alliés au contact), Interposition (reçoit le coup d'un allié ; une chance sur deux d'être placé pour, INVENTÉ) ; 2 End chacune | LIVRE VI ch. 4 (lignes 390 à 393) |
| Loups | *Flanc Coordonné* : + d6 si un allié a frappé la même cible ce round, 2 End ; au plus un bonus par cible et par round | LIVRE VI ; limite `04` §7.3 |
| Joueur à la première tentative | population d'esquive 35 / 45 / 55 / 65 / 75 % de poids 15 / 30 / 30 / 20 / 5 % ; 3 Jetons de Connaissance = + 7 points d'esquive | INVENTÉ (DOC 01 §3.2 pour le principe) |

« Victoire » = le boss est mort (agonie comprise) ; pour 4 éclaireurs seuls, la meute fuit quand la moitié est hors combat (LIVRE III). « Défaite » = tous les héros à 0 Vitalité. « ≥ 1 à terre » = au moins un héros à 0.

### 1.2 Les quatre fiches (document 04 §4 et §6.3, avec les corrections de krunt)

| | Krunt3 | Taranis | Cyril | Pascal |
|---|---|---|---|---|
| Attributs finaux (FOR / AGI / END) | 9 / 8 / 9 | 5 / **11** / **6** (v2 ; était 5 / 12 / 5) | 5 / 6 / 6 | 7 / 6 / 8 |
| Vitalité (cases / PC) | 13 / 52 | **10 / 40** (v2 ; était 9 / 36) | 10 / 40 | 12 / 48 |
| Défense avec armure ; CA | 19 ; 2 (cuir) | 19 ; 2 (cuir) | 13 ; 1 | **18 ; 4 (cuir + bouclier)** (v2 ; était 19 ; 5, maille + bouclier : la maille exige un forgeron de niveau 8-15 [L Livre VIII]) |
| Bonus d'attaque ; arme | 13 ; Double Lame 1d6+1d6 | **15** (v2 ; était 16) ; Arc 1d8 | 9 ; Épée Longue 1d8 | 10 ; Épée et Bouclier 1d6 |
| Dégâts par touche (jeu) | 9,0 | 7,5 | 5,5 | 4,5 |
| Mana ; mode | 6 ; Flux | 6 ; Rituel | 8 ; Flux | 6 ; Ancrage |
| Posture | Ours (Provocation, Mur de Chair, Interposition) | Loup | Loup | Loup |
| Spécificités simulées | Provocation selon le test ; Souffle du Réceptacle (variante) | *Tir Ciblé* (2 Mana, Exposé), **bagage de départ** | Soin de Vitalité + 1 case (2 Mana) ; *Présence Rassurante* | **attaque de base seule** (correction de krunt) |
| Potions de soin (Endurance + 7) | 2 | 2 (v2 ; était 4, bagage) **+ 2 Herbes Stabilisantes** (+2 cases de Vitalité) | 2 | 3 (alchimiste) |

**Bagage de départ de Taranis, version v3 (`08` §4)** : ni piège à colle ni huile de feu ; 2 Herbes Stabilisantes (+2 cases de Vitalité sous 50 % de Vitalité) en plus des 2 potions de base. *(Version d'origine de ce document, INVENTÉE et remplacée : 4 potions de soin, 1 Piège à Colle posé avant le combat, 1 Huile de Feu.)* **Pascal, attaque de base seule** : variantes « soutien » (Garde Haute, 3 Herbes Stabilisantes + 2 Vitalité) et « bombe » (3 bombes de feu 2d6, niveau 5) comparées au §6.

### 1.3 Les adversaires (LIVRE III, section V ; ids de `donnees/monstres/crochues.json`)

Les noms du Livre III (Velodrak, Velokrak, Garuvorn…) sont les anciens noms de travail ; le roster porte Dorgane (`cro02`), Alizade (`cro01`), Balafrette (`cro17`), Delirande (`cro18`). La fiche du chef est à la section V du Livre III, lignes 326 à 370 du fichier (la ligne 227 de la consigne tombe dans l'en-tête et le portrait de la fiche, lignes 225 à 240).

| Adversaire | Rang, CR | Vitalité | Défense | Attaques principales | Phases |
|---|---|---|---|---|---|
| **Éclaireur** (`cro01`, x 4) | ◆, 1 | 6 | 7 | Morsure 1d4+3 ; Griffes 1d4+5 ; Charge en coin 2d4+3 (3 ou plus) | 1 |
| **Chef de meute** (`cro02`) | ◆◆, 4 | 27 | 11 | Morsure 2d6+7 (Saignée) ; Queue 1d8+7 ; Charge 2d8+7 ; Vocalisation ; Phase 2 : Déluge 3 x (1d6+7), Morsure 3d6+7, Charge x 2 | 2 (50 %, déclencheur) |
| **Élite** (`cro17`, Garuvorn) | ◆◆◆, 12 | 58 | 19 | Charge 3d8+13 ; Morsure 2d8+13 + venin 3 /round ; Queue 2d6+13 ; Frénésie 4 x (1d8+13) | 3 (65 %, 30 %) |
| **Légendaire** (`cro18`, Garuvorn Sourd) | ◆◆◆◆, 18 | 79 | 21 | comme l'élite avec FOR 16, **2 attaques par action** ; Frénésie totale ; agonie 1d6 rounds | 2 (40 %) |

Échelle des fiches pour mémoire (Livre III, mesuré sur le fichier) : Vitalité 6 (CR 1), 20 à 36 (CR 4), 58 à 76 (CR 12), 88 à 96 (CR 16), 120 à 220 (CR 19 à 24, dont les Dragons). Le Garuvorn Sourd (79) est en dessous des autres légendaires.

Les héros affrontent les éclaireurs et le chef au **palier 0** (rang I, début de campagne), l'élite au **palier 2** (50 % de l'histoire : rang III, + 4 points d'attribut, qualité + 1, CA + 1) et le légendaire au **palier 4** (100 % : rang V, + 7 points, qualité + 2, CA + 2), selon `04` §5.3. Le palier est INVENTÉ dans le détail.

---

## 2. Ce que les livres et les documents disent déjà (rappel)

- Le document 01 §4.1 annonce le problème : fiches écrites pour quatre joueurs au tour par tour, donc un coefficient K sur la Vitalité (K = 20 chef, 4 meute) et un facteur 0,65 sur les dégâts reçus.
- Le document 04 §6.2 mesure le chef à 1,4 à 1,8 round, 0 % de héros à terre, et signale que « le modèle de dégâts du Livre I ne donne aucun rôle de tank » (§6.4 point 1). Les essais ci-dessous confirment le diagnostic et le chiffrent.
- Le document 01 §12 prévoit ◆◆ en 5 à 8 minutes ; la consigne de cette tâche demande 2 à 4 minutes en solo pour le boss de la démo. Les deux ne sont compatibles qu'en distinguant le combat entier (2 à 4 min) de la phase 1 (le critère 4.6 parle de la phase 1 seule). **À trancher** (§11).

---

## 3. Le problème d'échelle, avec des chiffres

### 3.1 Calcul direct (E0 : aucun tirage)

| Héros | Dégâts par touche | par round de 4 s (2,4 touches) | par seconde | Vitalité |
|---|---|---|---|---|
| Krunt3 | 9,0 | 21,6 | 5,4 | 13 cases = 52 PC |
| Taranis | 7,5 | 18,0 | 4,5 | 9 = 36 PC |
| Cyril | 5,5 | 13,2 | 3,3 | 10 = 40 PC |
| Pascal | 4,5 | 10,8 | 2,7 | 12 = 48 PC |

Touches nécessaires pour abattre la créature aux chiffres bruts (K = 1), dureté de zone comprise :

| Cible | Vitalité | Défense | Dureté | Krunt3 | Taranis | Cyril | Pascal |
|---|---|---|---|---|---|---|---|
| un éclaireur | 6 | 7 | 1,12 | 1 | 1 | 1 | 2 |
| **chef de meute** | 27 | 11 | 0,96 | **4** | 4 | 6 | 7 |
| élite CR 12 (héros palier 2) | 58 | 19 | 0,64 | 10 | 11 | 14 | 14 |
| légendaire CR 18 (palier 2 ici) | 79 | 21 | 0,56 | 15 | 17 | 22 | 22 |

**Pourquoi le chef est « trivial » pour la table.** Sa Vitalité de 27 vaut 4 à 7 touches d'un héros. Quatre héros qui touchent à 0,6 /s l'abattent en **1,8 s de calcul pur**, **10 à 12 s en pratique** (agonie de 2 rounds, premiers coups à manquer). Le Livre III écrit « 27 » pour un monde où un dé d8 inflige 4,5 : le rapport Vitalité sur dégâts par touche est de **6** (27 / 4,5), donc 1,5 round à quatre ; la cible de 2 à 4 minutes (30 à 60 rounds de 4 s) demande un rapport de **100 à 200** en solo.

**Le facteur d'échelle est 16, pas 4.** Un héros seul n'a que le quart des dégâts de la table (x 4 de durée) et que le quart de la réserve de Vitalité (le monstre concentre tous ses coups sur lui). Les deux effets se multiplient : à l'échelle du Livre, le chef contre un héros seul tue en 2 à 4 rounds (95 à 98 % de défaites), contre quatre il meurt en 3 rounds.

**Le monstre grandit plus vite que le héros.** De CR 1 à CR 18, la Vitalité du livre monte de 6 à 79 (x 13) alors que les dégâts d'une touche de héros ne montent que de 4,5 à 9 à 12 aux paliers 2 à 4 (x 2 à 2,5) : les touches à porter passent de 1 à 15 / 22, donc le combat à K = 1 passe de 1 à 5 rounds pour quatre héros. Les dégâts des monstres suivent : morsure du chef 14 (Vitalité du héros 13, rapport 1,1), élite 26,5 (rapport 1,8 pour un héros de palier 2, Vitalité 15), légendaire 29,5 en deux attaques par action (rapport 3,5 par action pour un héros de palier 4, Vitalité 17). **Aucune règle du livre ne fait croître la Vitalité du héros comme le monstre** : Livre X ch. 13 la fait passer de 12 à 26 en 30 niveaux, mais la campagne ne va qu'à 15 ou 16 (`04` §5.3).

### 3.2 Échelle « Livre », K = 1 (E1)

| Configuration | Scénario | Modèle A | Modèle B | Modèle C |
|---|---|---|---|---|
| **Krunt3 seul** | chef + 4 éclaireurs | 3 % de victoires, 16 s | 0 %, 8 s | 2 %, 8 s |
| Taranis seul | idem | 5 %, 16 s | 2 %, 8 s | 2 %, 8 s |
| Cyril seul / Pascal seul | idem | 0 % | 0 % | 0 % |
| Krunt3 seul | élite / légendaire | 0 % / 0 % | 0 % / 0 % | 0 % / 0 % |
| Duo Krunt3 + Cyril | chef + 4 éclaireurs | 13 %, 24 s | 5 %, 16 s | 5 %, 16 s |
| **Table (4 héros)** | chef seul | 100 %, 12 s | 100 %, 12 s | 100 %, 12 s |
| Table | chef + 4 éclaireurs | 100 %, 16 s | 98 %, 16 s | 98 %, 16 s |
| Table | élite CR 12 | 92 %, 12 s | 88 %, 12 s | 91 %, 12 s |
| Table | légendaire CR 18 | 1 % | 0 % | 0 % |

La table gagne le chef à 100 % sans l'ombre d'un risque de défaite, mais **pas sans risque individuel** : « au moins un héros à terre » 66 à 73 % avec les éclaireurs (Krunt3, qui tient le rôle de tank, perd en moyenne 9 à 10 cases sur 13, les trois autres 0,4 à 3). L'élite se gagne encore à 90 %, le légendaire jamais : à CR 18 les héros du palier 4 (Vitalité 13 à 17) tombent en un ou deux coups de 29.

**Réconciliation avec le document 04 §6.2** (chef seul, quatre héros, modèle A, K = 1, 1 000 tirages) :

| Cas | Victoire | Durée moyenne | ≥ 1 à terre |
|---|---|---|---|
| sans tank, sans agonie ni phases (équivalent du document 04) | 100 % | 1,6 round | **0 %** |
| sans tank, agonie de 2 rounds | 100 % | 2,6 rounds (10 s) | 36 % |
| tank joué, agonie de 2 rounds | 100 % | 2,6 rounds | 35 % |

Le « 0 % de personnage à terre » du document 04 vient de l'oubli de l'agonie du chef (LIVRE III : 1d4 rounds à pleine capacité ; DOC 01 : 8 s) ; avec elle un héros sur trois tombe. Le fond (trivial, 100 % de victoires) ne change pas.

**Ce qu'il faudrait de K à la table (échelle Livre, modèle A, K_meute = 1)** :

| K | chef + éclaireurs : victoire / durée / ≥ 1 à terre | élite : victoire / durée |
|---|---|---|
| 1 | 100 % / 16 s / 66 % | 93 % / 12 s |
| 2 | 98 % / 24 s / 80 % | 27 % / 28 s |
| 3 | 92 % / 28 s / 86 % | 2 % / 32 s |
| 4 | 81 % / 36 s / 91 % | 0 % |
| 6 | 51 % / 48 s / 97 % | 0 % |

À la table, K = 2 à 4 donne un combat de 6 à 9 rounds et 80 à 98 % de victoires pour le chef, mais **l'élite est déjà infranchissable à K = 2** : à CR 12 il faut baisser les dégâts reçus, pas monter la Vitalité (voir §7.4).

### 3.3 Échelle « jeu » sans correction, K = 1 (E2)

| Héros | chef seul | chef + éclaireurs |
|---|---|---|
| Krunt3 | 66 % de victoires, 12 s | 42 %, 20 s |
| Taranis | 81 %, 12 s | 40 %, 16 s |
| Cyril | 17 %, 12 s | 5 %, 24 s |
| Pascal | 38 %, 16 s | 4 %, 24 s |
| Krunt3 + Cyril | 100 %, 8 s | 100 %, 16 s |
| 4 héros | 100 %, 8 s | 100 %, 8 s |

À K = 1 le combat dure **8 à 24 secondes** : 5 à 10 % de la cible, et Krunt3 seul perd tout de même 10 à 11 cases sur 13 pendant ce temps (le chef frappe 1,6 fois par round avec des coups de 9 PC pour 52 PC de Vitalité).

### 3.4 K seul ne suffit pas (E3a)

Échelle jeu du document 01 (facteur 0,65, une attaque toutes les 2,5 s), modèle C, chef + éclaireurs (K_meute = K / 5), joueur moyen. Victoire / durée médiane :

| K | Krunt3 | Taranis | Cyril | Pascal |
|---|---|---|---|---|
| 1 | 39 % / 20 s | 39 % / 16 s | 4 % / 24 s | 3 % / 24 s |
| 2 | 16 % / 20 s | 19 % / 20 s | 1 % / 28 s | 0 % / 24 s |
| 4 | 1 % / 28 s | 2 % / 24 s | 0 % | 0 % |
| 8 | 0 % / 32 s | 0 % / 28 s | 0 % | 0 % |
| 20 | 0 % / 28 s | 0 % / 28 s | 0 % / 16 s | 0 % / 20 s |

(La durée affichée à K élevé est celle de la défaite, pas du combat visé.) **Le héros n'a pas le temps de tuer un chef à K = 20 : il meurt en 28 s.** La perte de Vitalité est de 53 cases par minute à K = 1 et 21 à K = 20 contre une cible de 5. **Un K de 20 sans autre correction fait de la démo un mur.** Le document 01 §12 le sait (« 90 PC en 5 min contre 40 PC de Vitalité, il faut des soins ») sans le chiffrer : le calcul de contrôle prévoit 22 cases perdues en 5 minutes, soit 4 à 5 fois la cible de 3 à 7.

---

## 4. Les trois modèles de dégâts comparés

### 4.1 À difficulté égale (E9 : Krunt3 seul, K = 20, chef + éclaireurs, kd recalibré pour 45 % à la première tentative)

| Modèle | kd calibré | 1re tentative | avec 3 Jetons | Durée médiane | Vit. perdue par minute | **Spirale** (défaites à Endurance < 2) | Temps sans esquive |
|---|---|---|---|---|---|---|---|
| A (Livre I) | 0,669 | 47 % | 53 % (+ 6) | 2 min 24 s | 4,8 | **100 %** | 33 % |
| B (Livres II / IX) | 0,160 | 47 % | 61 % (+ 14) | 2 min 24 s | 5,2 | 56 % | 27 % |
| **C (deux barres)** | 0,170 | 45 % | **64 % (+ 19)** | 2 min 24 s | 5,2 | **39 %** | **17 %** |

Lectures :

- **A absorbe presque tout tant que l'Endurance se régénère** : il lui faut un kd 4 fois plus haut pour la même difficulté (0,67 contre 0,17). Sans régénération (échelle Livre) il n'y a pas de combat : 2 coups de chef vident 23 points. Il peut être retenu **seulement** comme « tampon régénérant » (le repli du document 01 §4.6) ; la spirale est alors 100 % par construction, puisqu'on ne tombe qu'à Endurance 0.
- **B est jouable** mais l'attaque qui coûte de l'Endurance ajoute des moments où l'on ne peut plus esquiver (27 % du temps) et rend le Hors Combat plus fréquent à Endurance basse.
- **C est le seul où la connaissance (Jetons, + 7 points d'esquive) change nettement l'issue** (+ 19 points contre + 6 pour A), ce que le document 01 veut obtenir. Il manque 14 points pour passer le critère « spirale < 25 % ».

### 4.2 Le seuil de spirale dépend de la régénération (E9, modèle C)

| Régénération d'Endurance par round de 4 s | kd calibré | Spirale | Temps sans esquive |
|---|---|---|---|
| 3,0 (0,75 /s) | 0,149 | 76 % | 36 % |
| **5,0 (1,25 /s)** (valeur des tableaux) | 0,172 | 35 % | 16 % |
| **6,5 (1,6 /s)** | 0,178 | **15 %** | 10 % |
| 8,0 (2 /s, document 01) | 0,176 | 8 % | 7 % |

**Le document 01 §3.2 (2 points par seconde après 0,8 s sans dépense) passe le critère** ; mon réglage de 5 par round est volontairement prudent. Recommandation : **2 /s, délai de 0,8 s**, soit 6,5 à 8 par round de 4 s.

### 4.3 À l'échelle du Livre (K = 1, quatre héros, chef + éclaireurs)

| | A | B | C |
|---|---|---|---|
| Victoire | 100 % | 98 % | 98 % |
| ≥ 1 héros à terre | 66 % | 71 % | 73 % |
| Endurance dépensée par Krunt3 | 13,7 | 12,0 | 9,7 |
| Vitalité perdue par Krunt3 | 9,3 | 8,5 | 9,9 |

Les trois modèles se valent quand le combat dure 4 rounds ; leurs différences ne comptent que dans les combats longs (§4.1). **Le choix du modèle est donc un choix de combat solo en temps réel**, pas de table.

### 4.4 Verdict

**Retenir le modèle C** (deux barres, esquive et garde payées en Endurance, Persévérer à 1 case), avec régénération de 2 /s. Mettre à la table le modèle A (le Livre I) ne coûte rien puisque les combats sont courts. Le protocole 4.6 du document 01 (trois builds A, B, C) reste à exécuter, mais les résultats ci-dessus indiquent d'écarter A et B sauf mauvaise surprise : le test coûte alors surtout du temps.

---

## 5. Krunt3 peut-il tenir la première ligne ?

**Réponse courte : non avec Double Lame et cuir, oui avec bouclier et maille, et jamais « gratuitement » dans les modèles A et B.**

### 5.1 Échelle Livre (E4a, K = 1, quatre héros)

| Scénario | Modèle | Tank joué | Part des coups sur Krunt3 | Krunt3 à terre | un autre à terre (par héros) | ≥ 1 à terre | Victoire |
|---|---|---|---|---|---|---|---|
| chef + éclaireurs | A | oui | 63 % | 59 % | 11 % | 65 % | 100 % |
| chef + éclaireurs | A | non | 25 % | 15 % | 24 % | 64 % | 100 % |
| chef + éclaireurs | C | oui | 61 % | 64 % | 19 % | 74 % | 98 % |
| chef + éclaireurs | C | non | 27 % | 29 % | 35 % | 79 % | 98 % |
| élite CR 12 | A | oui | 54 % | 85 % | 25 % | 89 % | 94 % |
| élite CR 12 | A | non | 30 % | 42 % | 41 % | 87 % | 93 % |
| élite CR 12 | C | oui | 49 % | 90 % | 32 % | 92 % | 90 % |
| élite CR 12 | C | non | 30 % | 52 % | 42 % | 89 % | 89 % |

Le tank **déplace** les coups (25 % à 60 % des coups sur Krunt3) et **protège un peu les autres** (24 % à 11 % de chances de tomber), mais il **ne diminue pas le risque global** (≥ 1 à terre : 64 à 65 % contre 65 %) ni ne gagne plus de combats : Krunt3 tombe presque trois fois sur cinq au lieu d'une sur sept. C'est la conclusion du document 04 (« pas de rôle de tank dans le modèle du Livre I »), qui s'étend aux modèles B et C à l'échelle du Livre.

### 5.2 Échelle jeu, à difficulté égale (E4b : kd calibré sans tank pour 75 % de victoires de la table, K = 60, chef + éclaireurs)

| Modèle | kd | Kit de Krunt3 | Tank | Part des coups | Krunt3 à terre | autre à terre (par héros) | ≥ 1 à terre | Victoire |
|---|---|---|---|---|---|---|---|---|
| A | 1,49 | base | aucun | 24 % | 7 % | 15 % | 35 % | 97 % |
| A | 1,49 | base | Provocation | 26 % | 99 % | 50 % | 99 % | 62 % |
| A | 1,49 | base | complet | 20 % | 100 % | 61 % | 100 % | 51 % |
| B | 0,82 | base | aucun | 22 % | 45 % | 45 % | 70 % | 73 % |
| B | 0,82 | base | Provocation | 32 % | 99 % | 61 % | 99 % | 52 % |
| B | 0,82 | base | complet | 31 % | 100 % | 82 % | 100 % | 26 % |
| **C** | 0,83 | base | aucun | 22 % | 45 % | 45 % | 72 % | **75 %** |
| **C** | 0,83 | base | Provocation | 34 % | **99 %** | 49 % | 99 % | **64 %** |
| **C** | 0,83 | base | complet | 31 % | 100 % | 68 % | 100 % | **43 %** |
| C | 0,83 | plaques (CA 4) | aucun / Provocation / complet | 24 / 40 / 34 % | 35 / 95 / 100 % | 38 / 37 / 60 % | 62 / 95 / 100 % | 80 / 73 / 52 % |
| C | 0,83 | **bouclier + maille** | aucun | 38 % | 55 % | 55 % | 78 % | 62 % |
| C | 0,83 | **bouclier + maille** | Provocation | **58 %** | 95 % | 36 % | 95 % | **76 %** |
| C | 0,83 | bouclier + maille | complet | 53 % | 99 % | 46 % | 99 % | 66 % |

(« complet » = Provocation + Mur de Chair + Interposition ; kd élevé parce que la table fait 3 fois les dégâts d'un héros seul.)

- **Avec le kit de base, jouer le tank est une erreur** : Krunt3 tombe dans 99 à 100 % des combats, la victoire baisse de 11 points (Provocation) à 32 points (complet). Raison : Provocation + Mur de Chair + Interposition coûtent jusqu'à 6 Endurance par round, davantage que la régénération, donc plus d'esquive après deux rounds ; et les coups qu'il attire (34 à 58 %) tombent sur 13 cases de Vitalité, comme un autre héros.
- **Avec Épée et Bouclier et maille** (garde de 60 %, CA 5), le tank paie : victoire 76 % avec Provocation contre 62 % sans tank avec le même kit (**+ 14 points**), et contre 75 % pour l'équipe de base sans tank. Mais **Krunt3 tombe encore 95 % du temps** : il prend 58 % des coups pendant 2 minutes. Il « tient » le temps d'une phase, pas d'un combat.
- **En duo avec Cyril (E4d, kd calibré sans tank pour 75 %)** : kit de base **12 % de victoires** (Krunt3 à terre 98 %, Cyril 88 %) ; kit bouclier **94 %** (Krunt3 à terre 14 %, Cyril 6 %). Avec un soigneur derrière lui, la garde fait la différence.
- **Contre l'élite (E4c, K = 40)**, même constat : base, Provocation 70 % contre 71 % sans tank, complet 27 % ; bouclier, Provocation 70 % contre 62 % sans.

### 5.3 Recommandations pour Krunt3 (à décider, §11)

1. **Ne pas lui donner le rôle de tank avec la Double Lame.** Rôle de jeu réaliste : **fer de lance** (dégâts maximaux par touche, 20 à 24 % des dégâts à la table, Vitalité 13), Provocation limitée à une utilisation de Posture ponctuelle (relancer l'attention du chef quand un autre héros est à moins de 30 % de Vitalité), pas à chaque round.
2. **Si krunt veut un vrai tank** : changer le kit (le sprite de Krunt3 est de toute façon à refaire, `00-decisions.md`) en **Épée et Bouclier** + armure de maille, c'est-à-dire l'École Gardien Mobile, qui est celle que `04` §3.1 donne à Pascal. Il faudrait alors trouver une autre école ou un autre rôle à Pascal. **Ours + Danse Rouge** est classé « tension créative » (LIVRE VI ch. 13 §5) : la simulation donne une raison mécanique à la tension.
3. **Valeurs de départ pour le prototype** : probabilité de cible prioritaire de Provocation 0,5 au lieu de 0,8 (non testé : la sensibilité à P_PROVOC est à mesurer), Mur de Chair et Interposition sans combinaison (ils épuisent l'Endurance).
4. **Mur de Chair** réduit de 2 les dégâts aux alliés, ce qui vaut 14 % d'une morsure de 14 : ce n'est pas le levier.

---

## 6. Rôles, parts de dégâts, corrections de krunt

### 6.1 Parts des dégâts (E6)

| Échelle, variante | Krunt3 / Taranis / Cyril / Pascal | ≥ 1 à terre | Victoire |
|---|---|---|---|
| Livre K = 1, **référence** (bagage, Pascal « base ») | **24 % / 35 % / 23 % / 18 %** | 67 % | 100 % |
| Livre K = 1, sans bagage de Taranis | 23 / 29 / 25 / 23 % | 76 % | 96 % |
| Livre K = 1, Pascal « soutien » | 24 / 35 / 23 / 18 % | 62 % | 100 % |
| Livre K = 1, Pascal « bombe » | 21 / 30 / 20 / **29 %** | 60 % | 100 % |
| Livre K = 1, *Flanc Coordonné* cumulable | 23 / 34 / 23 / 20 % | 58 % | 100 % |
| Livre K = 3, référence | 18 / 37 / 24 / 21 % | 84 % | 93 % |
| Livre K = 3, sans bagage de Taranis | 18 / 30 / 26 / 26 % | 89 % | 78 % |
| Livre K = 3, Pascal « bombe » | 16 / 30 / 21 / 33 % | 78 % | 97 % |
| Jeu K = 60, kd 0,15, référence | 20 / **38** / 24 / 17 % | 0 % | 100 % |
| Jeu K = 60, sans bagage | 22 / 32 / 26 / 19 % | 0 % | 100 % |

- **[Obsolète, voir §12] Taranis (fiche d'origine) est le premier dégâts de la table (35 à 38 %)** alors que sa part théorique est de 29 % (4,5 /s sur 15,9) : *Tir Ciblé* met la cible en Exposé (x 1,25 pour tous), le *Flanc Coordonné* ajoute un d6 à ses tirs et à ceux des autres Loups, l'huile de feu ajoute 2,5. Sans bagage il redescend à 29 à 32 %. Le document 04 §6.4 point 3 voulait « surveiller » : c'est mesuré. Pas de correction nécessaire tant qu'il reste la fiche la plus fragile (Vitalité 9, Mana 6 en Rituel : *Tir Ciblé* 3 fois par combat).
- **Pascal « base » est le dernier (17 à 18 %)**, ce qui est voulu (rempart) ; ses bombes à 3 charges le montent à 29 à 33 %.
- ***Flanc Coordonné* cumulable** ne change presque pas les parts de dégâts et réduit un peu le risque (« ≥ 1 à terre » 58 % contre 67 % à K = 1) : la meute tombe plus vite. La limite du document 04 §7.3 ne se justifie pas par cette simulation : à garder pour la lisibilité plus que pour l'équilibre.

### 6.2 Taranis avec son bagage (solo, E3c et E6)

> **Obsolète pour la fiche v2 : voir §12.** Le tableau ci-dessous mesure l'ancien bagage (4 potions, piège, huile). Le rejeu v3 (2 Herbes Stabilisantes, ni piège ni huile) donne 41 % de victoire à la première tentative avec le bagage et 12 % sans, à K = 20 et kd 0,15.

| | Taranis avec bagage | sans bagage |
|---|---|---|
| Victoire à la 1re tentative (K = 20, kd 0,15, chef + éclaireurs) | **39 %** | **18 %** |
| Durée médiane | 2 min 08 s | 2 min 44 s |

Le bagage d'origine (4 potions, piège, huile) valait **21 points de victoire** en solo : il fait de Taranis un personnage qui ne souffre pas au départ, ce que krunt a demandé. *(Conclusion remplacée par le rejeu v3 : les 2 Herbes valent environ 29 points de victoire en solo, à ± 6 points ; c'est un soin de Vitalité à surveiller.)* À garder comme **bagage à usage unique par chasse** (les consommables se reconstituent au camp).

### 6.3 Pascal sans bombes (solo, E3c et E3d)

| Variante | K pour 85 à 100 % de victoires à la 1re tentative | Durée |
|---|---|---|
| **« base » (attaque seule)** | **K = 10** (87 % ; à K = 14 : 11 %) | 2 min 20 s |
| « soutien » (Garde Haute, Herbes) | K = 14 (99 %) ; à K = 20 : 11 % | 3 min 12 s |
| « bombe » (3 bombes de feu) | K = 12 (55 %) | 2 min 32 s |

À K = 20, Pascal « base » ne gagne **jamais** (0 %). **L'attaque de base seule est trop faible pour porter un combat de 2 minutes contre un chef de K = 20** : il dure le double de Krunt3 (2,7 contre 5,4 de dégâts par seconde) et son armure ne compense pas. Deux voies : un K propre à chaque personnage en solo (K_perso, §8) ou un petit kit offensif à Pascal (3 bombes au niveau 1 : le document 04 §6.4 point 4 le proposait, la correction de krunt l'écarte).

### 6.4 Cyril : le soin est trop efficace (E3c, E3d, E6)

| | Victoire 1re tentative | Durée | Vit. perdue brute (cases, victoires) |
|---|---|---|---|
| Soin 2 Mana, K = 20 | **100 %** | 4 min 32 s | 24,5 (au moins 14 soins pour une Vitalité de 10) |
| Soin 4 Mana, K = 20 | 77 % | 4 min 24 s | – |
| Soin 4 Mana, K = 16 | 88 % (94 % avec Jetons) | 3 min 32 s | 17,9 |

Le *Flux* rend 1 Mana par touche réussie (DOC 01 §3.5) ; avec 2,4 touches par round, Cyril gagne plus de Mana qu'elle n'en dépense et se soigne d'1 case par round. Cyril **ne perd jamais** : c'est un défaut de réglage, pas un trait de rôle. Proposition : soin à **4 Mana** ou, équivalent, gain de Mana du Flux plafonné à 1 par seconde et soin à 3 Mana (à tester).

---

## 7. Corriger l'échelle : les leviers, avec des chiffres

### 7.1 Un levier à la fois (E5 : Krunt3 seul, modèle C, joueur moyen ; « brut » = facteur 0,65, tempo 1,6)

| Configuration | Victoire | Durée médiane | Vit. perdue par victoire | par minute |
|---|---|---|---|---|
| L0 brut : chef seul, K = 1 | 63 % | 12 s | 8,7 | 53,4 |
| L1 brut : chef seul, **K = 6** | 1 % | 24 s | 12,7 | 30,1 |
| L2 brut : + éclaireurs, K = 6, K_meute = 1 | 0 % | 28 s | – | 26,1 |
| L3 brut : **K = 20** | 0 % | 36 s | – | 21,1 |
| **L4 K = 20, kd 0,15, tempo 1,2 (chef seul)** | **93 %** | 2 min 04 s | 9,9 | 4,8 |
| L5 L4 + **éclaireurs** (K_meute = 4) | 82 % | 2 min 24 s | 10,6 | 4,6 |
| L6 L5 **sans phases ni agonie** | 100 % | 2 min 20 s | 6,9 | 2,9 |
| L7 L5 + **terrain** (feu 25 %, sol instable 20 % par round) | 52 % | 2 min 36 s | 11,4 | 4,7 |
| L8 L7 avec kd 0,12 pour compenser | 94 % | 2 min 40 s | 10,2 | 3,9 |

Effet de chaque levier, mesuré :

- **K seul : aucune victoire** (L1, L3). K (durée) et kd (dégâts reçus) sont **indissociables**.
- **Éclaireurs** (L4 à L5) : − 11 points de victoire, + 20 s ; la pression en cases par minute est stable (4,6 à 4,8) parce que les éclaireurs remplacent des coups du chef. Ils servent le **jeu** (décision tactique : éclaireurs d'abord ou cornes) plus que la difficulté.
- **Phases et agonie** (L5 à L6) : **valent 18 points de victoire et 3,7 cases par victoire** ; sans la phase 2 (Déluge, Morsure renforcée, cadence + 25 %) et sans l'agonie de 2 rounds, le chef est trop gentil. Les phases sont **le levier de pression le plus économique** : elles ne coûtent aucun PV supplémentaire.
- **Terrain** (L5 à L7) : sol instable et zone de feu ajoutent de la pression (− 30 points de victoire) ; **à compenser en baissant kd** (L8 : 94 %). Les dégâts de terrain doivent suivre le même coefficient kd que ceux du monstre, sinon ils dominent (sans cette règle, la simulation a donné 3 % de victoires).
- **Rang de boss** : K et kd dépendent du rang (§7.4), pas seulement de la Vitalité.

### 7.2 K et kd ensemble (E3b : Krunt3 seul, chef + éclaireurs, tempo 1,2, 1re tentative de la population / durée médiane)

| K | kd 0,08 | kd 0,10 | kd 0,12 | kd 0,15 | kd 0,20 |
|---|---|---|---|---|---|
| 12 | 100 % / 1 min 28 | 100 % / 1 min 28 | 100 % / 1 min 28 | 99 % / 1 min 28 | 87 % / 1 min 28 |
| 16 | 100 % / 1 min 56 | 100 % | 99 % | 90 % | 53 % |
| **20** | 100 % / 2 min 28 | 99 % / 2 min 28 | 93 % / 2 min 24 | **67 %** / 2 min 24 | 24 % / 2 min 24 |
| 25 | 100 % / 3 min 00 | 92 % | 70 % | 35 % / 2 min 56 | 9 % |
| 30 | 95 % / 3 min 36 | 69 % | 42 % / 3 min 28 | 15 % | 2 % |

Règles tirées du tableau (Krunt3, chef + éclaireurs, tempo 1,2) :
- **Durée ≈ 7 s par point de K** (K = 20 : 2 min 24 s ; K = 30 : 3 min 28 s) ; elle varie peu avec kd.
- **La victoire baisse d'environ 9 points par + 0,01 de kd** autour de K = 20 (93 % à kd 0,12, 67 % à 0,15, 24 % à 0,20).
- **Pour garder la même victoire quand K monte, kd doit baisser** : à K = 25, kd 0,10 donne 92 % (K = 20, kd 0,12 : 93 %) ; à K = 30, kd 0,08 donne 95 %.

### 7.3 Peu de gros coups ou beaucoup de petits : l'équivalence (E8)

Krunt3 seul, K = 20, chef + éclaireurs, kd calibré pour **45 % à la première tentative** :

| Actions du chef par round | Cadence | kd | Morsure déchirante (PC après cuir) | 1re tentative | Durée | Vit. perdue par minute |
|---|---|---|---|---|---|---|
| 0,4 | toutes les 10 s | 0,645 | 5,3 PC (10,2 % de la Vitalité) | 45 % | 2 min 16 | 5,5 |
| 0,6 | toutes les 6,7 s | 0,407 | 3,3 PC (6,4 %) | 46 % | 2 min 20 | 5,4 |
| **0,8** | **toutes les 5 s** | **0,290** | **2,4 PC (4,6 %)** | 45 % | 2 min 20 | 5,4 |
| 1,2 | toutes les 3,3 s | 0,174 | 1,4 PC (2,7 %) | 43 % | 2 min 24 | 5,2 |
| 1,6 (document 01) | toutes les 2,5 s | 0,111 | 0,9 PC (1,7 %) | 46 % | 2 min 28 | 5,0 |

**Invariant mesuré** : kd x tempo ≈ 0,21 (de 0,18 à 0,26) pour le chef. Le document 01 (une attaque toutes les 2,5 s, 9 PC par morsure) est **9 fois trop dur** : à ce tempo une morsure doit faire 0,9 PC. **Pour le jeu (attaques à télégraphier 500 à 700 ms, lisibles à 360 px de hauteur), choisir 5 s entre deux actions et 2,4 PC par morsure** ; c'est ce que contient le tableau du §8.

### 7.4 Rangs supérieurs (E7 : Krunt3 seul, kd calibré pour 45 % à la 1re tentative, héros au palier du scénario)

| Scénario | K | Palier | kd calibré | 1re tentative | avec 3 Jetons | Durée | Vit. perdue par minute |
|---|---|---|---|---|---|---|---|
| chef + éclaireurs | 20 | 0 | 0,172 | 44 % | 62 % | 2 min 24 s | 5,2 |
| **élite CR 12** | 8 | 2 | 0,089 | 46 % | 62 % | 2 min 44 s | 5,2 |
| élite CR 12 | **10** | 2 | **0,070** | 45 % | 67 % | 3 min 28 s | 4,2 |
| élite CR 12 | 12 | 2 | 0,058 | 45 % | 65 % | 4 min 08 s | 3,5 |
| **légendaire CR 18** | 4 | 4 | 0,027 | 43 % | 59 % | 2 min 16 s | 7,2 |
| légendaire CR 18 | **5** | 4 | **0,020** | 48 % | 60 % | 2 min 56 s | 5,6 |
| légendaire CR 18 | 6 | 4 | 0,016 | 45 % | 58 % | 3 min 36 s | 4,5 |

(Tempo du chef 1,2 action par round ; élite 1,5 ; légendaire 1,7 action de 2 attaques, ces deux derniers fixés dans le script.)

**À rang élevé, K diminue et kd s'effondre** : K = 10 puis 5, kd 0,07 puis 0,02. Raison : la dureté (0,64 puis 0,56) et les résistances divisent déjà les dégâts du héros, et les dégâts de l'élite (3d8+13 = 26,5) valent presque 2 morsures de chef pour une Vitalité de héros qui n'a monté que de 13 à 16. Le **produit kd x tempo vaut 0,21 (chef), 0,105 (élite), 0,034 par action (légendaire, 2 attaques par action)** : chaque rang divise la pression par 2 à 3 pour les mêmes héros. **La règle de rang n'est pas « K plus grand » mais « durée cible fixée, dégâts reçus ramenés à la pression de 5 cases par minute »**.

Quatre héros contre élite (K = 30 à 50, kd 0,06) : 100 % de victoires, 2 min 24 s à 4 min 04, aucun à terre ; contre légendaire (K = 12 à 20, kd 0,02) : 100 %, 1 min 32 à 2 min 44 s. À la table, la même règle donne le même résultat : **K proportionnel au nombre de héros** (K élite 10 solo, 40 à quatre).

Alternative par la formule de durée : **PV de chasse = durée cible x DPS du héros x 0,8** (rendement mesuré). Pour 150 s : chef 590 PV pour Krunt3 (K = 22), 490 pour Taranis (K = 18), 360 pour Cyril (K = 13), 295 pour Pascal (K = 11) ; élite 346 à 392 PV (K = 6 à 7), légendaire 363 à 383 PV (K = 5) pour Krunt3 et Taranis. L'accord avec les K calibrés (20, 10, 5) est bon pour le chef, plus lâche aux rangs élevés (la formule suppose les héros au palier 2).

### 7.5 Sensibilité à l'habileté du joueur (E7)

Réglage K = 20, kd 0,15, tempo 1,2, chef + éclaireurs :

| Esquive du joueur | Krunt3 : victoire / durée | Taranis : victoire / durée |
|---|---|---|
| 35 % | 15 % / 2 min 16 | 5 % / 1 min 48 |
| 45 % | 48 % / 2 min 24 | 18 % / 1 min 56 |
| **55 %** | **81 %** / 2 min 24 | **48 %** / 2 min 04 |
| 65 % | 96 % | 83 % |
| 75 % | 100 % | 98 % |

**La pente est raide** : 10 points d'esquive font passer de 15 à 81 % de victoires. Un réglage de précision n'a pas de sens avant le test humain : le but du prototype est d'**estimer l'esquive réelle des testeurs**, puis d'ajuster kd (§9).

---

## 8. Paramètres initiaux pour le prototype Godot

**Principe** : ces valeurs partent de la simulation (modèle C, échelle jeu). Elles donnent, pour un joueur moyen et le chef de la démo, **45 % de victoires à la première tentative, 60 à 65 % avec 3 Jetons, 2 min 20 s de combat, 5,4 cases perdues par minute**. Tout est à retoucher au test.

| Paramètre | Valeur initiale | Source / mesure |
|---|---|---|
| **Modèle de dégâts** | C : deux barres, esquive et garde payées en Endurance, Persévérer à Endurance 0 | E9 |
| Vitalité du héros | 4 + END cases, 4 PC par case | DOC 01 §4.2 |
| Endurance | 10 ; **régénération 2 /s après 0,8 s sans dépense** ; esquive 2 End ; garde 1 End par 2 PC bloqués ; technique de Posture 2 End | DOC 01 §3.2 ; E9 : spirale 8 % à 2 /s |
| Touches utiles | 0,6 par seconde (2,4 par round de 4 s) | DOC 01 §12 |
| Armure | − 5 % par point de CA, plafond 35 % | DOC 01 §4.3 |
| **K chef de meute (◆◆)** | **20** pour Krunt3 ; **K_perso** : Taranis 18, Cyril 16 (soin 4 Mana), Pascal 10 (« base ») à 14 (« soutien ») | E3b, E3c, E3d |
| **K éclaireurs (◆)** | **4** (Vitalité 24 PC, 2 à 3 touches) | DOC 01 ; E5 |
| **K élite (◆◆◆)** | **10** (héros au palier 2) | E7 |
| **K légendaire (◆◆◆◆)** | **5** (héros au palier 4) | E7 |
| **Tempo du chef (actions)** | **1 toutes les 5 s** (0,8 par round) ; phase 2 : + 25 % (1 toutes les 4 s) | E8 |
| Tempo d'un éclaireur | 1 toutes les 15 s chacun (4 éclaireurs : 1 attaque toutes les 3,7 s) | E8 (cadence / 3) |
| **kd du chef** (facteur total = 0,65 x kd) | **0,29** (si 1 action toutes les 5 s) ; facteur total 0,19 ; **ou** 0,17 (1 toutes les 3,3 s), 0,65 (1 toutes les 10 s) | E8 |
| kd de l'élite (tempo 1,5 / round) | **0,07** | E7 |
| kd du légendaire (tempo 1,7 / round, 2 attaques) | **0,02** | E7 |
| Dégâts de terrain | **multipliés par le même kd que le monstre** | E5 (L7) |
| Morsure déchirante du chef | **2,4 PC** après cuir, 2,6 avant armure (14 x 0,65 x 0,29) | E8 |
| Frappe de queue / Charge / Morsure renforcée | 2,2 / 3,0 / 3,3 PC avant armure (11,5 / 16 / 17,5 x 0,19) | calcul |
| Déluge de crocs (phase 2) | 3 x 2,0 PC | calcul |
| Éclaireur (Morsure, Griffes, Charge en coin) | 1,0 / 1,4 / 1,5 PC avant armure | calcul |
| Phase 2 | à 50 % **et** déclencheur (3 éclaireurs morts, point faible touché, fuite) ; **forcée à 30 %** | DOC 01 §5.3 ; E5 : valent 18 points |
| Agonie du chef | 8 s (2 rounds) | E5 |
| Jetons de Connaissance | 3 ; ensemble = + 7 points d'esquive dans la simulation (fenêtre parfaite de 150 ms + 2 images par jeton) | E9 : + 19 points de victoire |
| Cibles | 45 % de victoires en première tentative sans jeton, 60 à 65 % avec 3 | DOC 01 §4.6 (35 à 50 % et 60 à 75 %) |
| Soin de Cyril | Vitalité + 1 case pour **4 Mana** (au lieu de 2) | E3d |
| Tank de Krunt3 | pas de Provocation systématique ; sinon Épée et Bouclier + maille | §5 |
| Taranis | bagage à usage unique par chasse (2 Herbes Stabilisantes ; ni piège ni huile en v3) | §6.2, §12 |
| Pascal (base) | K = 10, ou lui donner dès le niveau 1 un petit kit offensif | §6.3 |

**Formule de contrôle** : durée ≈ 7 s x K (chef + éclaireurs, Krunt3). Victoire ≈ − 9 points par + 0,01 de kd autour de K = 20 (à tempo 1,2).

**Équivalence tempo / kd à retenir** : kd x actions par round ≈ 0,21 (chef). Pour 1 action toutes les 3,3 s (1,2 par round) kd = 0,17 ; toutes les 5 s (0,8) kd = 0,29 ; toutes les 10 s (0,4) kd = 0,65.

---

## 9. Plan de test avec seuils de réussite

**Principe** : un test = un build du prototype, un combat de boss (chef + 4 éclaireurs, phase 1 et 2), le héros Krunt3 en solo. **Au moins 8 testeurs, 3 essais chacun**, dont krunt et 2 joueurs de jeux d'action ; mesures automatiques journalisées (durée, coups subis, Endurance à chaque coup, cause du Hors Combat, esquives parfaites, potions). Les seuils reprennent le document 01 §4.6 et ajoutent ceux que la simulation a rendus mesurables.

| # | Mesure | Seuil de réussite | Si le seuil n'est pas atteint |
|---|---|---|---|
| T1 | **Durée du combat entier (chef + éclaireurs), 1er essai, solo** | **médiane de 2 à 4 min** (cible 2 min 20 s) ; 80 % des essais entre 1 min 30 s et 5 min | trop court : K + 20 % ; trop long : K − 20 % (durée ≈ 7 s par point de K) |
| T2 | **Victoire au 1er essai sans jeton** | **35 à 50 %** | trop haute : kd + 0,01 par tranche de 9 points à retirer ; trop basse : kd − 0,01 par tranche de 9 points |
| T3 | Victoire au 1er essai avec 3 Jetons | 60 à 75 % | si l'écart est inférieur à 15 points : élargir la fenêtre d'esquive par jeton (+ 2 images) |
| T4 | **Cases perdues par minute (joueur moyen)** | **4 à 6** (simulation : 5,2) ; Vitalité restante médiane à la victoire ≥ 2 cases sur 13 | hors fourchette : revoir kd avant K |
| T5 | **Spirale** : part des Hors Combat quand l'Endurance < 2 | **< 25 % des échecs** (simulation : 8 % à 2 /s ; 39 % à 1,25 /s) | augmenter la régénération ou baisser le coût d'esquive à 1,5 |
| T6 | Part du temps sans esquive possible (Endurance < 2) | **< 20 %** (simulation : 7 % à 2 /s) | idem |
| T7 | Équité perçue (1 à 5) ; lisibilité | **≥ 3,5** ; ≥ 4 pour la lisibilité des télégraphies | allonger les télégraphies (500 à 700 ms), pas diminuer les dégâts |
| T8 | **Phase 2 forcée** : proportion de combats où le chef reste en phase 1 sous 30 % | 0 % | vérifier le déclencheur |
| T9 | **K par personnage** : mêmes seuils T1 et T2 pour Taranis, Cyril, Pascal | durée 2 à 4 min et victoire 35 à 50 % avec K_perso du §8 | ajuster K_perso ; si Pascal « base » dépasse 4 min à K = 10, lui donner un kit offensif |
| T10 | **Cyril** : fréquence de Vitalité soignée par minute | ≤ 2 cases par minute ; victoire solo 40 à 55 % | coût du soin 4 Mana, plafond du Flux |
| T11 | **Tank** (2 à 4 humains ou IA) : Krunt3 avec bouclier tient 70 % des combats de 2 min avec Provocation | victoire d'équipe ≥ celle de l'équipe sans tank | si non, limiter Provocation ou changer le kit |
| T12 | **Élite et légendaire** : seuils T1 et T2 avec K = 10 / kd 0,07 et K = 5 / kd 0,02 (héros aux paliers 2 et 4) | idem | appliquer la règle « kd x tempo constant par rang » |
| T13 | **Comparaison des trois modèles** (protocole 4.6 du document 01) | C doit battre A et B sur T4, T5 et T7 ; sinon revoir la régénération | – |

**Ordre** : T5 et T6 d'abord (la régénération conditionne tout), puis T1, T2, T4 (K, kd, tempo), puis T9 à T12.

**Réglage en boucle** : après chaque série, estimer l'esquive effective des testeurs (probabilité de ne pas être touché sur une attaque télégraphiée) : si elle dépasse 65 %, remonter kd ; si elle est sous 45 %, baisser kd et allonger les télégraphies. **L'esquive effective est le premier paramètre à mesurer**, parce que 10 points d'esquive font passer de 15 % à 81 % de victoires (§7.5).

---

## 10. Limites (honnêtes)

1. **Temps abstrait** : un round de 4 s regroupe 2,4 touches et 1 à 2 attaques de monstre. La simulation ne voit ni le positionnement, ni la hauteur des hurtbox, ni les fenêtres de punition, ni les télégraphies. Les « esquives réussies » sont des probabilités constantes ; un humain est bien plus variable (une série de 3 échecs de suite est plus fréquente que dans un tirage indépendant).
2. **IA de héros minimale** : Krunt3 relance ses techniques à chaque round tant qu'il a 4 d'Endurance ; Cyril soigne le plus blessé sous 60 % ; Taranis lance *Tir Ciblé* dès que la cible n'est pas Exposée et qu'il a 2 Mana ; tous visent d'abord les éclaireurs. Aucun joueur réel ne joue ainsi : les parts de dégâts et le tank sont des ordres de grandeur.
3. **Hypothèses non issues des livres** : probabilité de cible prioritaire (0,8), part d'Interposition (0,5), poids des attaques des monstres, régénération (5 / round dans les tableaux), esquive 55 % et sa pente par AGI, effet des Jetons (+ 7 points), coût du modèle B (0,4 End par touche), bagage de Taranis, kits de Pascal, paliers des héros évolués, durées d'états, Riposte à 1 End une fois par round.
4. **Modèle des monstres simplifié** : une seule cible par attaque (hormis la queue qui en touche deux), pas de Ralenti ni de Secoué sur les touches des héros (le Secoué ne divise que l'esquive), pas d'immunités ni de brisures (les parts de dégâts de zone sont moyennées), pas de fuite du monstre, pas de capture, pas de Vocalisation qui réagit aux brisures. Le chef attaque dès le round 1 alors que la fiche prévoit un début « Territoire » où il laisse sa meute engager (DOC 01 §13.2) : le combat réel sera plus doux au début.
5. **Niveaux et fiches** : les héros du palier 2 et 4 sont une paramétrisation grossière (points d'attribut répartis moitié END moitié attaque, qualité + 1 à + 2). Les rangs d'École, les techniques de rang II et plus ne sont pas simulés. Le Souffle du Réceptacle de Krunt3 est simulé mais sans effet mesurable aux tailles de combat testées.
6. **Pas de soins hors combat**, pas d'Infirmerie, pas de familier, pas de pièges autres que le piège à colle de Taranis, pas d'alchimie de combat sauf huile de feu et bombes de Pascal.
7. **Statistique** : 600 tirages par cellule (1 000 pour la réconciliation), soit ± 4 points sur un pourcentage et ± 1 case sur une moyenne de Vitalité ; la population de joueurs est un mélange de cinq niveaux d'habileté, pas une mesure. Les tableaux calibrés (kd) sont obtenus par dichotomie sur 9 itérations et sont stables à ± 0,01.
8. **Table et jeu solo sont deux expériences** : le jeu est solo, la table se joue au tour par tour avec des dés. Les K et kd de ce document valent pour le solo temps réel ; pour la table, le K de table est de l'ordre de 2 à 4 (échelle Livre, §3.2) et la table n'a pas été calibrée contre un vrai MJ.
9. **Rythme** : la consigne demande des durées de 2 à 4 minutes ; le document 01 §12 prévoit 5 à 8 minutes pour un ◆◆. Rien ici ne tranche cette question de rythme : elle est dans les mains de krunt.

---

## 11. Questions et décisions pour krunt

| # | Question | Ce que dit la simulation |
|---|---|---|
| 1 | **Durée cible d'un boss ◆◆ en solo : 2 à 4 min, ou 5 à 8 min (document 01 §12) ?** | 2 min 20 s à K = 20 ; 5 à 8 min demande K = 50 à 70 et kd ÷ 2 à 3 : possible, mais la pression de 5 cases par minute sur 5 à 8 minutes demande des soins (Potions de Vitalité) |
| 2 | **Krunt3 est-il un tank ou un fer de lance ?** Sinon, accepter un changement de kit (Épée et Bouclier, maille) et revoir l'École de Pascal | Double Lame + cuir : le tank perd 99 % des combats de Krunt3 ; bouclier : victoire de l'équipe + 14 points |
| 3 | **Régénération d'Endurance de 2 /s** (document 01) : confirmée comme règle de jeu ? | spirale 8 % contre 35 % à 1,25 /s |
| 4 | **Modèle de dégâts C** retenu (le protocole 4.6 reste à exécuter) | meilleur sur 3 critères sur 3 |
| 5 | **K propre à chaque personnage en solo, ou un kit de départ pour Pascal ?** | facteur 2 entre Krunt3 et Pascal « base » |
| 6 | **Soin de Cyril : 4 Mana** accepté ? | à 2 Mana elle ne perd jamais en solo |
| 7 | **Le « 3 à 7 cases perdues par victoire »** (document 01 §4.6) remplacé par **les cases perdues par minute** et la **Vitalité restante** ? | incompatible avec 35 à 50 % de victoires (10 à 12 cases perdues sur 13) |
| 8 | **Contenu du bagage de Taranis** (v3 : carquois, instruments, carnet de pisteur, 7 jours de rations, 2 Herbes Stabilisantes, Carnet des Routes, boussole éteinte) | les 2 Herbes valent environ 29 points de victoire en solo (§12) |
| 9 | Phase 2 : passage forcé à 30 % si le déclencheur manque | oui, mesuré utile (phases : 18 points de victoire) |

---

## Annexe : liste des tableaux produits par le script

`echelle` (E0), `livre` (E1 + réconciliation + K de table), `jeu` (E2), `K` (E3a à E3e), `tank` (E4a à E4d), `leviers` (E5), `variantes` (E6), `competence` (E7), `equiv` (E8), `modeles` (E9). La graine de base est `SEED = 20261006` ; chaque tableau utilise une graine dérivée de l'étiquette de sa cellule (CRC32), donc ajouter un tableau ne modifie pas les autres. Les paramètres modifiables (PRESETS, ESQUIVE_BASE, P_PROVOC, P_INTERPO, RECO, POP, BAGAGE_TARANIS, HEROS) sont en tête du fichier.

---

## 12. Rejeu v3 (2026-10-06) : fiche v2 de Taranis, Défense 18 de Pascal

**Ce qui a changé dans `outils/simu_combat.py`** : Taranis AGI 11 / END 6 (Vitalité 10), attaque 15 (11 + 3 + 1 de rang I), initiative 17, dégâts par touche 11 ; Pascal en cuir + bouclier (CA 4, Défense 18) ; bagage v3 de Taranis : ni piège à colle ni huile de feu, 2 Herbes Stabilisantes (+2 cases de Vitalité, utilisées sous 50 % de Vitalité), 2 potions de base ; le kit « bouclier » de Krunt3 (variante du §5) est cuir + bouclier (+2 CA) et non plus maille + bouclier (+3). Graine 20261006, **300 tirages par cellule** (± 6 points sur un pourcentage), rapport complet exécuté en 4 min 30 s ; les sections `variantes` (7 s) et `tank` suffisent pour les tableaux ci-dessous.

**E6 : parts des dégâts et risque (table de quatre héros, modèle A)**

| Échelle, variante | Krunt3 / Taranis / Cyril / Pascal | ≥ 1 à terre | Victoire |
|---|---|---|---|
| Livre K = 1, référence (bagage v3 ; Pascal « base ») | 23 % / **29 %** / 25 % / 23 % | 72 % | 99 % |
| Livre K = 1, sans les Herbes | 23 / 30 / 25 / 23 % | 74 % | 98 % |
| Livre K = 1, Pascal « bombe » (hors décision de krunt) | 20 / 25 / 22 / 33 % | 73 % | 100 % |
| Livre K = 3, référence | 18 / **30** / 25 / 26 % | 93 % | **76 %** (était 94 %) |
| Livre K = 3, sans les Herbes | 18 / 30 / 26 / 25 % | 89 % | 74 % |
| Jeu K = 60, kd 0,15, modèle C, référence | 24 / **29** / 27 / 20 % | 0 % | 100 % (durée 2 min 08 s) |

**Taranis seul, K = 20, kd 0,15, modèle C, première tentative** : avec le bagage v3 **41 %** (3 min 16 s), sans les Herbes **12 %** ; K = 18 : 58 % (E3c, rapport complet). Cyril : 100 % avec le soin à 2 Mana, 77 % à 4 Mana (inchangé). Pascal « base » : K = 10 donne 71 % à la première tentative (inchangé).

**Tank de Krunt3 (E4b, modèle C, K = 60, kd calibré sans tank pour 75 %)** : sans tank, victoire 80 % ; Provocation seule 58 % (Krunt3 à terre 98 %) ; Provocation + Mur de Chair + Interposition 42 % (Krunt3 à terre 100 %). Avec le kit cuir + bouclier : 62 % sans tank, 67 % avec Provocation, 61 % en complet ; **duo Krunt3 + Cyril** (K = 40) : 12 % avec le kit de base, **85 % avec cuir + bouclier** (était 94 % avec maille + bouclier).

**Ce que cela change dans les conclusions**
1. **Taranis n'est plus le premier des dégâts** (29 à 30 % à quatre contre 35 à 38 %) : il n'écrase plus la table, la correction du §6.4 point 3 de `04` (un point d'AGI vers END) a suffi. Pas d'autre réglage à faire.
2. **Le bagage de `08` vaut moins que celui de la v1 à la table** (plus de piège ni d'huile) mais **les 2 Herbes pèsent lourd en solo** (41 % contre 12 %). À surveiller au test : l'Herbe Stabilisante est un soin de Vitalité de +2 cases (DD 10 [L Livre VII]) ; si krunt la trouve trop forte, passer à 1 Herbe (question `10` Q23).
3. **La table est plus difficile à K = 3** (76 % de victoires au lieu de 94 %) : la Défense 18 de Pascal, la perte du piège et de l'huile de Taranis et son point d'AGI en moins jouent ensemble. Le chef de meute reste « trivial » à K = 1 (99 %).
4. **Krunt3 reste un fer de lance** : le résultat du tank est inchangé (Provocation seule : Krunt3 à terre dans 98 % des combats ; complet : 100 %). Pour tenir la première ligne il faudrait cuir + bouclier, c'est-à-dire l'école de Pascal (Gardien Mobile).
5. **Pas rejoué** : le calibrage de K_perso et kd pour les quatre personnages (E3c, tableau du §8) est inchangé pour Krunt3, Cyril et Pascal et très proche pour Taranis (K = 18 : 58 %) : à confirmer au prototype. Les sections E1, E2, E5, E7, E8, E9 (Krunt3 seul) ne dépendent pas de ces fiches.
