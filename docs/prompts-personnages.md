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
