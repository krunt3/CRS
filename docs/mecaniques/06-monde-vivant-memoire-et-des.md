# 06 — Monde ouvert vivant : mémoire du monde et jets de dés

Rédigé le 2026-10-05 après la précision de krunt sur la structure du jeu. Chiffres de départ à tester. Ce chapitre **complète et corrige** les cinq autres.

> **Mise à jour du 2026-10-06 (passe v3, décisions de krunt).** Deux points du chapitre d'origine sont **remplacés** : (1) il n'y a pas « quatre intrigues séparées » mais **une intrigue commune avec des différences** (mêmes faits fondateurs, mêmes antagonistes, mêmes échéances ; différences de statistiques, de métier, de clan, de marques et de fin) ; (2) **les trois autres joueurs apparaissent dans le mode solo de chacun, en PNJ** : « chaque joueur aura son personnage, et pas un autre » (chacun ne contrôle que le sien). La règle « Ne pas créer de copies PNJ » est donc supprimée. Arrivée : les trois autres arrivent **tous au moment du cataclysme, par un portail magique** (pas de calendrier étalé) ; ce qui se passe après l'arrivée est une case ouverte. Voir `docs/trame/10-trame-v3.md` §1 et §6.

## 1. Ce que krunt a décidé

1. **Quatre joueurs, quatre personnages, quatre mondes.** À la table (JDR en ligne avec un Maître du Jeu), les quatre joueurs jouent ensemble. Dans le jeu vidéo, **chacun joue son personnage de son côté, en solo, dans un monde ouvert en pixel art**. ~~Il n'y a pas forcément une seule intrigue : chaque joueur développe la sienne.~~ **Corrigé (passe v3) : une intrigue commune, avec des différences par joueur.** Les trois autres personnages apparaissent dans le monde de chacun en PNJ. Le lien entre les joueurs, c'est la table et le journal d'événements (PocketBase), pas un réseau temps réel.
2. **Le monde se souvient.** Chaque interaction, chaque choix modifie le ressenti et la réaction du monde envers ce joueur. Exemple de krunt : tuer un animal blessé → les autres animaux ont peur de lui, le dressage devient presque impossible ; aider un animal blessé → l'animal peut lui rendre la pareille, se laisser dresser, ou (cas des dragons légendaires) l'aider ou l'attaquer.
3. **Il y aura des dés dans le jeu.** Dans les moments de réaction du monde (rencontre avec un animal, un dragon légendaire, dressage, négociation), le résultat dépend d'un lancer **aléatoire**, comme à la table. Le combat reste en temps réel, adresse du joueur.

## 2. Ce que cela change dans les chapitres 01 à 05

| Chapitre | Hypothèse des agents | Correction |
|---|---|---|
| Tous | « Un héros actif, les trois autres en compagnons ou soutiens » | **Corrigé (passe v3, décision de krunt)** : chaque joueur ne contrôle que **son** personnage, mais **les trois autres apparaissent dans son monde en PNJ** (tous arrivés au moment du cataclysme par un portail magique, comportement et mémoire du monde : `docs/trame/10-trame-v3.md` §6). La règle d'origine « Ne pas créer de copies PNJ » est **supprimée**. Les autres compagnons du joueur restent des PNJ originaux et des familiers. |
| 01 | « Combat sans d20 » | Reste vrai pour le **combat** (hitbox, esquive). Les dés interviennent **avant et autour** du combat : réaction des créatures, dressage, fuite, rencontres. |
| 02 | Artisanat déterministe | À garder (pas de perte de matériaux par malchance), sauf choix explicite du joueur (mode « Forcer »). |
| 04 | Joute en mode Auto par défaut | Compatible : on ajoute des **jets visibles** aux points de bascule (persuasion, défi, jugement). |
| 05 | Démo = un seul héros et un seul clan | Compatible : **un monde par joueur**, mêmes cartes et mêmes 60 amorces de quêtes, entrées différentes selon l'origine, le clan, le métier. |

## 3. La Mémoire du monde (système de marques)

### 3.1 Principe
Chaque événement du journal (Acte, Trace, Conséquence : Trinité du Livre I) peut déposer des **Marques** dans le monde de CE joueur. Les marques ne sont ni des points ni une jauge visible : ce sont des étiquettes, portées par une **cible**, qui modifient des jets, des distances de fuite, des prix, des accès. Le joueur les découvre par les réactions (animaux qui reculent, un clan qui se tait), comme l'Honneur du Livre II qui n'est jamais affiché en chiffres.

