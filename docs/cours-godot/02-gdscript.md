# Module 2 : GDScript, les bases

## Objectif

Lire et écrire de petits scripts. GDScript ressemble à Python : l'indentation (le décalage des lignes) donne la structure.

## À savoir

- Un **script** est attaché à un nœud et lui donne un comportement.
- Un script commence par `extends` suivi du type de nœud auquel il s'applique.
- Godot appelle automatiquement certaines fonctions : `_ready()` (une fois, quand le nœud est prêt), `_process(delta)` (à chaque image) et `_physics_process(delta)` (à intervalle fixe, pour la physique). `delta` est le temps écoulé depuis la dernière image : on multiplie les vitesses par `delta` pour que le jeu aille à la même vitesse sur tous les appareils.

## Les notions essentielles

### Variables et types

```gdscript
extends Node2D

var vie := 100              # Godot devine que c'est un entier
var nom: String = "Krunt"   # type écrit explicitement
const GRAVITE := 1500.0     # constante : ne change jamais

@export var vitesse := 200.0  # visible et modifiable dans l'inspecteur
```

Écrire le type (`:=` ou `: Type`) aide Godot à repérer les erreurs et accélère le jeu : prends l'habitude de le faire.

### Fonctions

```gdscript
func perdre_vie(montant: int) -> void:
	vie -= montant
	if vie <= 0:
		mourir()

func mourir() -> void:
	queue_free()   # supprime ce nœud
```

### Conditions et boucles

```gdscript
if vie > 50:
	print("En forme")
elif vie > 0:
	print("Blessé")
else:
	print("Mort")

for i in range(3):
	print(i)    # affiche 0, 1, 2
```

### Tableaux et dictionnaires

```gdscript
var armes := ["épée", "arc", "hache"]
armes.append("lance")

var palette := {"peau": 2, "cheveux": 5}
print(palette["peau"])   # affiche 2
```

### Énumérations et `match` (très utile pour les états)

```gdscript
enum Etat { REPOS, MARCHE, ATTAQUE }
var etat := Etat.REPOS

func mettre_a_jour() -> void:
	match etat:
		Etat.REPOS:
			print("il se repose")
		Etat.MARCHE:
			print("il marche")
		Etat.ATTAQUE:
			print("il attaque")
```

### Signaux (la façon dont les nœuds se parlent)

Un **signal** est un message qu'un nœud envoie sans savoir qui l'écoute.

```gdscript
signal vie_changee(nouvelle_vie: int)

func perdre_vie(montant: int) -> void:
	vie -= montant
	vie_changee.emit(vie)   # envoie le message
```

Un autre nœud s'y abonne :

```gdscript
func _ready() -> void:
	$Joueur.vie_changee.connect(_on_vie_changee)

func _on_vie_changee(nouvelle_vie: int) -> void:
	$BarreDeVie.value = nouvelle_vie
```

Règle d'or : **on appelle vers le bas, on signale vers le haut**. Un parent peut appeler les fonctions de ses enfants ; un enfant envoie des signaux à son parent sans le connaître.

### Accéder à d'autres nœuds

```gdscript
$Sprite2D                       # enfant direct nommé Sprite2D
$Corps/Epee                     # petit-enfant
@onready var sprite: Sprite2D = $Sprite2D   # garde la référence, prête dès _ready()
get_node("../Autre")            # écriture longue
```

`@onready` règle un piège classique : les enfants n'existent pas encore avant `_ready()`.

**Écris le type de la variable** (`: Sprite2D`, `: AnimatedSprite2D`...) quand elle pointe vers un nœud : sans lui, Godot ne sait pas quelles fonctions le nœud possède et peut refuser ton code ou te donner de fausses erreurs.

## Exercice

Crée un nœud `Node2D` avec un script qui :
1. déclare `@export var vitesse := 100.0` ;
2. dans `_process(delta)`, déplace le nœud vers la droite : `position.x += vitesse * delta` ;
3. affiche dans la console (`print`) quand le nœud dépasse x = 500.

Puis change `vitesse` dans l'inspecteur sans toucher au code.

## Erreurs fréquentes

- **Mélanger tabulations et espaces** : GDScript refuse. Garde les tabulations que Godot insère.
- **Oublier `@onready`** devant une variable qui pointe vers un enfant (`null instance`).
- **Oublier `delta`** : le jeu va deux fois plus vite sur un appareil deux fois plus rapide.

## Pour aller plus loin

Documentation : « GDScript reference » et « GDScript style guide ».
