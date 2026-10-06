# 08 : Fiches v2 des quatre personnages et briefs de sprites

> **Passe v3 (2026-10-06)** : somme d'attributs de Pascal corrigée (7/6/8/9/5/7 = 42), comptes de palette recalculés (Pascal 23), contenu de la Dette de Sang aligné sur la Braise. Synthèse canonique des fiches : `10-trame-v3.md` §2. Reste de ce document : référence (JSON du VTT, sprites).

Rédigé le 2026-10-06. Domaine : (1) appliquer les décisions de krunt aux quatre fiches (Krunt3, Taranis, Cyril, Pascal) en respectant les règles de création des livres ; (2) écrire un brief de sprite et un prompt PixelLab simplifié pour chacun, avec la déclinaison « porteur de l'entité » de Krunt3 (sans spoiler).

**Légende.** **[L]** = ce que disent les livres (livre et lieu). **[P]** = proposition de Claude. **[INV]** = invention sans appui dans les livres, à tester. **[V#]** = point à valider par krunt (liste en §10). Aucun commit n'a été fait. Ce document remplace les fiches JSON de `04-equilibrage-personnages.md` §9.1 à 9.4 ; le reste de `04` (profils de progression, simulation, recrues) reste valable sous réserve des corrections du §8.

---

## 0. En bref

- **Les quatre fiches v2 respectent le budget de création** : 42 points d'attributs (3 à 12, bonus d'origine ensuite), Vitalité 4+END, Endurance 10, Honneur 4 à 6, 17 points de compétence (max 3), 6 PA d'avantages avec au plus 2 Majeurs et 3 mineurs, gain de handicaps plafonné à +4, un seul Handicap Majeur gratuit, métiers à ★1, équipement de départ « niveau 1-5 » (Livre VIII ch. 9 §5).
- **Décisions de krunt appliquées** : Krunt3 aux Frères de l'Épreuve (« Ordre du Jugement » en surnom), Ours, Danse Rouge, Espion/Infiltrateur, Lames Franches, Îles des Serments ; Taranis Chasseur-Pisteur + Cartographe, Navigateurs Gris, Guilde de Chasse, **avec un bagage de départ** (§4) ; Cyril Sceau Pourpre, Mage Blanc ; Pascal Sceau Pourpre, Alchimiste, **attaque de base seule jusqu'aux bombes** ; régions de l'Atlas sans surnoms.
- **Ordre de Pascal** : je recommande **Sentinelles du Pacte** (fiche déjà rédigée dans `03` §3.4, à ajouter à StoryForge), avec **Culte des Ancêtres Veilleurs** (canonique, Hautes Terres) en repli (§5).
- **« Deux Lames »** : le Livre VI justifie de **garder Danse Rouge** ; je n'ai pas de meilleure proposition (§6).
- **Sprites** : quatre silhouettes volontairement incompatibles (Krunt3 large et bas à manteau de fourrure, Taranis haut et étroit avec arc vertical et sac bossu, Cyril colonne à manteau évasé, Pascal court et carré avec bouclier rond). Chacun a une palette de 23 à 30 couleurs sur 32 (§9.6, comptes recalculés). Le sprite à la hache à deux mains est abandonné : Krunt3 porte **deux lames courtes**.

---

## 1. Décisions appliquées et hypothèses

| Sujet | Décision de krunt | Application dans ce document | Statut |
|---|---|---|---|
| Krunt3, ordre | Frères de l'Épreuve ; « Ordre du Jugement » = surnom populaire | `ordre-nom` = Frères de l'Épreuve ; surnom dans `_extras.ordre-surnom` | décidé |
| Krunt3, Posture | Ours | Ours | décidé |
| Krunt3, école | « Deux Lames » : l'école la plus proche des livres | **Danse Rouge** (§6) | proposé, [V1] |
| Krunt3, métier / clan / région | Espion/Infiltrateur ; Lames Franches ; Atlas sans surnom | Espion/Infiltrateur ★1 ; Lames Franches ; **Îles des Serments** | région proposée, [V2] |
| Taranis, métier | Chasseur-Pisteur + Cartographe | principal Chasseur-Pisteur (variante désertique), secondaire Cartographe (variante explorateur), tous deux ★1 | décidé |
| Taranis, bagage | part avec un bagage de départ | §4 | proposé, [V3] |
| Taranis, clan / guilde | Navigateurs Gris ; Guilde de Chasse | idem ; région **Déserts Rouges** | région proposée, [V2] |
| Cyril | Sceau Pourpre ; Mage Blanc | idem ; région Cœur Impérial ; guilde Marchands Libres (inchangée) | décidé |
| Pascal, clan | Sceau Pourpre | idem ; région **Hautes Terres Claniques** (adoption par serment) | région proposée, [V2] |
| Pascal, métier | Alchimiste ; attaque de base seule avant les bombes | §5.3 | décidé |
| Pascal, ordre | « le plus cohérent » | **Sentinelles du Pacte** (fiche à ajouter) ; repli Culte des Ancêtres Veilleurs | proposé, [V4] |
| Régions | Atlas, sans surnoms | noms seuls (« Îles des Serments », pas « Là où refuser est déjà une défaite ») | décidé |
| Fiches du VTT | des essais | non suivies ; la fiche v2 est calculée depuis les règles | décidé |

---

## 2. Règles de création appliquées (contrôle)

