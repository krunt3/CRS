# Module 9 : interface, tactile, écrans larges

## Objectif

Un jeu jouable au doigt sur un téléphone, avec une interface qui ne se fait pas couper par les encoches.

## À savoir

- Les **nœuds `Control`** servent à l'interface (boutons, barres, textes). Leurs positions se règlent par rapport aux **ancres** : ce sont elles qui permettent à l'interface de s'adapter aux écrans de toutes tailles.
- Les interfaces vivent dans un **`CanvasLayer`**, un calque à part qui ne bouge pas avec la caméra.

## Étape 1 : le HUD (barre de vie, pièges restants)

1. Crée une scène `scenes/hud.tscn` : racine `CanvasLayer`, enfant `Control` (disposition : « Plein écran »), puis un `MarginContainer` avec une `ProgressBar` (la vie) et un `Label` (les pièges).
2. **Ancre le HUD aux bords** : sélectionne le `MarginContainer`, utilise le menu « Disposition » > « Haut à gauche ». Ainsi il suit le coin même si l'écran est plus large.
3. Dans `MarginContainer`, règle les marges (Theme Overrides > Constants) à environ 24 px pour s'écarter des coins arrondis.

Un script simple pour le mettre à jour :

```gdscript
extends CanvasLayer

@onready var barre: ProgressBar = $Control/MarginContainer/VBoxContainer/BarreVie
@onready var pieges: Label = $Control/MarginContainer/VBoxContainer/Pieges

func definir_vie(valeur: int, maximum: int) -> void:
	barre.max_value = maximum
	barre.value = valeur

func definir_pieges(nombre: int) -> void:
	pieges.text = "Pièges : %d" % nombre
```

Le héros appelle ces fonctions quand sa vie ou ses pièges changent (ou, mieux, il envoie un signal que le HUD écoute : « on signale vers le haut »).

## Étape 2 : la zone sûre (encoches, coins arrondis, barre de gestes)

Sur Android, la zone sûre est la partie de l'écran qui n'est pas masquée. Godot permet de la lire :

```gdscript
func _ready() -> void:
	var zone := DisplayServer.get_display_safe_area()   # Rect2i en pixels écran
	print(zone)
```

La zone est en **pixels de l'écran réel**, pas en pixels de ton image de jeu. Il faut la convertir : lis la taille de la fenêtre (`DisplayServer.window_get_size()`) et la taille de ton image (`get_viewport().get_visible_rect().size`) pour calculer les marges proportionnelles, puis applique-les en marges du `MarginContainer`. *(À tester sur un vrai téléphone avec une encoche : les valeurs varient selon l'appareil.)*

**Plan B simple** : une marge fixe généreuse (5 % de la largeur de chaque côté). Moins précis, mais robuste, et suffisant pour une démo.

## Étape 3 : les commandes tactiles

Les boutons tactiles se branchent sur les **mêmes actions** que le clavier : le code du héros ne change pas.

1. Dans ton `CanvasLayer`, ajoute des nœuds **`TouchScreenButton`**.
2. Pour chacun, règle **Texture Normal** (l'image du bouton) et **Action** (le nom de l'action : `saut`, `attaque`, `piege`...). Quand le doigt touche le bouton, Godot déclenche l'action comme une touche.
3. Place les boutons d'attaque et de saut en bas à droite, la croix de direction (`gauche`, `droite`) en bas à gauche.
4. **Taille minimale** : un bouton fait au moins 8 à 10 mm physiques pour un pouce. Sur un écran de 1280 px de large (environ 14 cm), cela fait à peu près 90 px.
5. **Masque d'affichage** : dans l'inspecteur, **Visibility Mode** : choisis « Touchscreen Only » pour que les boutons n'apparaissent que sur téléphone, pas sur PC.

### Le joystick flottant (plus confortable)

Un joystick qui apparaît là où le pouce se pose est plus confortable que des boutons fixes, mais Godot n'en fournit pas de natif. Deux options :
- l'écrire toi-même avec un `Control` qui écoute `InputEventScreenTouch` et `InputEventScreenDrag`, puis appelle `Input.action_press("droite", force)` / `Input.action_release(...)` ;
- utiliser une extension de la communauté *(à vérifier : cherche « virtual joystick » dans l'Asset Library, et vérifie qu'elle est maintenue et compatible Godot 4)*.

Pour la première démo, des boutons fixes suffisent.

## Étape 4 : l'écran extensible

Tu as réglé `Stretch Aspect = expand` au module 1. Conséquences à vérifier :
- ton **décor** doit être plus large que la zone d'action (module 5) ;
- ton **HUD** s'ancre aux coins, pas à des positions absolues ;
- tu testes sur plusieurs formes de fenêtre : redimensionne la fenêtre du jeu à des rapports 16:9, 20:9 et 4:3.

## Le jeu avec une manette

Branche une manette et vérifie que les actions de l'Input Map réagissent. Si tu as déjà associé des boutons (module 4), elle fonctionne sans autre code. Prévois de **masquer les boutons tactiles** quand une manette est détectée *(à faire en écoutant `Input.joy_connection_changed`)*.

## Exercice

1. Crée un HUD avec une barre de vie et un compteur de pièges, branchés sur ton héros.
2. Ajoute quatre boutons tactiles (gauche, droite, saut, attaque).
3. Redimensionne la fenêtre en 16:9, 20:9 et 4:3 : rien ne doit être coupé ni mal placé.
4. Exporte sur ton téléphone (module 11) et joue vraiment avec : sont-ce les bons endroits pour tes pouces ? Les boutons te cachent-ils l'action ?

## Erreurs fréquentes

- **Les boutons ne réagissent pas** : le nom de l'action ne correspond pas à celui de l'Input Map.
- **Le HUD est coupé** : ancres mal réglées ou pas de marge.
- **Les boutons s'affichent sur PC** : le mode de visibilité n'est pas réglé sur « Touchscreen Only ».

## Pour aller plus loin

Documentation : « Size and anchors », « Using containers », « InputEvent » et « Multiple resolutions ».
