# Module 8 : le monstre de chasse et les pièges

## Objectif

Le cœur de ton jeu : un monstre qui patrouille, te traque, charge, fuit, et qu'on peut piéger, dans une longue arène latérale.

## À savoir

- **Une machine à états** : le monstre est toujours dans un seul **état** (patrouille, traque, charge...). À chaque état correspond un comportement, et des règles disent quand passer à un autre. C'est la méthode standard pour l'IA d'un jeu.
- **Dessine d'abord l'état sur papier** : une boîte par état, une flèche par transition, avec la condition écrite dessus. Un monstre bien conçu se lit sur un schéma de 6 boîtes.

```
PATROUILLE --(joueur détecté)--> TRAQUE --(joueur proche)--> CHARGE
    ^                               |                           |
    |                               |                      (fin de charge)
    |                               v                           v
    +-------(fin de fuite)----- FUITE <--(vie basse)---- RECUPERATION --> TRAQUE
                                                                  
ASSOMME (venant de n'importe quel état, quand il tombe dans un piège) --> TRAQUE
```

## Étape 1 : la scène du monstre

Crée `scenes/monstre.tscn` avec un `CharacterBody2D` racine (couche 3, masque 1), une `CollisionShape2D`, un `AnimatedSprite2D`, une `Hurtbox` (couche 7, masque 4) et une `Hitbox` (couche 5), comme pour le héros au module 7.

## Étape 2 : le script du monstre

`scripts/monstre.gd` :

```gdscript
extends CharacterBody2D

enum Etat { PATROUILLE, TRAQUE, CHARGE, RECUPERATION, FUITE, ASSOMME }

@export var vitesse_patrouille := 70.0
@export var vitesse_traque := 140.0
@export var vitesse_charge := 380.0
@export var vitesse_fuite := 200.0
@export var portee_detection := 700.0
@export var portee_charge := 260.0
@export var gravite := 1500.0
@export var vie_max := 300
@export var seuil_fuite := 0.3        # fuit sous 30 % de vie
@export var limite_gauche := 0.0      # bornes de la patrouille (position x)
@export var limite_droite := 2000.0

var etat := Etat.PATROUILLE
var vie := 0
var _minuteur := 0.0
var _dir := 1.0
var _joueur: Node2D

func _ready() -> void:
	vie = vie_max
	_joueur = get_tree().get_first_node_in_group("joueur")
	$Hurtbox.recu_degats.connect(_on_recu_degats)

func _physics_process(delta: float) -> void:
	if not is_on_floor():
		velocity.y += gravite * delta

	match etat:
		Etat.PATROUILLE: _patrouille()
		Etat.TRAQUE: _traque()
		Etat.CHARGE: _charge(delta)
		Etat.RECUPERATION: _recuperation(delta)
		Etat.FUITE: _fuite(delta)
		Etat.ASSOMME: _assomme(delta)

	move_and_slide()
	$AnimatedSprite2D.flip_h = _dir < 0.0

func _changer_etat(nouveau: Etat, duree := 0.0) -> void:
	etat = nouveau
	_minuteur = duree

func _distance_joueur() -> float:
	if _joueur == null:
		return INF
	return absf(_joueur.global_position.x - global_position.x)

func _vers_joueur() -> float:
	return signf(_joueur.global_position.x - global_position.x)

# --- Les états ---

func _patrouille() -> void:
	if global_position.x <= limite_gauche:
		_dir = 1.0
	elif global_position.x >= limite_droite:
		_dir = -1.0
	velocity.x = _dir * vitesse_patrouille
	if _distance_joueur() < portee_detection:
		_changer_etat(Etat.TRAQUE)

func _traque() -> void:
	if _joueur == null:
		_changer_etat(Etat.PATROUILLE)
		return
	_dir = _vers_joueur()
	velocity.x = _dir * vitesse_traque
	if _distance_joueur() > portee_detection * 1.5:
		_changer_etat(Etat.PATROUILLE)       # il perd la trace
	elif _distance_joueur() < portee_charge:
		_dir = _vers_joueur()
		_changer_etat(Etat.CHARGE, 0.8)      # il fonce droit devant pendant 0,8 s

func _charge(delta: float) -> void:
	velocity.x = _dir * vitesse_charge
	_minuteur -= delta
	if _minuteur <= 0.0 or is_on_wall():
		_changer_etat(Etat.RECUPERATION, 1.2)

func _recuperation(delta: float) -> void:
	velocity.x = move_toward(velocity.x, 0.0, 800.0 * delta)
	_minuteur -= delta
	if _minuteur <= 0.0:
		_changer_etat(Etat.TRAQUE)

func _fuite(delta: float) -> void:
	if _joueur != null:
		_dir = -_vers_joueur()
	velocity.x = _dir * vitesse_fuite
	_minuteur -= delta
	if _minuteur <= 0.0:
		_changer_etat(Etat.TRAQUE)

func _assomme(delta: float) -> void:
	velocity.x = 0.0
	_minuteur -= delta
	if _minuteur <= 0.0:
		_changer_etat(Etat.TRAQUE)

# --- Réactions externes ---

func assommer(duree: float) -> void:        # appelée par un piège
	_changer_etat(Etat.ASSOMME, duree)

func _on_recu_degats(montant: int, _origine: Vector2) -> void:
	vie -= montant
	if vie <= 0:
		queue_free()                         # à remplacer par une animation de mort et du butin
	elif vie < vie_max * seuil_fuite and etat != Etat.FUITE:
		_changer_etat(Etat.FUITE, 4.0)
```

