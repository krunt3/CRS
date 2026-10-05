# Bible graphique du Jeu B

**Statut : BROUILLON. Rien n'est encore verrouillé.**
Rédigée le 2026-10-05. Chaque décision reste « À DÉCIDER » jusqu'à ce que l'utilisateur la valide. Une fois toutes les décisions prises, ce document est complété et figé (voir la section 8).

## 1. Pourquoi ce document

La taille des sprites, la grille de tuiles et les règles de palette se dessinent une fois et se maintiennent pendant tout le projet. Les changer plus tard oblige à redessiner tout ce qui existe. Ce document fixe ces choix en un seul endroit.

## 2. Données de départ

- **Idée de base de l'utilisateur** : héros de **96 px de haut sur 48 px de large** *(interprétation à confirmer : hauteur × largeur)*, tuile de 32 px. 96 px = exactement 3 tuiles.
- **Étude de jeux de référence** (voir `etude-jeux-reference.md`) : un héros de plateforme fait 13 à 17 % de la hauteur de l'image, un héros d'exploration en vue 3/4 fait 10 à 12 %, un boss courant fait 2 à 3× le héros, un boss colosse de 5× est vu en partie.
- **Outil de génération envisagé : PixelLab (pixellab.ai).** Les contraintes qui comptent pour les tailles sont dans la section 3.

## 3. Contraintes de PixelLab

| Contrainte | Valeur | Fiabilité |
|---|---|---|
| Animation par squelette : tailles de canevas acceptées | **256×256, 128×128, 64×64, 32×32, 16×16** (carrés uniquement) | **Lu sur la page de documentation** « Animate with skeleton » |
| Animation par squelette : abonnement | « Tier 1 » minimum | Lu sur la même page |
| Directions | 4 (S, O, E, N) ou 8 (avec les diagonales) | Lu sur la page de documentation « Character options » |
| Types de proportions de personnage | bipède réaliste, quadrupède minuscule, bipède semi-chibi | Lu sur la même page |
| Tailles de canevas pour la génération d'images | de 16 à 512 px | Résumé de recherche, **non confirmé sur la page lue** |
| Rotation (changer la direction) : taille maximale | 128×128 par image | Résumé de recherche, **non confirmé** |
| Animation par squelette : nombre d'images maximum | 16 | Résumé de recherche, **non confirmé** |
| Qualité à petite taille | meilleure aux grandes tailles ; 16×16 possible mais plus faible | Résumé de recherche, **non confirmé** |
| Tailles de tuile des jeux de tuiles générés | non indiquée | **À vérifier dans l'outil** |
| Vue de profil, vue de dessus | indiquées comme « vues et directions », sans détail | **À vérifier dans l'outil** |

**Conséquence directe :** les canevas d'animation sont **carrés et en puissances de 2**. Un personnage de 96×48 doit tenir dans une case de 128×128. Un boss de plus de 256 px de haut ne peut pas être animé en une seule image : il faut l'assembler à partir de plusieurs pièces.

## 4. Les deux scénarios chiffrés

La résolution décide de tout le reste. Les pourcentages de l'écran sont identiques dans les deux scénarios : seul le nombre de pixels change.

### Scénario A : HD, image de 720 px de haut, tuile de 32 px

| Élément | Hauteur (px) | En tuiles | % de l'écran | Case PixelLab | Remarque |
|---|---|---|---|---|---|
| Tuile | 32 | 1 | – | – | Grille de base |
| Héros de plateforme | 96 (× 48 de large) | 3 | 13,3 % | **128×128** | 75 % de la case, marge pour les armes |
| Héros d'exploration 3/4 | 80 | 2,5 | 11,1 % | 128×128 | Environ 2/3 de la proportion de profil |
| PNJ adulte | 80 | 2,5 | 11,1 % | 128×128 | Même gabarit que le héros 3/4 |
| PNJ enfant | 64 | 2 | 8,9 % | 64×64 ou 128×128 | |
| Petit monstre | 32 à 64 | 1 à 2 | 4 à 9 % | 64×64 | |
| Monstre moyen | 96 à 160 | 3 à 5 | 13 à 22 % | 256×256 pour 160 | |
| Boss courant | 192 à 224 | 6 à 7 | 27 à 31 % | **256×256** | **Plafond de PixelLab** : 2 à 2,3× le héros |
| Boss de 3× | 288 | 9 | 40 % | dépasse 256 | **Assemblage de pièces nécessaire** |
| Colosse (5×, vu en partie) | 480 | 15 | 67 % | dépasse 256 | **Assemblage de pièces nécessaire** |

