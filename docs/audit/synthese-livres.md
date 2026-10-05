# Synthèse de l'audit des 10 livres CRS

Rédigée le 2026-10-05. Détail complet, livre par livre : `notes-lecture-livres.md`.

## Ce qui a été lu, et comment

| Livre | Lecture |
|---|---|
| I Règles, II MJ, V Histoire, VI Écoles, VII Métiers, VIII Joueur, IX Annexes, X Compléments, IV Atlas | lus en entier (ou en entier pour les parties de règles, balayage structurel pour les 30 fiches de métiers et les fiches de clans répétitives) |
| III Bestiaire (35 000 lignes) | **pas lu mot à mot.** Analyse par script de toutes les fiches (266) + lecture complète de 4 fiches types et de tous les index. Les chiffres individuels de chaque créature n'ont pas été relus. |

Ce qui manque : les 8 autres livres que tu possèdes (tu parlais de 18). Je n'ai pas pu vérifier ce qu'ils disent.

## Le verdict, franchement

Les livres sont riches, cohérents dans l'esprit, et le Livre I contient déjà le jeu vidéo (la Boucle de Chasse). Mais **ils ne forment pas encore un système unique**. Ils ont été écrits par couches, avec au moins deux « générations » de règles qui se contredisent sur les fondations : le Livre I (et le Bestiaire) décrivent un système à peu de cases, sans niveaux de personnage, avec attributs FOR/AGI/END/ESP/VOL/PRE ; les Livres IX et X (et une partie du VII) décrivent un système à niveaux 1–30, à XP, à CA, avec des attributs de type D&D. Les deux sont jouables, **ils ne sont pas compatibles**.

Pour le Jeu B, c'est exploitable. Mais il faut **trancher avant de coder les jauges, les dégâts et la progression**, sinon on codera un hybride.

## Les 10 décisions à prendre (par ordre d'urgence pour le jeu)

Chaque ligne : le conflit, mon avis, ce qui change si tu décides autrement.

