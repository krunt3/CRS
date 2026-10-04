# Module 4 : le héros de plateforme

## Objectif

Un héros qui court, saute et tombe, avec un bon ressenti.

## À savoir

- **`CharacterBody2D`** est le nœud fait pour un personnage que tu contrôles. Il a une propriété `velocity` (la vitesse) et une fonction `move_and_slide()` qui le déplace en respectant les collisions.
- Un `CharacterBody2D` doit avoir un enfant **`CollisionShape2D`** avec une forme (`RectangleShape2D` ou `CapsuleShape2D`) pour exister physiquement.
- La physique se programme dans `_physics_process(delta)`, pas dans `_process`.

## Étape 1 : les touches

Dans **Projet > Paramètres du projet > Input Map** (Contrôles), ajoute ces actions et associe-leur des touches :

| Action | Touches |
|---|---|
| `gauche` | Flèche gauche, joystick gauche vers la gauche |
| `droite` | Flèche droite, joystick gauche vers la droite |
| `saut` | Espace, bouton A de la manette |
| `attaque` | Touche X, bouton X de la manette |
| `haut`, `bas` | Flèches haut et bas (pour la vue 3/4, module 6) |

Les noms que tu choisis ici sont ceux que le code utilise. Les boutons tactiles (module 9) se brancheront sur les mêmes actions : tu n'auras donc rien à changer dans le code du héros.

## Étape 2 : le déplacement de base

Sur le nœud racine `CharacterBody2D` de `heros.tscn`, attache ce script `scripts/heros_plateforme.gd` :

```gdscript
extends CharacterBody2D

@export var vitesse := 260.0
@export var force_saut := -520.0
@export var gravite := 1500.0

@onready var anim: AnimatedSprite2D = $AnimatedSprite2D

func _physics_process(delta: float) -> void:
	# La gravité tire vers le bas quand on n'est pas au sol
	if not is_on_floor():
		velocity.y += gravite * delta

	# Déplacement horizontal : -1 (gauche), 0, ou 1 (droite)
	var direction := Input.get_axis("gauche", "droite")
	velocity.x = direction * vitesse

	# Saut
	if Input.is_action_just_pressed("saut") and is_on_floor():
		velocity.y = force_saut

	move_and_slide()
	_mettre_a_jour_animation(direction)

func _mettre_a_jour_animation(direction: float) -> void:
	if direction != 0.0:
		anim.flip_h = direction < 0.0
	if not is_on_floor():
		anim.play("saut")
	elif direction != 0.0:
		anim.play("marche")
	else:
		anim.play("repos")
```

Pour l'essayer, il te faut un sol : dans `test.tscn`, ajoute un `StaticBody2D` avec une `CollisionShape2D` rectangulaire large, placé sous le héros. Lance avec F6.

## Étape 3 : le ressenti (c'est ce qui fait un bon jeu)

Deux améliorations que tous les jeux de plateforme utilisent, sans que le joueur s'en rende compte :

- **Temps de grâce (« coyote time »)** : tu peux encore sauter une fraction de seconde après avoir quitté le bord d'une plateforme.
- **Saut mémorisé (« jump buffer »)** : si tu appuies sur saut un peu avant d'atterrir, le saut part dès que tu touches le sol.

```gdscript
extends CharacterBody2D

@export var vitesse := 260.0
@export var force_saut := -520.0
@export var gravite := 1500.0
@export var temps_grace := 0.10
@export var temps_memoire := 0.10

var _grace := 0.0
var _memoire := 0.0

func _physics_process(delta: float) -> void:
	if is_on_floor():
		_grace = temps_grace
	else:
		_grace -= delta
		velocity.y += gravite * delta

	if Input.is_action_just_pressed("saut"):
		_memoire = temps_memoire
	else:
		_memoire -= delta

	if _memoire > 0.0 and _grace > 0.0:
		velocity.y = force_saut
		_memoire = 0.0
		_grace = 0.0

	# Saut plus court si on relâche tôt la touche
	if Input.is_action_just_released("saut") and velocity.y < 0.0:
		velocity.y *= 0.5

	velocity.x = Input.get_axis("gauche", "droite") * vitesse
	move_and_slide()
```

Règle les valeurs en jouant : ce sont elles qui donnent le caractère de ton héros.

## Exercice

1. Ajoute un temps de grâce et un saut mémorisé et vérifie la différence au ressenti.
2. Fais varier `gravite` et `force_saut` : un saut lourd (gravité forte) ou léger (flottant) change complètement le jeu.
3. Ajoute un **double saut** (indice : un compteur de sauts restants, remis à 1 quand le héros touche le sol).

## Erreurs fréquentes

- **Le héros traverse le sol** : il manque une `CollisionShape2D` sur l'un des deux, ou la forme n'a pas de taille.
- **Il glisse sur place** : mauvaise **couche de collision / masque** (module 7 explique ces réglages).
- **Il saute n'importe quand** : `is_on_floor()` n'est valable qu'après un `move_and_slide()`.

## Pour aller plus loin

Documentation : « Using CharacterBody2D/3D » et « Physics introduction ».
