# Test PixelLab : le héros en 64 px ou en 96 px ?

Rédigé le 2026-10-05. Ce test sert à confirmer ou corriger le scénario C de la bible graphique (formats PixelForge actuels, héros de 32×64 px).

## Pourquoi PixelLab, et un outil de contrôle

D'après des comparatifs que je dois relativiser (plusieurs sont écrits par des concurrents ou des vendeurs), deux outils produisent du **vrai pixel art à taille exacte**, au lieu d'imiter l'apparence :

| Outil | Ce qu'on en sait | Pour ce test |
|---|---|---|
| **PixelLab** (pixellab.ai) | Tailles de 16 à 512 px, personnages en 4 ou 8 directions, animation par squelette (cases de 16, 32, 64, 128, 256), outil web « Characters », extension Aseprite, essai gratuit sans carte bancaire | **Outil principal** : c'est celui que tu comptes utiliser |
| **Retro Diffusion** | Tailles exactes de 16 à 384 px, palette limitée, extension Aseprite (achat), API | **Contrôle facultatif** : une deuxième opinion si PixelLab te déçoit |

Les générateurs d'images généralistes (ChatGPT et équivalents) ne conviennent pas : ils produisent une image haute résolution qui imite le pixel art, avec des pixels irréguliers.

## Ce que l'essai gratuit permet

D'après des résumés de recherche, non confirmés : 40 générations rapides, puis 5 plus lentes par jour ; images jusqu'à 200×200 ; outils limités. **L'animation par squelette demande l'abonnement « Tier 1 ».** Les essais 1 à 3 ci-dessous tiennent dans l'essai gratuit ; l'essai 4 demande un mois d'abonnement.

## Prompt du héros (à adapter)

À coller dans la description du personnage. Remplace les éléments entre crochets par l'apparence réelle de ton héros (krunt).

```
A human monster hunter in a medieval fantasy world, lean athletic build, short [hair color] hair, [skin tone] skin, wearing worn leather armor with a few light steel plates on the shoulders and forearms, a [dark red] scarf, a belt with pouches, sturdy boots, holding a large single-handed sword at his side. Serious, determined face. Side view, facing right, standing idle pose. Clean pixel art, selective dark outline of one pixel, flat shading with three tones per material, limited palette of about 16 colors, no anti-aliasing, no gradients, no dithering, no blur, transparent background.
```

Si l'outil propose un champ séparé « négatif », ajoute :

```
blurry, smooth gradients, anti-aliasing, 3D render, painting, photo, text, watermark, cropped, extra limbs
```

## Réglages à choisir dans l'outil

| Réglage | Valeur | Remarque |
|---|---|---|
| Taille de la case (canevas) | **128×128** | Case carrée, héros à environ 50 % de la hauteur |
| Taille du personnage | Réglée pour obtenir **64 px de haut** (essai 1), puis **96 px de haut** (essai 2) | L'outil propose une option de taille ou d'échelle en pourcentage : 64/128 = 50 %, 96/128 = 75 %. Vérifie le résultat avec le script, pas à l'œil |
| Proportions | Bipède réaliste (essais 1 et 2), bipède semi-chibi (essai 3) | Options citées dans la documentation de l'outil |
| Vue | De profil (side), si l'option existe ; sinon la vue la plus proche | À vérifier dans l'outil |
| Directions | Une seule pour commencer (est), puis 4 si l'essai est concluant | Économise les générations gratuites |
| Fond | Transparent | |

## Les essais

| N° | Essai | Case | Hauteur du héros | Proportions | Abonnement |
|---|---|---|---|---|---|
| 1 | Scénario C : héros du format PixelForge actuel | 128×128 | **64 px** | réaliste | non |
| 2 | Scénario A : héros plus grand | 128×128 | **96 px** | réaliste | non |
| 3 | Lisibilité du visage à 64 px | 128×128 | 64 px | **semi-chibi** | non |
| 4 | Cycle de marche de 8 images, avec le meilleur des essais 1 à 3 | 128×128 | celui retenu | celui retenu | **oui (Tier 1)** |
| 5 | Boss à 2× le héros | 256×256 | 128 px | réaliste | oui |

**Pour chaque essai, génère jusqu'à 4 variantes** du même prompt et garde la meilleure. Note combien de variantes ont été nécessaires : c'est le « taux de rejet ».

## Mesurer au lieu de juger à l'œil

Le script `outils/mesure_sprite.py` vérifie les points objectifs. Il nécessite Pillow (`pip install pillow`).

```
python3 outils/mesure_sprite.py heros_64.png --case 128 --hauteur 64
python3 outils/mesure_sprite.py marche_*.png --case 128 --hauteur 64
```

Il indique, pour chaque image : la hauteur et la largeur réelles du personnage, sa part de la case, la marge sous les pieds, le nombre de couleurs, les pixels semi-transparents (il ne doit y en avoir aucun), et un éventuel **agrandissement caché** (un sprite « petit » agrandi, fréquent avec les IA). Sur une série d'images, il compare la hauteur, la position des pieds et les couleurs d'une image à l'autre : c'est le test de la cohérence d'animation.