| # | Conflit | Sources | Ma proposition | Impact Jeu B |
|---|---|---|---|---|
| 1 | **Système d'attributs et de jauges** : FOR/AGI/END/ESP/VOL/PRE, Vitalité = 4 + END, Endurance 10 fixe (L1, Bestiaire) contre Force/Dextérité/Endurance/Intelligence/Sagesse/Charisme, Vitalité = 10 + 2×FOR + END (L10) | L1, L3, L10 | **Garder le Livre I** (le Bestiaire, 266 fiches, l'utilise déjà). Traiter le Livre X §1 et §5 comme à réécrire. | Définit toutes les barres de vie et d'énergie du HUD. Bloquant. |
| 2 | **Niveaux de personnage et XP** : jalons narratifs sans XP (L2) contre XP par métier (L9) contre niveaux 1–30 avec XP cumulée (L10) | L2, L9, L10 | Pour un jeu vidéo : **XP par métier, niveaux 1–30 du Livre VII** (déjà chiffrés avec DD), les jalons narratifs servent pour les paliers 5/10/15/20/25/30. | Définit l'arbre de progression, les récompenses de chasse. |
| 3 | **Modèle de dégâts** : un dé qui frappe l'Endurance d'abord (L1) contre d12 sur Vitalité + coût d10 d'Endurance (L2/L9) | L1, L2, L9 | À arbitrer **par test jouable** : le prototype de combat doit appliquer un seul modèle. Je proposerais celui du Livre I (cases peu nombreuses, lisibles à l'écran). | Cœur du combat. Bloquant pour le prototype. |
| 4 | **Échelle de l'Honneur** : 0–10, ou −25/+25, ou Karma | L1, L2, L10, L8 | **0–10 avec 5 seuils** (déjà utilisée par les prérequis des Postures et par les armures du Livre X). Traiter −25/+25 comme une échelle de gains cumulés. | Interface du Retour au Clan, conditions de déblocage. |
| 5 | **Forge : collective ou individuelle, 20 ou 40** | L1, L2, L9 | Forge **individuelle**, paliers de 10 de 0 à 40 (comme dans la table du Livre I) ; le Bastion donne un bonus collectif. | Progression d'artisanat et d'équipement. |
| 6 | **Rangs des créatures** (4 symboles ◆, I–V/VI, Courant/Rare/Élite) et table CR fausse | L2, L3, L4, L10 | Une seule table : ◆ Commun CR 1–4, ◆◆ Rare 5–9, ◆◆◆ Élite 10–15, ◆◆◆◆ Légendaire 16+ (c'est ce que les index donnent réellement). Mapper I–IV. Supprimer « rang V » et « rang VI » ou les définir. | Difficulté des chasses, XP des créatures. |
| 7 | **Phases de combat** : 3 phases à 60/30 (L1) contre 1 à 4 phases à seuils variables dans les 266 fiches | L1, L3 | **Garder les seuils des fiches** (ils sont écrits). Corriger le Livre I pour dire « 1 à 4 phases, voir fiche ». Les 5 états deviennent optionnels. | Machine à états des boss. Déjà adapté à 4 phases. |
| 8 | **Tendue (réussite tendue)** : DD..DD+1 (L1) contre DD..DD+4 (L2) contre intervalles de dés (L9) | L1, L2, L9 | **DD..DD+4** (le plus pratique, défini dans le Livre II). Aligner L1 et L9. | Résolution des jets en jeu. |
| 9 | **Métiers : 3 étoiles, 30 niveaux, 2 ou 3 métiers max** | L1, L2, L7 | 30 niveaux ; ★ = niveaux 1–10, ★★ = 11–20, ★★★ = 21–30 ; **2 métiers** (un troisième = variante spéciale). | Arbre de professions. |
| 10 | **Éléments** : Feu/Eau/Terre/Vent/Foudre (A), Wu Xing (B), + Air/Glace (C), + Poison/Ombre/Dragon (Bestiaire), + Éther (L10) | L1, L5, L6, L7, L3, L10 | Un tableau unique (par exemple : 6 éléments Feu, Eau, Terre, Vent, Foudre, Glace ; + Ombre et Éther comme « énergies » ; Poison/Paralysie/Sommeil = états, pas éléments). | Faiblesses des boss, enchantements, palette de couleurs des effets. |

Autres points structurants, à traiter après :

- **Phoenix** : deux versions (quatre phoenix domestiques de CR 10–11 dans le Bestiaire, phœnix primordiaux secrets dans l'Atlas). À résoudre avant d'écrire la trame.
- **Bastion** : quatre échelles (niveaux de bâtiments L1, Ancrage 0–20 L2, rang I–III de l'Atlas, rang 1–20 du L10).
- **Ordres/clans** : 12 ou 14 clans, 7 ou 8 ordres, blocs d'influence à trois définitions.
- **Nom du monde** : Palmaria ou pas.
- **Géographie** : positions cardinales des régions contradictoires, pas de carte. Ne pas dessiner de carte avant d'avoir figé ce point.
- **Frise du temps** : 200, 300 ans, 2 ou 4 siècles selon les livres.
- **Tables truquées ou tronquées** : tables d12 des régions (L9), index d'ancien format (L9), Forgeron d'Armures (L7), textes coupés (L7).

## Ce qui est solide, et que le jeu peut prendre tel quel

- La **Boucle de Chasse en 4 temps** (Livre I) et le **Retour au Clan** (Récolte, Récit, Rituel).
- Les **fiches de créatures** : trois attaques par phase, faiblesses, points faibles, matériaux, brisures. Un script peut les transformer en données de boss.
- La **Trinité Acte/Trace/Conséquence** pour le journal d'événements PocketBase.
- Les **60 hooks de quête**, les **40 tensions actives** (compteurs de monde), les 8 cartes d'exploration phœnix de l'Atlas, les contrats de la Guilde de Chasse.
- Les **recettes d'alchimie** (≈ 50), les **bonus de série d'armures**, la météo par terrain.
- Les 14 types d'armes : 6 familles d'animation (voir `livres-crs-vers-jeu-b.md`).

## Points que le jeu doit corriger tout de suite

1. **Les noms de monstres et le roster** : une grande partie du Bestiaire transpose des monstres de *Monster Hunter* avec des noms respellés (liste dans les notes du Livre III). Pour un jeu commercial, c'est un risque sérieux. À régler **avant** de produire les sprites de boss : nouveaux noms et nouvelles silhouettes, même si les statistiques et les comportements restent. Je pense que tu devrais le faire même pour la table, pour que le projet soit entièrement tien.
2. **Les Dragons Anciens (9 à 14 m)** ne rentrent pas dans la limite des 320 px. Les traiter comme des décors/événements (par exemple 3 séquences cinématiques), pas comme des sprites de boss.
3. **Le premier boss** : un Velodrak ou équivalent (CR 4, 2 phases, adds de meute). C'est la bonne taille et la bonne complexité pour valider animation, hitbox et machine à états.

## Ce qu'il faudra ajuster dans les livres plus tard (ordre conseillé)

1. Trancher les 10 décisions ci-dessus ; écrire une page « Règles canoniques » de 2 pages que tous les livres suivent.
2. Corriger les livres un par un en suivant : I, II, IX, X (règles), puis III (rangs, phases), puis VII (tableau du Forgeron d'Armures, textes tronqués), puis V et IV (frise, géographie).
3. Régénérer les index du Livre IX (anciens numéros de chapitres, tables d12 tronquées) à partir du contenu corrigé.
4. Faire la carte seulement après la correction de la géographie.

## Interaction avec les décisions déjà prises pour le Jeu B

- **Hauteur 360 px, héros 64 px, boss ≤ 320 px** : cohérent avec le Bestiaire pour 184 créatures sur 210 (tous les Dragons exceptés).
- **Quatre personnages = une histoire** : le Livre VIII donne déjà ce qu'il faut (origines, axes culturels, avantages/handicaps).
- **Pas de « nombre de niveaux »** : confirmé par la Boucle de Chasse. Mais le Livre VII contient bien des niveaux de **métier** (1–30), à ne pas confondre avec des niveaux de jeu.
- **Date cible 16 mars 2028** : compatible avec une démo **« une zone, une chasse complète, trois quêtes de plateforme »** si les décisions 1 à 5 sont prises dans les deux prochains mois. Sinon le risque est de coder deux fois le combat.
