# Étude de jeux de référence : échelle des personnages

Rédigée le 2026-10-05, pour la décision de direction artistique du Jeu B (jeu Android lié à CRS).

## Méthode et limites (à lire avant les chiffres)

- **Source des mesures** : captures d'écran officielles des pages Steam des jeux (1920×1080 en général, d'autres tailles pour certains jeux). Je n'ai pas joué aux jeux ni lu leurs fichiers.
- **Ce qui est mesuré** : la hauteur du personnage principal, en pixels de la capture, rapportée à la hauteur de l'image (« % de la hauteur »). Ce pourcentage ne dépend pas de la résolution ni de l'agrandissement : c'est la proportion que voit le joueur.
- **Taille du pixel d'art** : lue visuellement sur des agrandissements (combien de pixels d'écran fait un pixel du dessin). La résolution native en découle : `hauteur de l'image ÷ taille du pixel`. **C'est une estimation**, marquée « ≈ ».
- **Précision** : une mesure sur une capture, dans une pose donnée, à quelques pixels près. Une pose de course ou d'attaque change la hauteur. Les mesures sont des ordres de grandeur, pas des spécifications.
- **« partiel »** : le personnage était coupé ou à moitié visible sur la capture. La valeur est une estimation basse précision.
- **« non mesuré »** : capture téléchargée mais pas encore mesurée.
- **Les captures ne sont pas dans le dépôt** (images protégées). Elles sont dans le dossier de travail de la session et seront perdues à sa fin.

## Jeux en vue de profil (plateforme, combat)

| Jeu | Héros, % de la hauteur | Pixel d'art (px écran) | Résolution native estimée | Boss / héros | Remarque |
|---|---|---|---|---|---|
| Blasphemous | ≈ 13,5 % (capirote compris) | ≈ 5 | ≈ 216 | ≈ 4 à 5× (boss vu en partie) | Boss colossal derrière un balcon |
| Metal Slug 3 | ≈ 14 à 17 % | non mesuré | 224 (valeur connue du jeu d'origine, non revérifiée) | ≈ 2,3× (grand crabe) | Capture en 600×450 |
| Mariachi Legends | ≈ 16 % | non mesuré | non mesuré | non mesuré | Metroidvania, jeu à venir |
| Katana Zero | ≈ 16,5 % (humain debout) | non mesuré | non mesuré | – | |
| Huntdown: Overtime | ≈ 15,7 % | ≈ 4 | ≈ 270 | non mesuré | Éclairage moderne sur pixel art |
| Owlboy | ≈ 9,6 % | non mesuré | non mesuré | non mesuré | Héros petit, peu de décor au sol |
| Goodbye Seoul | ≈ 14 à 17 % (en course) | ≈ 6 | ≈ 180 | – | **Décors 3D**, personnage en pixel art |
| Skinwalker: First Blood | humain ≈ 19 % (estimé), forme de bête ≈ 35 % | ≈ 6 à 7 | ≈ 160 à 215 | bête ≈ 1,8× l'humain | Deux formes, deux échelles |
| Shadow Sacrament | ≈ 14 % (estimé sur planche) | ≈ 6 à 7 | ≈ 160 | – | Très sombre, difficile à mesurer |

## Jeux en vue 3/4 (exploration)

| Jeu | Héros, % de la hauteur | Pixel d'art | Résolution native estimée | Héros en pixels d'art | Remarque |
|---|---|---|---|---|---|
| Sea of Stars | ≈ 10,2 % | ≈ 5 | ≈ 216 | ≈ 22 | Mesuré sur la capture 1920×1080 |
| Chained Echoes | ≈ 12,2 % | ≈ 4 | ≈ 270 | ≈ 33 | |
| CrossCode | ≈ 9,8 % | 2 (capture 1136×640) | ≈ 320 | ≈ 31 | Résolution cohérente avec 568×320 en natif |
| Hyper Light Drifter | ≈ 10 à 12 % (partiel) | non mesuré | non mesuré | – | |
| Eastward | ≈ 9 à 10 % (partiel) | non mesuré | non mesuré | – | |
| Arcadian Atlas | ≈ 15 % (partiel) | non mesuré | non mesuré | – | Vue plus proche (jeu tactique) |

## Téléchargées mais non mesurées

Kill The Shadow (décors 3D HD + personnages en pixel art), The Road of Dust and Sorrow, Dead Cells (rendu 3D converti en pixels), et pour une seconde passe les captures de Hyper Light Drifter, Eastward et Arcadian Atlas.

## Non disponibles sur Steam (captures à fournir)

Princess Crown, Guardian Heroes, The Legend of Zelda: A Link to the Past, Castlevania II: Belmont's Revenge (Game Boy), Long Gone (jeu à venir, en 3D), Back In Time (jeu à venir).

## Ce que montrent les mesures

1. **En vue de profil, le héros fait 13 à 17 % de la hauteur de l'image** dans la plupart des jeux (médiane ≈ 15 %). Owlboy est plus petit (≈ 10 %).
2. **En vue 3/4, le héros fait 10 à 12 %**, soit environ les deux tiers de la proportion de la vue de profil. La caméra voit plus large autour du personnage.
3. **Les résolutions natives estimées vont de ≈ 180 à ≈ 320 px de haut.** Dans cet échantillon de vrais pixel arts, aucun jeu n'est en 720 px natif. Ceux qui paraissent « HD » (Goodbye Seoul, Kill The Shadow, Long Gone) combinent un décor en 3D et des personnages en pixel art.
4. **Les boss courants font 2 à 3 fois le héros** (Metal Slug, la forme de bête de Skinwalker). Les boss de spectacle atteignent 5× ou plus, mais **sont vus en partie** (Blasphemous). Un boss de 5× vu en entier est exceptionnel.

## Conséquences pour le Jeu B (à valider)

Hauteurs de héros qui reproduisent ces proportions, selon la hauteur d'image :

| Hauteur d'image | Héros plateforme (13 à 17 %) | Héros 3/4 (10 à 12 %) | Boss courant (2 à 3×) | Boss colosse (5×) |
|---|---|---|---|---|
| 270 px | 35 à 46 px | 27 à 32 px | 70 à 140 px | ≈ 200 px |
| 360 px | 47 à 61 px | 36 à 43 px | 95 à 185 px | ≈ 270 px |
| 720 px | 94 à 122 px | 72 à 86 px | 190 à 370 px | ≈ 540 px |

- **Le héros de 128 px dans une image de 720 px fait 17,8 %** : c'est au haut de la fourchette des jeux de profil, donc grand. Dans une image de 360 px, la même proportion donne 64 px.
- **Les deux modes de jeu n'ont pas la même échelle.** Un héros d'exploration 3/4 est plus petit qu'un héros de plateforme d'environ un tiers. Un même sprite ne peut pas servir aux deux sans changer la caméra ou le redessiner.
- **Un boss de 5× en entier est un cas rare.** Prévois des boss courants à 2 ou 3× et un petit nombre de colosses vus en partie.

## Pistes pour la suite

- Mesures de seconde passe sur les jeux non mesurés et sur les captures partielles.
- Images à fournir pour les jeux hors Steam.
- Décisions à prendre dans la « bible graphique » : hauteur d'image, hauteur du héros (profil et 3/4), rapport boss/héros, taille de tuile, palette, contour, direction de la lumière, nombre d'images par animation.
