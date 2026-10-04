# Génération procédurale par règles — base de connaissances

Notes de recherche pour le projet Forge Suite (Jeu A : CRS, Jeu B : jeu Android lié à CRS).
Rédigées le 2026-10-04. Elles servent de contexte à toute session Claude Code qui n'a pas l'historique du projet.

**Principe retenu avec l'utilisateur :** générer cartes et niveaux par des règles et du hasard contrôlé, pas par une IA. Tout doit tourner en local, être reproductible et ne dépendre d'aucun service externe.

## Statut des informations

- **Vérifié par recherche (titres et extraits lus, pas les dépôts en entier)** : les liens de la section « Sources ».
- **Connaissance générale, non revérifiée ici** : tout ce qui est marqué *(à vérifier)*. Vérifier la licence et l'état de maintenance d'une bibliothèque avant de l'adopter.

## Trois besoins distincts dans le projet

| Besoin | Outil du projet | Nature |
|---|---|---|
| Carte d'exploration en vue de dessus / 3/4 (mode principal du jeu, aussi utilisée par la table virtuelle CRS) | MapForge (JavaScript) | Grille de tuiles, régions, biomes, lieux |
| Niveaux de plateforme et arènes de chasse (niveau long façon Metal Slug) | LevelForge, export `.tmj` vers Godot | Grille de tuiles, côté jeu |
| Monde entier (lore, régions, relations) | StoryForge | Pas de la génération de tuiles, mais fournit les paramètres (climat, culture, danger) |

## Techniques utiles

### 1. Bruit en couches (terrain, biomes)

Principe de Minecraft : une graine (seed) alimente un bruit de gradient (Perlin ou simplex). On additionne plusieurs bruits de fréquences et d'amplitudes différentes pour un résultat naturel. Pour choisir le biome en un point, on calcule plusieurs paramètres de climat (température, humidité, distance à la côte, érosion, une valeur « étrange » pour les variantes) et on prend le biome dont les paramètres cibles sont les plus proches. Ensuite une phase de « peuplement » ajoute arbres, ressources et structures.

- **Intérêt pour toi :** tes régions de Palmaria ont déjà une identité (culture, zone Tenue / Marge / Royaumes Sauvages, niveau de Corruption). Ces valeurs peuvent être les « paramètres de climat » : le bruit ne décide que du détail local.
- **Godot :** `FastNoiseLite` est intégré au moteur.
- **JavaScript :** bruit simplex dans rot.js (voir plus bas), ou une petite bibliothèque dédiée *(à vérifier)*.

### 2. Assemblage de salles ou de segments préfabriqués

On dessine à la main quelques segments (un écran de large chacun, par exemple), chacun avec des « prises » à gauche et à droite (hauteur du sol, entrée, sortie). Le générateur les enchaîne selon des règles de compatibilité.

- **Intérêt pour toi :** c'est la méthode la plus adaptée à l'arène de chasse. Le résultat est toujours jouable parce que chaque segment a été dessiné et testé par toi.
- Chaque segment peut porter des **emplacements de pièges** et des **points de trajet du monstre** (patrouille, fuite, retour).

### 3. Générateurs de salles et de couloirs (BSP, « digger »)

Découpe l'espace en salles reliées par des couloirs. rot.js fournit un générateur « Digger » et peut renvoyer la liste des salles et des couloirs après génération.

- **Intérêt :** donjons, souterrains, intérieurs de bâtiments en vue de dessus.

### 4. Automates cellulaires (grottes)

Part d'un bruit aléatoire de cases pleines / vides, puis lisse en appliquant une règle de voisinage plusieurs fois. rot.js a un générateur « Cellular ».

- **Intérêt :** grottes, zones corrompues, forêts irrégulières.

### 5. Marche de l'ivrogne (« drunkard's walk »)

Un point se déplace au hasard en creusant. Simple, utile pour des chemins ou des rivières irréguliers.

### 6. Wave Function Collapse (WFC)

On fournit un exemple ou des règles d'adjacence entre tuiles ; l'algorithme remplit une zone en respectant ces règles. Donne de la variété visuelle cohérente (villages, ruines, décors).

- **Limite :** il faut définir correctement les règles d'adjacence de chaque tuile. Le résultat est « plausible », pas « conçu » : à réserver à la variation décorative, pas aux lieux importants pour l'histoire.

## Bibliothèques et outils

### JavaScript (pour MapForge et les outils Forge)

