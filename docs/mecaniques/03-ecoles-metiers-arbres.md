# Écoles, Postures, Métiers et arbres de compétences : création et progression des quatre personnages

Document de conception du Jeu B (Android, Godot 4, 2D pixel art). Rédigé le 2026-10-05. Domaine : création de personnage, Écoles, Postures, Métiers, arbres de compétences, progression, gestion des quatre personnages.

Sources lues : Livre I ch. 2, 3, 4 (création, Écoles, Métiers, Posture, Compétences) ; Livre II ch. 3 (jalons) et §4 des codes régionaux (20 régions) ; Livre VI en entier (14 + 8 + 7 Écoles, Postures, modes de Mana, secrètes, index) ; Livre VII ch. 1-2 et fiches Chasseur-Pisteur, Dépeceur, Éleveur, Dresseur, Trappeur (tables 1-30 relues) ; Livre VIII ch. 1-3, 5-6 ; Livre IX ch. 3 et 5, tableau des 14 armes. Les 25 autres fiches de Métiers n'ont pas été relues ligne à ligne (balayage de structure par l'audit précédent).

Statut : proposition, rien n'est validé par krunt. Tous les chiffres de jeu sont marqués « à tester ».

**Conflits entre livres résolus dans ce document (options provisoires du brief)** :
- Option 1 : attributs FOR/AGI/END/ESP/VOL/PRE, Vitalité max = 4 + END, Endurance 10 (le Livre X est ignoré).
- Option 2 : XP par métier, niveaux 1-30, paliers 5/10/15/20/25/30 validés par jalons narratifs (Livre II « sans XP » et Livre I « 3 étoiles » sont réconciliés ci-dessous : étoiles = tranches de 10 niveaux).
- Option 4 : Honneur 0-10 (Postures Légendaires à Honneur 7+).
- Option 9 : 30 niveaux, 2 métiers maximum (le « 3e métier » du Livre VII est supprimé).
- Option 10 : éléments Feu, Eau, Terre, Vent, Foudre, Glace + Ombre/Éther ; les Postures Légendaires gardent leurs noms et leur cycle Bois/Feu/Métal/Eau/Terre uniquement comme habillage narratif, jamais comme élément de dégâts.
- Mana de départ : le Livre I dit « 2 × rang » (2 Mana au rang I, soit une seule Technique), le Livre VI dit « 6-8 Mana au rang I ». Conflit résolu par le Livre VI (table au §3.2 ci-dessous), seul compatible avec une action en temps réel.

---

## 1. Ce que disent les livres

### 1.1 Les trois couches (Livre I ch. 3, Livre VI ch. 1)

| Couche | Question | Contenu | Progression dans les livres |
|---|---|---|---|
| École | Comment ? | 5 rangs, 1 Technique par rang, mode de récupération du Mana, tabou | Rang I à V, jamais « par points » : moment narratif fort |
| Métier | Quoi ? | 30 Métiers, 5 blocs, 2 maximum par personnage | Livre I : 3 étoiles ; Livres VII/IX : 30 niveaux, XP |
| Posture | Pourquoi ? | 4 naturelles, 5 légendaires, 1 suprême, Résonances | Évolue par jalon narratif ; Légendaire à Honneur 7+ |

Phrase du Livre I ch. 3 §5 à retenir : « pas un système de classes, pas un arbre de talents, mais trois questions distinctes ». Un arbre de compétences est donc une **traduction** (nécessaire pour un jeu vidéo), pas une fidélité au livre. Voir §2.

### 1.2 Création de personnage (Livre I ch. 3 §7, 10 étapes)

| Étape | Règle | Chiffres |
|---|---|---|
| 1 | La phrase (qui est-il, quelle tension) | texte libre |
| 2 | Origine : 1d20 sur les 20 régions | avantage(s) de création, parfois +1 attribut |
| 3 | Attributs | 42 points sur 6 attributs, min 3, max 12 par attribut (avant bonus d'origine) |
| 4 | Jauges | Vitalité max = 4 + END (7 à 16 cases) ; Endurance max 10 |
| 5 | École rang I (Aspirant) | 2 premières Techniques accessibles, Mana de départ, +2 points de Compétence |
| 6 | Métier principal ★ (+ secondaire optionnel) | +2 points de Compétence |
| 7 | Posture : questionnaire de 5 questions | +1 point de Compétence ; 4 Techniques de Posture |
| 8 | Compétences | 12 points libres + 5 de bonus = 17 ; max 3 par Compétence à la création |
| 9 | Honneur de départ | 4-6 (« Reconnu »), origine ±1 |
| 10 | La phrase, revisitée | confirmation |

Livre VIII ch. 1 ajoute : **6 Points d'Avantage (PA)** et **1 Handicap Majeur obligatoire** (+3 PA de plus au maximum via handicaps, plafond de gain +4 PA, 2 Avantages Majeurs et 3 Mineurs au maximum, Avantage lié au métier principal : −1 PA). Un Handicap doit être activé par le MJ au moins une fois par session. Et 5 axes culturels (Combat : Devoir / Nécessité / Expression ; Mort : Sacrée / Pragmatique / Redoutée ; Magie : Sacrée / Outil / Suspecte ; Autorité : Légitime / Contractuelle / Rejetée ; Étranger : Hospitalité / Méfiance / Rejet) : une option par axe, aucun bonus chiffré, ils modifient les réactions des PNJ et les gains d'Honneur.

Les attributs secondaires sont dérivés : Défense = AGI+END, Initiative = AGI+VOL, Précision = AGI+ESP, Résistance mentale = VOL+ESP, Autorité sociale = PRE+Honneur. Les Compétences vont de 0 à 5 (21 Compétences listées).

### 1.3 Les 20 régions d'origine (Livre II ch. 4 §4, tableau d20 ; Livre IX ch. 3 pour les extrêmes)

| d20 | Région | Avantage principal | Contrainte principale |
|---|---|---|---|
| 1 | Cœur Impérial | Avantage vs autorités, +1 Réputation | Désobéissance publique = −1 Honneur |
| 2 | Provinces Nobles | +1 Statut, cercles nobles | Obligations familiales |
| 3 | Cités Libres Marchandes | Avantage négociation | Dettes contraignantes |
| 4 | Hautes Terres Claniques | **+1 VOL**, résiste à la peur clanique | Vendettas de clan |
| 5 | Forêts Totémiques | Bonus survie/traque | −1 social en ville |
| 6 | Îles des Serments | **+1 END**, résilience après échec critique | Refuser un défi = −1 Honneur |
| 7 | Marches Frontalières | Avantage en terrain hostile | Réputation instable ailleurs |
| 8 | Terres Ravagées | Résistance corruption | Marques permanentes |
| 9 | Déserts Rouges | Survie extrême | −1 social urbain, impulsivité punie |
| 10 | Sanctuaires Éthériques | Avantage rituels | Dogmes stricts |
| 11 | Cités Astrales | Savoir rare | −1 pratique |
| 12 | Failles du Monde | Avantage magie risquée | Corruption progressive |
| 13 | Royaumes Marins | Avantage aquatique | −1 hors mer après 2 sessions |
| 14 | Archipels Nomades | +1 mobilité, esquive | Autorité rejetée |
| 15 | Royaumes de l'Ombre | Avantage discrétion | Réputation négative (bloc Ordre) |
| 16 | Cités Voilées | Avantage tromperie | Pas de liens sincères officiels |
| 17 | Théocraties Sacrées | Protection corruption | Surveillance si transgression |
| 18 | Terres des Prophètes | Avantage intuition | Destin imposé |
| 19 | Confluences | Bonus polyvalent | Identité floue |
| 20 | Terres Sans Nom | Liberté totale | Aucun réseau |

Constat chiffré : seules **deux** régions (4 et 6) donnent un bonus d'attribut explicite ; les 18 autres sont des « avantages » narratifs sans valeur numérique. Livre IX ajoute pour chaque région un « Avantage Cheater » et un « Malus Inhumain » (ex. Îles des Serments : « L'Épreuve Suprême », transformer un échec critique en réussite héroïque, contre « Toujours Plus Haut », chaque réussite impose une épreuve plus dangereuse), réservés aux campagnes avancées. Le Livre I annonce une table d'origine « §4 de ce chapitre » qui n'existe pas (le §4 est la Posture) : la table réelle est dans le Livre II.

### 1.4 Les Écoles (Livre VI)

**Inventaire** : 14 Martiales (une arme, une philosophie, un tabou), 8 Mystiques (un élément ou domaine, des interdits doctrinaux), 7 Techniques (savoirs pratiques, rangs I-V avec « capacité clé », pas de Techniques de combat), 4 domaines Interdits (Nécrotechnie, Manipulation mémorielle, Corruption dirigée, Pactes abyssaux : jamais à la création, jalon narratif obligatoire), 15 Techniques Secrètes en 5 familles (hors rang, pas plus puissantes qu un rang V, découvertes).

**Rangs et coûts** : une Technique par rang. Rangs I, II, III : 2 Mana ; IV : 3 Mana ; V : 4 ou 5 Mana. Titres : Aspirant, Initié, Disciple, Maître, Pilier. La table du Livre VI §13.6 donne le Mana typique : rang I 6-8, II 8-10, III 10-12, IV 12-15, V 15+.

**Les quatre modes de récupération du Mana** (Livre VI ch. 3) :

| Mode | Gain de Mana (livre) | Écoles |
|---|---|---|
| Flux | +1 par attaque réussie, +1 par déplacement significatif, +2 par manœuvre réussie | Flux Tranchant, Danse Rouge, Mutation, Ascension, Rafale, Voies Hautes |
| Ancrage | +1 par round sans bouger, +2 pour un tour entièrement défensif, +1 par dégât absorbé sans reculer | Coup Final, Mur Vivant, Fracas Juste, Gardien Mobile, Ancrage (arbalète lourde), Fondations |
| Rituel | Récupération complète lors d'un repos court avec action rituelle, +1 par action hors combat liée à l'école, rien en combat | Résonances, Marées Liées, Liens Spirituels, Archives Stellaires, École du Flux, Souffle Long |
| Sacrifice | +2 par point de Vitalité perdu volontairement, +1 par état négatif accepté, +3 pour une chute à 0 Vitalité survivie | Jugement Scellé, Cendres Vives, Fil Céleste, Équilibre Instable |

À 0 Mana, une Technique d'École reste possible : elle coûte de l'Endurance à la place et déclenche un jet de Tension (Livre I ch. 2 §6).

**Les 14 Écoles Martiales** (arme, mode, tabou ; Technique de rang V) :

