# Mécaniques du Jeu B 02 : le Bastion, la Forge et l'artisanat

Statut : proposition de conception (2026-10-05), à valider par krunt. Les chiffres marqués « à tester » sont des valeurs de départ, pas des vérités. Les références « L1 ch. 6 » désignent Livre I, chapitre 6, etc.

Périmètre : la couche de gestion entre les chasses (Bastion, Ancrage, bâtiments, PNJ, événements, défense, sièges), la Forge, l'alchimie, la récolte, le dépeçage, l'inventaire, la progression d'artisan, et la boucle économique récolte → traitement → forge/alchimie → équipement → chasse.

## 0. Résumé en dix lignes

1. Le Bastion devient un **hub explorable en vue 3/4** avec un **menu de gestion** par-dessus. Les écrans de gestion sont des menus, pas du temps réel.
2. L'unité de temps n'est **pas le jour** mais la **Semaine de Bastion** : une Phase de Bastion = une semaine fictive. Le hub n'a pas de temps qui passe.
3. La Phase en 5 temps du Livre II (Rapport, Forge, Activités, Événement, Projection) devient une **suite de 5 écrans courts** (3 à 6 minutes réelles au total).
4. L'Ancrage 0–20 reste la jauge maîtresse. Il débloque bâtiments et PNJ. Les 18 bâtiments coûtent en tout **68 lots de matériaux** (25 Standard, 19 Supérieurs, 11 Rares, 13 Élémentaires).
5. Les jets de d20 d'artisanat deviennent un **calcul déterministe** (Score contre DD, avec une « Marge ») plus un **geste tactile optionnel** qui remplace la variance du dé.
6. La Forge est **individuelle** (0–40), le Bastion donne le bonus collectif. Un seul objet Légendaire par personnage.
7. La qualité des matériaux dépend de **comment la créature a été vaincue** : c'est le lien central entre chasse et forge (Rapport de chasse, section 2.12).
8. La **Défense du Bastion** est un mode de chasse inversé : une arène latérale où les bâtiments sont des plateformes interactives (section 2.8).
9. Les **sièges** (Livre X) sont reportés après la démo et abstraits en jauges, sans combat de masse.
10. Recommandation partie 3 : **un seul Bastion par campagne**, partagé, avec des liens PNJ, une Forge et un inventaire **par personnage** (section 2.19).

---

## 1. Ce que disent les livres

### 1.1 Le Bastion et l'Ancrage (L1 ch. 6, L2 « Phase de Bastion », L9 ch. 11 §9)

- Le Bastion est « un réseau de camps établis chasse après chasse », pas un lieu fixe. Il peut être attaqué, endommagé, détruit. Il n'est pas un mini-jeu séparé : il produit de la Tension et de l'Honneur.
- **Ancrage 0 à 20**, cinq états : 0–3 Camp provisoire, 4–7 Avant-poste, 8–12 Bastion établi, 13–17 Bastion reconnu, 18–20 Bastion légendaire.
- Montées : chasse réussie dans la région +1, construction d'un bâtiment +1, arrivée d'un PNJ notable +1, rituel d'établissement ou cérémonie de clan +1 à +2, défense réussie +2, résolution d'un conflit politique régional +2.
- Baisses : attaque non repoussée −5, abandon plus d'un arc −3, trahison publique −2, départ d'un PNJ majeur sans remplacement −1.
- Les seuils de palier (4, 8, 13, 18) exigent un **Jalon de Bastion** (L2 §3). Les points intermédiaires montent un par un.
- Capacité en bâtiments actifs : 0 (Ancrage 0–3), 3 (4–7), 6 (8–12), 10 (13–17), 18 (18–20).
- Honneur lié au Bastion : défense d'une menace notable +1 collectif, atteindre Ancrage 13 +1 permanent collectif, abandon −1 collectif, perte d'un PNJ par négligence −1 collectif.
- Affinité élémentaire du Bastion (choix à Ancrage 8+) : Feu, Eau, Terre, Métal, Bois selon le L1 ch. 6 §8 et le L2. Influe sur les matériaux disponibles, les créatures attaquantes, des bonus de rituels.

### 1.2 Temps libre et Phase de Bastion (L1 ch. 6 §3, L2 ch. « Phase de Bastion »)

- Ancrage 0–3 : **Temps Libre**, 5 activités simples (Repos complet : Vitalité +3 et Endurance pleine ; Travail de Forge : Forge +2 si matériaux ; activité sociale : Honneur ±1 ; rien : Tension −1 ; action risquée : Tension +2).
- Ancrage 4+ : **Phase de Bastion**, en **5 temps invariables** : 1 Rapport de Chasse (un joueur raconte, 1 à 3 phrases, l'audience dépend de l'Ancrage) ; 2 Dépenses de Forge collective ; 3 Activités individuelles (une par personnage) ; 4 Événement de Bastion (d20) ; 5 Projection (deux phrases, une pression ouverte).
- 10 activités du Temps 3 : Forger (Forge, 1 semaine), S'entraîner (Salle d'Entraînement, 2 semaines, jet DD de montée de rang), Rechercher (Bibliothèque/Archives, 1 semaine, révèle une faiblesse élémentaire), Cultiver (Jardin/Serre, 1 semaine, 1d4 ou 1d6 consommables selon la saison), Négocier (Quartier Diplomatique), Patrouiller (Tour de Guet, Tension −2), Tenir conseil (Salle du Conseil), Pratiquer rituel (Sanctuaire/Temple, 3 jours, Mana plein), Lire/Documenter (Salle des Mémoires, secret + ligne de Journal), Se reposer (tout camp, Vitalité et Endurance pleines, Tension −1).
- Durée : « ellipse » fixée par le MJ (une journée à une semaine, voire « le temps nécessaire »). La Phase se déclenche au **retour** d'une chasse significative (Trinité produite), à la fin d'un arc ou à un Jalon de Bastion, pas à chaque sortie.
- **Table d'événements d20** (L2 §2 Temps 4) : 20 événements (départ de PNJ, marchand de matériaux rares, créature qui rôde, messager de clan, usure d'un bâtiment, inconnu qui demande refuge, vol de ressources, etc.). Règle : l'événement doit créer une décision pour le groupe.

### 1.3 Les 18 bâtiments (L1 ch. 6 §4)