### Scénario B : rétro, image de 360 px de haut, tuile de 16 px

| Élément | Hauteur (px) | En tuiles | % de l'écran | Case PixelLab | Remarque |
|---|---|---|---|---|---|
| Tuile | 16 | 1 | – | – | Grille de base |
| Héros de plateforme | 48 (× 24 de large) | 3 | 13,3 % | **64×64** | 75 % de la case |
| Héros d'exploration 3/4 | 40 | 2,5 | 11,1 % | 64×64 | |
| PNJ adulte | 40 | 2,5 | 11,1 % | 64×64 | |
| PNJ enfant | 32 | 2 | 8,9 % | 32×32 ou 64×64 | |
| Petit monstre | 16 à 32 | 1 à 2 | 4 à 9 % | 32×32 | |
| Monstre moyen | 48 à 80 | 3 à 5 | 13 à 22 % | 128×128 | |
| Boss courant | 96 à 144 | 6 à 9 | 27 à 40 % | **128×128 ou 256×256** | Entre dans une case |
| Colosse (5×, vu en partie) | 240 | 15 | 67 % | **256×256** (94 %, juste) | Marge très faible : assemblage de 2 pièces recommandé |

### Comparaison honnête

| | Scénario A (HD, 96 px) | Scénario B (rétro, 48 px) |
|---|---|---|
| Cohérence avec les jeux de référence (proportions) | Oui | Oui |
| Entre dans les cases de PixelLab | Héros oui ; boss > 2,3× : **assemblage de pièces** | Tout entre, colosse juste |
| Pixels par image du héros | ≈ 4 600 | ≈ 1 150 (4 fois moins) |
| Mémoire estimée d'un boss de 80 images | ≈ 20 Mo (case 256) | ≈ 5 à 20 Mo (case 128 ou 256) |
| Qualité attendue de la génération | Meilleure (plus de pixels) | **À tester** : PixelLab semble plus fiable aux grandes tailles |
| Pixels réguliers sur téléphone (720, 1080, 1440 px de haut) | Net sur 720 et 1440 seulement | **Net sur les trois** |
| Changement par rapport à ton pipeline actuel (96 px) | Aucun | Formats PixelForge à refaire |

## 5. Règles de cohérence (valables dans les deux scénarios)

1. **Tout est un multiple de la tuile ou d'une demi-tuile** : personnages, monstres, objets, pièges. Si la résolution change, tout se recalcule.
2. **Les cases sont carrées et en puissances de 2** (contrainte de PixelLab) : 32, 64, 128, 256.
3. **La ligne de sol dans chaque case est à la même place** : les pieds se posent à 1/16 de la hauteur de la case en partant du bas (8 px pour une case de 128, 4 px pour une case de 64). Le point d'ancrage dans Godot est le bas-centre.
4. **Le héros occupe environ 75 % de sa case**, pour laisser la place aux armes et aux effets.
5. **Les hitbox sont définies en tuiles, pas au pixel** : zone vulnérable du héros d'environ 1 tuile de large et 2,5 à 2,75 tuiles de haut.
6. **Palette de 16 couleurs par personnage, 32 par région**, une fois les images générées réduites (étape de nettoyage dans PixelForge).
7. **Les boss sont définis par leur hauteur en tuiles** (6, 9 ou 15), pas en pixels.
8. **Vue de profil : une direction dessinée et un miroir. Vue 3/4 : trois directions dessinées (bas, haut, côté) et un miroir.**

