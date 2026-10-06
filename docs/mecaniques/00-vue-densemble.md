# Mécaniques du Jeu B : vue d'ensemble

Rédigée le 2026-10-05 à partir des cinq chapitres produits par des agents (relus ici par leurs sommaires et leurs questions ouvertes, **pas ligne à ligne**). Tous les chiffres sont des **hypothèses à tester**. Elles appliquent mes propositions provisoires de la section « Règles des livres » du formulaire de cadrage : rien n'est figé tant que krunt ne les a pas validées.

| Chapitre | Contenu | Lignes |
|---|---|---|
| [01 Chasse et combat](01-chasse-et-combat.md) | Boucle de chasse en 4 temps, combat tactile en temps réel, modèle de dégâts à tester, phases, jetons, brisures, matériaux, premier boss décrit pas à pas | 896 |
| [02 Bastion, forge, artisanat](02-bastion-forge-artisanat.md) | Hub de Bastion et Phase de Bastion en 5 écrans, 18 bâtiments, forge, alchimie, récolte, défense du Bastion | 862 |
| [03 Écoles, métiers, arbres](03-ecoles-metiers-arbres.md) | Création et prologue, système d'arbres de compétences (JSON), courbe d'XP, quatre personnages | 704 |
| [04 Diplomatie, joutes, réputation](04-diplomatie-joutes-reputation.md) | Joute verbale tactile (5 variantes), réputation par faction, Retour au Clan, dialogues, 4 scènes | 777 |
| [05 Clan, monde, économie, familiers](05-clan-monde-economie-familiers.md) | 14 clans, campagne en saisons, carte par îles, 40 tensions, économie, dressage et élevage | 648 |

## La boucle d'une saison (assemblage des cinq chapitres)

Traque en vue 3/4 (jetons de connaissance, pièges, météo) → Affrontement en arène latérale (dégâts, brisures, phases, familier) → Retour au Clan (Récolte, Récit, Rituel : scène de dialogue, réputation, Honneur) → Phase de Bastion (5 écrans : rapport, forge, activités, événement, projection) → voyage, tensions du monde, nouvelle désignation. Les quêtes de plateforme alimentent la récolte et le monde. Tout écrit un Acte / une Trace / une Conséquence dans le journal PocketBase.

## Les décisions qui reviennent dans plusieurs chapitres

Ce sont celles qui, tant qu'elles ne sont pas tranchées, bloquent l'écriture du code. Mon avis (franc) est indiqué.

