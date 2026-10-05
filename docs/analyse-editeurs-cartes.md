# MapForge et LevelForge : faut-il les construire, ou Godot suffit-il ?

Rédigée le 2026-10-05. Recherche web (sources en bas) + ce que le projet demande. Question de krunt : « Mapforge et Levelforge servent-ils vraiment, ou Godot gère-t-il directement ? Et sinon, existe-t-il des logiciels open source qui font gagner du temps ? »

## Réponse courte

**Ne construis ni MapForge ni LevelForge pour le jeu.** Godot 4 fait déjà l'édition de cartes de tuiles, et deux éditeurs libres éprouvés (Tiled, LDtk) peuvent s'y brancher si l'édition dans Godot ne suffit pas. Ce qu'il peut rester à fabriquer, ce sont de **petits scripts** (génération, validation, lien avec le canon StoryForge et le roster de monstres), pas un éditeur complet. Le cas du **CRSVTT** (cartes de table, accessibles en ligne) est différent et peut se décider plus tard.

## Ce que Godot 4 fait déjà
- **TileMapLayer** (le nœud TileMap a été remplacé en 4.3 par des couches séparées) : peinture de tuiles, plusieurs couches, collisions et physique par tuile.
- **Terrains (autotiling)** : on peint « herbe ici, terre là » et Godot choisit les tuiles qui s'enchaînent aux bords (règles de voisinage). Le code peut aussi poser des terrains par script (`set_cells_terrain_connect`), donc la génération procédurale est possible sans éditeur externe.
- **Scènes** : on peut poser des monstres, des PNJ, des déclencheurs directement comme nœuds.
- **Extension communautaire « Better Terrain »** pour pallier les limites de l'éditeur de terrains.
Ce que je n'ai **pas** pu vérifier : les détails de navigation par tuile, et les performances sur Android pour de grandes cartes.

## Éditeurs libres existants
| Outil | Licence | Intérêt pour ce projet | Pont vers Godot 4 |
|---|---|---|---|
| **Tiled** | GPL v2+ (éditeur), BSD pour la bibliothèque | Standard éprouvé ; tuiles, objets, couches ; format JSON ou TMX | Importeur **YATI** (MIT) pour Godot 4, plusieurs forks |
| **LDtk** | MIT | Pensé pour le level design moderne : vue « monde » de plusieurs niveaux, entités avec champs personnalisés, couches automatiques par règles | Plusieurs importeurs MIT pour Godot 4 (heygleeson, amano, etc.) |
| **Azgaar's Fantasy Map Generator** | MIT | Carte du monde générée dans le navigateur (régions, états, routes), export SVG/PNG/JSON | Pas de Godot ; utile pour la **carte du monde** et la table |
Attention : les importeurs sont maintenus par la communauté, pas par Godot. Un importeur qui cesse d'être maintenu après une mise à jour de Godot est un risque réel. Le format de sortie de Tiled et de LDtk est de toute façon du **JSON lisible**, donc un script de conversion maison reste possible.

## Où chaque option gagne
- **Cartes 3/4 d'exploration et niveaux de plateforme/arènes** : Godot seul suffit pour la démo (une zone). Si tu veux poser beaucoup de monstres, PNJ, déclencheurs et amorces de quête avec des champs (cle_id du roster, DD, tags), **LDtk** est le plus adapté (entités à champs, vue monde pour un monde ouvert par zones). Tiled fait la même chose avec un peu plus de configuration.
- **Génération par règles et validation** (chemins accessibles, densité de monstres selon le rang, zones interdites) : scripts maison (Python ou GDScript) sur le JSON de LDtk/Tiled ou sur la scène Godot. C'est le seul endroit où une « Forge » peut apporter ce que les autres n'ont pas.
- **Carte du monde** (20 régions, îles, routes) : Azgaar pour dégrossir, mais **la géographie des livres est contradictoire** (voir `docs/audit/notes-lecture-livres.md`, Atlas). Il faut corriger les positions avant de générer.
- **CRSVTT** (cartes de combat en table, en ligne) : cas à part. Le plus simple est de partir d'**images et de grilles importées** avec brouillard de guerre, sans éditeur. Un éditeur de tuiles dans le navigateur est un chantier lourd ; à réserver après la démo du jeu.

## Recommandation
1. **MapForge et LevelForge : ne pas démarrer.** Retirer des 6 semaines d'outils.
2. **Pour la démo** : Godot (TileMapLayer + terrains) seul ; essayer **LDtk** sur une zone en parallèle (une journée) pour décider si les entités à champs et la vue monde valent le détour.
3. **Après la démo** : un script de validation de cartes et, si nécessaire, un petit générateur. **Pas d'éditeur maison.**
4. **CRSVTT** : décider plus tard ; commencer par import d'image, grille, brouillard.

## À faire pour trancher pour de bon
- Un essai de 1 journée : une zone 3/4 de 40×30 tuiles faite (a) dans Godot seul, (b) dans LDtk avec importeur. Comparer le temps, la lisibilité du résultat, la facilité d'y poser des entités du roster.
- Vérifier la compatibilité de l'importeur LDtk choisi avec la version de Godot utilisée.
- Mesurer les performances sur le téléphone cible.

## Sources
- [LDtk (dépôt officiel, licence MIT)](https://github.com/deepnight/ldtk)
- [Importeurs LDtk pour Godot 4 (bibliothèque d'assets)](https://godotengine.org/asset-library/asset/2181) · [heygleeson/godot-ldtk-importer](https://github.com/heygleeson/godot-ldtk-importer)
- [Tiled (dépôt officiel)](https://github.com/mapeditor/tiled) · [YATI, importeur Tiled pour Godot 4 (MIT)](https://godotengine.org/asset-library/asset/1772)
- [Better Terrain (extension Godot 4)](https://github.com/Portponky/better-terrain) · [Guide des terrains Godot](https://uhiyama-lab.com/en/notes/godot/terrains-autotile-setup/)
- [Azgaar's Fantasy Map Generator (MIT)](https://github.com/Azgaar/Fantasy-Map-Generator)
