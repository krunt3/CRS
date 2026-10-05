# Mécaniques du Jeu B, chapitre 05 : clan, monde, voyage, économie et familiers

Domaine : la couche de jeu **entre les chasses** (gestion du clan, carte-monde, voyage, économie) et la **relation aux familiers** (dressage, lien, élevage, montures). Les mécaniques de combat, de chasse latérale, de progression d'arbres et de Bastion détaillé sont traitées par d'autres chapitres ; celui-ci n'y touche que par ses interfaces.

Sources lues : Livre I (ch. 2, 4, 6, 8, 9, 10), Livre II (ch. 3, 4, 5, 8, 9), Livre III (fiches types, section « Dressage »), Livre IV (Atlas entier), Livre V (ch. 2, 3, guildes), Livre VI (École T6), Livre VII (Éleveur, Dresseur, Maître des Montures), Livre VIII (ch. 7, 9), Livre IX (tables d12, régions, armes), Livre X (ch. 11, 12), plus `donnees/monstres/*.json` et `docs/roster-monstres.md`.

Conflits résolus par les options canoniques provisoires (une ligne chacun) :
- Honneur : conflit résolu par l'option 4 (échelle 0 à 10, cinq seuils). L'« Honneur de Clan » (−25/+25) du Livre VIII devient ici une **Faveur de clan** de 0 à 10 par clan, jamais montrée en chiffres.
- Éléments : conflit résolu par l'option 10 (Feu, Eau, Terre, Vent, Foudre, Glace, Ombre, Éther) ; le Wu Xing (Bois, Métal) n'est pas utilisé ici.
- Rangs des créatures : conflit résolu par l'option 6 (◆ CR 1 à 4, ◆◆ 5 à 9, ◆◆◆ 10 à 15, ◆◆◆◆ 16+). Les CR du roster sont ceux de `donnees/monstres`.
- Forge : conflit résolu par l'option 5 (Forge individuelle 0 à 40). Le « sablier » de Forge de Livre II est donc lu à l'échelle du héros.
- Réussite tendue : option 8 (DD à DD+4) ; les jets de voyage et de dressage du livre deviennent des seuils, voir 2.

---

## 1. Ce que disent les livres

### 1.1 Architecture clanique (Livre V, ch. 2)

Un **clan** se définit par sa valeur fondamentale, ce qu'on est prêt à défendre (une guilde par le métier, un ordre par la croyance). Un personnage peut appartenir à un clan, une guilde et un ordre à la fois, avec des obligations parfois contradictoires.

| Sujet | Règle du livre |
|---|---|
| Entrée | Naissance, adoption, serment, reconnaissance. Critères propres : Sceau Pourpre exige une démonstration de capacité juridique ; Lames Franches un choix libre significatif ; Cendres Liées d'avoir survécu à une perte comparable. |
| Sortie | Exclusion possible partout (exil rituel temporaire ou exclusion publique permanente), conséquences variables. |
| Sans clan | Possible mais coûteux ; norme sans stigmate aux Confluences et aux Marches Frontalières. |
| Obligations universelles | Défendre un membre en danger direct ; ne pas agir contre les intérêts fondamentaux du clan ; transmettre les valeurs aux plus jeunes. |
| Tensions | Conflit d'obligations entre deux clans ; valeur du clan contre valeur personnelle ; évolution de l'affiliation. |
| Affiliation régionale | Tableau §5 : un clan dominant par région (Sceau Pourpre au Cœur Impérial, Pierres Hautes aux Hautes Terres, Marée Profonde aux Royaumes Marins, etc.) ; 7 régions n'ont aucun clan dominant. |

**Les 14 clans** (Livre V, ch. 3, la quatrième de couverture dit 12, le sommaire 14, le texte 14 : conflit résolu en gardant 14). Chaque fiche contient nature, origines, organisation, philosophie, alliances, conflits canoniques, 3 hooks de quête, « avantages mécaniques », archétypes. Avantages mécaniques, résumés :

| Clan | Avantage mécanique du PJ affilié (Livre V) |
|---|---|
| Sceau Pourpre | Statut légal reconnu, archives juridiques, autorité en négociation officielle, Exécuteurs Mandatés |
| Lames Franches | Bonus en duel et escarmouche, réseau de mercenaires et d'armes rares, liberté contractuelle |
| Marée Profonde | Navigation avancée et occulte, rituels marins, réseau portuaire, protection des entités abyssales (zones de pacte) |
| Ciel Brisé | Technologies célestes, bonus Éther/gravité/déplacement, accès aux ruines aériennes (Récupérateurs) |
| Veilleurs Sylvestres | Bonus nature, survie et magie tellurique, sanctuaires, chemins cachés des Marche-Feuilles |
| Maisons Anciennes | Réseaux nobles, droits héréditaires, soutien discret, Archives Scellées selon le rang |
| Cendres Liées | Résistance feu, Corruption, fatigue extrême ; refuges clandestins ; rituels de survie collective |
| Mille Voix | Réseaux d'information, bonus sociaux, influence à grande échelle |
| Pierres Hautes | Résistance physique et mentale, refuges fortifiés, ingénierie militaire |
| Navigateurs Gris | Bonus exploration/survie, routes alternatives rares, moindres pénalités de terrain extrême |
| Porte-Flammes | Résistance feu et peur, rituels de purification, bonus en combat idéologique |
| Porteurs de Cicatrices | Archives de comportement de créatures (bonus de préparation avant chasse), bonus de Forge sur matériaux de créatures déjà affrontées, Soigneurs des Cicatrices |
| Veines d'Éther | Lecture des flux, cartographie des Écouteurs, bonus d'identification magique |
| Masques Brisés | Méthodes d'enquête, consultation des Archivistes des Impossibles, Protecteurs de Vérité |

Guildes (Livre V, ch. 4) utiles ici : **Guilde de Chasse** (Conseil des Primes = tarification des contrats ; Contremaîtres Régionaux ; **Certificateurs** = qualité des pièces ; Formateurs ; Archivistes de Chasse), Marchands Libres (crédit, Banquiers de Dette), Navigateurs (cartes certifiées, brevets), Ports Unifiés, Soigneurs.

### 1.2 Les Porteurs de Cicatrices et la Consignation (Livre V, clan 12)

Le clan des chasseurs légendaires, « méthodologique » : la cicatrice est une information. Hiérarchie : **Apprentis Marqués** (déjà une cicatrice significative de créature rang II+), **Cicatrisés de Rang** (survie documentée d'une créature rang III+, droit de vote doctrinal), **Cercle des Sept** (conseil directeur, toujours sept), **Archivistes de Combat** (documentent sur le terrain), **Forgerons des Cicatrices** (forgent seulement avec des créatures que le groupe a lui-même affrontées). **Rituel central : la Consignation**, après chaque chasse significative : créature, comportements observés, ce qui a marché, ce qui a échoué, cicatrices obtenues. Non optionnelle : qui refuse perd progressivement l'accès aux archives des autres (« isolement informationnel »). Conflits canoniques : l'Archiviste Disparu, le Débat de la Forge Empoisonnée, la Confrontation de Velhor (une créature rang IV non répertoriée a fermé les caravanes pendant 3 mois).

### 1.3 Retour au Clan et Trinité (Livre I, ch. 4 §6-7)

Le Retour est « aussi important que l'Affrontement » : **Récolte** (qualité Standard, Supérieure, Élémentaire, Rare selon *comment* la créature est vaincue ; fuite = rien et Tension +2), **Récit** (scène jouée devant le clan, « principal moment de mouvement de l'Honneur » : on valorise cohésion, protection des vulnérables, exploitation d'une faiblesse, parties rares préservées, rapidité ou patience), **Rituel** (offrande, serment, forge cérémonielle, veillée). **Trinité** : toute chasse significative produit un **Acte**, une **Trace** et une **Conséquence**, simultanément ; elle fonctionne même dans l'échec.

### 1.4 Bastion, Ancrage, Phase (Livre I ch. 6 ; Livre II ch. 5)

Ancrage 0 à 20 : Camp provisoire 0-3, Avant-poste 4-7, Bastion établi 8-12, reconnu 13-17, légendaire 18-20. Monte par : chasse réussie dans la région +1, bâtiment +1, PNJ notable +1, cérémonie de clan +1 à +2, défense réussie +2, conflit politique résolu +2 ; baisse : attaque non repoussée −5, abandon plus d'un arc −3. Plafond de bâtiments 0/3/6/10/18 (18 bâtiments existent). 8 PNJ avec contrainte narrative (Forgeron et Guérisseur à Ancrage 4, Bibliothécaire et Herboriste à 8, Ambassadeur de Clan et Maître d'École à 13, Artisan d'Éther à 18). **Phase de Bastion** en 5 temps (Rapport de chasse, Dépenses de Forge, Activités individuelles, Événement d20, Projection) ; 10 activités (Forger, S'entraîner, Rechercher, Cultiver, Négocier, Patrouiller, Tenir conseil, Pratiquer rituel, Documenter, Se reposer). Conflit : trois échelles d'Ancrage incompatibles entre Livres I, II/IX/X et l'Atlas (« rang I à III ») ; ce chapitre utilise Livre I.

### 1.5 Campagne et jalons (Livre II, ch. 3, 8, 9)

- 5 jalons (Métier, Compétence, Posture, Bastion, Honneur) ; collectifs (Bastion toujours) ou individuels ; cadence indicative : 2 à 4 jalons individuels et 1 collectif par arc de 3 à 5 sessions.
- Campagne en 3 arcs : **Établissement** (4 à 8 sessions), **Confrontation** (6 à 10, Tension à son maximum au moins une fois), **Résolution**. Campagne de Chasse : arc 1 = 3 à 5 créatures ◆ à ◆◆ (Forge palier 1 vers 2), arc 2 = 2 à 3 créatures ◆◆ à ◆◆◆ (palier 2 vers 3), arc 3 = 1 à 2 ◆◆◆ puis la créature légendaire (palier 3 vers Légendaire). La créature légendaire agit sur le monde dès l'arc 1 (rumeurs, zones désertées).
- « Les éclats achètent des choses, ils ne progressent pas des personnages » (Livre II ch. 9 §6).

### 1.6 Jauges sociales (Livre I ch. 2 ; Livre VIII ch. 7, 9)

Honneur 0 à 10 : Paria 0-1, Suspect 2-3, Reconnu 4-6 (départ de tous), Estimé 7-8, Légendaire 9-10 ; les chiffres ne sont jamais montrés au joueur, il lit les réactions. **Tension** : jauge collective 1 à 10 (calme, vigilance 3-4, pression 5-6, danger proche 7-8, rupture 9-10) ; baisse : chasse discrète −1, repos long −1, Patrouille −2 ; hausse : combat bruyant en zone habitée +2, Bastion attaqué non défendu +3. Livre VIII ajoute Réputation Publique (−25/+25) et **Infamie** 0 à 10 (≥ 5 : les guildes mettent une prime, certaines factions attaquent sans négocier) ; le Livre II élargit la Tension à 13-16, 17+ (conflit, voir 5).

### 1.7 Le monde (Livre IV, Livre II ch. 4, Livre IX ch. 1-2)

