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

D'après des résumés de recherche, non confirmés : 40 générations rapides, puis 5 plus lentes par jour ; images limitées à **64×64** (constaté par l'utilisateur le 2026-10-05 ; les résumés de recherche annonçaient 200×200) ; outils limités. **L'animation par squelette demande l'abonnement « Tier 1 ».** Les essais 1 à 3 ci-dessous tiennent dans l'essai gratuit ; l'essai 4 demande un mois d'abonnement.

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


## Résultats de l'essai 1 bis (2026-10-05)

Deuxième génération avec le **modèle de prompt non rempli** (crochets laissés tels quels). Même réglages que l'essai 1 : modèle « mannequin », vue de profil, 8 directions, case de 64×64.

| Critère | Résultat | Verdict |
|---|---|---|
| Hauteur du héros | 62 px sur les 8 images | OK |
| Part de la case | 97 %, marge de 1 px sous les pieds | À corriger (case de 128) |
| Pixels semi-transparents | 0 | OK |
| Agrandissement caché | aucun | OK |
| Stabilité hauteur et pieds | écart 0 px | OK |
| Couleurs | 46 à 48 par image (32 de face), 64 sur l'ensemble | Dépassé (cible 24 à 32) |

**Lecture visuelle :** meilleur que l'essai 1. Le visage est lisible dans les 8 directions (barbe, regard, cicatrice possible), les proportions sont plus ramassées, la silhouette est nette. Tenue : tunique verte, sangles de cuir croisées, une épaulière d'acier, brassards, épée courte à la main, long bâton sur le dos. C'est un bon point de départ, mais **ce n'est pas un personnage choisi** : l'outil a improvisé tous les détails.

Les couleurs restent au-dessus de la cible : réduction à 24 ou 32 couleurs nécessaire dans PixelForge (voir plus haut).


## Résultats de l'essai 1 ter : le chasseur en armure de wyverne rouge (2026-10-05)

Génération avec le prompt complet du personnage 1 (voir `prompts-personnages.md`), sur l'essai gratuit : case de **64×64** (**limite constatée de l'essai gratuit**), modèle « mannequin », vue de profil, 8 directions, sans animation.

| Critère | Résultat | Verdict |
|---|---|---|
| Hauteur du héros | 60 à 64 px (écart 4) | OK |
| Part de la case | 94 à 100 % | À corriger (case de 128) |
| Pieds (bas du personnage) | 61 à 64 px (écart 3) | À voir : écart légèrement supérieur au seuil de 2 px |
| Pixels semi-transparents, agrandissement caché | 0, aucun | OK |
| Couleurs | **63 à 64 par image, 95 sur l'ensemble** | Dépassé (cible 24 à 32) |

**Fidélité à la référence :** forte. Retrouvés : cheveux châtains en bataille, mine sérieuse, armure rouge-orange à écailles, grandes plumes orange et crème (devenues une grande cape-ailes), tablier vert d'eau, épée-fendoir ensanglantée sur l'épaule, bottes rouges. Écarts : proportions ramassées (grosse tête, jambes courtes, environ 3,5 têtes de haut contre 7 sur la référence), emblème bronze et détails de ceinture peu lisibles, épée qui masque la tête dans les vues de dos.

**Réduction à une palette commune de 32 couleurs** (les 8 directions partagent la même palette) : le rendu est conservé. Palette enregistrée dans `donnees/palette_chasseur_wyverne_32.json`. Défaut visible : la lame d'acier prend une teinte verdâtre, à retoucher dans PixelForge.

## Plan du mois d'abonnement (Tier 1)

**Pourquoi attendre :** l'essai gratuit est limité à 64×64 et l'animation par squelette demande le Tier 1. Prendre l'abonnement quand les prompts sont prêts et que la liste ci-dessous est préparée, pour utiliser le mois à fond, puis résilier.

| Ordre | À produire | Case | Taille du perso | Critère de réussite |
|---|---|---|---|---|
| 1 | Héros de profil, 4 directions | 128 | ≈ 64 px | Hauteur 64 ± 4, marge ≥ 4 px sous les pieds |
| 2 | Animation d'attente (6 images) et de marche (8 images), vers l'est | 128 | ≈ 64 px | Écart de hauteur ≤ 4 px, pieds ≤ 2 px, aucune couleur nouvelle |
| 3 | Course (8), saut (3), dégâts (2) | 128 | ≈ 64 px | Idem |
| 4 | Attaque en 3 temps de l'épée-fendoir (6 images par coup) | 128 | ≈ 64 px | L'épée reste dans la case |
| 5 | Héros en vue 3/4 (de dessus), 4 directions, marche | 64 ou 128 | ≈ 48 px | Lisible, même palette que le profil |
| 6 | Boss à 2× le héros | 256 | ≈ 128 px | Lisible, cohérent d'une image à l'autre |
| 7 | Jeu de tuiles (auto-tiling) de 32 px | – | – | Les bords se raccordent |
| 8 | Export de tout, test d'import dans Godot | – | – | Les animations tournent à 10 images/s |