## Grille de décision

| Critère | Seuil | Essai 1 (64) | Essai 2 (96) | Essai 3 (chibi) |
|---|---|---|---|---|
| Hauteur mesurée | cible ± 4 px | | | |
| Pixels semi-transparents | 0 | | | |
| Agrandissement caché | aucun (x1) | | | |
| Couleurs | ≤ 32 | | | |
| Visage lisible à taille réelle (oui / non) | oui | | | |
| Armure et arme reconnaissables (oui / non) | oui | | | |
| Variantes nécessaires pour un bon résultat | ≤ 4 | | | |
| Envie de garder le résultat (oui / non) | oui | | | |

**Règle de décision :**
- Si l'essai 1 (64 px) passe, **le scénario C est confirmé** : on verrouille les formats actuels.
- Si l'essai 1 échoue sur la lisibilité mais l'essai 2 passe, **on passe au scénario A** (héros de 96 px, formats ×1,5).
- Si seul l'essai 3 (semi-chibi) passe, **on change de style de proportions** avant de changer de taille.
- Si aucun ne passe, **on essaie Retro Diffusion** avant de conclure.

## Cohérence d'animation (essai 4)

Mêmes mesures sur les 8 images de marche. Seuils : écart de hauteur ≤ 4 px, écart de position des pieds ≤ 2 px, aucune couleur nouvelle d'une image à l'autre. En plus, regarde l'animation en boucle à 10 images par seconde : les pas sont-ils réguliers, les pieds glissent-ils, le visage change-t-il ?

## À consigner dans la bible graphique

Taille retenue, nombre de variantes par essai, résultat de chaque ligne de la grille, temps passé par essai.


## Résultats de l'essai 1 (2026-10-05)

Essai réalisé sur l'essai gratuit de PixelLab : outil « Characters », modèle « mannequin », vue de profil (« side »), **8 directions**, case de **64×64** (et non 128×128), sans animation. Le prompt a été collé **avec ses crochets non remplacés** (`[hair color]`, `[skin tone]`, `[dark red]`), donc l'apparence n'est pas celle de krunt.

### Mesures (script `outils/mesure_sprite.py`, 8 images)

| Critère | Seuil | Résultat | Verdict |
|---|---|---|---|
| Hauteur du héros | 64 ± 4 px | 62 à 63 px | OK |
| Part de la case | ≈ 50 % (case de 128) | **97 %** (case de 64) | À corriger : aucune marge |
| Marge sous les pieds | 4 px | 1 à 2 px | À corriger |
| Pixels semi-transparents | 0 | 0 | OK |
| Agrandissement caché | aucun | aucun (x1) | OK |
| Stabilité hauteur et pieds sur les 8 directions | écart ≤ 4 et ≤ 2 px | 1 et 1 px | OK |
| Couleurs par image | ≤ 32 | **50 à 55** (58 sur l'ensemble) | **Dépassé** : le prompt demandait environ 16 |

### Lecture visuelle

- **Armure, écharpe, épée, bottes : tous reconnaissables** à 62 px de haut. Les contours sont propres, sans flou ni lissage.
- **Les proportions sont massives** (épaules très larges, torse épais), alors que le prompt disait « lean athletic ». Largeur mesurée : 39 px (profil) à 57 px (face) pour 62 px de haut, soit bien plus que le gabarit 1:2 des formats PixelForge (32×64).
- **Le visage est petit et peu expressif.** Lisible de face (sud) et à l'ouest, presque absent de profil à l'est (caché derrière l'épaulière). La peau est pâle, verdâtre : aucun teint n'avait été précisé.
- **La vue « side » à 8 directions produit des vues de face et de dos droites**, pas des vues de dessus. Elles ne conviennent pas à l'exploration en 3/4 (il faudra une vue de dessus pour ce mode).

### Réduction du nombre de couleurs (réduction automatique, sans retouche)

| Couleurs | Résultat |
|---|---|
| 32 | Presque identique à l'original |
| 24 | Très proche, léger appauvrissement des tons de peau |
| 16 | Perte nette : la peau devient grise, les reflets du métal disparaissent |

**Conséquence : la règle « 16 couleurs par personnage » de la bible est trop stricte pour ce niveau de détail** sans retouche à la main. À 64 px, **24 à 32 couleurs** par personnage conservent le rendu.

### Verdict provisoire

- **Le scénario C est plausible** : un héros de 62 px de haut est lisible et propre. La taille n'est pas le problème.
- **Reste à tester** : la même chose dans une **case de 128**, puis une **animation** (essai 4, abonnement nécessaire). Une case de 64 sans marge ne permet ni coups d'épée, ni animation par squelette.
- **À corriger au prochain essai** : remplacer tous les crochets du prompt, préciser le teint et la silhouette, utiliser une image de référence (voir plus bas).