### 3.2 Cibles et portées
| Portée | Exemple | Effet typique |
|---|---|---|
| Créature individuelle | le monstre épargné, l'animal achevé | rancune ou dette envers ce joueur |
| Espèce (`cle_id`) | « les bipèdes de meute » | réaction de toute l'espèce |
| Famille (groupe du roster) | tous les canidés, toutes les grandes volantes | réaction de la famille, plus faible |
| Région | Hautes Terres Claniques | prix, accès, hospitalité |
| Faction (clan, guilde, ordre) | Porteurs de Cicatrices | réputation (chapitre 04) |
| Personnage (PNJ, dont les trois autres joueurs) | un PNJ compagnon se souvient d'un geste cruel | confiance, aide à la libération de la Braise, départ |
| Monde | « a tué un phœnix » | rumeurs, contrats, Terres Inconnues |

### 3.3 Table des gestes qui déposent une marque (extrait de départ)
| Geste du joueur | Marque (cible) | Valeur |
|---|---|---|
| Achever un animal blessé qui fuyait | Cruauté (espèce, famille) | −1 à −2 |
| Soigner ou nourrir un animal blessé | Dette (créature), Compassion (espèce) | +1 à +2 |
| Chasser selon les rites et le contrat | Respect (région) | +1 |
| Tuer un animal sacré sans rites | Sacrilège (région, faction) | −2 à −3 |
| Laisser fuir une créature (aucun matériau) | Clémence (créature) | +1 |
| Tuer un phœnix | Catastrophe (monde) | −5 et événement |

Les marques s'estompent lentement (une cicatrice, jamais complètement). Valeurs de départ à tester.

### 3.4 Effets mesurables
- **Réaction des animaux** : le cran d'attitude (voir 3.5) modifie la distance de fuite, la probabilité d'attaque et l'éveil des meutes.
- **Dressage** : `DD final = DD de la fiche (Livre III, de 6 à 18 selon l'espèce) + modificateur de marque`. Crainte : +4 par cran ; Hostile : dressage impossible tant que la marque n'est pas réparée. Confiance : −2 puis −4. Une Dette envers la créature individuelle peut ouvrir un **lien sans épreuve**.
- **Animaux légendaires** (grands volants, Fauves sacrés, phoenix) : la table de réaction 4.3.
- **Prix et accès** : les marques de région et de faction modifient prix, contrats, quêtes (chapitres 04 et 05).

### 3.5 Les cinq crans d'attitude (par espèce ou famille)
`Hostile (−2) · Craintif (−1) · Neutre (0) · Familier (+1) · Confiant (+2)`. Affiché au joueur par le comportement (animation de recul, de curiosité) et dans le carnet de pistage en mots, jamais en chiffres.

## 4. Les lancers de dés

### 4.1 Règle de base
Reprise des livres : **d20 + Attribut + Compétence contre un DD**, avec les issues du Livre II : **réussite** (≥ DD), **réussite tendue** (DD à DD+4, option 8 du formulaire), **échec**, **20 naturel** (réussite critique), **1 naturel** (échec critique). Le jet est **montré** (animation de dé, liste des modificateurs) : le joueur voit ce qui pèse.

### 4.2 Où les dés interviennent
| Moment | Jet | DD de départ |
|---|---|---|
| Réaction d'une créature sauvage non hostile | d20 + Présence + compétence Pistage ou Dressage | DD de la fiche ± marques |
| Dressage (Phase 1 Approche, Phase 3 Apprentissage) | d20 + AGI/ESP + Dressage | DD de la fiche (Livre III) ± marques |
| Rencontre d'un animal légendaire | table 4.3 | DD = 14 + CR/2 |
| Persuasion, défi, jugement | tournant de la joute (chapitre 04) | DD de l'interlocuteur |
| Poursuite, fuite du monstre | jet de l'Écart (Livre II) | selon l'Écart |
| Événements de voyage, tables d12 des régions | d12 du Livre IX | — |

**Pas de dés** pour : toucher ou être touché au combat, esquive, fabrication, dépenses.