| Outil | Rôle | Remarque |
|---|---|---|
| [rot.js](https://github.com/ondras/rot.js) | Générateurs de labyrinthes, cavernes (cellulaire) et donjons, générateur aléatoire avec graine, champ de vision, recherche de chemin, bruit | Écrit en JavaScript, couvre presque toutes les techniques ci-dessus sauf WFC. Licence *(à vérifier)* |
| [kchapelier/wavefunctioncollapse](https://github.com/kchapelier/wavefunctioncollapse) | Portage JavaScript de l'implémentation originale de WFC | Référence JavaScript pour WFC. Licence *(à vérifier)* |
| [blazinwfc](https://github.com/Arkyris/blazinwfc) | WFC en JavaScript, orienté vitesse et jeux de tuiles complexes, renvoie un tableau d'indices de tuiles | Pensé pour Phaser mais utilisable pour n'importe quel rendu |
| [MohammadHossinzehi/wave-function-collapse](https://github.com/MohammadHossinzehi/wave-function-collapse) | WFC en JavaScript pur, sans dépendance, modèles « overlapping » et « tiled », retour arrière | Petit et lisible : utile pour comprendre ou adapter |

### Godot 4 (pour le jeu)

| Outil | Rôle |
|---|---|
| `FastNoiseLite` | Bruit intégré au moteur (relief, biomes) |
| [Wave Function Collapse (Asset Library)](https://godotengine.org/asset-library/asset/1951) | Addon WFC avec retour arrière : garantit l'absence de cases cassées |
| [Procedural-Map-Generator (Asset Library)](https://godotengine.org/asset-library/asset/2979) | Modifie une TileMap avec automates cellulaires, WFC et d'autres algorithmes |
| [Lommix/infinite_worlds](https://github.com/Lommix/infinite_worlds) | Addon de monde infini par WFC avec outils d'éditeur |
| [Angular-Angel/wfclab](https://github.com/Angular-Angel/wfclab) | Application Godot 4 pour explorer la génération par l'exemple |

### Autres pistes *(non vérifiées ici)*

- **Tiled « Automapping »** : règles qui placent automatiquement des tuiles de transition ; Tiled est déjà dans ton pipeline vers Godot (`.tmj`).
- **Azgaar's Fantasy Map Generator** : générateur de cartes de monde de fantasy, open source ; peut inspirer le niveau « monde » de StoryForge.
- **Diagrammes de Voronoï** : classique pour découper un continent en régions ou territoires.

## Principes d'architecture proposés

1. **Un générateur est une fonction pure** : `(paramètres, graine) → grille de numéros de tuiles` en JSON. Aucun état caché.
2. **La graine rend la carte reproductible.** Avec la même graine, la table de jeu (CRS) et le jeu Android affichent exactement la même carte. C'est un atout direct pour ton idée « un seul jeu sur deux médias ».
3. **Génération assistée, pas aveugle** : le résultat s'ouvre dans MapForge ou LevelForge, où tu corriges à la main. Les lieux importants pour l'histoire sont dessinés à la main et posés par-dessus.
4. **Validation automatique** : après génération, vérifier par recherche de chemin (tu as déjà A* dans MapForge) que les zones clés sont atteignables.
5. **Les paramètres viennent du canon** : région, culture, niveau de Corruption, danger viennent de StoryForge, pas codés en dur.

## Ordre d'essai conseillé

1. Dans MapForge : relief et biomes d'une région avec bruit en couches et rot.js, paramétrés par les valeurs de la région.
2. Pour la chasse : un assembleur de segments préfabriqués avec emplacements de pièges et trajets du monstre.
3. Plus tard : WFC pour la variation décorative (villages, ruines).

## Pièges à éviter

- Générer sans validation : une carte « jolie » peut être injouable.
- Utiliser WFC pour des lieux qui portent l'intrigue : le résultat manque d'intention.
- Ajouter des paramètres de génération avant d'avoir une carte simple qui marche.
- Adopter une bibliothèque sans vérifier sa licence et sa maintenance.

## Sources

- [World generation (Minecraft Wiki)](https://minecraft.wiki/w/World_generation)
- [The World Generation of Minecraft (Alan Zucconi)](https://www.alanzucconi.com/2022/06/05/minecraft-world-generation/)
- [World Generation Overview (Microsoft Learn, Minecraft)](https://learn.microsoft.com/en-us/minecraft/creator/documents/world-generation?view=minecraft-bedrock-stable)
- [Procedural Generation in Godot 4: 5 Patterns from Real Indie Games](https://ziva.sh/blogs/godot-procedural-generation)
- [20 Free Procedural Generation Tools and Libraries (2026 Edition)](https://gamineai.com/resources/20-free-procedural-generation-tools-and-libraries-2026-edition)
- [rot.js : manuel des générateurs de donjons](https://github.com/ondras/rot.js/blob/master/manual/pages/map/dungeon.html)
- [Building a roguelike game with Rot.js (LogRocket)](https://blog.logrocket.com/building-a-roguelike-game-with-rot-js/)
- [Sujet GitHub « wavefunctioncollapse »](https://github.com/topics/wavefunctioncollapse)
- [Sujet GitHub « procgen »](https://github.com/topics/procgen)
