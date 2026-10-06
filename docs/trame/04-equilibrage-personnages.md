# Équilibrage des quatre personnages (Krunt3, Taranis, Cyril, Pascal) et de deux recrues

> **Remplacé en partie par `10-trame-v3.md` (passe v3, 2026-10-06), `08-fiches-v2-et-sprites.md` (fiches v2) et `07-essais-equilibrage.md` (simulations).** Ne plus utiliser les fiches JSON du §9 (obsolètes) : Taranis n'est plus Espion (Chasseur-Pisteur + Cartographe), n'est pas né aux Marches (Déserts Rouges) et part avec un bagage de départ ; Pascal est au Sceau Pourpre, en cuir et bouclier (Défense 18), sans bombe de départ ; l'ordre de Krunt3 est celui des Frères de l'Épreuve ; aucune Résonance à la création ; Éclats 30 / 120 / 90 / 60. Les passages concernés sont corrigés ci-dessous (passe v3). Voir `09-revalidation.md`.


> **Réconciliation (2026-10-06, passe v3)** : ce document avait rattaché Krunt3 à l'**Ordre du Flux**. Or l'Ordre du Flux est **l'antagoniste validé** (il a détruit la famille de Krunt) : l'ordre de Krunt3 est les **Frères de l'Épreuve** (décision de krunt). Pour Pascal : clan **Sceau Pourpre** (décision de krunt) ; ordre : Sentinelles du Pacte (ordre à créer, `03` §3.4) ou, en repli, Culte des Ancêtres Veilleurs : **question ouverte** (`10` Q17).



Rédigé le 2026-10-06. Domaine : accorder les fiches aux livres (StoryForge fait foi), les équilibrer pour qu'elles portent la quête de `02-trame-v1.md`, leur donner des rôles et des courbes de progression différents, et traiter le cas des trois Loups.

**Légende.** `LIVRE` = ce que disent les livres (avec numéro). `PROP` = ma proposition. `INVENTÉ` = valeur d'équilibrage sans appui dans les livres, **à tester**. Rien n'est figé tant que krunt ne l'a pas validé. Aucun commit n'a été fait.

---

## 0. En bref

