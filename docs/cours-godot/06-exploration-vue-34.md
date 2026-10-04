# Module 6 : l'exploration en vue 3/4

## Objectif

Un héros qui se déplace en vue de dessus (type Zelda), derrière et devant les objets, et qui passe du mode exploration au mode plateforme.

## À savoir

- La vue 3/4 est une vue de dessus légèrement inclinée : on voit le dessus des objets et un peu leur face avant.
- **Pas de gravité** : le héros se déplace dans les quatre directions.
- **Trois directions dessinées** (bas, haut, côté) suffisent : le côté gauche est le miroir du côté droit.

## Étape 1 : le héros en vue 3/4

Crée une scène `heros_explo.tscn` avec un `CharacterBody2D` racine, une `CollisionShape2D` **petite et placée aux pieds** (pas sur tout le corps : le héros doit pouvoir passer « devant » un mur), et un `AnimatedSprite2D` avec les animations `repos_bas`, `repos_haut`, `repos_cote`, `marche_bas`, `marche_haut`, `marche_cote`.

```gdscript
extends CharacterBody2D

@export var vitesse := 180.0
@onready var anim: AnimatedSprite2D = $AnimatedSprite2D

var _regard := "bas"   # "bas", "haut" ou "cote"

func _physics_process(_delta: float) -> void:
	var direction := Input.get_vector("gauche", "droite", "haut", "bas")
	velocity = direction * vitesse
	move_and_slide()
	_mettre_a_jour_animation(direction)

func _mettre_a_jour_animation(direction: Vector2) -> void:
	if direction != Vector2.ZERO:
		if absf(direction.x) > absf(direction.y):
			_regard = "cote"
			anim.flip_h = direction.x < 0.0
		elif direction.y > 0.0:
			_regard = "bas"
		else:
			_regard = "haut"
		anim.play("marche_" + _regard)
	else:
		anim.play("repos_" + _regard)
```

`Input.get_vector` renvoie un vecteur déjà normalisé : le héros ne va pas plus vite en diagonale.

## Étape 2 : passer devant et derrière (le tri en profondeur)

Dans une vue 3/4, un héros qui monte doit passer **derrière** un arbre, et quand il descend, **devant**. On l'obtient en triant les objets par leur position verticale :

1. Place tes objets (héros, arbres, maisons, monstres) dans un nœud `Node2D` commun, par exemple `Objets`.
2. Dans l'inspecteur de `Objets`, active **Y Sort Enabled** (dans la section « Ordering »).
3. Pour chaque objet, la **position** du nœud doit être placée **aux pieds** de l'objet : c'est ce point qui décide de l'ordre.
4. Pour tes `TileMapLayer` qui contiennent des tuiles hautes (arbres, murs), active aussi **Y Sort Enabled** sur la couche et règle le décalage vertical d'ordre (« Y Sort Origin ») des tuiles concernées dans le TileSet.

## Étape 3 : les collisions en 3/4

- Les collisions des murs et des arbres ne couvrent que **leur base**, pas leur hauteur visuelle.
- Le héros a une petite collision aux pieds : il passe derrière un arbre sans se coincer dans le feuillage.

## Étape 4 : passer de l'exploration à la plateforme

Les quêtes se jouent en plateforme. La méthode la plus simple : **changer de scène**.

```gdscript
# Dans un déclencheur de quête (par exemple un Area2D à l'entrée d'une grotte)
func _on_body_entered(body: Node2D) -> void:
	if body.is_in_group("joueur"):
		get_tree().change_scene_to_file("res://scenes/quete_grotte.tscn")
```

Ajoute ton héros au groupe `joueur` (inspecteur > onglet **Nœud** > **Groupes**). Pour revenir à l'exploration à la fin de la quête, le niveau de plateforme appelle `change_scene_to_file` vers la scène d'exploration.

**Limite à connaître** : changer de scène détruit l'ancienne. Pour garder l'état (position du joueur, quêtes en cours, objets), il faut le conserver dans un **autoload** (un script toujours actif), vu au module 10.

## Exercice

Construis une petite zone d'exploration :
- un sol de tuiles, un arbre et un mur avec collision à la base ;
- un héros qui passe devant et derrière l'arbre selon sa position verticale ;
- un déclencheur qui charge le niveau de plateforme du module 5 ;
- dans le niveau de plateforme, un panneau de sortie qui renvoie à l'exploration.

## Erreurs fréquentes

- **Le héros passe toujours devant (ou toujours derrière)** : le point d'origine du sprite n'est pas aux pieds, ou **Y Sort Enabled** n'est pas activé sur le parent commun.
- **Le héros se coince dans les murs** : sa collision couvre tout le corps.
- **Vitesse plus rapide en diagonale** : tu as utilisé deux `get_axis` au lieu de `get_vector`.

## Pour aller plus loin

Documentation : « Using TileMaps » (section sur le tri en profondeur) et « Changing scenes manually ».
