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
