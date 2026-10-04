# Module 1 : installer, créer le projet, régler l'écran

## Objectif

Avoir un projet Godot qui se lance, avec le bon rendu et les bons réglages d'écran pour Android.

## À savoir

- **Godot** est un seul programme : l'éditeur et le moteur. Il n'a pas besoin d'installation, c'est un exécutable portable.
- **Un projet** est un dossier contenant un fichier `project.godot`.
- **Compatibility** est le mode de rendu à choisir : c'est le plus prudent pour couvrir beaucoup de téléphones, y compris les modestes. Les autres modes (Forward+, Mobile) demandent un GPU plus récent. Ce choix se fait à la création du projet ; on peut le changer plus tard mais c'est plus pénible.

## Pas à pas

1. **Télécharge Godot 4** (version « standard », pas « .NET », sauf si tu veux le C#) depuis le site officiel https://godotengine.org/download. Mets l'exécutable sur ta clé USB.
2. **Lance Godot.** Dans le gestionnaire de projets, clique sur « Nouveau projet ».
3. **Nom** : `jeu-b`. **Dossier** : celui du dépôt. **Rendu** : choisis **Compatibility**.
4. Clique sur « Créer ». L'éditeur s'ouvre.
5. **Fais connaissance avec l'éditeur** : à gauche, le **dock Scène** (l'arbre des nœuds) et le **système de fichiers** ; au centre, la **vue** (2D, 3D, Script) ; à droite, l'**inspecteur** (les propriétés du nœud sélectionné).
6. **Crée une première scène** : clique sur « Scène 2D », renomme le nœud en `Test`, enregistre-la sous `scenes/test.tscn`, puis lance-la avec F6 (« Lancer la scène actuelle »). Une fenêtre grise s'ouvre : c'est normal.

## Réglages d'écran (Projet > Paramètres du projet)

Cherche chaque réglage avec la barre de recherche, et active « Paramètres avancés » en haut si nécessaire.

### Si tu pars sur le HD (image de 720 px de haut)

| Réglage | Valeur |
|---|---|
| Display > Window > Size > Viewport Width | 1280 |
| Display > Window > Size > Viewport Height | 720 |
| Display > Window > Stretch > Mode | `canvas_items` |
| Display > Window > Stretch > Aspect | `expand` |
| Display > Window > Handheld > Orientation | `landscape` |
| Rendering > Textures > Canvas Textures > Default Texture Filter | `Linear` (ou `Nearest` si tu veux voir les pixels) |

### Si tu pars sur le rétro 32 bits (image de 360 px de haut)

| Réglage | Valeur |
|---|---|
| Viewport Width / Height | 640 / 360 |
| Stretch > Mode | `viewport` |
| Stretch > Aspect | `expand` |
| Stretch > Scale Mode | `integer` *(à vérifier selon la version)* |
| Default Texture Filter | `Nearest` |

**Ce que fait `expand`** : l'image garde la même hauteur et gagne en largeur sur les téléphones très larges (20:9). C'est ce qui évite les bandes noires latérales. Conséquence : ton décor doit déborder des deux côtés de la zone d'action, et ton interface doit se placer par rapport aux bords de l'écran (module 9).

**Ce que fait `integer`** : l'image est agrandie par multiples entiers, donc les pixels restent réguliers.

## Exercice

Crée la scène `test.tscn` avec un nœud `ColorRect` (un rectangle de couleur) de la taille de l'écran, lance-la, puis change la taille de la fenêtre pour voir comment l'image réagit. Fais-le avec les deux jeux de réglages (HD et rétro) et note ce que tu constates.

## Erreurs fréquentes

- **Mauvais rendu choisi** : si tu as oublié Compatibility, change-le dans les paramètres du projet (Rendering > Renderer) puis redémarre l'éditeur.
- **Pixels flous** : le filtre de texture par défaut n'est pas `Nearest` (pour le pixel art).
- **Rien ne se passe en lançant le projet** : aucune « scène principale » n'est définie. Clique droit sur ta scène > « Définir comme scène principale ».

## Pour aller plus loin

Documentation : « Multiple resolutions » (plusieurs résolutions) et « Project settings ».