- Trois couches : **Zone Tenue**, **Marge**, **Royaumes Sauvages** (« la Marge avance et recule selon les saisons, l'activité des créatures et la solidité des bastions »).
- **20 régions** en 6 blocs/zones (Nord, Centre, Est, Ouest, Sud, Ombre). Chaque fiche : géographie, entités politiques, économie, faune, ville principale, lieux notables, **2 tensions actives**, 3 hooks = **40 tensions** et **60 hooks**. Conflit : la liste de §3 du chapitre 1 de l'Atlas cite « Terres Fracturées » (inexistante) et oublie Îles des Serments, Cités Astrales, Théocraties Sacrées ; conflit résolu par les 20 fiches (voir 2.5).
- **Trois Terres Inconnues** : l'**Archipel des Îles Brûlantes** (Île Noire « la Canopée », Île Cendrée « le Site », Île du Rivage « l'Approche », avec un phœnix juvénile), les **Îlots Dispersés** (5 îlots à 2 à 5 jours de traversée du continent : Vents Chauds, Os Blancs, Muet, Marchands Perdus, Rouge) et le **Continent Nord** (falaise de glace, cinq expéditions repoussées sans l'avoir atteint ; ne s'ouvre qu'à un groupe qui a compris le cycle des phœnix).
- Routes : Voies Tenues, Marchandes, Pistes de Chasse, Voies Secrètes. Trois grands axes (Route du Fer Gris 22 à 30 jours, Passage du Voile 8 à 12, Voie des Cendres 6) ; 5 passages naturels ; table des incidents de route d8 ; distances (Kûrath-Shon vers Velhan 340 km : 17 j à pied, 9 à cheval, 22 en caravane).
- Sites dangereux : Ruines Profondes, Fosses Naturelles, Sites Corrompus ; table de génération 6 colonnes d6. Postes de chasse numérotés (PX-17), avant-postes, Bastions abandonnés jouables.
- **Tables d'événements** (Livre IX ch. 1) : 20 tables régionales + 1 inter-régionale. Anomalie : elles sont titrées « d12 » mais contiennent **9 entrées** (la table des Terres Sans Nom en contient 27) ; la table inter-régionale du Livre II ch. 4 en contient 12. Conflit résolu : les tables du Livre II/IX sont utilisées telles quelles par tirage d9 (ou d12 relancé si 10-12), à compléter plus tard.

### 1.8 Voyage et survie (Livre I ch. 8 ; Livre X ch. 11-12)

- Voyage en **étapes**, 1 à 3 jets par étape, 4 rôles (navigateur Endurance + Exploration, guetteur Agilité + Perception, intendant Volonté + Survie, médecin Esprit + Médecine). Durées : courte 1 étape (terrain difficile 2), moyenne 2-3 (4-5), longue 4-6 (7-10).
- Provisions : 1 portion par étape et par personne (−1 Endurance max par étape sans nourriture) ; eau : 2 portions (−2 Endurance max sans eau, Désavantage). Désert : eau doublée. Fatigue persistante : sans repos long pendant 3 étapes, Endurance max −2 par étape supplémentaire. Repos court (10-30 min : moitié de l'Endurance), long (8 h : toute), complet (24-48 h : + 1 Vitalité).
- Campement : sommaire, défensif (+1 End max récupérée), abri construit (Vitalité doublée), Bastion (soins complets, immunité à la fatigue persistante).
- Météo : 7 conditions au Livre I ; **Livre X** : 4 saisons de 3 mois (printemps créatures territoriales, été plus agressives, automne migrations et ressources abondantes, hiver créatures rares), tables d12 météo pour 6 terrains (incohérence : titre « 6 terrains × 4 saisons » mais tables non saisonnières) ; chaleur (> 40 °C), froid (< −5 °C), déshydratation (1 L par 4 h, 1 L par 2 h en chaleur), faim ; orientation (DD 12 forêt, 14 montagne/désert, 16 Terres Ravagées, 18 Failles ; boussole −3, carte −2).
- Ruines : zones narratives, pièges (détecter, désamorcer, éviter). Récolte : 5 types de points, épuisés 1d4 jours.

### 1.9 Économie (Livre I ch. 10 ; Livre II ch. 9 ; Livre IX ; Livre V)

- Monnaie : **l'éclat**. Valeurs indicatives (Livre I ch. 10) : ◆ 1-5, ◆◆ 10-30, ◆◆◆ 50-100, ◆◆◆◆ 200-500, ◆◆◆◆◆ 1 000+. Aucun prix d'armes, d'armures ni de services n'est donné dans les livres. Conflit : ces raretés à 5 losanges ne sont pas les rangs de créatures (4 losanges, option 6).
- Ce que les éclats font : réparations, matériaux de base, accès sociaux, infrastructures du Bastion, informateurs. Ce qu'ils ne font pas : progresser, remplacer les matériaux de chasse, racheter l'Honneur ; en région stricte (Théocraties, Hautes Terres), payer pour obtenir ce que l'Honneur devrait donner coûte de l'Honneur.
- Qualités d'armes (Basique à Légendaire, niveau de forgeron 1 à 30) et usure à 3 niveaux (Intact, Endommagé, Brisé : réparation par forgeron niveau 5+) ; armures non entretenues : −1 CA après 5 combats.
- Dettes sociales (Livre I ch. 9 §VII.b) : **Faveur**, **Dette de sang**, **Pacte d'intérêts**, **Compte ouvert** ; elles « empirent avec le temps ». Exclusion : 4 niveaux (désaveu discret, mise à l'écart DD +3, exclusion formelle, exil).
- Guilde de Chasse : le Conseil des Primes valide et tarife, les Certificateurs évaluent les pièces, les Archivistes documentent. Villes par service : contrats haut niveau (Kûrath-Shon, Seren-Vol, bourgs des Marches), meilleur prix des pièces (Velhan, Port de Menûl, marchés des Confluences), forge spécialisée, discrétion (Cités Voilées).

### 1.10 Dressage et élevage (Livre III, VI, VII ; JSON)

- Fiche de créature (section VII) : Difficulté, **lien maximal** (Impensable, Partiel/Conditionné, Affectif, Symbiotique), **Intelligence** (Faible à Très élevée, présente seulement sur ~14 fiches), âge idéal, durées minimales. **Trois phases** : Approche (jet AGI + Dressage, DD variable ; la meute, le sang, le territoire modifient le DD), **Jalon narratif** (la créature *choisit* : suivre sans contrainte, défendre le dresseur), Apprentissage (DD qui baisse après N réussites, liste de comportements dressables et non dressables) ; parfois une Phase 4 (second jalon). Une section « Rupture » (par exemple régression après 10 jours sans le dresseur). Conflit : le Livre VI dit « quatre phases » (Approche, Conditionnement, Lien, Rupture) ; conflit résolu par 3 phases + Rupture comme état, comme les fiches.
- Exemple chiffré (ancien Velokrak, aujourd'hui **Alizade** cro01) : Phase 1 DD 12, Phase 3 DD 10 puis 8 après 3 réussites, lien conditionné, régression après 10 jours. Pour **Dorgane** (cro02, ancien Velodrak, CR 4) : Phase 1 DD 15 (20 en présence de la meute), Phase 3 DD 13 puis 10 après 4 réussites, deux arcs narratifs de durée. Attention : le JSON `donnees/monstres` indique `difficulte_dd: null` pour ces deux créatures alors que le Livre III donne le DD ; 28 des 106 familiers ont un DD nul.
- Métiers : **Éleveur de Créatures** (lignées stables niv. 5, Lignée Signature 10, d'Élite 15, Chef-d'Œuvre Vivant 20, Créature Légendaire Vivante 30 ; DD 8 à 32), **Dresseur de Monstres** (Lien Stable 5, Signature 10, d'Élite 15, Chef-d'Œuvre 20, Lien Runo-Vivant 25, Lien Nommé Vivant 30 ; **niv. 24 « Pacte intentionnel »** pour créature consciente, DD 25), **Maître des Montures** (Monture Stable 5 à Monture Nommée Vivante 30). École T6 Dressage & Domestication : Rang V = **Lien Légendaire** avec une créature de rang III+.
- Donnée de jeu (`donnees/monstres/*.json`, champ `familier`) : **106 familiers** avec `lien_max` (conditionné 44, affectif 28, partiel 17, symbiotique 9, élevage 8), `difficulte_dd`, `roles`, `aide_combat`, `transport`, `capacite_transport`, `age_ideal`, `limite`. Rôles : éclaireur 39, assistant de combat 33, garde 31, récolte 30, signal 28, pisteur 22, bête de somme 19, monture terrestre 15, soin 8, monture marine 3, monture aérienne 2. Transports : terrestre 21, aérien 2 (Aquilarak cha07, Wistrelle fau03), maritime 2 (Pressoir lev16, Prairelle lev22) plus Poterne lev08 (monture marine sans transport déclaré). Phœnix : « Lien de cycle » symbiotique, jamais dressable.

---

## 2. Traduction en jeu vidéo

### 2.1 Principe : trois niveaux de temps

Les livres sont écrits pour une table qui joue « une phrase par joueur » entre les chasses. Dans un jeu 2D tactile, cela devient trois niveaux de temps et d'interfaces, jamais de jets de d20 visibles :

| Niveau | Contenu | Mode d'écran | Durée réelle |
|---|---|---|---|
| Macro (saison) | Contrats, clan, voyage entre zones, tensions, boutique, Bastion | Interface et carte-monde | 3 à 5 h par saison (voir 2.11) |
| Méso (étape, zone) | Exploration d'une zone, traque, quêtes de plateforme, rencontres | Vue 3/4 et plateforme | 20 à 60 min |
| Micro (chasse) | Affrontement | Arène latérale | 10 à 25 min |

Règles de traduction communes (à valider) : (a) un jet d20 du livre devient un **calcul silencieux** quand l'enjeu est la logistique (provisions, orientation) et un **geste d'adresse** quand l'enjeu est la relation (dressage, récit) ; (b) un DD du livre devient un **paramètre de difficulté** (largeur de fenêtre, vitesse, tolérance) ; (c) l'Honneur, la Tension, la Corruption et la Faveur de clan **n'ont pas de barre** : le joueur lit des attitudes, des prix, des accès (Livre II : « montrer les conséquences, jamais les chiffres ») ; (d) tout ce qui est « entre deux sessions » (ellipses, temps libre) devient un **tick de saison** calculé par le jeu.

### 2.2 Le clan comme couche de jeu

**Gardé** : valeur du clan, obligations universelles, avantages mécaniques, rites d'entrée, Consignation. **Simplifié** : 14 clans modélisés par un même gabarit de données (voir 3.2) ; la hiérarchie en 4 grades. **Supprimé** : vote, politique interne détaillée du clan, mariages et pactes formels (hors démo). **Automatisé** : effets de Faveur, attitudes des PNJ.

**Affiliation par héros.** Chaque héros a (a) un **clan d'origine** (une des 14 fiches ou « sans clan »), (b) jusqu'à 2 **affinités** acquises, (c) sa **Faveur** (0 à 10) avec chacun des 14 clans, (d) un **profil culturel** (Livre VIII, 5 axes : combat, mort, magie, autorité, étranger) qui ne donne aucun bonus mais change les options de dialogue et le poids du Récit. Les quatre héros ne sont pas encore définis dans le dépôt (seul le héros 1, jeune chasseur en armure de wyverne rouge, a un visuel). Proposition de gabarit à valider :

| Héros | Clan d'origine proposé | Affinités | Profil culturel type | Rôle de voyage naturel |
|---|---|---|---|---|
| 1. Chasseur en armure de wyverne | Porteurs de Cicatrices (Apprenti Marqué) | Lames Franches ; Pierres Hautes | Combat : épreuve ; Autorité : respect | Guetteur / intendant de la traque |
| 2. (à définir) pisteur ou forestier | Veilleurs Sylvestres | Navigateurs Gris | Magie : respect de l'équilibre | Navigateur |
| 3. (à définir) forgeron ou érudit | Veines d'Éther ou Maisons Anciennes | Mille Voix | Autorité : légitimité | Intendant |
| 4. (à définir) soigneur ou diplomate | Cendres Liées ou Mille Voix | Marée Profonde | Mort : mémoire, Étranger : ouvert | Médecin |

Ces choix sont des **hypothèses de départ** : le dépôt ne fixe ni l'identité ni les clans des héros 2 à 4.

**Hiérarchie et rôles.** Gabarit à 4 grades, avec rites de passage (un rite = une quête ou une scène, jamais un jet) :

| Grade | Nom générique | Condition | Porteurs de Cicatrices (exemple complet) |
|---|---|---|---|
| 0 | Affilié (sans grade) | Rite d'entrée | Entrée : une cicatrice documentée (créature ◆◆ CR 5-9) |
| 1 | Membre | Rite 1 accompli, Faveur ≥ 4 | **Apprenti Marqué** : Rite de Marquage (Consignation complète d'une créature ◆◆ avec cicatrice) |
| 2 | Titulaire | Rite 2, Faveur ≥ 7 | **Cicatrisé de Rang** : survie documentée d'une créature ◆◆◆ (CR 10 à 15) |
| 3 | Conseil | Jalon d'arc 3, Faveur ≥ 9 | **Siège du Cercle des Sept** : un des sept sièges, vacance déclenchée par un jalon collectif |

Les rôles de spécialisation (Archiviste de Combat, Forgeron des Cicatrices…) deviennent des **métiers de clan** rattachés aux arbres de métiers (autre chapitre), pas des grades.

**Effets de grade (à tester)** : chaque clan donne 1 avantage au grade 1, 1 de plus au grade 2, 1 « signature » au grade 3. Exemple pour les Porteurs : grade 1 = les Archives du clan offrent 1 **Jeton de Connaissance gratuit** (sur les 3 maximum) pour toute espèce déjà consignée ; grade 2 = les Soigneurs des Cicatrices retirent une blessure persistante légère par saison ; grade 3 = bonus de Forge sur matériaux de créatures déjà affrontées (le bonus du livre). Pour les 13 autres clans, la table 1.1 fournit l'avantage de base ; la valeur chiffrée sera fixée clan par clan.

**Ressources du clan.** 5 types, présents dans le gabarit : **Archives** (information), **Refuges** (points de repos sûrs sur les routes, voir 2.6), **Réseau** (contacts, événements et prix), **Ateliers** (forge, soins), **Muscle** (aide en défense du Bastion). Jamais de monnaie propre : un clan donne de l'accès, pas de l'argent.

**Obligations (« Appel du Clan »).** Trois obligations universelles du livre deviennent trois **types d'appels** avec échéance en jours de monde :
1. *Défense d'un membre* (secours, alerte, timer court, 3 à 6 jours) ;
2. *Intérêt du clan* (ne pas signer ce contrat, ne pas livrer ce matériau à un rival ; choix de dialogue) ;
3. *Transmission* (enseigner à un jeune PNJ : mini-quête de mentorat, 1 Récit supplémentaire).
Accepter : Faveur +1 et accès ; refuser : Faveur −1 et mémoire du clan (Conséquence au journal) ; ignorer jusqu'à échéance : Faveur −2 et événement hostile possible. Au maximum 1 appel en cours par clan, 2 au total.

**Rituels.** Le rituel du Retour au Clan (offrande, serment, forge cérémonielle, veillée) devient un **choix de rituel** à 3 options au Retour (voir 2.3) ; la forge cérémonielle donne +2 Honneur collectif si réussie, −2 si ratée (valeurs du livre, à lire comme Faveur).

**Faveur de clan (0 à 10, par clan).** Visible seulement par 5 « crans » d'icône de sceau (Hostile 0-1, Méfiant 2-3, Neutre 4-6, Allié 7-8, Frère 9-10), pas par un nombre. Elle remplace l'Honneur de Clan du Livre VIII (conflit résolu par l'option 4). Honneur individuel (0 à 10) reste séparé ; le **Conflit Personnel/Clan** du livre (personnellement respecté mais collectivement suspect) est conservé comme **flag narratif** (Honneur ≥ 7 et Faveur d'un clan ≤ 3) qui ouvre une scène dédiée.

### 2.3 Retour au Clan et Consignation (le journal du joueur)

Le Retour est une **scène** de 3 à 6 minutes, jamais un écran de butin :

1. **Récolte** (dépeçage, autre chapitre) : qualité fixée par la manière de vaincre (flags `manière` du journal).
2. **Récit** : le jeu propose, parmi ce qui s'est **réellement** produit pendant la chasse (flags : `cohesion`, `protege_faible`, `faiblesse_exploitee`, `parties_preservees`, `patience`, `rapidite`, `contrainte_respectee`), jusqu'à **3 éléments** à mettre en avant. Le joueur peut aussi **embellir** (choisir un élément faux) : risque d'**Exposition** différée (voir 5). L'Honneur varie de ±1 à ±2 selon le **code de la région** (valeur centrale du Livre II, par exemple Hautes Terres : le serment ; Cités Libres : la parole donnée ; Marches : l'efficacité prouvée ; Îles des Serments : l'épreuve acceptée). Les PNJ réagissent par attitudes (regards, offres, silence), pas par chiffres.
3. **Rituel** : choix parmi 3 (offrande, serment, veillée), le quatrième (forge cérémonielle) exige un atelier et du temps.
4. **Consignation** : voir ci-dessous.

**Consignation = journal du joueur** (Porteurs de Cicatrices, mais offerte à tous comme « Carnet de chasse » ; chez les Porteurs elle est obligatoire). Le jeu **pré-remplit** une fiche de chasse à partir du journal d'événements : créature, comportements observés (phases vues, attaques télégraphiées, jetons utilisés), ce qui a fonctionné (faiblesse, piège, ouverture), ce qui a échoué (esquive manquée récurrente, phase ratée), **cicatrices** obtenues. Le joueur ne rédige pas : il **valide et choisit 2 à 3 leçons** parmi 6 à 8 propositions (une phrase chacune, générée à partir des flags), et peut ajouter une ligne libre (champ texte court, optionnel, sync PocketBase). Effets :
- La fiche **débloque durablement** une information dans les Archives (comportements d'espèce, visibles dans les prochaines traques : c'est la source du Jeton gratuit des Porteurs) ;
- Une Consignation **complète** après chasse significative donne Faveur +1 chez les Porteurs ; **refuser** : Faveur −1 puis perte progressive de l'accès aux Archives (le seuil du livre : « isolement informationnel ») ;
- Les cicatrices s'affichent sur le portrait du héros dans le Carnet.
La Consignation est le **pont naturel entre le jeu et la table** : elle est la source lisible du journal (voir 2.10).

### 2.4 Campagne, progression collective, jalons

**Gardé** : les trois arcs, la Trinité, les jalons collectifs et individuels. **Supprimé** : la validation par le MJ (« le MJ dit… »). **Automatisé** : détection des jalons par des **conditions de données** sur le journal.

| Jalon (Livre II) | Condition automatique (exemple) | Effet |
|---|---|---|
| Métier | Quête ou chasse de métier ◆ supérieure au grade actuel + témoin PNJ reconnu | Palier de métier (autre chapitre) |
| Compétence | Usage « central et décisif » : action clé d'une chasse ou d'un mini-jeu réussie à difficulté élevée, une fois par arc | +1 compétence |
| Posture | Événement de rupture au journal (choix de dialogue à Honneur ≥ 7 pour les Légendaires) | Nouvelle posture |
| Bastion (collectif) | Défense réussie, ou palier d'Ancrage atteint avec jalon préalable | Palier d'Ancrage |
| Honneur | Acte public irréversible (Récit, serment, trahison) | Variation d'Honneur par saut |

Progression « collective » : Tension et Ancrage sont **par partie** (le groupe de la sauvegarde) ; Faveurs et Honneur sont **par héros**. Chaque saison (voir 2.11) calcule un **bilan** : jalons gagnés, tensions avancées, Faveurs modifiées, conséquences ouvertes. Cadence cible : 1 jalon individuel et 0,5 collectif par saison en moyenne (le livre : 2 à 4 individuels et 1 collectif par arc de 3 à 5 sessions ; une saison valant ~1,3 session).

**Structure des arcs en saisons (à tester)** : Arc 1 Établissement = 4 saisons (Ancrage 0 vers 8, 3 à 5 créatures ◆ à ◆◆), Arc 2 Confrontation = 5 saisons (Ancrage 8 vers 13, 2 à 3 créatures ◆◆ à ◆◆◆, au moins un pic de Tension 9-10), Arc 3 Résolution = 3 saisons (créature légendaire et Terres Inconnues). Total 12 saisons (3 années de monde), 40 à 60 h de jeu. Trop long pour une première campagne : la démo n'en joue qu'une moitié (voir 6).

### 2.5 La carte-monde par îles et zones débloquées

**Structure de la carte** : un graphe de **nœuds de zone** reliés par des **liens** (route terrestre, passage naturel, traversée maritime, vol). Quatre masses :
1. **Le Continent** : 20 régions groupées en 6 zones (Nord : Hautes Terres Claniques, Marches Frontalières, [Terres Fracturées écartée] ; Centre : Cœur Impérial, Provinces Nobles, Confluences ; Est : Forêts Totémiques, Sanctuaires Éthériques, Terres des Prophètes ; Ouest : Cités Libres Marchandes, Cités Voilées, Archipels Nomades ; Sud : Déserts Rouges, Royaumes Marins, Failles du Monde ; Ombre : Royaumes de l'Ombre, Terres Ravagées, Terres Sans Nom ; plus Îles des Serments, Cités Astrales, Théocraties Sacrées que l'Atlas oublie dans §3). Conflit résolu en suivant les 20 fiches (Îles des Serments, Cités Astrales et Théocraties placées par leurs alliances du Livre IX).
2. **Les Îlots Dispersés** : 5 nœuds mineurs, 2 à 5 jours de mer du continent (route des Confréries Vagabondes).
3. **L'Archipel des Îles Brûlantes** : 3 nœuds (Noire, Cendrée, Rivage), accessibles par les Royaumes Marins ou les Confréries.
4. **Le Continent Nord** : un nœud final, fermé par défaut.

**États d'un nœud (4)** : *Inconnu* (non affiché), *Rumeur* (silhouette et nom, ouvert par un contrat, un PNJ ou une carte), *Cartographié* (Marge visible : routes, postes de chasse, sites répertoriés), *Tenu* (un Bastion ou un poste actif ; voyage plus sûr et rapide). Le fond de carte montre la **couche Tenue / Marge / Royaumes Sauvages** du Livre IV (frontières mouvantes : la Marge avance ou recule à chaque saison selon les tensions).

**Déblocage** (ce qui ouvre un nœud ou un lien) : (a) **contrat de la Guilde** vers une région (ouvre en Rumeur) ; (b) **carte certifiée** des Navigateurs (achat, ou récompense : ouvre Cartographié, vaut aussi pour la couche des sites) ; (c) **Voie Secrète** révélée par un PNJ ou un clan (Passage du Voile, via Faveur ≥ 7 de Navigateurs Gris ou Mille Voix) ; (d) **Ancrage** d'un Bastion dans la zone (passe en Tenu) ; (e) **pilote** pour la mer : Royaumes Marins (Marée Profonde), Confréries Vagabondes (Archipels Nomades) ; (f) **conditions de journal** pour les Terres Inconnues : Îles Brûlantes = Faveur ≥ 5 d'un pilote et Tension ≤ 6 ; **Continent Nord** = flag `cycle_phenix_compris`, posé après avoir consigné au moins 3 des 4 indices d'archive (fragments de l'Île Cendrée, passage observé aux Vents Chauds, Os Blancs, Juvénile du Rivage). Conflit : le Bestiaire (4 phœnix ◆◆◆ proches des communautés) et l'Atlas (phœnix secrets, tuer = catastrophe) se contredisent ; **ce chapitre suit l'Atlas** pour le monde (les 4 phœnix du roster deviennent des liens de cycle ou des événements, jamais des cibles de contrat standard).

Les 20 régions, en une table de référence pour les données (valeur centrale tirée du Livre II ch. 4, clan dominant du Livre V ch. 2, titre des 2 tensions de l'Atlas) :

| # | Région | Clan dominant | Valeur centrale | Tensions actives (T-nn) |
|---|---|---|---|---|
| 1 | Cœur Impérial | Sceau Pourpre | Légitimité légale | T01 Audit de la Saison Rouge, T02 Contrat Incomplet |
| 2 | Provinces Nobles | Maisons Anciennes | Le nom et le rang | T03 Guerre Feutrée Arkhen/Vosel, T04 Schisme du Panthéon |
| 3 | Cités Libres Marchandes | Mille Voix | La parole donnée | T05 Guerre des Prix, T06 Contrat de la Guilde de Chasse |
| 4 | Hautes Terres Claniques | Pierres Hautes | Le serment collectif | T07 Vendetta de Cent Ans, T08 Contrat Extérieur |
| 5 | Forêts Totémiques | Veilleurs Sylvestres | Équilibre du vivant | T09 Question de la Lisière, T10 Cercle Brisé |
| 6 | Îles des Serments | aucun | L'épreuve acceptée | T11 Défi Sans Réponse, T12 Créature Inconnue |
| 7 | Marches Frontalières | Navigateurs Gris | Efficacité prouvée | T13 Route du Nord, T14 Disparition du Convoi |
| 8 | Terres Ravagées | Cendres Liées | Tenir debout | T15 Avancée du Cœur Gris, T16 Culte des Survivants |
| 9 | Déserts Rouges | aucun | Maîtrise de soi | T17 Source de l'Est, T18 Influence des Théocraties |
| 10 | Sanctuaires Éthériques | aucun | Pureté du flux | T19 Sanctuaire Scellé, T20 Veilleur Déviant |
| 11 | Cités Astrales | aucun | Transmission du savoir | T21 Schisme Discret, T22 Demande des Terres Ravagées |
| 12 | Failles du Monde | Ciel Brisé | Survie dans le chaos | T23 Faille en Expansion, T24 Expédition Perdue |
| 13 | Royaumes Marins | Marée Profonde | Loyauté d'équipage | T25 Guerre des Routes, T26 Créature du Détroit |
| 14 | Archipels Nomades | Navigateurs Gris | Indépendance absolue | T27 Confrérie Brisée, T28 Contrat de Silence |
| 15 | Royaumes de l'Ombre | aucun | Discrétion = survie | T29 Purge Interne, T30 Alliance avec les Cités Voilées |
| 16 | Cités Voilées | aucun | Maîtrise de l'image | T31 Compétition avec l'Ombre, T32 Masque Brisé |
| 17 | Théocraties Sacrées | aucun | Obéissance à la foi | T33 Schisme Silencieux, T34 Demande d'Inquisition |
| 18 | Terres des Prophètes | aucun | Destinée assumée | T35 Prophétie Convergente, T36 Prophète Silencieux |
| 19 | Confluences | Cendres Liées | Adaptation perpétuelle | T37 Émeute Culturelle, T38 Pression des Provinces |
| 20 | Terres Sans Nom | aucun | Absence de code | T39 Vestige Trouvé, T40 Attrait Croissant |

### 2.6 Voyage et exploration (Livre I ch. 8, Livre X)

**Gardé** : l'étape comme unité, les 4 rôles, la pression sur l'Endurance, les provisions et l'eau, les 3 repos, les environnements dangereux, la météo par table. **Simplifié** : un voyage se joue en **2 niveaux** :
- **Voyage long (carte-monde)** : le joueur trace une route entre deux nœuds, voit le **nombre d'étapes** (courte 1 à 2, moyenne 2 à 5, longue 4 à 10 selon terrain), le **coût en provisions**, le **risque** (couleur de la voie : Tenue verte, Marchande jaune, Piste orange, Secrète violette) et lance. Chaque étape est **résolue en 1 écran** d'une dizaine de secondes (un événement tiré, une décision à 2 ou 3 boutons) ;
- **Étape jouée (zone 3/4)** : quand un événement le demande (rencontre, site dangereux, trace de créature, secours), on **entre dans la zone** en vue 3/4 : le joueur explore, ramasse, esquive, traque. L'étape jouée est la seule qui exige de l'adresse.

**Les 4 jets de voyage deviennent des « postes »** : navigateur (probabilité de s'égarer), guetteur (détection d'embuscade, événement évitable ou non), intendant (consommation de provisions), médecin (blessure persistante aggravée ou non). Un joueur solo ne peut remplir qu'un poste directement ; les autres sont assurés par **compagnons** (PNJ de Bastion, familiers à rôle éclaireur/pisteur/garde/signal) ou **laissés vacants** avec la pénalité du livre (équivalent du Désavantage : événement défavorable plus probable). Le poste **change l'événement tiré**, pas un jet visible.

**Formules proposées (à tester).** Une étape :
- Provisions consommées : 1 portion + 2 d'eau par personne ; chaleur extrême ou désert : eau ×2.
- Événement : tirage sur la table de la région (9 entrées Livre IX) avec une probabilité de **déclenchement** `p_evt = 0,35 + 0,05 × (Tension − 3)` (borne 0,15 à 0,70), plus un tirage sur la table d8 des incidents de route (Voie Marchande ou moindre) avec `p = 0,20`.
- Jauge « Fatigue de route » : +1 par étape ; −1 par repos long ; ≥ 3 ⇒ Endurance max −2 par étape suivante (règle du livre). Aucune barre séparée : l'icône de gourde et de lune s'allume quand la pénalité s'applique.
- Navigation : probabilité de s'égarer `p_égaré = clamp(0,05 + (DD_terrain − 11) × 0,06 − bonus_outils, 0, 0,6)` avec DD_terrain = 12 forêt, 14 montagne/désert, 16 Terres Ravagées, 18 Failles ; bonus des outils : boussole 0,09, carte régionale 0,06, boussole éthérique 0,12 ; nuit ou brouillard : +4 au DD.

**Météo.** Une météo par jour de monde, tirée sur la table de terrain (6 tables Livre X ; les autres terrains retombent sur la table la plus proche, à compléter) et modifiée par la saison (pondération simple : hiver ×2 sur les cases froides, été ×2 sur les cases chaudes). Effets visuels (pluie, brouillard) et mécaniques directs (visibilité réduite en exploration, traces effacées en 1 h, tempête = on ne voyage pas).

**Repos et camp.** Écran de **camp** à la fin d'une étape : choisir la qualité (sommaire, défensif, abri construit), le **guet** (qui veille), le **repas** (provisions) ; repos court = bouton « souffler » (moitié de l'Endurance), long = « dormir », complet = « se retirer » (exige un abri ou un Refuge de clan). Les **Refuges** (ressource de clan) sont des points fixes sur les routes de la carte : en dormir fait gagner Fatigue −1 supplémentaire.

**Environnements dangereux** : les 5 du Livre I deviennent 5 « tags » de zone avec effets passifs (marais : +1 étape ; désert : eau ×2 ; haute montagne : Endurance max −1 jusqu'à acclimatation après 2 étapes ; ruines : lumière requise ; Failles/Zones corrompues : tick de Corruption, autre chapitre). Les règles chaleur, froid, déshydratation et faim du Livre X sont **résumées en 3 paliers** (avertissement, pénalité, danger) par ressource, avec une icône qui clignote, plutôt que la table d'heures.

**Routes et sites dangereux.** Les 3 grands axes et les 5 passages naturels du Livre IV sont des **liens spéciaux** : Route du Fer Gris (22 à 30 jours : 7 à 10 étapes de 3 jours, voyageable en caravane contre péage), Passage du Voile (voie secrète, 8 à 12 jours), Voie des Cendres (piste de chasse, 6 jours, saisonnière : migrations actives selon la saison), Col de l'Éperon (fermé 4 mois par an), Passage Bas de Tyr (nuit seulement). Les **sites dangereux** (Ruines Profondes, Fosses Naturelles, Sites Corrompus) sont des **donjons-plateforme** générés par la table 6 colonnes d6 du livre (voir `docs/generation-procedurale.md`) ; ce chapitre fixe seulement leur interface (carte : symboles ⬟ répertorié, ⬠ non cartographié, légende du Livre IV ch. 9).

### 2.7 Moyens de transport (montures, bêtes de somme, mer et ciel)

**Données disponibles** : 15 montures terrestres, 19 bêtes de somme, 3 marines, 2 aériennes (voir 1.10). La rareté des transports aérien et maritime est un **fait de design à assumer** : le jeu ne peut pas reposer sur des montures volantes pour passer d'une île à l'autre.

| Transport | Source | Effet de jeu proposé (à tester) |
|---|---|---|
| À pied | Défaut | Étapes du tableau du livre ; 0 éclat |
| Bête de somme (19) | `bete_de_somme` (ex. Colporin, Bœurak, Équirak) | Capacité de charge : +6 emplacements d'inventaire de voyage, provisions ×1,5 par portion transportée ; vitesse = piéton |
| Monture terrestre (15) | `monture_terre` (ex. Dorgane, Équirak, Dambrais) | Étapes ÷ 2 en terrain standard (arrondi supérieur), Endurance de route −1 par étape évitée ; 1 personnage ou « groupe de 2-4 » selon `capacite_transport` ; impossible en terrain « falaise » ou « mer » (champ `limite`) |
| Caravane | Livre IV ch. 9 | Étapes × 1,3 (plus lent) mais sans consommation de provisions personnelles ; frais d'escorte en éclats ; 1 incident de route d8 forcé par tronçon |
| Monture marine (3) | Pressoir (estuaire, 2 à 4 personnes), Prairelle (2 à 4), Poterne (1) | Remonte un fleuve ou longe une côte : accès à des routes fluviales et estuaires, **pas** haute mer (Pressoir est explicitement trop lent) |
| Navire à pilote | Royaumes Marins, Confréries Vagabondes, Ports Unifiés | **Seul moyen de franchir** les mers vers les Îlots Dispersés et Îles Brûlantes ; durée 2 à 5 jours ; coût en éclats ; Faveur d'un clan marin (Marée Profonde, Navigateurs Gris) abaisse le prix et ouvre les routes sûres |
| Monture aérienne (2) | Aquilarak (CR 4, DD 11, 1 personnage, « courtes distances », se fatigue vite), Wistrelle (CR 11, symbiotique, DD 18, 1 personnage, refuse tout cavalier hors lien complet) | **Raccourcis, pas transport de groupe** : Aquilarak survole une zone de 1 étape (franchit un ravin, une falaise) ; Wistrelle permet à 1 personnage de passer d'une île à l'autre seul, et le groupe suit par navire (le jeu **n'impose pas** la monture) |

**Interface** : le choix du transport apparaît sur l'écran de planification de voyage (une ligne par option avec icône, durée, coût, risque). Les montures ont une **Endurance de monture** (0 à 10) qui baisse par étape ; à 0 elles sont K.O. (voir 2.9).

**Conflit data** : Poterne (lev08) a le rôle `monture_mer` mais `transport: null`. À corriger dans le JSON (voir 7, question 8).

### 2.8 Tensions actives et monde vivant

**Gardé** : les 40 tensions (une à deux par région), leurs chiffres (Cœur Gris : 3 m/an passé à 7 m/an ; Fissure Centrale : +10 à 15 m/mois, routes des Marches atteintes en environ 18 mois ; convoi des Ravins de Keth : disparu depuis 3 semaines ; Créature du Détroit : 40 % du trafic commercial). **Traduit** : chaque tension est une **horloge**.

| Champ | Sens |
|---|---|
| `type` | `front` (progression physique), `horloge` (échéance), `mystère` (se résout par enquête), `faction` (rapport de forces) |
| `etape` / `etape_max` | Position de l'horloge (0 à 4 en général) |
| `pas_par_saison` | Progression automatique à chaque saison (0, 0,5 ou 1) |
| `leviers` | Tags d'actes qui la freinent ou l'accélèrent (par exemple `chasse_creature_detroit`, `route_securisee`) |
| `si_max` | Conséquence quand elle atteint son maximum (un événement et une modification d'état de monde) |
| `visibilite` | `cachée`, `rumeur`, `visible` |

Exemples chiffrés (à valider avec le MJ de la table) :
- **T23 Faille en Expansion** : `type front`, `etape_max 6`, `pas_par_saison 1` (≈ 30 m par mois ⇒ 18 mois = 6 saisons), `si_max` : les premières routes des Marches sont coupées (lien du graphe désactivé, Marge recule).
- **T15 Avancée du Cœur Gris** : `front`, `etape_max 8`, `pas_par_saison 0,5` si aucun levier ; passe à 1 si Tension globale ≥ 7 ; `si_max` : une ville des Terres Ravagées est évacuée.
- **T14 Disparition du Convoi** : `mystère`, `etape_max 3`, `pas 1` (la rumeur s'envenime) ; à l'étape 3, une guilde accuse un clan ; résolue par le hook « Convoi Fantôme » (le convoi s'est caché volontairement).
- **T26 Créature du Détroit** : `horloge`, `etape_max 4`, chaque étape coûte du trafic (prix des matériaux marins +10 % par étape) ; tuer la créature (chasse ◆◆◆) la clôt.

**Monde vivant sans simulation lourde** : la simulation tourne **à la fin de chaque saison**, hors écran, sur les tensions des zones débloquées et des zones adjacentes (au plus 12 tensions simulées ; les autres progressent en lot). Une tension de zone non visitée avance de moitié. Le résultat est écrit au journal (voir 3.5) et peut être lu **par la table** (le MJ humain) qui a le droit de la faire avancer à la main.

**Événements régionaux.** À l'entrée d'une région, puis une fois par saison dans une région où le groupe a un Bastion ou une Faveur ≥ 4 d'un clan présent, tirer un événement de la table de la région (Livre IX). Chaque événement du livre reçoit un **tag de type** (danger, social, politique, opportunité) et un **modèle de scène** : politique ⇒ scène de dialogue à choix ; danger ⇒ étape jouée ; opportunité ⇒ contrat ou marchand. Mauvaise nouvelle : 180 événements (20 × 9) à tagger ; réduction pour la démo, voir 6.

### 2.9 Économie

**Gardé** : l'éclat, les 5 raretés, le principe « argent = outil, jamais progression », les dettes sociales, la certification, le Conseil des Primes. **Supprimé** : micro-gestion de prix par objet (pas de marchandage manuel, remplacé par 3 attitudes du marchand selon la Faveur) ; l'inventaire de monnaie fractionnée. **Ajouté (à valider)** : des prix, absents du livre.

**Contrats de la Guilde de Chasse.** Un contrat est un objet de données (voir 3.4) : mandant, créature, zone, contraintes (garder la tête intacte, préserver une partie rare, zone intacte), échéance en jours de monde, prime. Les 3 formes de Désignation du Livre I (Nécessité, Contrat, Prestige) sont des **types**. Le **Conseil des Primes** fixe la prime par formule ; le **Contremaître Régional** les affiche au **tableau de contrats** (3 à 6 contrats visibles selon l'Ancrage et la Faveur de la Guilde). Les **Certificateurs** évaluent la qualité des pièces au moment du rendu : la qualité (Standard, Supérieure, Élémentaire, Rare) donne un **multiplicateur de prix** et conditionne les **clauses** du contrat.

**Formules de départ (tout à tester).**
- Prime de base : `prime = round(10 × CR^1,5)` éclats (CR 1 ⇒ 10 ; CR 4 ⇒ 80 ; CR 8 ⇒ 226 ; CR 12 ⇒ 416 ; CR 18 ⇒ 763) ; Nécessité × 0,8 (on agit parce qu'il le faut) ; Prestige × 1,5 mais ±2 Honneur ; clause respectée +15 % chacune, clause violée −25 %.
- Prix d'une pièce de monstre : `base_rareté` du livre (◆ 3 ; ◆◆ 20 ; ◆◆◆ 75 ; ◆◆◆◆ 350 ; ◆◆◆◆◆ 1 000 éclats) × multiplicateur de qualité (Standard 1,0 ; Supérieure 1,5 ; Élémentaire 2,0 ; Rare 3,0) × multiplicateur de lieu (Velhan et Menûl 1,25 ; village 0,6). Une chasse CR 12 ◆◆◆ livre 3 à 5 pièces : revenu moyen d'environ 450 éclats avec qualité Supérieure.
- Dépenses de voyage : provisions 2 éclats la portion, eau 1, caravane 15 par étape et par personne, navire de 60 à 200 selon la durée (2 à 5 jours), réparation 20 % du prix d'achat par niveau d'usure.
- Ordre de grandeur cible : un héros niveau de départ gagne ~300 éclats par saison et en dépense ~250 (voyage, réparation, provisions, consommables) ; l'excédent finance le Bastion.
- **Garde-fous du livre** : aucun achat de niveau, de Posture, de Forge ni d'Honneur ; vendre des matériaux de chasse ne donne **pas** de bonus de Forge ; dépenser pour contourner l'Honneur en région stricte donne un malus d'Honneur (−1) et un rappel du PNJ.

**Boutiques.** Trois niveaux de stock selon la **catégorie d'établissement** (Village, Bourg, Cité du Livre IV) et l'**Ancrage** du Bastion : provisions et soins de base partout ; consommables et armes Standard dans les bourgs ; armes Supérieures, accessoires et cartes certifiées en cité ; objets Rare et Signature seulement chez forgerons reconnus et ne se vendent pas (ils se commandent, comme le livre). Stock renouvelé à chaque saison ; un **marchand itinérant** arrive au Bastion selon la table d'événements d20 (case 2, matériaux rares à prix élevé).

**Dettes.** Quatre types du livre en données (3.4, table `obligations`) : Faveur, Dette de sang, Pacte d'intérêts, Compte ouvert. Chaque dette a une **échéance souple** (en saisons), une valeur d'« intérêt narratif » qui augmente chaque saison (paliers 1 à 3), un créancier (PNJ ou clan). Elle apparaît dans l'écran **Obligations** (liste), jamais comme une dette chiffrée en éclats, sauf pour le **prêt des Marchands Libres** (seule dette monétaire : prêt de 100 à 500 éclats, intérêt de 10 % par saison à tester, saisie d'un actif du Bastion en cas de retard de 2 saisons). Un clan qui perd patience propose l'Exclusion (4 niveaux du livre) : niveaux 1 à 2 automatiques, niveaux 3 et 4 par jalon collectif seulement.

### 2.10 Familiers : états, origines, dressage, lien, combat, K.O., élevage

**Modèle déjà défini dans CharForge** (à respecter) : 3 états de relation **Sauvage, Habituée, Dressée** ; origines **dressage, vol d'œuf ovipare, élevage** ; élevage avec résultat **perdu / normal moins bon / exceptionnel** ; inter-espèces **reporté** ; seuil d'intelligence légendaire **à définir** (proposé ci-dessous). Le terme « Habituée » est féminin dans CharForge : conservé tel quel dans les données (`habituee`).

**Correspondance états relation vs lien maximal (`lien_max`).** Les deux axes sont distincts : l'état dit où en est *cet individu*, le lien maximal dit jusqu'où l'espèce peut aller.

| État (CharForge) | Définition de jeu | Capacités |
|---|---|---|
| Sauvage | Pas de phase 1 réussie. Hostile ou méfiant. | Aucune ; l'animal fuit ou attaque. |
| Habituée | Phase 1 réussie et jalon narratif accompli : tolère le héros, le suit, mange à la main. | Suivi, rôles passifs : éclaireur, pisteur, signal, bête de somme, garde statique ; **ne combat pas**. |
| Dressée | Phase 3 achevée jusqu'au `lien_max` : obéit aux ordres de la liste dressable. | Tous les rôles de la fiche, **aide en combat**, monture, transport. |

Le `lien_max` de l'espèce plafonne la **profondeur** du dressage : *conditionné* (obéissance conditionnée, régresse vite), *partiel*, *affectif* (défend le héros, ordres complexes), *symbiotique* (9 cas : Wistrelle, phœnix, etc.), *élevage* (8 cas : espèces d'élevage, lien d'enclos).

**Origines.**
1. **Dressage (créature sauvage)** : les 3 phases du Livre III, voir plus bas. Jeune de préférence (`age_ideal`).
2. **Vol d'œuf ovipare** : possible quand l'espèce est ovipare (à ajouter dans les données : `oviparite: true`, fréquent chez les bipèdes de meute et les grands volants). Mini-séquence **furtive en vue 3/4** vers un nid (gardé par un adulte, comportements de patrouille), puis **incubation** (3 à 8 jours de monde selon la taille, à garder au chaud : action de camp). L'éclosion produit un individu **déjà Habituée** (imprégnation) avec un bonus de DD de −3 à la phase 3. Conséquences au journal : Faveur des Veilleurs Sylvestres −1 si l'espèce est protégée (Livre V : « La Chasse Interdite »), Infamie si l'espèce est une espèce sacrée (Théocraties), Tension +1 si les parents survivent et traquent.
3. **Élevage** (au Bastion, bâtiment « Enclos », autre chapitre, plafond de bâtiments) : deux parents **Dressés** d'une même espèce (inter-espèces reporté) produisent une couvée ; résultat tiré par une table pondérée : **perdu 15 %**, **normal moins bon 55 %**, **normal exceptionnel 30 %** (à tester) ; modifié par le niveau d'Éleveur du héros ou du PNJ (Lignée Stable niv. 5 : −5 points de « perdu », Lignée Signature niv. 10 : +10 points d'« exceptionnel »). « Exceptionnel » = +1 palier de stat de soutien (cf. plus bas) et lien_max conservé. « Moins bon » = stats −1 palier, durée de croissance +50 %. « Perdu » = œuf non éclos, nourriture perdue, aucune pénalité d'Honneur.

**Dressage : les 3 phases du Livre III en mini-jeux tactiles.** Le DD d'espèce (`difficulte_dd`, 1 à 18 dans les données, souvent 10 à 14) règle la difficulté, le niveau de Dresseur du héros (Livre VII, DD 8 à 32 selon niveau) règle la tolérance. Définition : `delta = DD_espèce − DD_niveau_dresseur` (négatif = facile).

*Phase 1, Approche (mini-jeu « Cercle de confiance », en vue 3/4, 30 à 60 s)* : la créature est dans un **cercle de tolérance** ; le joueur **maintient le doigt** sur un bouton nourriture et **déplace le héros à l'écran** vers la créature par glissement lent. Une jauge de **Confiance** (cachée par une silhouette de queue ou de souffle) monte quand le glissement est lent et constant, et **baisse** à chaque geste brusque ou si la meute est à portée (règle du livre : odeur de meute = échec automatique ou DD +5). Réussite tendue (confiance 70 %) : la créature tolère la présence ; Réussite (100 %) : elle mange dans la main. Paramètres : fenêtre de vitesse acceptée = `clamp(45 − 3 × delta, 10, 45)` degrés par seconde ; difficultés additionnelles du livre (créature blessée = plus ouverte : −2 ; en présence de sa meute : +5 ; de nuit : +2).

*Phase 2, Jalon narratif (sans jet)* : un **événement scripté** que le jeu déclenche quand les conditions sont remplies : la créature *choisit* de suivre le héros sur une distance (trajet à pied de 2 étapes **sans** la maintenir par la nourriture) ou de le défendre face à une menace (rencontre créée par le jeu et reconnue par flag `jalon_lien`). Le jeu ne le force pas : il le **propose** lors d'un événement de voyage ; c'est le joueur qui choisit d'engager la rencontre. Durée minimale en **jours de monde** (3 jours au minimum en Phase 1, comme la fiche).

*Phase 3, Apprentissage (mini-jeu « Ordres », 3 à 4 séances de 45 s)* : séquences de **gestes** (glisser vers une cible, appui long, double appui) à exécuter dans le bon ordre et le bon rythme (rythme et tolérance calés sur le `delta`) ; chaque réussite fait **baisser le DD** comme dans le livre (DD 10 puis 8 après 3 réussites ; DD 13 puis 10 après 4). Chaque séance **débloque un comportement** parmi la liste dressable de la fiche (suivi, garde statique, signal d'alerte, attaque sur désignation, retour sur commande) ; les comportements **non dressables** de la fiche restent des limites (par exemple « fuit si une alarme de sa meute retentit »). Une séance par jour de monde minimum.

*Rupture* : un compteur `jours_sans_soin` ; au-delà du seuil de la fiche (par exemple 10 jours) l'état redescend d'un cran (Dressée → Habituée → Sauvage) et le lien **ne se reconstruit pas avec le même individu** pour les espèces à lien conditionné (fidèle au livre : « le lien ne se reconstruit pas »). Cause d'erreur de design : un joueur qui laisse son familier au Bastion pendant un arc le perdrait injustement ; **mesure** : au Bastion, un PNJ soigneur ou un Enclos suspend le compteur, et l'écran Familier affiche une icône d'alerte dès 70 % du seuil.

**Lien et attachement.** Une jauge de **Lien** (0 à 100) par familier, jamais montrée en chiffres : elle monte par soins, repas, chasses en commun, nuits au camp ; elle baisse par abandon, K.O. répétés, ordre contraire à sa nature. Seuils : 25 (Habituée), 60 (Dressée), 85 (Lien Signature, gain d'un bonus propre), 100 (Lien Légendaire, voir ci-dessous).

**Aide en combat.** Chaque familier dressé de rôle `assistant_combat`, `garde`, `signal` ou `soin` fournit **1 action** assignée à un bouton secondaire du HUD de chasse (pas de contrôle direct du familier, pour tenir sur 360 px et sur un seul pouce). Actions types dérivées du champ `aide_combat` (texte déjà écrit pour les 106) :
- **Distraction** : le monstre détourne sa prochaine attaque de 1,5 s (Canarak : mord la jambe ; Aquilarak : pique le point faible) ;
- **Alerte** : télégraphie un coup arrière ou une attaque de phase (rôle `signal` ; équivalent d'un Jeton de Connaissance éphémère) ;
- **Charge** ou **ouverture** : brise la garde d'un monstre à partie blindée (Dorgane, Pressoir) ;
- **Soin** : rôle `soin` (8 espèces), rend 1 point de Vitalité par minute à portée ;
- **Éclairage** ou **éblouissement** (phœnix, Wistrelle) : désavantage temporaire d'une cible.
Temps de recharge 12 à 25 s selon le CR (à tester). Le familier est **absent** des phases où le héros combat un Dragon Ancien (cinématiques) et des quêtes de plateforme en espace étroit.

**K.O. et soins.** Le champ `aide_combat` des 106 familiers dit qu'ils peuvent être « mis K.O. par fatigue, puis soignés ». Traduction : une **Endurance de familier** (0 à 10) que chaque action consomme (1 à 2) ; à 0, il est **K.O.** : il se retire de la chasse (icône de repos), n'a pas de cicatrice, revient après un repos au camp ou **un soin** (consommable `ration_familier`, ou un Guérisseur). Un familier à 0 Vitalité (touché plusieurs fois) devient **blessé** : il perd un palier de Lien pour 1 à 3 saisons et subit une **cicatrice visible** (Trace au journal). Le jeu **ne tue jamais** un familier de manière définitive à la démo (aucun permadeath : option « mort définitive » en mode difficile, v0.4+).

**Intelligence et Lien Légendaire (seuil proposé).** Le Livre III donne une **Intelligence** (Faible, Faible-moyenne, Moyenne, Élevée, Très élevée) sur 14 fiches seulement ; la donnée n'existe pas dans le JSON. Le Livre VI dit que le Lien Légendaire exige une créature de **rang III ou plus** (◆◆◆, CR 10+) et le Livre VII que le Pacte intentionnel (Dresseur niveau 24) vise une « créature consciente ». **Proposition** : ajouter `intelligence` (1 à 5) à chaque familier (par défaut déduite de `lien_max` : conditionné 1-2, partiel 2-3, affectif 3-4, symbiotique 4-5) et définir le **seuil légendaire** par la conjonction de trois conditions : `intelligence ≥ 4` **et** `CR ≥ 10` (◆◆◆) **et** `lien_max ∈ {affectif, symbiotique}` ; en jeu, le héros doit en plus avoir **Dresseur niveau 24** et **Lien ≥ 85**. Les familiers répondant à ces conditions sont rares (≈ 5 à 10 sur 106 selon la donnée, à compter après ajout du champ) : c'est voulu, le Lien Légendaire est une récompense d'arc 3. Wistrelle (CR 11, symbiotique, DD 18) est le premier candidat naturel.

**Interface tactile du familier.** (a) **Fiche Familier** : portrait (sprite), état (Sauvage/Habituée/Dressée), Lien (5 crans), rôles (icônes), Endurance, comportements débloqués, âge ; (b) **boutons de soin** (nourrir, caresser, soigner) à 48 dp minimum ; (c) **HUD de chasse** : un bouton (icône du familier) à droite du pouce, avec cercle de recharge ; (d) **Mini-jeux** décrits plus haut, en plein écran, gestes à un doigt, pas de lecture de texte pendant l'action.

### 2.11 Journal d'événements PocketBase (Acte / Trace / Conséquence)

Chaque événement **significatif** du jeu écrit un enregistrement dont le contenu est **trois champs obligatoires** (règle de design du Livre I : la Trinité ne se livre pas en trois temps). Un événement qui ne remplit pas les trois n'est pas écrit au journal des événements : il va dans un **log mineur** local (non synchronisé). Types d'événements de ce chapitre :

| Type | Acte (quoi) | Trace (marque permanente) | Conséquence (coût) |
|---|---|---|---|
| `chasse` | créature, manière de vaincre, jetons utilisés | pièce forgée, cicatrice, titre, Consignation | dette, Faveur ±, créature qui reviendra, route ouverte ou fermée |
| `voyage` | itinéraire, événements d'étape, pertes | carte révélée, nœud passé en Rumeur ou Cartographié | provisions perdues, Tension +, rencontre d'une faction |
| `clan` | appel accepté/refusé, rite, Récit | grade, sceau, objet nommé | Faveur ±, appel suivant, Exposition |
| `contrat` | contrat accepté/rendu/refusé | certificat, prime reçue | réputation auprès de la Guilde, mandant revient |
| `familier` | phase de dressage, éclosion, K.O., rupture | état du familier, cicatrice | Lien, Faveur d'un clan protecteur, Tension |
| `tension` | horloge qui avance | changement d'état du nœud, événement régional | lien du graphe coupé, créature déplacée |
| `economie` | achat, dette, prêt | objet acquis, titre foncier | intérêt qui monte, saisie |

Les événements sont **append-only**, horodatés en temps réel et en **temps de monde** (saison, jour). La **table de jeu** (MJ humain) peut ajouter des événements (`source: table`) qui s'appliquent au jeu à la synchronisation suivante, ou **clore** une tension. Voir 3.5 pour le schéma.

### 2.12 Boucle de jeu à l'échelle de la campagne : une saison de jeu

Une **saison** (3 mois de monde, 3 à 5 heures réelles). Elle reprend les 4 temps du Livre I, la Phase de Bastion du Livre II et la diplomatie, en sept **étapes**, chacune avec son écran :

| # | Étape | Écrans et mode | Ce qui se passe | Durée |
|---|---|---|---|---|
| 1 | **Convocation** | Interface | Bilan de la saison précédente (jalons, tensions, Faveurs), **tableau de contrats** + appels de clan + Tension ; **Désignation** d'une cible (Nécessité, Contrat ou Prestige) | 5 min |
| 2 | **Préparation** | Interface, Bastion | Phase de Bastion de départ : forge, achats, soins, familier (soin, dressage), choix de transport | 10 à 15 min |
| 3 | **Voyage** | Carte-monde, étapes, 3/4 | 1 à 3 étapes jouées, camp, météo, route choisie, événements régionaux | 20 à 40 min |
| 4 | **Traque** | 3/4 | Repérage, jetons de Connaissance (max 3), pièges | 15 à 25 min |
| 5 | **Affrontement** | Arène latérale | Chasse (autre chapitre) ; le familier aide ; manière de vaincre enregistrée | 10 à 25 min |
| 6 | **Retour au Clan** | Scène, interface | Récolte, Récit, Rituel, **Consignation** ; rendu du contrat et certification | 10 à 15 min |
| 7 | **Bastion et diplomatie** | Interface, dialogue | Phase de Bastion (rapport, activités), événement d'Ancrage, **scène politique** (Salle du Conseil, Ambassadeur de Clan, duel verbal ou négociation, autre chapitre), **tick de saison** (tensions, météo, Marge) et Projection | 15 à 25 min |

Chaque saison comporte **2 chasses** (une ◆ à ◆◆ « d'entretien » et une ◆◆ à ◆◆◆ « de campagne »), **1 à 2 quêtes de plateforme** (cueillette, minage, ruines) intercalées pendant le Voyage ou la Préparation, **1 scène de clan**, **1 voyage entre zones** (ou 1 séjour au Bastion), **1 scène de diplomatie**. Le **tick de saison** applique : progression des horloges, renouvellement des boutiques et du tableau de contrats, vieillissement des dettes, changement de saison (modificateur de météo, migrations), recul ou avancée de la Marge, évolution du Lien des familiers laissés au Bastion. La **saison se termine** par un écran « Bilan » de 60 secondes (Trinité de la saison, 3 lignes) ; c'est aussi la **sauvegarde de campagne** et la synchronisation PocketBase.

---

## 3. Modèle de données

Tous les fichiers sont des **JSON exportables** ; les tables PocketBase portent les mêmes champs. Convention : identifiants courts (`snake_case` pour les clés, `id` du roster pour les créatures, par exemple `cro02`).

### 3.1 `regions.json` (20 entrées)

```json
{
  "id": "marches_frontalieres", "numero": 7, "nom": "Marches Frontalières",
  "zone": "nord", "bloc": "rouge", "ile": "continent",
  "valeur_centrale": "efficacité prouvée",
  "avantage": "avantage terrain hostile", "contrainte": "réputation instable hors des Marches",
  "clan_dominant": "navigateurs_gris", "guildes": ["guilde_de_chasse"], "ordres": [],
  "villes": [{"id": "dureth", "nom": "Dureth", "categorie": "bourg", "habitants": 6000}],
  "lieux": ["poste_7", "ravins_de_keth"],
  "tensions": ["T13", "T14"],
  "table_evenements": "evt_marches", "table_meteo": "terrain_marches",
  "creatures_rangs": {"I-II": "meutes partout", "III": "territoires dans le tiers central"},
  "alliances": ["cites_libres", "confluences"], "tensions_fortes": ["coeur_imperial", "theocraties"],
  "etat_defaut": "marge"
}
```

### 3.2 `clans.json` (14 entrées)

```json
{
  "id": "porteurs_cicatrices", "numero": 12, "nom": "Porteurs de Cicatrices",
  "devise": "Chaque blessure est une leçon gravée dans la chair.",
  "valeur": "la cicatrice est une information",
  "regions": [], "alliances": ["guilde_de_chasse", "guilde_des_soigneurs", "archivistes_stellaires"],
  "frictions": ["guildes_contrats_sans_documentation"],
  "grades": [
    {"niveau": 1, "nom": "Apprenti Marqué", "rite": "rite_marquage", "faveur_min": 4,
     "avantage": {"cle": "archives_jeton_gratuit", "valeur": 1}},
    {"niveau": 2, "nom": "Cicatrisé de Rang", "rite": "rite_cicatrise", "faveur_min": 7,
     "avantage": {"cle": "soins_cicatrices_saison", "valeur": 1}},
    {"niveau": 3, "nom": "Cercle des Sept", "rite": "jalon_arc3", "faveur_min": 9,
     "avantage": {"cle": "bonus_forge_creatures_affrontees", "valeur": 1}}
  ],
  "ressources": ["archives", "ateliers", "soigneurs"],
  "obligations": ["consigner_apres_chasse_significative", "defendre_un_membre", "transmettre"],
  "rituel": "consignation",
  "hooks": ["archive_incomplete", "cicatrice_impossible", "debat_de_methode"]
}
```

### 3.3 `relations_clan` (par héros, par clan)

```json
{ "heros": "h1", "clan": "porteurs_cicatrices", "faveur": 5, "grade": 1,
  "origine": true, "affinite": false, "appel_en_cours": "appel_0042",
  "derniere_consignation": {"saison": 3, "creature": "cro02"} }
```
`faveur` entier 0 à 10 ; `grade` 0 à 3 ; l'interface n'affiche jamais le nombre.

### 3.4 Contrats, obligations, dettes

```json
{ "id": "ct_0107", "type": "contrat", "mandant": "guilde_de_chasse", "region": "marches_frontalieres",
  "creature": "cro02", "contraintes": ["garder_la_tete_intacte"],
  "echeance_jours": 21, "prime_base": 80, "prime_modificateurs": {"clause_respectee": 0.15, "clause_violee": -0.25},
  "etat": "disponible" }
```
```json
{ "id": "ob_0021", "categorie": "faveur", "creancier": "ourse_de_fer", "heros": "h1",
  "origine_evenement": "ev_00931", "echeance_saisons": 2, "interet_narratif": 1, "etat": "ouverte" }
```
`categorie` ∈ `faveur`, `dette_de_sang`, `pacte_interets`, `compte_ouvert`, `pret_marchands` (seule avec `montant_eclats`).

### 3.5 Journal d'événements (PocketBase, collection `evenements`)

```json
{
  "id": "ev_00931", "source": "jeu", "heros": "h1",
  "t_reel": "2028-03-16T14:20:00Z", "t_monde": {"saison": 3, "jour": 41, "region": "marches_frontalieres"},
  "type": "chasse",
  "acte": {"creature": "cro02", "maniere": ["faiblesse_exploitee", "parties_preservees"], "jetons_utilises": 2, "qualite_matiere": "superieure"},
  "trace": {"objet": null, "cicatrice": "cicatrice_flanc_gauche", "consignation": "cs_0014", "titre": null},
  "consequence": {"faveur": {"porteurs_cicatrices": 1}, "tension_delta": -1,
                  "horloge": {"T14": 0}, "dettes_ouvertes": [], "cree": "creature_reviendra:cro02"},
  "visible_table": true
}
```
Règles : `acte`, `trace`, `consequence` non nuls (au moins une clé non vide chacun, sinon l'événement n'est pas écrit). `source` ∈ `jeu`, `table` ; un événement de table porte `applique_jeu: false` jusqu'à synchronisation.

### 3.6 Tensions, tables d'événements, météo

```json
{ "id": "T23", "region": "failles_du_monde", "titre": "La Faille en Expansion",
  "type": "front", "etape": 1, "etape_max": 6, "pas_par_saison": 1,
  "leviers": ["expedition_fissure", "alerte_guildes"], "visibilite": "rumeur",
  "si_max": {"lien_coupe": ["failles_vers_marches"], "evenement": "evt_route_nord_coupee"},
  "source_livre": "Atlas ch. 2, région 12" }
```
```json
{ "id": "evt_marches", "region": "marches_frontalieres",
  "entrees": [
    {"n": 1, "titre": "Escarmouche sans commanditaire clair", "tag": "danger", "scene": "etape_jouee"},
    {"n": 2, "titre": "Mercenaires retournant leur veste", "tag": "politique", "scene": "dialogue"},
    {"n": 3, "titre": "Autorité locale renversée", "tag": "politique", "scene": "dialogue"}
  ] }
```
```json
{ "id": "terrain_hautes_terres", "terrain": "hautes_terres", "d12": [
    {"plage": [1,2], "meteo": "brouillard_epais", "visibilite_m": 10, "effets": ["desavantage_perception", "piste_desavantage"]},
    {"plage": [11,11], "meteo": "tempete_neige_ou_orage", "visibilite_m": 5, "effets": ["feu_impossible", "deplacement_-2m"]}
  ] }
```

### 3.7 Familiers : extension du champ existant

Le champ `familier` des fiches (`donnees/monstres/*.json`) reste tel quel. **Ajouts proposés** (champs optionnels à backfiller par script) :
```json
"familier": {
  "possible": true, "lien_max": "affectif", "difficulte_dd": 15,
  "oviparite": true, "intelligence": 3, "legendaire_eligible": false,
  "phases": {"approche_dd": 15, "approche_dd_meute": 20, "apprentissage_dd": 13, "apprentissage_dd_reduit": 10, "reussites_pour_reduire": 4,
             "jalon": "defendre_le_dresseur", "duree_min_phase1_jours": 14, "seances_phase3": 4},
  "comportements_dressables": ["suivi", "protection_campement", "attaque_sur_designation", "retour_sur_commande"],
  "comportements_non_dressables": ["reaction_au_rugissement_dominant"],
  "rupture_jours": 10, "reconstruction_possible": false,
  "endurance_familier": 8, "recharge_aide_s": 18
}
```
Valeurs issues du Livre III (via `ligne_livre3` dans `correspondance.json`) pour `phases`, `rupture_jours`, `comportements_*` ; défauts calculés sinon.

Instance joueur (`familiers_joueur`) :
```json
{ "id": "fam_0007", "heros": "h1", "espece": "cro02", "nom": "Brindille",
  "etat": "habituee", "lien": 41, "origine": "vol_oeuf", "age_jours": 62,
  "phase": 2, "seances_faites": 0, "jours_sans_soin": 3, "endurance": 8, "blessure": null,
  "comportements": ["suivi"], "stats_soutien": {"palier": 0}, "cicatrices": [], "lignee": null }
```
Élevage (`elevages`) :
```json
{ "id": "el_003", "parents": ["fam_0007", "fam_0011"], "espece": "cro02", "debut_saison": 5,
  "resultat": "exceptionnel", "naissance_saison": 6, "enclos": "bat_enclos_1" }
```
`etat` ∈ `sauvage`, `habituee`, `dressee` ; `resultat` ∈ `perdu`, `normal_moins_bon`, `exceptionnel`.

---

## 4. Interfaces et flux

Écran de 360 px de haut, paysage ; cibles tactiles ≥ 48 dp ; navigation à un pouce ; ouvrir les écrans par la gauche, valider à droite.

| Écran | Contenu | Entrées et sorties |
|---|---|---|
| **Carte-monde** | Graphe des 4 masses, états des nœuds, couche Tenue/Marge/Royaumes Sauvages, tensions par icône (point d'exclamation sur les zones à tension visible), pastilles de clans | Appui sur un nœud : fiche de zone ; « Planifier un voyage » |
| **Fiche de zone** | Région, valeur centrale (une phrase), Faveur de clans présents (sceaux), tensions visibles (titre et phrase), contrats, ville principale | Boutons : Voyager, Camper, Contrats |
| **Planification de voyage** | Route (liste d'étapes), voie, saison, météo prévue, transport (liste), provisions requises, risque, postes de voyage (4 icônes de compagnons) | « Partir » ⇒ écran d'étape |
| **Étape de voyage** | Texte court (≤ 2 lignes), image-vignette, 2 ou 3 boutons de décision, état des provisions et de la fatigue (icônes) | Décision ⇒ résultat ou entrée en zone jouée |
| **Camp** | Qualité du camp, guet (qui veille), repas, soin du familier, repos court/long | Quitter ⇒ prochaine étape ou retour |
| **Tableau de contrats** | 3 à 6 cartes (créature silhouette, mandant, prime, délai, contraintes en icônes) | Accepter ⇒ Préparation ; Refuser ⇒ conséquence éventuelle (journal) |
| **Écran Clan (hub)** | Liste des clans connus, sceaux de Faveur (5 crans), grade, appel en cours (chronomètre en jours), ressources disponibles | Ouvrir un clan ⇒ fiche, Appels, Rites |
| **Fiche de clan** | Valeur, hiérarchie (grades en escalier), avantage débloqué, hooks de quête disponibles, Ambassadeur | Accepter un hook ⇒ quête ; Demander un rite |
| **Récit (Retour au Clan)** | Décor du clan, PNJ anciens, 3 emplacements d'éléments à mettre en avant (cartes), choix de rituel | Valider ⇒ attitudes des PNJ (animation courte), puis Consignation |
| **Consignation (Carnet de chasse)** | Fiche pré-remplie, 6 à 8 leçons à choisir (2 à 3), ligne libre, cicatrices | Valider ⇒ écriture au journal ; Passer ⇒ Faveur −1 chez les Porteurs |
| **Carnet / Journal** | Frise du temps (saisons), filtre par héros/clan/région/type ; chaque entrée en 3 lignes (Acte, Trace, Conséquence) ; sync de table | Lecture seule ; entrées de table en couleur différente |
| **Boutique** | Onglets (provisions, matériaux, équipement, cartes, objets de clan), prix en éclats, qualité, indicateur de Faveur | Acheter/Vendre ; vendre déclenche la certification |
| **Obligations** | Liste des dettes (4 catégories), créancier, urgence en 3 niveaux | Honorer/Négocier/Ignorer |
| **Fiche Familier** | Voir 2.10 | Nourrir, soigner, assigner un rôle, choisir le familier actif |
| **Mini-jeu Approche** | Plein écran, 3/4 ; jauge de Confiance indirecte, cercle de tolérance | Doigt glissé lentement ; réussite/échec avec leçon |
| **Mini-jeu Ordres** | Séquences de gestes, rythme | 3 à 4 séances ; débloque des comportements |
| **Élevage (Enclos)** | Deux parents, durée, chance affichée en 3 crans (faible/moyenne/haute), résultat | « Lancer l'élevage » ; résultat au tick de saison |
| **Bilan de saison** | 3 lignes de Trinité, jalons, Faveurs en flèches, tensions en icônes | « Continuer » ⇒ nouvelle saison, sauvegarde et sync |

États de flux principaux : `saison.convocation → preparation → voyage → traque → affrontement → retour → bastion → bilan → saison+1`. Un voyage peut s'interrompre en **étape jouée** (zone 3/4) puis reprendre ; une chasse peut échouer (la créature fuit : pas de matière, Tension +2, créature revient à la saison suivante, voir Livre I).

---

## 5. Chiffres d'équilibrage de départ (à tester)

| Élément | Valeur initiale | Remarque |
|---|---|---|
| Honneur de départ | 5 (Reconnu) | Livre I : 4-6 ; Récit : ±1 à ±2 |
| Faveur de départ | clan d'origine 5 ; affinités 4 ; autres 3 ; clans en tension avec le clan d'origine 2 | échelle 0 à 10 |
| Tension de départ | 2 | échelle 1 à 10 ; pas de Tension 13+ à la démo (Livre II) |
| Gain de Faveur | Consignation +1, rendu de contrat avec clause +0,5 (cumul par demi-points), appel accepté +1, appel refusé −1, ignoré −2 | plafonné à ±2 par saison et par clan |
| Probabilité d'événement de voyage | 0,35 + 0,05 × (Tension − 3), bornes 0,15 à 0,70 | voir 2.6 |
| Provisions par étape | 1 ration et 2 eau ; chaleur ou désert : eau ×2 | prix 2 éclats / 1 éclat |
| Fatigue de route | +1 par étape ; −1 par repos long ; ≥ 3 : Endurance max −2 par étape | règle du livre |
| Prime de contrat | `10 × CR^1,5` | Nécessité ×0,8 ; Prestige ×1,5 |
| Prix d'une pièce | rareté (3 / 20 / 75 / 350 / 1 000) × qualité (1 / 1,5 / 2 / 3) × lieu (0,6 à 1,25) | éclats |
| Revenu cible par saison | ≈ 300 éclats au départ (arc 1), ≈ 700 (arc 2), ≈ 1 500 (arc 3) | dépenses ≈ 80 % |
| Prêt Marchands Libres | 100 à 500 éclats, intérêt 10 % par saison, saisie à 2 saisons de retard | seule dette en éclats |
| Dressage Approche | fenêtre de vitesse `clamp(45 − 3 × delta, 10, 45)` °/s ; Confiance 70 % pour réussite tendue, 100 % pour réussite | `delta = DD_espèce − DD_dresseur` |
| Dressage Apprentissage | 3 à 4 séances de 45 s ; DD −2 ou −3 après 3 ou 4 réussites | fidèle au livre |
| Durée minimale Phase 1 | 3 jours de monde (espèces faciles) à 14 jours (espèces difficiles) | fiche |
| Rupture | 10 jours sans soin (conditionné), 20 (affectif), jamais (symbiotique) | à tester |
| Lien | 0 à 100 ; Habituée 25, Dressée 60, Signature 85, Légendaire 100 | caché |
| Aide en combat | recharge 12 à 25 s, 1 action | selon CR |
| Élevage | perdu 15 % / moins bon 55 % / exceptionnel 30 % ; Éleveur niv. 5 : −5 pts de perdu ; niv. 10 : +10 pts d'exceptionnel | à tester |
| Couvaison d'œuf volé | 3 à 8 jours de monde | taille de l'espèce |
| Tick de saison | 12 tensions simulées au plus ; zones non visitées avancent de moitié | allège la charge |
| Durée de saison | 3 à 5 h réelles ; 12 saisons en campagne complète | 40 à 60 h |

Garde-fous : (1) tout nombre de ce tableau doit pouvoir changer **sans coder** (fichier de paramètres JSON) ; (2) simuler 12 saisons sur tableur avant de coder le tick (vérifier que le revenu ne dépasse pas les dépenses de plus de 25 %) ; (3) le joueur ne voit **jamais** Faveur, Tension, Infamie ni Lien en chiffres.

---

## 6. Portée démo (16 mars 2028) et feuille de route

**Rappel** : 1 zone, 1 chasse complète, 2-3 quêtes de plateforme. Ce chapitre fournit le **cadre autour** de cette chasse.

**Recommandation de zone** : **Marches Frontalières** (Dureth, Poste 7, Ravins de Keth), avec le clan **Porteurs de Cicatrices** comme clan de démonstration (il n'a pas d'ancrage régional, il peut donc être « amené » par le héros). Raisons : les contrats de la Guilde de Chasse y sont naturels (bourgs, postes de chasse), la tension **T14 Disparition du Convoi** est un fil d'enquête prêt à jouer (3 hooks, contrats, Ourse de Fer), les meutes de rang I-II sont dans la liste du roster (bipèdes de meute `cro`, Alizade, Dorgane), et le familier-démo (Alizade, conditionné, CR 1) est dans la même zone. Alternative : Hautes Terres Claniques (Kûrath-Shon).

**Sous-ensemble minimal v0.1 (démo)** :
1. **Journal d'événements** : collection `evenements` avec le gabarit Acte/Trace/Conséquence, 1 événement par chasse et par contrat, affichage dans le Carnet (liste simple) ; synchronisation manuelle.
2. **Contrats** : tableau de 3 contrats (1 Nécessité, 2 Contrats) avec primes de la formule, 1 clause chacun, rendu avec certification en 3 qualités (pas de Rare).
3. **Clan** : 1 clan (Porteurs de Cicatrices), grades 0 à 1 seulement, Faveur à 5 crans, **Récit** (3 éléments à mettre en avant, 4 régions-codes au plus, ici Marches) et **Consignation** pré-remplie avec 6 leçons ; 1 appel de clan scripté.
4. **Voyage** : 1 route de 3 étapes entre Dureth et un poste de chasse, provisions et eau (icônes), météo tirée sur 6 entrées, 1 étape jouée en zone 3/4, 1 camp.
5. **Familier** : 1 espèce (Alizade), 3 phases en mini-jeux simplifiés (Approche + Jalon scripté + 1 séance d'Ordres), état Habituée à Dressée, 1 action d'aide en combat (distraction), K.O. et soin, **sans élevage, sans œuf, sans monture**.
6. **Économie** : boutique unique (provisions, 3 consommables, 2 armes Standard), prime et vente, pas de prêt.
7. **Tensions** : 2 tensions simulées (T14 et T13) avec 4 étapes, tick de fin de démo.

**Feuille de route**

| Version | Contenu |
|---|---|
| v0.1 (démo, 16 mars 2028) | Voir ci-dessus |
| v0.2 | 3 clans (Porteurs, Navigateurs Gris, Mille Voix), grades 0 à 2, Appels de clan complets, 5 régions avec tables d'événements, boutique par établissement, dettes (Faveur et Compte ouvert), élevage (Enclos), vol d'œuf |
| v0.3 | Les 20 régions et les 40 tensions (horloges), carte-monde complète du continent, navire à pilote et Îlots Dispersés, monture terrestre et bête de somme, météo et saisons |
| v0.4 | 14 clans, Îles Brûlantes, familiers symbiotiques, Lien Légendaire, mort définitive optionnelle, mode « Marque Régionale » (Livre IX, option hardcore) |
| v1.0 | Continent Nord, arcs de campagne complets, synchronisation avec la table dans les deux sens |

**Jugement honnête** : les chapitres du livre qui paraissent les plus attrayants (14 clans, 40 tensions, 180 événements, élevage, 106 familiers) sont aussi les plus coûteux en **contenu** (écriture, illustration, tags) plus qu'en code. Pour un créateur seul, le risque n'est pas technique : c'est la **fabrication de contenu**. Le gabarit commun de clan et le format des tensions servent à rendre ce contenu **saisissable par des données**, mais il y aura quand même ~500 lignes de texte à écrire avant v0.3.

---

## 7. Questions ouvertes (à trancher par krunt)

1. **Un héros ou quatre à la fois ?** « Quatre personnages jouables (4 joueurs) » : si chaque partie joue **un seul héros** (les trois autres étant des compagnons PNJ), les 4 rôles de voyage et la Faveur par héros fonctionnent. Si le joueur gère une **équipe de quatre**, tout le chapitre double de charge d'interface. *Recommandation : un héros actif par partie, les autres rôles tenus par des compagnons et des familiers ; la table (MJ humain) garde la logique à quatre.*
2. **Qui sont les quatre héros ?** Les clans d'origine et affinités ne sont pas définis. *Recommandation : fixer **au moins le clan d'origine et un profil culturel** des 4 avant v0.2 ; le tableau de 2.2 est une hypothèse.*
3. **Combien de clans pour la démo ?** *Recommandation : un seul (Porteurs de Cicatrices) pour v0.1, car sa mécanique (Consignation) coïncide avec le journal.* Trois pour v0.2, quatorze à v0.4.
4. **Le joueur doit-il voir Faveur et Honneur en chiffres ?** Le Livre II l'interdit. *Recommandation : suivre le livre (crans et attitudes), et ajouter un mode « table » qui les affiche pour le MJ humain seulement.*
5. **Temps réel du calendrier.** Une saison de 3 à 5 heures est-elle bien tenable avec 14 à 24 h par semaine pour le développement ? C'est la question de **durée de jeu**, pas de production. *Recommandation : tester la boucle complète en papier (tableur) avant de coder les écrans.*
6. **Prix et économie.** Le livre ne donne aucun prix d'arme ou de service ; les formules de 2.9 sont inventées. *Recommandation : valider le tableau de revenus sur une simulation de 12 saisons avant de fixer les prix dans le JSON ; garder tout dans un fichier de paramètres.*
7. **Mort définitive des familiers.** Le livre parle de K.O. et de soin, jamais de mort. *Recommandation : pas de mort par défaut ; la **rupture** de lien et la **blessure** suffisent comme coût.*
8. **Données du roster à corriger.** (a) 28 familiers sur 106 ont `difficulte_dd: null` alors que le Livre III donne les DD (par exemple Alizade DD 12, Dorgane DD 15) ; (b) Poterne a `monture_mer` mais pas de `transport` ; (c) aucun champ `intelligence`, `oviparite`, `phases`. *Recommandation : script de backfill depuis `correspondance.json` (`ligne_livre3`) ; je le recommande avant toute implémentation du dressage.*
9. **Seuil d'intelligence légendaire.** Proposé : `intelligence ≥ 4`, `CR ≥ 10`, `lien_max` affectif ou symbiotique, Dresseur 24, Lien ≥ 85. *Recommandation : accepter ce seuil comme point de départ et le recompter après backfill.*
10. **Transport aérien et maritime.** Seuls 2 familiers volent et 3 nagent ; le passage des îles repose donc sur des **navires à pilote**. *Recommandation : assumer ce choix, et faire des montures volantes des raccourcis de fin d'arc (Wistrelle), non un transport de masse.*
11. **Phœnix : Bestiaire ou Atlas ?** Les deux versions se contredisent (quatre phœnix connus à CR 10-11 contre quelques dizaines secrets, tuer = catastrophe). *Recommandation : suivre l'Atlas (cohérent avec l'Île Cendrée et le Continent Nord) et transformer les 4 fiches du Bestiaire en liens de cycle ou événements.*
12. **Tables d'événements.** Titrées d12 mais à 9 entrées ; 180 événements à tagger. *Recommandation : n'en tagger que 5 régions pour v0.2 et compléter les cases 10-12 au besoin.*
13. **Diplomatie.** Ce chapitre prévoit la scène politique de fin de saison sans la détailler (duel verbal, Composure). *Recommandation : la traiter dans un chapitre séparé, mais réserver dès maintenant un emplacement de 15 minutes par saison dans la boucle.*
14. **Ambition de la carte.** Quatre masses, 20 régions, 40 tensions : très ambitieux pour un jeu solo tactile. *Recommandation : ne livrer **aucune carte continentale complète** avant v0.3 ; la démo n'affiche qu'une zone et une route.*

---

## 8. Ponts avec les autres domaines

- **Chasse et boss** (autre chapitre) : fournit `manière`, `jetons_utilises`, `qualite_matiere`, `cicatrices` ; ce chapitre attend ces flags pour le Récit, la Consignation et les primes ; attend aussi le slot du bouton « aide du familier » dans le HUD de chasse.
- **Bastion et métiers** (autre chapitre) : l'Enclos, l'Écurie, le Quartier Diplomatique, la Salle du Conseil et les 8 PNJ ; ce chapitre attend l'**Ancrage** (paliers), la **Phase de Bastion** et les arbres Éleveur, Dresseur, Maître des Montures, Marchand, Cartographe.
- **Diplomatie et dialogue** (autre chapitre) : duel verbal, Composure, négociation d'Ambassadeur ; ce chapitre attend des scènes appelables par `scene_id` avec issue (Faveur, Honneur, dettes) renvoyée au journal.
- **Progression et jalons** : attend la liste unique des jalons et l'arbre par métier ; ce chapitre fournit les conditions de données.
- **Données monstres** (`donnees/monstres`) : attend le backfill des champs `familier` (7 et 3.7) et la fixation des rangs ; fournit les tags `oviparite` et `intelligence`.
- **PixelForge / SceneForge / StoryForge** : sprites de familiers à 3 états (Sauvage/Habituée/Dressée : pose, collier, expression), icônes de sceaux de Faveur (14 × 5 crans), fonds de zones par région, scènes de Retour au Clan ; textes des 40 tensions et 180 événements à écrire.
- **CharForge** : doit exposer `clans.json`, `relations_clan`, `familiers_joueur` et le champ `familier` étendu ; l'export JSON de 3 doit rester stable.
- **PocketBase et table de jeu** : schéma `evenements` de 3.5 ; règle « trois champs obligatoires » ; événements `source: table` appliqués à la synchronisation suivante.