## 6. Budget d'animation par personnage (à ajuster)

| Animation | Images |
|---|---|
| Repos | 4 à 6 |
| Marche | 8 |
| Course | 8 |
| Saut (montée, sommet, descente) | 3 |
| Réception | 2 |
| Attaque (par coup d'une combinaison de 3) | 6 par coup |
| Dégâts | 2 |
| Mort | 8 |
| Pose de piège | 4 |
| **Total vue de profil** | **≈ 60** |
| Vue 3/4 : repos 2 + marche 6, dans 3 directions | ≈ 24 à 32 |

Avec PixelLab, jusqu'à 16 images par animation d'après un résumé de recherche (à confirmer).

## 7. Formats à préenregistrer dans PixelForge (selon le scénario retenu)

Liste à compléter après la décision. Pour chaque format : nom, taille de la case, ligne de sol, ancrage, palette.

| Format | Scénario A | Scénario B |
|---|---|---|
| Tuile | 32×32 | 16×16 |
| Héros / PNJ | 128×128 | 64×64 |
| Petit monstre | 64×64 | 32×32 |
| Monstre moyen | 256×256 | 128×128 |
| Boss | 256×256 (pièces au-delà) | 128×128 ou 256×256 |

## 8. Décisions à verrouiller

Chaque ligne passe de « À DÉCIDER » à « VERROUILLÉ » avec la date. Après verrouillage, un changement se fait par une procédure explicite (section 9).

| N° | Décision | Choix | Statut | Date |
|---|---|---|---|---|
| 1 | Résolution de l'image (hauteur) | A : 720 / B : 360 | À DÉCIDER | |
| 2 | Largeur extensible, hauteur fixe | Recommandé | À DÉCIDER | |
| 3 | Taille de la tuile | 32 (A) ou 16 (B) | À DÉCIDER | |
| 4 | Hauteur du héros de plateforme | 96 (A) ou 48 (B) | À DÉCIDER | |
| 5 | Largeur du héros | 48 (A) ou 24 (B) *(à confirmer)* | À DÉCIDER | |
| 6 | Hauteur du héros en vue 3/4 | 80 (A) ou 40 (B) | À DÉCIDER | |
| 7 | Boss courant et colosse | voir section 4 | À DÉCIDER | |
| 8 | Contour des sprites (noir, coloré, aucun) | | À DÉCIDER | |
| 9 | Direction de la lumière | | À DÉCIDER | |
| 10 | Nombre de couleurs par personnage et par région | 16 / 32 | À DÉCIDER | |
| 11 | Budget d'animation par personnage | voir section 6 | À DÉCIDER | |
| 12 | Personnalisation (corps de base + palettes) | | À DÉCIDER | |
| 13 | Nombre de personnages jouables de la démo | | À DÉCIDER | |
| 14 | Outil de génération et son abonnement | PixelLab | À DÉCIDER | |

## 9. Procédure pour changer une décision verrouillée

1. Écrire le changement, la raison et la liste de tout ce qui sera à refaire (sprites, tuiles, palettes, formats PixelForge, hitbox).
2. Estimer le travail perdu en nombre d'images et en heures.
3. N'accepter le changement que s'il vaut ce coût. Sinon, adapter autour (par exemple en jouant sur la caméra).
4. Mettre à jour ce document, la date et la version.

## 10. Sources

- Documentation PixelLab, animation par squelette : https://www.pixellab.ai/docs/tools/animate-with-skeleton
- Documentation PixelLab, options de personnage : https://www.pixellab.ai/docs/options/character
- PixelLab, site : https://www.pixellab.ai/
- PixelLab, API : https://www.pixellab.ai/pixellab-api et https://api.pixellab.ai/v2/docs
- Étude de jeux de référence : `etude-jeux-reference.md`
