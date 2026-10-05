# Kit d'essai : cartes, tuiles et sprites (32×32, gratuit)

Rassemblé le 2026-10-05 pour que tous les essais (Godot seul contre LDtk, voir `docs/analyse-editeurs-cartes.md`) partent des **mêmes bases**. Rien ici n'est de l'art final : ce sont des éléments gratuits de remplacement, à remplacer plus tard par les sprites PixelForge / PixelLab.

## Licence et crédits
Tous les fichiers viennent d'**OpenGameArt.org** et sont déclarés **CC0** (domaine public) sur leur page au 2026-10-05, ce qui autorise l'usage commercial sans attribution. Les crédits sont tout de même conservés dans `inventaire.json` (titre, auteur, page source, taille, usage). Ne rien ajouter à ce dossier sans vérifier sa licence. Un pack de la même collection (« 32x64 Female Base Sprite ») était en CC-BY 3.0 : **non inclus**. Un autre (« RPG Tileset 32x32 », jeu de donjon) est aussi en CC-BY 3.0 : **non inclus**.

## Contenu
| Dossier | Fichiers | Grille 32×32 | À quoi ça sert |
|---|---|---|---|
| `tuiles_topdown/` | 8 feuilles : terrain autotile (herbe, terre, eau), sol herbe/sable, eau, pierre/terre, herbe variée, chemin, mur rocheux | oui | Zone d'exploration en vue 3/4 (Traque) |
| `tuiles_donjon/` | ruines mythiques, grotte pourpre | oui | Sites dangereux, ruines, arènes de roche |
| `tuiles_plateforme/` | forêt (sol, arbres, buissons, rochers, panneau, grotte), terre et herbe, boue et herbe | oui | Quêtes de plateforme, arène latérale de chasse |
| `sprites/heros_et_pnj/` | mannequin 32×48 (3 colonnes × 4 directions), personnage animé 32 px | oui | Héros et PNJ provisoires |
| `sprites/ennemis_provisoires/` | zombie et squelette, chauve-souris | oui | Ennemis de remplissage |
| `sprites/monstres_silhouettes/` | 11 silhouettes aux **vraies hauteurs** du roster (le chef de meute 70 px, ses éclaireurs, un grand volant 117 px, un familier 16 px…) | n/a | Valider les proportions face au héros (64 px) avant tout dessin |
| `decor_extras_grille_a_verifier/` | village/eau/arbres (944×720), arbres et herbe (1664×816), cabane, arbres et buissons | **non** (à vérifier à l'import) | Décor supplémentaire, à tester seulement si la grille convient |
| `entites_test.json` | 11 monstres/familiers du roster, 2 PNJ, 1 amorce de quête, 3 points de Traque, 1 piège, 1 gisement, 1 départ | n/a | Entités à recréer comme champs dans LDtk ou comme nœuds dans Godot |
| `inventaire.json` | 22 fichiers : source, auteur, licence, taille | n/a | Traçabilité |
| `apercu_kit.png` | aperçu de tout le kit | n/a | Vue d'ensemble |

## La zone d'essai (identique dans les deux outils)
- **Carte** : 40×30 tuiles (1 280×960 px), vue 3/4, zone « Marches Frontalières » : clairière, chemin, un cours d'eau, un bosquet, un site de ruines.
- **Calques** : sol (autotile), obstacles (arbres, rochers, eau), décor, entités.
- **Entités à poser** : départ du héros, 3 points de Traque (jetons 1 à 3), chef de meute et 4 éclaireurs (`cro02` et `cro01`, ou les silhouettes), un piège, un gisement, un PNJ, une amorce de quête.
- **Champs d'entité** (LDtk) / propriétés (Godot) : `cle_id` (roster), `dd`, `tags`, `jeton`.
- **Arène latérale** : une seconde carte, plateforme, 120×15 tuiles, avec les tuiles de `tuiles_plateforme/`.
- **Mesures à noter** : temps pour peindre la zone, temps pour poser les entités, temps de rechargement après modification, lisibilité du résultat, fluidité sur le téléphone.

## Rappels
- Hauteur de l'image de jeu : 360 px ; héros : 64 px de profil, 48 px en vue 3/4 ; boss ≤ 320 px.
- Les silhouettes ne sont pas des sprites : ce sont des rectangles étiquetés, pour voir les proportions.
- Quand PixelForge produira les tuiles et sprites définitifs, remplacer fichier par fichier ; les noms des entités (`cle_id`) ne changent pas.