| Règle [L] | Source | Krunt3 | Taranis | Cyril | Pascal |
|---|---|---|---|---|---|
| 42 points, 3 à 12 par attribut | Livre I ch. 3 §7 étape 3 | 42 (9/8/8/4/7/6) | 42 (5/11/6/9/6/5) | 42 (5/6/6/8/9/8) | 42 (7/6/8/9/5/**7**, +1 VOL d'origine) |
| Bonus d'origine après répartition | Livre I ch. 2 §4 ; Livre II ch. 4 | Îles : +1 END | aucun | aucun | Hautes Terres : +1 VOL |
| Vitalité = 4 + END | Livre I ch. 2 §4 | 13 | 10 | 10 | 12 |
| Endurance = 10 | Livre I ch. 3 §7 étape 4 | 10 | 10 | 10 | 10 |
| Honneur de départ 4 à 6 | Livre I ch. 3 §7 étape 9 | 4 | 4 | 5 | 6 |
| Compétences : 12 + 2 + 2 + 1 = 17, max 3 | Livre I ch. 3 §6 | 17 | 17 | 17 | 17 |
| Métier ★1, second ≤ principal, 2 au plus | Livre I ch. 3 §7 étape 6 | 1 métier | 2 métiers ★1/★1 | 1 métier | 1 métier |
| École rang I, une Technique de rang I | Livre VI ch. 2 | Fuite Tranchante | Tir Ciblé | Première Vague | Garde Haute |
| Posture : 4 Techniques, 2 Endurance | Livre VI ch. 4 | Ours | Loup | Loup | Loup |
| PA : 6, +1 Handicap Majeur gratuit, gain ≤ +4, ≤ 2 Majeurs, ≤ 3 mineurs | Livre VIII ch. 1 | 9 PA (6 + 3), 2 Maj. + 3 min. | 6 PA, 1 Maj. + 3 min. | 6 PA (3 + 2 + 1), aucun inutilisé | 7 PA (6 + 1), 2 Maj. + 1 min. |
| Incompatibilités métier / avantage | Livre VIII ch. 1 §7 | aucune (pas d'Autorité Naturelle) | aucune | aucune (pas d'Affinité Nécrotique) | aucune |
| Équipement « niveaux 1-5 » : outils de base, arme simple, tenue fonctionnelle ; un objet symbolique | Livre VIII ch. 9 §5 | oui | oui, plus bagage (§4) | oui | oui (**plus de maille**) |
| Forge et Tension collectives, 0 | Livre I ch. 2 | hors fiche | hors fiche | hors fiche | hors fiche |
| Mana de départ | **Livre I : 2** ; **Livre VI ch. 13 §6 : 6 à 8** | 6 | 6 | 8 | 6 |

Mana : les livres se contredisent ([L] Livre I ch. 3 §7 : « 2 × rang » ; Livre VI : 6 à 8 au rang I). Je garde la valeur du Livre VI et la formule de `04` §4.1 (6, +1 si VOL final ≥ 8, +1 si métier de magie, plafond 8). Si krunt choisit le Livre I, remplacer par 2 pour les quatre. [V5]

---

## 3. Les quatre fiches v2

### 3.1 Identité et affiliations

| | **Krunt3** | **Taranis** | **Cyril** | **Pascal** |
|---|---|---|---|---|
| Rôle | Héros, fer de lance (PNJ pendant les phases de JDR, krunt étant MJ) | Éclaireur-cartographe, tireur | Soin, serment, voix | Rempart alchimiste |
| Région d'origine (Atlas, sans surnom) | **Îles des Serments** (6) | **Déserts Rouges** (9) | **Cœur Impérial** (1) | **Hautes Terres Claniques** (4) |
| Bonus d'origine | +1 END | aucun d'attribut | aucun d'attribut | +1 VOL |
| Clan | Lames Franches | Navigateurs Gris | Sceau Pourpre | Sceau Pourpre (adoption par serment) |
| Guilde | Guilde Martiale | Guilde de Chasse | Marchands Libres | Guilde Martiale |
| Ordre | **Frères de l'Épreuve** (surnom : « Ordre du Jugement ») | aucun | aucun | **Sentinelles du Pacte** [INV, fiche à ajouter] |
| Posture | Ours | Loup | Loup | Loup |
| École (rang I) | Danse Rouge (Double Lame, mode Flux) | Souffle Long (Arc, mode Rituel) | Flux Tranchant (Épée Longue, mode Flux) | Gardien Mobile (Épée et Bouclier, mode Ancrage) |
| Métier principal ★1 | Espion / Infiltrateur (variante occulte) | Chasseur-Pisteur (variante désertique) | Mage Blanc | Alchimiste (variante martiale) |
| Métier secondaire ★1 | aucun (Mage Noir interdit à la création ; tentation par jalon, voir `04` §5.4) | **Cartographe** (variante explorateur) | aucun | aucun |
| Profil de progression (`04` §5) | Pacte | Étincelle, **tempéré** (§8) | Graine | Roc |
| Affinité d'origine (`region-elem`, hors livres) | — | Vent | Métal | Terre |

Notes de cohérence :
- **Krunt3** : un Lame Franche (aucun territoire, aucun maître permanent) qui est aussi un Frère de l'Épreuve (ordre de juges) : tension de rôle utile [L Livre V clan 2, Atlas Région 6]. Les Îles produisent « des personnes formées » qui partent chercher fortune : c'est exactement son profil [L Atlas Région 6]. Le clan Lames Franches n'a pas de région propre ; les Îles n'ont pas de clan dominant (Livre V §5 : « — ») : la place est libre.
- **Taranis** : Navigateurs Gris et Guilde de Chasse sont dominants aux Marches Frontalières (Livre V §5), lieu d'arrivée de la trame. Je l'origine dans les **Déserts Rouges** (steppe rocailleuse à vents, Guilde de Chasse présente, Passage Bas de Tyr de contrebande) : continuité avec la « Steppe du Vent » du VTT, et il n'est pas « né aux Marches », ce qui préserve la prémisse (`03` §2.1, `05` §4.2). Il connaît pourtant les Marches par son métier : **c'est un voyageur**. Alternative : Marches Frontalières (correspondance parfaite au tableau Livre V §5, mais il serait chez lui).
- **Pascal** : le Livre V autorise un clan hors de sa région « avec rupture culturelle à jouer » [L Livre V §5]. Le Sceau Pourpre y recrute par « démonstration de capacité juridique » ou serment [L Livre V ch. 2]. Les Hautes Terres abritent la Vallée des Serments (Atlas) : décor de l'adoption. Pierres Hautes (clan dominant) est allié de la Guilde Martiale et ennemi des Lames Franches [L Livre V ch. 7 §2].
- **Cyril** : correspondance parfaite : clan dominant Sceau Pourpre, guilde Marchands Libres [L Livre V §5]. Son ordre reste vide : l'Ordre du Flux est allié du Sceau mais il est **l'antagoniste validé** (`05`), on ne l'impose pas.
- Guildes : spécialités alignées sur StoryForge (`03` §4) : Guilde Martiale (Krunt3 : guerre contractuelle, Officiers-Loges ; Pascal : Capitaineries de défense), Guilde de Chasse (contrats, formation), Marchands Libres (crédit, dette et voies commerciales).

### 3.2 Attributs et dérivés

| | FOR | AGI | END | ESP | VOL | PRE | Somme | Final |
|---|---|---|---|---|---|---|---|---|
| **Krunt3** | 9 | 8 | 8 (+1) | 4 | 7 | 6 | 42 | END **9** |
| **Taranis** | 5 | 11 | 6 | 9 | 6 | 5 | 42 | — |
| **Cyril** | 5 | 6 | 6 | 8 | 9 | 8 | 42 | — |
| **Pascal** | 7 | 6 | 8 | 9 | 5 (+1) | 7 | 42 | VOL **6** |

| Dérivé | Krunt3 | Taranis | Cyril | Pascal |
|---|---|---|---|---|
| Vitalité max (4 + END) | **13** | **10** | **10** | **12** |
| Endurance max | 10 | 10 | 10 | 10 |
| Mana de départ [V5] | 6 | 6 | 8 | 6 |
| Honneur | 4 | 4 | 5 | 6 |
| Défense (AGI + END) | 17 | 17 | 12 | 14 |
| Défense avec armure et bouclier | **19** (cuir +2) | **19** (cuir +2) | **13** (vêtements renforcés +1) | **18** (cuir +2, bouclier +2) |
| Initiative (AGI + VOL) | 15 | 17 | 15 | 12 |
| Précision (AGI + ESP) | 12 | 20 | 14 | 15 |
| Résistance mentale (VOL + ESP) | 11 | 15 | 17 | 15 |
| Autorité sociale (PRE + Honneur) | 10 | 9 | 13 | 13 |

Défense avec armure : [P] AGI + END + CA de l'armure (`04` §1.4 n° 7). Armures [L] Livre IX ch. 7 : vêtements renforcés +1, cuir +2, maille +3 (forgeron niveau 8-15), plaques +4 (forgeron niveau 15-25). Épée et Bouclier : « protection +2 CA » [L Livre IX ch. 6].

### 3.3 École, Posture, Techniques

| | Krunt3 | Taranis | Cyril | Pascal |
|---|---|---|---|---|
| Technique d'École rang I (2 Mana) | *Fuite Tranchante* | *Tir Ciblé* | *Première Vague* | *Garde Haute* (défensive, aucune attaque) |
| Techniques de Posture (4, 2 End chacune) | *Interposition, Ancrage (Ours), Provocation, Mur de Chair* | *Appel de Meute, Flanc Coordonné, Présence Rassurante, Sacrifice de Meute* | idem | idem |
| Technique « d'ouverture » de meute [INV, `04` §7.3] | Interposition | Flanc Coordonné | Présence Rassurante | Sacrifice de Meute |
| Tabou d'école [L Livre VI §4] | Perdre le contrôle de soi | Tirer sans cible claire | Briser volontairement le flux | Abandonner un allié protégé |
| Arme (qualité Standard) | Double Lame 1d6+1d6 | Arc 1d8, 80 m, désavantage au contact | Épée Longue 1d8 | Épée et Bouclier 1d6, protection +2 |
| Armure | cuir +2 | cuir +2 | vêtements renforcés +1 | cuir +2 (maille +3 reportée) |
| Résonance de départ | aucune | **aucune** (retirée, voir §8) | aucune | aucune |

### 3.4 Compétences (17 points, maximum 3 à la création)

Compétences du Livre I ch. 3 §6 : Athlétisme, Corps-à-corps, Brisement, Discrétion, Acrobaties, Tir & lancers, Esquive active, Résistance, Marche forcée, Perception, Traque, Connaissance (domaine), Médecine, Artisanat, Concentration, Résistance mentale, Intimidation froide, Persuasion, Tromperie, Commandement, Représentation.

| | Krunt3 | Taranis | Cyril | Pascal |
|---|---|---|---|---|
| Niveau 3 | Corps-à-corps, Esquive active, Discrétion | Tir & lancers, Traque, Perception, Connaissance (cartographie et géographie) | Médecine, Concentration, Persuasion | Artisanat (alchimie), Connaissance (alchimie et plantes), Résistance |
| Niveau 2 | Résistance, Intimidation froide | Marche forcée | Corps-à-corps, Connaissance (droit et serments) | Corps-à-corps |
| Niveau 1 | Tromperie, Perception, Athlétisme, Résistance mentale | Discrétion, Esquive active, Connaissance (créatures) | Représentation, Résistance mentale, Perception, Esquive active | Perception, Athlétisme, Commandement, Médecine, Résistance mentale, Esquive active |
| **Total** | 9+4+4 = **17** | 12+2+3 = **17** | 9+4+4 = **17** | 9+2+6 = **17** |

Bonus de jet = attribut + compétence (avant le d20). Krunt3 : attaque 9+3 = 12 ; discrétion 8+3 = 11 ; perception 4+1 = 5 (faiblesse voulue). Taranis : attaque à distance 11+3 = 14 ; traque 9+3 = 12 ; cartographie 9+3 = 12. Cyril : soin 8+3 = 11 ; persuasion 8+3 = 11. Pascal : alchimie 9+3 = 12 ; résistance 8+3 = 11. Chaque rôle est le meilleur du groupe dans son domaine.

### 3.5 Avantages et handicaps (Livre VIII)

| | Avantages (PA) | Handicaps (gain de PA) | Total PA |
|---|---|---|---|
| **Krunt3** | Maîtrise de Combat (Danse Rouge, Majeur 3) ; Vision Éthérique (Majeur 3) ; Réflexes Affûtés (1) ; Récupération Accélérée (1) ; Posture Défensive (1) = **9** | **Réceptacle** (unique, remplace le Majeur gratuit) ; **Dette de Sang : créancier du pacte** (Majeur, +3) | 6 + 3 = 9 |
| **Taranis** | **Préparateur Obsessionnel** (Majeur 3) ; Réflexes Affûtés (1) ; Réseau Local, Marches (1) ; Improvisation Pratique (1) = **6** | **Dette de Sang envers le Cercle des Boussoles Éteintes** (Majeur gratuit) | 6 |
| **Cyril** | Nom Respecté (Majeur 3) ; Canal Stable (Majeur 3 − 1 synergie Mage Blanc = 2) ; Résistance Partielle (1) = **6** | **Serment Absolu** (Majeur gratuit) | 6 |
| **Pascal** | Corps Endurci (Majeur 3) ; Ingénieur Méthodique (Majeur 3, **sans synergie** [V6]) ; Économie de Matériaux (1) = **7** | **Blessure Ancienne** (Majeur gratuit, −2 à courir) ; Code Personnel Rigide (+1) | 6 + 1 = 7 |

Contrôles : Krunt3 a 2 Majeurs et 3 mineurs (limites atteintes) ; gain de handicaps +3 (≤ 4). Cyril : le Livre VIII donne « Mage Blanc + Canal Stable −1 PA » ; Nom Respecté demande Honneur ≥ +5 (lu comme Honneur 5 sur l'échelle du Livre I) ; Canal Stable demande « Karma ≥ +3 » (lu comme Honneur ≥ 5, incohérence Livre I / VIII, `04` §1.4 n° 5) ; les 6 PA sont dépensés (3 + 2 + 1), aucun n'est perdu. Taranis : Préparateur Obsessionnel est l'expression mécanique du bagage (§4) ; sa limite [L] : « inutilisable en situation improvisée ou d'urgence ».

Handicaps uniques de Krunt3 (le Livre VIII ch. 4 §3 exige des conditions d'activation claires et une validation du MJ avant la première session) :
- **Réceptacle** [INV, [V7]] : une entité habite Krunt3. *Activation* : au moins une fois par arc, et sur Échec critique ou quand il se met en danger, le MJ déclenche une manifestation involontaire (chaleur, vision, impulsion). *Limites* : l'entité n'est ni alliée ni ennemie par défaut ; la manifestation peut aider ou gêner au choix du MJ. Rédigé **neutre** pour tenir compte de la décision « l'entité ne le maudit peut-être pas ».
- **Dette de Sang : créancier du pacte** : le Livre VIII définit Dette de Sang comme « obligation narrative récurrente envers une faction, une personne ou une institution » (déclenchement : une fois par arc minimum). Le **contenu** de la dette (créancier, prix) est celui de la trame révisée : **l'ancien coût par l'oubli de noms est retiré** (décision de krunt), il ne doit donc pas figurer sur la fiche. La dette est celle de la **Braise** (Loyer quotidien de l'Écho, `06` §2 et `10` §4.3) et de la **Dette du Flux** (`05` §2.6 créance 1). [V8 : résolu par la décision de krunt, reste à confirmer le dosage]

### 3.6 Équipement de départ et Éclats

Principe [L Livre VIII ch. 9 §5] : niveaux 1-5 = outils de base, arme simple, tenue fonctionnelle, **un objet symbolique** ; l'équipement reflète le statut, pas un budget. Rien de Supérieur, aucun objet nommé, aucune maille (forgeron niveau 8+). Pas de règle de monnaie de départ dans les livres : les Éclats sont [INV] et volontairement faibles (`05` §4.4 : chacun arrive avec ce qu'il portait).

| | Krunt3 | Taranis | Cyril | Pascal |
|---|---|---|---|---|
| Armes | deux lames courtes | arc long + carquois | épée longue | épée courte + bouclier rond |
| Tenue | cuir + manteau de fourrure | cuir + cape grise | manteau long, étole pourpre | cuir + plaques d'acier plates |
| Outil de métier | une tenue neutre et un faux nom (Espion : « sans rien de compromettant ») | kit de pisteur, **instruments de cartographe**, **carnet de pisteur** | trousse de soins, symbole du Sceau | alambic de campagne, mortier, 5 fioles |
| Objet symbolique | un cordon rouge coupé noué au poignet (contrat tranché : Code de la Lame Libre) | une **boussole éteinte** (aiguille immobile) offerte par son premier Passeur | un **sceau de cire** de famille, jamais utilisé | une **lanterne de Guetteur** de fer, héritée de sa première Veille |
| Éclats [INV] | 30 | 120 | 90 | 60 |
| Provisions (`05` §4.4 : eau 1 jour, 3 rations) | ce qu'il porte | **bagage complet (§4)** | idem base | idem base |

### 3.7 Champs narratifs (Livre VIII ch. 9) : propositions de départ à réécrire par chaque joueur

| | Tension initiale | Objectif majeur | Relations (2 établies, 1 problématique, 1 ambiguë) |
|---|---|---|---|
| **Krunt3** | un acte accompli dans le deuil, dont il porte les suites | « Que les miens ne soient pas partis pour rien » | établies : le Cercle de Fer qui l'a formé ; un Gardien de son île ; problématique : un Capitaine Fractal dont il a refusé le contrat ; ambiguë : ce qui l'habite |
| **Taranis** | cartes prêtées par le Cercle des Boussoles Éteintes à rapporter complétées | « Tracer la route que personne n'a osé tracer » | établies : son Passeur ; la Guilde de Chasse (contrat en cours) ; problématique : un Cartographe Gris rival ; ambiguë : le client du contrat |
| **Cyril** | un serment prêté et pas encore éprouvé | « Que la parole donnée tienne, même contre moi » | établies : un Juge de Serment mentor ; un syndic des Marchands Libres ; problématique : un Lame Franche qu'il a dû faire condamner ; ambiguë : un Archiviste de Loi |
| **Pascal** | une Veille qu'il a quittée à contrecœur | « Retrouver ma place sur un seuil que je pourrai tenir » | établies : son capitaine de Guetteurs ; un forgeron de Pierres Hautes ; problématique : un Porte-Sceau qui l'a nommé en défaut ; ambiguë : un Voile Noir ? (MJ : à ne pas révéler) |

---

## 4. Taranis : le bagage de départ

**Ce que décide krunt** : Taranis part avec un bagage de départ et n'est donc pas un personnage faible au départ.

**Justification narrative [P]** : un Navigateur Gris est un Passeur : il voyage toujours prêt. Au moment du transport il était en expédition (contrat de la Guilde de Chasse, cartes du Cercle à compléter) : **il arrive avec son sac** quand les autres arrivent avec ce qu'ils portaient (`05` §4.4). Le bagage est un **avantage de départ qui s'épuise**, pas un pouvoir permanent.

**Limites imposées par les livres** [L Livre VIII ch. 9 §5, Livre IX] :
- Statut « niveaux 1-5 » : outils de base, arme simple, tenue fonctionnelle, **un** objet symbolique. Pas d'objet Supérieur (réservé aux niveaux 11-15), pas de maille, pas d'objet nommé.
- Qualité d'arme **Standard**, armure **cuir +2** (Livre IX ch. 6 et 7).
- Accessoires choisis dans la liste du Livre IX ch. 8 §1 : **carnet de pisteur** (+1 aux tests de Traque, « Guildes de chasse »). Pas de Focaliseur, pas de Boussole éthérique (Analyseurs d'Éther).
- PA : 6 maximum ; le bagage se paie avec **Préparateur Obsessionnel** (3 PA) : « avant une mission planifiée : +1 sur toutes les premières actions techniques, accès narratif à un équipement adapté ; inutilisable en situation improvisée ou d'urgence ».

**Contenu du bagage (« le Sac du Passeur »)**

| Bloc | Contenu | Règle ou limite |
|---|---|---|
| **Équipement** | Arc long Standard (1d8) ; carquois de 20 flèches [INV : les livres n'ont pas de règle de munitions] ; armure de cuir +2 ; couteau ; sac à dos avec couverture et bivouac léger ; corde de 15 m ; silex ; 2 gourdes | tout Basique ou Standard ; usure normale (Livre IX ch. 6 §3 : Endommagé après 3 combats intenses sans entretien) |
| **Outils de métier** | kit de pisteur (collets, cordelette, craie de piste) ; **instruments de cartographe** (compas, règle, plumes, encres, étui à cartes, carnets) ; **carnet de pisteur** (+1 Traque) | outils de base du niveau 1 (Chasseur : pistage simple, DD 8 ; Cartographe : relevé basique, DD 8 [L Livre VII]) |
| **Savoirs** | **Carnet des Routes** : croquis de ses propres itinéraires, la moitié sud et est des Marches, **avec une zone blanche aux Ravins de Keth** (carte à compléter) ; **signes de piste des Gris** (le code des Passeurs) ; notes sur les créatures de rang I-II (Connaissance (créatures) 1) | savoir narratif : le MJ donne l'information, aucune réussite automatique ; une carte « incomplète et volontairement fausse par endroits » est le style des Cartographes Gris [L Livre V clan 10] |
| **Ressources** | 120 Éclats [INV] ; 7 jours de rations, 2 jours d'eau (les autres : 3 rations, 1 jour) ; 2 doses d'Herbe Stabilisante (+2 Vitalité, DD 10 [L Livre VII, recettes de soin]) ; la lettre d'un contrat de la Guilde de Chasse en cours | **consommables finis** : vers J10 il ne reste que les compétences et les outils |
| **Objet symbolique** | la **boussole éteinte** (aiguille immobile) | piste de trame [INV] : l'aiguille bouge près de l'entité (à n'activer que si krunt le veut) [V3] |
| **Contrepartie** | **Dette de Sang envers le Cercle des Boussoles Éteintes** : les instruments et les cartes sont prêtés ; il doit rapporter l'information (hook « La Route Impossible », Livre V clan 10) | handicap Majeur gratuit, activé au moins une fois par arc |

**Effet sur l'équilibre.** Taranis perd 1 AGI (12 vers 11) au profit de END (5 vers 6), comme `04` §6.4 point 3 le prévoyait si l'archer écrasait Krunt3 ; il perd la Résonance de départ et le rang « Étincelle » devient **tempéré** (multiplicateur d'XP 1,15 au lieu de 1,25, PS de départ 1, voir §8). Son avantage de départ est **temporaire et fini** : le but est qu'il soit un guide compétent en première semaine, pas un personnage meilleur pour toute la campagne.

---

## 5. Pascal : l'ordre le plus cohérent, et l'attaque de base seule

### 5.1 Les trois candidats

| Candidat | Ce que disent les livres | Pour Pascal (Sceau Pourpre, Hautes Terres, Guilde Martiale, Alchimiste, Garde Mobile) | Défaut |
|---|---|---|---|
| **A. Sentinelles du Pacte** (ordre à créer, fiche `03` §3.4) | [INV] construite avec des briques du Livre V : Guerre des Pactes Brisés (fondatrice du Sceau Pourpre), Gardiens de Crête des Pierres Hautes, Exécuteurs Mandatés du Sceau, Cols de l'Atlas | **La seule qui réunit les trois attaches de Pascal** : clan Sceau Pourpre (pactes), région Hautes Terres (cols, Gardiens de Crête), Guilde Martiale (contrats de garnison). Reprend le nom et la philosophie du VTT de krunt (« Protection des frontières »). Emplacement libre : le tableau Livre V §5 donne « — » comme ordre actif des **Marches Frontalières**. Hooks prêts (« Le Seuil Sans Nom », « La Relève qui ne vient pas »). | à ajouter à StoryForge ; invention |
| **B. Culte des Ancêtres Veilleurs** (canonique) | [L] ordre actif des Hautes Terres (Livre V §5, Livre II) ; les Veilleurs légitiment les serments devant les ancêtres ; **pas de fiche** dans Livre V ch. 5 | Cohérent avec les serments du Sceau, et écho direct du **rite funéraire** (piste C de la technique) | religion, pas un ordre armé ; **aussi sans fiche** : StoryForge devrait la compléter de toute façon ; rien pour la frontière ni pour l'Alchimiste |
| **C. Ordre du Flux** (canonique, Cœur Impérial) | [L] Livre V ch. 5 ; allié du Sceau Pourpre | Lien historique avec le Sceau (le Conclave inclut des prêtres du Flux [L Livre V clan 1]) | **c'est l'antagoniste validé** : y mettre un joueur révèle la piste ou la brouille |

Écartés : Gardiens Sylvestres (frontière naturelle, harmonie), Frères de l'Épreuve (déjà à Krunt3).

### 5.2 Recommandation [P]

**A : Sentinelles du Pacte.** `ordre-nom` = « Sentinelles du Pacte », `ordre-philo` = « Veiller les seuils : nul ne passe sans être nommé » (`03` §3.4). Raisons : (1) c'est le choix de krunt ; (2) aucun ordre canonique ne couvre « la frontière sous pacte » (`03` §3.3) ; (3) la fiche est construite **uniquement** avec des matériaux du Livre V, donc elle s'insère sans contredire les livres ; (4) elle donne à Pascal un **conflit de loyauté** : un phénomène qui fait traverser des inconnus sans passer aucun seuil viole le principe de son ordre, et un Guetteur doit « nommer » Krunt (`03` §3.4, « Lien avec la trame ») ; (5) elle évite l'Ordre du Flux. **Repli** si krunt ne veut pas ajouter d'ordre : B, Culte des Ancêtres Veilleurs, en ajoutant une fiche courte à StoryForge (de toute façon manquante). Ajouter : « Sentinelles du Pacte » dans le tableau Livre V §5 (Marches Frontalières, ordre actif) et un alias dans les listes du VTT. [V4]

Remarque pour le MJ (ne pas révéler aux joueurs) : le Sceau Pourpre est issu en partie de prêtres du Flux [L Livre V clan 1] et allié de l'Ordre du Flux ; Cyril et Pascal ont donc, par leur clan, un lien lointain avec l'antagoniste. C'est une piste, pas un fait de fiche.

### 5.3 « Seulement l'attaque de base avant ses bombes »

| Élément | Traitement |
|---|---|
| Technique d'École rang I | *Garde Haute* [L] : −3 aux dégâts reçus, **pas d'attaque** : c'est une Technique défensive, donc compatible avec la décision |
| Métier Alchimiste ★1 | [L Livre VII] niveau 1 : potions mineures ; niveau 2 : antidotes simples ; niveau 3 : potions stables ; **niveau 4 : bombes légères** ; niveau 8 : bombes alchimiques. Avant le niveau 4 : **aucune Technique offensive** |
| Offensive de Pascal | **attaque de base** (épée 1d6, d20 + FOR + Corps-à-corps) uniquement |
| Techniques de Posture Loup | les quatre sont des Techniques de **soutien collectif** ; *Flanc Coordonné* ajoute un d6 si un allié a déjà frappé la cible. Lecture souple : on les laisse (la Posture est une règle de création). Lecture stricte : reporter *Flanc Coordonné* au rang II. [V9] |
| Première bombe | niveau 4 du métier, soit environ **10 % de l'histoire** pour le profil Roc (`04` §5.3 : niveau 4 à 10 %) |
| Incohérence [L] | Livre VII : bombes légères niveau 4 et bombes alchimiques niveau 8 ; Livre X ch. 6 : bombes alchimiques **rang 5**. Je retiens le Livre VII (le niveau 4 est le premier palier utile) |

Cela rend Pascal volontairement **plus faible en attaque en Acte I** (déjà noté `04` §6.4 point 4). Compensations : Défense 18, Vitalité 12, *Garde Haute*, potions et Herbe Stabilisante, ravitaillement de survie. Ne pas lui donner la *Bombe de Feu* de départ (idée de `04`), puisque krunt demande l'attaque de base seule.

---

## 6. Krunt3 : l'école la plus proche de « Deux Lames »

Examen du Livre VI [L], chapitre « Écoles Martiales » et §5 de compatibilité :

| Candidate | Arme (Livre IX) | Mode | Tabou | Compatibilité Ours (Livre VI §5) | Verdict |
|---|---|---|---|---|---|
| **Danse Rouge** | **Double Lame** 1d6+1d6 | Flux | **Perdre le contrôle de soi** | « tension créative : ancrage contre vitesse » | **Retenue** |
| Mutation | Hache-Épée (une arme à deux formes) | Flux | S'enfermer dans une seule forme | non listée | écartée : c'est l'arme de l'ancien sprite, rejeté |
| Coup Final | Grande Lame (deux mains) | Ancrage | Frapper sans intention de conclure | non listée | écartée : deux mains |
| Mur Vivant / Fracas Juste | Lance / Marteau | Ancrage | | **naturellement compatibles Ours** | écartées : plus rien de « Deux Lames » |

**Danse Rouge est la seule école à deux lames** ; son **tabou** (« perdre le contrôle de soi ») fait écho à l'entité qui l'habite, et sa Technique de rang V (*Transe Écarlate*, Avantage sur toutes les attaques, mais « tu ne peux pas te défendre ») est un thème de trame prêt à l'emploi. Le Livre VI classe Ours + Danse Rouge en « tension créative » : c'est une **tension assumée**, pas une impossibilité (« pas de contrainte mécanique, mais cohérence attendue »). Je n'ai donc pas de meilleure proposition. Le sprite doit refléter l'école : **deux lames courtes**.

À noter : `05` §2.3 fait allumer le Feu des Noms avec une « école de feu, mode Sacrifice » de Krunt ; Krunt3 n'a pas d'école de feu (Danse Rouge est en mode Flux). Le rite est un rite de clan, pas une Technique d'École : à réécrire dans `05` (ce n'est pas l'objet de ce document). [V10]

---

## 7. Les quatre fiches v2 en JSON (clés du VTT)

**Mode d'emploi.** Le bloc principal ne contient que des clés observées dans la base du VTT (`attr-*`, `gauge-*`, `clan-*`, `guilde-*`, `ordre-*`, `ecole`, `tech-ecole`, `posture`, `tech-posture`, `m1-nom`, `m1-stars-val`, `region`, `region-elem`, `arme-*`, `eclats`). L'objet `_extras` contient des clés **proposées** (non observées) : à renommer selon l'export réel de CharForge ou à retirer. `tech-ecole` et `tech-posture` contiennent la **Technique** de rang I (`03` §7.3 : ce sont des libellés de sélection de technique, pas des noms d'école). `tension` et `forge` sont retirés des fiches (jauges collectives) ; `gauge-ten` et `gauge-forge` sont conservés à 0 par compatibilité avec le VTT. Les clés `attr_*` (tiret bas) de Krunt3 sont à synchroniser ou à supprimer. Aucun champ `joueur`.

### 7.1 Krunt3

```json
{
  "nom": "Krunt3",
  "attr-for": 9, "attr-agi": 8, "attr-end": 9, "attr-esp": 4, "attr-vol": 7, "attr-pre": 6,
  "gauge-vit": 13, "gauge-end": 10, "gauge-mana": 6, "gauge-hon": 4, "gauge-ten": 0, "gauge-forge": 0,
  "clan-nom": "Lames Franches",
  "clan-devise": "Nul ne nous commande. Nul ne nous possède.",
  "guilde-nom": "Guilde Martiale",
  "guilde-spec": "Guerre contractuelle (Officiers-Loges : discipline et soldes)",
  "ordre-nom": "Frères de l'Épreuve",
  "ordre-philo": "Juger par l'épreuve : seuls ceux qui ont prouvé leur valeur jugent les autres",
  "ecole": "Danse Rouge",
  "tech-ecole": "Fuite Tranchante",
  "posture": "Ours",
  "tech-posture": "Interposition",
  "m1-nom": "Espion / Infiltrateur",
  "m1-stars-val": 1,
  "region": "Îles des Serments",
  "region-elem": "—",
  "arme-nom": "Double Lame",
  "arme-degats": "1d6+1d6",
  "eclats": 30,
  "_extras": {
    "ordre-surnom": "Ordre du Jugement",
    "ecole-vtt-ancien": "Deux Lames",
    "ecole-rang": 1,
    "mana-mode": "Flux",
    "tabou-ecole": "Perdre le contrôle de soi",
    "tech-posture-liste": ["Interposition", "Ancrage (Ours)", "Provocation", "Mur de Chair"],
    "m1-variante": "Occulte",
    "m2-nom": "",
    "competences": {"corps_a_corps": 3, "esquive_active": 3, "discretion": 3, "resistance": 2, "intimidation_froide": 2, "tromperie": 1, "perception": 1, "athletisme": 1, "resistance_mentale": 1},
    "avantages": ["Maîtrise de Combat (Danse Rouge)", "Vision Éthérique", "Réflexes Affûtés", "Récupération Accélérée", "Posture Défensive"],
    "handicaps": ["Réceptacle (unique, remplace le Majeur gratuit)", "Dette de Sang : créancier du pacte (contenu fixé par la trame révisée)"],
    "pa-total": 9,
    "armure": "Armure légère (cuir) +2",
    "defense-avec-armure": 19,
    "objet-symbolique": "Cordon rouge coupé noué au poignet",
    "profil-progression": "Pacte",
    "role": "Héros, fer de lance (PNJ pendant les phases de JDR)",
    "sprite-ref": "docs/trame/08-fiches-v2-et-sprites.md §9.1"
  }
}
```

### 7.2 Taranis

```json
{
  "nom": "Taranis",
  "attr-for": 5, "attr-agi": 11, "attr-end": 6, "attr-esp": 9, "attr-vol": 6, "attr-pre": 5,
  "gauge-vit": 10, "gauge-end": 10, "gauge-mana": 6, "gauge-hon": 4, "gauge-ten": 0, "gauge-forge": 0,
  "clan-nom": "Navigateurs Gris",
  "clan-devise": "Là où la route meurt, nous avançons encore.",
  "guilde-nom": "Guilde de Chasse",
  "guilde-spec": "Contrats de chasse, formation",
  "ordre-nom": "",
  "ordre-philo": "",
  "ecole": "Souffle Long",
  "tech-ecole": "Tir Ciblé",
  "posture": "Loup",
  "tech-posture": "Flanc Coordonné",
  "m1-nom": "Chasseur-Pisteur",
  "m1-stars-val": 1,
  "region": "Déserts Rouges",
  "region-elem": "Vent",
  "arme-nom": "Arc long",
  "arme-degats": "1d8",
  "eclats": 120,
  "_extras": {
    "ecole-vtt-ancien": "Arc Précis",
    "ecole-rang": 1,
    "mana-mode": "Rituel",
    "tabou-ecole": "Tirer sans cible claire",
    "tech-posture-liste": ["Appel de Meute", "Flanc Coordonné", "Présence Rassurante", "Sacrifice de Meute"],
    "m1-variante": "Désertique",
    "m2-nom": "Cartographe", "m2-stars-val": 1, "m2-variante": "Explorateur",
    "competences": {"tir_et_lancers": 3, "traque": 3, "perception": 3, "connaissance_cartographie_geographie": 3, "marche_forcee": 2, "discretion": 1, "esquive_active": 1, "connaissance_creatures": 1},
    "avantages": ["Préparateur Obsessionnel", "Réflexes Affûtés", "Réseau Local (Marches Frontalières)", "Improvisation Pratique"],
    "handicaps": ["Dette de Sang envers le Cercle des Boussoles Éteintes (Majeur gratuit)"],
    "pa-total": 6,
    "armure": "Armure légère (cuir) +2",
    "defense-avec-armure": 19,
    "bagage-depart": {
      "equipement": ["Arc long Standard 1d8", "Carquois de 20 flèches", "Armure de cuir +2", "Couteau", "Sac à dos, couverture, bivouac léger", "Corde 15 m", "Silex", "2 gourdes"],
      "outils-metier": ["Kit de pisteur", "Instruments de cartographe", "Carnet de pisteur (+1 Traque)"],
      "savoirs": ["Carnet des Routes (Marches sud et est, zone blanche aux Ravins de Keth)", "Signes de piste des Gris", "Notes sur les créatures de rang I-II"],
      "ressources": {"eclats": 120, "rations-jours": 7, "eau-jours": 2, "herbe-stabilisante": 2, "lettre-contrat-guilde-chasse": 1},
      "objet-symbolique": "Boussole éteinte",
      "contrepartie": "Dette de Sang (Cercle des Boussoles Éteintes) ; consommables finis (épuisés vers J10)"
    },
    "profil-progression": "Étincelle tempéré",
    "jalons-ecole-pct": [10, 25, 55, 85],
    "xp-metier-mult": 1.15, "ps-depart": 1, "plafond-attribut": 16,
    "role": "Éclaireur-cartographe, tireur",
    "sprite-ref": "docs/trame/08-fiches-v2-et-sprites.md §9.2"
  }
}
```

### 7.3 Cyril

```json
{
  "nom": "Cyril",
  "attr-for": 5, "attr-agi": 6, "attr-end": 6, "attr-esp": 8, "attr-vol": 9, "attr-pre": 8,
  "gauge-vit": 10, "gauge-end": 10, "gauge-mana": 8, "gauge-hon": 5, "gauge-ten": 0, "gauge-forge": 0,
  "clan-nom": "Sceau Pourpre",
  "clan-devise": "Un serment scellé vaut plus qu'une armée.",
  "guilde-nom": "Marchands Libres",
  "guilde-spec": "Crédit, dette et voies commerciales",
  "ordre-nom": "",
  "ordre-philo": "",
  "ecole": "Flux Tranchant",
  "tech-ecole": "Première Vague",
  "posture": "Loup",
  "tech-posture": "Présence Rassurante",
  "m1-nom": "Mage Blanc",
  "m1-stars-val": 1,
  "region": "Cœur Impérial",
  "region-elem": "Métal",
  "arme-nom": "Épée Longue",
  "arme-degats": "1d8",
  "eclats": 90,
  "_extras": {
    "ecole-vtt-ancien": "Lame Droite",
    "ecole-rang": 1,
    "mana-mode": "Flux",
    "tabou-ecole": "Briser volontairement le flux",
    "tech-posture-liste": ["Appel de Meute", "Flanc Coordonné", "Présence Rassurante", "Sacrifice de Meute"],
    "m2-nom": "",
    "competences": {"medecine": 3, "concentration": 3, "persuasion": 3, "corps_a_corps": 2, "connaissance_droit_serments": 2, "representation": 1, "resistance_mentale": 1, "perception": 1, "esquive_active": 1},
    "avantages": ["Nom Respecté", "Canal Stable (−1 PA, synergie Mage Blanc)", "Résistance Partielle"],
    "handicaps": ["Serment Absolu : ne jamais rompre un serment prêté (Majeur gratuit)"],
    "pa-total": 6,
    "armure": "Vêtements renforcés +1",
    "defense-avec-armure": 13,
    "objet-symbolique": "Sceau de cire de famille, jamais utilisé",
    "profil-progression": "Graine",
    "jalons-ecole-pct": [20, 40, 70, 95],
    "xp-metier-mult": "1.0 jusqu'au niveau 10, puis 1.5", "ps-depart": 1, "plafond-attribut": "20 sur ESP/VOL/PRE, 16 sinon",
    "posture-legendaire-visee": "Dragon Azur (Honneur ≥ 7)",
    "role": "Soin, serment, voix",
    "sprite-ref": "docs/trame/08-fiches-v2-et-sprites.md §9.3"
  }
}
```

### 7.4 Pascal

```json
{
  "nom": "Pascal",
  "attr-for": 7, "attr-agi": 6, "attr-end": 8, "attr-esp": 9, "attr-vol": 6, "attr-pre": 7,
  "gauge-vit": 12, "gauge-end": 10, "gauge-mana": 6, "gauge-hon": 6, "gauge-ten": 0, "gauge-forge": 0,
  "clan-nom": "Sceau Pourpre",
  "clan-devise": "Un serment scellé vaut plus qu'une armée.",
  "guilde-nom": "Guilde Martiale",
  "guilde-spec": "Capitaineries de défense (garde, siège)",
  "ordre-nom": "Sentinelles du Pacte",
  "ordre-philo": "Veiller les seuils : nul ne passe sans être nommé",
  "ecole": "Gardien Mobile",
  "tech-ecole": "Garde Haute",
  "posture": "Loup",
  "tech-posture": "Sacrifice de Meute",
  "m1-nom": "Alchimiste",
  "m1-stars-val": 1,
  "region": "Hautes Terres Claniques",
  "region-elem": "Terre",
  "arme-nom": "Épée et Bouclier",
  "arme-degats": "1d6",
  "arm-pieds-nom": "Bottes de marche renforcées",
  "arm-pieds-def": "0",
  "arm-pieds-effet": "Blessure Ancienne : −2 à courir",
  "arm-pieds-etat": "Standard",
  "arm-pieds-mat": "cuir",
  "eclats": 60,
  "_extras": {
    "ecole-vtt-ancien": "Lame Droite",
    "ecole-rang": 1,
    "mana-mode": "Ancrage",
    "tabou-ecole": "Abandonner un allié protégé",
    "ordre-repli": "Culte des Ancêtres Veilleurs (si les Sentinelles du Pacte ne sont pas ajoutées à StoryForge)",
    "tech-posture-liste": ["Appel de Meute", "Flanc Coordonné", "Présence Rassurante", "Sacrifice de Meute"],
    "m1-variante": "Martiale",
    "m2-nom": "",
    "competences": {"artisanat_alchimie": 3, "connaissance_alchimie_plantes": 3, "resistance": 3, "corps_a_corps": 2, "perception": 1, "athletisme": 1, "commandement": 1, "medecine": 1, "resistance_mentale": 1, "esquive_active": 1},
    "avantages": ["Corps Endurci", "Ingénieur Méthodique (sans synergie, à valider)", "Économie de Matériaux"],
    "handicaps": ["Blessure Ancienne (courir −2, Majeur gratuit)", "Code Personnel Rigide : on ne quitte pas sa Veille (+1)"],
    "pa-total": 7,
    "armure": "Armure légère (cuir) +2 ; bouclier +2 (inclus dans Épée et Bouclier)",
    "defense-avec-armure": 18,
    "offensive-avant-bombes": "attaque de base uniquement (Garde Haute est défensive)",
    "premiere-bombe": "niveau 4 du métier (bombes légères, Livre VII)",
    "objet-symbolique": "Lanterne de Guetteur en fer",
    "profil-progression": "Roc",
    "jalons-ecole-pct": [25, 50, 80, 100],
    "xp-metier-mult": 0.8, "ps-depart": 2, "plafond-attribut": 14,
    "role": "Rempart alchimiste",
    "sprite-ref": "docs/trame/08-fiches-v2-et-sprites.md §9.4"
  }
}
```

---

## 8. Corrections par rapport au document 04

| # | Sujet | Document 04 (v1) | v2 | Raison |
|---|---|---|---|---|
| 1 | **Ordre de Krunt3** (JSON §9.1) | Frères de l'Épreuve déjà dans l'en-tête, « Dettes et correction (Arbitres du Flux) » en `ordre-philo` | Frères de l'Épreuve, philosophie « Juger par l'épreuve… » ; « Ordre du Jugement » = surnom | décision de krunt ; l'Ordre du Flux est l'antagoniste, pas l'ordre de Krunt3 |
| 2 | **Métier de Taranis** | Espion/Infiltrateur + Chasseur-Pisteur secondaire | **Chasseur-Pisteur** principal + **Cartographe** secondaire | décision de krunt ; lève le doublon d'Espion avec Krunt3 |
| 3 | **Résonance de Taranis** | Faucon : *Point Faible* dès le départ + avantage unique « Ancien Faucon » | retirées | une Résonance vient d'un **changement de Posture par jalon** [L Livre VI] ; elle ne s'acquiert pas à la création ; l'avantage unique inutile avec le bagage |
| 4 | **Attributs de Taranis** | 5/12/5/9/6/5 (Vit 9) | 5/**11**/**6**/9/6/5 (Vit **10**) | le bagage compense la fragilité ; `04` §6.4 point 3 prévoyait ce transfert si l'archer dominait |
| 5 | **Taranis, PA** | Ancien Faucon (3) + 3 mineurs | **Préparateur Obsessionnel** (3) + 3 mineurs | exprime le bagage (§4) |
| 6 | **Région de Taranis** | Marches Frontalières | **Déserts Rouges** | il ne doit pas être « chez lui » au lieu d'arrivée (`03` §2.1, `05` §4.2) ; conserve l'esprit « steppe à vent » du VTT |
| 7 | **Éclats de départ** | 100 / 80 / 150 / 250 | **30 / 120 / 90 / 60** | pas de règle dans les livres ; Pascal à 250 était incompatible avec le statut « niveaux 1-5 » ; seul Taranis porte un surplus |
| 8 | **Armure de Pascal** | maille +3 (Défense 19) | **cuir +2** + bouclier +2 (Défense **18**) | la maille demande un forgeron de niveau 8-15 ; « niveaux 1-5 = tenue fonctionnelle » [L Livre VIII ch. 9 §5, Livre IX ch. 7] |
| 9 | **Équipement « Supérieur » de Roc** | « une pièce de qualité Supérieure » | retiré | « Niveaux 11-15 : 1 objet de qualité supérieure » [L Livre VIII ch. 9 §5] |
| 10 | **Pascal, PA** | Corps Endurci + Ingénieur Méthodique (−1 synergie) + Économie + Posture Défensive = 7 | Corps Endurci + Ingénieur Méthodique (**sans synergie**) + Économie = 7 | le Livre VIII ne cite la synergie qu'avec un Forgeron d'Armures ; à valider |
| 11 | **Pascal, ordre** | Culte des Ancêtres Veilleurs | **Sentinelles du Pacte** (repli : Culte) | choix de krunt ; fiche déjà écrite |
| 12 | **Pascal, points de savoir** | 4 PS « déjà dépensés dans le kit » | 2 PS | le kit est limité par le Livre VIII |
| 13 | **Pascal, attaque** | Bombe de Feu de départ proposée | attaque de base seule jusqu'au niveau 4 | décision de krunt |
| 14 | **Krunt3, compétences** | Discrétion 2, Commandement 1, Perception 1, Athlétisme 1, Résistance mentale 1 | Discrétion **3**, **sans Commandement** | un Espion doit être fort en Discrétion ; chez les Lames « aucun membre ne peut commander un autre sans son consentement » [L Livre V clan 2] |
| 15 | **Krunt3, Dette de Sang** | « Dette de Sang (le Pacte) » ; prix implicite (noms) | dette au « créancier du pacte » : la Braise et la Dette du Flux | le coût par l'oubli de noms est retiré (décision de krunt) |
| 16 | **Krunt3, Réceptacle** | handicap unique présenté comme malédiction | formulation neutre (l'entité ne le maudit peut-être pas) | décision de krunt du 2026-10-06 |
| 17 | **`tech-ecole`, `tech-posture`** | nom de l'école, nom de la Posture | **Technique** de rang I et Technique d'ouverture | `03` §7.3 |
| 18 | **`ordre-philo` de Cyril** | vide | vide, mais l'option « Ordre du Flux » est écartée explicitement | antagoniste validé |
| 19 | **Cyril, PA** | 3 + 2 + 1 = 6 | identique (comptabilité rendue explicite : 6 PA disponibles, 6 dépensés) | clarté |
| 20 | **Tension de Krunt3** | 1 dans la fiche test | 0 ; Tension et Forge hors fiche | jauges collectives [L Livre I ch. 2] |

**Inchangés par rapport au document 04** : attributs de Krunt3, Cyril et Pascal, Mana, Défense de Krunt3 et de Cyril, techniques de Posture, profils Pacte, Graine et Roc (hors les PS de Pascal), école de Pascal (Gardien Mobile, retenue en `03`), école de Cyril (Flux Tranchant), recrues A et B.

---

## 9. Sprites : briefs et prompts PixelLab

### 9.1 Principes communs

**Format retenu** [L `bible-graphique.md`, scénario C provisoire] : héros de profil dans une case de **128** (personnage d'environ **64 px** de haut, ligne de sol à 1/16 de la case) ; vue 3/4 « low top-down » dans une case de **64** (personnage d'environ **48 px**) ; palette de **32 couleurs maximum** par personnage, **commune** au profil et au 3/4 ; contour sombre de 1 px ; ombrage plat à deux tons par matière. Sur l'essai gratuit : case 64 pour le profil, case 48 pour le 3/4 (le personnage remplit la case ; `test-pixellab.md`, essais 1 ter et 3/4 v2 à 44 px).

**Consignes de simplification** [L `prompts-personnages.md`, v2] : aplats larges à deux tons, **armure à plaques plates** (jamais de maille, d'écailles ni de rivets), peu de détails, une seule instruction d'image par ligne, pas de motif.

**Ligne de style commune (à reprendre mot pour mot dans les quatre prompts)** :

```
Very simple design for a tiny sprite: large flat color areas with only two tones per material, a few big flat plates, no chainmail, no scale pattern, no rivets, no small details. Large readable head, simplified face with clear eyes, face clearly lit, strong readable silhouette. Clean pixel art, selective dark outline of one pixel, flat shading with only two tones per material, limited palette of about 24 colors, no anti-aliasing, no gradients, no dithering, no noise, no texture, transparent background.
```

**Champ négatif commun** : `scales pattern, chainmail pattern, rivets, small details, texture, noise, speckle, gradients, blurry, 3D render, painting, photo, text, watermark, cropped, extra limbs`.

**Fin de prompt, vue de profil** : `Side view facing right, idle standing pose.`
**Fin de prompt, vue 3/4** : `Seen in a three-quarter top-down view, camera slightly above, like a classic 16-bit action RPG. Idle standing pose.`
(Réglages vus aux essais : vue « low top-down », 4 directions suffisent en 3/4 avec le miroir ; modèle « mannequin » ; ne pas fixer de hauteur à l'outil, la mesurer ensuite avec `outils/mesure_sprite.py`.)

**Pour que les quatre soient distincts en ombre chinoise**, chacun a une forme dominante différente et aucune ne dépasse sa zone :

| | **Krunt3** | **Taranis** | **Cyril** | **Pascal** |
|---|---|---|---|---|
| Forme dominante | trapèze renversé large et bas | rectangle haut et étroit avec une bosse dans le dos | colonne qui s'évase en cloche | carré court avec un disque |
| Hauteur de profil (viser) | 64 px | 64 px (arc compris) | 62 px | **58 px** (plus court) |
| Largeur maximale de profil (viser) | **~44 px** (manteau + lames) | **~30 px** (sac + arc) | **~28 px** (manteau évasé) | **~38 px** (bouclier de ~20 px) |
| Rapport largeur / hauteur | 0,69 | 0,47 | 0,45 | 0,66 |
| Sommet | tête nue, épaules de fourrure arrondies, **rien au-dessus de la tête** | **capuche pointue + arc vertical** qui dépasse | tête nue, col haut, cheveux courts | **casque rond** bas |
| Bas | jambes écartées, pans de tissu rouge | jambes fines, écharpe flottante | **pans de manteau évasés** cachent les jambes | bottes courtes, **jambe gauche raide** |
| Ligne forte | deux **horizontales** (lames aux hanches) | **verticale** de l'arc, **diagonale** du tube à cartes | **diagonale** de l'épée au côté, étole verticale | **cercle** du bouclier, bandoulière de fioles |
| Coupes gabarit de 3/4 (48 px) | 48 de haut, ~34 de large | 48 de haut, ~24 de large | 47 de haut, ~22 de large | 44 de haut, ~30 de large |

**Test d'ombre chinoise** : remplir chaque sprite en noir sur fond clair, les aligner côte à côte à 64 px de haut ; chaque forme doit se reconnaître en une seconde. Refuser tout résultat où deux silhouettes se ressemblent (par exemple Cyril et Taranis, tous deux étroits : l'arc vertical et le sac contre le manteau évasé et l'épée doivent les séparer).

**Couleurs dominantes** (pour qu'aucun ne se confonde en miniature) : Krunt3 **rouge brique et brun charbon** ; Taranis **gris cendre et sable, accent turquoise** ; Cyril **crème et pourpre prune, accent or** ; Pascal **bleu acier et vert olive, accent ambre**. Cyril et Pascal partagent le pourpre (clan Sceau Pourpre) : dominant chez Cyril, un simple brassard chez Pascal.

### 9.2 Krunt3

**Concept (cohérent avec la fiche).**
- **Région Îles des Serments** [L Atlas Région 6] : archipel subarctique, vents, pins rabougris, os et dents de créatures marines, fourrures locales, austérité (« aucun ornement superflu ») : un **manteau de fourrure pâle** sur les épaules, des **amulettes d'os**, aucun bijou.
- **Épreuve des Frères** : l'épreuve d'initiation est une nuit dans le territoire d'un Fennak des Glaces : **trois cicatrices de griffes parallèles** sur la joue gauche (détail lisible dès 64 px par trois pixels clairs).
- **Clan Lames Franches** [L Livre V clan 2] : « une lame ne doit jamais être liée à vie » : un **cordon rouge coupé** noué au poignet (trois pixels). Aucun emblème de clan.
- **Posture Ours** : corps large, penché en avant, jambes écartées, **centre de gravité bas**.
- **École Danse Rouge** : **deux lames courtes recourbées** (une dans la main proche, une horizontale dans le bas du dos), poignées enveloppées de **tissu rouge** dont les pans flottent (lecture de la vitesse sans mouvement).
- **Métier Espion/Infiltrateur occulte** : sous la fourrure (amovible), une tenue sombre et neutre à capuche baissée : « un Espion commence sans rien de compromettant sur lui » [L Livre VIII ch. 9 §5]. Contraste voulu : un colosse qui n'a pas l'air d'un espion.
- **Rôle** : héros, fer de lance, tenue de survivant.
- **Visage** : la fiche décrit l'ancien sprite avec une **barbe rousse tressée** : je la **garde** (signe d'identité) ; âge ~35 ans, regard sombre et calme.
- **Peau** : l'ancien sprite avait la **peau rouge**. Je propose une **peau hâlée et rougie par le vent** (rouge brique doux) pour que le rouge reste l'identité de la palette sans rendre la peau irréelle. [V11 : si krunt tient à une peau rouge franche, remplacer les trois tons de peau par un rouge plus saturé, la palette le permet]
- **Abandonné** : la hache à deux mains (rien au-dessus de la tête ; silhouette large et basse, pas haute).

**Détails distinctifs (à garder à 64 px)**, par priorité : (1) manteau de fourrure pâle aux épaules ; (2) barbe rousse tressée ; (3) deux lames et pans de tissu rouge ; (4) trois cicatrices ; (5) cordon rouge au poignet (peut disparaître à 48 px).

**Prompt PixelLab, vue de profil (case 128, personnage ~64 px)**

```
A heavy-set human warrior in his mid-thirties, very broad shoulders, hunched forward bear-like stance, ruddy wind-burnt skin, short copper-red hair, a thick copper-red braided beard, three parallel claw scars on the left cheek, stern calm expression. He wears a big pale gray fur mantle over both shoulders forming one wide rounded shape, a dark charcoal-brown jerkin with one big flat steel shoulder plate on the left and plain flat steel bracers, a brick-red cloth sash at the waist with two short red cloth tails, dark trousers and brown boots, a small cut red cord on the wrist. He holds one short curved sword low in the hand nearest the viewer, and a second short curved sword lies horizontally across the lower back, red cloth wrapped on both hilts. No two-handed weapon, nothing above the head. Wide low stance. Dominant colors: brick red and charcoal brown; accents: bone cream and pale fur gray.
[LIGNE DE STYLE COMMUNE]
Side view facing right, idle standing pose.
```

**Prompt PixelLab, vue 3/4 (case 64, personnage ~48 px)** : même texte, avec : `Wide low stance, broad shoulders seen from slightly above.` et la fin 3/4 de §9.1. Si le résultat est trop chargé : supprimer les cicatrices et le cordon (garder fourrure, barbe, lames, pans rouges).

**Déclinaison « porteur de la malédiction » (signes visibles discrets d'une entité, sans spoiler)**

Principe : des signes **ambigus**, qui peuvent se lire comme une maladie, une bénédiction ou une fièvre. **Aucune plume, aucun oiseau, aucune flamme, aucune aile, aucune aura, aucun œil lumineux** : rien qui nomme l'entité ni la piste du phœnix. Les signes ne se voient que **de près** et augmentent par paliers (le palier suit un compteur de trame, `05` §3.1 : marques visibles à partir d'un seuil intermédiaire, visibles de tous à un seuil haut, valeurs hypothétiques).

| Palier | Signes | Pixels en jeu |
|---|---|---|
| **A, sans signe** | sprite normal | 0 |
| **B, discret** (variante demandée) | **veines chaudes** : fins traits orange doux sur le cou et le dos des mains (2 à 4 pixels par zone) ; **une mèche gris cendre** au temple gauche (3 à 5 pixels) ; **reflet chaud** dans l'œil visible (1 pixel orange) ; **2 à 3 braises minuscules** qui dérivent près de l'épaule (pixels isolés, animés) | ~15 à 20 pixels |
| **C, visible** | les mêmes signes, veines plus longues remontant sur les avant-bras et le menton, mèche grise plus large, 4 à 6 braises, **cendre claire** déposée sur la fourrure | ~40 à 50 pixels |

**Méthode (recommandée) : calque de retouche, pas une nouvelle génération.** Générer le sprite normal, puis dessiner les signes dans **PixelForge** avec les **quatre couleurs de braise réservées** de la palette (§9.6). Raisons : même silhouette et même palette garanties, coût nul en générations, et PixelLab a tendance à inventer des flammes ou une aura à la place de quelques pixels. Animation : les braises sont des pixels isolés qui montent de 1 à 2 px sur 6 images ; les veines pulsent entre deux tons.

Prompt de secours si l'on doit régénérer (ajouté à la fin du prompt du personnage, **avant** la ligne de style) :

```
Add very subtle signs only: thin warm orange glowing veins on the neck and on the back of both hands, a single ash-gray streak in the hair at the left temple, a faint warm orange glint in the visible eye, two or three tiny ember pixels drifting near the left shoulder. Everything else stays identical. No flames, no wings, no feathers, no aura, no glow outline, no horns.
```

Champ négatif additionnel : `flames, fire, wings, feathers, bird, aura, halo, glowing eyes, horns, blood, skull`.

### 9.3 Taranis

**Concept.**
- **Région Déserts Rouges** [L Atlas Région 9] : plateau aride, poussière rouge, vent, silence (« le silence est une langue ») : tons **sable** et **cendre**, un **foulard** qui couvre le bas du visage, pas de bavardage visuel.
- **Clan Navigateurs Gris** [L Livre V clan 10] : **gris** (« ils n'appartiennent jamais entièrement à un pouvoir ») ; Cartographes Gris, Passeurs, Vigies du Brouillard : **cape grise à capuche pointue**, **fine ligne turquoise** (la mer, les routes) sur l'écharpe et le bord de capuche.
- **Guilde de Chasse** : pas d'emblème (économie de détails) ; le **carnet de pisteur** à la ceinture suffit.
- **Posture Loup** : mince, tendu, regard vers l'avant ; aucun motif de loup.
- **École Souffle Long** : **arc long vertical** aussi haut que lui (« voir avant d'être vu ») ; carquois à la hanche.
- **Métiers Chasseur-Pisteur désertique + Cartographe explorateur** : **tube à cartes** en bandoulière sur le dos, **boussole** au sternum (peut disparaître), carnets à la ceinture.
- **Bagage de départ** (§4) : **grand sac à dos arrondi** avec **couverture roulée** dessus et **deux gourdes** à la ceinture : c'est ce qui le distingue des trois autres, qui n'ont que ce qu'ils portaient.
- **Rôle** : éclaireur-guide, le plus mobile, le moins protégé (Vitalité 10, cuir) : tenue légère.
- **Visage** : ~28 ans, peau olive hâlée, cheveux courts sombres sous la capuche, yeux attentifs.

**Détails distinctifs par priorité** : (1) capuche pointue et pan d'écharpe qui flotte ; (2) arc long vertical ; (3) sac bossu avec couverture roulée ; (4) tube à cartes en diagonale ; (5) deux gourdes, boussole.

**Prompt, vue de profil**

```
A lean tall human scout in his late twenties, weathered olive-tan skin, short dark hair under a pointed ash-gray hood, a long gray scarf covering the lower face with one long scarf tail flowing behind, calm alert eyes. He wears an open ash-gray hooded cloak, a sand-tan tunic, a brown leather chest strap, one big flat leather plate on the right shoulder and plain flat leather bracers, brown trousers and boots. A big rounded brown backpack with a rolled sand-tan bedroll on top, a long brown map tube slung diagonally across the back, two small waterskins at the belt, a quiver on the hip. He holds a tall recurved longbow vertically in the hand nearest the viewer, as tall as his body. A thin teal stripe on the scarf end and on the hood edge. Dominant colors: ash gray and sand tan; accents: teal and a little brass.
[LIGNE DE STYLE COMMUNE]
Side view facing right, idle standing pose.
```

**Prompt, vue 3/4** : remplacer `Side view...` par la fin 3/4 de §9.1 ; si trop chargé : supprimer boussole, gourdes, carquois (garder capuche, arc, sac et couverture, tube).

### 9.4 Cyril

**Concept.**
- **Région Cœur Impérial** [L Atlas Région 1] : centre administratif, plaine cultivée, tenue formelle (« l'argument légal prime ») : **manteau long et soigné**, rien de guerrier.
- **Clan Sceau Pourpre** [L Livre V clan 1] : gouverne par la reconnaissance, le sceau, la loi écrite : **étole pourpre prune** tombant des deux épaules, **médaillon rond de sceau de cire** au sternum, **parchemin roulé** à la ceinture.
- **Guilde Marchands Libres** : une **petite bourse** à la ceinture (discrète, peut disparaître).
- **Posture Loup** : debout droit, ouvert, mains libres ; **aucune posture agressive**.
- **École Flux Tranchant** : **épée longue droite** dans un fourreau simple à la hanche gauche (« lame droite » du VTT d'origine) ; équilibre, polyvalence.
- **Métier Mage Blanc** [L Livre VII : « gardien de l'équilibre vital »] : **blanc crème** dominant, **gants blancs**, col haut, **fermoir doré** ; un petit **cristal de focalisation** inutile (aucun bâton, pour ne pas ressembler à un mage classique et rester distinct de l'arc de Taranis).
- **Rôle** : soin et voix, arrière-garde ; il paraît fragile (Défense 13).
- **Visage** : ~28 ans, peau claire, cheveux bruns courts et nets, regard calme et appliqué ; aucune barbe.

**Détails distinctifs par priorité** : (1) manteau crème évasé jusqu'aux genoux ; (2) étole pourpre et médaillon rond ; (3) épée droite au côté ; (4) gants blancs ; (5) parchemin à la ceinture.

**Prompt, vue de profil**

```
A slender human young jurist and healer in his late twenties, fair skin, short neat dark brown hair, no beard, calm attentive expression. He wears a long cream-white knee-length coat with a high collar, flaring at the hem, a plum-crimson stole hanging from both shoulders to the knees with a round plum wax-seal medallion on the chest, a small gold clasp at the collar, plain white gloves, a brown leather belt with a small rolled scroll, dark slate trousers and brown boots. A straight longsword in a plain brown scabbard on the left hip. No armor, no staff, no hat. Dominant colors: cream white and plum crimson; accents: gold and slate blue.
[LIGNE DE STYLE COMMUNE]
Side view facing right, idle standing pose.
```

**Prompt, vue 3/4** : remplacer par la fin 3/4 ; si trop chargé : supprimer parchemin, fermoir, gants (garder manteau, étole, médaillon, épée).

### 9.5 Pascal

**Concept.**
- **Région Hautes Terres Claniques** [L Atlas Région 4] : collines boisées, passes fermées l'hiver, clans de crête : **vert olive** (forêts) et **pierre**, **demi-cape à capuchon** épaisse.
- **Clan Sceau Pourpre, par adoption** : un **brassard pourpre** fin au bras gauche (signe de serment).
- **Guilde Martiale** : tenue de soldat de garnison ; aucun insigne.
- **Ordre Sentinelles du Pacte** (§5) : une **lanterne de Guetteur** en fer à la ceinture ; posture « on ne quitte pas sa Veille » : pieds plantés, bouclier en avant.
- **Posture Loup** : stable, tourné vers le groupe (bouclier orienté pour couvrir).
- **École Gardien Mobile** : **bouclier rond en bois** à ombilic de fer, large (20 px), **épée courte droite**.
- **Métier Alchimiste martial** : **bandoulière de cuir portant quatre fioles de verre** (deux ambre, deux vertes) en travers de la poitrine, **lunettes de protection relevées** sur le front, **sac de composants** ; il n'a pas encore de bombes (aucune fiole ne ressemble à une bombe).
- **Blessure Ancienne** : **jambe gauche raide**, botte renforcée de cuir et de fer, poids sur la jambe droite (lisible par une jambe plus droite que l'autre).
- **Rôle** : rempart, seconde ligne, ravitailleur : **le plus court et le plus massif** après Krunt3 en largeur.
- **Visage** : ~35 ans, peau brune, barbe courte sombre, regard sérieux.

**Détails distinctifs par priorité** : (1) grand disque de bouclier ; (2) casque rond avec lunettes relevées ; (3) bandoulière de fioles ambre et vertes ; (4) demi-cape olive ; (5) lanterne, brassard pourpre, jambe raide.

**Prompt, vue de profil**

```
A short stocky human soldier and alchemist in his mid-thirties, brown skin, short dark beard, serious expression. He wears a plain round iron cap helmet with goggles pushed up on the forehead, steel-blue armor made of a few big flat plates (breastplate, two shoulder plates, plain greaves), a short olive-green hooded half-cape on the shoulders, a brown leather bandolier across the chest holding four glass vials (two amber, two green), a small iron lantern at the belt, a thin plum-crimson armband on the upper arm. A large round wooden shield with an iron center on the arm nearest the viewer, a short straight sword in the other hand. His left leg is stiff with a thick leather and iron brace on the boot, weight on the right leg. Planted wide stance. Dominant colors: steel blue and olive green; accents: amber and a little plum crimson.
[LIGNE DE STYLE COMMUNE]
Side view facing right, idle standing pose.
```

**Prompt, vue 3/4** : remplacer par la fin 3/4 ; si trop chargé : supprimer lanterne, brassard, lunettes (garder casque, bouclier, fioles, demi-cape).

### 9.6 Palettes (32 couleurs maximum, communes au profil et au 3/4)

Valeurs de départ **choisies à la main** [INV], à réajuster dans PixelForge après la génération (réduction automatique à 32 couleurs, voir `test-pixellab.md` : 24 à 32 conserve le rendu ; l'acier prend facilement une teinte verdâtre). Le tronc commun de huit couleurs permet de garder les quatre sprites de la même famille.

**Tronc commun (8)** : contour `#1d1a24` ; blanc cassé `#f3ece0` ; acier sombre `#4a5160`, moyen `#7d8696`, clair `#b9c1cc` ; cuir sombre `#4a3022`, moyen `#7a5232`, clair `#a97b4a`.

| | Krunt3 (30) | Taranis (24) | Cyril (26) | Pascal (23) |
|---|---|---|---|---|
| Peau (3) | `#8f4a36` `#b9694a` `#d98d66` (rouge hâlé) | `#7a5a3a` `#a47b52` `#cfa174` (olive hâlé) | `#b98462` `#e1ad87` `#f4cfaa` (clair) | `#6e4430` `#946248` `#bb8661` (brun) |
| Cheveux, barbe | cuivre roux `#5a2418` `#8d3a1f` `#c2602a` | brun très sombre `#2a1f1a` `#4a3628` | brun `#2d2430` `#4d3f4a` | noir brun `#241a17` `#3d2c26` |
| Matière dominante | rouge brique `#5c1417` `#8e2420` `#c4452f` ; jerkin charbon `#2b2723` `#433a34` `#5d5149` | cape gris cendre `#4f5a58` `#7b8a86` `#a9b8b2` ; tunique sable `#8d7650` `#bda06b` `#e0cb94` | manteau crème `#7d7670` `#a79f96` `#d4cabb` `#efe7d6` ; ardoise `#4a5578` `#7787b0` | acier bleu `#3f4b63` `#647492` `#93a4c4` ; cape olive `#3b4a2c` `#5f7340` `#8da060` |
| Matière secondaire | fourrure `#5b5560` `#8e8890` `#cfc9c4` ; os `#8c8068` `#c2b79a` `#e6dcc1` | — | — | — |
| Accent | **braise réservée (4)** : `#7a2c10` `#d9531e` `#ff9b3d` `#ffd37a` (utilisées seulement par la variante porteur ; ne pas les employer ailleurs) | turquoise `#1f5f66` `#36a39e` `#8fd8cf` ; laiton `#8a6a1f` `#d6a93a` | pourpre prune `#4e1334` `#7d1f4d` `#b0356b` `#d26a8e` ; or `#8a6a1f` `#d6a93a` `#f3d57a` | ambre `#8a4a12` `#e08a1e` `#ffd070` ; verre vert `#2d7a52` `#6fd09a` ; brassard pourpre (partagé avec Cyril) `#7d1f4d` `#b0356b` |
| Total (tronc commun compris) | 8+3+3+3+3+3+3+4 = 30 | 8+3+2+3+3+3+2 = 24 | 8+3+2+4+2+4+3 = 26 | 8+3+2+3+3+2+2 = 23 |

Sous le plafond de 32 pour les quatre ; il reste 2 couleurs libres chez Krunt3, 8 chez Taranis, 6 chez Cyril, 9 chez Pascal pour l'acier, le blanc des yeux ou une retouche. Si le métal verdit encore, passer à 40 couleurs (règle 6 de la bible : « 40 si un matériau en demande plus »).

### 9.7 Procédure de validation des sprites

1. Générer le profil (case 128 ou 64 selon l'abonnement), **vérifier la hauteur et la largeur** avec `outils/mesure_sprite.py` contre le tableau du §9.1 (hauteur cible ± 4 px).
2. Réduire à la palette du personnage dans PixelForge, retoucher l'acier si besoin.
3. Générer le 3/4 avec le même texte de personnage et la **même palette**.
4. **Test d'ombre chinoise** des quatre (§9.1) : refuser tout doublon de silhouette.
5. Krunt3 : dessiner la **variante B (porteur)** en calque de retouche avec les 4 couleurs de braise ; garder le fichier du calque séparé pour animer les braises.
6. Conserver pour chaque personnage le prompt exact qui a produit le résultat retenu (`prompts-personnages.md`, méthode §7).

---

## 10. Ce qui est inventé, et ce qui est à valider par krunt

### 10.1 Inventé

- Tous les **Éclats de départ** (30, 120, 90, 60) : aucune règle dans les livres.
- Le **contenu** du bagage de Taranis (carquois de 20, 7 jours de rations, Carnet des Routes avec zone blanche aux Ravins de Keth, boussole éteinte, lettre de contrat), la **Dette de Sang** envers le Cercle des Boussoles Éteintes (le nom du Cercle est canonique, la dette est inventée), l'idée qu'il a été transporté « en expédition ».
- Les **objets symboliques** et les **champs narratifs** du §3.7 (tension, objectifs, relations) : propositions à réécrire par chaque joueur.
- Le **profil « Étincelle tempéré »** (XP × 1,15, PS de départ 1), le **PS 2 de Pascal**, la **technique d'ouverture de meute** de chacun (reprise de `04` §7.3, inventée).
- **Réceptacle** (handicap unique) et la rédaction neutre ; la **Dette de Sang du pacte** (contenu à fixer).
- Les **Sentinelles du Pacte** (fiche de `03` §3.4, déjà marquée [INV]).
- Le **concept visuel** des quatre sprites (tenues, couleurs, accessoires), les **palettes hexadécimales**, les **dimensions cibles** (largeurs, hauteur de 58 px pour Pascal), les **signes de la variante porteur** et leurs paliers.

### 10.2 À valider par krunt (par ordre d'importance)

| # | Question | Ma recommandation |
|---|---|---|
| **V1** | Danse Rouge pour « Deux Lames » (Ours + Danse Rouge = tension créative du Livre VI) ? | oui (§6) |
| **V2** | Régions : Îles des Serments (Krunt3), Déserts Rouges (Taranis), Cœur Impérial (Cyril), Hautes Terres Claniques (Pascal) ; **Taranis aux Marches** serait-il préférable (il est chez lui) ? | Déserts Rouges |
| **V3** | Le bagage de Taranis : contenu, durée (épuisé vers J10), et la boussole qui réagit à l'entité (piste de trame) ? | oui, sauf la boussole si l'on ne veut pas lier Taranis à l'entité |
| **V4** | Pascal : Sentinelles du Pacte (ajout à StoryForge) ou Culte des Ancêtres Veilleurs ? | Sentinelles du Pacte |
| **V5** | Mana de départ : Livre VI (6 à 8) ou Livre I (2) ? | Livre VI (6, 6, 8, 6) |
| **V6** | Ingénieur Méthodique de Pascal sans synergie ; Canal Stable de Cyril avec la synergie du livre ; lecture de « Karma » comme Honneur | accepter |
| **V7** | Handicap unique « Réceptacle » (neutre : l'entité n'est pas forcément une malédiction) | accepter, à confirmer avec la version finale de l'entité (`05`) |
| **V8** | Contenu de la **Dette de Sang** de Krunt3 (créancier du pacte) ; le prix « oublier des noms » est retiré (décision de krunt) | contenu = la Braise et la Dette du Flux (`10` §4.3) ; dosage à confirmer |
| **V9** | Flanc Coordonné de Pascal : lecture souple (gardé) ou stricte (retiré au rang II) ? | gardé |
| **V10** | `05` §2.3 : réécrire le « Feu des Noms » comme rite de clan (Krunt3 n'a pas d'école de feu) | oui |
| **V11** | Sprite de Krunt3 : peau hâlée rougie (proposée) ou rouge franche ? Garde-t-on la barbe rousse tressée ? | hâlée rougie, barbe gardée |
| **V12** | Variante « porteur » : signes ambigus (veines chaudes, mèche cendre, braises discrètes) acceptés ? Palier B suffit ? | oui, palier B ; le palier C selon la trame |
| **V13** | Hauteurs de sprite : Pascal à 58 px au lieu de 64 ? | oui, pour la silhouette |

### 10.3 Incohérences rencontrées dans les livres

| # | Incohérence | Où | Ce que je retiens |
|---|---|---|---|
| 1 | Mana de départ : 2 (Livre I) ou 6 à 8 (Livre VI) | Livre I ch. 3 §7 ; Livre VI ch. 13 §6 | 6 à 8 |
| 2 | Bombes alchimiques : niveau 8 (Livre VII) ou rang 5 (Livre X ch. 6) | Livre VII ; Livre X | niveau 4 pour les bombes légères |
| 3 | Aucune règle de monnaie ni de budget de départ | Livre I ; Livre VIII ch. 9 | Éclats inventés, faibles |
| 4 | Honneur : 0 à 10 (Livre I) ou −25 à +25 (Livre VIII), « Karma » du Livre VIII sans équivalent au Livre I | Livre I ; Livre VIII | échelle du Livre I |
| 5 | Une seule technique d'École au rang I (Livre VI) ou deux (Livre I étape 5) | Livre I ; Livre VI | une |
| 6 | Pas de compétence « Orientation » ni « Cartographie » dans la liste du Livre I ; le Cartographe repose sur Connaissance (domaine) | Livre I ch. 3 §6 ; Livre VII | Connaissance (cartographie et géographie) |
| 7 | Frères de l'Épreuve, Culte des Ancêtres : ordres cités sans fiche dans Livre V ch. 5 | Livre V ; Atlas | à ajouter (`03` §12) |

---

## Compte rendu (5 lignes)

1. **Couvert** : quatre fiches v2 conformes aux règles de création (42 points, jauges, 17 compétences, PA, équipement « niveaux 1-5 »), en JSON (clés du VTT) et en tableaux, avec 20 corrections (liste du §8) par rapport à `04` ; bagage de Taranis défini dans les limites des Livres I, VIII et IX ; Danse Rouge justifiée ; ordre de Pascal tranché ; briefs et prompts PixelLab pour les quatre, avec palettes, tailles et test d'ombre chinoise, et la variante « porteur » de Krunt3 en calque de braises sans spoiler.
2. **Faible** : Éclats, bagage, objectifs et relations sont des inventions à valider ; le contenu de la Dette de Sang de Krunt3 dépend du dosage de la Braise (qui remplace l'ancien coût par l'oubli de noms) ; les palettes et dimensions de sprites n'ont pas été testées dans PixelLab ; le Mana de départ reste ambigu entre les livres.
3. **Recommandation 1** : valider d'abord V2 (régions, surtout Taranis) et V4 (Sentinelles du Pacte), car ils conditionnent les listes StoryForge et du VTT.
4. **Recommandation 2** : générer les sprites dans l'ordre Krunt3 (profil puis calque porteur), Pascal, Cyril, Taranis, et faire le test d'ombre chinoise **avant** l'animation ; le calque de braises est un fichier à part.
5. **Recommandation 3** : fixer le dosage de la Braise (qui a remplacé l'ancien coût par l'oubli de noms) avant de figer la Dette de Sang et le handicap Réceptacle de Krunt3 ; le « Feu des Noms » de `05` §2.3 est déjà réécrit en rite de clan (passe v3).
