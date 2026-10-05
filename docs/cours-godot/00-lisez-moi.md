# Cours Godot 4 pour « La première chasse »

Cours conçu pour le Jeu B (jeu Android lié à CRS) : exploration en vue 3/4, quêtes en plateforme, chasses en arène longue contre un monstre mobile.
Rédigé le 2026-10-04.

## À lire d'abord : ce que ce cours est et n'est pas

- **Il est ciblé.** Il t'amène à une chose précise : une première chasse jouable sur ton téléphone. Il ne couvre pas tout Godot.
- **Il n'a pas été testé.** Je n'ai pas pu installer Godot pour exécuter le code. Les exemples sont écrits pour Godot 4 à partir de ma connaissance du moteur. Quand un menu ou un nom de nœud a changé selon les versions, c'est signalé par *(à vérifier)*. La documentation officielle fait foi : https://docs.godotengine.org/fr/ (ou `/en/stable/` pour la version anglaise, plus à jour).
- **Version visée : Godot 4.3 ou plus récent.** Deux changements importants depuis 4.3 : le nœud `TileMapLayer` remplace `TileMap`, et `Parallax2D` remplace `ParallaxBackground`.
- **Rendu : Compatibility.** À choisir à la création du projet (module 1). C'est le choix le plus prudent pour les téléphones variés.

## Prérequis

- Un PC (Windows ou Linux) avec Godot 4, qui existe en version portable : un seul exécutable à mettre sur ta clé USB.
- Aucune expérience de programmation requise : le module 2 part de zéro.
- Des sprites de test. Pas besoin de beaux sprites : un carré de couleur suffit pour apprendre.

## Plan

| Module | Contenu | Résultat |
|---|---|---|
| 1 | Installer, créer le projet, réglages d'écran | Un projet qui se lance, à la bonne résolution |
| 2 | GDScript : les bases | Tu lis et écris des petits scripts |
| 3 | Scènes, nœuds, sprites, animation | Un personnage animé à l'écran |
| 4 | Héros de plateforme | Un héros qui court et saute |
| 5 | Tuiles, niveaux, parallaxe | Un niveau avec sol, plateformes, décor |
| 6 | Exploration en vue 3/4 | Un héros qui se déplace en vue de dessus |
| 7 | Combat : hitbox et hurtbox | Des coups qui touchent et font des dégâts |
| 8 | Le monstre de chasse et les pièges | Le cœur du jeu |
| 9 | Interface, tactile, écrans larges | Un jeu jouable au doigt |
| 10 | Données, sauvegarde, palettes, lien CRS | Sauvegarde, export du personnage, changement de couleurs |
| 11 | Effets, performance, export Android | Un APK sur ton téléphone |
| 12 | Projet : la première chasse | Tout assemblé, avec une liste de contrôle |
| 13 | Animation et hitbox, cours complet (à lire avec les modules 3 et 7) | Budget d'images, phases d'une attaque, hitbox par arme |

Suis les modules dans l'ordre. Chacun se termine par un **exercice** : ne passe pas au suivant tant qu'il n'est pas fait.

## Organisation du projet

Mets le projet Godot dans son propre dossier, par exemple `jeu-b/`, avec un fichier `.gitignore` qui exclut le dossier `.godot/` (cache de Godot, régénéré automatiquement). Ainsi une session Claude Code sur ton Termux peut lire tes scripts `.gd` et tes scènes `.tscn` (ce sont des fichiers texte) pour t'aider à les corriger.

```
jeu-b/
  project.godot
  scenes/          les scènes (.tscn)
  scripts/         les scripts (.gd)
  assets/
    sprites/       images des personnages et monstres
    tuiles/        images des tuiles
    audio/
  donnees/         palettes, objets, monstres (JSON)
```

## Règles de travail conseillées

1. **Une scène = une chose** (le héros, le monstre, un piège, un niveau). On assemble en plaçant les scènes les unes dans les autres.
2. **Teste tout de suite.** Appuie sur F5 (ou le bouton lecture) après chaque petit changement.
3. **Utilise des carrés de couleur** tant que tu n'as pas de sprites : on teste les mécaniques d'abord, l'art ensuite.
4. **Commit souvent** : une version qui marche, c'est une version à laquelle revenir.

## Ressources officielles

- Documentation : https://docs.godotengine.org/en/stable/
- Premier jeu en 2D (tutoriel officiel) : section « Your first 2D game » de la documentation
- Référence GDScript : section « GDScript » de la documentation