**Lis le code en suivant le schéma.** Chaque fonction `_etat()` fait deux choses : le comportement (régler `velocity`), puis la décision de changer d'état. C'est ce qui rend la machine facile à agrandir : pour un nouveau comportement, tu ajoutes une valeur à `Etat`, une fonction et une ligne dans `match`.

**Les réglages sont dans l'inspecteur** (`@export`) : c'est là que tu donnes sa personnalité à chaque monstre, sans toucher au code.

## Étape 3 : les pièges

Un piège est une `Area2D` qui attend qu'un monstre entre dedans. `scripts/piege.gd` :

```gdscript
extends Area2D

@export var duree_assomme := 3.0
@export var usage_unique := true

func _ready() -> void:
	body_entered.connect(_on_body_entered)

func _on_body_entered(corps: Node2D) -> void:
	if corps.has_method("assommer"):
		corps.assommer(duree_assomme)
		if usage_unique:
			queue_free()
```

Règle sa **couche** sur 8 (pieges) et son **masque** sur 3 (monstres). Crée la scène `scenes/piege.tscn` avec un `Sprite2D` et une `CollisionShape2D`.

**Poser un piège depuis le héros** : ajoute au script du héros :

```gdscript
@export var scene_piege: PackedScene     # glisse piege.tscn ici dans l'inspecteur
@export var pieges_max := 3
var pieges_restants := 3

func _poser_piege() -> void:
	if pieges_restants <= 0:
		return
	pieges_restants -= 1
	var piege := scene_piege.instantiate()
	piege.global_position = global_position
	get_parent().add_child(piege)
```

et, dans `_physics_process`, avec une nouvelle action `piege` dans l'Input Map :

```gdscript
	if Input.is_action_just_pressed("piege"):
		_poser_piege()
```

## Étape 4 : l'arène longue

1. Crée une scène `arene.tscn` avec un niveau très large (module 5) : plusieurs écrans de longueur, des plateformes, des obstacles.
2. Place le héros (groupe `joueur`) à gauche, le monstre à droite, avec ses `limite_gauche` et `limite_droite` réglées.
3. La `Camera2D` suit le héros, avec des limites aux extrémités du niveau.
4. **Pour que le joueur sache où est le monstre** quand il est hors de l'écran : ajoute dans l'interface (module 9) une flèche sur le bord de l'écran qui indique sa direction.

## Ce qui rend une chasse amusante

- **Des signaux lisibles** : une courte animation de préparation avant la charge (le joueur peut réagir).
- **De l'espace pour faire des erreurs** : un moment de récupération du monstre après une attaque, pour que le joueur puisse contre-attaquer.
- **Des choix** : suivre le monstre de près, ou courir en avant poser un piège.
- **De la variété** : chaque monstre, avec les mêmes états mais des réglages et des attaques différents, se joue différemment.

## Exercice

1. Fais tourner l'arène avec le monstre ci-dessus et des carrés de couleur à la place des sprites.
2. Lance le jeu et joue-le : le monstre est-il menaçant ? Injuste ? Ennuyeux ? Règle les vitesses et les durées jusqu'à ce que ce soit plaisant.
3. Ajoute un état **SAUT** : le monstre saute par-dessus le joueur au lieu de charger (indice : une `velocity.y` négative au moment de la transition).
4. Ajoute le piège et vérifie que le monstre s'assomme.
5. Note ce qui t'étonne : c'est ce que tu dois corriger.

## Erreurs fréquentes

- **Le monstre ne bouge pas** : `_joueur` est `null` parce que le héros n'est pas dans le groupe `joueur`.
- **Le piège ne se déclenche pas** : couche et masque mal réglés (module 7).
- **Le monstre change d'état à chaque image** : une transition qui se déclenche immédiatement (ex : `_charge` qui revient tout de suite à `RECUPERATION` parce que `is_on_wall()` est vrai).

## Pour aller plus loin

Plus tard, quand tu auras une dizaine d'états, passe d'un `match` géant à un **nœud par état** (chaque état est un petit script) : le code reste lisible. Recherche « state machine pattern Godot 4 » ; la documentation officielle a une page sur les scripts réutilisables dans « Best practices ».