- Les fiches actuelles sont des **fiches de test** : quatre sur quatre dépassent ou ne respectent pas le budget de création (60 points au lieu de 42 pour trois d'entre elles, 27 pour Krunt3), les jauges ne suivent pas les formules (Vitalité 20 au lieu de 4+END), Pascal est « Maître » (3 étoiles) avec 5 000 Éclats et un « sabre laser ».
- **Trois des quatre Écoles du VTT n'existent pas dans le Livre VI** (Arc Précis, Deux Lames, Lame Droite). Je propose les plus proches : **Souffle Long** (Arc), **Danse Rouge** (Double Lame), **Flux Tranchant** (Épée Longue) pour Cyril et **Gardien Mobile** (Épée et Bouclier) pour Pascal, afin que les deux « Lame Droite » ne soient pas des doublons.
- Quatre rôles : **Krunt3 = fer de lance maudit** (première ligne offensive, porte le Pacte), **Taranis = vigie tireur** (éclaireur, guide des terres hostiles), **Cyril = voix du serment** (soin et diplomatie), **Pascal = rempart alchimiste** (seconde ligne, vivres, potions).
- Quatre profils de progression : **Pascal « Roc »** (fort au départ, lent), **Taranis « Étincelle »** (faible au départ, rapide), **Cyril « Graine »** (plafond haut, éclot tard), **Krunt3 « Pacte »** (courbe en dents de scie, plafond le plus haut, au prix de Marques).
- Les trois Loups se différencient par l'**École (modes de Mana différents : Rituel, Flux, Ancrage)**, le **métier**, le **rôle de meute** (voix, ancre, œil) et, au jalon seulement, une **Résonance** (aucune à la création).
- Simulation simple : les fiches équilibrées sont **plus fragiles que les fiches de test** (c'est voulu), le modèle de dégâts du Livre I ne donne **aucun rôle de tank** contre une créature d'élite (écart signalé), et les trois Loups cumulent trop de *Flanc Coordonné* (limite proposée).

---

## 1. Ce que disent les livres (règles de création et de progression)

### 1.1 Création (Livre I, ch. 3 §7, et ch. 2)

| Règle | Valeur du livre | Source |
|---|---|---|
| Étapes de création | 10 : phrase, origine (1d20), attributs, Vitalité/Endurance, École, Métier, Posture, Compétences, Honneur, phrase revisitée | LIVRE I ch. 3 §7 |
| Attributs | **42 points** sur 6 attributs (FOR, AGI, END, ESP, VOL, PRE) ; **min 3, max 12** par attribut ; puis bonus d'origine | LIVRE I ch. 3 §7 étape 3 |
| Origines à bonus d'attribut | Hautes Terres Claniques **+1 VOL** ; Îles des Serments **+1 END** (les autres régions donnent des avantages narratifs) | LIVRE II §4, LIVRE I ch. 2 §4 |
| Attributs secondaires | Défense = AGI+END ; Initiative = AGI+VOL ; Précision = AGI+ESP ; Résistance mentale = VOL+ESP ; Autorité sociale = PRE+Honneur | LIVRE I ch. 2 §2 |
| Vitalité max | **4 + END** (7 à 16 cases) | LIVRE I ch. 2 §4 |
| Endurance max | **10** à la création (modifiable par origine ou Posture) | LIVRE I ch. 3 §7 étape 4 |
| Mana de départ | **Trois valeurs** : Livre I « 2 × Rang » (2) ; **Livre VI, table de progression : Rang I = 6 à 8 Mana** ; Livre X : 8 | LIVRE I, VI ch. 13 §6, X ch. 13 |
| École | rang I (Aspirant) ; une Technique de rang I ; coût des Techniques 2 Mana (rang I à III), 3 (IV), 4-5 (V) | LIVRE VI ch. 2 |
| Métier | 1 étoile à la création ; 2 métiers au plus (le second ≤ le principal) ; 30 niveaux en jalons (Livre VII) | LIVRE I, VII |
| Posture | questionnaire en 5 questions ; **4 Techniques de Posture**, 2 Endurance chacune | LIVRE I, VI ch. 4 |
| Compétences | **12 points libres** + 2 (École) + 2 (Métier) + 1 (Posture) = **17**, **max 3** par compétence à la création, échelle 0 à 5 | LIVRE I ch. 3 §6 |
| Honneur de départ | **4 à 6** (Reconnu), ±1 selon l'origine ; jauge 0 à 10 | LIVRE I ch. 2 §8, ch. 3 étape 9 |
| Forge, Tension | collectives, 0 au départ | LIVRE I ch. 2 |
| Avantages et handicaps | **6 PA** ; 1 Handicap Majeur obligatoire gratuit ; Avantage mineur 1 PA, majeur 3 PA ; Handicap mineur +1 PA (2 au plus), majeur +3 PA ; **gain plafonné à +4 PA** ; **2 Majeurs et 3 mineurs au plus** ; avantage lié au métier principal : −1 PA | LIVRE VIII ch. 1 |
| Avantage ou handicap unique | liés à l'histoire, valident par le MJ, remplacent 1 Majeur (exemple « Marqué par un Phœnix ») | LIVRE VIII ch. 4 §3 |
| Incompatibilités | Espion/Infiltrateur : pas d'Autorité Naturelle ; Mage Blanc : pas d'Affinité Nécrotique ; Espion + Sentinelle d'Honneur = conflit identitaire ; Mage Noir + Mage Blanc = incompatibilité totale ; **Espion + Mage Noir = efficacité maximale** | LIVRE VII ch. 2, VIII ch. 1 §7 |

### 1.2 Écoles, Postures, Résonances (Livre VI)

- **14 Écoles Martiales, une par arme** : Coup Final (Grande Lame, Ancrage), Flux Tranchant (Épée Longue, Flux), Gardien Mobile (Épée et Bouclier, Ancrage), **Danse Rouge (Double Lame, Flux)**, Fracas Juste (Marteau), Résonances (Cor de Chasse, Rituel), Mur Vivant (Lance), Jugement Scellé (Arbalète-Lance, Sacrifice), Mutation (Hache-Épée), Équilibre Instable, Ascension, **Souffle Long (Arc, Rituel)**, Rafale, Ancrage (Arbalète Lourde). 8 Mystiques, 7 Techniques, 4 domaines interdits (accès jamais à la création).
- **Techniques de rang I** : Danse Rouge *Fuite Tranchante* (désengagement + frappe, 2 Mana) ; Souffle Long *Tir Ciblé* (état Exposé, 2 Mana) ; Flux Tranchant *Première Vague* (attaque légère, Avantage sur le prochain jet, 2 Mana) ; Gardien Mobile *Garde Haute* (−3 aux dégâts reçus, pas d'attaque, 2 Mana).
- **Quatre modes de Mana** : Flux (par l'action), Ancrage (par l'immobilité), Rituel (acte délibéré hors combat, rien en combat), Sacrifice (par un prix payé : +2 Mana par Vitalité perdue volontairement).
- **Loup** : Appel de Meute (allié agit hors tour), Flanc Coordonné (+d6 et ignore 1 armure si un allié a attaqué la même cible), Présence Rassurante (retire un état), Sacrifice de Meute (−3 Vitalité pour soi, Avantage à tous). Honneur : monte si le groupe réussit grâce à lui, **chute s'il abandonne un allié**.
- **Ours** : Interposition, Ancrage, Provocation, Mur de Chair (−2 dégâts aux alliés au contact). Honneur : monte par sacrifices publics, chute par retrait lâche.
- **Compatibilités Posture × École** (Livre VI ch. 13 §5) : Loup va avec Résonances, Gardien Mobile, Flux Tranchant ; Ours avec Mur Vivant, Fracas Juste, Fondations ; **Ours + Danse Rouge est listé comme « tension créative » (ancrage contre vitesse)**.
- **Résonance** : changer de Posture par jalon laisse une Technique de l'ancienne Posture, **gratuite, une fois par session**, si l'on dit en une phrase pourquoi. Elles s'accumulent. (À ne pas confondre avec l'**École** « Résonances », qui est celle du Cor de Chasse.)
- **Posture Légendaire** : Honneur 7 ou plus et jalon majeur ; elle s'ajoute à la Posture naturelle (Dragon Azur = soutien et soin).

### 1.3 Métiers (Livre VII), progression (Livres VII, IX, X)

- **Espion / Infiltrateur** (Social) : niveau 1 « Discrétion basique », 5 « Secret Fondamental » ; variantes : agent de cour, infiltrateur urbain, **éclaireur secret** (zones hostiles), **occulte** (cultes et ordres secrets), éthérique.
- **Mage Blanc** (Magie) : niveau 1 soins mineurs (DD 8), 4 régénération (Endurance restaurée), 6 soins de blessures graves, 8 soins de groupe, 12 purification des malédictions ; **Alchimiste** (Artisan) : niveau 1 potions mineures, 4 bombes légères, **bombes alchimiques à partir du rang 5** (Livre X ch. 6) ; recettes de soin : Herbe Stabilisante +2 Vitalité (rang 1, DD 10).
- **Niveaux de métier** : 30, par jalons narratifs ; paliers 5, 10, 15, 20, 25, 30. **XP cumulée** : niveau 5 = 1 100, 10 = 4 100, 15 = 12 000, 20 = 30 000 (Livre X ch. 13).
- **Points d'attribut gagnés** aux paliers : +2 (5), +2 (10), +3 (15), +3 (20), +4 (25), +4 (30), au plus +1, +1, +2, +2, +2, +3 par attribut (Livre X ch. 13 §1).
- **Rang d'École** par niveau : rang II au niveau 5-7, III vers 10, IV vers 15-17, V vers 20-22 (Livre X) ; « 3 à 5 sessions » pour le rang II (Livre VI).

### 1.4 Incohérences entre livres (à garder en tête)

| # | Sujet | Conflit | Ce que je retiens |
|---|---|---|---|
| 1 | Échelle des attributs | Création 3 à 12 (L.I ch. 3) ; « 1 à 20 » (L.I ch. 2) ; Livre X ch. 13 emploie **autres attributs** (Dextérité, Intelligence, Sagesse, Charisme) | Les six du Livre I ; échelle 3-12 à la création |
| 2 | Vitalité | 4+END (L.I) contre « Vita 12 au niveau 1 » et 10+2×FOR+END (L.X) | **4+END** |
| 3 | Mana de départ | 2 (L.I) / 6-8 (L.VI) / 8 (L.X) | **6 à 8** (formule §3.4) ; déjà retenu par `mecaniques/03` |
| 4 | Techniques d'École au rang I | « deux premières » (L.I) contre une par rang (L.VI) | **Une** (L.VI) |
| 5 | Honneur | 0 à 10, départ 4-6, pas de karma (L.I) contre −25 à +25, départ 0 à +3, Karma, Infamie (L.VIII) | **Livre I** (déjà retenu : « Honneur jamais en chiffres » côté joueur) ; Karma des Livres VIII lu comme Honneur + Marques |
| 6 | Métier | 3 étoiles (L.I) contre 30 niveaux (L.VII/X) | Étoiles = tranches de 10 niveaux (déjà dans `mecaniques/03`) ; départ = ★1, niveau 1 |
| 7 | Défense | AGI+END (L.I) ; « AGI + armure » (`mecaniques/01`) ; CA des armures (L.IX) | AGI+END **+ CA de l'armure** (PROP) |
| 8 | Endurance | 10 fixe (L.I) contre 10 + 2×END + niveau/5 (L.X) | **10** |

---

## 2. Diagnostic des fiches actuelles (base du VTT)

| Point | Krunt3 | Taranis | Cyril | Pascal |
|---|---|---|---|---|
| Attributs (`attr-*`) | 10 partout = **60 pts** (+18 sur le budget) | 10 partout = **60** | 10 partout = **60** | 10 partout = **60** |
| Attributs détaillés (`attr_*`) | FOR 5, AGI 5, END 3, ESP 3, VOL 5, PRE 6 = **27 pts** (15 non dépensés) | — | — | — |
| Vitalité (jauge) | 20 (formule : 4+END = 14 ou 7 selon la clé) | 15 | 20 | 11 |
| Endurance (jauge) | 20 (livre : 10) | 15 | 20 | 13 |
| Mana (jauge) | 20 (livre : 6 à 8) | 10 | 20 | 9 |
| Honneur | 4 (conforme) | 5 (conforme) | **7** (au-dessus de 4-6) | 5 |
| Tension (collective) | **1** (devrait être 0) | 0 | 0 | 0 |
| École | « Deux Lames » (**absente** du Livre VI) | « Arc Précis » (**absente**) | « Lame Droite » (**absente**) | « Lame Droite » (doublon de Cyril) |
| Métier | Espion/Infiltrateur | Espion/Infiltrateur (**doublon**) | Mage Blanc | Alchimiste **3 étoiles** (au lieu de 1) |
| Équipement | — | — | — | « sabre laser » 1d20, bottes « Boulet » en adamentium (état Légendaire), **5 000 Éclats** (le revenu cible est de 300 par saison) |
| Ordre | « Ordre du Jugement » (**inconnu**) | — | — | « Sentinelles du Pacte » (**inconnu**) |
| Région | « Plaines Franches » (**inconnue**) | « Steppes du Vent » (**inconnue**) | « Terres du Sceau » (**inconnue**) | « Cols Fortifiés » (**inconnue**) |

Lecture : les quatre fiches sont des essais d'outil, pas des personnages. Krunt3 est le seul avec un début de répartition, **mais elle dépense 27 points sur 42** et donne END 3 à un Ours (Vitalité 7). Rien de tout cela ne doit servir de base d'équilibrage. Deux comptes de test supplémentaires existent (cf. `01-personnages-et-point-de-depart.md`) : ils sont ignorés ici.

---

## 3. Correspondance des noms (StoryForge = les livres font foi)

### 3.1 Écoles (PROP)

| VTT | Livre VI (proposé) | Pourquoi | Mode de Mana | Arme (Livre IX) |
|---|---|---|---|---|
| Deux Lames (Krunt3) | **Danse Rouge** | seule école à double lame ; tabou « perdre le contrôle de soi » (écho de la malédiction) | Flux | Double Lame 1d6+1d6 |
| Arc Précis (Taranis) | **Souffle Long** | seule école de l'arc ; « voir avant d'être vu » | Rituel | Arc 1d8, 80 m, Désavantage au contact |
| Lame Droite (Cyril) | **Flux Tranchant** | épée longue, équilibrée, polyvalente ; compatible Loup | Flux | Épée Longue 1d8 |
| Lame Droite (Pascal) | **Gardien Mobile** | épée droite **et bouclier** ; compatible Loup ; tabou « abandonner un allié protégé » (colle à la Posture Loup) | Ancrage | Épée et Bouclier 1d6, protection +2 |

Raison du changement pour Pascal : garder « Lame Droite » pour les deux Sceau Pourpre donnerait deux fiches identiques en combat. **C'est la seule modification de choix de krunt que je propose** ; si krunt la refuse, voir §7.4.

Note de cohérence visuelle : le sprite de Krunt3 (`docs/prompts-personnages.md`) porte une **hache à deux mains** dans le dos. Danse Rouge demande deux lames courtes. Choix à faire : redessiner le sprite, ou prendre **Mutation** (Hache-Épée, Flux) à la place (mais Ours + Mutation n'est pas dans la table de compatibilité).

### 3.2 Régions, clans, guildes, ordres (PROP)

Le tableau d'affiliation du Livre V §5 est indicatif ; un clan hors de sa région est possible « avec rupture culturelle » (Livre V). Les régions du VTT ne sont **pas** conservées : l'Atlas fait foi (« Atlas, sans surnoms »). `region-elem` (Wu Xing, propre à l'application) n'est qu'une **affinité facultative, hors canon** (`10` Q19) ; il n'y a pas de lien région-élément dans les livres.

| | Krunt3 | Taranis | Cyril | Pascal |
|---|---|---|---|---|
| Région VTT | Plaines Franches | Steppes du Vent | Terres du Sceau | Cols Fortifiés |
| **Région du Livre II (proposée)** | **Îles des Serments** (6) : « l'épreuve acceptée », **+1 END**, Guilde Martiale présente ; les Martiales y sont favorisées (Livre VI) | **Déserts Rouges** (9) : steppe rocailleuse à vents, Guilde de Chasse présente [L Atlas, Livre V l.382] ; il connaît les Marches par son métier (Navigateurs Gris et Guilde de Chasse y dominent) mais n'y est pas né | **Cœur Impérial** (1) : Sceau Pourpre, Marchands Libres, « +1 Réputation avec autorités » | **Hautes Terres Claniques** (4) : Guilde Martiale, **+1 VOL** ; Sceau Pourpre = clan d'**adoption** par serment |
| Clan (choix de krunt) | Lames Franches | Navigateurs Gris | Sceau Pourpre | Sceau Pourpre |
| Guilde (choix de krunt) | Guilde Martiale | Guilde de Chasse | Marchands Libres | Guilde Martiale |
| Ordre VTT → **ordre du Livre V** | Ordre du Jugement (justice et loi) → **Frères de l'Épreuve** (décision de krunt ; « Ordre du Jugement » = surnom). L'Ordre du Flux est l'antagoniste, pas l'ordre de Krunt3. | — | — (aucun ; Ordre du Flux possible) | Sentinelles du Pacte (protection des frontières), ordre à créer ([INV], `03` §3.4) ; **repli** : Culte des Ancêtres Veilleurs (Hautes Terres) : non tranché (`10` Q17) |

À signaler : l'Ordre du Flux interdit universellement la Nécrotechnie (Livre VI ch. 11) : c'est l'antagoniste (`05`, `10` §3). Krunt3 n'en est **pas** membre : son lien avec le Flux passe par la loyauté ou la dette. Un point de correspondance StoryForge est à ajouter pour l'alias « Ordre du Jugement » → Frères de l'Épreuve.

---

## 4. Les quatre fiches équilibrées de départ

### 4.1 Budget des 42 points, attributs finaux, jauges (PROP)

| | FOR | AGI | END | ESP | VOL | PRE | Somme | Bonus d'origine | Attributs finaux |
|---|---|---|---|---|---|---|---|---|---|
| **Krunt3** | 9 | 8 | 8 | 4 | 7 | 6 | **42** | +1 END (Îles des Serments) | END **9** |
| **Taranis** | 5 | 11 | 6 | 9 | 6 | 5 | **42** | aucun | — |
| **Cyril** | 5 | 6 | 6 | 8 | 9 | 8 | **42** | aucun (+1 Réputation) | — |
| **Pascal** | 7 | 6 | 8 | 9 | 5 | 7 | **42** | +1 VOL (Hautes Terres) | VOL **6** |

Aucun attribut ne dépasse 12 ni ne descend sous 3 avant bonus ; Krunt3 a un ESP de 4 (faiblesse volontaire). *(Passe v3 : Taranis passe de AGI 12 / END 5 à AGI 11 / END 6, comme le prévoyait le §6.4 point 3 ; voir `08` §3.2.)*

| Dérivé | Krunt3 | Taranis | Cyril | Pascal |
|---|---|---|---|---|
| **Vitalité max (4+END)** | **13** | **10** | **10** | **12** |
| Endurance max | 10 | 10 | 10 | 10 |
| **Mana de départ** (formule §3.4) | **6** | **6** | **8** | **6** |
| Honneur de départ | 4 | 4 | 5 | 6 |
| Tension / Forge (collectives) | 0 / 0 | 0 / 0 | 0 / 0 | 0 / 0 |
| Défense (AGI+END) / avec armure | 17 / **19** (cuir +2) | 17 / **19** (cuir +2) | 12 / **13** (vêtements renforcés +1) | 14 / **18** (cuir +2, bouclier +2 ; la maille exige un forgeron de niveau 8-15 [L Livre VIII]) |
| Initiative (AGI+VOL) | 15 | 17 | 15 | 12 |
| Précision (AGI+ESP) | 12 | 20 | 14 | 15 |
| Résistance mentale (VOL+ESP) | 11 | 15 | 17 | 15 |
| Autorité sociale (PRE+Honneur) | 10 | 9 | 13 | 13 |

#### Formule de Mana de départ (PROP, tient dans la fourchette 6-8 du Livre VI)
`Mana = 6 + 1 si VOL (final) ≥ 8 + 1 si École Mystique ou métier de magie`, plafonné à 8. Cyril (VOL 9, Mage Blanc) : 8. Les trois autres : 6.

### 4.2 École, rang, Posture, Techniques, Métier, avantages (PROP)

| | Krunt3 | Taranis | Cyril | Pascal |
|---|---|---|---|---|
| **École, rang** | Danse Rouge, **I** | Souffle Long, **I** | Flux Tranchant, **I** | Gardien Mobile, **I** |
| **Technique d'École de départ** | *Fuite Tranchante* (2 Mana) | *Tir Ciblé* (2 Mana) | *Première Vague* (2 Mana) | *Garde Haute* (2 Mana) |
| **Posture** | **Ours** | Loup | Loup | Loup |
| **Techniques de Posture** (4, 2 End chacune) | Interposition, Ancrage, Provocation, Mur de Chair | Appel de Meute, Flanc Coordonné, Présence Rassurante, Sacrifice de Meute | idem | idem |
| **Résonance de départ** | aucune | **aucune** (une Résonance ne s'acquiert que par changement de Posture [L Livre VI l.575-596] ; ni Faucon pour Taranis, ni Ours pour Pascal : un Loup n'a pas de Résonance Ours) | aucune (Légendaire plus tard) | aucune |
| **Métier principal (★1)** | Espion / Infiltrateur (variante **occulte**) | **Chasseur-Pisteur** (variante désertique) | **Mage Blanc** | **Alchimiste** (variante martiale) |
| **Métier secondaire (★1)** | aucun (Mage Noir possible plus tard, voir §5.4) | **Cartographe** (variante explorateur) | aucun | aucun |
| **Honneur** | 4 | 4 | 5 | 6 |
| **Arme (Standard)** | Double Lame 1d6+1d6 | Arc 1d8 | Épée Longue 1d8 | Épée et Bouclier 1d6 |
| **Armure** | cuir (+2) | cuir (+2) | vêtements renforcés (+1) | cuir (+2) + bouclier (+2) |
| **Éclats de départ** [INV] | 30 | 120 | 90 | 60 *(valeurs de `08` §3.6 ; l'ancienne ligne 100 / 80 / 150 / 250 est abandonnée)* |

Le nombre de Techniques de départ est 4 (Posture) + 1 (École rang I) = 5 (aucune Résonance à la création).

### 4.3 Compétences : 17 points (12 + 2 + 2 + 1), max 3

| | Krunt3 | Taranis | Cyril | Pascal |
|---|---|---|---|---|
| Niveau 3 | Corps-à-corps, Esquive active | Tir et lancers, Discrétion, Perception, Traque | Médecine, Concentration, Persuasion | Artisanat, Connaissance (alchimie), Résistance |
| Niveau 2 | Discrétion, Résistance, Intimidation froide | Marche forcée | Corps-à-corps, Connaissance (droit et serments) | Corps-à-corps |
| Niveau 1 | Perception, Tromperie, Commandement, Athlétisme, Résistance mentale | Esquive active, Connaissance (créatures), Acrobaties | Représentation, Résistance mentale, Perception, Esquive active | Perception, Athlétisme, Commandement, Médecine, Résistance mentale, Esquive active |
| **Total** | 3+3+2+2+2+1+1+1+1+1 = **17** | 3+3+3+3+2+1+1+1 = **17** | 3+3+3+2+2+1+1+1+1 = **17** | 3+3+3+2+1+1+1+1+1+1 = **17** |

Bonus de jet (attribut + compétence), pour le tableau de contrôle du §6.3.

### 4.4 Avantages et handicaps (Livre VIII)

| | Avantages (PA) | Handicaps |
|---|---|---|
| **Krunt3** (9 PA) | Maîtrise de Combat (Danse Rouge, 3) ; Vision Éthérique (3) ; Réflexes Affûtés (1) ; Récupération Accélérée (1) ; Posture Défensive (1) | **Handicap unique « Réceptacle »** (remplace le Majeur obligatoire gratuit : instabilité du Pacte, voir §5.4) ; **Dette de Sang** (+3 PA : le Pacte à payer) |
| **Taranis** (6 PA) | **Préparateur Obsessionnel** (3 ; exprime le bagage de départ, `08` §4) ; Réflexes Affûtés (1) ; Réseau Local, Marches (1) ; Improvisation Pratique (1). *(L'avantage unique « Ancien Faucon » est abandonné : invention sans appui dans le Livre VIII.)* | Dette de Sang envers le Cercle des Boussoles Éteintes (Majeur obligatoire) |
| **Cyril** (6 PA) | Nom Respecté (3, Honneur ≥ 5 : respecté) ; Canal Stable (3 − 1 synergie = 2) ; Résistance Partielle (1) | **Serment Absolu** (Majeur obligatoire) : ne jamais rompre un serment prêté, même à un ennemi du clan ; piège pour la voie « abandonner Krunt » |
| **Pascal** (7 PA) | Corps Endurci (3) ; Ingénieur Méthodique (3 − 1 = 2) ; Économie de Matériaux (1) ; Posture Défensive (1) | **Blessure Ancienne** (Majeur obligatoire, −2 à courir : clin d'œil aux bottes « Boulet » de la fiche test) ; Code Personnel Rigide (+1) |

Remarques de conformité : Espion + Autorité Naturelle est interdit (non pris) ; Mage Blanc + Affinité Nécrotique est interdit (non pris) ; Canal Stable demande « Karma ≥ +3 » : je le lis comme Honneur ≥ 5 (voir incohérence 5). Krunt3 a **9 PA** (6 + 3 de la Dette de Sang) : c'est autorisé (gain ≤ 4) mais il est le plus doté, voir écart §6.4.

### 4.5 Rôles narratif et de jeu

| | Rôle de jeu | Rôle dans la trame | Faiblesse volontaire | Ce qui lui est confié |
|---|---|---|---|---|
| **Krunt3** | **Fer de lance** : dégâts les plus élevés (deux dés), Vitalité 13 ; **Provocation ponctuelle seulement** : pas un tank (`07` §5 : avec Double Lame et cuir, la première ligne est impossible) | **Le héros** et le réceptacle ; les autres gravitent autour de lui | ESP 4 (Perception 5), Mana 6, Corruption, Pacte | Choisir à chaque Marque de Pacte entre puissance et les autres |
| **Taranis** | **Vigie tireur** : portée 80 m, Traque, Initiative 17, Tir Ciblé (Exposé) | **Guide des terres hostiles** : il est chez lui **côté clan et guilde** aux Marches mais étranger côté naissance (Déserts Rouges) ; il est celui qui peut rentrer le plus facilement, donc celui pour qui « abandonner » coûte le moins cher à court terme | Vitalité 10, Mana 6 (Rituel : pas de récupération en combat), Désavantage au contact | Les pistes, les routes, la survie ; sa dette envers le Cercle des Boussoles Éteintes |
| **Cyril** | **Soin et voix** : Mage Blanc, Présence Rassurante, Résistance mentale 17, Autorité 13 | **Le porte-parole et l'arbitre** : fait le lien juridique (clan Sceau Pourpre, ennemi des Lames Franches) | Défense 13, Vitalité 10, AGI 6 | Les serments, la négociation, stabiliser Krunt |
| **Pascal** | **Rempart alchimiste** : Défense 18, Vitalité 12, Garde Haute, Herbe Stabilisante (+2 Vitalité) | **L'intendance de la survie** : vivres, antidotes, potions, forge ; ancre morale (Loup et Gardien) | Dégâts les plus faibles, Initiative 12, jambe blessée (−2 à courir) | La survie de base : eau, soins, abri ; bombes légères à partir du **niveau 4** du métier [L Livre VII l.709], **aucune bombe de départ** (décision de krunt : attaque de base seule) |

Couverture des besoins de l'équipe : **combat de contact** (Krunt3, Pascal), **distance** (Taranis), **soin** (Cyril, Pascal), **fabrication** (Pascal), **discrétion** (Krunt3, Taranis), **social** (Cyril, Krunt3 faible), **survie** (Taranis, Pascal). Manques : **première ligne mystique** et **diplomate de métier** (voir §8).

---

## 5. Profils de progression (PROP, tous les chiffres sont INVENTÉS à tester)

### 5.1 Principe
Le départ est identique pour tous (42 points, rang I, ★1). Ce qui change est le **rythme** et le **plafond**. Quatre profils, trois leviers chiffrés :

| Levier | Où il agit | Base (doc `mecaniques/03`) |
|---|---|---|
| **Jalons d'École** (rang II, III, IV, V, exprimés en % d'avancement de l'histoire) | rang d'École | II fin Acte I (~20 %), III ~35 %, IV ~70 %, V ~95 % |
| **XP de métier** (multiplicateur sur l'XP gagnée) | niveau du métier principal, donc paliers d'attributs | table du Livre X |
| **Points de Savoir (PS)** : départ et multiplicateur de gain | branches latérales de l'arbre | +1 par niveau du métier principal, +0,5 du secondaire, +2 par jalon, soit ~67 PS sur la campagne |
| **Plafond d'attribut** | niveau maximal de chaque attribut par paliers | 18 points au total aux paliers 5 à 30 (Livre X) |
| **Honneur de départ** | accès aux Postures Légendaires (Honneur ≥ 7) | 4 à 6 |

### 5.2 Les quatre profils

| | **Roc** (Pascal) | **Étincelle** (Taranis) | **Graine** (Cyril) | **Pacte** (Krunt3) |
|---|---|---|---|---|
| Idée | fort au départ, lent | faible au départ, évolue vite | départ moyen, **plafond haut**, éclot tard | départ solide, courbe en dents de scie, **plafond le plus haut** au prix de Marques |
| Jalons d'École (II / III / IV / V) | 25 % / 50 % / 80 % / après-jeu | 10 % / 25 % / 55 % / 85 % | 20 % / 40 % / 70 % / 95 % | 15 % / 35 % / 65 % / 90 % (le Pacte peut avancer un rang, §5.4) |
| Multiplicateur d'XP de métier | × 0,8 | **× 1,15** (tempéré, `08` §8 ; était × 1,25) | × 1,0 jusqu'au niveau 10, **× 1,5** ensuite | × 1,0 |
| PS au départ | **2** (`08` §8 ; était 4) | 1 (`08` §8 ; était 0) | 1 | 2 |
| Multiplicateur de gain de PS | × 0,8 | × 1,5 jusqu'au rang III, puis × 0,8 | × 0,8 jusqu'au rang III, puis × 1,3 | × 1,0, plus **Marques** (monnaie à part) |
| Total de PS en campagne (≈) | 2 + 54 = **56** | 1 + 72 = **73** | 1 + 74 = **75** | 2 + 67 = **69** (+ Marques) |
| Plafond d'attribut (par paliers) | **14** | **16** | **20** sur ESP, VOL, PRE ; 16 sur les autres | **18** sur FOR, AGI, END ; au-delà de 16, il faut avoir 3 Marques |
| Honneur de départ | 6 | 4 | 5 | 4 |
| Posture Légendaire visée | Tortue Noire (protection) | Faucon étendu (Oiseau Vermillon ?) | **Dragon Azur** (soin) à Honneur ≥ 7 | aucune (l'entité est la « Posture » en négatif) |
| Équipement de départ [INV] | aucune pièce Supérieure (réservée aux niveaux 11-15 [L Livre VIII ch. 9 §5]), 60 Éclats | 120 Éclats + bagage | 90 Éclats | 30 Éclats (il a tout perdu) |

Choix de forme : la courbe d'Étincelle est **rapide puis lente**, celle de Graine **lente puis rapide**, pour que les quatre se croisent plutôt que de se dépasser sans cesse.

### 5.3 Points de contrôle (hypothèse : 12 000 XP de métier sur la campagne, soit niveau 15 en fin pour un profil neutre)

| Avancement de l'histoire | Roc | Étincelle | Graine | Pacte |
|---|---|---|---|---|
| **10 %** : rang d'École / niveau de métier / points d'attribut gagnés | I / 4 / 0 | **II** / 6 / 2 | I / 5 / 2 | I / 5 / 2 |
| **25 %** | II / 7 / 2 | **III** / 9 / 2 | II / 8 / 2 | II / 8 / 2 |
| **50 %** | III / 10 / 4 | III / 12 / 4 | III / 12 / 4 | III / 11 / 4 |
| **75 %** | III / 12 / 4 | **IV** / 14 / 4 | IV / 14 / 4 | IV / 13 / 4 |
| **100 %** | IV / 13 / 4 | **IV** / 16 / 7 (V : voir note) | IV / 16 / 7 (V : voir note) | IV / 15 / 7 (V : voir note) |

**Note (passe v3, rang V)** : le Livre X place le rang V d'École au **niveau 20** (l.1512) ; avec 12 000 XP de campagne (niveau 15 à 16) personne ne l'atteint à 100 %. L'ancien tableau (rang V à 100 % pour trois profils) est **ramené au rang IV** ; les jalons « V » des profils (§5.2 : 85 %, 90 %, 95 %) sont **hors campagne** tant que krunt n'a pas tranché (`10` Q26 : abaisser le seuil ou allonger la campagne).

Lecture : à 10 % Étincelle est la plus avancée, à 25 % il a déjà le rang III ; Roc, le plus solide au départ (Vitalité 12, Défense 18, kit, 2 PS), est rattrapé vers 25 % et dépassé ensuite. Graine commence comme Roc et rejoint Étincelle vers 50 %, avec un plafond bien supérieur. Les écarts de niveau restent de 3 à 4 niveaux de métier au plus, ce qui ne casse pas les contrats communs (« rang I à II » jusqu'à 25 %).

### 5.4 Le Pacte de Krunt3 (INVENTÉ, à raccorder à `05-antagoniste-et-technique.md`)
- **Marques de Pacte** : compteur de 0 à 5, visible du MJ seulement (« jamais en chiffres » côté joueur).
- **Souffle du Réceptacle** : une fois par combat, action gratuite : Endurance pleine, +d6 de dégâts pendant **12 secondes** (temps réel) ; coût : **+3 braises** (`06` §2.4) et Tension +1 (collective). Les **Marques de Pacte** montent à chaque **Embrasement**, pas à chaque usage.
- **Marque 2** : le rang d'École peut avancer d'un cran hors jalon (la malédiction paie) ; **Marque 3** : plafond d'attribut de 16 levé jusqu'à 18 ; **Marque 5 = Embrasement général** (événement de trame, voir `10` §4.3 ; le mot « Saturation » est réservé au seuil de Corruption 19-24 du Livre II).
- Les Marques redescendent par des actes d'**aide aux autres** (karma positif du brief) : c'est ce qui rend utile la voie « aider Krunt ».
- Appuis dans les livres : mode de Mana **Sacrifice** (+2 Mana par Vitalité perdue), Techniques Secrètes Liées au Phénix (*Absorption de Corruption*, Livre VI ch. 12), handicap unique « Marqué par un Phœnix » (Livre VIII). Piste de métier secondaire **Mage Noir** (Espion + Mage Noir = « efficacité maximale », Livre VII) comme tentation, jamais à la création.

---

## 6. Vérification de l'équilibre (simulation simple, honnête sur ses limites)

Script : `scratchpad/sim/sim.py` (non versionné). Hypothèses : modèle du Livre I (d20 + attribut + compétence + rang contre Défense ; l'Endurance absorbe d'abord les coups puis la Vitalité) ; un Acte par round ; touche plafonnée à 95 %. **Le chef de meute de la démo** reprend les chiffres de `mecaniques/01` (Vitalité 27, Défense 11, morsure 2d6+7). **Le monstre d'élite (Vitalité 60, Défense 17, +10 au toucher, 2d8+9) est INVENTÉ** pour tester des combats plus longs. 20 000 à 30 000 tirages.

### 6.1 Chiffres par fiche

| | Krunt3 | Taranis | Cyril | Pascal |
|---|---|---|---|---|
| Vitalité (cases) / en points de coup (×4) | 13 / 52 | 10 / 40 | 10 / 40 | 12 / 48 |
| Défense avec armure | 19 | 19 | 13 | 18 |
| Dé de l'arme, dégâts moyens | 2 × 3,5 = **7,0** | 4,5 | 4,5 | 3,5 |
| Dégâts moyens par Acte, contre Défense 11 | **6,65** | 4,3 | 4,3 | 3,3 |
| Dégâts par Acte, modèle C de `mecaniques/01` (dé + floor(attr/4)) | 11 (2 × 5,5) | **7,5** | 5,5 | 4,5 |
| Coups du chef (9 points de coup, armure déduite) avant « Hors Combat » | **6,4** | 4,4 | 4,7 | **7,1** |

### 6.2 Combats simulés (4 fiches ensemble)

| Scénario | Rounds moyens | Victoire | Au moins un à 0 Vitalité |
|---|---|---|---|
| Chef de meute (27 / Déf. 11), Flanc Coordonné cumulé | 1,4 | 100 % | 0 % |
| Chef de meute, Flanc Coordonné **limité à 1 par round** | 1,8 | 100 % | 0 % |
| **Élite inventée** (60 / Déf. 17), Flanc cumulé | 3,4 | 97 % | 42 % |
| Élite inventée, Flanc **limité** | 4,1 | 95 % | **58 %** |
| Élite inventée, sans Provocation de Krunt3 | 4,0 | 97 % | 60 % |
| **Contre-épreuve : quatre fiches de test (10 partout, épée 1d8, Vitalité 14)** contre la même élite | 3,8 | 100 % | **38 %** |

Part des dégâts totaux (élite, Flanc limité) : Krunt3 24 %, **Taranis 38 %**, Cyril 20 %, Pascal 17 %. Sur le chef, avec Flanc limité : 30 / 34 / 20 / 15 %.

### 6.3 Tests de compétence (attribut + compétence, avant le d20)

| Test | Krunt3 | Taranis | Cyril | Pascal |
|---|---|---|---|---|
| Attaque (attr. + comp. + rang I + avantages) | 13 | 15 | 9 | 10 |
| Discrétion (AGI + comp.) | 10 | **15** | 6 | 6 |
| Perception / Traque (ESP + comp.) | 5 | **12** | 9 | 10 |
| Soin, Médecine (ESP + comp.) | 4 | 9 | **11** | 10 |
| Artisanat, alchimie (ESP + comp.) | 4 | 9 | 8 | **12** |
| Persuasion (PRE + comp.) | 7 (Tromperie) | 5 | **11** | 7 |
| Résistance physique (END + comp.) | **11** | 5 | 6 | 11 |
| Résistance mentale (VOL + comp.) | 8 | 6 | **10** | 7 |

Chaque rôle est **le meilleur du groupe dans son domaine** ; personne n'est nul partout. Les DD standards du Livre I (10 facile, 15 standard) sont tenables en spécialité (avec d20 + 10 à 15) et risqués hors spécialité (d20 + 4 à 7).

### 6.4 Écarts signalés (ce qui ne va pas encore)

1. **Le modèle de dégâts du Livre I ne donne pas de rôle de tank** (confirmé par `07` §5 et par le rejeu de `07` §12 : même en modèle C, Krunt3 avec Double Lame et cuir est à terre dans plus de 95 % des combats s'il fait la Provocation + Mur de Chair + Interposition ; il reste fer de lance). Contre l'élite inventée, la Provocation de Krunt3 ne change presque rien (58 % contre 60 % de risque qu'un personnage tombe) car une morsure de 18 dépasse Endurance + Vitalité (23). Cela confirme l'avis de `mecaniques/01` (modèle C, deux barres séparées) : le rôle de première ligne n'existe que dans ce modèle. **À trancher avant d'équilibrer Krunt3 en tank.**
2. **Le chef de meute est trivial pour quatre fiches équilibrées** (1,4 à 1,8 round, 0 % de personnage à terre). Ce n'est pas un défaut des fiches mais de l'échelle des monstres (coefficient K de `mecaniques/01`). À régler côté monstres, pas ici.
3. **Taranis faisait le plus de dégâts** (34 à 38 % avec la fiche d'origine ; **29 à 30 %** avec la fiche v2 AGI 11 / END 6 et le bagage de `08` : rejeu en `07` §12) alors qu'il est « faible au départ ». Compensations existantes : Vitalité 10 (v2), Mana 6 en mode Rituel (3 Tirs Ciblés par combat, aucune récupération en combat), Désavantage au contact. **Fait en v2** : un point d'AGI a été déplacé vers END (12 vers 11).
4. **Pascal fait peu de dégâts** (15 à 17 %) : par construction (rôle de rempart), compensé par Défense 18, Garde Haute, Herbe Stabilisante (+2 Vitalité, DD 10). **Ses bombes légères n'arrivent qu'au niveau 4 du métier** [L Livre VII] : l'Acte I est son point faible. La piste « *Bombe de Feu* de départ » est **abandonnée** : krunt demande l'attaque de base seule avant les bombes.
5. **Cyril est le plus fragile en mêlée** (Défense 13, Vitalité 10). Voulu (soin), mais il doit rester en arrière : *Présence Rassurante* exige d'être **au contact** de l'allié (Livre VI) : tension à jouer.
6. **Krunt3 est le mieux doté** : 9 PA, dégâts maximaux, Vitalité 13. C'est le prix de deux handicaps lourds (Réceptacle, Dette de Sang) et du Pacte. Si le test le trouve trop fort, retirer *Vision Éthérique* ou *Posture Défensive*.
7. **Flanc Coordonné cumulé par trois Loups est trop fort** (chef abattu en 1,4 round contre 1,8 avec la limite). Limite proposée au §7.3.
8. **Mana très limité** (6 pour trois fiches) : un seul combat peut vider la jauge. À valider au prototype.

---

## 7. Les trois Loups

### 7.1 Ce que dit le livre
La Posture Loup donne **les mêmes quatre Techniques à tous** : le Loup est défini par la cohésion (« un combat est gagné quand tout le monde revient »). La différenciation ne vient donc **pas** de la Posture, mais des trois autres couches (École, Métier, Résonance) et des attributs. Chute d'Honneur : « s'il abandonne un allié ou refuse une coordination possible ».

### 7.2 Comment les différencier (PROP)

| | **Taranis, l'œil** | **Cyril, la voix** | **Pascal, l'ancre** |
|---|---|---|---|
| École, mode de Mana | Souffle Long, **Rituel** | Flux Tranchant, **Flux** | Gardien Mobile, **Ancrage** |
| Métier | Chasseur-Pisteur + Cartographe | Mage Blanc | Alchimiste |
| Technique de Loup d'ouverture | *Flanc Coordonné* (tir de flanc à distance) | *Présence Rassurante* + *Appel de Meute* | *Sacrifice de Meute* + *Garde Haute* |
| Rôle dans la meute | repère, tire, ouvre l'Exposé | soigne, retire les états, coordonne | encaisse, tient la ligne, ravitaille |
| Résonance | aucune (retirée : une Résonance ne s'acquiert que par changement de Posture [L Livre VI]) | aucune (Dragon Azur plus tard) | aucune (pas d'Ours pour un Loup) |
| Attribut dominant | AGI 11 | VOL 9, PRE 8 | END 8, ESP 9 |
| Honneur / début de courbe | 4, Étincelle | 5, Graine | 6, Roc |
| Clan | Navigateurs Gris (routes, frontières) | Sceau Pourpre (serments, loi) | Sceau Pourpre par adoption (Hautes Terres) |

Trois modes de Mana différents (Rituel, Flux, Ancrage) font que chaque Loup **joue sa jauge autrement** : Taranis planifie (aucun Mana en combat), Cyril entretient son flux en frappant, Pascal récupère en tenant sa position. Danse Rouge de Krunt3 est aussi en Flux, mais le Pacte lui ajoute un mode **Sacrifice**.

### 7.3 Règles de meute proposées (INVENTÉES, à tester)
- **Spécialité de meute** : le **premier** usage par combat de sa Technique de Loup « d'ouverture » coûte **1 Endurance** au lieu de 2 (Taranis : *Flanc Coordonné* ; Cyril : *Présence Rassurante* ; Pascal : *Sacrifice de Meute*).
- ***Flanc Coordonné* ne se cumule pas** : au plus un bonus de +d6 par cible et par round (simulation : chef abattu en 1,8 round au lieu de 1,4).
- ***Appel de Meute* ne se chaîne pas** : un allié déjà appelé ce round ne peut pas appeler un autre.
- **Meute complète** : si les trois Loups sont à portée de voix au début d'un combat, une fois par combat, un Loup peut déclarer un **ordre de meute** (un allié gagne Avantage sur un jet) sans coût. Ce bonus rappelle le thème « tous vivants ».

### 7.4 Ce que cela donne en jeu et dans la trame
- **Face à Krunt3 (Ours, solitaire)** : le Loup se bat pour que *tous* reviennent ; l'Ours tient la ligne seul. Les trois Loups **perdent de l'Honneur s'ils abandonnent un allié**, donc la voie « abandonner Krunt3 » est coûteuse pour eux par leur propre Posture, pas seulement par leur clan.
- **Les trois n'ont pas la même tentation** : Taranis peut rentrer le plus facilement (il connaît les Marches par son métier et son clan y domine), Cyril est bloqué par son *Serment Absolu* (s'il a juré à Krunt3, il ne partira pas), Pascal a sa Blessure Ancienne et une loyauté de Sentinelle. C'est un **conflit de meute écrit dans les fiches**.
- **Cyril et Pascal sont tous deux Sceau Pourpre** (clan ennemi des Lames Franches de Krunt3) : leur rôle de **trait d'union** entre clans rivaux est naturel, avec deux colorations : le juriste (Cyril) et le soldat adopté (Pascal).
- **Si krunt refuse que Pascal soit Gardien Mobile** (garder « Lame Droite » = Flux Tranchant pour les deux) : différencier par le **Métier et les attributs** (Pascal Alchimiste en seconde ligne, END et ESP ; Cyril Mage Blanc en Mana 8) et donner à Pascal un **bouclier en équipement** seulement. La différence d'École disparaît (deux modes Flux), la meute perd un mode de Mana.

---

## 8. Deux recrues pour combler les manques (joueur ou PNJ, PROP)

Manques de l'équipe : une **première ligne mystique** (aucune École Mystique chez les quatre) et un **diplomate de métier** (Cyril est un juriste soignant, pas un diplomate). Autres Postures absentes : Faucon et Félin.

### 8.1 Recrue A : la Gardienne des Pierres (première ligne mystique)
- **Concept** : survivante des Terres Ravagées, mur vivant qui inscrit des runes d'ancrage dans le sol ; elle résiste à la Corruption que Krunt3 attire, mais souffre dans les zones à fort Mana (**Sensibilité Éthérique Douloureuse**, Livre VIII) : drame obligé près de lui.
- **École** : **Fondations** (Terre, **Ancrage**, École Mystique : *Solidification* au rang I, *Renforcement* +3 d'armure à un allié au rang II). Compatible Ours (Livre VI).
- **Posture** : **Ours** (deuxième Ours, assumé : Krunt3 est l'Ours offensif et maudit, elle l'Ours défensif et stable). Variante pour diversifier : Faucon.
- **Métier** : Runiste / Glyphiste ★1. **Clan** : Cendres Liées (résistance à la Corruption, refuges clandestins). **Guilde** : Guilde des Soigneurs. **Ordre** : Porte-Cendres. **Région** : Terres Ravagées.
- **Attributs** : FOR 8, AGI 4, END 10, ESP 6, VOL 9, PRE 5 (= 42). Vitalité **14**, Endurance 10, Mana **8** (VOL ≥ 8 et École Mystique), Honneur 4. Défense 14 (17 en maille).
- **Profil de progression** : Roc (fort, lent).

### 8.2 Recrue B : la Langue du Pacte (diplomate)
- **Concept** : négociatrice des Mille Voix, spécialiste des ententes avec ce qui n'est pas humain. Son **École Liens Spirituels** (*Perception des Esprits*, rang I ; *Pacte Mineur*, rang II) lui permet de **percevoir et de parler à l'entité** logée en Krunt3 : c'est l'outil narratif manquant pour comprendre le Pacte.
- **École** : Liens Spirituels (Âme, Rituel). **Posture** : **Faucon** (lecture et information : Lecture du Terrain, Point Faible, Anticipation, Prédiction). Les Mille Voix sont ennemis de l'Ordre Dogmatique (Livre V), un conflit prêt à l'emploi.
- **Métier** : Diplomate ★1 (principal) + **Gardien des Accords ★1** (synergie du Livre VII « pactes solides », tension : « conflits d'intérêt »). **Clan** : Mille Voix. **Guilde** : Marchands Libres. **Ordre** : Cultes Syncrétiques. **Région** : Cités Libres Marchandes.
- **Attributs** : FOR 3, AGI 6, END 5, ESP 9, VOL 9, PRE 10 (= 42). Vitalité **9**, Endurance 10, Mana **8**, Honneur 5. Défense 11. **Pas d'arme** (non-combattante : sa force est à la table de négociation).
- **Profil de progression** : Étincelle (faible au départ, rapide).

Ces deux recrues ne prennent **pas** de Posture Loup et complètent les trois modes de Mana (Ancrage, Rituel). Elles sont à marquer « recrue » (le brief : « au pire on recrutera un joueur ou un PNJ »).

---

## 9. Fiches JSON prêtes à importer (CharForge, clés du VTT)

> **OBSOLÈTE (passe v3, 2026-10-06) : ne pas importer ces fiches.** Elles sont remplacées par `08-fiches-v2-et-sprites.md` §7. Les valeurs les plus dangereuses sont corrigées sur place ci-dessous (Taranis : métier, région, attributs, Résonance, avantage, Éclats ; Pascal : ordre, armure, Éclats, Résonance prévue ; Éclats de Krunt3 et de Cyril) ; le reste (compétences, profils) est à relire dans `08`.

**Mode d'emploi.**
- Le bloc principal ne contient que des **clés observées dans la base** (`attr-for`…, `gauge-*`, `clan-*`, `guilde-*`, `ordre-*`, `ecole`, `posture`, `m1-nom`, `m1-stars-val`, `region`, `region-elem`, `tech-ecole`, `tech-posture`, `arme-*`, `arm-pieds-*`, `eclats`). Les jauges portent la valeur de départ (courante = maximale) ; je n'ai pas vu de clé de maximum.
- L'objet **`_extras`** contient des clés **proposées** (non observées dans la base : métier secondaire, compétences, avantages, technique de rang I, Résonance, Marques, profil…) : à renommer selon l'export réel de CharForge ou à supprimer s'il refuse les clés inconnues. Les clés `attr_*` (avec tiret bas) existent en double dans la base de Krunt3 : à synchroniser si besoin.
- `ecole` est le **nom du Livre VI** ; l'ancien nom du VTT est conservé dans `_extras.ecole-vtt`. Les champs `joueur` ne sont pas repris (données personnelles). Pour Pascal, les clés d'équipement de test (`arme-*`, `arm-pieds-*`, `eclats`) sont remplacées ; les cases `tl-*`, `snap*`, `tbl-*`, `weight-*` ne sont pas touchées.

### 9.1 Krunt3

```json
{
  "nom": "Krunt3",
  "attr-for": 9, "attr-agi": 8, "attr-end": 9, "attr-esp": 4, "attr-vol": 7, "attr-pre": 6,
  "gauge-vit": 13, "gauge-end": 10, "gauge-mana": 6, "gauge-hon": 4, "gauge-ten": 0, "gauge-forge": 0,
  "clan-nom": "Lames Franches",
  "clan-devise": "Nul ne nous commande. Nul ne nous possède.",
  "guilde-nom": "Guilde Martiale",
  "guilde-spec": "Administration de la guerre",
  "ordre-nom": "Frères de l'Épreuve",
  "ordre-philo": "Dettes et correction (Arbitres du Flux)",
  "ecole": "Danse Rouge",
  "tech-ecole": "Danse Rouge",
  "posture": "Ours",
  "tech-posture": "Ours",
  "m1-nom": "Espion / Infiltrateur",
  "m1-stars-val": 1,
  "region": "Îles des Serments",
  "region-elem": "—",
  "arme-nom": "Double Lame",
  "arme-degats": "1d6+1d6",
  "eclats": 30,
  "_extras": {
    "ecole-vtt": "Deux Lames",
    "ecole-rang": 1,
    "tech-ecole-r1": "Fuite Tranchante",
    "tech-posture-liste": ["Interposition", "Ancrage", "Provocation", "Mur de Chair"],
    "mana-mode": "Flux",
    "m1-variante": "Occulte",
    "m2-nom": "",
    "competences": {"corps_a_corps": 3, "esquive_active": 3, "discretion": 2, "resistance": 2, "intimidation_froide": 2, "perception": 1, "tromperie": 1, "commandement": 1, "athletisme": 1, "resistance_mentale": 1},
    "avantages": ["Maîtrise de Combat (Danse Rouge)", "Vision Éthérique", "Réflexes Affûtés", "Récupération Accélérée", "Posture Défensive"],
    "handicaps": ["Réceptacle (unique, remplace le Majeur obligatoire)", "Dette de Sang (le Pacte)"],
    "pa-total": 9,
    "armure": "Armure légère (cuir) +2",
    "pacte-marques": 0,
    "profil-progression": "Pacte",
    "jalons-ecole-pct": [15, 35, 65, 90],
    "xp-metier-mult": 1.0, "ps-depart": 2, "plafond-attribut": 18,
    "role": "Fer de lance maudit"
  }
}
```

### 9.2 Taranis

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
  "ecole": "Souffle Long",
  "tech-ecole": "Souffle Long",
  "posture": "Loup",
  "tech-posture": "Loup",
  "m1-nom": "Chasseur-Pisteur",
  "m1-stars-val": 1,
  "region": "Déserts Rouges",
  "region-elem": "Vent",
  "arme-nom": "Arc",
  "arme-degats": "1d8",
  "eclats": 120,
  "_extras": {
    "ecole-vtt": "Arc Précis",
    "ecole-rang": 1,
    "tech-ecole-r1": "Tir Ciblé",
    "tech-posture-liste": ["Appel de Meute", "Flanc Coordonné", "Présence Rassurante", "Sacrifice de Meute"],
    "specialite-meute": "Flanc Coordonné",
    "resonance": [],
    "mana-mode": "Rituel",
    "m1-variante": "Désertique",
    "m2-nom": "Cartographe", "m2-stars-val": 1,
    "competences": {"tir_et_lancers": 3, "discretion": 3, "perception": 3, "traque": 3, "marche_forcee": 2, "esquive_active": 1, "connaissance_creatures": 1, "acrobaties": 1},
    "avantages": ["Préparateur Obsessionnel", "Réflexes Affûtés", "Réseau Local (Marches)", "Improvisation Pratique"],
    "handicaps": ["Dette de Sang (Cercle des Boussoles Éteintes)"],
    "pa-total": 6,
    "armure": "Armure légère (cuir) +2",
    "profil-progression": "Étincelle",
    "jalons-ecole-pct": [10, 25, 55, 85],
    "xp-metier-mult": 1.25, "ps-depart": 0, "plafond-attribut": 16,
    "role": "Vigie tireur"
  }
}
```

### 9.3 Cyril

```json
{
  "nom": "Cyril",
  "attr-for": 5, "attr-agi": 6, "attr-end": 6, "attr-esp": 8, "attr-vol": 9, "attr-pre": 8,
  "gauge-vit": 10, "gauge-end": 10, "gauge-mana": 8, "gauge-hon": 5, "gauge-ten": 0, "gauge-forge": 0,
  "clan-nom": "Sceau Pourpre",
  "clan-devise": "Un serment scellé vaut plus qu'une armée",
  "guilde-nom": "Marchands Libres",
  "guilde-spec": "Commerce, contrats, économie",
  "ordre-nom": "",
  "ecole": "Flux Tranchant",
  "tech-ecole": "Flux Tranchant",
  "posture": "Loup",
  "tech-posture": "Loup",
  "m1-nom": "Mage Blanc",
  "m1-stars-val": 1,
  "region": "Cœur Impérial",
  "region-elem": "Métal",
  "arme-nom": "Épée Longue",
  "arme-degats": "1d8",
  "eclats": 90,
  "_extras": {
    "ecole-vtt": "Lame Droite",
    "ecole-rang": 1,
    "tech-ecole-r1": "Première Vague",
    "tech-posture-liste": ["Appel de Meute", "Flanc Coordonné", "Présence Rassurante", "Sacrifice de Meute"],
    "specialite-meute": "Présence Rassurante",
    "resonance": [],
    "mana-mode": "Flux",
    "m2-nom": "",
    "competences": {"medecine": 3, "concentration": 3, "persuasion": 3, "corps_a_corps": 2, "connaissance_droit_serments": 2, "representation": 1, "resistance_mentale": 1, "perception": 1, "esquive_active": 1},
    "avantages": ["Nom Respecté", "Canal Stable (−1 PA synergie Mage Blanc)", "Résistance Partielle"],
    "handicaps": ["Serment Absolu (ne jamais rompre un serment prêté)"],
    "pa-total": 6,
    "armure": "Vêtements renforcés +1",
    "profil-progression": "Graine",
    "jalons-ecole-pct": [20, 40, 70, 95],
    "xp-metier-mult": "1.0 jusqu'au niveau 10, puis 1.5", "ps-depart": 1, "plafond-attribut": "20 sur ESP/VOL/PRE, 16 sinon",
    "posture-legendaire-visee": "Dragon Azur (Honneur ≥ 7)",
    "role": "Voix du serment, soin"
  }
}
```

### 9.4 Pascal

```json
{
  "nom": "Pascal",
  "attr-for": 7, "attr-agi": 6, "attr-end": 8, "attr-esp": 9, "attr-vol": 6, "attr-pre": 7,
  "gauge-vit": 12, "gauge-end": 10, "gauge-mana": 6, "gauge-hon": 6, "gauge-ten": 0, "gauge-forge": 0,
  "clan-nom": "Sceau Pourpre",
  "clan-devise": "Un serment scellé vaut plus qu'une armée",
  "guilde-nom": "Guilde Martiale",
  "guilde-spec": "Capitaineries de défense (garde, siège)",
  "ordre-nom": "Sentinelles du Pacte",
  "ordre-philo": "Veiller les seuils : nul ne passe sans être nommé",
  "ecole": "Gardien Mobile",
  "tech-ecole": "Gardien Mobile",
  "posture": "Loup",
  "tech-posture": "Loup",
  "m1-nom": "Alchimiste",
  "m1-stars-val": 1,
  "region": "Hautes Terres Claniques",
  "region-elem": "Terre",
  "arme-nom": "Épée et Bouclier",
  "arme-degats": "1d6",
  "arm-pieds-nom": "Bottes de marche",
  "arm-pieds-def": "0",
  "arm-pieds-effet": "Blessure Ancienne : −2 à courir",
  "arm-pieds-etat": "Usé",
  "arm-pieds-mat": "cuir",
  "eclats": 60,
  "_extras": {
    "ecole-vtt": "Lame Droite",
    "ecole-rang": 1,
    "tech-ecole-r1": "Garde Haute",
    "tech-posture-liste": ["Appel de Meute", "Flanc Coordonné", "Présence Rassurante", "Sacrifice de Meute"],
    "specialite-meute": "Sacrifice de Meute",
    "resonance": [],
    "mana-mode": "Ancrage",
    "m1-variante": "Martiale",
    "m2-nom": "",
    "competences": {"artisanat": 3, "connaissance_alchimie": 3, "resistance": 3, "corps_a_corps": 2, "perception": 1, "athletisme": 1, "commandement": 1, "medecine": 1, "resistance_mentale": 1, "esquive_active": 1},
    "avantages": ["Corps Endurci", "Ingénieur Méthodique (−1 PA synergie)", "Économie de Matériaux", "Posture Défensive"],
    "handicaps": ["Blessure Ancienne (courir −2)", "Code Personnel Rigide"],
    "pa-total": 7,
    "armure": "Armure légère (cuir) +2 ; bouclier +2 (Défense 18)",
    "profil-progression": "Roc",
    "jalons-ecole-pct": [25, 50, 80, 100],
    "xp-metier-mult": 0.8, "ps-depart": 4, "plafond-attribut": 14,
    "role": "Rempart alchimiste"
  }
}
```

### 9.5 Recrue A : Gardienne des Pierres (nom à donner)

```json
{
  "nom": "Recrue A (Gardienne des Pierres)",
  "attr-for": 8, "attr-agi": 4, "attr-end": 10, "attr-esp": 6, "attr-vol": 9, "attr-pre": 5,
  "gauge-vit": 14, "gauge-end": 10, "gauge-mana": 8, "gauge-hon": 4, "gauge-ten": 0, "gauge-forge": 0,
  "clan-nom": "Cendres Liées",
  "guilde-nom": "Guilde des Soigneurs",
  "ordre-nom": "Porte-Cendres",
  "ecole": "Fondations",
  "tech-ecole": "Fondations",
  "posture": "Ours",
  "tech-posture": "Ours",
  "m1-nom": "Runiste / Glyphiste",
  "m1-stars-val": 1,
  "region": "Terres Ravagées",
  "region-elem": "Terre",
  "arme-nom": "Bâton ferré",
  "arme-degats": "1d6",
  "eclats": 100,
  "_extras": {
    "ecole-rang": 1,
    "tech-ecole-r1": "Solidification",
    "tech-posture-liste": ["Interposition", "Ancrage", "Provocation", "Mur de Chair"],
    "mana-mode": "Ancrage",
    "competences": {"resistance": 3, "concentration": 3, "corps_a_corps": 2, "athletisme": 2, "artisanat": 2, "resistance_mentale": 2, "brisement": 1, "perception": 1, "intimidation_froide": 1},
    "avantages": ["Corps Endurci", "Affinité Élémentaire (Terre)"],
    "handicaps": ["Sensibilité Éthérique Douloureuse (Majeur obligatoire)"],
    "pa-total": 6,
    "armure": "Armure intermédiaire (maille) +3",
    "profil-progression": "Roc",
    "role": "Première ligne mystique (recrue)"
  }
}
```

### 9.6 Recrue B : Langue du Pacte (nom à donner)

```json
{
  "nom": "Recrue B (Langue du Pacte)",
  "attr-for": 3, "attr-agi": 6, "attr-end": 5, "attr-esp": 9, "attr-vol": 9, "attr-pre": 10,
  "gauge-vit": 9, "gauge-end": 10, "gauge-mana": 8, "gauge-hon": 5, "gauge-ten": 0, "gauge-forge": 0,
  "clan-nom": "Mille Voix",
  "clan-devise": "Une rumeur peut abattre un royaume avant qu'une armée ne l'atteigne.",
  "guilde-nom": "Marchands Libres",
  "ordre-nom": "Cultes Syncrétiques",
  "ecole": "Liens Spirituels",
  "tech-ecole": "Liens Spirituels",
  "posture": "Faucon",
  "tech-posture": "Faucon",
  "m1-nom": "Diplomate",
  "m1-stars-val": 1,
  "region": "Cités Libres Marchandes",
  "region-elem": "—",
  "eclats": 150,
  "_extras": {
    "ecole-rang": 1,
    "tech-ecole-r1": "Perception des Esprits",
    "tech-posture-liste": ["Lecture du Terrain", "Point Faible", "Anticipation", "Prédiction"],
    "mana-mode": "Rituel",
    "m2-nom": "Gardien des Accords", "m2-stars-val": 1,
    "competences": {"persuasion": 3, "connaissance_serments_esprits": 3, "representation": 2, "perception": 2, "concentration": 2, "resistance_mentale": 2, "tromperie": 1, "commandement": 1, "esquive_active": 1},
    "avantages": ["Vision Éthérique", "Réseau Local", "Réputation Spécialisée", "Accès Administratif"],
    "handicaps": ["Réputation Entachée (Majeur obligatoire)"],
    "pa-total": 6,
    "armure": "Vêtements renforcés +1",
    "profil-progression": "Étincelle",
    "role": "Diplomate, interprète de l'entité (recrue)"
  }
}
```

---

## 10. Ce qui est inventé, ce qui est à tester, ce qu'il faut demander à krunt

### 10.1 Inventé (aucun appui dans les livres)
Les multiplicateurs d'XP et de PS, les pourcentages de jalons d'École, les plafonds d'attribut par profil, l'hypothèse de 12 000 XP de campagne, les Marques de Pacte et le Souffle du Réceptacle, la spécialité de meute, la limite de *Flanc Coordonné*, l'ordre de meute, la formule de Mana de départ, les Éclats de départ, le monstre d'élite (60 / 17 / +10 / 2d8+9), les rattachements région/clan/ordre pour les ordres inconnus, les deux recrues, les avantages/handicaps uniques (Réceptacle, Ancien Faucon), toutes les clés `_extras`.

### 10.2 À tester (par ordre d'importance)
1. **Tank en modèle C** : mesurer si Krunt3 (Vitalité 13, Mur de Chair, Provocation) tient réellement la première ligne contre le chef de meute (`mecaniques/01` §4.6).
2. **Mana 6 à 8** : un combat de chef suffit-il à vider les trois fiches à 6 Mana ?
3. **Taranis contre Krunt3** : dégâts réels en temps réel (arc 80 m, désavantage au contact).
4. **Pascal à l'Acte I** : sans bombes avant le niveau 4, a-t-il assez à faire en combat ?
5. **Profils de progression** : tableau §5.3 sur une partie réelle ; ajuster les pourcentages de jalons.
6. **Meute à trois** : règles §7.3.

### 10.3 Questions pour krunt
1. **Pascal Gardien Mobile** (au lieu de « Lame Droite » en double avec Cyril) : accepté ?
2. **Krunt3 et Taranis tous deux Espions** : **résolu** (décision de krunt) : Taranis est Chasseur-Pisteur + Cartographe.
3. **Sprite de Krunt3** (hache à deux mains) contre **Deux Lames** : redessiner ou changer d'École ?
4. **Ordre de Krunt3** : **résolu** (décision de krunt) : Frères de l'Épreuve ; « Ordre du Jugement » = surnom.
5. **Les deux recrues** : joueurs ou PNJ ? Le nombre de joueurs réels est-il bien de quatre ?
6. **Honneur** : valeur du Livre I (0 à 10, jamais affichée en chiffres) retenue pour les fiches ?
