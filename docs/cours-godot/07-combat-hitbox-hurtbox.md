# Module 7 : le combat, hitbox et hurtbox

## Objectif

Des coups qui touchent au bon moment, des dégâts qui ont du sens, et un combat qui paraît juste.

## À savoir

- **Hurtbox** (zone vulnérable) : la zone où un personnage **peut être touché**. Elle est petite et fixe, plus petite que le dessin.
- **Hitbox** (zone d'attaque) : la zone qui **fait mal**. Elle n'existe que pendant les images où le coup part.
- Les deux sont des nœuds **`Area2D`** avec une `CollisionShape2D`. Une `Area2D` ne bloque pas les corps : elle **détecte** les chevauchements et envoie des signaux.

Exemple : une cape traîne dans le dos du héros. Si sa zone vulnérable suivait le dessin, un monstre le toucherait « à travers » la cape et le joueur trouverait ça injuste. Avec une petite hurtbox sur le corps, la cape ne compte pas.

## Couches et masques de collision

Godot a 32 couches. Deux réglages sur chaque nœud de collision :
- **Layer** (couche) : « je suis dans cette catégorie » ;
- **Mask** (masque) : « je détecte ces catégories ».

Donne-leur des noms dans **Projet > Paramètres du projet > Layer Names > 2D Physics** :

| N° | Nom | Qui y est |
|---|---|---|
| 1 | monde | tuiles solides |
| 2 | joueur | corps du héros |
| 3 | monstres | corps des monstres |
| 4 | hitbox_joueur | zone d'attaque du héros |
| 5 | hitbox_monstre | zone d'attaque du monstre |
| 6 | hurtbox_joueur | zone vulnérable du héros |
| 7 | hurtbox_monstre | zone vulnérable du monstre |
| 8 | pieges | pièges |

Et leurs réglages :

| Nœud | Layer | Mask |
|---|---|---|
| Corps du héros | 2 | 1 (monde) |
| Corps du monstre | 3 | 1 (monde) |
| Hitbox du héros | 4 | rien (c'est la hurtbox qui détecte) |
| Hurtbox du monstre | 7 | 4 (hitbox du héros) |
| Hitbox du monstre | 5 | rien |
| Hurtbox du héros | 6 | 5 (hitbox du monstre) |

**La règle** : c'est la hurtbox qui détecte la hitbox, pas l'inverse. Ainsi une attaque qui touche deux monstres compte bien deux fois, un par monstre.

## Étape 1 : les deux scripts

`scripts/hitbox.gd` :

```gdscript
class_name Hitbox
extends Area2D

@export var degats := 10
```

`scripts/hurtbox.gd` :

```gdscript
class_name Hurtbox
extends Area2D

signal recu_degats(montant: int, origine: Vector2)

@export var duree_invincibilite := 0.5
var _invincible := false

func _ready() -> void:
	area_entered.connect(_on_area_entered)

func _on_area_entered(zone: Area2D) -> void:
	if _invincible:
		return
	if zone is Hitbox:
		recu_degats.emit(zone.degats, zone.global_position)
		_invincible = true
		await get_tree().create_timer(duree_invincibilite).timeout
		_invincible = false
```

Le temps d'invincibilité évite qu'un seul coup compte dix fois, et laisse au joueur une seconde chance après un coup.

## Étape 2 : brancher le héros

Dans `heros.tscn`, ajoute :
- un `Area2D` nommé `Hurtbox` avec le script `hurtbox.gd`, une petite `CollisionShape2D` sur le corps ;
- un `Area2D` nommé `Hitbox` avec le script `hitbox.gd`, une `CollisionShape2D` devant le héros, **désactivée au départ** (case « Disabled » cochée).

Ajoute au script du héros :

```gdscript
@export var vie_max := 100
var vie := 0
var _attaque_en_cours := false
var _recul := 0.0   # durée pendant laquelle le héros est repoussé et ne contrôle plus ses mouvements

func _ready() -> void:
	vie = vie_max
	$Hurtbox.recu_degats.connect(_on_recu_degats)
	anim.frame_changed.connect(_on_frame_changed)

func _on_recu_degats(montant: int, origine: Vector2) -> void:
	vie -= montant
	# Recul : le héros est repoussé à l'opposé du coup
	var sens := signf(global_position.x - origine.x)
	velocity = Vector2(sens * 300.0, -250.0)
	_recul = 0.25
	if vie <= 0:
		queue_free()   # à remplacer par une vraie défaite

func _attaquer() -> void:
	_attaque_en_cours = true
	anim.play("attaque")
	await anim.animation_finished
	_attaque_en_cours = false

# Active la zone de coup seulement sur certaines images de l'animation
func _on_frame_changed() -> void:
	if anim.animation == "attaque":
		var actif := anim.frame == 3 or anim.frame == 4
		$Hitbox/CollisionShape2D.set_deferred("disabled", not actif)
	else:
		$Hitbox/CollisionShape2D.set_deferred("disabled", true)
```

**Important :** le script du module 4 remet `velocity.x` à zéro ou à la vitesse de course à **chaque image** : le recul serait annulé aussitôt. Il faut donc suspendre le contrôle du joueur pendant le recul. Dans `_physics_process`, remplace la ligne `velocity.x = Input.get_axis("gauche", "droite") * vitesse` par :

```gdscript
	if _recul > 0.0:
		_recul -= delta   # le héros subit le recul, on ne touche pas à velocity.x
	else:
		velocity.x = Input.get_axis("gauche", "droite") * vitesse
```

Et, toujours dans `_physics_process`, avant `move_and_slide()`, ajoute :

```gdscript
	if Input.is_action_just_pressed("attaque") and not _attaque_en_cours:
		_attaquer()
```

**`set_deferred`** : on ne peut pas activer ou désactiver une zone de collision au milieu d'un calcul de physique ; `set_deferred` attend la fin du calcul.

**Quelles images ?** Frame 3 et 4 sont un exemple. Regarde ton animation image par image : la hitbox ne doit exister que quand le coup part, pas pendant la préparation ni le retour. C'est ce qui rend un combat lisible et juste.

**Le miroir** : si le héros regarde à gauche (`flip_h`), la hitbox doit aussi passer à gauche. Le plus simple : place la `Hitbox` dans un nœud `Node2D` pivot, dont tu inverses l'échelle (`scale.x = -1`) quand le héros se retourne.

## Étape 3 : le ressenti d'un coup (« game feel »)

Trois petits effets qui font qu'un coup « porte » :
- **Recul** du monstre ou du héros touché (déjà dans le code ci-dessus) ;
- **Clignotement** du sprite touché (`modulate` qui passe au blanc puis revient) ;
- **Courte pause** de l'image au moment du coup : mets `Engine.time_scale = 0.05` pendant 0,05 seconde via un minuteur, puis remets-le à 1. À utiliser avec modération.

## Pour les attaques des monstres (la chasse)

Un gros monstre a plusieurs attaques, chacune avec sa propre zone de coup, active sur ses propres images. Le principe est le même que pour le héros. Pour des zones complexes qui suivent l'animation (une queue qui balaie), utilise `AnimationPlayer` pour animer la position et l'activation de la `CollisionShape2D` image par image. Si Godot affiche une erreur du type « flushing queries », règle l'AnimationPlayer en mode de rappel « physics » *(à vérifier selon la version)*.

## Exercice

1. Ajoute un mannequin d'entraînement : un `StaticBody2D` avec une `Hurtbox` qui affiche les dégâts reçus dans la console.
2. Fais en sorte que seule la phase de frappe de ton animation fasse des dégâts.
3. Vérifie que le héros ne peut pas se blesser lui-même.
4. Règle l'invincibilité pour qu'elle te paraisse juste.

## Erreurs fréquentes

- **Rien ne se déclenche** : les masques de collision sont mal réglés. Contrôle chaque ligne du tableau.
- **Dégâts en rafale** : pas d'invincibilité, ou la hitbox reste active toute l'animation.
- **Erreur en changeant `disabled`** : utilise `set_deferred`.

## Pour aller plus loin

Documentation : « Using Area2D », « Collision layers and masks » (dans « Physics introduction »).
