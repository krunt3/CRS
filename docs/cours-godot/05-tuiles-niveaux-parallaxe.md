# Module 5 : tuiles, niveaux, parallaxe

## Objectif

Construire un niveau de plateforme avec un sol, des plateformes, un décor et de la profondeur.

## À savoir

- **TileSet** : la ressource qui décrit tes tuiles (l'image, la taille d'une tuile, les collisions de chaque tuile).
- **`TileMapLayer`** : le nœud qui pose les tuiles sur une grille. *(À partir de Godot 4.3. Avant, c'était le nœud `TileMap`, désormais déconseillé. Vérifie ta version.)*
- **Une couche = un rôle** : sol, décor, premier plan. On empile plusieurs `TileMapLayer`.

## Étape 1 : créer un TileSet

1. Prépare une image de tuiles (une grille de cases identiques). Elle doit être cohérente avec la taille que tu as choisie dans le formulaire (par exemple 32 px).
2. Ajoute un nœud `TileMapLayer` à ta scène de niveau.
3. Dans l'inspecteur, **Tile Set** > « Nouveau TileSet ». Règle **Tile Size** à la taille de ta tuile.
4. Ouvre l'éditeur de TileSet (en bas) et glisse ton image dedans : accepte la création automatique des tuiles.

## Étape 2 : donner une collision aux tuiles

1. Dans les propriétés du TileSet, ouvre **Physics Layers** et ajoute une couche. Note son numéro de **Collision Layer** (tu en auras besoin).
2. Dans l'éditeur de TileSet, onglet **Paint**, choisis la propriété **Physics Layer 0** et peins sur chaque tuile la zone solide (par défaut un carré entier).
3. **Limite à connaître** : d'après ton rapport, Godot ne gère qu'une seule forme de collision par tuile dans un TileSet. Dessine donc des tuiles dont la collision est un simple polygone.
4. **Plateformes traversables par le bas** : dans les propriétés de la forme d'une tuile, active **One Way Collision** (« collision à sens unique »).

## Étape 3 : peindre le niveau

1. Sélectionne le `TileMapLayer`. Choisis une tuile dans le panneau du bas et peins avec la souris dans la vue.
2. Lance : ton héros doit marcher sur les tuiles.

## Étape 4 : les terrains (peindre sans se soucier des bords)

Les **terrains** (Terrains) choisissent automatiquement la bonne tuile de bord ou de coin. Dans le TileSet : **Terrain Sets** > ajoute un ensemble, un terrain, puis assigne à chaque tuile la partie du terrain qu'elle représente (coins, côtés). Ensuite, dans le panneau de peinture, l'onglet **Terrains** te laisse peindre « de la terre » sans choisir chaque tuile. C'est l'étape la plus longue à installer, mais celle qui rend la construction d'un niveau agréable.

## Étape 5 : le décor et la parallaxe

- **Parallaxe** : les couches lointaines défilent plus lentement que le premier plan, ce qui crée la profondeur. Dans Godot 4.3+, utilise le nœud `Parallax2D` avec un enfant `Sprite2D` ; règle **Scroll Scale** (par exemple 0,3 pour un fond lointain, 1 pour la couche du joueur). *(Avant 4.3 : `ParallaxBackground` et `ParallaxLayer`.)*
- **Largeur** : puisque ton écran est extensible, les fonds doivent être **plus larges** que la zone d'action. Active la répétition (`Repeat`) pour que le fond se prolonge.
- **Caméra** : ajoute une `Camera2D` comme enfant du héros ; active **Position Smoothing** pour un suivi doux. Règle les **Limits** (gauche, droite, bas) pour que la caméra ne sorte pas du niveau.

## Importer des cartes depuis Tiled

Godot ne lit pas directement les cartes `.tmj` de Tiled. Il existe des extensions pour ça dans l'Asset Library *(à vérifier : choisis une extension récente et maintenue)*. Pour ton premier niveau, peins directement dans Godot : cela évite une étape et te permet de tester sans quitter l'éditeur.

## Exercice

Construis un petit niveau de plateforme :
- un sol continu, trois plateformes à des hauteurs différentes dont une traversable par le bas ;
- deux couches de fond de parallaxe ;
- une `Camera2D` qui suit le héros avec des limites.

Teste-le en courant d'un bout à l'autre et en sautant sur chaque plateforme.

## Erreurs fréquentes

- **Le héros traverse les tuiles** : la **couche** de collision du TileSet et le **masque** du héros ne correspondent pas (module 7).
- **Des lignes entre les tuiles** : l'import des tuiles n'est pas en `Nearest`, ou la caméra a une position non entière. Active **Pixel Snap** dans les paramètres du projet *(à vérifier)*.
- **Le fond s'arrête sur un téléphone large** : le fond n'est pas répété ou pas assez large.

## Pour aller plus loin

Documentation : « Using TileMaps », « Using TileSets » et « 2D parallax ».