| # | École | Arme | Mode | Tabou | Rang V (coût) |
|---|---|---|---|---|---|
| 1 | Coup Final | Grande Lame | Ancrage | Frapper sans intention de conclure | Frappe Décisive (4) |
| 2 | Flux Tranchant | Épée Longue | Flux | Briser volontairement le flux | Danse du Vide (5) |
| 3 | Gardien Mobile | Épée & Bouclier | Ancrage | Abandonner un allié protégé | Rempart Vivant (4) |
| 4 | Danse Rouge | Double Lame | Flux | Perdre le contrôle de soi | Transe Écarlate (4) |
| 5 | Fracas Juste | Marteau | Ancrage | Frapper hors cible vitale | Jugement d'Impact (5) |
| 6 | Résonances | Cor de Chasse | Rituel | Jouer pour soi seul | Symphonie de Guerre (5) |
| 7 | Mur Vivant | Lance | Ancrage | Rompre la ligne | Bastion Absolu (4) |
| 8 | Jugement Scellé | Arbalète-Lance | Sacrifice | Explosion non maîtrisée | Sentence Pyrique (4) |
| 9 | Mutation | Hache-Épée | Flux | S'enfermer dans une forme | Forme Instable Ultime (5) |
| 10 | Équilibre Instable | Lame Chargée | Sacrifice | Libérer sans préparation | Libération Totale (5) |
| 11 | Ascension | Glaive-Insecte | Flux (et Sacrifice, conflit) | Rompre le lien avec le Kinsect | Ascension Parfaite (5) |
| 12 | Souffle Long | Arc | Rituel | Tirer sans cible claire | Flèche du Silence (4) |
| 13 | Rafale | Arbalète Légère | Flux | (absent du livre) | Pluie Contrôlée (4) |
| 14 | Ancrage | Arbalète Lourde | Ancrage | (absent du livre) | Barrage Absolu (4) |

**Les 8 Écoles Mystiques** : Marées Liées (Eau, Rituel), Cendres Vives (Feu, Sacrifice, ne peut pas soigner), Voies Hautes (Vent, Flux), Fil Céleste (Foudre, Sacrifice), Fondations (Terre, Ancrage), École du Flux (Éther pur, Rituel), Liens Spirituels (Âme, Rituel), Archives Stellaires (Cosmique, Rituel). Rangs : canalisation sûre, sorts codifiés, effets persistants, altération de zone, rituel majeur. Chaque École a des « interdits » doctrinaux (Marées Liées : destruction brutale, assèchement volontaire).

**Les 7 Écoles Techniques** : Forge d'Éther, Alchimie Structurée, Chirurgie & Reconstruction, Logistique & Réseaux, Archivistes Techniques, Dressage & Domestication, Architecture & Fortification. Pas de Technique chiffrée : une « capacité clé » par rang (ex. Chirurgie rang I : stabiliser un personnage à 0 Vitalité ; Dressage rang III : lien de confiance avec une créature précise ; Architecture rang IV : superviser un Bastion de rang II).

**Compatibilités** : « une école = une incompatibilité » (une seule École principale ; deux Écoles martiales sont incompatibles ; une École mystique peut coexister avec une martiale). Changer d'École est une rupture doctrinale avec perte d'Honneur. Compatibilité conseillée Posture x École au Livre VI §13.5.

### 1.5 Les Postures (Livre VI ch. 4-7, Livre I ch. 3 §4)

**Quatre naturelles**, 4 Techniques chacune, toutes à **2 Endurance** :

