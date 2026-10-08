# Prompts de personnages pour PixelLab

Rédigé le 2026-10-05. Base de départ pour obtenir des personnages qui correspondent à ce que l'utilisateur imagine.

## Règle numéro 1

**Remplacer tous les crochets avant de lancer la génération.** Lors du deuxième essai, le modèle de prompt a été collé tel quel (`[role]`, `[build: lean / athletic / stocky]`, etc.) : l'outil a inventé les détails à la place de l'utilisateur. Le résultat est bon, mais ce n'est pas un personnage choisi.

## Structure d'un prompt

```
A human [role], [build], [age], [skin tone], [hair style and color], [face: expression, scar, beard],
wearing [outfit and materials], [2 dominant colors + 1 accent color], carrying [weapon].
Large readable head, simplified face with clear eyes, readable silhouette.
Clean pixel art, selective dark outline of one pixel, flat shading with three tones per material,
limited palette of about 24 colors, no anti-aliasing, no gradients, no dithering, transparent background.
```

Remarque : la formule « tall slim proportions » du premier prompt était contradictoire avec « large readable head ». À 64 px de haut, privilégier la lisibilité du visage (tête plus grande, silhouette plus ramassée).

## Prompt de base décrit à partir de l'image obtenue (essai du 2026-10-05)

Description rédigée en regardant les 8 images produites par l'outil. Elle sert de point de départ reproductible. Les détails marqués (?) sont incertains.

```
A human monster hunter, athletic and sturdy build, mid-thirties, tanned skin, short messy brown hair, short full brown beard, a faint scar above one eyebrow (?), calm serious determined expression, wearing a sleeveless dark green tunic with crossed brown leather chest straps and a belt with pouches, a single polished steel pauldron on the left shoulder, steel vambraces on both forearms, dark blue-gray trousers with tan trim, brown leather boots with tan cuffs, carrying a short steel sword in the right hand and a long staff with an ornate head strapped across the back. Dominant colors: forest green, brown and steel gray; accent: warm tan. Large readable head, simplified face with clear eyes, readable silhouette. Clean pixel art, selective dark outline of one pixel, flat shading with three tones per material, limited palette of about 24 colors, no anti-aliasing, no gradients, no dithering, transparent background.
```

## Variations (un seul changement à la fois)

| Pour changer | Remplacer dans le prompt |
|---|---|
| La corpulence | `athletic and sturdy build` par `lean and wiry build` ou `broad and heavy build` |
| L'âge | `mid-thirties` par `early twenties` ou `late fifties, gray at the temples` |
| Le teint | `tanned skin` par `dark brown skin`, `pale freckled skin`, `olive skin` |
| Les cheveux | `short messy brown hair` par `long black hair tied back`, `shaved head`, `braided red hair` |
| Le visage | `short full brown beard` par `clean-shaven`, `thin mustache`, `long braided beard` |
| La tenue | `sleeveless dark green tunic` par `long dark red coat`, `hooded gray cloak`, `full leather jerkin` |
| Les couleurs | `forest green, brown and steel gray` par `deep red, black and bronze` |
| L'arme | `short steel sword` par `greatsword`, `spear`, `two daggers`, `crossbow` |
| L'insigne de guilde | ajouter `a small [color] guild emblem on the left pauldron` |

## Méthode pour approcher ce que l'utilisateur imagine

1. **Écrire la fiche du personnage en français** : corpulence, âge, visage, teint, cheveux, tenue, couleurs, arme, attitude, signe distinctif.
2. **La traduire dans la structure ci-dessus**, sans crochet.
3. **Générer, puis comparer** à l'idée de départ, point par point.
4. **Modifier une seule ligne à la fois** (tableau des variations) pour savoir ce qui produit quoi.
5. **Utiliser les images de référence** : d'après le site de PixelLab, l'outil peut convertir un dessin de référence en personnage jouable et retoucher des vêtements ou accessoires en conservant le style. À vérifier dans l'outil, ces fonctions n'ont pas été essayées ici.
6. **Retoucher les couleurs dans PixelForge** plutôt que de régénérer : changer la teinte d'une écharpe ou d'une peau est bien moins coûteux qu'une nouvelle génération.
7. **Garder le prompt qui a produit le personnage retenu** avec l'image : c'est la seule façon de refaire un personnage de la même famille.

## Cohérence entre personnages