**À noter à chaque étape :** nombre de générations consommées, variantes rejetées, temps passé. Le coût en générations de chaque animation n'est pas connu : commencer par les étapes 1 et 2 pour le mesurer avant de planifier le reste.


## Résultats de l'essai 3/4 : vue « low top-down » (2026-10-05)

Génération avec le prompt du personnage 1 (fin remplacée par la version 3/4), sur l'essai gratuit : vue **« low top-down »**, 8 directions, modèle « mannequin », sans animation. **Case de 48×48** (et non 64×64).

| Critère | Résultat | Verdict |
|---|---|---|
| Hauteur du héros | 42 à 47 px (cible 48 ± 4) | OK, mais écart de 5 px entre directions (les vues de dos sont plus petites) |
| Part de la case | 88 à 98 % | Aucune marge pour animer |
| Pieds (bas du personnage) | écart de 2 px | OK |
| Pixels semi-transparents, agrandissement caché | 0, aucun | OK |
| Couleurs | **64 par image, 115 sur l'ensemble** | Très au-dessus de la cible (24 à 32) |

**Lecture visuelle :**
- Le personnage reste **reconnaissable** : mêmes cheveux, même épée sur l'épaule, même cape-ailes orange, même tablier vert d'eau. La continuité avec la vue de profil est bonne.
- **Le visage est lisible** de face et de trois quarts (yeux sombres, cheveux), mais plus rude qu'à 64 px.
- **L'armure est devenue du bruit** : le motif d'écailles se transforme en taches orange, noires et crème à fort contraste, et la vue de face est moins lisible que la vue de profil à 64 px. La cape-ailes vue de dos, en grandes surfaces, se lit très bien.
- La vue « low top-down » reste proche d'une vue de face avec un léger angle : c'est ce qu'on attend d'une vue 3/4 à la Sea of Stars.

**Contrainte découverte :** l'animation par squelette de PixelLab n'accepte que des cases de **16, 32, 64, 128 ou 256 px** (documentation). Une case de **48 ne pourra pas être animée par squelette**. Pour le héros 3/4, utiliser une **case de 64 avec un personnage d'environ 48 px**.

**Correction à apporter au prompt :** simplifier fortement l'armure à cette taille (grandes surfaces à deux tons, pas de motif d'écailles). Voir `prompts-personnages.md`.


## Résultats de l'essai 3/4 v2 : prompt simplifié (2026-10-05)

Génération avec le prompt v2 (armure en aplats à deux tons, sans écailles). Vue « low top-down », 8 directions, **case de 64×64**, essai gratuit.

| Critère | Résultat | Verdict |
|---|---|---|
| Hauteur du héros | **58 à 62 px** (cible 48 ± 4) | **Hors cible** : le réglage de taille du personnage n'a pas été appliqué, il remplit la case |
| Part de la case | 91 à 97 % | Aucune marge pour animer |
| Pieds | écart de 3 px | À voir (seuil 2 px) |
| Pixels semi-transparents, agrandissement caché | 0, aucun | OK |
| Couleurs | 64 par image, 97 sur l'ensemble | Dépassé |

**Lecture visuelle :** nettement plus propre et lisible que la v1. Le visage est net (sourcils, yeux, bouche), l'épée est franche, la cape-ailes orange forme une grande surface lisible, le tablier vert d'eau ressort. Pertes par rapport à la référence : les plaques de plumes aux épaules sont devenues une cape, les éclaboussures de sang sur la lame ont disparu (« plain steel blade »), l'emblème bronze n'est plus visible.

**Attention à la comparaison :** la v2 est plus lisible en partie parce qu'elle a **62 px de haut au lieu de 47** pour la v1. On ne peut donc pas conclure que le prompt simplifié tient à 48 px.

**Conséquence de choix :** à 62 px, le héros en vue 3/4 a la même taille que le héros de profil (17,8 % d'une image de 360 px). Les jeux en vue 3/4 mesurés sont plutôt à 10 à 12 %.