| Posture | Rôle | Techniques |
|---|---|---|
| Loup (cohésion) | soutien de groupe | Appel de Meute (Ouverture pour un allié), Flanc Coordonné (+d6, ignore 1 armure si un allié a frappé), Présence Rassurante (retire Exposé/Déséquilibré/Épuisé), Sacrifice de Meute (−3 Vitalité, alliés Avantage) |
| Faucon (lecture) | information | Lecture du Terrain (révèle état et prochain mouvement), Point Faible (Avantage au groupe), Anticipation (annule une attaque), Prédiction (nomme l'action : si juste, Avantage au groupe) |
| Ours (protection) | tank | Interposition, Ancrage (immunité au déplacement), Provocation (cible l'Ours, alliés Ouverture gratuite), Mur de Chair (−2 dégâts aux alliés au contact) |
| Félin (précision) | burst | Frappe Décisive (dés x2, risque en retour), Disparition, Patience du Prédateur (Avantage si aucune attaque), Ciblage Vital (ignore 2 armure) |

**Cinq légendaires** (Honneur 7+ et jalon majeur, s'ajoutent à la Posture naturelle) : Dragon Azur (soin, ultime Éclosion 4 End, 1 par chasse), Oiseau Vermillon (Déflagration 4 End), Tigre Blanc (Jugement Final 5 End), Tortue Noire (Abîsse 4 End), Phénix (disparu, moteur de campagne, inaccessible). Chacun : 4 Techniques + 1 ultime. **Posture Suprême** (Dragon Ancien) : unique par campagne, nécessite une Posture Légendaire, Technique Équilibre des Cinq (8 End, 1 par session), un « prix » narratif (dette ouverte).

**Résonance** : quand la Posture change par jalon, une Technique de l'ancienne reste disponible 1 fois par session, gratuite, si l'on peut dire en une phrase pourquoi. Elles s'accumulent sans limite.

**Questionnaire** : 5 questions (menace, victoire, sacrifice, ennemi plus fort, question ouverte du MJ), chaque réponse pointe vers une Posture (tableau Livre VI §4.1).

### 1.6 Les 30 Métiers (Livre VII)

| Bloc | Métiers |
|---|---|
| 1. Artisans & Techniques | Forgeron d'Armures, Forgeron d'Armes, Artisan d'Éther, Runiste/Glyphiste, Alchimiste, Herboriste/Botaniste |
| 2. Monde Sauvage & Chasse | Chasseur-Pisteur, Dépeceur, Éleveur de Créatures, Dresseur de Monstres, Naturaliste, Trappeur Élémentaire |
| 3. Savoir & Logistique | Maître des Montures, Scribe d'Éther, Cartographe, Médecin/Chirurgien, Conservateur/Artisan de Reliques, Analyseur d'Éther |
| 4. Social & Politique | Diplomate, Marchand/Logisticien, Instructeur/Mentor, Sentinelle d'Honneur, Espion/Infiltrateur, Gardien des Accords |
| 5. Magie & Arcanes | Mage Blanc, Mage Noir (niveau 30+ requis, Livre I), Mage Rouge, Mage Vert, Occultiste d'Ombre, Élémentaliste |

Chaque fiche contient : statut social par tranche de 5 niveaux, synergies naturelles, « métier en tension », 5 variantes culturelles, un tableau des niveaux 1 à 30 (compétence, outil/condition, **DD du test**, capacité débloquée) et **6 paliers de signature** (5, 10, 15, 20, 25, 30). Les DD vont de 8 (niveau 1) à 32 (niveau 30) ; ils baissent aux niveaux 6 (11) et 17 (18) dans toutes les fiches. XP cumulée (Livre IX ch. 5, **identique pour les 30 métiers**) : 700 (niv. 5), 3 200 (10), 9 200 (15), 20 200 (20), 39 200 (25), 72 000 (30). Règle : 2 Métiers, secondaire plus lent. Synergies recommandées (Livre VII ch. 2) : Forgeron d'Armes + Chasseur-Pisteur, Forgeron d'Armures + Dépeceur, Alchimiste + Herboriste, Cartographe + Maître des Montures, Chasseur-Pisteur + Trappeur Élémentaire, Instructeur + tout (progression plus lente), etc. Combinaisons instables : Occultiste + Médecin, Mage Noir + Mage Blanc, Espion + Sentinelle.

### 1.7 Jalons (Livre II ch. 3)

Cinq types : Métier, Compétence, Posture, Bastion, Honneur. Un jalon se déclenche quand le monde **voit et reconnaît** un acte. Cadence indicative pour 4 joueurs : 2 à 4 jalons individuels et 1 collectif par arc de 3 à 5 sessions. La Trinité Acte / Trace / Conséquence est la grille de lecture. Il n'existe **pas de jalon d'École** alors que le Livre I exige un « moment narratif fort » pour chaque rang : lacune comblée au §6.

---

## 2. Diagnostic critique : ce qu'il faut couper, fusionner, ajouter

**Verdict en trois lignes.** Le livre décrit une identité à trois couches, riche et cohérente, mais **sa progression est faite pour un maître de jeu humain** (« le MJ valide »). Un jeu vidéo n'a pas de MJ : il lui faut des déclencheurs mesurables. Et 29 Écoles + 30 Métiers x 30 niveaux représentent environ 1 500 points de contenu pour un développeur seul ; la démo n'en peut porter que 1 %.

**Ce que les chiffres disent du volume :**

| Élément | Quantité dans les livres | Coût de contenu en jeu |
|---|---|---|
| Techniques d'École martiales | 14 x 5 = 70 | 70 skills x (animation + effet + icône + son) |
| Techniques d'École mystiques | 8 x 5 = 40 | 40 effets de zone/états |
| Techniques de Posture | 16 naturelles + 25 légendaires + 1 suprême | 42 |
| Techniques Secrètes | 15 | 15 |
| Niveaux de Métier | 30 x 30 = 900 lignes | 900 capacités (mais voir ci-dessous) |
| Total approximatif | plus de 1 000 éléments | irréaliste pour 14-24 h par semaine |

**Les tables de Métiers sont en partie des gabarits.** Relues pour Chasseur-Pisteur, Dépeceur, Dresseur, Trappeur, Éleveur : les niveaux 16 à 30 suivent le même squelette dans les cinq (16 « Perception/Imprégnation éthérique mineure », 21 « Auto-régulation/protection », 24 « Fusion intentionnelle », 25 « Scellement runique mineur », 26 « Créatures d'Élite », 27 « Harmonisation », 28 « Scellement avancé, doubles runes », 29 « pur, essence primordiale », 30 « Légendaire/Nommé Vivant »), avec des mots changés. Les paliers de signature se nomment toujours « X Maîtrisé, Signature, d'Élite, Chef-d'œuvre, Runo-X, Nommé Vivant ». **Conséquence** : on ne peut pas donner 30 mécaniques de jeu distinctes par métier. Les niveaux 1 à 15 sont différenciés et concrets ; au-delà, il faut écrire des effets originaux ou accepter des niveaux « techniquement » vides (gain de statut et de tolérance de mini-jeu seulement).

**Ce qu'il faut couper (recommandation) :**

1. **Bloc 5 « Magie & Arcanes » comme Métiers jouables** : il double les 8 Écoles Mystiques (Mage Rouge = Cendres Vives, Mage Vert = Voies Hautes/Fondations, etc.). Garder les Écoles Mystiques seulement ; les 6 « Mages » deviennent des titres de PNJ.
2. **Les 7 Écoles Techniques ne sont pas des arbres de combat** : elles recoupent les Métiers (Forge d'Éther = Forgeron + Artisan d'Éther ; Alchimie = Alchimiste ; Chirurgie = Médecin ; Dressage = Dresseur ; Architecture = Bastion). Les fondre dans les arbres de Métier (une « école technique » devient le rang d'un métier) et dans le Bastion. Supprimer comme catégorie d'École jouable.
3. **Les Écoles Interdites** (4) : événements de campagne, jamais un arbre. Pas de v1.
4. **Les Techniques Secrètes** (15) : garder 4 comme récompenses de quêtes de fin de jeu (Retour en Arrière, Emprunt de Posture, Lecture de Cicatrice, Marque du Temps) ; les familles Phénix et Fusion sont hors périmètre.
5. **Les 14 Écoles Martiales** : regrouper par famille d'animation (cf. `docs/livres-crs-vers-jeu-b.md`, 6 familles). Démo : 3. Version 1.0 : 7 (une ou deux par famille). Les Écoles 13 et 14 n'ont pas de tabou : à écrire ou à couper (recommandation : couper Rafale, garder Ancrage lourd en v2).
6. **Les 30 Métiers** : démo 3 (Chasseur-Pisteur, Dépeceur, Herboriste), version 1.0 environ 12 (voir §10). Les autres restent des PNJ et des étiquettes d'Honneur.
7. **Les Compétences (21)** : une couche de plus (attributs 42 pts, 12 + 5 points de Compétence, 6 PA d'Avantages, Écoles, Métiers, Posture : six couches !). Pour le jeu : 8 Compétences (Corps-à-corps, Tir et lancers, Esquive active, Perception, Traque, Artisanat, Médecine, Persuasion), niveaux 0 à 3 à la création, 5 au plafond, **sans écran de répartition dans la démo** (valeurs fixées par personnage).
8. **Avantages/Handicaps** (catalogue du Livre VIII : ~40) : garder 12 Avantages et 10 Handicaps qui se traduisent en règles mesurables (§4.5). Supprimer l'obligation « le MJ active un Handicap par session » : le jeu le déclenche par règle.
9. **Variantes « Cheater / Inhumain » et Marque Régionale hardcore** (Livre IX) : v2, mode optionnel.
10. **Les ultimes à 8 Endurance** (Équilibre des Cinq) : avec Endurance 10, 8 est presque tout le réservoir ; la Posture Suprême est une cinématique et une capacité unique, pas un arbre.

**Ce qu'il faut ajouter (le livre n'a pas de quoi le faire) :**

- Un **déclencheur de jalon mesurable** (un jalon n'est plus « reconnu par le MJ » mais défini par des conditions de journal, voir §6.3).
- Une **monnaie de progression** (Points de Savoir) puisque le livre n'a pas de points à dépenser.
- Un **jalon d'École** (rang) à côté des cinq types du Livre II.
- Des **variantes de Techniques** (nœuds latéraux) : sans elles, un arbre d'École serait une file de 5 cases à débloquer dans l'ordre, sans choix.

---

## 3. Traduction en mécaniques de jeu vidéo

### 3.1 Principes de conversion (valables pour tout le document)

| Concept du livre | Dans le jeu | Raison |
|---|---|---|
| 1 round | **4 secondes** réelles | durée d'un enchaînement lisible ; à tester |
| Jet d'attaque d20 | **abandonné en combat** : touche = collision de hitbox | un d20 ne se lit pas à 360 px |
| « Avantage » | +25 % de dégâts sur la prochaine touche (fenêtre de 4 s), ne se cumule pas | le livre dit « deux sources = un seul Avantage » |
| « Désavantage » | −25 % de dégâts, ou perte d'un état | |
| « dé de dégâts » | multiplicateur = moyenne du nouveau dé / moyenne du dé de l'arme (d12 sur arme d10 = x1,2 ; dé −2 = x0,65 environ) | garde les proportions du livre sans dé |
| Ouverture | marqueur sur un allié : sa prochaine Technique coûte 0 pendant 3 s | la règle du livre (« hors de son tour ») devient une fenêtre |
| Jet de Tension | +1 Tension collective (jauge d'un autre chapitre) | |
| Exposé / Déséquilibré / Épuisé / Concentré / En Transe / Hors de portée | états à icône et durée fixe (Exposé = +25 % dégâts reçus 4 s ; Déséquilibré = étourdi 1,5 s et Techniques bloquées ; Épuisé = −25 % ; En Transe = +50 % dégâts, +25 % dégâts reçus 8 s) | |
| Distances | 1 m = 32 px (héros de 64 px = 2 m environ) | à confirmer avec le domaine combat |

### 3.2 Jauges (Livre I ch. 2)

| Jauge | Formule | Dans le jeu |
|---|---|---|
| Vitalité | 4 + END (7 à 16 cases) | segments de cœur ; la case vide « cicatrice » : à 0, hors de combat 6 s puis relevé par allié, sinon échec de chasse |
| Endurance | 10 | barre de 10 segments ; régénération 1 par 1,2 s hors esquive ; esquive 1 ; Technique de Posture 2 |
| Mana | selon rang : **6 / 8 / 10 / 12 / 15** (rangs I à V) | barre à segments de 1 ; à 0, Technique « à crédit » : coût x2 en Endurance, +1 Tension |
| Honneur | 0-10 | jamais affiché en chiffre (le livre le cache au joueur) : jauge de 5 états (Paria, Suspect, Reconnu, Estimé, Légendaire) visible en écran Clan |

### 3.3 Attributs : effet en jeu (hypothèse à tester)

| Attribut | Effet |
|---|---|
| FOR | dégâts de mêlée x(1 + 0,04 x (FOR − 6)) ; charge portable |
| AGI | vitesse de déplacement +2 % par point au-dessus de 6 ; fenêtre d'esquive parfaite +10 ms par point |
| END | Vitalité (4 + END) ; résistance aux états poison/épuisement |
| ESP | tolérance du mini-jeu de lecture d'indice ; Précision ; alchimie |
| VOL | Mana max +1 par 3 points au-dessus de 6 ; résistance à la peur/panique ; Initiative |
| PRE | options de dialogue et gains d'Honneur au Récit ; Autorité sociale |

### 3.4 Les modes de Mana en temps réel

| Mode | Règle de jeu | Régulateur anti-abus | Public visé |
|---|---|---|---|
| Flux | +1 Mana par touche (une fois par 6 s au maximum), +1 par esquive/dash de 96 px ou plus, +2 par esquive parfaite ou parade réussie | plafond environ 12 Mana/min | joueur mobile, agressif |
| Ancrage | +1 Mana toutes les 4 s **immobile** (garde levée ou charge en cours), +2 si on tient une garde 4 s, +1 par coup absorbé sans reculer | plafond environ 15 Mana/min mais seulement à l'arrêt | joueur patient, tank |
| Rituel | aucun gain en combat ; **remplissage complet** en 6 s d'action rituelle (immobile, interrompue par un coup) à une **Halte** ; +1 par action école hors combat (cueillir, offrande, eau) | Haltes tous les 2 500 px environ dans les arènes longues (à valider avec le domaine arènes) | joueur planificateur, soutien |
| Sacrifice | +2 par case de Vitalité perdue volontairement (bouton « Prix », 1 case), +1 par état négatif accepté, +3 si on survit à 0 | 1 Prix par 10 s ; jamais sous 1 case sauf rang V | joueur expert, haut risque |

Revenu moyen visé : environ 8 Mana/min en combat actif (hors Rituel : réservoir x1,25 en compensation). La règle « à 0 Mana, Technique à crédit en Endurance » est conservée parce qu'elle donne un choix tendu au lieu d'un bouton grisé.

### 3.5 Postures en jeu

Les Techniques de Posture (2 Endurance) sont des **boutons de rôle** avec recharge de 6 s ; elles s'insèrent dans le même sélecteur que les Techniques d'École (§5.7). Traductions principales :

| Posture | Technique | Effet jeu (à tester) |
|---|---|---|
| Loup | Appel de Meute | cible d'allié : Ouverture 3 s ; en solo, le partenaire IA ou le familier reçoit l'Ouverture |
| Loup | Sacrifice de Meute | −1,5 case de Vitalité, tous alliés Avantage 4 s |
| Faucon | Lecture du Terrain | affiche 4 s la barre de Vitalité de la créature, ses états et sa prochaine attaque télégraphiée (+0,6 s de préavis) |
| Faucon | Prédiction | choisir parmi 3 icônes l'attaque suivante : si juste, groupe Avantage 4 s |
| Ours | Provocation | 4 s, la créature cible l'Ours ; alliés : Ouverture |
| Ours | Interposition | redirige le prochain coup reçu par l'allié désigné (dégâts sur l'Ours) |
| Félin | Frappe Décisive (Posture) | x2 dégâts du prochain coup ; si raté : subit 50 % des dégâts qu'il aurait infligés |
| Félin | Patience du Prédateur | 4 s sans attaquer : prochaine touche Avantage et ignorant Désavantage |

**Résonance** : après un changement de Posture (jalon), un emplacement « Résonance » est créé ; la condition narrative devient un **contexte détectable** (liste de 3 contextes par Technique, ex. Interposition : un allié sous 30 % de Vitalité est ciblé). Une fois par chasse, gratuite. La règle du livre « le MJ juge » est impossible : un contexte par Technique est le prix à payer.

### 3.6 Jets de Métier : du d20 au mini-jeu

Le test d20 + attribut + Compétence contre DD devient une **marge** : m = B + 10 − DD, avec B = attribut + Compétence + niveau de métier / 3 (invention, à tester) :

| Marge | État du test | Ce qui se passe |
|---|---|---|
| m ≥ 5 | Maîtrisé | succès automatique, aucune saisie |
| 0 ≤ m ≤ 4 | **Réussite tendue** (le DD à DD+4 du brief) | mini-jeu à fenêtre large ; succès avec un coût (temps, usure, qualité −1) |
| −5 ≤ m ≤ −1 | Difficile | mini-jeu à fenêtre étroite, pas d'erreur permise |
| m ≤ −6 | Hors de portée | grisé, indice « revenir plus fort » |

Les DD des fiches (8 à 32) deviennent les **difficultés des cibles** (une trace de ◆ Commun : DD 8 à 13 ; un ◆◆◆ : DD 18 à 22) et non des jets de dés.

---

## 4. Création de personnage : écrans et prologue jouable

### 4.1 Principe

Quatre personnages écrits d'une seule histoire, jouables chacun par un joueur réel. Il ne faut donc **ni d20 d'origine ni création libre complète dans la démo**. Deux parcours :

- **Parcours Histoire** (par défaut, jeu) : le personnage est prédéfini ; le joueur prend des décisions qui comptent (Posture, Handicap, Métier secondaire, répartition de 12 points d'attributs libres autour d'un gabarit).
- **Parcours Atelier** (CharForge, outil et table) : création complète en 10 étapes, qui exporte le même JSON. C'est aussi ce qui sert à la version JDR de table.

Règle : le même schéma de données (§5.8) pour les deux.

### 4.2 Proposition provisoire des quatre personnages (à valider par krunt)

Les quatre personnages n'existent pas encore dans les documents (seul un sprite de chasseur à grande lame est défini dans `docs/prompts-personnages.md`). Cette répartition couvre les 4 Postures (4 rôles de coopération), 4 modes de Mana distincts et les métiers de la démo.

| | Perso 1 | Perso 2 | Perso 3 | Perso 4 |
|---|---|---|---|---|
| Rôle | burst, pisteur | tank, forge | soutien | information, zone |
| Posture attendue | Félin | Ours | Loup | Faucon |
| École | Coup Final (Grande Lame, Ancrage) | Mur Vivant (Lance, Ancrage) | Résonances (Cor, Rituel) | Marées Liées (Eau, Rituel) |
| Métiers | Chasseur-Pisteur + Trappeur Élémentaire | Dépeceur + Forgeron d'Armures | Herboriste + Médecin | Naturaliste + Cartographe |
| Région | 4 Hautes Terres (+1 VOL) | 6 Îles des Serments (+1 END) | 3 Cités Libres Marchandes | 10 Sanctuaires Éthériques |
| Honneur de départ | 5 | 5 | 6 | 4 (marginal) |
| Handicap majeur type | Dette de Sang | Refus de défi = honte | Paria (cités) ou Dette | Dogmes stricts |

Note : Posture et École de tous les personnages se croisent (Faucon + Marées Liées : « tension créative », le livre ne la recommande pas, ce qui en fait un bon personnage). Le Félin et Coup Final partagent un nom de Technique (« Frappe Décisive ») : renommer l'une dans les données (`cf_t5` / `pos_felin_t1`) pour éviter la collision.

### 4.3 Flux de création (écrans)

| # | Écran | Ce que le joueur fait | Durée visée |
|---|---|---|---|
| C1 | Choix du personnage | 4 cartes (portrait 64 px agrandi, phrase d'accroche, rôle), indication des places coop prises | 20 s |
| C2 | Phrase (étape 1) | choisit 1 phrase parmi 3 qui expriment la tension du personnage ; stockée dans le journal | 20 s |
| C3 | Origine (étape 2) | carte des régions (3/4 en vignettes) : la région de ce personnage est fixée, le joueur choisit l'axe culturel d'1 des 5 axes seulement (Combat, Mort, Magie, Autorité, Étranger) en démo ; les 5 en v1 | 40 s |
| C4 | Attributs (étape 3) | 42 points, gabarit prérempli, 6 curseurs avec boutons − / + de 44 px, bornes 3-12, aperçu « Vitalité 4+END » | 60 s |
| C5 | Avantages / Handicaps | 6 PA, cartes à balayer ; 1 Handicap majeur imposé (4 propositions) | 60 s |
| C6 | École | démonstration de 8 s en boucle des 2 premières Techniques ; confirmation | 30 s |
| C7 | Métier | 2 cartes (principal imposé, secondaire au choix parmi 2) | 20 s |
| C8 | Posture | **pas un écran : voir prologue (§4.4)** ; l'écran affiche seulement le résultat | 10 s |
| C9 | Compétences | démo : fixées ; v1 : répartition de 12 points (8 Compétences) | 0 s / 60 s |
| C10 | Fiche et phrase revisitée | récapitulatif ; la phrase est relue ; « Commencer » | 20 s |

Total démo : environ 4 minutes de menus, ce qui est acceptable parce que le prologue (4.4) porte le reste. Si cela dépasse 5 minutes, couper C3 et C5 (valeurs fixées).

### 4.4 Le prologue jouable (questionnaire de Posture en scènes)

Le questionnaire en 5 questions (Livre I §4.3) devient **4 vignettes jouées + 1 choix narratif** (la question du MJ), au cours d'un prologue de 8 à 12 minutes par personnage, mêlant les trois modes de jeu. Aucune étiquette de Posture n'apparaît : le jeu note les comportements.

| Question du livre | Vignette de jeu | Ce que le jeu mesure | Loup / Faucon / Ours / Félin |
|---|---|---|---|
| Q1 la menace arrive | plateforme de profil : une créature de ◆ surgit, 5 s, 4 gestes possibles | premier bouton pressé | appeler le groupe (bouton cri) / reculer et observer (zoom caméra) / s'interposer devant le PNJ / contourner par la droite |
| Q2 la chasse est finie | écran de score : 4 conditions de victoire cochées en tapant | choix de la fierté | tous vivants / anticipé / cicatrices / le coup final |
| Q3 le clan demande un sacrifice | dialogue du Retour au Clan : 4 réponses | donner part du butin, plan, sécurité, anonymat | |
| Q4 l'ennemi est plus fort | 3/4 : une meute bloque le chemin ; 4 solutions praticables | ressources collectives / examiner ce qu'on a raté / tenir le passage / attendre | |
| Q5 question ouverte | dialogue sur le passé du personnage | confirme ou nuance | |

Règle de décision : chaque vignette ajoute 1 point à une Posture, la question 5 départage les égalités ; le joueur voit « Posture proposée : X » et peut **accepter ou choisir la seconde** (tension) au prix d'une phrase d'explication. Pour que la coopération fonctionne, le lobby avertit si deux joueurs ont la même Posture (mais ne l'interdit pas).

**Un prologue par personnage** (4 prologues de 8 à 12 minutes) est un **gros coût de contenu** : 40 minutes de jeu à produire. Version économique : un prologue commun de 15 minutes (une chasse de nécessité) où chaque joueur traverse les 4 vignettes avec son personnage, avec 3 lignes de dialogue spécifiques par personnage. Recommandation : commencer par la version économique.

### 4.5 Avantages et Handicaps : catalogue minimal jouable

| Type | Nom (Livre VIII) | Règle de jeu mesurable |
|---|---|---|
| Av. Majeur 3 PA | Maîtrise de Combat | +1 attaque ou défense (fixe), 1 manœuvre exclusive (une variante de Technique) |
| Av. Majeur 3 PA | Présence Martiale | 1re attaque ennemie du combat : Désavantage sur les ◆ ; immunité peur 1 fois par chasse |
| Av. Majeur 3 PA | Corps Endurci | coups ≤ 2 dégâts ignorés hors chasse ; Épuisé retiré 1 fois par chasse |
| Av. Majeur 3 PA | Nom Respecté | +2 aux dialogues avec autorités ; condition Honneur ≥ 5, suspendu à Honneur ≤ 0 |
| Av. Mineur 1 PA | Réflexes Affûtés | +1 Initiative ; Posture Défensive (+1 défense si immobile) |
| Hand. Majeur +3 PA | Paria | −2 aux dialogues institutionnels ; certaines boutiques fermées |
| Hand. Majeur +3 PA | Dette de Sang | une quête-dette par acte, refus = conséquence grave au journal |
| Hand. Mineur +1 PA | Attachement Exploitable | un PNJ est pris en otage ou menacé dans une quête par acte |

Le Handicap devient un **événement déclenché par le journal** (ex. « Dette de Sang : à la fin de chaque acte, ajouter la quête-dette »), ce qui remplace « le MJ active un Handicap par session ». Le catalogue complet de 40 est à réduire à 22 (12 + 10) pour la v1.

### 4.6 Origines et axes culturels dans le jeu

- Origine = **valeurs de départ** (région, +1 attribut pour 4 et 6, Honneur ±1) et **table de réactions** des PNJ de l'histoire (3 variantes de dialogue au plus par scène clé).
- Axes culturels = **8 à 10 variables de dialogue** (Combat Devoir/Nécessité/Expression change les gains d'Honneur au Récit : fuir un combat = −1 pour Devoir, 0 pour Nécessité).
- Mettre l'origine en **choix** (pas de d20) : le hasard est hostile à un récit à quatre personnages écrits.

---

## 5. Système d'arbres de compétences

### 5.1 Architecture générale

Un personnage possède **trois familles d'arbres** (une par couche d'identité) :

| Arbre | Combien | Contenu | Nœuds typiques |
|---|---|---|---|
| Arbre d'École | 1 par École (démo : 4 ; v1 : 7 martiales + 4 mystiques) | 5 Techniques canoniques + branches (Maîtrise du mode, Variantes, Voie du tabou) | environ 15-19 |
| Arbre de Métier | 1 par **bloc** (5 blocs, v1 : 3), un **tronc par métier** | 30 niveaux du livre (tronc) + branches de savoir-faire | environ 40 par métier |
| Arbre de Posture | 1 (4 Naturelles + Légendaires) | Techniques de la Posture, emplacements de Résonance, ultimes | 4 + 5 + emplacements |

Un nœud est de l'un des types : `technique` (canonique, issue d'un livre), `variante` (modifie une Technique, mutuellement exclusive par paire), `passif`, `capacite` (niveau de métier), `signature` (palier 5/10/15/20/25/30), `sommet` (capstone), `porte` (condition narrative sans effet).

### 5.2 Trois sources de déblocage, une seule monnaie

| Source | Déblocage | Coût |
|---|---|---|
| **Rang d'École** (I à V) | les Techniques canoniques s'obtiennent **gratuitement** au rang, jamais achetées (fidélité au livre : « 1 par rang ») | 0 PS, mais **jalon d'École** requis |
| **Niveau de Métier** (1 à 30) | les capacités du tronc s'obtiennent automatiquement au niveau ; les paliers (5/10/...) exigent un jalon | 0 PS |
| **Points de Savoir (PS)** | branches latérales : variantes, passifs, sommets | 1 à 3 PS par nœud |

**Gain de PS** : +1 par niveau de Métier principal (de 2 à 30 : 29 PS), +1 par **deux** niveaux du secondaire (14 PS), +2 par jalon (Rang d'École, Posture, Honneur ; environ 12 jalons = 24 PS). Total d'une campagne complète : environ **67 PS**, contre environ 11 PS (École, exemple A) + 14 PS (École mystique, exemple B) + 12 PS (Métier de chasse, exemple C) à tout acheter dans une branche : un joueur ne remplit jamais tout, il choisit.

### 5.3 Prérequis et verrous

- `requiert` : liste de nœuds (ET). Au plus **2** prérequis par nœud (lisibilité sur 360 px).
- `requiert_au_moins_un` : OU (utilisé pour les variantes d'un même rang).
- `porte` : `{type: "rang_ecole"|"niveau_metier"|"jalon"|"honneur"|"posture"|"metier_secondaire"|"objet", valeur}`.
- `exclusif_avec` : un seul de la paire (variantes). Déverrouillable au Bastion (§5.5).
- Les **interdits doctrinaux** sont des `interdits_effets` de l'École (liste d'étiquettes) : un nœud de l'arbre ne peut pas porter un effet dont l'étiquette y figure. Exemple Marées Liées : `["degats_directs","assechement"]` ; Cendres Vives : `["soin_direct"]`. Un script de validation (comme `outils/valider_monstres.py`) rejette un nœud en infraction. C'est l'implémentation la moins chère d'un interdit.

### 5.4 Le tabou comme règle de jeu (Livre VI : « un tabou par École »)

Chaque École porte un **tabou** avec un détecteur, un compteur et une sanction, tous mesurables :

| Champ | Valeur générique |
|---|---|
| `detecteur` | règle de jeu (ex. `annule_charge_longue_x3`) |
| compteur | `violations_chasse` (remis à 0 à chaque chasse) |
| sanction souple | **Dissonance** : le mode de Mana de l'École est coupé 20 s ; icône claire |
| sanction forte | à 3 violations dans une chasse : Trace « Hésitation » au journal, Honneur −1 au Retour au Clan |
| récompense | **épreuve du rang V** : réussir une chasse de l'École sans aucune violation débloque le sommet de l'arbre |

### 5.5 Respec

| Quoi | Règle |
|---|---|
| Techniques canoniques, portes, rangs, niveaux | **non remboursables** (c'est de l'histoire, pas un choix de build) |
| Variantes, passifs, sommets (PS) | remboursés à 100 % au Bastion (ou à un Camp avec Veillée), coût en Écus = 10 x PS remboursés, **gratuit la première fois par rang d'École** |
| Paires exclusives de variantes | échange libre au Camp avant une chasse (c'est un équipement de build) |
| Changer d'École | **une fois par campagne**, par une quête de rupture doctrinale ; rang ramené à I, Honneur −2, ancienne Posture non touchée ; interdit en démo |
| Changer de Posture | jalon narratif uniquement ; crée une Résonance (§3.5) |

### 5.6 Limites tactiles (360 px de haut)

- Une barre d'action de **7 touches maximum** en chasse : Attaque, Esquive, 3 emplacements de Techniques (École ou Posture, au choix), Objet, Ordre au familier.
- Le joueur équipe **3 Techniques** (4 au rang IV) parmi toutes celles qu'il possède ; l'équipement se fait au Camp et au prologue de chasse, pas pendant l'action.
- Cibles tactiles **44 x 44 px minimum** (environ 9 mm sur un téléphone de 7 cm de haut).
- Écran d'arbre : défilement vertical, **5 colonnes** (les 5 rangs) x **3 lignes** (branches) ; pas de pincement ni de glisser précis.
- Achat d'un nœud : **appui long de 0,6 s** pour confirmer (pas de double tape accidentel) ; détail du nœud en bas, jamais en fenêtre flottante.
- Une information, une couleur : disponible (couleur pleine), verrouillé par porte (cadenas + condition), verrouillé par PS manquants (grisé + coût), exclu (rayé).
- Aucun nœud ne demande de lire plus de **12 mots** en jeu : le texte long vit dans le Codex.

### 5.7 Sélecteur de Techniques en chasse

L1, L2, L3 : trois boutons ronds de 56 px dans la zone pouce droit, au-dessus d'Attaque ; **appui bref** = utilisation, **appui maintenu** = version « chargée » si la Technique en a une (Charge Profonde). Chaque bouton montre : icône, coût (point bleu = Mana, point jaune = Endurance), anneau de recharge. Si Mana insuffisant : bouton orange avec « à crédit ».

### 5.8 Schéma de données CharForge (JSON)

Un fichier par arbre, versionné. Clés en français, `snake_case`, comme les fiches `donnees/monstres/*.json`.

```json
{
  "version": 1,
  "id_arbre": "ecole_coup_final",
  "type": "ecole",
  "titre": "Coup Final",
  "source": {"livre": 6, "chapitre": 8, "ecole": 1},
  "mode_mana": "ancrage",
  "arme": "grande_lame",
  "interdits_effets": [],
  "tabou": {
    "texte": "Frapper sans intention de conclure",
    "detecteur": "annule_charge_x3",
    "sanction_souple": "dissonance_20s",
    "sanction_forte": {"trace": "hesitation", "honneur": -1, "seuil_violations": 3}
  },
  "noeuds": [
    {
      "id": "cf_t1",
      "type": "technique",
      "titre": "Posture Lourde",
      "branche": "tronc",
      "rang": 1,
      "requiert": [],
      "porte": {"type": "rang_ecole", "valeur": 1},
      "cout_ps": 0,
      "cout_ressource": {"mana": 2},
      "recharge_s": 6,
      "effets": [
        {"op": "avantage_prochain", "duree_s": 4},
        {"op": "immobilise_soi", "duree_s": 4}
      ],
      "tactile": {"geste": "appui_bref", "maintenu": null},
      "pos": {"col": 1, "ligne": 2},
      "source": {"livre": 6, "ch": 8, "ecole": 1, "rang": 1}
    }
  ]
}
```

Champs obligatoires d'un nœud : `id`, `type`, `titre`, `requiert`, `cout_ps`, `effets`, `pos`, `source`. Le champ `source` garantit la **traçabilité vers le livre** (les inventions de conception portent `"source": {"ajout": true}`). Opérations d'effet admises (liste fermée, validée par script) : `avantage_prochain`, `desavantage`, `degats_mult`, `immobilise_soi`, `ignore_armure`, `etat_applique` (Exposé, Déséquilibré, Épuisé, Concentré, En Transe, Hors de portée), `zone`, `ouverture`, `rejeu`, `brise_partie`, `gain_mana`, `cout_mana_delta`, `stat_passive`, `soin_endurance`, `invoque`. Une `zone` porte `{rayon_px, duree_s, effet}`.

État de progression d'un personnage (stocké dans PocketBase, `progression_perso`) :

```json
{
  "perso_id": "p1",
  "points_savoir": {"gagnes": 14, "depenses": 9},
  "ecole": {"id": "coup_final", "rang": 3, "noeuds": ["cf_t1","cf_t2","cf_t3","cf_p1","cf_v2a"]},
  "posture": {"id": "felin", "noeuds": ["pf_t1","pf_t2"], "resonances": []},
  "metiers": [
    {"id": "chasseur_pisteur", "xp": 380, "niveau": 11, "palier_valide": 10, "variante": "forestier", "noeuds": ["cp_l1","cp_l2","cp_s5"]},
    {"id": "trappeur_elementaire", "xp": 95, "niveau": 6, "palier_valide": 5, "noeuds": []}
  ],
  "equipement_techniques": ["cf_t2", "cf_t4", "pf_t1"],
  "respec": {"gratuits_restants": 1, "dernier": "2028-03-16T10:00:00"},
  "modifie_le": "2028-03-16T10:00:00"
}
```

### 5.9 Exemple A : École martiale **Coup Final** (Livre VI ch. 8 École 1), chiffré

Grande Lame, d10, mode **Ancrage**, tabou « Frapper sans intention de conclure ». Mana max : 6, 8, 10, 12, 15 aux rangs I à V.

**Tronc canonique (gratuit au rang, jalon d'École requis)** :

| Id | Rang | Technique (livre) | Coût Mana | Traduction jeu (à tester) |
|---|---|---|---|---|
| cf_t1 | I | Posture Lourde : prochain jet d'attaque Avantage, immobile | 2 | racine 4 s, la prochaine touche x1,25 (Avantage) |
| cf_t2 | II | Charge Profonde : d12 au lieu du dé habituel, délai visible | 2 | appui maintenu 1,2 s, télégraphie visible, x1,2 |
| cf_t3 | III | Lecture du Moment : après un échec, relancer une fois | 2 | si l'attaque ne touche rien ou est parée, rejeu instantané dans 1,5 s sans coût d'Endurance |
| cf_t4 | IV | Coup Briseur : ignore armure/carapace, dégâts directs sur la Vitalité | 3 | `ignore_armure`, touche une partie : +30 % de jauge de brisure |
| cf_t5 | V | Frappe Décisive : si touché, dégâts maximaux automatiques ; si raté, Exposé | 4 | touche : dégâts = valeur maximale du dé ; raté : Exposé (+25 % reçus, 4 s) |

Mode Ancrage : +1 Mana par 4 s immobile, +2 par garde tenue 4 s, +1 par coup absorbé sans reculer. Tabou : annuler une charge de plus de 0,5 s 3 fois dans une chasse = Dissonance (Ancrage coupé 20 s) puis Trace « Hésitation ».

**Branches de choix (ajouts de conception, `ajout: true`)** :

| Id | Branche | Nom | Requiert | PS | Effet |
|---|---|---|---|---|---|
| cf_p1 | Patience | Racines | cf_t1 | 1 | Ancrage : +1 Mana par 3 s au lieu de 4 s |
| cf_p2 | Patience | Garde Lourde | cf_p1 | 1 | planté : dégâts reçus −15 % |
| cf_p3 | Patience | Mémoire du Poids | cf_p2, cf_t3 | 2 | Mana max +2 |
| cf_v2a | Charge | Charge Longue | cf_t2 | 2 | préparation 1,8 s, x1,5, exclusif avec cf_v2b |
| cf_v2b | Charge | Charge Brève | cf_t2 | 2 | préparation 0,8 s, x1,1, exclusif avec cf_v2a |
| cf_v4a | Charge | Briseur de Carapace | cf_t4 | 2 | Coup Briseur : brisure +60 % au lieu de +30 %, exclusif avec cf_v4b |
| cf_v4b | Charge | Briseur Net | cf_t4 | 2 | Coup Briseur coûte 2 Mana au lieu de 3, sans brisure, exclusif avec cf_v4a |
| cf_c1 | Conclure | Intention Pure | cf_t5 + épreuve sans violation | 3 | Frappe Décisive qui conclut une phase : +3 Mana remboursés, Honneur +1 au Retour |

**Totaux** : 5 canoniques + 8 branches = 13 nœuds ; 14 PS pour tout acheter, 12 PS sans les exclusifs doublons (un seul de cf_v2a/b et cf_v4a/b : 2 + 2 + 1 + 1 + 2 + 3 = 11 PS). Un joueur de rang V a donc dépensé environ 11 PS sur environ 67 PS.

### 5.10 Exemple B : École mystique **Marées Liées** (Livre VI ch. 9 École 1), chiffré

Eau, mode **Rituel**, interdits « destruction brutale, assèchement volontaire » : `interdits_effets: ["degats_directs","assechement"]`, donc **aucune Technique de cette École n'inflige de dégâts** : elle contrôle, protège, ouvre des passages. C'est la raison pour laquelle elle sert aussi dans les **quêtes de plateforme** (ponts d'eau).

**Mana** : 6, 8, 10, 12, 15 (+25 % de réservoir en compensation : 8, 10, 12, 15, 19). **Rituel** : remplissage complet en 6 s immobile à une **Halte** ; +1 Mana par plein de gourde à un point d'eau (3/4 et plateforme) ; aucun gain en combat.

| Id | Rang | Technique (livre) | Coût | Traduction jeu (à tester) |
|---|---|---|---|---|
| ml_t1 | I | Flux Hydrique : zone d'eau qui ralentit | 2 | zone ronde 160 px de rayon, 6 s, ennemis −30 % de vitesse |
| ml_t2 | II | Forme Liquide : barrière, pont ou projectile | 2 | roue de 3 formes : barrière (absorbe 1 coup, 6 s), pont (plateforme 128 x 16 px, 6 s), jet (pousse de 64 px, 0 dégât, interrompt une canalisation) |
| ml_t3 | III | Courant Persistant : zone 3 rounds | 2 | zone 12 s, −30 % vitesse, courant qui pousse le long d'un sens choisi |
| ml_t4 | IV | Marée Tournante : alliés libres, ennemis entravés | 3 | zone 224 px, 8 s : alliés insensibles au ralentissement et +15 % vitesse, ennemis −50 % |
| ml_t5 | V | Appel de l'Abîme Calme : une créature engloutie, immobilisée 2 rounds, indemne | 5 | cible immobilisée 8 s (≤ ◆◆◆), 3 s sur une créature à phases (Grand Monstre, une fois par phase) |

**Branches (ajouts)** :

| Id | Branche | Nom | Requiert | PS | Effet |
|---|---|---|---|---|---|
| ml_m1 | Courants | Zone élargie | ml_t1 | 1 | rayon +25 % |
| ml_m2 | Courants | Lit durable | ml_t1 | 1 | durée +2 s |
| ml_m3 | Courants | Eau claire | ml_t3, ml_m1 | 2 | la zone retire 1 état négatif (poison, brûlure) aux alliés/s |
| ml_f1 | Formes | Barrière épaisse | ml_t2 | 1 | barrière absorbe 2 coups |
| ml_f2 | Formes | Pont long | ml_t2 | 1 | pont 192 px |
| ml_f3 | Formes | Jet d'étourdissement | ml_t2, ml_t3 | 2 | le jet applique Déséquilibré 1,5 s |
| ml_r1 | Rituel | Gourde de Marée | ml_t1 | 1 | un plein de gourde à toute surface d'eau : +1 Mana (5 s) |
| ml_r2 | Rituel | Halte accélérée | ml_t3 | 2 | remplissage à la Halte en 4 s au lieu de 6 |
| ml_c1 | Sommet | Mémoire du Fleuve | ml_t5 | 3 | Abîme Calme sur 2 cibles |

**Totaux** : 5 canoniques + 9 branches = 14 nœuds ; 14 PS pour tout acheter. Tabou : l'interdit est atteint **par conception** (aucun effet de dégât ne peut être ajouté) : coût d'implémentation nul, et c'est le bon modèle pour les 8 Écoles Mystiques.

### 5.11 Exemple C : Métier de chasse **Chasseur-Pisteur** (Livre VII bloc 2), chiffré

**Tronc : niveaux 1 à 10 (capacités du livre, effets de jeu proposés, XP de jeu cumulée, voir §6.1)** :

| Niv. | XP cumulée jeu | DD (livre) | Capacité du livre | Effet de jeu (à tester) |
|---|---|---|---|---|
| 1 | 0 | 8 | Pistage simple (sol meuble) | traces fraîches visibles en vue 3/4 dans un rayon de 160 px sur sol meuble ou boue |
| 2 | 10 | 10 | Repérage fiable (soleil, mousse) | flèche d'orientation vers l'indice le plus proche à moins de 480 px |
| 3 | 20 | 11 | Estimation taille/vitesse (foulée) | lire une empreinte révèle la taille (symbole ◆) et la vitesse de la créature au Codex |
| 4 | 40 | 12 | Discrétion accrue (camouflage terrain) | dans la végétation, rayon de détection des créatures −25 % |
| **5** | **70** | 13 | **Piste Maîtrisée** (signature) | **jalon requis** ; chaque lecture d'indice réussie rapporte 1 Jeton avec une marge de tolérance +10 % (le livre : « analyse comportementale +10 % ») |
| 6 | 95 | 11 | Pistage indirect (lecture olfactive) | indicateur de vent : détecte une créature sous le vent à 320 px |
| 7 | 130 | 14 | Coupure de trajectoire | affiche sur la carte 3/4 le couloir de fuite probable ; piège posé dessus +25 % d'efficacité |
| 8 | 180 | 15 | Poursuite longue | quand la créature fuit, la poursuite dure +50 % avant « perdue » |
| 9 | 245 | 15 | Réduction d'embuscades | probabilité d'embuscade en 3/4 −30 % |
| **10** | **320** | 16 | **Traque Signature** (signature) | **jalon requis** ; choix d'**un** type d'information pour 1 Jeton par chasse (action standard, action spéciale, déclencheur de phase, faiblesse) |

Tranche 11-15 (DD 17 à 20) : Créatures rares, lecture multi-indices, traque silencieuse, terrain extrême, **15 : Traque d'Élite**. 16-20 (DD 20 à 22) : perception éthérique, lecture émotionnelle, **20 : Chef-d'Œuvre de Traque**. 21-25 et 26-30 : voir le diagnostic §2 (gabarit) : prévoir des effets **originaux** à écrire seulement pour les paliers 15, 20, 25, 30 (4 signatures) et laisser les 12 autres niveaux comme gains de tolérance et de statut.

**Branches de savoir-faire (ajouts, `ajout: true`)**, achetées avec des PS :

| Id | Branche | Nom | Requiert | PS | Effet |
|---|---|---|---|---|---|
| cp_var | Variante | Forestier (pièges naturels, discrétion) | niv. 5 | 2 | −15 % de détection ; pièges de végétation sans consommable |
| cp_var | Variante | Désertique (traces minérales) | niv. 5 | 2 | lit les traces sur roche/sable ; |
| cp_var | Variante | Montagnard (traque verticale) | niv. 5 | 2 | traces en plateforme verticale ; Endurance +1 |
| cp_var | Variante | Marécageux (pistage olfactif et sonore) | niv. 5 | 2 | détection sonore 360° dans 160 px |
| cp_var | Variante | Nocturne | niv. 5 | 2 | vision de nuit, traces visibles dans l'obscurité |
| cp_b1 | Pistes | Lecteur patient | niv. 3 | 1 | la fenêtre de lecture d'indice s'élargit de 0,3 s |
| cp_b2 | Pistes | Œil du chasseur | cp_b1, niv. 5 | 2 | le 2e Jeton d'une chasse est gratuit |
| cp_b3 | Pistes | Contre-vent | niv. 6 | 1 | l'odeur du joueur est masquée à 60 % |
| cp_syn1 | Synergie | Points faibles anatomiques | métier secondaire = Dépeceur | 1 | une partie faible de la créature est marquée après le Jeton « faiblesse » |
| cp_syn2 | Synergie | Chasse combinée | métier secondaire = Trappeur Élémentaire | 1 | un piège est déjà amorcé au début de la chasse (1 piège gratuit) |

Les variantes culturelles sont **exclusives entre elles** (une par personnage, choisie au niveau 5). Total : 20 nœuds de tronc (niv. 1-10) + 10 de branche = 30 nœuds pour la démo ; 12 PS pour tout acheter hors variantes alternatives.

**Dépeceur (même structure, niveaux 1 à 10, capacités du livre)** : 1 Cuir brut ; 2 Viande exploitable ; 3 Trophées simples ; 4 Griffes, dents ; **5 Peau Maîtrisée** (analyse anatomique +10 %) ; 6 Cuirs résistants ; 7 Catalyseurs (venins) ; 8 Plaques organiques ; 9 Matériaux durables (conservation +15 %) ; **10 Extraction Signature**. Dans le jeu, c'est un **mini-jeu de dépeçage** (lignes de coupe à tracer au doigt sur la silhouette de la créature, tolérance selon marge, voir §3.6) : chaque capacité ouvre un matériau ou une qualité (Standard, Supérieure, Rare). C'est la meilleure interface tactile du Métier : tracer = intuitif.

### 5.12 Exemple D (court) : arbre de Posture **Ours**

| Id | Nœud | Source | Porte | PS |
|---|---|---|---|---|
| po_t1 | Provocation | Livre VI ch. 4 | création | 0 |
| po_t2 | Ancrage | idem | création | 0 |
| po_t3 | Interposition | idem | jalon de Posture 1 (premier sacrifice public) | 0 |
| po_t4 | Mur de Chair | idem | jalon de Posture 2 | 0 |
| po_p1 | Tenir la ligne (−1 case de dégâts quand planté) | ajout | po_t2 | 1 |
| po_p2 | Écho de la Meute (Provocation donne une Ouverture à 2 alliés) | ajout | po_t1 + po_p1 | 2 |
| po_l | Porte Légendaire : Tortue Noire / Dragon Azur | Livre VI ch. 5 | Honneur ≥ 7 + jalon majeur | porte |
| po_u | emplacement de Résonance (après un changement de Posture) | Livre VI ch. 7 | jalon de Posture | porte |

Les 4 Techniques naturelles sont **toutes accordées** dans la démo (il n'y en a que quatre) ; en v1 les 2 premières à la création, les 2 suivantes par jalon de Posture, pour éviter qu un jeu court n'expose tout.

---

## 6. Courbe de progression

### 6.1 XP par Métier (niveaux 1 à 30, plafond 30)

XP de livre (Livre IX ch. 5, identique aux 30 métiers) x **0,1** pour le jeu. Les niveaux intermédiaires suivent une courbe croissante par tranche (à tester) :

| Niveau | XP jeu | Niveau | XP jeu | Niveau | XP jeu |
|---|---|---|---|---|---|
| 1 | 0 | 11 | 380 | 21 | 2 210 |
| 2 | 10 | 12 | 470 | 22 | 2 495 |
| 3 | 20 | 13 | 590 | 23 | 2 875 |
| 4 | 40 | 14 | 740 | 24 | 3 350 |
| **5** | **70** | **15** | **920** | **25** | **3 920** |
| 6 | 95 | 16 | 1 030 | 26 | 4 250 |
| 7 | 130 | 17 | 1 195 | 27 | 4 740 |
| 8 | 180 | 18 | 1 415 | 28 | 5 395 |
| 9 | 245 | 19 | 1 690 | 29 | 6 215 |
| **10** | **320** | **20** | **2 020** | **30** | **7 200** |

Étoiles du Livre I : ★ = niveaux 1-10, ★★ = 11-20, ★★★ = 21-30 (affichage ; pas de règle propre). **Plafond : niveau 30**. Le Métier secondaire gagne **50 %** de l'XP (« progresse plus lentement », Livre VII).

**Sources d'XP (à tester)** : chaque action de jeu porte un tag de métier.

| Action | XP principal | Remarque |
|---|---|---|
| Lecture d'indice réussie (Chasseur-Pisteur) | 4 (tendue : 6) | max 3 par chasse (3 Jetons) |
| Traque complète (3 Jetons) | 12 | |
| Chasse terminée | 10 + 6 x CR (CR de la créature), x1,25 qualité Supérieure, x1,5 Rare/Élémentaire | ◆ CR 1 : 16 ; CR 4 : 34 ; CR 10 : 70 ; CR 16 : 106 |
| Dépeçage réussi (Dépeceur) | 6 + 3 x CR, x qualité | |
| Cueillette de quête (Herboriste) | 3 par plante rare, 15 par quête | |
| Jalon de Retour au Clan (Récit) | +25 % de l'XP de la chasse, tous métiers actifs | encourage le Récit |

### 6.2 Rythme visé (à tester)

Hypothèse : une activité = 25 minutes de jeu (chasse) ou 15 minutes (quête de plateforme) ; campagne complète = 60 à 80 heures.

| Palier | XP à gagner dans la tranche | CR typique | XP par chasse | Chasses environ | Niveau atteint à environ |
|---|---|---|---|---|---|
| 5 | 70 | 1-4 | 20-40 | 3 | 2 h |
| 10 | 250 | 4-6 | 40-50 | 6 | 5 h |
| 15 | 600 | 8-11 | 60-80 | 9 | 10 h |
| 20 | 1 100 | 12-15 | 90-100 | 12 | 17 h |
| 25 | 1 900 | 15-18 | 100-120 | 17 | 26 h |
| 30 | 3 280 | 18-22 | 130-150 | 24 | 40 h |

Le niveau 30 du métier principal est un **objectif de fin de jeu / après-jeu** ; le métier secondaire s'arrête vers 15-20. Le « un personnage par campagne » du brief est lu ainsi : la **Posture Suprême** (Dragon Ancien) n'est atteignable que par **un seul** des quatre personnages (Livre VI ch. 6), le niveau 30 de métier est atteignable par tous.

### 6.3 Jalons narratifs : paliers 5, 10, 15, 20, 25, 30

L'XP monte jusqu'au seuil du palier puis **s'accumule en attente** : le niveau suivant ne s'ouvre qu'après le **jalon de palier**, une quête d'épreuve. Définition mesurable d'un jalon (condition lue dans le journal PocketBase) :

```json
{"id": "jalon_cp_5", "type": "metier", "metier": "chasseur_pisteur", "palier": 5,
 "conditions": [
   {"journal": "chasse_terminee", "cr_min": 2, "jetons": 3},
   {"journal": "temoin", "role": "maitre_pisteur", "present": true}
 ],
 "recompense": {"ps": 2, "etoile": null, "trace": "piste_maitrisee"}}
```

- Le jalon est **reconnu par un PNJ** (un « témoin », comme le Livre II : « vu, jugé, accepté ») : jamais par un chiffre seul.
- Les épreuves sont des **modèles** (chasse d'épreuve avec contrainte, contrat de maître) : 6 modèles par bloc de métier, avec 1 ligne unique par personnage principal. Seuls les 4 personnages de l'histoire ont des épreuves écrites à la main ; les autres sont générées (StoryForge).
- **Jalon d'École** (nouveau, comble la lacune du Livre II) : même mécanisme, 4 par École (rang II, III, IV, V). Rang I à la création, rang II à la fin du premier acte, III à environ 35 % de l'histoire, IV à 70 %, V à 95 % ou après-jeu (cadence du Livre VI §13.6 : « 3-5 sessions » pour le rang II).
- **Jalon de Posture** : légendaire = Honneur ≥ 7 et jalon majeur ; chaque Légendaire a une « condition narrative type » (Livre VI ch. 5) qui devient une quête.
- **Jalon d'Honneur** : l'Honneur change par sauts (Livre II) : +1 / +2 / −2 par événement du Retour au Clan.

### 6.4 Rang de contrat (pas de niveau de joueur)

Pas de niveau global : chaque contrat de chasse affiche une **recommandation en rangs et étoiles**.

| Créature | Rang d'École conseillé | Étoile du métier conseillée |
|---|---|---|
| ◆ Commun (CR 1-4) | I-II | ★ (niveaux 1-5) |
| ◆◆ Rare (CR 5-9) | II-III | ★ à ★★ |
| ◆◆◆ Élite (CR 10-15) | III-IV | ★★ |
| ◆◆◆◆ Légendaire (CR 16+) | IV-V | ★★ à ★★★ |

---

## 7. Gestion des quatre personnages

### 7.1 Différences

| Dimension | Ce qui diffère | Visible à l'écran par |
|---|---|---|
| Corps | palette et silhouette (domaine sprites) | 64 px, couleurs de région |
| Origine | région, Honneur, réactions PNJ, 1 attribut | dialogues, boutiques |
| École | arme, mode de Mana, 5 Techniques | arme, barre d'action |
| Posture | rôle de groupe, 4 Techniques de Posture | 2 boutons de rôle |
| Métier | activités, matériaux, quêtes | mini-jeux, Camp |
| Familier | animal apprivoisé (domaine dressage) | compagnon à l'écran |

### 7.2 Synergies de groupe (coopération entre joueurs réels)

Les 4 Postures couvrent les 4 rôles ; les synergies utiles à chaque mode :

| Combo | Effet de jeu | Source |
|---|---|---|
| Ours Provocation + Loup Appel de Meute | l'Ours attire l'attention, le Loup donne l'Ouverture au Félin qui frappe | Livre VI Posture + Ouverture |
| Faucon Point Faible → Félin Ciblage Vital | +25 % puis ignore 2 armure sur la partie marquée | Livre VI ch. 4 |
| Marées Liées zone + Coup Final charge | la cible ralentie est plus facile à toucher avec la Charge Profonde | École x École |
| Résonances Rythme de Guerre | +1 aux jets d'attaque de tous pendant 2 rounds → +10 % de dégâts 8 s | Livre VI Résonances II |
| Dépeceur + Forgeron d'Armures | matériaux organiques utilisés par la forge (synergie du Livre VII) | Livre VII ch. 2 |

Règle de design : **aucune synergie n'est obligatoire** ; chaque personnage doit être viable seul avec un partenaire IA. Le coop apporte du plaisir et de la puissance, pas la possibilité de gagner.

### 7.3 Coopération

- 1 à 4 joueurs par chasse. Chaque joueur contrôle **son** personnage et garde ses arbres.
- Solo : un **partenaire IA** (un des trois autres personnages, choisi au lobby) avec un comportement scripté simple (utilise ses Techniques de Posture quand les conditions sont réunies). Pas trois alliés IA : lisibilité à 360 px.
- Les jalons individuels (Métier, École, Posture) se gagnent seuls ; les jalons collectifs (Bastion, jalon d'Honneur de groupe) profitent à tous (Livre II : « jalons de Bastion toujours collectifs »).
- Journal : un Acte, une Trace, une Conséquence **par chasse et par groupe**, avec la liste des `perso_id` présents.
- Variable de contenu : la chasse s'ajuste au nombre de joueurs (Vitalité de la créature x(1 + 0,6 x (n − 1)) : 1,0 / 1,6 / 2,2 / 2,8 ; dégâts inchangés ; à tester par le domaine combat).

### 7.4 Équilibrage de départ (tout à tester)

| Réglage | Valeur initiale | Raison |
|---|---|---|
| Mana max rang I à V | 6, 8, 10, 12, 15 ; +25 % pour Rituel | table du Livre VI |
| Coût Technique | 2, 2, 2, 3, 4-5 Mana (livre) | |
| Recharge de Technique de Posture | 6 s | avec Endurance 10 : 5 usages max sans régénération |
| Revenu de Mana en combat | 8 Mana/min visé ; Flux ≤ 12, Ancrage ≤ 15 à l'arrêt | normaliser les quatre modes |
| Endurance | 10 ; régénération 1 par 1,2 s ; esquive 1 | |
| Vitalité | 4 + END ; END par défaut 7 (11 cases) | |
| 42 points d'attributs | gabarit par personnage : pic à 10, plancher à 4 | évite les builds à 3 en END |
| Avantage | x1,25 ; ne se cumule pas | règle du livre |
| XP de jeu | Livre IX x 0,1 | |
| PS | 1 par niveau principal, 0,5 par niveau secondaire, 2 par jalon | environ 67 PS en campagne |
| Respec | gratuit au premier changement par rang ; ensuite 10 Écus par PS | |

Test d'équilibrage recommandé avant toute extension : un **banc de simulation** (script Godot headless) qui joue les 4 personnages contre un ◆ Commun et un ◆◆ Rare et mesure le temps de victoire par mode de Mana, avant d'ajouter la 5e École.

---

## 8. Modèle de données et PocketBase

Collections (réutilisent le journal d'événements du brief) :

| Collection | Champs principaux | Remarque |
|---|---|---|
| `personnages` | id, nom, phrase, origine_id, axes_culturels (json), attributs (json 6 valeurs), avantages (json), handicaps (json), honneur, posture_id, ecole_id, rang_ecole, metiers (json), corps/palette | export CharForge |
| `progression_perso` | perso_id, points_savoir, noeuds_debloques (json), equipement_techniques, respec (json), modifie_le | schéma §5.8 |
| `arbres` | fichiers JSON statiques versionnés (`donnees/arbres/*.json`) | pas dans PocketBase : dans le dépôt, comme `donnees/monstres/` |
| `jalons` | id, type, perso_id, palier, conditions_json, valide_le, temoin_pnj | conditions lues dans le journal |
| `evenements` (existant) | acte, trace, consequence, perso_ids, chasse_id, qualite, jetons_utilises | Trinité du Livre II |

`donnees/arbres/` doit contenir : `ecole_*.json`, `metier_bloc2_chasse.json`, `posture_naturelle.json`, `posture_legendaire.json`, plus un `valider_arbres.py` (même esprit que `outils/valider_monstres.py` : ids uniques, prérequis acycliques, `interdits_effets` respectés, ≤ 2 prérequis, coûts entiers).

---

## 9. Écrans et états de la progression

| # | Écran | Contenu | Accès |
|---|---|---|---|
| P1 | Fiche du personnage | portrait, jauges, attributs, École/Posture/Métiers, étoiles, Honneur par états | Camp, menu |
| P2 | Arbre (3 onglets : École, Posture, Métier) | nœuds par colonne de rang, PS disponibles, bouton « Respec » | Camp seulement (pas en chasse) |
| P3 | Détail d'un nœud | texte ≤ 12 mots, coût, conditions, aperçu animé 3 s | appui sur un nœud |
| P4 | Équipement des Techniques | 3-4 emplacements, glisser depuis la liste | Camp, préparation de chasse |
| P5 | Journal des jalons | jalons accomplis, épreuves disponibles, témoins | menu |
| P6 | Épreuve de palier | quête proposée par un PNJ témoin | carte 3/4 |
| P7 | Résumé de fin de chasse | XP par métier, jetons, jalons débloqués, PS gagnés | après chasse |
| P8 | Lobby coop | 4 places, personnage et Posture de chacun, avertissement doublons | menu |

États d'un nœud : `masque` (condition non vue, pour éviter le spoil), `verrouille_porte`, `verrouille_ps`, `disponible`, `achete`, `exclu`, `equipe`. Transitions : `disponible` → `achete` (appui long, PS déduits) ; `achete` → `disponible` (respec) ; `disponible` → `exclu` (choix de la variante opposée).

---

## 10. Portée démo (16 mars 2028) et feuille de route

### 10.1 Sous-ensemble minimal pour la démo (1 zone, 1 chasse, 2-3 quêtes)

| Élément | Démo | Pourquoi |
|---|---|---|
| Personnages | 4 jouables, parcours Histoire, prologue commun de 15 min | l'histoire est à quatre |
| Écoles | **4** : Coup Final, Mur Vivant, Résonances, Marées Liées ; **rangs I à III** | 12 Techniques ; 3 modes de Mana sur 4 (Flux et Sacrifice hors démo) |
| Postures | 4 naturelles, 2 Techniques chacune accordées d'emblée (8 Techniques) | rôles de coop |
| Métiers | **3** : Chasseur-Pisteur, Dépeceur, Herboriste ; niveaux 1 à 10 ; 1 jalon de palier (5) | boucle Désignation/Traque/Affrontement/Dépeçage + cueillette en quête |
| Arbres | 4 arbres d'École (environ 40 nœuds), Posture Ours/Loup/Faucon/Félin (8 nœuds), Chasseur-Pisteur et Dépeceur niv. 1-10 (50 nœuds) | environ 100 nœuds à écrire et valider |
| Attributs | 42 points, gabarit prérempli, 6 curseurs | |
| Avantages/Handicaps | 1 Handicap imposé, 6 PA sur 8 cartes | |
| Hors démo | Compétences (valeurs fixes), respec, Résonance, Légendaires, Posture Suprême, changement d'École, Écoles Techniques/Interdites/Secrètes, 25 autres Métiers | |

Le nombre de Techniques à animer (12 + 8 = 20) reste énorme pour un artiste seul : chaque Technique a au moins une animation (4 à 8 images à 64 px). Si le budget d'images est serré (500 à 800 images cibles, `docs/livres-crs-vers-jeu-b.md`), garder **2 Techniques par École** dans la démo (rangs I-II) et reporter le rang III à la v0.2.

### 10.2 Feuille de route par versions

| Version | Contenu | Estimation |
|---|---|---|
| **v0.1** (démo 2028-03) | §10.1 ; arbre en lecture + achat ; pas de respec | |
| v0.2 | rangs III à V des 4 Écoles ; Résonance ; respec ; Compétences ; 5 axes culturels | |
| v0.3 | Flux Tranchant, Danse Rouge, Souffle Long, Fracas Juste ; Voies Hautes ; mode Flux/Sacrifice | 7 martiales + 2 mystiques |
| v0.4 | Métiers : Forgeron d'Armes, Forgeron d'Armures, Alchimiste, Trappeur, Dresseur, Médecin, Diplomate (7) ; arbre de bloc 1 et 3 | 10 métiers |
| v1.0 | Postures Légendaires (4) et Suprême (cinématique) ; 2 Techniques Secrètes ; 12 métiers ; coop en ligne | |
| v2 | Écoles Techniques fondues en Bastion ; Écoles Interdites en quêtes ; mode hardcore ; Marque régionale | |

**Métiers v1.0 (12)** : Chasseur-Pisteur, Dépeceur, Trappeur Élémentaire, Dresseur de Monstres, Forgeron d'Armes, Forgeron d'Armures, Alchimiste, Herboriste, Médecin, Cartographe, Diplomate, Marchand. Raison : chacun a une **boucle de jeu** (mini-jeu, quête ou écran) ; les 18 autres n'en ont pas.

---

## 11. Questions ouvertes (pour krunt)

1. **Quatre personnages prédéfinis ou création libre dans le jeu ?** Recommandation : prédéfinis (parcours Histoire) pour le jeu, création libre uniquement dans CharForge et pour la table. Une création libre à quatre personnages dilue l'histoire et multiplie les cas à tester.
2. **Les quatre personnages : proposition du §4.2 (Félin / Ours / Loup / Faucon) acceptée ?** À défaut, donner leur concept en deux lignes chacun : toute la répartition d'Écoles et de Métiers en découle.
3. **« Niveau 30 plafond, un seul personnage par campagne » : interprétation correcte ?** Recommandation : niveau 30 atteignable par tout le monde (après-jeu), Posture Suprême unique par campagne.
4. **Points de Savoir : une monnaie unique ou une par arbre ?** Recommandation : une seule (moins d'écrans, plus de choix).
5. **Coût en contenu des jalons.** Un jalon avec témoin PNJ par palier, par métier et par École, c'est des centaines de quêtes. Recommandation : modèles générés + 1 jalon écrit à la main par personnage et par palier de rang d'École uniquement (16 quêtes).
6. **Niveaux de métier 16 à 30 : les écrire ou les laisser « vides » ?** Recommandation : écrire seulement les 4 signatures 15/20/25/30 et accepter le reste comme gain de tolérance, tant que le jeu n'a pas atteint ces niveaux.
7. **Bloc 5 « Magie » : supprimer ?** Recommandation : oui, il double les Écoles Mystiques.
8. **Écoles Techniques : fusionner dans les métiers et le Bastion ?** Recommandation : oui.
9. **Honnêteté sur l'ampleur.** 29 Écoles et 30 Métiers ne tiennent pas dans un jeu solo/coop tactile développé seul en 18 mois : **plafond réaliste v1.0 = 11 Écoles et 12 Métiers**. Valider ce plafond maintenant évite d'écrire des tables que le jeu n'ouvrira jamais.
10. **Coop en ligne ou local ?** Le brief parle de 4 joueurs réels : si c'est du réseau, le coût d'infrastructure dépasse largement celui des arbres. Recommandation : v0.1 en solo + partenaire IA, coop locale ou asynchrone (journal partagé) avant tout réseau temps réel.
11. **Tabou : sanction « Dissonance » acceptable ?** Recommandation : oui, car elle rend le tabou visible sans punir fort ; l'Honneur −1 n'arrive qu'au Retour au Clan.
12. **Mana de départ : table du Livre VI (6 à 8) ou règle du Livre I (2 x rang) ?** Recommandation : table du Livre VI, déjà retenue ici ; corriger le Livre I.
13. **Compétences (21) : conserver ?** Recommandation : réduire à 8, valeurs fixes dans la démo, répartition libre en v0.2.
14. **Résonance** : les « conditions narratives » doivent être remplacées par 3 contextes détectables par Technique. Valider ce principe avant de l'écrire.
15. **Ouverture en solo** : le partenaire IA reçoit-il l'Ouverture, ou l'Ouverture est-elle supprimée en solo (remplacée par un bonus personnel) ? Recommandation : bonus personnel (réduction de recharge de 3 s) en solo.

---

## 12. Ponts avec les autres domaines

- **Combat (Livre III, dégâts, états, phases)** : attend les valeurs de base de l'arme, la table des états (Exposé, Déséquilibré, Épuisé, En Transe), la longueur du « round » (4 s) et la règle de dégâts (modèle Livre I) ; ce chapitre n'exprime les dégâts qu'en multiplicateurs.
- **Arènes et chasses** : attend l'emplacement des **Haltes** (Rituel), les points d'eau (Marées Liées), les murs et structures (Fracas, Fracas Juste), et les parties de créature ciblables (brisure).
- **Dressage et familiers (106)** : attend le format des ordres de familier et les compétences de l'École Dressage/du métier Dresseur ; les nœuds `cp_syn*` et Dresseur supposent ce format.
- **Forge, Bastion, alchimie** : attend la liste des matériaux par qualité (Standard/Supérieure/Rare/Élémentaire) pour le dépeçage, et le modèle de Forge individuelle 0-40 ; Forgeron d'Armes/Armures liés aux niveaux de la table des armes (Livre IX §2).
- **Social, Honneur, clan** : attend les 5 états d'Honneur et les événements du Retour au Clan pour les jalons ; les axes culturels y sont des variables de dialogue.
- **Journal PocketBase / StoryForge** : attend les types d'événements `jalon_*`, `chasse_terminee`, `temoin`, et le format de condition des jalons (§6.3).
- **Interface et ergonomie tactile** : attend la grille de boutons (7 maximum), les cibles de 44 px et la bibliothèque d'icônes des états.
- **Outils (CharForge)** : attend le schéma JSON du §5.8 (champs, `version`, `modifie_le`) et le script de validation `valider_arbres.py`.