### 4.3 Table de réaction d'un animal légendaire (exemple)
Jet : d20 + Présence + bonus de marque ± Dette.
| Résultat | Issue |
|---|---|
| 20 naturel | La créature aide spontanément (attaque un autre monstre, emporte le joueur) ou ouvre un lien symbiotique. |
| ≥ DD+5 | Lien proposé (épreuve de dressage allégée). |
| DD à DD+4 | Tolérance : la créature observe, suit, laisse une plume ou une trace ; piste vers une quête. |
| < DD | Indifférence : elle s'éloigne. |
| ≤ DD−6 | Hostilité : elle attaque ou charge. |
| 1 naturel | Attaque immédiate, avec phase d'alerte raccourcie. |
Les Dragons Anciens ne sont pas concernés par la table : ce sont des événements cinématiques (décision de krunt).

### 4.4 Garde-fous contre la frustration (propositions)
1. **Information avant le jet** : le joueur voit quelles marques pèsent (un symbole de cran) et peut renoncer.
2. **Relance limitée** : un nombre de points (de Destin, ou Jetons de Connaissance) à définir.
3. **Résultat enregistré dans le journal** : recharger la sauvegarde ne refait pas le jet (graine liée à l'identifiant d'événement).
4. **Un échec critique est une aventure, pas une punition** : l'attaque d'un légendaire ouvre une chasse ou une fuite jouable.
5. **Option de difficulté** : mode « sans hasard » (les jets prennent la valeur moyenne) pour qui préfère.

## 5. Ce que cela demande aux données
Nouvelles collections PocketBase (proposition) :
- `marques` : `{id, joueur_id, portee, cible_id, tag, valeur, evenement_id, date, estompe_a}`.
- `attitudes` : `{joueur_id, cible_id, cran}` (calculé depuis les marques).
- `jets` : `{id, joueur_id, evenement_id, contexte, d20, modificateurs[], dd, resultat}`.
Le roster `donnees/monstres/*.json` fournit déjà `cle_id`, `familier.difficulte_dd`, `lien_max`, `cr`, `groupe`. Le journal (Acte/Trace/Conséquence) devient la source de vérité ; le Maître du Jeu peut y lire et y écrire pour injecter des conséquences dans le monde de chaque joueur.

## 6. Une intrigue commune, quatre mondes
- **Un monde par joueur, une intrigue commune avec des différences.** Mêmes cartes, mêmes 20 régions, mêmes 40 tensions du monde, mêmes faits fondateurs ; l'**origine**, le **clan**, le **métier** et les **marques** décident des portes qui s'ouvrent et des indices qu'on obtient. Les trois autres joueurs sont des PNJ du monde.
- **Les arcs personnels** viennent de gabarits (hooks de l'Atlas) filtrés par l'origine et les marques, plus quelques arcs écrits à la main par joueur (la « trame » du projet).
- **Un cadre commun pour la table** : les quatre mondes partagent un calendrier et des tensions de départ identiques, pour que les récits se rejoignent aux sessions JDR. Le Maître du Jeu peut y faire avancer une tension pour tous.
- **Monde ouvert pixel art** : à l'échelle d'un développeur seul, il s'agit de **grandes zones reliées** (carte-monde par îles et zones débloquées, chapitre 05), chargées une à la fois, pas d'un monde continu. Démo : une zone.

## 7. Honnêteté sur l'ampleur
- La mémoire du monde est **bon marché si elle reste de la donnée** : une table de gestes, des marques, cinq crans, quelques effets. Elle devient **très chère** si on veut une simulation d'animaux individuels. Je recommande : espèce et famille seulement, créature individuelle réservée aux animaux liés à une quête.
- Quatre mondes sur une même intrigue multiplient l'écriture des différences (lentilles d'indices, voie solo et voie table, comportement des PNJ). Sans gabarits, c'est le mur de production. Il faut un moteur d'amorces (Atlas : 60 hooks) plutôt que quatre scénarios.
- Le hasard visible fait partie du pitch (« comme à la table ») ; c'est un choix à tester avec de vrais joueurs, pas à défendre sur papier.

## 8. Questions ouvertes
1. Le journal est-il la seule jonction entre joueurs, ou y a-t-il un événement partagé (messagerie, objet donné par le MJ) ?
2. Les marques sont-elles visibles par le MJ dans CharForge ? (Recommandation : oui.)
3. Relances : Points de Destin ou Jetons de Connaissance ?
4. Mode « sans hasard » : oui ou non ?
5. Démo : quelle zone et quels gestes déposent des marques ? (Recommandation : 6 gestes, 2 espèces, la zone des Marches Frontalières.)