Pour que les 4 personnages de CRS paraissent venir du même jeu :
- **réutiliser la même ligne de style** (contour, ombrage, palette, proportions) mot pour mot ;
- **ne changer que la partie « personnage »** du prompt ;
- **même case, même taille de personnage, même vue**.

## Personnage 1 : le chasseur en armure de wyverne rouge

Référence fournie par l'utilisateur le 2026-10-05 : image d'une animation d'attente en 18 images (image générée par une IA, le texte JSON qu'elle contient est du remplissage sans valeur). Jeune chasseur, cheveux châtains en bataille, mine sérieuse, armure rouge-orange à écailles et plaques en forme de plumes, grande épée de type fendoir posée sur l'épaule, tablier vert, ceinture de cuir.

**Attention : la référence est beaucoup plus détaillée que ce que permet un personnage de 64 px de haut** (écailles individuelles, plumes détaillées, éclaboussures de sang). À 64 px, il faut garder : la silhouette (épée sur l'épaule, grandes plaques de plumes aux épaules), la palette (rouge-orange, crème, brun, vert d'eau, gris acier) et quelques éléments emblématiques. Les écailles se suggèrent par un motif à deux tons, pas une par une.

### Prompt complet (à 64 px de haut, case de 128)

```
A young human monster hunter in his early twenties, athletic build, fair skin, messy short brown hair with a longer front lock, serious determined frown, no beard. He wears a full set of armor crafted from a fire wyvern's scales: an orange-red scale breastplate with crossed brown leather straps and a small round bronze emblem at the collar, layered feather-shaped plates in orange and cream on the shoulders and back like folded wings, red-orange scale bracers, greaves and boots, a brown leather belt with pouches, dark brown trousers and a short teal-green cloth tabard hanging in front of the belt. He carries a huge cleaver-style greatsword with a wide steel blade streaked with dark red blood, resting on his right shoulder, gripped with his right hand. Idle standing pose, wide stance. Large readable head, simplified face with clear eyes and a frown, strong readable silhouette with big feather-shaped shoulder plates. Scales suggested by a simple two-tone pattern, not individual scales. Dominant colors: red-orange and brown; accents: cream feather tips, teal green, steel gray. Clean pixel art, selective dark outline of one pixel, flat shading with three tones per material, limited palette of about 28 colors, no anti-aliasing, no gradients, no dithering, transparent background.
```

### Prompt court (si l'outil limite la longueur)

```
Young human monster hunter, early twenties, messy short brown hair, serious frown. Orange-red wyvern-scale armor with large feather-shaped shoulder plates in orange and cream, brown leather straps and belt, teal-green tabard, red boots. Huge cleaver greatsword with a bloodied steel blade resting on his right shoulder. Idle stance. Large readable head, strong silhouette. Clean pixel art, one-pixel dark outline, flat shading, about 28 colors, no anti-aliasing, no gradients, transparent background.
```

### Négatif (si l'outil a ce champ)

```
blurry, smooth gradients, anti-aliasing, 3D render, painting, photo, text, watermark, cropped, extra limbs, individual scales, tiny details, beard
```

### Réglages