10 fonctionnels (Forge, Infirmerie, Salle d'Entraînement, Bibliothèque de Terrain, Jardin Médicinal, Salle des Archives, Tour de Guet, Quartier Diplomatique, Sanctuaire, Salle des Mémoires) et 8 culturels (Temple, Forge Élémentaire, Marché, Scène/Place Publique, Dojo, Serre Alchimique, Donjon/Salle du Conseil, Observatoire). Chacun a un Ancrage minimum, un coût en matériaux (Standard, Supérieurs, Rares, Élémentaires) et un effet. Le tableau complet traduit est en 2.5.

### 1.4 Les 8 PNJ du Bastion (L1 ch. 6 §5, L2 §4)

Forgeron, Guérisseur, Éclaireur (Ancrage 4) ; Bibliothécaire, Herboriste (8) ; Ambassadeur de Clan, Maître d'École (13) ; Artisan d'Éther (18). Chacun a une **fonction** et une **contrainte narrative** (le Forgeron part si la Forge est vide trop longtemps, « après 2 Phases sans matériaux » selon le L2 ; le Guérisseur refuse de soigner après une transgression d'Honneur ; l'Éclaireur a des dettes et peut trahir ; l'Herboriste refuse les poisons ; etc.). Ils arrivent naturellement ou par recrutement actif.

### 1.5 La Défense du Bastion (L1 ch. 6 §6, L2 §6)

« Chasse inversée » : la proie vient au groupe, pas de Désignation, la Traque est remplacée par une **Phase de Préparation défensive** à durée limitée. Avantages par bâtiment actif : Tour de Guet (pas de surprise, le groupe choisit le terrain), Forge (1 Ouverture élémentaire gratuite), Infirmerie (1 récupération de Vitalité en combat), Archives (faiblesse connue sans Jetons), Jardin/Serre (1 consommable de plus), Tour + Archives (avantage au premier jet d'initiative). Résultats : réussite totale (Ancrage +2, Honneur collectif +1), avec pertes (bâtiments endommagés, Tension +1), échec (Ancrage −5, bâtiments détruits, PNJ en fuite ou morts, Tension +3). Reconstruction : Ancrage repart de 0, bâtiments à moitié prix, première défense réussie après reconstruction = Ancrage +3 (L2).

### 1.6 Les sièges (L10 ch. 9–10)

Combat de masse (unités de 10 à 100, Vitalité d'unité 5 à 50, Moral 0–10, actions de faction) et siège en 4 phases (Investissement 1–7 jours, Pression 1–4 semaines, Assaut 1 jour, Résolution). Structure du Bastion : 20 / 40 / 70 / 120 selon l'Ancrage ; brèche à DD 10 / 14 / 18 / 22 ; machines de siège (catapulte 2d8 Structure, bélier 1d12, trébuchet 3d8, baliste 1d10 Vitalité d'unité, lance éthérique 2d10). Les PJ interviennent par missions spéciales (éliminer le commandant : Moral adverse −3 ; saboter l'artillerie ; briser un flanc ; protéger le commandant). Ravitaillement : 10–50 défenseurs 30 jours (rang 1–5), 100 pendant 60 jours (6–10), 500+ pendant 90+ (11–20). Moral de garnison : départ 7, −1 par semaine sans ravitaillement.

### 1.7 La Forge (L1 ch. 5, L2 §6, L9 ch. 6–8, L10 ch. 1–4)

- Jauge **0 à 40**, paliers de 10, **unidirectionnelle** (« la Forge ne recule jamais »). Apprenti 0–9, Ouvrier 10–19, Artisan 20–29, Maître 30–39, Légendaire 40.
- Montée de palier par moment narratif, conditions : matériau de qualité supérieure au palier, atelier adapté, contexte signifiant, enseignement d'un artisan supérieur. **Reconnaissance** obligatoire : sans regard du monde, pas de progression.
- **Un seul objet Légendaire par personnage et par carrière** : exige palier 40, Forge Élémentaire (Ancrage 13+), rituel de clan, matériaux rares d'une créature d'envergure, intention déclarée.
- Matériaux : 4 qualités (Standard : victoire rapide ; Supérieure : combat long d'usure ; Élémentaire : faiblesse exploitée ; Rare : parties précises préservées). Ils héritent de l'affinité de la créature (Feu écailles, Eau os, Terre carapace, Vent plumes, Foudre noyau). Qualité maximale selon le lieu : terrain ouvert et camp provisoire = Standard ; Bastion avec Forge = Supérieure ; Forge Élémentaire = Rare/Élémentaire stable.
- Processus en **4 étapes** : Lecture (jet ESP ou VOL), Intention, Travail (DD 10 / 15 / 20 / 25 / 30+), Reconnaissance. Résultats : critique (propriété inattendue), réussite, tendue (une propriété instable), échec (matériaux perdus ou récupérables), échec critique (incident).
- Synergies : l'arme d'École du forgeron lui-même (rang III+) donne +1 dé de dégâts ; armure adaptée à la Posture (Artisan) réduit de 1 le coût d'une Technique par session ; forger pour une autre École : DD +3. Combinaisons élémentaires : générateurs (Artisan, DD +3), contrôle (Maître, instable, option avancée).
- Équipement (L9/L10) : 14 types d'armes, 8 familles de créatures, **112 armes** (14 × 8) et **40 armures** (5 pièces × 8 familles), bonus de série à 3 et 5 pièces. Qualités d'arme : Basique −1 (forgeron 1–5), Standard (5–10), Supérieure +1 (10–15), Rare +1 et propriété (15–20), Signature +1 et propriété élémentaire (20–25), Légendaire (26–30). Usure en 3 états (Intact, Endommagé, Brisé) ; armure non entretenue après 5 combats : −1 CA. Fiche d'arme type : Grande Lame de Griffes, 1d10+1, matériaux Griffe Acérée ×3, Écaille Commune ×5, Dent Tranchante ×2, rang forgeron 8+.
- Honneur : cérémonie de clan +1 individuel, forger pour un ennemi −2, refuser un allié −1, atteindre Artisan publiquement +1 collectif, forge cérémonielle réussie +2 collectif (échec −2). Variantes régionales de forge cérémonielle (6 régions).

### 1.8 La récolte et le dépeçage (L1 ch. « Alchimie & Objets de terrain », L10 ch. 1)

- 5 types de points de récolte (plantes, minéraux, eau, insectes, épaves/ruines). Jet de récolte : échec = rien et point épuisé ; tendue (DD 10–12) = 1 commun ; réussite (13–17) = 1d4 avec chance de rare (d6 = 6) ; critique = 1d6 + 1 rare. Le point se renouvelle après 1d4 jours.
- Catalogue : 15 herbes, 8 champignons, 12 minerais, 12 insectes/divers, avec raretés ◆ à ◆◆◆◆◆ et valeurs (◆ 1–5 éclats ; ◆◆ 10–30 ; ◆◆◆ 50–100 ; ◆◆◆◆ 200–500 ; ◆◆◆◆◆ 1 000+).
- Dépeçage par famille (L10) : chaque partie du corps a une méthode, un DD, un **taux de base** (par exemple Griffes Acérées 60 %, Dent Tranchante 50 %, Gemme de Meute 10 %, Écaille Dorée 3 %). Dépeceur rang 5+ : +15 % ; **sans Dépeceur, taux divisés par 2** ; découpe ciblée en combat : −2 aux dégâts mais matériau garanti si la zone est brisée ; créature brûlée ou noyée : perte des matériaux de peau, d'organe ou solubles ; conservation de 24 à 72 h (Spectres : 4 h).

### 1.9 L'alchimie (L1 ch. 10, L9 partie IV, L10 partie II)

- Jet d'alchimie : d20 + ESP + Artisanat contre DD de formule ; tendue = 1 utilisation en moins ; échec = matériaux perdus ; critique = +1 unité. Recettes L1 : 13 potions (par exemple Potion de Soin : Herbe des Clairières + Eau Pure, DD 10, +2d4+2 Endurance), 11 bombes/pièges, 8 huiles/équipement.
- L9 : processus (Identification, Extraction, Préparation 1 à 4 h, Stabilisation, Conservation), recettes complètes par rang (soins, endurance/mana, résistances, poisons, préparations).
- L10 : **rangs alchimiques** (1–5 potions simples ; 6–10 effets prolongés ; 11–15 catalyseurs et mélange de deux bases ; 16–20 mutations et alchimie de combat ; 21–25 transmutations ; 26–30 Formule Parfaite), **qualité** (Brute −1 / Standard / Affinée +1 / Concentrée +2 / Parfaite +3, avec DD −3 à +8), **table d'effets secondaires d12**, 12 grenades (Bombe de Feu 2d6, Nova Alchimique 3d6 zone 6 m…), 8 huiles d'arme, 5 protections, 9 mutations temporaires (4 h maximum, permanentes interdites), 8 catalyseurs, 50 recettes élargies (rang 1 à 30).
- Règle d'usage : un consommable en combat coûte 1 Acte ; **10 consommables par type** au maximum en combat, le reste à la base.

### 1.10 Conflits entre livres relevés dans ce domaine, et résolution retenue

| Conflit | Résolution dans ce document |
|---|---|
| Forge collective (L1 ch. 2, L2) ou individuelle (L1 ch. 5, L8) ; 0–20 (L2) ou 0–40 (L1) | Conflit résolu par l'option 5 : **individuelle, 0–40**. Le bonus collectif passe par les bâtiments. Le tableau de DD collectif du L2 est converti (section 5). |
| Forge « jamais passive » mais Temps Libre « Forge +2 » | **Un seul mode** : points de Forge gagnés par objets reconnus (2.13), jamais en passif. Le « +2 » devient « chef-d'œuvre ». |
| Seuils d'Ancrage : 0–3/4–7/8–12/13–17/18–20 (L1, L2) contre 0–5/6–10/11–15/16–20 (L9, L10) | **L1 et L2 retenus** (les jalons 4/8/13/18 sont écrits). Zones d'influence de L9 (5/15/30 km) réutilisées pour la carte du monde. |
| Capacité 0 bâtiment à Ancrage 0–3, mais Forge et Infirmerie « Ancrage minimum 0 » | **Capacité 2 au Camp provisoire** (Forge et Infirmerie seulement). Proposition de krunt à valider. |
| Exemples du L1 (Ancrage 8 avec Forge Élémentaire, Ancrage 13 avec Salle du Conseil) | Les Ancrages minimum du tableau des bâtiments l'emportent. |
| Soins : Endurance +2d4+2 (L1) contre Vitalité +2 à +12 (L9/L10) | Conflit résolu par l'option 1 (Vitalité 4+END, petite échelle) : soins de Vitalité convertis à +1 / +2 / +3 (section 5.6). Les soins d'Endurance du L1 gardés. |
| Éléments : Vent/Foudre (forge L1) contre Bois/Métal (Bastion) | Conflit résolu par l'option 10 : Feu, Eau, Terre, Vent, Foudre, Glace ; l'affinité du Bastion devient une de ces six. Bois = Vent et Métal = Foudre pour la correspondance des bonus. |
| Niveau forgeron : Forge 0–40 (L1) contre niveau de métier 1–30 (L9/L10) | **Les deux existent** (2.13) : le niveau de métier ouvre les **recettes**, la jauge Forge plafonne la **qualité**. |
| Jardin Médicinal (Ancrage 4) exige un Herboriste qui arrive à Ancrage 8 | L'Herboriste est **recrutable par quête dès Ancrage 4** ; il arrive naturellement à 8. |
| Rang d'Atelier « Rang I–III » (Atlas), « niveaux de bâtiments » (L1), « rang 1–20 » (L10) | Une seule échelle dans le jeu : **Ancrage 0–20**. Les rangs de l'Atlas deviennent des étiquettes de ville. |

---

## 2. Traduction en jeu vidéo

### 2.1 Principes directeurs

- **Le Bastion est le seul endroit où le temps est un budget.** Partout ailleurs (plateforme, chasse) il est une action. Ici, chaque Phase offre un petit nombre de **créneaux** à répartir.
- **Pas de gestion en temps réel.** Aucun bâtiment ne produit pendant que le joueur joue. Tout se règle à la Phase. C'est ce qui rend le jeu jouable en transports et par séances courtes.
- **Un choix par créneau, un effet lisible.** Le livre le dit : « une phrase, un effet, on passe ». Chaque activité tient en une icône, une ligne de texte et une confirmation.
- **Les jets deviennent des calculs visibles.** Le joueur voit « Score 17 contre DD 13, Marge +4 » avant de s'engager. Le hasard reste pour la récolte et les événements, pas pour l'artisanat.
- **Les contraintes narratives des PNJ deviennent des variables** (compteurs, drapeaux) qui déclenchent des cartes d'événement, jamais des pénalités muettes.

### 2.2 Le temps : la Semaine de Bastion (réponse à « un jour de Bastion ? »)

Réponse : **non**, pas de jour de Bastion. Raisons : les durées fictives des livres sont en semaines (Forger 1 semaine, S'entraîner 2 semaines, Cultiver 1 semaine, saisons de 3 mois), et un jour ferait multiplier les écrans.

- **1 Phase de Bastion = 1 Semaine de Bastion.** Le calendrier du monde avance d'une semaine par Phase, plus la durée des voyages. 13 semaines par saison, 4 saisons (L10 ch. 11).
- Chaque personnage dispose de **créneaux** par Phase : **2** à Ancrage 0–3, **3** à 4–12, **4** à 13+. Un créneau = une activité. Les activités longues coûtent plus (tableau 2.4). Les activités de 2 semaines (S'entraîner) coûtent 2 créneaux, mais occupent une seule Phase.
- Un **projet long** (objet de Maître : « deux Phases », L2 exemple 2) est une barre de progression qui s'étale sur plusieurs Phases. Le personnage peut y consacrer 1 créneau par Phase.
- **Phase complète ou allégée.** Chasse avec Trinité produite (Acte, Trace, Conséquence) = Phase complète (5 temps). Chasse mineure ou quête de plateforme = **Phase allégée** : Temps 1 (rapport en une ligne) et Temps 3 seulement, soit 1 à 2 minutes.
- **Fenêtres.** Le Temps 4 ou une annonce du MJ-système peut imposer « Vous avez 1 journée » (L2 exemple 4) : la Phase passe à **1 seul créneau** par personnage et l'écran Planificateur affiche le sablier. Mécanique rare, réservée aux crises.
- **Pas de temps qui passe dans le hub.** Marcher dans le Bastion, parler, ouvrir le coffre ne consomme rien. Seules les confirmations de Phase avancent le calendrier.

### 2.3 La Phase de Bastion en 5 temps, traduite en écrans

| Temps du livre | Écran du jeu | Ce que fait le joueur | Automatisé |
|---|---|---|---|
| 1 Rapport de Chasse | **S-Rapport** : scène de dialogue courte devant l'audience (PNJ présents, Scène si construite) | Choisit un **ton** parmi 3 (honnête, modeste, grandiloquent) et 1 à 2 **faits mis en avant** (parmi ceux de la chasse : faiblesse exploitée, parties préservées, aide d'un allié, blessure d'un coéquipier) | Calcul de l'Honneur ±1 selon le code régional ; réaction des PNJ ; écriture de l'Acte dans le journal |
| 2 Forge collective | **S-Atelier** (établi commun) et **S-Chantier** | Répartit les matériaux du stock commun entre les projets des personnages ; lance ou poursuit **un seul chantier** | Contrôle des prérequis (Forge, rang, matériaux) ; arbitrage des conflits de matériaux par file d'attente |
| 3 Activités | **S-Planificateur** : une grille « personnages × créneaux » avec les icônes des activités disponibles | Remplit ses créneaux. Le jeu propose un **plan recommandé** modifiable en un tap pour les personnages non joués | Effets immédiats (Vitalité, Tension, Mana, montée de rang à jet DD) |
| 4 Événement | **S-Événement** : carte illustrée, 2 à 3 choix | Prend une décision ; peut parfois reporter | Tirage pondéré (2.7) ; application des conséquences |
| 5 Projection | **S-Projection** : résumé en 4 lignes et **une pression ouverte** | Lit, accepte, voit le calendrier | Journal PocketBase (Trace et Conséquence) ; retour au hub |

Règle d'or reprise du livre : **la Phase pose une tension, elle ne la résout pas.** Le jeu doit toujours laisser au moins un fil ouvert en Projection (quête, demande de clan, menace à la périphérie).

### 2.4 Activités individuelles : coûts en créneaux et effets de jeu

| Activité (L1) | Bâtiment | Créneaux | Effet de jeu (proposé) |
|---|---|---|---|
| Se reposer | tout camp | 1 | Vitalité et Endurance pleines, Tension −1 |
| Forger | Forge | 1 (objet ◆ à ◆◆), 2 (◆◆◆), 3 (◆◆◆◆) | Ouvre l'**Établi** (2.13) |
| Brasser (alchimie) | Jardin/Serre ou trousse | 1 | Jusqu'à 3 crafts de consommables (2.14) |
| S'entraîner | Salle d'Entraînement | 2 | Tentative de montée de rang d'École : Score contre DD du rang visé (II = 13, III = 16, IV = 20, V = 22 : à tester, calqué sur « DD max » de L9) |
| Rechercher | Bibliothèque ou Archives | 1 | Révèle la faiblesse élémentaire d'une créature déjà croisée ; choix de la créature parmi celles du journal |
| Cultiver | Jardin ou Serre | 1 | Produit des consommables : 1d4 (Été, Hiver) ou 1d6 (Printemps, Automne) |
| Négocier | Quartier Diplomatique | 1 | Honneur ±1 et création d'une **obligation** (une carte de quête de clan) |
| Patrouiller | Tour de Guet | 1 | Tension −2 et « alerte précoce » : prévient d'une menace au prochain Temps 4 |
| Tenir conseil | Salle du Conseil | 1 | Invite un clan ou un ordre : lance une quête politique |
| Pratiquer rituel | Sanctuaire ou Temple | 1 | Mana plein, rituel de Résonance (ou Légendaire au Temple) |
| Lire / Documenter | Salle des Mémoires | 1 | Secret d'une créature passée et +1 ligne de Journal |
| Temps Libre (Ancrage 0–3) | aucun | 1 | Les 5 activités du Temps Libre sont **les mêmes boutons** avec moins de choix |

Décision de conception : **un seul système** pour Temps Libre et Phase de Bastion. À Ancrage 0–3 l'écran affiche les mêmes boutons mais seulement ceux qui n'exigent aucun bâtiment. On évite ainsi deux jeux à coder. Le « Travail de Forge » du Temps Libre ouvre l'Établi de camp (qualité Standard maximum, comme le dit L1 ch. 5 §7).

### 2.5 Les 18 bâtiments traduits

Coûts en **lots** : Std = Standard, Sup = Supérieurs, Rare, Élém = Élémentaires. Durée de chantier proposée : 1 Phase (Ancrage min 0–7), 2 Phases (8–12), 3 Phases (13+). Un seul chantier à la fois ; **deux** si le joueur dispose du PNJ Forgeron (il aide).

| id | Bâtiment | Anc. min | Coût | Effet de jeu dans la Phase | Bonus Traque / Chasse | Bonus Défense |
|---|---|:-:|---|---|---|---|
| forge | Forge | 0 | Std ×5 | Débloque l'Établi (qualité Supérieure max) ; entretien auto des équipements | — | Ouverture élémentaire gratuite |
| infirmerie | Infirmerie | 0 | Std ×3 | Repos : Vitalité +2 en plus ; soins gratuits au Guérisseur | Départ de chasse avec Vitalité pleine | 1 soin de Vitalité en combat (civière) |
| entrainement | Salle d'Entraînement | 4 | Std ×4 | Active S'entraîner (jet DD) | — | — |
| biblio | Bibliothèque de Terrain | 4 | Sup ×3 | Active Rechercher | **+1 Jeton de Connaissance max à la Traque suivante (3 devient 4)** | — |
| jardin | Jardin Médicinal | 4 | Std ×3 + Herboriste | 1 consommable gratuit par Phase | — | 1 consommable en plus |
| archives | Salle des Archives | 8 | Sup ×4 | Révèle propriétés cachées des matériaux (Lecture) | **Faiblesse élémentaire connue sans dépenser de Jeton** | Faiblesse connue |
| tour | Tour de Guet | 8 | Std ×4 | Active Patrouiller ; Tension −1 passif par Phase | Retrait d'embuscades au départ ; choix du terrain en défense | Pas de surprise, choix du terrain |
| diplo | Quartier Diplomatique | 8 | Rare ×2 | Active Négocier ; +1 Honneur local | — | — |
| sanctuaire | Sanctuaire | 8 | Élém ×2 | Mana entier au repos long ; rituels de Résonance | — | — |
| memoires | Salle des Mémoires | 8 | Sup ×3 | +1 ligne de Journal ; secret de créature | Indices bonus sur créatures déjà vaincues | — |
| temple | Temple / Lieu Rituel | 13 | Élém ×3 | Rituels de Posture et de Forge Légendaires | — | — |
| forge_elem | Forge Élémentaire | 13 | Élém ×5 + Maître Forgeron | Qualité Rare/Élémentaire stable ; combinaisons Wu Xing ; Forge Légendaire | — | — |
| marche | Marché | 13 | Sup ×5 | Achat de matériaux ◆◆◆ sans chasse (stock tournant de 4 articles) | — | — |
| scene | Scène / Place Publique | 13 | Std ×6 | Rapport joué en public : +1 Honneur individuel ; rumeurs plus rapides | — | — |
| dojo | Dojo / Ring d'Épreuve | 13 | Sup ×4 | Duels d'Honneur ; épreuves de rang publiques | — | — |
| serre | Serre Alchimique | 13 | Élém ×3 + Herboriste | 1d6 consommables **élémentaires** par Phase | — | 1 consommable en plus |
| donjon | Donjon / Salle du Conseil | 18 | Rare ×5 | Événements politiques majeurs ; invitations formelles | — | — |
| observatoire | Observatoire | 18 | Rare ×4 + Bibliothécaire | Migrations de créatures visibles sur 2 régions (déverrouille des chasses rares) | Chasses rares | — |

Total des 18 : **25 Std, 19 Sup, 11 Rare, 13 Élém = 68 lots**.

**Conversion des lots.** Un lot est une **ressource abstraite**. Dans l'inventaire, chaque matériau a une étiquette de tier (Std, Sup, Rare, Élém) et une catégorie « construction » ou non. 1 lot Sup = 2 lots Std ; 1 lot Rare ou Élém ne se remplace pas. Les **éclats** peuvent payer les lots Std et Sup (Std = 7 éclats, Sup = 30 éclats, soit 150 % de la valeur marchande) mais **jamais** les lots Rare et Élém : ceux-ci viennent de chasses ou du Marché (L2 §6 : l'argent ne remplace pas les matériaux de chasse).

**États d'un bâtiment** : opérationnel, endommagé (effet réduit de moitié, réparation avec 1 lot du même tier), détruit (reconstruction à moitié prix, L1). Un bâtiment qui demande un PNJ reste **inactif** si le PNJ part (Jardin, Serre, Forge Élémentaire, Observatoire).

**Capacité** (L1) : 2 bâtiments à Ancrage 0–3 (**modification proposée**, voir 1.10), 3 (4–7), 6 (8–12), 10 (13–17), 18 (18–20). Le jeu affiche « Emplacements 3/6 » et permet de **mettre un bâtiment en sommeil** sans le détruire pour en activer un autre (change de choix stratégique gratuitement une fois par saison). Choix volontairement plus généreux que le livre : à tester.

### 2.6 Ancrage : sources, baisses, Jalons de Bastion

Table de l'Ancrage reprise telle quelle (1.1), avec trois règles de jeu :

- **Plafond par Phase** : +3 Ancrage maximum par Phase (hors défense et jalons), pour éviter qu'une chasse + un chantier + un PNJ fassent sauter un palier.
- **« Chasse réussie dans la région » compte une fois par Phase** et seulement si la chasse produit une Trinité complète.
- **Jalon de Bastion = quête scénarisée** qui bloque le franchissement des paliers 4, 8, 13, 18. Le compteur reste à N−1 tant que la quête n'est pas faite (« 3/4, jalon requis »). Les quatre jalons sont des quêtes de plateforme ou de dialogue écrites une fois.
  - Jalon 4 (démo) : escorter le futur Forgeron jusqu'au camp.
  - Jalon 8 : première visite du clan local ; le clan consulte.
  - Jalon 13 : rituel d'établissement ou conflit politique tranché.
  - Jalon 18 : événement de campagne (siège repoussé ou rassemblement).
- Baisses : jamais invisibles. À −3 d'abandon, le jeu **avertit à la Phase précédente** (« Le camp n'a pas vu de chasseur depuis 2 arcs »). La première baisse n'arrive qu'après l'avertissement.

### 2.7 Événements de Bastion (la table d20 comme cartes)

20 cartes dans `evenements_bastion.json`. Tirage pondéré selon : Tension actuelle, PNJ présents, bâtiments actifs, saison, flags du journal. Chaque carte propose **2 à 3 choix** avec coût et conséquence. Règle du livre conservée : « l'événement ne doit pas être neutre ». Ci-dessous le portage des 20 résultats (le n° est le jet d20 du livre).

| d20 | Carte | Type | Choix de jeu (résumé) |
|:-:|---|---|---|
| 1 | Offre ailleurs | PNJ | Contre-offre (éclats ou lot) / laisser partir (Ancrage −1 si majeur) |
| 2 | Marchand de matériaux rares | Économie | Acheter 1 à 3 articles (prix ×1,5) / refuser |
| 3 | Créature curieuse | Chasse | L'observer (gagne 1 Jeton pour cette espèce) / la chasser (chasse non préparée) |
| 4 | Messager de clan | Politique | Accepter la demande (quête) / refuser (Honneur −1 si Ancrage 13+) |
| 5 | Usure précoce | Bâtiment | Réparer (1 lot) / ignorer (devient « endommagé » à la Phase suivante) |
| 6 | Inconnu demande refuge | Moral | Accueillir (PNJ temporaire, risque) / refuser |
| 7 | Confidence d'un PNJ | PNJ | Écouter (lien +1) / couper |
| 8 | Rumeur | Tension | Tension +1 ; démentir (Négocier) ou assumer |
| 9 | Ancien allié | Politique | Rendre la faveur (quête) / décliner |
| 10 | Dispute de PNJ | PNJ | Arbitrer (lien +1 pour l'un, −1 pour l'autre) |
| 11 | Météo | Environnement | Un créneau d'activité extérieure perdu ; Cultiver impossible cette Phase |
| 12 | Traces d'intrusion | Menace | Patrouille (créneau) / ignorer (+1 danger pour la Défense) |
| 13 | Courrier lointain | Politique | Lire (accroche d'arc) / classer |
| 14 | PNJ blessé | PNJ | Soigner (Infirmerie) / bâtiment lié inactif 1 Phase |
| 15 | Offre d'alliance | Politique | Accepter (conditions) / refuser |
| 16 | Envoyé d'un Ordre | Politique | Recevoir (Honneur ±) / éconduire |
| 17 | Ressources disparues | Économie | Enquêter (1 créneau) / perdre 1d3 lots |
| 18 | Ennemi repéré | Menace | Prévenir (Éclaireur) / affronter (chasse de nécessité) |
| 19 | Rituel réussi | Bonus | Bonus gratuit : Mana plein pour tous, ou +1 Honneur |
| 20 | Tirage double | Méta | Deux cartes ; le joueur choisit l'ordre |

Un **événement préparé** (scénarisé par l'histoire) remplace le tirage quand la Phase suit un jalon ou une quête majeure, exactement comme dit le livre.

### 2.8 La Défense du Bastion : la proie vient à la base (mode de jeu)

**Intention.** C'est la seule chasse où le joueur **défend ce qu'il a construit**. Elle réutilise l'arène latérale de chasse (type Metal Slug) mais l'arène est **le Bastion lui-même**, vu de profil : le joueur voit sur un seul écran ses bâtiments devenus décor jouable. La perte est personnelle (bâtiments qui brûlent, PNJ en danger), ce qui crée de l'émotion à faible coût de production : l'arène est un assemblage de sprites de bâtiments déjà dessinés pour le hub.

**Déclenchement.** Trois sources : (1) **Tension 10** (« rupture », L1 ch. 2 §9) ; (2) un événement de Phase annoncé deux Phases avant (traces d'intrusion, ennemi repéré, rapport de l'Éclaireur) ; (3) une chasse précédente où la créature s'est **échappée** (L2 : « une créature qui s'échappe peut revenir »). Jamais sans avertissement (règle L2 §6). Le joueur peut **différer d'une Phase** une fois si l'avertissement est donné.

**Étape 1 : Préparation défensive** (remplace la Traque). Écran de plan : la silhouette du Bastion avec ses emplacements. Le joueur dispose de **points de préparation** (3 par défaut, comme les 3 Jetons de la Traque, +1 avec Tour de Guet) et d'un **temps limité** (60 secondes de réflexion réelles, ou illimité en mode accessibilité). Il les dépense pour :
- choisir le **terrain** parmi 2 ou 3 variantes (réservé à la Tour de Guet ; sinon terrain imposé) : Palissade, Gué, Cour centrale ;
- poser **3 types d'aménagement** : piège (Piège à Colle ou Tonnerre depuis l'inventaire), barricade (lot Std), foyer d'huile (Huile de Feu) ;
- **assigner les PNJ** à des postes (le Guérisseur à l'Infirmerie, le Forgeron à la Forge, l'Éclaireur en tour) ;
- consulter la fiche du monstre : faiblesse élémentaire **gratuite** si Archives, sinon à 1 point.

**Étape 2 : l'arène.** Défilement latéral court (2 à 3 écrans de large, pas la très longue arène de chasse) : à gauche l'entrée où arrive la créature, à droite le **Cœur du Bastion** (le foyer de l'Ancrage). Le monstre est joué comme une fiche normale (phases, attaques télégraphiées, brisures) avec deux ajouts :
- **Il frappe aussi le décor.** Ses attaques peuvent cibler les bâtiments : chaque bâtiment a des **points de Structure** et passe opérationnel → endommagé → détruit. Dégâts de structure par coup : 1 + CR÷2 (arrondi bas), plafonnés à 6, à tester. Le monstre cible d'abord le bâtiment le plus proche, sauf s'il est **attiré** (Appât Olfactif, L1 VII.c) vers un leurre.
- **Les bâtiments sont des interactions** (bouton d'action en vol d'oiseau sur l'écran, hors du joueur actif) :

| Bâtiment actif | Interaction en défense (tactile) | Coût / limite |
|---|---|---|
| Tour de Guet | Pas de surprise : le premier mouvement du monstre est télégraphié 1 seconde plus tôt ; terrain choisi | Passif |
| Forge | **Ouverture élémentaire gratuite** : une fois, le joueur peut déclencher une brisure de zone avec l'élément choisi | 1 fois |
| Infirmerie | **Civière** : appuyer sur l'icône du lit pour soigner un personnage (Vitalité +1) | 1 fois ; 2 avec Guérisseur |
| Salle des Archives | La faiblesse s'affiche en surbrillance sur le monstre | Passif |
| Jardin ou Serre | Caisse de consommables à ramasser sur le terrain | +1 consommable |
| Tour + Archives | Premier assaut du joueur : 5 secondes de **dégâts ×1,5** | 1 fois |
| Sanctuaire (proposé) | Mana +50 % au premier palier de phase du monstre | 1 fois |
| Dojo (proposé) | Ralentit la barre de Moral de la créature (si elle fuit) | Passif |

**Étape 3 : fin du combat.** Le combat prend fin quand la créature est vaincue, qu'elle **bat en retraite** (à 25 % de Vitalité elle fuit si le joueur l'a terrorisée : bruit, feu), ou quand l'une des défaites arrive : Cœur à 0 Structure, ou tous les chasseurs hors de combat.

| Résultat | Condition (proposée) | Conséquences (livre) |
|---|---|---|
| **Réussite totale** | Monstre vaincu, aucun bâtiment détruit, Cœur ≥ 50 % | Ancrage +2, Honneur collectif +1, la région apprend que le Bastion tient ; **butin de dépeçage** garanti |
| **Réussite avec pertes** | Monstre vaincu ou en fuite, au moins un bâtiment endommagé ou détruit | Réparations (matériaux), Tension +1 |
| **Échec** | Cœur à 0 ou chasseurs vaincus | Ancrage −5, bâtiments détruits, PNJ fuient ou meurent (jamais un PNJ de l'histoire principale), Tension +3 |

**Après l'échec.** Le jeu n'efface rien : Ancrage 0, **reconstruction à moitié prix**, PNJ survivants qui reviennent avec une nouvelle contrainte (L1), première défense réussie après reconstruction = Ancrage +3 (L2). Le joueur est conduit à une **scène d'arrivée** muette (décor noirci, enclume froide) puis à une Phase de reconstruction réduite aux activités sans bâtiment. L'échec est une **boucle narrative** voulue, jamais un game over.

**Difficulté.** La créature est choisie par le système : CR ≈ Ancrage ÷ 2 + 2 (Ancrage 4 : CR 4 ; Ancrage 13 : CR 8 ; Ancrage 18+ : CR 11), à tester. Une défense dure environ **5 à 7 minutes** réelles. Fréquence cible : une défense toutes les 5 à 6 Phases, soit 3 à 4 par campagne de 20 Phases.

**Coût de production.** Réutilise : sprites des bâtiments du hub, fiches de monstres existantes (donnees/monstres/*.json), système de brisures. Nouveau : barres de Structure des bâtiments, boutons d'interaction, écran de préparation. Estimation : 1 à 2 semaines de Godot une fois la chasse standard en place. À livrer **après** la démo (version 0.3).

### 2.9 Les sièges (Livre X)

**Position honnête : hors démo, et probablement hors 1.0.** Le combat de masse (unités, Moral, initiative de faction) est un jeu à part entière et n'ajoute rien à un jeu à quatre chasseurs. Proposition de traduction minimale, si krunt tient au siège comme événement de campagne :

- **Une seule séquence scénarisée par campagne** (Jalon de Bastion 18 ou fin d'arc), pas un mode répétable.
- **Phases 1 et 2 (Investissement, Pression)** = 3 à 4 **Phases de Bastion spéciales** à 1 créneau par personnage. Décisions : Ravitailler, Renforcer (lots), Envoyer un messager, Sortir en force. Deux jauges : **Structure** (20 / 30 / 40 / 70 / 120 selon l'Ancrage, mapping L1/L10 en 1.10) et **Moral de garnison** (départ 7, −1 par Phase sans ravitaillement, comme L10). Aucune simulation d'unités : l'adversaire est une barre « Pression » qui monte selon un script.
- **Phase 3 (Assaut)** = **4 mini-arènes** en défilement latéral, une par « mission spéciale » du livre : éliminer le commandant adverse, saboter l'artillerie, briser un flanc, protéger le commandant allié. Chaque réussite réduit la Pression de 25 %.
- **Phase 4 (Résolution)** applique les tables de défense (2.8).

Les machines de siège (catapulte, bélier, trébuchet, lance éthérique) sont des **décors animés** dans l'arène d'assaut, pas des unités à gérer.

### 2.10 PNJ du Bastion

Chaque PNJ est une **fiche de données** avec une fonction (bonus), une contrainte (compteur) et un **lien par personnage** (0 à 5) pour que chacun des quatre personnages ait des relations différentes (L1 : « relations différentes avec ses PNJ »).

| PNJ | Arrive | Fonction de jeu | Compteur de contrainte | Déclencheur de la carte d'avertissement |
|---|:-:|---|---|---|
| Forgeron | 4 | +1 chantier simultané ; améliore les objets des personnages en cours de Phase ; produit des objets ◆ à ◆◆ pour les stocks | `phases_forge_vide` | À 1 : avertissement ; à 2 : demande à partir (L2 « après 2 Phases ») |
| Guérisseur | 4 | Soins gratuits ; 2e civière en défense | `transgression_honneur` (action tagguée) | Refuse de soigner 1 Phase après une transgression ; réconciliation par dialogue |
| Éclaireur | 4 | Alerte précoce (Temps 4) ; +1 indice au Temps 1 de Traque | `dette` (jauge 0–5) | À 3 : une faction a un levier ; carte « trahison possible » |
| Bibliothécaire | 8 | Active Rechercher ; Observatoire | `quete_archives` | Quand un matériau rare est rapporté : demande d'accès |
| Herboriste | 8 (recrutable dès 4) | Gère Jardin et Serre ; refuse les recettes « interdit » | `recette_interdite_demandee` | Bloque les recettes taguées `interdit` (poisons) |
| Ambassadeur de Clan | 13 | Interface clan : quêtes politiques ; accès aux ressources du clan | `exigence_clan` | Une demande toutes les 3 à 4 Phases ; refus répétés = Honneur − |
| Maître d'École | 13 | Montée de rang d'École **sans jalon** | épreuve publique | Toute montée de rang déclenche une **épreuve** (duel ou test en arène courte) |
| Artisan d'Éther | 18 | Forge Élémentaire avancée ; artefacts | `attention_ordres` | +1 Tension par arc où il est actif |

### 2.11 Récolte : les quêtes de plateforme

La récolte se joue dans les **quêtes de plateforme** (cueillette, minage, ruines) et, plus rarement, en exploration 3/4.

- **Points de récolte** : 5 types du livre (plantes, minéraux, eau, insectes, ruines) avec une **icône pulsante** sur le décor. Un point utilisé est grisé jusqu'au retour au Bastion (renouvellement à la Phase, qui remplace « 1d4 jours »).
- **Résolution en 3 niveaux** (remplace le jet de récolte) : appui bref = **Commun** (1 unité) ; appui synchronisé avec un anneau qui rétrécit = **Bon** (1d4, soit 1 à 4, et 1 chance sur 6 d'un rare) ; synchronisation parfaite avec l'outil adapté (faucille, pioche, flacon) = **Parfait** (1d6 + 1 rare garanti). Les probabilités du livre sont conservées.
- **Outils** : un outil par type (faucille, pioche, flacon, filet, pince). Un outil absent = plafonné à Commun. Les outils sont des objets forgés ou achetés (Std).
- **Compétence** : les DD du livre (10–12 tendue, 13–17 réussite) deviennent la **largeur de la fenêtre** de synchronisation : Survie/Exploration/Perception élevée = fenêtre plus large. À niveau 1, fenêtre de 0,5 s ; à niveau 5, 0,9 s (à tester).
- **Familier « récolte »** : certains familiers du roster portent le rôle `recolte` ou `bete_de_somme` (par exemple Colporin, cro13). Un tel familier **ramasse un Commun à chaque point** en parallèle et ajoute **4 emplacements** de sac.
- **Danger** : ruines et zones corrompues peuvent déclencher une embuscade ou de la Corruption ; les quêtes sont l'endroit où les plateformes sont dangereuses, pas la récolte en soi.

### 2.12 Dépeçage et qualité des matériaux de chasse

**Le lien central chasse → forge** est la **qualité**. Le Livre I la définit par la manière de vaincre ; le jeu la calcule à la fin du combat à partir de quatre mesures déjà disponibles dans l'arène :

| Qualité du matériau | Condition de jeu (proposée, à tester) |
|---|---|
| **Standard** | Victoire sans condition particulière |
| **Supérieure** | Durée du combat ≥ 70 % de la durée de référence de la fiche (combat « d'usure ») **ou** ≥ 2 phases du monstre franchies |
| **Élémentaire** | ≥ 40 % des dégâts infligés avec l'élément de la faiblesse (ou ≥ 3 « Ouvertures » élémentaires réussies) |
| **Rare** | Parties « précieuses » du monstre préservées : zones marquées ne subissent aucun dégât de feu/explosion ET mort non élémentaire destructrice. Les parties **brisées** sur zones ciblées sont préservées par définition. |

Les qualités ne se substituent pas (L1) : le résultat est **par matériau**, pas par chasse, ce qui donne des chasses où seules 2 pièces sont Élémentaires. L'écran de **Rapport de chasse** (fin de combat) affiche un bilan par partie (« Écaille : Élémentaire. Griffe : Standard. Corne : brisée, préservée »).

**Le mini-jeu de dépeçage** (quelques dizaines de secondes, après le combat ; il remplace la dépense du Dépeceur) :
1. La carcasse apparaît en silhouette avec des **zones** (une par partie du catalogue de la famille : dos, griffes, mâchoire, queue, glande…).
2. Le joueur dispose d'une **barre d'outil** (6 coups de couteau au départ) et d'un **temps** (45 s).
3. Chaque zone se **trace du doigt** le long d'une ligne : précision de tracé = bonus ou malus sur le **taux** de la partie (par exemple Griffes Acérées 60 % de base : tracé parfait +20 points, raté −20 points).
4. Les parties **brisées pendant le combat** sont déjà « garanties » et n'exigent aucun coup.
5. Les parties **risquées** (queue avant mort, glandes, Spectres) exigent un **préalable** : section avant KO (déclarée en combat), neutralisation (flacon d'antidote), stabilisation (Résidu Éthérique en 30 minutes de jeu = 20 s réelles avant dégradation).

Règles du livre conservées : **sans Dépeceur dans le groupe, taux ÷ 2** (le jeu propose un **Couteau de dépeceur** acheté qui ramène à ×0,75, pour ne pas bloquer les groupes sans le métier) ; Dépeceur rang 5+ : +15 % ; créature tuée par le feu ou par noyade : parties concernées **perdues** (affichées en rouge avant la fin du combat) ; conservation : seuls les matériaux marqués `perissable` (organes, Spectres) disparaissent, **après 2 Phases** (organes) ou **à l'écran suivant** (Résidu Éthérique non stabilisé). L'alchimiste ou l'herboriste peut doubler la durée.

### 2.13 La Forge

**Deux progressions parallèles, un seul geste.**

| Quoi | Échelle | Rôle dans le jeu | Se gagne par |
|---|---|---|---|
| **Jauge Forge** (individuelle) | 0–40, paliers 10 | **Plafond de qualité**, accès à des mécaniques (nommer un objet, Forge Élémentaire) | Objets reconnus (ci-dessous) |
| **Niveau de métier Forgeron d'Armes / d'Armures** | 1–30 | **Recettes disponibles** (rang requis), bonus au Score | XP par métier (option 2 : « Chef-d'œuvre créé 300–800 XP », « Contrat de métier 100–500 ») |

Équivalence indicative entre Forge et niveau (cohérente avec L9 ch. 6 §2) : Apprenti 0–9 ≈ niveaux 1–10 ; Ouvrier ≈ 8–15 ; Artisan ≈ 15–22 ; Maître ≈ 22–29 ; Légendaire ≈ 30. Les deux avancent d'un même geste ; si l'équilibrage montre une redondance, **fusionner** (question ouverte 3).

**Gain de Forge.** Un objet forgé fait gagner de la Forge s'il est **reconnu**. Reconnaissance automatique quand : (a) la qualité de l'objet est ≥ celle de la **qualité maximale du palier** ; ou (b) c'est une **commande de PNJ ou de clan** ; ou (c) un matériau de tier supérieur au palier a été utilisé ; ou (d) un artisan de palier supérieur a enseigné. Gain : **+1** pour un objet reconnu, **+2** pour un chef-d'œuvre (Rare ou nommé), **0** sinon, avec un maximum de **+2 par Phase et par personnage** (anti-grind). Les paliers 10, 20, 30 exigent un **Jalon de Forge** (une commande scénarisée : par exemple une pièce pour un clan ennemi d'un autre) ; la jauge s'arrête à 9, 19, 29 jusque là, exactement comme l'Ancrage.

**Qualité maximale par palier** (L1 tableau « où forge-t-on », L9 ch. 6 §2) :

| Forge | Palier | Qualité d'objet maximale | Matériaux admis (qualité) | Lieu minimal |
|:-:|---|---|---|---|
| 0–9 | Apprenti | Basique, Standard | Standard ; rare ou élémentaire avec **Désavantage** (Marge −3) | Camp |
| 10–19 | Ouvrier | Supérieure | Supérieure ; élémentaire mineur stable | Forge |
| 20–29 | Artisan | Rare, Élémentaire (jusqu'à 2 éléments) | Élémentaire stable, noyaux majeurs, combinés | Forge ; **Forge Élémentaire** pour Élémentaire |
| 30–39 | Maître | Signature ; **objet nommé** | Rare, cristaux d'âme | Forge Élémentaire |
| 40 | Légendaire | **Un seul** objet Légendaire (unique par personnage) | Rare d'une créature d'envergure | Forge Élémentaire + Temple |

**L'Établi : les 4 étapes du livre en 4 écrans courts.**

1. **Lecture** (automatique) : le jeu révèle les propriétés du matériau. Sans Archives, les propriétés cachées s'affichent « ? » et ne se révèlent qu'à la forge (risque de surprise : Marge ±2). Avec Archives, tout est visible.
2. **Intention** : le joueur choisit **une orientation** sur trois : **Offensive** (+1 niveau de qualité sur la propriété d'attaque), **Défensive** (+1 sur la résistance), **Mobilité** (+1 sur Endurance ou déplacement). Pour un objet destiné à un autre personnage, il choisit à qui : forger pour quelqu'un d'une École différente donne **DD +3** si on n'a pas observé le porteur ; la **Posture** du porteur détermine l'orientation recommandée.
3. **Travail** : calcul ci-dessous, plus **geste optionnel** (chauffe en maintien, martelage au rythme, trempe au glissé) de 20 à 30 s qui produit une **Maîtrise** de 0 à 100 %. Ce geste remplace le d20.
4. **Reconnaissance** : carte de résultat (« Le clan salue »), Honneur et Forge, Trinité.

**Formule de Travail** (déterministe, à tester) :

```
Score  = 10 + mod(ESP ou VOL) + Artisanat + floor(niveau_métier / 2)
       + bonus_atelier + bonus_palier_forge + bonus_huile
       + geste, où geste = round((Maîtrise − 50) / 12,5)   [−4 à +4 ; 0 en mode auto]
Marge  = Score − DD
```

- `bonus_atelier` : camp 0, Forge +1, Forge Élémentaire +2. `bonus_palier_forge` : Apprenti 0, Ouvrier +1, Artisan +2, Maître +3, Légendaire +4. `bonus_huile` : Huile de Forgeron (L9, « +1 qualité à une forge ce jour ») +2.
- `DD` selon le rang de rareté de l'objet (L2) : ◆ 10, ◆◆ 13, ◆◆◆ 17, ◆◆◆◆ 22, ◆◆◆◆◆ 30. Ajouts : +3 combinaison générant des éléments (Artisan), +3 forger pour une autre École non observée, +2 première fois sur ce type d'objet.
- Résultat (réutilise la « réussite tendue DD..DD+4 », option 8) :

| Marge | Résultat | Détail de jeu |
|:-:|---|---|
| ≥ +10 | Réussite exceptionnelle | Une **propriété inattendue** tirée dans une liste de 3 ; Forge +1 bonus (soumis au plafond) |
| +5 à +9 | Réussite | Objet tel que prévu |
| 0 à +4 | **Tendue** | Objet fonctionnel, une propriété **instable** (−1 sur une stat ou 1 charge en moins) |
| −1 à −4 | **Hors de portée**, mais **« Forcer »** possible | Geste obligatoire ; Maîtrise ≥ 60 % : tendue ; sinon **matériaux perdus à 50 %** (récupérables avec du temps supplémentaire) |
| ≤ −5 | Impossible | Bouton grisé avec le détail du manque (« Rang 8 requis », « Forge Élémentaire requise ») |

Pas d'échec critique aléatoire : **l'incident de forge** (matériaux perdus, dégâts à l'atelier) n'existe qu'en **Forcer** ou en forge instable (Failles du Monde, Terre sans Phoenix).

**Synergies conservées.** Arme forgée par le propriétaire lui-même, École au rang III+ : **+1 dé de dégâts** et **liaison visible** (un petit emblème dans l'inventaire). Armure adaptée à la Posture (Artisan) : coût d'Endurance d'une Technique **−1 une fois par chasse** (le livre dit « par session », devenu « par chasse »).

**Éléments et Wu Xing.** Le jeu réduit les cycles à **une seule lecture** : chaque matériau a un élément ; **deux éléments générateurs** (Feu et Terre, Eau et Vent, etc., selon la correspondance 1.10) donnent une **synergie stable** (Artisan, DD +3) ; **deux éléments qui s'annulent** donnent une **Tension élémentaire** (Maître seulement : l'objet a une propriété puissante et une propriété aléatoire visible). L'anomalie du Phoenix devient un **flag de zone** : un objet à forte composante Terre forgé dans une zone instable gagne le défaut « Fissure » (−1, risque de passer Endommagé).

**Forge cérémonielle et Honneur.** Option du Temps 2 : « Forge cérémonielle » (plus long : 2 créneaux, demande un clan présent). Réussite : +2 Honneur collectif ; échec −2. Six variantes régionales = six **ambiances** de l'écran (feu de nuit, silence, cour, public, reconnaissance, instable). Même mécanique, d'autres sons et décors.

**Forge Légendaire.** Une **cinématique** (SceneForge) déclenchée au Temple, après : palier 40, Forge Élémentaire, Temple, matériaux Rares, intention déclarée (un dialogue à choix qui décide de la **propriété nommante**), rituel de clan. Un seul par personnage ; **il consomme** le personnage : sa Forge reste à 40 mais « l'investissement total » devient un **flag** (`legendaire_forge = true`) qui désactive définitivement la recette. L'objet est unique, nommé, **évolutif par usage** (chaque 5 chasses réussies avec lui, une ligne ajoutée à son histoire et une propriété mineure, jusqu'à 3).

### 2.14 L'alchimie

**Qui.** Le **Métier Alchimiste** (niveaux 1–30, rangs alchimiques de L10) pour les recettes ; les **Herboriste** et **Dépeceur** fournissent les ingrédients. Le joueur peut brasser avec une **trousse d'alchimiste** (objet de départ) n'importe où : camp, Bastion (Jardin, Serre augmentent le rendement).

**Résolution.** Même formule que l'Établi, avec `niveau_alchimiste` et `ESP + Artisanat`. DD = DD de la recette (L1/L9/L10, de 8 à 32). Résultat (rang de l'alchimiste suffisant) :

| Marge | Résultat |
|:-:|---|
| ≥ +10 | **+1 dose** (critique du livre) |
| +5 à +9 | Lot standard |
| 0 à +4 | **Tendue** : 1 dose en moins ou 1 utilisation en moins (comme L1) |
| < 0 | Recette non brassable (aucun échec par hasard), **sauf** en mode risque |

**Taille de lot.** Un craft produit **2 doses** pour les recettes ◆ (rang 1–10), **1 dose** pour les rangs 11+ (grenades, mutations). À tester : l'objectif est de ne pas faire brasser 40 fois la même potion.

**Qualité alchimique** (L10) : Brute (DD −3, effet −1, durée ×0,5), Standard, Affinée (+3 DD, effet +1, durée ×1,5), Concentrée (+5 DD, effet +2, ×2), Parfaite (+8 DD, rang 20+, +3, ×3, sans effet secondaire). Le joueur choisit la **qualité cible** avant de brasser ; la Marge dit si c'est possible. Brute est le mode « consommable de masse ».

**Mélange de bases** (rang 11+, mode « risque ») : deux potions combinées, DD = somme ÷ 2 arrondi supérieur. Le geste est un **mini-jeu d'instabilité** (barre à maintenir entre deux seuils). Succès : effet combiné, durée ÷ 2. Échec : **effet secondaire** (table d12 du L10). Dans la démo et en 1.0, **seuls 6 effets** sont retenus (explosion légère, fumée toxique, potion inversée, odeur persistante, rien, potion miraculeuse) ; le reste est cosmétique.

**Consommables en chasse.** Ceinture de combat de **4 emplacements rapides** (L1 : 10 par type max). Utiliser = tap sur l'icône, animation 0,6 s et **partage de recharge** de 3 s entre consommables (empêche l'enchaînement d'un tas de potions). Les huiles s'appliquent **hors combat** ou en action courte (3 rounds de combat devient **20 secondes**). Les grenades se lancent à 10 m (portée du L10) : visée par glissement, parabole affichée.

**Éthique et verrous.** Les recettes de poison portent le tag `interdit` (bloquées si l'Herboriste est au Bastion et en désaccord) ; les **mutations permanentes** sont interdites : une seule recette (Élixir de Transmutation, Formule Parfaite) est réservée au Grand Maître et déclenche un **Handicap** moral, comme L10. Premier pas simple : ne pas implémenter les mutations en démo.

### 2.15 Équipement : armes, armures, séries, usure

- **112 armes et 40 armures**, c'est un catalogue de données, pas de contenu à animer : chaque arme réutilise l'un des **6 jeux d'animation** de combat (voir `livres-crs-vers-jeu-b.md`). Seule l'**icône** et les statistiques changent. La génération se fait par **script** à partir d'un tableau « type d'arme × famille ».
- **Familles de créatures** : les 8 familles du L10 correspondent aux groupes du roster refondu (Bipèdes de meute, Grandes volantes A et B, Aquatiques, Terrestres, Cuirassées, Fauves sacrés, Dragons Anciens en matériaux de cinématique). La correspondance est dans `donnees/monstres/correspondance.json` (à compléter par un outil).
- **Bonus de série** : 3 pièces et 5 pièces d'une même famille (tableau L10 ch. 4). Affiché dans l'écran Équipement par une icône de pièces (3 puis 5 petits losanges) ; le bonus s'allume quand la pièce correspondante est portée.
- **Usure** simplifiée en **compteur d'entretien** de 0 à 3 par pièce : +1 par chasse intense (arme) ou par 5 chasses (armure, L9). À 3 : **Endommagé** (−1 dégât, pas d'effets spéciaux ; −1 CA). **Brisé** = hors service. L'**entretien est automatique** pendant la Phase si une Forge est active (coût de 5 éclats ou 1 lot Std par pièce). Sans Forge : réparation payante chez un PNJ de passage, ou « Brisé » assumé.
- **Armures hybrides** (rang 20+) et **amélioration** (rang 15+, une fois par armure) : réservées à la version 1.0.
- **Reliques** (rang 25–30) : objets d'histoire donnés par quêtes ; non forgeables.

### 2.16 Inventaire et stockage tactile

Trois contenants, un seul geste (glisser-déposer) :

| Contenant | Taille de départ | Extensions | Règles |
|---|:-:|---|---|
| **Sac de chasse** (porté) | 16 emplacements (grille 4×4) | +4 familier « bête de somme » (par exemple Colporin) ; +4 sac renforcé (Std) | Piles : matériaux 99, consommables 10 par type (L1) ; pas de poids, pas d'encombrement |
| **Ceinture de combat** | 4 emplacements rapides | +1 à Ancrage 8, +1 à 13 | Seul contenant utilisable en chasse (tap) |
| **Coffre du Bastion** (partagé) | 60 emplacements | +20 par palier d'Ancrage atteint (4, 8, 13, 18), soit 140 au maximum | Tri automatique ; « envoyer au coffre » à l'arrivée au Bastion |

- **Tri et lisibilité.** Cinq onglets aux icônes (Matériaux, Consommables, Équipement, Recettes, Objets d'histoire) ; **filtre rapide** par élément (puce colorée) et par qualité. Chaque matériau affiche un petit losange de rareté ◆ à ◆◆◆◆◆ et la bordure de **qualité** (4 teintes).
- **Équipement à l'écran Établi.** Les matériaux requis d'une recette s'affichent en lignes « 3/3 Griffe Acérée (Standard) », colorées si la quantité manque ; un bouton « ← prendre du coffre » compense en un tap.
- **Interdits.** Pas de gestion de poids, pas de durée de conservation sauf `perissable`, pas de sac à malice. C'est du **stockage**, pas de la survie. Les règles de faim, de soif, de chaleur (L10 ch. 12) sont **hors périmètre** de ce chapitre (voir ponts).

### 2.17 Les trois jauges d'artisanat

L'intitulé est ambigu dans le brief. J'interprète « trois jauges d'artisanat » comme les **trois jauges persistantes qui encadrent la couche artisanat/Bastion** (voir question 14 si krunt pensait à autre chose) :

| Jauge | Portée | Échelle | Rôle dans l'artisanat |
|---|---|---|---|
| **Forge** | Individuelle | 0–40, unidirectionnelle | Plafond de qualité, accès aux mécaniques (2.13) |
| **Ancrage** | Collective (Bastion) | 0–20, monte et descend | Bâtiments, capacité, PNJ, plafond de qualité par lieu |
| **Tension** | Collective (monde) | 0–10 (5 seuils) | Visibilité : une Forge active et visible la fait monter légèrement ; à 10 elle déclenche une **attaque de Bastion** |

Les trois sont **des barres fixes** dans le HUD du hub (360 px de haut : 3 barres de 6 px dans le coin supérieur, étiquetées par une icône : marteau, ancre, œil). L'Honneur (0–10), qui touche aussi le Bastion et la Forge, reste une jauge individuelle gérée dans la fiche de personnage (voir `01-...` si ce chapitre existe).

### 2.18 La boucle économique : récolte → traitement → forge/alchimie → équipement → chasse

```
[Quêtes de plateforme]  récolte de plantes, minerais, eau, insectes (outils)
        |  matériaux communs + peu communs
[Chasse]  dépeçage -> matériaux de créature (qualité Standard/Sup/Élém/Rare)
        |
[Retour au Bastion]  Rapport + stock commun + Coffre
        |
[Traitement]  (1) tri automatique ; (2) stabilisation des périssables ;
              (3) raffinage « lots » : Pierre Commune, Os, Cuir -> lots Std
        |
[Atelier]  Forge (armes, armures, huiles de forge)  |  Alchimie (potions, bombes, huiles)
        |   dépense des créneaux
[Équipement et consommables]  Ceinture 4 emplacements, armure, arme, huiles
        |
[Chasse suivante]  Traque (Jetons, Bibliothèque +1, Archives), départ avec Vitalité pleine
        |
(retour)
```

**Traitement** : étape volontairement légère. Elle ne coûte **aucun créneau** : à l'arrivée au Bastion, le jeu applique : tri, stabilisation automatique des périssables si Archives ou Herboriste, **raffinage** de matériaux bruts en lots (le joueur voit « +4 lots Std » dans le Rapport). C'est ici que **les lots de construction** se fabriquent : tout matériau de catégorie « construction » (pierre, os, bois, cuir, écailles) donne ses lots. Un matériau **de recette** (Griffe Acérée, Gemme de Meute…) ne se transforme pas en lot.

**Boucles de rétroaction** (le cœur de l'économie) :

1. **Chasse bien menée** → matériaux de qualité haute → objets de qualité haute → chasses plus faciles → matériaux plus rares.
2. **Chasse médiocre** → matériaux Standard → équipement Basique → chasse plus dure : la **boucle de rattrapage** est la défense (qui fournit du butin garanti) et le Marché (matériaux ◆◆◆ à prix ×1,5, à partir d'Ancrage 13).
3. **Éclats** : revenu des contrats et des ventes de surplus ; **dépenses** : lots Std/Sup, entretien, Marché. Pas de progression achetable (règle L2) : aucun éclat n'achète de Forge ni de niveau.
4. **Tension** : une Forge active la fait monter, les patrouilles la font baisser. Trop de Tension → défense du Bastion → **butin supplémentaire** mais risque d'Ancrage −5 : le **risque** a un prix et une récompense.

### 2.19 Partie 3 : quatre personnages, un Bastion partagé ou un par personnage ?

**Recommandation : un seul Bastion par campagne, partagé, avec trois couches individuelles.** Raisons :

- **L'histoire est unique** (décision krunt) et le livre dit « cet onglet est collectif : tous les PJ partagent le même Bastion » (L1 ch. 6 §9).
- Quatre Bastions = **4 fois le contenu** (bâtiments, PNJ, événements, défenses) pour un petit studio d'une personne. Impossible à tenir.
- Un Bastion partagé permet de **compter l'Ancrage une fois** et de conserver la logique « un groupe qui construit ensemble », au cœur du Livre I.

| Donnée | Portée | Pourquoi |
|---|---|---|
| Ancrage, bâtiments, Structure, Coffre, Tension | **Collective** | C'est le Bastion |
| Forge, niveau de métier, recettes connues, sac, ceinture | **Individuelle** | Option 5 ; chacun a ses métiers (2 max) |
| Honneur | **Individuelle** (0–10) avec un « Honneur de groupe » dérivé en lecture seule | Évite le flou L1 (« Honneur collectif » non défini) |
| Liens avec les 8 PNJ | **Par personnage** (0–5) | « relations différentes » (L1) |
| Affinité élémentaire du Bastion | **Collective**, choisie à Ancrage 8 | Un seul vote |
| Créneaux de Phase | **Par personnage** | Chacun planifie |
| Familier | Par personnage (sauf Bête de somme qui augmente son propre sac) | Dressage individuel |

**Modes de jeu.** Selon la décision de krunt sur « 4 joueurs » :
- **Un joueur qui incarne les quatre tour à tour** (histoire unique à quatre protagonistes) : la Phase est préparée pour les quatre mais **le joueur n'agit qu'avec le personnage actif**, les autres suivent un **plan recommandé** (accepté en un tap). En démo : **un seul personnage actif**, les autres absents.
- **Quatre joueurs en coopération locale ou en ligne** : chaque joueur règle sa grille de créneaux ; la Phase avance quand tous sont prêts ; le **conflit de matériaux** (L2) est arbitré par vote. Techniquement réalisable, mais non recommandé pour la 1.0.

**Divergences par personnage** (pour que quatre personnages se sentent différents sans quatre Bastions) : l'**origine** (20 régions, L8) donne un bonus de métier (par exemple Hautes Terres Claniques : forge cérémonielle de nuit) ; les **affinités de clan** donnent accès à des PNJ spécifiques (un envoyé de clan différent par personnage) ; les **métiers** ouvrent des activités propres (Forgeron, Alchimiste, Herboriste, Dépeceur, Cartographe). Le Bastion devient **le lieu de croisement** des quatre histoires.

---

## 3. Modèle de données

Tables proposées pour PocketBase / CharForge (JSON). Les identifiants sont des `id` courts stables ; les clés de roster (`cro01`…) viennent de `donnees/monstres/`.

### 3.1 `materiaux`

```json
{
  "id": "mat_griffe_acree",
  "nom": "Griffe Acérée",
  "categorie": "creature",             // plante | champignon | minerai | insecte | eau | creature | construction
  "famille_source": "crochues",        // groupe du roster
  "tier_construction": null,           // "std" | "sup" | "rare" | "elem" si utilisable comme lot
  "rarete": 1,                         // ◆ x n
  "valeur_eclats": [1, 5],
  "affinite": "neutre",                // feu | eau | terre | vent | foudre | glace | ombre | ether | neutre
  "perissable_phases": 0,              // 0 = non périssable ; 2 = organes
  "pile_max": 99,
  "partie_corps": "pattes_avant",      // pour dépeçage
  "taux_base": 0.60,
  "dd_decoupe": 10,
  "rang_depeceur_min": 0
}
```

### 3.2 `qualite_materiau` (instance dans l'inventaire)

```json
{ "materiau": "mat_griffe_acree", "qte": 3, "qualite": "superieure", "origine": {"chasse_id": "ch_0003", "monstre": "cro02"} }
```
`qualite` ∈ standard | superieure | elementaire | rare.

### 3.3 `recettes`

```json
{
  "id": "rec_lame_meute_std",
  "type": "arme",                      // arme | armure | accessoire | huile | consommable | bombe | mutation
  "famille": "crochues",
  "arme_type": "grande_lame",          // un des 14 types
  "nom": "Grande Lame de Meute",
  "dd_base": 13,
  "rang_requis": 3,                    // niveau de métier
  "palier_forge_min": 0,
  "metier": "forgeron_armes",
  "ingredients": [
    {"materiau": "mat_griffe_acree", "qte": 3},
    {"materiau": "mat_ecaille_commune", "qte": 5},
    {"materiau": "mat_dent_tranchante", "qte": 2}
  ],
  "resultat": {"equipement": "arme_grande_lame_meute", "qualite": "standard"},
  "tags": ["demo"],
  "creneaux": 1,
  "sources": "L10 ch. 2 §2 (rang 8, rabaissé pour la démo)"
}
```

### 3.4 `equipements`

```json
{
  "id": "arme_grande_lame_meute",
  "type": "arme", "arme_type": "grande_lame", "ecole": "coup_final",
  "degats": "1d10", "mod_qualite": 0, "affinite": null,
  "propriete": {"id": "tranchant_mortel", "texte": "Critique : saignement +1/round pendant 3 rounds"},
  "durabilite_max": 3,
  "famille": "crochues",
  "serie": {"famille": "crochues", "pieces_3": "init_+1d4", "pieces_5": "appel_meute"}
}
```
Pièce d'armure : `{"id":"armure_meute_heaume","slot":"heaume","ca":1,"resistance":null,"faiblesse":"feu","propriete":"Perception de Meute"}` ; bonus de série dans `series`.

### 3.5 `batiments`

```json
{
  "id": "forge",
  "nom": "Forge",
  "type": "fonctionnel",
  "ancrage_min": 0,
  "cout": {"std": 5},
  "pnj_requis": null,
  "chantier_phases": 1,
  "effets": [
    {"cle": "atelier.qualite_max", "valeur": "superieure"},
    {"cle": "atelier.bonus_score", "valeur": 1},
    {"cle": "entretien.auto", "valeur": true}
  ],
  "bonus_chasse": [],
  "bonus_defense": [{"cle": "defense.ouverture_elementaire_gratuite", "valeur": 1}],
  "structure_max": 8,
  "activites": ["forger"]
}
```
`structure_max` (proposé) : 6 pour un bâtiment Std, 8 Sup, 10 Rare/Élém ; ×1,5 avec Tour de Guet voisine (à tester).

### 3.6 `bastion_etat` (par campagne)

```json
{
  "campagne_id": "camp_001",
  "ancrage": 3,
  "jalons_valides": [],
  "tension": 2,
  "affinite": null,
  "batiments": [
    {"id": "forge", "etat": "operationnel", "sommeil": false, "structure": 8},
    {"id": "infirmerie", "etat": "chantier", "phases_restantes": 1}
  ],
  "chantier_actif": "infirmerie",
  "stock_lots": {"std": 4, "sup": 0, "rare": 0, "elem": 0},
  "eclats": 85,
  "semaine": 7,
  "saison": "printemps",
  "derniere_attaque": null
}
```

### 3.7 `pnj_bastion`

```json
{
  "id": "forgeron",
  "arrive_ancrage": 4,
  "fonction": ["chantier.+1", "forge.improve"],
  "contrainte": {"cle": "phases_forge_vide", "seuil_avert": 1, "seuil_depart": 2},
  "liens": {"perso_a": 2, "perso_b": 0},
  "present": false
}
```

### 3.8 `evenements_bastion`

```json
{
  "id": "evt_marchand_rare",
  "poids": 5,
  "conditions": {"ancrage_min": 4, "tension_max": 8},
  "titre": "Un marchand de matériaux rares",
  "choix": [
    {"id": "acheter", "cout": {"eclats": 120}, "effets": [{"stock": "mat_gemme_meute", "qte": 1}]},
    {"id": "refuser", "effets": []}
  ]
}
```

### 3.9 `artisan_perso` et `phase_log`

```json
{ "perso_id": "perso_a", "forge": 4, "forge_legendaire_faite": false,
  "metiers": [{"id": "forgeron_armes", "niveau": 3, "xp": 612}, {"id": "alchimiste", "niveau": 1, "xp": 60}],
  "recettes_connues": ["rec_potion_soin", "rec_lame_meute_std"] }
```
```json
{ "phase_id": "ph_0012", "semaine": 7, "type": "complete",
  "acte": "Chasse de Dorgane, 2 phases franchies",
  "trace": {"forge": ["arme_grande_lame_meute"], "batiments": ["forge"]},
  "consequence": {"ancrage": "+1", "tension": "-1", "evenement": "evt_traces_intrusion"} }
```
Ce `phase_log` alimente le **journal PocketBase** (Trinité) : un document par Phase.

---

## 4. Interfaces et flux

Tous les écrans sont conçus pour un affichage de **360 px de haut**. Cibles tactiles **≥ 40 px** de côté logique (≈ 48 dp). HUD du hub : les trois barres (Forge, Ancrage, Tension) en haut ; le calendrier (semaine, saison) en haut à droite.

### 4.1 Liste des écrans

| Écran | Rôle | Contenu et actions |
|---|---|---|
| **S01 Hub Bastion** | Exploration 3/4 | Marcher, parler aux PNJ, entrer dans les bâtiments. Bouton ☰ (menu). Bouton « Partir en chasse » (passe par la Désignation). |
| **S02 Carte des bâtiments** | Gestion du Bastion | Plan en tuiles : emplacements 3/6, icônes des 18 bâtiments (verrouillés en gris avec leur Ancrage min). Tap : fiche. |
| **S03 Fiche bâtiment** | Détails | Coût, effets, PNJ requis, bonus de chasse et de défense. Boutons : Construire, Mettre en sommeil, Réparer. |
| **S04 Rapport de chasse** (écran de fin de chasse) | Récolte, Récit | Bilan des matériaux par partie et qualité ; mini-jeu de dépeçage ; puis dialogue de Rapport. |
| **S05 Planificateur** | Temps 3 | Grille créneaux × personnages ; icônes d'activités ; plan recommandé. |
| **S06 Atelier / Établi** | Forge | Choisit une recette ; glisse les matériaux ; voit Score, DD, Marge ; Intention ; geste ; Reconnaissance. |
| **S07 Alchimie** | Brassage | Liste de recettes ; qualité cible ; lot ; geste d'instabilité pour les mélanges. |
| **S08 Inventaire** | Sac, ceinture, coffre | Onglets, glisser-déposer, tri, filtres. |
| **S09 Équipement** | Armes, armures, séries | Jauge d'entretien par pièce, bonus de série, comparatif. |
| **S10 Carte d'événement** | Temps 4 | Illustration, texte court, 2 à 3 boutons. |
| **S11 Projection** | Temps 5 | Résumé en 4 lignes, pression ouverte, calendrier ; bouton « Continuer ». |
| **S12 Fiche PNJ** | Dialogue, liens | Portrait, lien 0–5, besoin du moment, services. |
| **S13 Préparation défensive** | Défense | Plan du Bastion, points de préparation, postes des PNJ, fiche du monstre. |
| **S14 Arène de défense** | Combat | Défilement latéral court ; boutons d'interaction des bâtiments. |
| **S15 Cinématique de Forge Légendaire** | Événement | Dialogue de l'intention, scène, nom de l'objet. |
| **S16 Récolte (HUD plateforme)** | Quêtes | Anneau de synchronisation, outil actif, compteur du sac. |

### 4.2 Machine à états de la couche Bastion

```
HUB_LIBRE
  |-- (Partir en chasse) --> DESIGNATION --> TRAQUE --> CHASSE --> RAPPORT_CHASSE
  |-- (Quête de plateforme) --> QUETE --> RETOUR_LEGER --> PHASE_ALLEGEE
  |-- (Attaque annoncée ou Tension 10) --> PREPARATION_DEFENSIVE --> ARENE_DEFENSE --> RESULTAT_DEFENSE
RAPPORT_CHASSE --> PHASE_RAPPORT --> PHASE_ATELIER --> PHASE_ACTIVITES --> PHASE_EVENEMENT
              --> PHASE_PROJECTION --> HUB_LIBRE (calendrier +1 semaine)
PHASE_ALLEGEE = RAPPORT (1 ligne) --> ACTIVITES --> PROJECTION
RESULTAT_DEFENSE --> (réussite ou pertes) --> PHASE_ATELIER (réparations) --> HUB_LIBRE
                 --> (échec) --> SCENE_ARRIVEE_RUINES --> PHASE_RECONSTRUCTION
```

Transitions clés : **sauvegarde automatique** au passage de chaque temps. Le joueur peut quitter l'appli à tout moment sauf pendant ARENE_DEFENSE (reprise au début de l'arène).

### 4.3 Écran S06 Établi, détail

- Gauche : la **recette** (nom, icône, rang requis, DD).
- Centre : **trois colonnes** « Matériaux requis », « Ajout optionnel (huile, catalyseur) », « Intention ».
- Droite : **bloc de résultat prévu** (Score, DD, Marge avec code couleur : rouge < 0, orange 0–4, vert 5+, or 10+) et deux boutons : « Forger vite » (mode auto) et « Forger (geste) ».
- Bas : barre de **créneaux** restants.
- Après le geste : **carte de Reconnaissance** (« Le Forgeron hoche la tête : +1 Forge ») ; si palier à franchir : « Jalon de Forge requis : Commande de clan ».

### 4.4 Parcours type d'une Phase complète (durée visée : 4 à 6 minutes)

Dorgane vaincu en 2 phases. S04 : bilan (Écaille : Supérieure, Griffe : Standard, Corne brisée garantie), dépeçage 35 s, choix du ton au Rapport. S05 : 3 créneaux ; le joueur choisit Forger (1), Brasser (1), Se reposer (1). S06 : Lame de Meute en Marge +4 (tendue) ou geste à 80 % pour +2 de Score. S10 : carte « Traces d'intrusion », choix Patrouille (créneau suivant) ou ignorer. S11 : « Forge 3/40. Armure d'Alizade à fabriquer. Traces confirmées au nord. » Retour hub.

---

## 5. Chiffres d'équilibrage de départ (à tester)

### 5.1 Rythme global

| Élément | Valeur de départ | Commentaire |
|---|---|---|
| Une Phase complète | 4 à 6 minutes réelles | L2 : 5 à 20 minutes à la table, trop long en solo |
| Une Phase allégée | 1 à 2 minutes | |
| Cycle « quête + chasse + Phase » | 25 à 35 minutes | séance mobile typique |
| Phases par campagne | 20 à 25 | ≈ 6 mois fictifs (13 semaines par saison) |
| Cadence de défense | 1 toutes les 5 à 6 Phases | 3 à 4 par campagne |
| Ancrage visé après N Phases | 4 après 3, 8 après 8, 13 après 13, 18 après 20 | Plafond +3 par Phase |

### 5.2 Départ du joueur (démo)

- **Éclats** : 100. **Lots** : 6 Std (suffit à la Forge, +1 de reste). **Sac** : 3 Potions de Soin (Herbe des Clairières + Eau Pure), 1 Antidote, 2 Huiles d'Aiguisage, trousse d'alchimiste, Couteau de dépeçage (×0,75), faucille, pioche.
- **Jauges** : Forge 0, Ancrage 0, Tension 1. **Niveaux de métier** : 1.
- **Un seul chantier** : la Forge (1 Phase). L'Infirmerie suit.

### 5.3 Prix et conversions

| Rareté | Valeur (livre) | Lot (jeu) |
|---|---|---|
| ◆ Commun | 1–5 éclats | Std : 5–7 éclats si achat direct |
| ◆◆ Peu commun | 10–30 | Sup : 30 éclats |
| ◆◆◆ Rare | 50–100 | Rare : non achetable avant le Marché |
| ◆◆◆◆ Très rare | 200–500 | — |

Valeur de revente d'un surplus : **50 %** de la valeur du livre (0 pour les organes périssables).

### 5.4 Récolte

| Mesure | Départ |
|---|---|
| Points de récolte par quête de plateforme | 10 à 14 |
| Rendement moyen d'un point | Commun 1,0 ; Bon 2,5 ; Parfait 4,0 (+1 rare) |
| Taux de Bon au premier essai (niveau 1) | ≈ 50 % |
| Chances de rare sur Bon | 1/6 (livre) |
| Récolte typique d'une quête | ≈ 28 unités + 1 à 2 rares |

### 5.5 Dépeçage

- Taux de base : tableaux du L10 ch. 1 (par exemple 60 %, 50 %, 35 %, 10 %).
- Modificateurs : Dépeceur niveau 5+ **+15 points** ; sans Dépeceur **×0,5** (×0,75 avec Couteau) ; tracé parfait **+20 points**, raté **−20 points** ; plafond 95 %.
- Une chasse ◆◆ (CR 4–5) produit **6 à 9 parties**, dont **2 garanties** (brisures) ; Rare (◆◆◆) **9 à 12**.

### 5.6 Soins et consommables (conversion à la petite échelle de l'option 1)

| Objet | Livre | Jeu (départ) |
|---|---|---|
| Potion de Soin (Endurance) | +2d4+2 (moyenne 7) | **+6 Endurance** (sur 10) |
| Méga-Potion | Endurance pleine | Endurance pleine |
| Potion de Vitalité | +1 Vit (L1) | **+1 Vitalité** |
| Potion de Vitalité supérieure | +2 Vit | **+2 Vitalité** |
| Élixir de Récupération / Grand Élixir Vital (L9) | +5 / +12 Vit | **+2 / +3 Vitalité** |
| Antidote | retire EMPOISONNÉ | idem |
| Bombe de Feu | 2d6 feu | **8 dégâts** (valeur moyenne) en zone |
| Huile d'Aiguisage | +1 attaque, 1 h | **+1 dégât**, durée d'une chasse |

### 5.7 Forge

- **Score type** : niveau 1, ESP 2, Artisanat 3, camp : 10 + 2 + 3 + 0 + 0 + 0 = **15** contre DD 10 (Marge +5, réussite) ou DD 13 (+2, tendue). **Niveau 10 en Forge Élémentaire, Artisan** : 10 + 3 + 4 + 5 + 2 + 2 = **26** contre DD 22 (+4, tendue) ou DD 17 (+9, réussite).
- **Gains de Forge** : +1 ou +2 par objet reconnu, plafond +2 par Phase. **Vitesse cible** : Ouvrier (10) après 6 à 8 Phases, Artisan (20) après 14 à 16 Phases, Maître (30) après 24+ (donc **hors 1.0** pour la plupart), Légendaire hors portée d'une campagne de 20 Phases. Si krunt veut la Forge Légendaire dans la campagne, **réduire** les paliers ou allonger.
- **XP du métier** par objet (L10) : 300 à 800 pour un chef-d'œuvre ; viser niveau 8 à la fin de la campagne.

### 5.8 Bastion

- **Coût total** de 68 lots. À Ancrage 8 (6 bâtiments Std/Sup typiques) ≈ 22 lots ; à 13 (10 bâtiments) ≈ 42 lots ; à 18 (tous) 68 lots.
- **Structure** du Bastion (L10, remappée sur les états L1) : 20 (0–3), 30 (4–7), 40 (8–12), 70 (13–17), 120 (18–20). Structure des bâtiments : 6 (Std), 8 (Sup), 10 (Rare/Élém).
- **Dégâts de structure** d'une attaque de monstre : 1 + CR÷2 (arrondi bas), plafonné à 6.
- **CR du monstre en défense** : CR ≈ Ancrage ÷ 2 + 2.
- **Éclats de défense réussie** : 80 + 15 × CR (butin en plus).

### 5.9 Alchimie

- Lot : 2 doses (rangs 1–10), 1 dose (11+).
- **DD** : de 8 à 32 selon L1/L10. À niveau 5 : Score ≈ 10 + 2 + 3 + 2 + 1 = 18 : toutes les recettes ≤ DD 13 en réussite pleine.
- Délai de brassage (L9 : 1 à 4 h) : **non simulé**, absorbé par le coût de 1 créneau.

---

## 6. Portée démo (16 mars 2028) et feuille de route

### 6.1 Démo : le sous-ensemble minimal

**À implémenter d'abord (par ordre) :**

1. **Hub Bastion** sans PNJ animés (un seul écran 3/4, 2 bâtiments visibles) et le **menu** de gestion (S02, S03).
2. **Ancrage 0 à 4** avec 1 Jalon (escorte du Forgeron). Bâtiments : Forge (Std ×5) et Infirmerie (Std ×3). Le Forgeron arrive à 4.
3. **Rapport de chasse** : bilan par partie et qualité de matériau (S04) ; **dépeçage simplifié** (4 zones, sans mini-jeu : appui par zone, résultat selon un taux).
4. **Phase de Bastion allégée** : Temps 1 (1 ligne), Temps 3 (Planificateur avec 4 activités : Se reposer, Forger, Brasser, Patrouiller si Tour), Temps 5. **Pas de Temps 4** en démo sinon 3 cartes seulement.
5. **Établi** avec la formule de Marge, **mode auto uniquement** (pas de geste) ; 4 recettes : Potion de Soin, Antidote, Huile d'Aiguisage, Grande Lame de Meute ; 1 set d'armure (Alizade) de 5 pièces avec bonus de série à 3.
6. **Inventaire** : sac 16, ceinture 4, Coffre 60 ; filtres minimum.
7. **Récolte** : 1 quête de cueillette (10 points, 3 types), résolution en 2 niveaux.
8. **Journal PocketBase** : un document par Phase.

**Hors démo** : défense du Bastion, sièges, événements de Bastion complets, 14 des 18 bâtiments, PNJ autres que Forgeron et Guérisseur, forge cérémonielle, Forge Légendaire, alchimie avancée (mélange, mutations), Marché, quatre personnages, coopération.

### 6.2 Feuille de route par versions

| Version | Contenu | Estimation de travail (14–24 h/semaine) |
|---|---|---|
| **0.1 (démo, 16/03/2028)** | Voir 6.1 | Déjà dans le calendrier du jeu ; 3 à 4 semaines pour la couche Bastion + artisanat |
| **0.2** | 6 bâtiments (jusqu'à Ancrage 8), 5 PNJ, 8 cartes d'événement, geste de forge et dépeçage tracé, Alchimie rang 1–10 | 6 à 8 semaines |
| **0.3** | **Défense du Bastion** complète (une créature, 2 bâtiments interactifs), reconstruction, Tension active | 4 à 5 semaines |
| **0.4** | 10 bâtiments (Ancrage 13), Maître d'École, Ambassadeur, Marché, 20 événements, Alchimie rang 11–20 | 8 semaines |
| **0.5** | 4 personnages (jauges individuelles, liens PNJ individuels), Forge Élémentaire, hybrides | 8 semaines |
| **0.9** | 18 bâtiments, Forge Légendaire, forge cérémonielle, sièges abstraits | 8 à 10 semaines |
| **1.0** | Équilibrage, 8 familles d'armures, accessibilité (mode auto partout) | variable |

---

## 7. Questions ouvertes pour krunt

1. **Unité de temps** : Semaine de Bastion avec créneaux (ma proposition) ou « Jour de Bastion » ? *Recommandation : Semaine.* Le jour demanderait un calendrier plus dense et multiplierait les écrans par sept sans gain de jeu.
2. **Un Bastion ou quatre ?** *Recommandation : un seul, partagé* (section 2.19). Quatre Bastions : 4× le contenu. À trancher avant d'écrire la structure de sauvegarde.
3. **Forge et niveau de métier : deux progressions ou une ?** Le livre mélange les deux. *Recommandation : garder les deux en démo* (jauge = plafond, niveau = recettes) puis **fusionner** si les tests montrent de la redondance. Fusion possible : `Forge = ⌈niveau × 4/3⌉`.
4. **La Forge Légendaire dans la campagne ?** À 20 Phases, atteindre 40 est irréaliste (section 5.7). *Recommandation : la réserver à un personnage scénarisé (pas un choix libre) ou raccourcir les paliers.*
5. **Jets d'artisanat : déterministes ou avec hasard ?** *Recommandation : déterministes + geste optionnel* (pas de perte de matériaux rares par malchance). Compromis : mode « Forcer » avec risque.
6. **Mini-jeux de dépeçage et de forge : obligatoires ?** Ils coûtent cher à produire et à équilibrer. *Recommandation : tout doit être jouable en mode auto ; les mini-jeux sont des bonus de Marge (±4).* Les couper en démo.
7. **Capacité de bâtiments à Ancrage 0–3** (0 dans le livre, 2 dans ma proposition) : valider.
8. **Défense du Bastion** : un mode de chasse à part entière (ma proposition, version 0.3) ou un simple tableau de résultat comme dans le livre ? Je défends le mode jouable : c'est l'élément du chapitre le plus fort émotionnellement, et peu coûteux une fois la chasse existante.
9. **Sièges et combat de masse** : *recommandation franche : couper pour la 1.0*, ou garder un unique siège scénarisé abstrait (2.9). Un combat de masse complet est trop ambitieux pour un projet en solo.
10. **Éléments** : la correspondance Bois = Vent et Métal = Foudre, appliquée aux bonus du Bastion et aux combinaisons de forge (option 10). Valider, ou choisir de remplacer par Bois et Métal partout.
11. **Honneur de groupe** (« collectif » du livre, jamais défini) : *recommandation : dérivé en lecture seule* de la moyenne des Honneurs individuels, plus des bonus collectifs permanents (+1 à Ancrage 13).
12. **Nombre de recettes** : 112 armes + 40 armures + 60 recettes d'alchimie. *Recommandation : générer par script les armes/armures à partir de tables, ne dessiner que les icônes ; viser 24 armes et 8 armures en 0.5.*
13. **Éclats et lots** : les lots Std/Sup payables en éclats (150 % de la valeur) contredisent un peu l'esprit du livre (« l'argent ne remplace pas les matériaux de chasse »). *Recommandation : garder cette entorse pour Std/Sup seulement.*
14. **« Trois jauges d'artisanat »** : j'ai lu Forge, Ancrage et Tension. Si krunt pensait à autre chose (par exemple trois jauges propres au mini-jeu de forge, Chaleur, Cadence, Pureté), le préciser : la section 2.13 s'y adapte facilement.
15. **Mode multijoueur à quatre** : *recommandation : ne pas le prévoir en 1.0.* La Phase de Bastion à quatre joueurs en parallèle est un chantier réseau et d'interface.
16. **Défaites et PNJ morts** : le livre admet des PNJ morts. *Recommandation : jamais pour un PNJ lié à la trame principale* ; remplacement par « blessé, inactif 2 Phases ».

---

## 8. Ponts avec les autres domaines

- **Chasse et combat (domaine 01 et 03)** : fournir la **durée de référence**, le pourcentage de dégâts élémentaires, les brisures et les zones « précieuses » par monstre (pour la qualité des matériaux, 2.12) ; et un **format de fiche de monstre** réutilisable en arène de défense.
- **Jauges et progression (personnage)** : attendre la table de **XP par métier** (Livre VII + IX) pour Forgeron, Alchimiste, Herboriste, Dépeceur ; définition unique de l'**Honneur** individuel et de l'Honneur de groupe dérivé.
- **Métiers et compétences** : accès par métier aux activités du Planificateur ; Maître d'École (rangs d'École) ; lien Forgeron/Alchimiste avec l'arbre de compétences.
- **Familiers et dressage** : rôles `recolte` et `bete_de_somme` (sac, ramassage), Appât Olfactif et Répulsif (leurre en défense), état Sauvage/Habituée/Dressée.
- **Quêtes de plateforme et exploration** : points de récolte, outils, Jalons de Bastion (4, 8, 13, 18) comme quêtes écrites ; embuscades dans les ruines.
- **Diplomatie, clans, politique** : Ambassadeur de Clan, Quartier Diplomatique, Donjon, demandes de clan, forge cérémonielle par région.
- **Interface générale (HUD, menus)** : composants communs de liste, grille, barre de jauge, carte d'événement, fiche de PNJ ; conventions de 360 px.
- **Données et outils (CharForge, PocketBase)** : schémas 3.1 à 3.9 ; export JSON ; journal Acte/Trace/Conséquence par Phase.
