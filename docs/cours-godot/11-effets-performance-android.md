# Module 11 : effets, performance, export Android

## Objectif

Ajouter les effets qui font ton style visuel, mesurer ce qu'ils coûtent, et mettre le jeu sur ton téléphone.

## 1. Les effets visuels (et leur coût)

Si tu pars sur le **HD**, ces effets font le style : ils ne sont pas optionnels. Si tu pars sur le **rétro**, ils sont facultatifs.

| Effet | Nœud ou technique | Coût sur mobile |
|---|---|---|
| Lumière 2D | `PointLight2D` (avec une image de halo), `DirectionalLight2D` pour une ambiance globale | Moyen à élevé : chaque lumière redessine les objets qu'elle éclaire. Limite leur nombre. |
| Relief par lumière | Normal maps sur les sprites (via une ressource `CanvasTexture`) | Élevé : demande une normal map pour chaque image. |
| Particules | `CPUParticles2D` (plus sûr sur mobile) ou `GPUParticles2D` | Faible à moyen. Teste `GPUParticles2D` sur ton téléphone avant de t'y fier. |
| Flou de profondeur | Un shader sur les couches du premier plan | Moyen. |
| Parallaxe | `Parallax2D` (module 5) | Faible. |
| Teinte et ambiance | `CanvasModulate` : une couleur appliquée à tout l'écran | Très faible, très efficace. |

**Conseil** : commence par `CanvasModulate` (l'ambiance de chaque région par une teinte) et la parallaxe, puis ajoute une lumière à la fois, en mesurant.

### Exemple : une torche

Ajoute un `PointLight2D`, règle **Texture** sur une image de halo (un cercle flou, que tu peux dessiner dans PixelForge), **Energy** à 1 ou 1,5, **Color** orange. Pour des ombres, active **Shadow > Enabled** et ajoute des `LightOccluder2D` aux objets qui doivent en projeter *(les ombres coûtent cher : à réserver au strict nécessaire)*.

## 2. Mesurer avant d'optimiser

Pendant le jeu, ouvre le **Débogueur** (en bas) > **Moniteurs**. Surveille :
- **FPS** : le nombre d'images par seconde. Vise 60 stable.
- **Mémoire vidéo** et **mémoire des textures** : elles montent quand tu charges un gros monstre.
- **Nombre d'objets** et **appels de dessin**.

Puis le **Profileur** : il te dit quelle fonction prend le temps. N'optimise que ce qu'il montre.

**La règle d'or** : un test sur un vrai téléphone vaut dix tests sur PC. Un PC est cent fois plus puissant qu'un téléphone modeste. Si ton jeu tourne bien sur PC et mal sur le téléphone, c'est normal ; seul le téléphone compte.

### Réduire la mémoire
- **Planches de sprites** (« atlas ») : regroupe les images d'un même personnage dans une seule image pour moins d'appels de dessin.
- **Ne charge que ce qui sert** : décharge le monstre et le niveau précédents (le changement de scène le fait pour toi).
- **Gros sprites** : le monstre à 5× le héros est le plus gros consommateur. Pense à le découper en pièces animées (tête, bras, queue) plutôt qu'à le dessiner en entier à chaque image.
- **Compression** : pour le pixel art, garde **Lossless** (la compression de textures abîme les pixels nets). Tu peux utiliser une compression pour les fonds flous.

## 3. Exporter vers Android

Le premier export est souvent le plus long : ensuite tout va vite. Suis la page de la documentation « Exporting for Android », qui est à jour pour ta version. Résumé :

1. **Installe le JDK** (Java Development Kit, version recommandée par la documentation) et l'**Android SDK** (via Android Studio, ou les outils en ligne de commande seuls).
2. Dans Godot : **Éditeur > Paramètres de l'éditeur > Export > Android** : indique les chemins du JDK et du SDK.
3. **Installe les modèles d'export** : **Éditeur > Gérer les modèles d'export > Télécharger et installer**.
4. **Active la compression de textures pour mobile** : **Projet > Paramètres du projet > Rendering > Textures > VRAM Compression > Import ETC2 ASTC** *(Godot l'exige pour l'export Android en rendu Compatibility ; à vérifier si l'éditeur te le signale)*.
5. **Projet > Exporter > Ajouter > Android.** Pour un APK de test, laisse la clé de débogage par défaut ; coche l'architecture **arm64-v8a**.
6. **Pour tester vite** : active le **débogage USB** sur ton téléphone (Options pour les développeurs), branche-le au PC, et utilise l'icône Android en haut à droite de l'éditeur (déploiement en un clic).
7. **Pour le partager avec ton groupe** : exporte un **APK** (menu Exporter), envoie-le. Chaque joueur doit autoriser l'installation d'applications hors du Play Store.

**Pas de PC pour cette étape ?** Le téléphone seul ne suffit pas : l'export demande un ordinateur. Prévois-le pour tes séances de test.

## 4. Ton protocole de test sur téléphone

À chaque test, note :
- le **modèle** du téléphone ;
- la **cadence** moyenne et la pire (chute dans le combat de chasse ?) ;
- ce qui est **illisible** (boutons cachant l'action, texte trop petit) ;
- ce qui **chauffe** : un jeu qui fait chauffer le téléphone est trop gourmand, même s'il tient 60 images par seconde.

C'est avec ces notes que tu décideras de couper un effet ou un détail.

## Exercice

1. Ajoute un `CanvasModulate` de couleur différente à deux niveaux : ils doivent avoir une ambiance distincte.
2. Ajoute une lumière, mesure les FPS avant et après sur le téléphone.
3. Exporte un APK de ta scène de plateforme, installe-le, joue cinq minutes, remplis le protocole de test.

## Erreurs fréquentes

- **L'export échoue** : un chemin du JDK ou du SDK incorrect, ou une version non prise en charge (lis le message de la console).
- **Écran noir sur le téléphone** : souvent un problème de rendu. Vérifie que le projet est en Compatibility.
- **Jeu fluide sur PC et saccadé sur le téléphone** : normal. Mesure sur le téléphone.

## Pour aller plus loin

Documentation : « Exporting for Android », « Performance » (section « General optimization tips ») et « 2D lights and shadows ».
