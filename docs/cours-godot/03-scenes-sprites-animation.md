# Module 3 : scènes, nœuds, sprites, animation

## Objectif

Afficher un personnage animé à l'écran, avec des sprites venant de PixelForge.

## À savoir

- **Nœud** : la brique de base (une image, un son, une caméra, une zone de collision...).
- **Scène** : un arbre de nœuds enregistré dans un fichier `.tscn`. Une scène peut être placée dans une autre : c'est ainsi qu'on construit un jeu (le héros est une scène, le niveau en contient une copie).
- **Nœuds 2D utiles** : `Node2D` (base), `Sprite2D` (une image), `AnimatedSprite2D` (une animation image par image), `Camera2D`, `CollisionShape2D`.

## Importer des sprites depuis PixelForge

1. Exporte tes images en **PNG** (une image par frame, ou une planche de sprites avec des cases de taille identique).
2. Glisse les fichiers dans `assets/sprites/` depuis l'explorateur de fichiers : Godot les importe automatiquement.
3. Clique sur un fichier dans le dock « Système de fichiers » puis sur l'onglet **Import** (à côté de la scène). Pour du pixel art : **Filter** = `Nearest`, **Mipmaps** désactivés, **Compress Mode** = `Lossless`. Clique sur « Réimporter ».

## Animer avec `AnimatedSprite2D`

C'est le plus simple pour commencer.

1. Crée une scène `scenes/heros.tscn` avec un `CharacterBody2D` comme racine (on s'en servira au module 4), et ajoute-lui un enfant `AnimatedSprite2D`.
2. Dans l'inspecteur, **Sprite Frames** > « Nouveau SpriteFrames », puis clique sur la ressource pour ouvrir l'éditeur d'animation en bas.
3. Renomme l'animation `default` en `repos`. Ajoute des animations avec le bouton « Nouvelle animation » : `marche`, `saut`, `attaque`...
4. Ajoute les images : soit en les glissant une par une, soit avec « Ajouter des images depuis une feuille de sprites » (indique le nombre de colonnes et de lignes).
5. Règle la **vitesse** (images par seconde, par exemple 10) et la **boucle** (`repos` et `marche` en boucle, `attaque` et `saut` sans boucle).

Pour la lancer depuis un script :

```gdscript
@onready var anim: AnimatedSprite2D = $AnimatedSprite2D

func _ready() -> void:
	anim.play("repos")
```

## Animer avec `AnimationPlayer` (plus tard)

`AnimationPlayer` peut animer **n'importe quelle propriété** de n'importe quel nœud, pas seulement les images. C'est ce qui servira à activer les zones de coup au bon moment dans une attaque (module 7). Pour le moment, `AnimatedSprite2D` suffit.

## Le test du cycle de marche (à ne pas sauter)

C'est le test qui te dira si ton IA est utilisable pour les animations :
1. Produis **un cycle de marche en 8 images, dans une seule direction**.
2. Importe-les dans une animation `marche`, à 10 images par seconde.
3. Regarde-la tourner en boucle : le personnage a-t-il la même taille, les mêmes couleurs, les mêmes contours d'une image à l'autre ? Les pieds glissent-ils ou les pas sont-ils réguliers ?

Si ça tremble ou que l'apparence change, ton pipeline n'est pas encore prêt pour la production, et mieux vaut le savoir maintenant.

## Retourner un sprite (le miroir)

Pour regarder à gauche, inutile de dessiner une seconde animation :

```gdscript
anim.flip_h = true    # regarde à gauche
anim.flip_h = false   # regarde à droite
```

## Exercice

Crée la scène `heros.tscn` avec un `AnimatedSprite2D` à deux animations (`repos` et `marche`) à partir de tes sprites de test, ou de simples carrés de deux couleurs. Place-la dans `test.tscn` (glisse le fichier dans la scène). Lance et vérifie que l'animation tourne.

## Erreurs fréquentes

- **Sprite flou** : l'import n'est pas en `Nearest`.
- **Animation qui ne démarre pas** : oublier `play()`, ou une animation dont la vitesse est à 0.
- **Image décalée** : le centre du sprite n'est pas là où tu crois. Dans l'inspecteur, désactive **Centered** ou règle **Offset**.

## Pour aller plus loin

Documentation : « Using AnimatedSprite2D » et « Introduction to the animation features ».