1. **Un héros ou quatre ?** Les chapitres 01, 03, 04 et 05 butent tous sur le même point : « quatre personnages, quatre joueurs ». Trois lectures : (a) un joueur, un héros actif, les trois autres en compagnons/soutiens ; (b) coop locale ou asynchrone ; (c) coop en ligne temps réel. **Mon avis : (a) pour la démo, (b) plus tard, (c) hors de portée en solo.** C'est la décision la plus structurante. **Mise à jour du 2026-10-06 (décision de krunt)** : chaque joueur ne contrôle que **son** personnage ; **les trois autres apparaissent en PNJ dans son mode solo** ; la **démo n'a que Krunt**. Voir `docs/trame/10-trame-v3.md` §6 et §8.
2. **Modèle de dégâts.** Le chapitre 01 recommande le modèle C : deux barres séparées (Vitalité = vie, Endurance = carburant), car le modèle du Livre I (l'Endurance absorbe les coups) crée une spirale de mort en temps réel. C'est **différent** de ma proposition provisoire (Livre I). **Mon avis : l'agent a raison sur le fond ; on le tranche par le test des 3 builds du chapitre 01 (§4.6).**
3. **Périmètre des Écoles et Métiers.** Chapitre 03 : plafond réaliste 11 Écoles et 12 Métiers en v1.0, dont 4 Écoles et 3 Métiers en démo ; fondre les Écoles Techniques et le bloc Magie dans les Métiers et le Bastion. **Mon avis : oui.**
4. **Un seul Bastion partagé** par campagne (forge, liens PNJ et inventaire par personnage). **Mon avis : oui.**
5. **Artisanat déterministe**, jamais de perte de matériaux par malchance ; les mini-jeux de forge et de dépeçage restent facultatifs. **Mon avis : oui.**
6. **Honneur jamais affiché en chiffres** ; réputation = mémoire par faction construite depuis le journal ; Infamie remplacée par des « Marques ». **Mon avis : oui.**
7. **Pas de mort définitive** (héros, PNJ liés à la trame, familiers) : séquelle cosmétique, K.O., rupture de lien. **Mon avis : oui, c'est le bon choix sur mobile.**
8. **Phoenix : suivre l'Atlas** (primordiaux, secrets) et transformer les quatre fiches du Bestiaire en liens de cycle ou événements. **Mon avis : oui, mais c'est une décision de trame.**
9. **Taille du premier boss** (70 px à peine plus que le héros à 64 px) : accepter un « boss d'apprentissage » ou appliquer un facteur de lisibilité de 1,3 à tous les monstres. **Mon avis : le facteur 1,3 mérite un essai graphique avant de trancher.**
10. **Démo.** Cinq propositions convergentes : zone des Marches Frontalières, clan des Porteurs de Cicatrices (la Consignation = le journal), familier Alizade, un contrat de chasse (chef de meute + 4 à 6 éclaireurs), un seul Retour au Clan, une seule joute (défi d'honneur en Hautes Terres) + la persuasion, la couche Bastion minimale, 4 Écoles et 3 Métiers. **Mise à jour du 2026-10-06** : le héros de la démo est **Krunt seul** (J1 à J4, Braise affichée, première chasse du chef de meute, teaser de l'arrivée des autres) ; le choix du clan de démonstration reste ouvert (`docs/trame/10-trame-v3.md` §8 et Q27).

## Contradictions entre chapitres (à garder en tête)

- **« Un seul héros » (01, 03, 05) contre « quatre joueurs » (décision de krunt, 04 plus nuancé).** Voir point 1.
- **Honneur** : 01 propose une jauge cachée avec glyphe de seuil, 04 « jamais affiché », 05 « mode table affichant les chiffres pour le MJ humain seulement ». Cohérent si on retient « jamais en chiffres pour le joueur ».
- **Mana de départ** : 03 retient la table du Livre VI (6 à 8) ; la proposition provisoire disait Livre I. À corriger dans le formulaire.
- **Éléments** : 02 convertit Bois = Vent et Métal = Foudre pour les bonus de Bastion ; à valider avec le choix 10 du formulaire.
- **Difficulté de dressage** : 28 familiers sur 106 n'avaient pas de DD ; 11 retrouvés, 17 à compléter.
- **Poursuite** (01) : seule apparition de la plateforme dans une chasse ; coûteuse, hors démo.

## Vérification de réalité (honnête)

- Temps disponible : du 5 octobre 2026 au 16 mars 2028, environ 75 semaines. À 14–24 h par semaine : **1 050 à 1 800 heures au total**, sur lesquelles le développement des outils (CharForge, PixelForge, StoryForge, SceneForge) prend aussi du temps.
- Le seul chiffre de production fourni par les agents est celui de la diplomatie : environ **215 h** de technique et 25–30 h d'écriture pour **sa seule démo**. Les autres chapitres donnent des estimations en semaines (par exemple 3–4 semaines pour la couche Bastion de la démo) sans total consolidé. **Je ne vous donne pas de total** : il n'a pas été calculé et le faire sans prototype serait de la fiction.
- Ma conviction : **le combat et le premier boss (Dorgane) sont le vrai test**. Tant qu'ils ne sont pas jouables et amusants, la diplomatie, le Bastion et les arbres de compétences sont des paris sur du papier. La diplomatie est le pari le plus risqué (aucune référence existante, écriture qui devient « le vrai mur » au-delà de 400 h).
- Ordre conseillé : (1) prototype de combat avec les 3 builds de dégâts ; (2) une chasse complète ; (3) Retour au Clan simple ; (4) Bastion minimal ; (5) joute ; (6) arbres de compétences. La décision 1 (nombre de héros) précède tout cela.

## Ponts avec les données déjà produites

- `donnees/monstres/*.json` (272 entrées, 106 familiers) : utilisé par 01 (boss), 05 (dressage, transport).
- `docs/roster-monstres.md` : catalogue.
- `docs/audit/synthese-livres.md` : les 10 décisions des livres.
- Formulaire de cadrage : section « Règles des livres » (10 conflits) et section « Mécaniques de jeu » (décisions de ce document).