| Réglage | Valeur |
|---|---|
| Case | 128×128 |
| Taille du personnage | environ 64 px de haut (50 % de la case) |
| Vue | de profil (side), comme les essais précédents |
| Directions | 8 (ou 4 pour économiser les générations) |
| Image de référence | la vignette 1 de la référence, sans fond (si l'outil accepte une image de référence) |

### Si le résultat ne correspond pas

| Problème | Correction du prompt |
|---|---|
| Armure trop détaillée, illisible | ajouter `very simple armor shapes, large flat color areas` |
| Plaques de plumes trop discrètes | `oversized feather-shaped shoulder plates, wing-like silhouette` |
| Épée trop petite | `oversized greatsword, blade as long as his body` |
| Visage trop sombre ou écrasé | `face clearly lit, large eyes, no helmet` |
| Silhouette trop massive | `athletic proportions, narrow waist` |
| Couleurs trop nombreuses | remplacer `about 28 colors` par `exactly 24 colors` |


## Le chasseur en vue 3/4 (exploration)

**Faisable sur l'essai gratuit** : en case de 64×64, le héros 3/4 mesure environ 48 px de haut (75 % de la case), ce qui correspond au format « Perso 3/4 » de 32×48 px de la bible.

Réglages :
- Vue : **« low top-down »** d'abord (vue de dessus légèrement inclinée, style Zelda), puis « high top-down » pour comparer. Noms à vérifier dans l'outil.
- Directions : **4** (sud, ouest, est, nord) ; l'est peut être le miroir de l'ouest.
- Case 64×64, personnage réglé à environ 48 px de haut.

Prompt : reprendre le prompt complet du personnage 1 en remplaçant la fin par :

```
... Idle standing pose. Seen in a three-quarter top-down view, camera slightly above, like a classic 16-bit action RPG. Large readable head, simplified face with clear eyes, strong readable silhouette. Scales suggested by a simple two-tone pattern, not individual scales. Dominant colors: red-orange and brown; accents: cream feather tips, teal green, steel gray. Clean pixel art, selective dark outline of one pixel, flat shading with three tones per material, limited palette of about 28 colors, no anti-aliasing, no gradients, no dithering, transparent background.
```

Pour garder la même famille visuelle que la vue de profil : même palette (`donnees/palette_chasseur_wyverne_32.json`), même contour, même ombrage.

## Prompts d'animation (abonnement requis)

Dans l'outil « Characters », vérifier d'abord les animations prédéfinies (marche, course, attente). Pour les animations sur mesure, décrire le mouvement :

| Animation | Images | Description à donner |
|---|---|---|
| Attente | 6 | `standing idle, slow breathing, the greatsword resting on the right shoulder, the feathered cape swaying slightly` |
| Marche | 8 | `walking forward at a steady pace, greatsword resting on the shoulder, the feathered cape swaying behind` |
| Course | 8 | `running forward leaning ahead, greatsword held on the shoulder, the feathered cape flowing behind` |
| Saut | 3 | `jumping: knees bent, rising with the cape lifting, then falling` |
| Attaque | 6 par coup | `heavy overhead slash with the cleaver greatsword: lifts the blade from the shoulder, swings it down in front, recovers` |
| Dégâts | 2 | `flinches backward, head tilted back, cape flaring` |
| Mort | 8 | `falls to his knees then onto his back, the greatsword dropping` |

Conseil de la documentation de l'outil (animation par squelette) : régler la tête sur **« fixed head: always »** pour que le visage reste identique d'une image à l'autre. Utiliser les images de référence et les images figées pour garder la cohérence.


## Le chasseur en vue 3/4, version simplifiée pour 48 px (v2)

À utiliser parce que la première version (armure à écailles) devient du bruit à 48 px de haut. Réglages : vue « low top-down », **case de 64×64**, personnage réglé à **environ 48 px de haut** (la case doit être une des tailles acceptées par l'animation : 64).

```
A young human monster hunter in his early twenties, athletic build, fair skin, messy short brown hair, serious frown, no beard. Very simple design for a tiny sprite: red-orange armor made of large flat color areas with only two tones, no scale pattern, no small details; large orange feather-shaped shoulder plates and a long orange feathered cape forming one big readable shape; a teal-green cloth tabard; brown belt and boots; a huge cleaver greatsword with a plain steel blade resting on his right shoulder. Face clearly lit, large dark eyes, light skin. Three-quarter top-down view, camera slightly above, like a classic 16-bit action RPG. Idle standing pose. Strong readable silhouette. Clean pixel art, selective dark outline of one pixel, flat shading with only two tones per material, limited palette of about 24 colors, no anti-aliasing, no gradients, no dithering, no noise, no texture, transparent background.
```

Champ négatif : `scales pattern, small details, texture, noise, speckle, gradients, blurry, 3D render, painting, photo, text`.

Remarques :
- **4 directions suffisent en vue 3/4** (sud, nord, est, et l'ouest en miroir de l'est). Le miroir place l'épée sur l'épaule gauche : acceptable si le personnage est considéré comme ambidextre dans le jeu ; sinon générer l'ouest séparément.
- **Même palette que la vue de profil** (`donnees/palette_chasseur_wyverne_32.json`) pour que le personnage reste cohérent.
- Si le résultat reste trop chargé : remplacer `about 24 colors` par `exactly 20 colors`, ou passer le personnage à 56 px de haut (même taille de case, plus de pixels pour le détail).


## Personnage 2 : le guerrier aux deux lames (référence du 2026-10-08), candidat pour Krunt3

Référence fournie par l'utilisateur : illustration réaliste, homme blond aux cheveux courts, barbe courte blonde, regard calme, armure sombre à écailles de dragon (plastron, grandes épaulières à pointes, tassettes en écailles, jambières et bottes renforcées de cuir brun et de laiton), ceinture de cuir à bourses. **Deux épées courtes tenues en garde basse** : celle de droite (côté gauche de l'image) a une lame de flammes orange, celle de gauche une lame violette à fumée sombre ; deux poignées dépassent aussi derrière les épaules (rangement dans le dos).

**À 64 px (ou 48 px en 3/4), garder seulement** : la silhouette large et basse, les épaulières à pointes, les deux lames de couleurs opposées (orange / violet) qui sont l'élément emblématique, la cape d'écailles en pointes autour des hanches, les cheveux blonds. Les écailles se suggèrent par un motif à deux tons.

Rapport avec la trame : `docs/trame/08` donne déjà à Krunt3 « deux lames courtes » et une braise orange ; le violet est un ajout à décider (second élément, ou ombre / Éther) : à valider par krunt avant de l'imposer.

### Prompt complet (profil, case 128, personnage ~64 px)

```
A human monster hunter in his early thirties, broad and sturdy athletic build, fair skin, short messy blond hair, short blond beard, calm serious determined expression. He wears a full set of dark gunmetal-black dragon-scale armor: a scale breastplate with a raised collar, large spiked shoulder pauldrons, scale-pattern tassets like a short jagged skirt around the hips, armored vambraces, greaves and heavy boots, with brown leather straps, a wide brown belt with pouches and bronze buckles. Two short swords crossed in a sheath on his back, and he holds two short swords low in a ready stance: the one in his right hand has a blade of orange flames, the one in his left hand has a blade of dark purple smoky energy. Standing pose, wide stance. Large readable head, simplified face with clear eyes, strong readable silhouette with spiked shoulder plates. Scales suggested by a simple two-tone pattern, not individual scales. Dominant colors: dark charcoal and brown; accents: bright orange flame, violet, bronze. Clean pixel art, selective dark outline of one pixel, flat shading with three tones per material, limited palette of about 28 colors, no anti-aliasing, no gradients, no dithering, transparent background.
```

### Prompt court

```
Human monster hunter, early thirties, broad sturdy build, short messy blond hair and short beard, calm serious face. Dark charcoal dragon-scale armor with large spiked shoulder plates and a jagged scale skirt, brown leather belt and straps, bronze buckles. Two short swords held low: right one with an orange flame blade, left one with a purple smoky blade. Large readable head, strong silhouette. Clean pixel art, one-pixel dark outline, flat shading, about 28 colors, no anti-aliasing, no gradients, transparent background.
```

### Version 3/4 pour 48 px (case 64×64, vue « low top-down »)

```
A human monster hunter in his early thirties, sturdy build, fair skin, short blond hair, short blond beard. Very simple design for a tiny sprite: dark charcoal armor made of large flat color areas with only two tones, no scale pattern, no small details; two big spiked shoulder plates and a jagged skirt forming one readable shape; brown belt and boots. Two short swords held low, one with a bright orange flame blade, one with a violet blade, the two colors clearly readable. Face clearly lit, large dark eyes. Three-quarter top-down view, camera slightly above, like a classic 16-bit action RPG. Idle standing pose. Strong readable silhouette. Clean pixel art, selective dark outline of one pixel, flat shading with only two tones per material, limited palette of about 24 colors, no anti-aliasing, no gradients, no dithering, no noise, no texture, transparent background.
```

### Négatif

`scales pattern, small details, texture, noise, speckle, gradients, blurry, 3D render, painting, photo, text, watermark, cropped, extra limbs, helmet, tiny details`

### Réglages et variations

Mêmes réglages que le personnage 1 (case 128 ou 64, 4 ou 8 directions, une seule ligne de style).

| Problème | Correction |
|---|---|
| Lames trop discrètes | `oversized glowing blades, the flame and the purple glow clearly visible` |
| Armure illisible | `very simple armor shapes, large flat color areas` |
| Couleurs trop nombreuses | `exactly 24 colors` |
| Deux lames de même couleur | répéter `the right blade is orange fire, the left blade is violet` |
| Variante sans le violet (si krunt le refuse) | remplacer la lame violette par `a plain steel blade` |

Animations utiles : attente (`standing idle, slow breathing, the two flame trails flickering`), attaque (`fast alternating slashes with the two short swords, leaving an orange and a violet trail`), dégâts, mort.
