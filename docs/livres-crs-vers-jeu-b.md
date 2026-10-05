# Des livres CRS à la structure du Jeu B

Rédigé le 2026-10-05, à partir des livres que krunt a fournis en fichiers Markdown.

## Ce que j'ai lu, et ce que je n'ai pas lu

**Lu en détail :** Livre I (chapitre « La Boucle de Chasse », « Combat » section créatures, « Exploration & Survie » section Traque, jauges, Forge), Livre VIII (Supplément du Joueur, en entier), Livre IX (jusqu'aux recettes, le fichier est tronqué à 2000 lignes à la lecture).

**Pas encore lu :** Livre II (MJ, 400 Ko), Livre III (Bestiaire, 2,4 Mo), Livre IV (Atlas), Livre V (Histoire), Livre VI (Écoles et Techniques), Livre VII (Métiers), Livre X. Les fichiers sont dans le dossier de travail de la session (non copiés dans le dépôt : ce sont tes textes, volumineux ; dis-moi si tu veux les versionner).

Tout ce qui suit s'appuie donc sur les chapitres lus. Les tableaux de cohérence avec le Bestiaire, les Écoles et les Métiers restent à faire.

## La découverte principale : le jeu est déjà écrit dans le livre

Le Livre I décrit une **Boucle de Chasse en quatre temps**. C'est exactement la structure que tu décris pour le Jeu B (exploration en vue 3/4, phases de plateforme, longue chasse latérale). Il ne faut pas inventer de « niveaux » : il faut mettre la boucle du livre en jeu vidéo.

| Temps du livre | Ce qui se passe à la table | Équivalent dans le Jeu B | Vue |
|---|---|---|---|
| 1. **Désignation** | Le monde désigne une proie : Nécessité, Contrat ou Prestige. Quatre questions : quelle créature, qui désigne, pourquoi maintenant, quelles contraintes. | Écran de mission : dialogue avec le mandant (clan, guilde, ordre), contraintes affichées (par exemple « garder la tête intacte »). | Interface et scènes de dialogue |
| 2. **Traque** | Repérage, approche, lecture du terrain, pièges. Maximum **3 Jetons de Connaissance** par créature. | Exploration en vue 3/4 : traces, marques, empreintes à lire. Chaque indice trouvé donne un jeton (patterns, faiblesse, déclencheur de phase). Pose de pièges. | **3/4 (Zelda)** |
| 3. **Affrontement** | Combat contre la créature, trois phases, cinq états. La manière de la vaincre fixe la qualité des matériaux. | La chasse latérale, longue arène à la Metal Slug, où le monstre se déplace. Les jetons révèlent ses attaques à l'avance. | **Profil (plateforme)** |
| 4. **Retour au Clan** | Récolte, Récit (principal mouvement d'Honneur), Rituel. | Dépeçage (mini-jeu), récit au clan (choix de dialogue), forge, mise à jour des jauges. | Interface, Bastion |

Les **quêtes uniquement en plateforme** que tu décris correspondent aux **autres types de chasse** du livre (voir plus bas) et aux voyages et ruines du chapitre Exploration.

## Ce que le livre donne tout fait pour le jeu

### 1. Le monstre : trois phases, cinq états

Le livre définit pour chaque Boss ou Grand Monstre **trois phases** déclenchées par seuils de Vitalité :

| Phase | Vitalité | Comportement type |
|---|---|---|
| 1. Normal | 100 à 60 % | Action standard + action spéciale |
| 2. Blessé | 59 à 30 % | Change d'approche, nouvelle action |
| 3. Désespéré | 29 à 0 % | Tout ou rien, une action ultime par combat |

Et **cinq états comportementaux** (Territoire, Menacée, Blessée, Désespérée, Effondrée). C'est une **machine à états** prête pour Godot (module 8 du cours). Chaque état change les attaques disponibles et les risques. Une créature peut aussi **fuir** : c'est un état du jeu avec une conséquence (aucun matériau, Tension +2).

→ Conséquence pour le dessin : un boss a 3 phases × quelques attaques. C'est un bon argument pour un boss en **squelette** (modifier le comportement sans redessiner).

### 2. Les Jetons de Connaissance, un mécanisme de jeu parfait

- Un jeton = une information sur une phase (action standard, action spéciale, déclencheur, faiblesse, comportement final).
- Maximum 3 par créature. Non conservés d'une expédition à l'autre.
- En jeu : plus tu traques, plus **le combat devient lisible** (télégraphie des attaques à l'écran, faiblesse affichée, déclencheur de phase annoncé). Sans jeton, tu découvres en encaissant.

C'est la bonne réponse à ta question « ce monstre part à droite pendant que je vais à gauche » : la Traque et les pièges posés en amont comptent dans la fiction et dans le jeu.

### 3. La qualité des matériaux dépend du comment

| Comment | Qualité |
|---|---|
| Rapidement | Standard |
| Long combat d'usure | Supérieure |
| Faiblesse élémentaire exploitée | Élémentaire |
| Parties rares préservées | Rare |
| Fuite de la créature | Aucun, Tension +2 |

Ça devient le **score de fin de chasse** et les récompenses. Il faut des **parties de corps ciblables** (queue coupable, zone préservable) : à penser dans la hitbox du boss (cours module 13, plusieurs hurtbox par partie).

### 4. Le Retour au Clan : un mode de jeu à part

Récolte + Récit + Rituel, avec l'Honneur qui bouge. Ce n'est pas une cinématique : le livre dit que le Retour est « une session à part entière ». Dans le jeu : une scène de dialogue à choix où le joueur raconte la chasse ; la réaction du clan dépend de la manière dont tu as chassé (contraintes du contrat respectées ou non, protection des plus faibles, patience ou rapidité) et de la région (certaines valorisent l'humilité).

### 5. La Trinité de Progression : une règle pour ton journal d'événements

Chaque chasse produit **un Acte, une Trace, une Conséquence**. C'est exactement la structure de ton journal PocketBase :
- **Acte** : événement enregistré (chasse faite, manière de vaincre, jetons utilisés).
- **Trace** : objet forgé, cicatrice, titre accordé.
- **Conséquence** : dette, porte fermée, ennemi créé, route ouverte, créature qui reviendra.

Un événement du journal pourrait donc avoir ces trois champs. Les conséquences sont ce qui revient à la table et ce que la table renvoie dans le jeu.

### 6. Les jauges, directement en interface

| Jauge | Portée | Dans le jeu |
|---|---|---|
| Vitalité | individuelle | barre de vie, cicatrice permanente si case vide |
| Endurance | individuelle | barre d'énergie (esquive, coups lourds) |
| Mana | individuelle | selon l'école : Flux, Ancrage, Rituel, Sacrifice |
| Honneur | individuelle | en dehors du combat, 5 seuils |
| Forge | **collective** | progression artisanale (paliers de 10, de 0 à 40), liée au Bastion |
| Tension | **collective** | pression du monde, monte avec le temps passé |

Les deux jauges collectives (Forge, Tension) sont **le lien entre les quatre joueurs et la table** : une seule valeur partagée.

### 7. Les 14 armes : un budget d'animation prêt à l'emploi

Le Livre IX donne 14 armes avec leur école. Pour le budget d'images (module 13 du cours), voici un **regroupement par famille d'animation** proposé ; les différences se règlent dans les chiffres :

| Famille d'animation | Armes du livre | Remarque |
|---|---|---|
| Une main + bouclier | Épée Longue, Épée & Bouclier, Hache-Épée | Trois armes, mêmes bases |
| Deux mains lourdes | Grande Lame, Marteau, Lame Chargée | Longue préparation |
| Deux armes | Double Lame | Série propre (attaques rapides) |
| Perche | Lance, Glaive-Insecte | Le glaive demande aussi un compagnon (Kinsect) |
| Tir | Arc, Arbalète Légère, Arbalète Lourde, Arbalète-Lance | Viser, tirer, recharger |
| Soutien | Cor de Chasse | Pas de dégâts directs, animations de jeu d'instrument |

Six séries de combat au lieu de quatorze. C'est l'argument le plus concret pour garder 500 à 800 images au lieu de 1 500.

### 8. Les autres types de chasse du livre

| Type | Origine | Dans le Jeu B |
|---|---|---|
| Nécessité | Menace immédiate | Chasse sans Traque, sans jeton, urgence |
| Contrat | Mandant, conditions | Contraintes affichées, évaluation au Retour |
| Prestige | Défi public | Honneur ±2, risque plus élevé |
| Défense du Bastion | La proie vient au groupe | Mode « défense de base » avec bâtiments qui donnent des avantages |

### 9. Le Bastion et la Forge, ce que les quêtes de cueillette et de minage nourrissent

- **Récolte** de plantes, champignons, minerais, insectes (Livre I, chapitre « Alchimie et objets de terrain » ; Livre IX, ingrédients et recettes). Ce sont les **quêtes de plateforme** : cueillette, minage, exploration de ruines.
- **Forge** : paliers 0 à 40, un seul objet Légendaire par personnage.
- **Bastion** : base fixe avec bâtiments (Tour de Guet, Forge, Infirmerie, Archives, Jardin) qui donnent des bonus à la Traque et à la défense.

Ton idée « le jeu de rôle appliqué aux phases de Monster Hunter » est donc **le propos du Livre I**. La traduction en jeu est un travail de découpage, pas d'invention.

## Pour tes quatre personnages

Le Livre VIII donne ce qui distingue les personnages **sans changer l'histoire** :
- origine régionale (20 régions, chacune avec un bonus et un malus, et l'option avantage « Cheater » / malus « inhumain »),
- cinq axes culturels (combat, mort, magie, autorité, étranger) qui changent les réactions et les gains d'Honneur,
- avantages et handicaps (6 PA, un handicap majeur obligatoire),
- métiers et écoles.

Un seul scénario, quatre combinaisons de ces éléments : ça correspond à ce que tu as décrit. Ça influe sur l'**interface** (choix de dialogues, réactions du clan), pas sur les sprites. Les sprites changent par le corps, la palette et l'équipement.

## Réponse à « le nombre de niveaux »

Il n'y a pas de niveaux. Le monde est une carte d'exploration (3/4) avec :
- des **zones** (les 20 régions, une seule au départ),
- des **quêtes** de plateforme (cueillette, minage, ruines),
- des **chasses** : Désignation, Traque (3/4), Affrontement (profil), Retour.

Le formulaire marque cette question « hors sujet ». Si on veut un chiffre pour la démo : **une zone, une chasse complète, deux ou trois quêtes de plateforme**.

## À faire pour compléter

1. Lire le Livre VI (Écoles et Techniques) et le Livre VII (Métiers) : ce sont les arbres de compétences à transposer en arbre dans le jeu.
2. Lire le Livre III (Bestiaire) pour choisir **le premier monstre** de la démo, avec ses trois phases déjà décrites (ou à écrire).
3. Choisir **une région de départ** dans le Livre IV (Atlas) et ses tables d'événements (Livre IX, tables d12).
4. Transformer la Boucle de Chasse en **données** pour PocketBase (chasse, désignation, jetons, états, Trinité) : propositions de champs à écrire ensuite.
5. Tester sur un prototype : une chasse de Nécessité (pas de Traque) est la plus courte à construire, donc la meilleure première démo.
