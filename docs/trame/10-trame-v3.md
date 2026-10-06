# 10 : Trame v3 (canonique, consolidée)

Rédigé le 2026-10-06. Ce document est **autonome** : on peut le lire sans les documents 01 à 09. Il consolide les décisions de krunt (`00-decisions.md`, qui fait foi), la revalidation (`09-revalidation.md`) et les propositions des documents 03 à 08, avec les corrections « haute » de la revalidation appliquées. Il **remplace** les documents anciens sur les points suivants : ordre de Krunt3, métier de Taranis, clan de Pascal, coût du pacte, nom du rite, entité, sanctions de clan, rôle des trois autres joueurs en solo, démo, chronologie. Pour tout le reste (barèmes de simulation, JSON du VTT, briefs de sprites), les documents 04, 07 et 08 restent la référence, sous les réserves indiquées ici.

**Légende.** **[L]** = fait vérifié dans un livre (Livre I = règles, II = MJ, III = Bestiaire, IV = Atlas, V = Histoire et politique, VI = Écoles, VII = Métiers, VIII = Supplément Joueurs, IX et X = Suppléments MJ). **[P]** = proposition de ma part, à valider. **[INV]** = invention sans appui dans les livres (aucun nom propre inventé hors StoryForge, sauf marqué). **[?]** = lecture d'une parole de krunt, à confirmer. Tous les chiffres (DD, délais, crans) sont des hypothèses à tester.

---

## 0. L'essentiel en douze lignes

1. **Krunt3 est le héros.** Pour ramener sa famille détruite, il a accompli une technique oubliée (le Rappel). Cela a tourné mal : il est devenu le réceptacle d'une entité qui a arraché des inconnus à leur foyer pour les jeter près de lui (le « Filet »). Lieu d'arrivée : les Marches Frontalières, aux Ravins de Keth.
2. **L'antagoniste est l'Ordre du Flux** (vérité en couches, deux fausses pistes). Le Flux « ne ment jamais » : il est seulement absent de la fiction tant que personne ne l'interroge.
3. **L'entité** est une vérité en quatre étages (surface « malédiction », Écho de phœnix, Gardien du Nord, Krunt lui-même). Elle ne maudit peut-être pas Krunt : elle l'empêche de mourir de ce qu'il a fait.
4. **Le coût du pacte est la Braise** : une jauge de 8 crans et un cadran de 24 h. L'ancien coût par l'oubli de noms et l'ancien nom du rite sont **retirés entièrement** (décision de krunt, journal `00`). Le rite funéraire s'appelle **la Veillée** et la technique **le Rappel** (**[?]** noms proposés, à confirmer).
5. **Chaque clan a son honneur.** Certains clans sont donneurs d'ordres (refuser leur mission est une faute) ; d'autres sont gardiens d'une légende (savoir qu'un lien existe avec le phœnix est un grand avantage ; les jeunes l'ignorent, les anciens s'en offusquent). Tout passe par l'Honneur 0 à 10, la réputation de faction et les Marques (§5).
6. **Les trois autres joueurs apparaissent dans le solo de chacun, en PNJ** (arrivée J3 à J10). Chaque joueur ne contrôle que **son** personnage (§6).
7. **Un monde par joueur**, une **intrigue commune avec des différences** (lentille d'indices, clan, métier, marques, fin). La table (JDR en ligne) recoupe les quatre mondes.
8. **Chronologie J0 à J60** consolidée (§7) : une seule table, sans doublon de Neuf Nuits.
9. **Démo : Krunt seul**, J1 à J4, Braise affichée, survie, première chasse du chef de meute, teaser de l'arrivée des trois autres (§8, douze étapes).
10. **Les fiches v2 sont des essais** (krunt : ne pas les suivre à la lettre). Taranis part avec un bagage ; Pascal n'a que l'attaque de base avant ses bombes.
11. **La simulation est rejouée** avec la fiche v2 de Taranis et la Défense 18 de Pascal : Taranis n'est plus le premier des dégâts (29 à 30 %), et le rôle de tank de Krunt3 reste impossible (voir `07`, §12).
12. **Questions ouvertes** : 30, dédupliquées, chacune avec ma proposition (§9). Les contradictions que je ne peux pas trancher y sont listées, pas tranchées.

---

## 1. Prémisse, thème, structure du jeu

**Prémisse.** Suite à la destruction de sa famille, Krunt utilise une technique oubliée pour la faire revivre. Cela tourne mal : un pacte à payer, un coût d'utilisation. Krunt devient le réceptacle d'une entité mystérieuse ; d'autres personnes du continent sont transportées jusqu'à lui. Elles peuvent l'aider (Loyauté, Compassion) ou l'abandonner (l'honneur de leur clan est en jeu, §5). La survie est difficile : eau, abri, créatures, Corruption, en terres hostiles.

**Thème.** *Ce qu'on refuse de perdre finit par nous posséder.* Krunt a refusé de perdre les siens ; son clan, les Lames Franches, a pour devise « Nul ne nous commande. Nul ne nous possède. » [L Livre V clan 2]. Le Flux punit ce qui *persiste* au-delà de son cycle ; Krunt a refusé le cycle.

**Les trois antagonismes.** (1) l'antagoniste de la famille (l'Ordre du Flux, §3), (2) l'entité et son coût (§4), (3) la pression des clans et les terres hostiles (§5 et §7).

**Structure en solo et à la table.**
- À la **table** (JDR en ligne) : quatre joueurs. Krunt (le joueur) est aussi le MJ : Krunt3 est donc **PNJ pendant les phases de JDR**, et un autre MJ pourra prendre la suite ; krunt joue son personnage.
- Dans le **jeu vidéo** : chaque joueur joue **son** personnage, seul, dans **son** monde ouvert en pixel art. Les trois autres personnages apparaissent dans ce monde en **PNJ** (§6). Les quatre mondes partagent un cadre commun (mêmes faits fondateurs, mêmes antagonistes, mêmes échéances) et le journal d'événements (PocketBase) est la jonction avec la table.
- **Intrigue commune avec différences** : statistiques, métier, clan, marques déposées, fin. Chaque indice a une voie solo et une voie table (§3.4).
- **Dés visibles** aux moments de réaction du monde ; **le monde se souvient** (marques) ; **pas de mort définitive**.

---

## 2. Les quatre personnages (fiches courtes, v2)

Source détaillée : `08-fiches-v2-et-sprites.md` §3 et §7 (JSON). Valeurs corrigées par la revalidation : Taranis 5/11/6/9/6/5 (Vit 10) ; Pascal 7/6/8/9/5 (+1 VOL)/**7** (somme **42**), Défense **18** (cuir +2, bouclier +2) ; aucune Résonance à la création (une Résonance ne s'acquiert que par changement de Posture [L Livre VI]).

| | **Krunt3** | **Taranis** | **Cyril** | **Pascal** |
|---|---|---|---|---|
| Rôle | Héros, **fer de lance** (pas un tank) | Éclaireur-cartographe, tireur | Soin, serment, voix | Rempart alchimiste |
| Région (Atlas, sans surnom) | Îles des Serments | Déserts Rouges | Cœur Impérial | Hautes Terres Claniques |
| Clan | Lames Franches | Navigateurs Gris | Sceau Pourpre | Sceau Pourpre (adoption par serment) |
| Guilde | Guilde Martiale | Guilde de Chasse | Marchands Libres | Guilde Martiale |
| Ordre | **Frères de l'Épreuve** (surnom « Ordre du Jugement ») | aucun | aucun | Sentinelles du Pacte [INV] **[?]** |
| Posture / École | Ours / Danse Rouge **[?]** | Loup / Souffle Long | Loup / Flux Tranchant | Loup / Gardien Mobile |
| Métier (★1) | Espion / Infiltrateur | **Chasseur-Pisteur + Cartographe** | Mage Blanc | Alchimiste |
| Attributs FOR/AGI/END/ESP/VOL/PRE | 9/8/8 (+1)/4/7/6 | 5/11/6/9/6/5 | 5/6/6/8/9/8 | 7/6/8/9/5 (+1)/7 |
| Vitalité / Endurance / Mana [?] | 13 / 10 / 6 | 10 / 10 / 6 | 10 / 10 / 8 | 12 / 10 / 6 |
| Défense (avec armure) / Honneur | 19 / 4 | 19 / 4 | 13 / 5 | **18** / 6 |
| Attaque | deux lames courtes (Double Lame 1d6+1d6) | arc long (1d8, 80 m) | épée longue (1d8) | épée courte et bouclier (1d6) ; **attaque de base seule** jusqu'aux bombes (niveau 4, Livre VII) |
| Avantage clé / handicap | Maîtrise de Combat ; Réceptacle (neutre) + Dette de Sang du pacte | Préparateur Obsessionnel (bagage) ; Dette de Sang envers le Cercle des Boussoles Éteintes | Nom Respecté, Canal Stable ; Serment Absolu | Corps Endurci, Ingénieur Méthodique ; Blessure Ancienne |
| Lentille d'indices | l'intérieur (ce qui l'habite, le Cercle de Fer) | **La Route** (réseau, boussole, Nord) | **La Loi** (serments, cohérence, Archives) | **La Matière** (cendres, sel de restitution) |
| Tentation d'abandon | aucune (c'est lui qui est abandonné) | rentrer : le plus facile côté route | bloquée par son serment | loyauté de Sentinelle contre sa Veille quittée |
| Éclats / provisions de départ | 30 | 120, **bagage complet** | 90 | 60 |

**Notes de cohérence.**
- **Krunt3** : un Lame Franche (aucun territoire, aucun maître permanent) qui est aussi un Frère de l'Épreuve (ordre de juges) : tension de rôle utile [L Atlas région 6]. Son sprite à la hache à deux mains est **à refaire** (deux lames courtes, décision de krunt). Variante « porteur » du sprite : signes ambigus (veines chaudes, mèche cendre), sans spoiler.
- **Taranis** : chez lui **côté clan et guilde** aux Marches (Navigateurs Gris et Guilde de Chasse y dominent [L Livre V l.369-395]), mais **étranger côté naissance** (Déserts Rouges). « Aucun clan ne protège » ne vaut que pour les trois autres. Il part avec un **bagage de départ** (carquois, instruments de cartographe, carnet de pisteur, 7 jours de rations, 2 Herbes Stabilisantes, Carnet des Routes avec une zone blanche aux Ravins de Keth, boussole éteinte) : un avantage fini, épuisé vers J10.
- **Cyril et Pascal** sont tous deux Sceau Pourpre (décision de krunt) : ils sont « frères de serment » ; un seul des deux a prêté un serment d'aide (§5, §3.4).
- **Trois Loups et un Ours** : hasard de création assumé ; on recrutera un joueur ou un PNJ au besoin (§9, Q28). Les trois Loups se différencient par l'École (Rituel, Flux, Ancrage), le métier et le rôle de meute.
- **Combat** (rejoué, voir `07` §12) : Krunt3 avec Double Lame et cuir **ne tient pas la première ligne** (Provocation ponctuelle seulement). Taranis avec le bagage v2 vaut 41 % de victoire en solo contre 12 % sans les Herbes ; il n'est plus le premier des dégâts (29 à 30 % à quatre).

---

## 3. L'antagoniste : l'Ordre du Flux, en couches

### 3.1 Ce que disent les livres [L]

- **Ordre du Flux** : Brise-Flux « envoyés quand la négociation échoue et la dette devient existentielle » ; rituels *Rite de Restitution*, *Bris de Stagnation* (« destruction rituelle d'un lieu ou d'une lignée, jamais improvisée »), *Droit de Correction des Arbitres* ; « ils ne mentent jamais, ne sauvent personne, ils équilibrent » ; alliés : Sceau Pourpre et **Maisons Anciennes** ; hostilités : Porte-Flammes, Voile Noir (Livre V ch. 5 et ch. 7). Nécrotechnie « interdite universellement par l'Ordre du Flux » (Livre VI ch. 11).
- **La huitième famille** : « Une huitième famille existait, non identifiée, ou délibérément ignorée. Elle opère encore. [...] extension de *mémoire collective*. L'Ordre sait qu'elle existe. Il n'a pas encore décidé si ça constitue une dette. » (Livre V ch. 8, Purge des Sept Lignées, il y a environ 150 ans).
- Le Livre V ne donne **aucune hostilité** Flux/Lames Franches (c'est une déduction **[P]**) ; il donne l'alliance Flux / Maisons Anciennes, qui appuie la couche 3.

### 3.2 La vérité en couches

| Couche | Quoi | Qui | Découverte |
|---|---|---|---|
| Surface (version officielle) | « Éboulement magique, catastrophe de Corruption, bête » | Rapport de la Guilde de Chasse locale | Prologue |
| **Fausse piste 1** | « L'Administration des Pratiques a tué des praticiens non déclarés » (Audit de la Saison Rouge). Elle a réellement visité la ferme (visite d'audit **18 jours** avant le Bris : « aucune irrégularité »). Complice **involontaire** : elle a prêté son autorité sans connaître le but. | Administration des Pratiques (Sceau de l'Équilibre, Cœur Impérial [L Atlas]) | Semaines 1 à 3 |
| **Fausse piste 2** | Les Théocraties Sacrées (Purificateurs, Demande d'Inquisition) : motif crédible contre toute copie du cycle, mais elles auraient brûlé, publiquement. Menace de **deuxième acte** (poursuite de Krunt). | Théocraties Sacrées [L Atlas] | Semaines 3 à 8 |
| **Vérité 1** | Un *Bris de Stagnation* par le Flux sur la huitième lignée (la famille de Krunt) : une mémoire qui retient ses morts est une stagnation. Le Flux a **en partie raison** (le problème) et tort (la solution). | **Ordre du Flux** | Paliers 4 à 7 |
| Vérité 2 (option) | Un nœud du Voile Noir a dénoncé la famille au Flux, puis vendu à Krunt les cendres brutes et le Codex (courtier de Dureth). Intermédiaire, pas cause. | Voile Noir | Palier 6 |
| Vérité 3 (option, fin d'arc) | Une Maison Ancienne voulait effacer une lignée et ses archives ; Krunt est peut-être de son sang. Elle a dénoncé la « dette » au Flux plutôt que de tuer elle-même. Nom de la Maison : à choisir dans l'Atlas (Arkhen, Vosel) **[?]**. | Maison Ancienne (Lames de Succession) | Palier 7, fin d'arc |

**Pourquoi le Flux ne devient pas un méchant caricatural** : logique non humaine, peut avoir raison sur le problème et tort sur la solution (écho de l'Atlas ch. 14 §4). Le Sceau Pourpre (Cyril, Pascal) est son allié et garant de l'Accord des Cycles Normaux ; Cyril et Pascal ont donc, par leur clan, un lien lointain avec l'antagoniste (piste pour le MJ, pas un fait de fiche). **L'Ordre de Krunt3 est les Frères de l'Épreuve** (« Ordre du Jugement » = surnom populaire), **pas** le Flux. Le « Juge-mentor » qui a éloigné Krunt3 le jour du Bris est un **Gardien d'île des Frères**, mandaté ou trompé par le Flux ; le lien Krunt3-Flux passe par la loyauté ou la dette, pas par l'appartenance.

### 3.3 Les freins : pourquoi la vérité n'est pas découvrable trop vite

1. **Deux compétences croisées** par indice.
2. **Verrous de temps** : les paliers 4 à 7 n'existent pas avant la semaine 2 ou avant un événement. **Pas de jet tant que la condition n'est pas remplie** : le carnet affiche « rien à trouver pour l'instant » (un 20 naturel ne fait pas apparaître l'indice ; on n'a pas de jet qui échoue « parce que le monde ne répond pas encore », ce qui casserait la promesse de dés honnêtes).
3. **Contre-lecture** : chaque indice du Flux a une lecture plus facile qui pointe vers l'Administration ou les Théocraties.
4. **Témoins muets** : l'arbitre disparu, le Juge-mentor, le courtier du Voile, le Cercle de Fer des Lames (complice par omission).
5. **Le Flux ne ment pas mais ne parle pas** : l'Arbitre n'apparaît qu'au palier 7, si la bonne question a été posée (« Y a-t-il une dette envers le Flux sur cette famille ? »).

### 3.4 L'échelle de découverte (8 paliers) et la règle solo / table

DD indicatifs, d20 + attribut + compétence, jets **visibles**. Chaque palier donne un **indice**, pas la réponse. Deux échelles parallèles : **antagoniste** (0 à 7, ci-dessous) et **entité** (E0 à E7, §4.4).

| # | Quand | Indice | Talent | DD |
|---|---|---|---|---|
| 0 | Prologue | Version officielle : catastrophe ou bête | donné | n/a |
| 1 | Semaine 1 | **Pas de traces de créature** autour de la ferme ; cinq à sept paires de pas par la Voie des Cendres, chaussures grises de poussière, aucun sang | **Taranis** (Chasseur-Pisteur + Cartographe, Pistage, Observation) ; **Krunt3** en renfort (Espion) | 14 |
| 2 | Semaines 1 à 2 | La mort n'est pas de la Corruption : corps « rendus », sans signe nécrotique | **Cyril** (Lecture éthérique) ou **Pascal** | 15 |
| 3 | Semaine 2 | Poussière gris-bleu = **sel de restitution** ; le même sel contamine les sceaux de l'audit (renforce la fausse piste 1) | **Pascal** (Analyse de substances) | 16 |
| 4 | Semaines 2 à 3 | Archives de Loi : l'Accord des Cycles Normaux mentionne une « liste des exceptions » détenue par le Flux ; une lignée y est « en examen » | **Serment de Témoin** (Cyril ou Pascal) devant un Juge de Serment [INV] | 17 |
| 5 | Semaine 3 | Le **Cercle de Fer** savait la famille « en examen » et n'a pas prévenu | **Krunt3** (Code de la Lame Libre, Duel verbal) | 18 |
| 6 | Semaines 3 à 4 | L'ordre de mission qui a éloigné Krunt3 porte la signature de son **Gardien d'île** (Frères de l'Épreuve) ; le courtier de Dureth (Voile) a vendu cendres et Codex | **Taranis** ou **Krunt3** + réseau des Navigateurs Gris (ennemis du Voile) | 18 à 20 |
| 7 | Semaine 4+ | L'**Arbitre du Flux** répond sans mentir : dette, mandat, Rite de Restitution possible ; il ne dit pas qui a dénoncé | Poser la bonne question ; Sceau Pourpre pour contester le mandat en droit | 20 |

**Règle solo / table (chaque indice a deux voies).** *Voie table* : le joueur dont c'est la lentille le trouve ; le recoupement a lieu à la séance de JDR. *Voie solo* : le PNJ qui porte la lentille (§6) l'obtient et le vend à un prix (confiance, dette, faveur, temps), ou un PNJ passerelle le fournit (le Spectre aux Cendres, exorciste errant, déjà dans la campagne ; l'Ourse de Fer du Poste 7, neutralité absolue, « facture tout »). Un joueur Pascal peut ainsi atteindre les paliers 1, 5 et 6 en solo, **plus cher**.

### 3.5 Livres : écarts relevés et traitement

| Constat | Traitement dans cette trame |
|---|---|
| L'Atlas dit des Marches : « n'appartiennent à personne complètement » et « chaque acteur présent a une raison de ne pas vouloir de témoin » ; la formule « personne n'y est chez soi » **n'est pas dans l'Atlas** | Citer l'Atlas seulement ; retirer les guillemets de la formule fausse |
| L'arbitre senior disparu est du **Sceau de l'Équilibre**, à **Aurath** (Cœur Impérial) [L Atlas] ; le Sceau Pourpre (Livre V) et le Sceau de l'Équilibre (Atlas) sont deux entités | Le déclencheur du Sceau Pourpre n'est plus un « arbitre disparu dans les Marches » ; il tient au serment et au Rapport de Témoin |
| Le convoi de vingt personnes des Ravins de Keth s'est **caché volontairement** ; quelqu'un à Dureth a été payé pour signaler la « disparition » [L Atlas] ; aucun phœnix | **[P]** Le convoi portait les restes du phœnix tué ; le courtier de Dureth est la piste vers les mandants. Ce n'est pas dit dans l'Atlas |
| Le seul contrat de phœnix de l'Atlas vise « une créature de rang IV, région est, première Île des Brûlantes » ; le phœnix tué aux Ravins de Keth (nord) n'est pas celui-ci | **[?]** Q10 : en faire un second contrat |
| La phrase « la quantité de Corruption portée est visible » concerne un phœnix à sa mort, pas un hôte humain | Marquée **[P]** quand elle s'applique à Krunt |
| « Ancien Faucon » (avantage unique) et « Briseurs de Serments » (Lames) : absents des livres | **[INV]**. « Ancien Faucon » est retiré de la fiche de Taranis |

---

## 4. L'entité, la technique oubliée et le coût du pacte

### 4.1 La technique oubliée : A + B + C

| Piste | Ce que disent les livres | Apport |
|---|---|---|
| **A, cycle du phœnix** | Absorption, Saturation, Transformation ; mort violente = « libération non transformée » ; cendres post-renaissance neutralisent la Corruption [L Atlas ch. 13] | Les cendres, le filtre manquant |
| **B, Nécromancie interdite** | Mage Noir niv. 23 à 30 (« Déverrouillage Nécromancie » au niveau 30) [L Livre VII] ; Nécrotechnie interdite [L Livre VI ch. 11] ; Corruption : Nécro-animation +5 [L Livre II ch. 7] | L'inversion (retenir au lieu de délier) |
| **C, rite funéraire des Lames Franches** | **Rien dans les livres** (Livre VIII : axe « Mort Sacrée ») **[INV]** | **La Veillée** : on veille neuf nuits les morts pour les laisser partir ; le rite ne sait que *délier* |

**Histoire [INV].** Des soldats abandonnés sans sépulture ont copié la Transformation d'un phœnix à leur échelle (un feu, des cendres, des noms). Les « Veilleurs de Noms » ont été dispersés par la Guerre des Contrats Empoisonnés [L Livre V clan 2 : la guerre existe ; l'application au rite est inventée]. Il n'en reste qu'une lignée : celle de Krunt, la « huitième famille ». Elle conserve le **Rôle des Noms** et un fragment de la **Cendre Mère** (cendre du premier rite mêlée de cendres post-renaissance).

**Le Rappel (la nuit J0).** (1) le lieu : la ferme ruinée, éther instable ; (2) **les Neuf Nuits** de veille (T-9 à T0), *avant* le Rappel ; (3) le feu des noms : un **rite de clan**, pas une Technique d'École (Krunt3 n'a pas d'école de feu) ; (4) l'inversion : lire les noms à l'envers pour retenir ; (5) les cendres brutes, achetées à Dureth avec le Codex du Seuil ; (6) les corps se dressent, sans filtre : la Corruption s'accumule dans l'officiant ; (7) l'écho d'un phœnix entre par la porte ouverte.

**Ce qui tourne mal.** Pas de filtre (la Cendre Mère n'a suffi que pour un mort) ; la Corruption brute reste dans la zone et l'officiant ; l'Écho s'installe ; le Flux voit (toute nécro-animation est une dette) ; les Lames voient (« une lame qui retient les morts est un maître qu'on ne peut plus quitter »).

**Les Rappelés (la famille revenue).** Famille réduite à cinq **[?]** ; un seul est vraiment revenu, les autres sont des échos (Q8). Ils sont liés à Krunt par le **Fil de sang** et à leur foyer par la stagnation ; ils ne quittent pas un rayon d'environ un kilomètre. C'est la **Dette du Flux**, pas l'Écho.

### 4.2 L'entité : quatre étages

| Étage | Ce que c'est [P] | Veut | Agit | Ne fait pas |
|---|---|---|---|---|
| **0. Surface** | « Krunt est maudit : possédé par un esprit de feu » | (rumeur) | symptômes visibles | n/a |
| **1. L'Écho** | Le **cycle inachevé** d'un jeune phœnix tué en Absorption aux Ravins de Keth il y a ~11 mois **[INV]**. Un organe sans cerveau [L Atlas : le phœnix filtre « comme un rein »] | Finir sa Transformation (tendance, pas volonté) | Brûle la Corruption autour de Krunt (1 point/jour, 5 km), retient les Rappelés, envoie des images | Ne parle pas, n'attaque pas, ne pille pas la mémoire |
| **2. Le Gardien** | La volonté qui garde le Continent Nord (hypothèse C [L Atlas ch. 12 §4]) ; il perd un « organe » local à la mort du phœnix et se branche sur l'Écho | Clore le cycle brisé ; savoir si des humains ont compris le cycle ; garder le Nord fermé | Convictions, météo localisée, rêves ; **un seul acte fort : le Filet** | **Ne punit pas**, ne retient personne |
| **3. Krunt** | Un homme en deuil qui a forcé le cycle | Retrouver les siens | Sa voix, sa culpabilité : la voix des morts est en grande partie la sienne | n/a |

**Le « maudit » ou non** : la malédiction n'existe pas comme telle ; c'est la somme de trois dettes humaines (la Corruption de son rite, la Dette du Flux, la rupture avec les Lames) lue à travers un symptôme qui ressemble à une possession. Gardé comme **hypothèse que la table découvre**, pas comme vérité d'auteur (ambiguïté maintenue jusqu'à E2). **Indice central** : la Corruption **baisse** autour de lui (un malédicteur la sèmerait).

**Lecture du Gardien [?] (Q4)** : G3, le régulateur indifférent qui applique une règle et juge la compréhension du cycle ; G1 (protecteur) et G2 (geôlier) restent possibles et indiscernables jusqu'à E5.

**Pourquoi ces trois (Q5) [?]** : version mixte « deux appelés, un tombé ». Cyril et Pascal sont **appelés** (stabilisation et serment ; filtre) ; Taranis est **tombé** en apparence (le Filet prend une dizaine de personnes au hasard) mais **choisi par le Gardien** (un Navigateur est le seul passeur possible vers le Nord). Le hasard réel (trois Loups) est absorbé, pas expliqué.

### 4.3 La Braise (coût du pacte) **[P]**

Retrait complet, décidé par krunt : plus de prix par l'oubli de noms (la fatigue et le deuil suffisent), plus de rite portant l'ancien nom. **Le coût du pacte est la Braise.** Elle traduit « un pacte à payer, un coût d'utilisation » : le **coût d'utilisation** (chaque pouvoir la monte) et le **Loyer** quotidien (le pacte).

| Élément | Règle |
|---|---|
| **Affichage** | Un brasero sur Krunt (HUD du joueur ; au-dessus de lui quand il est PNJ) : **8 crans** en quatre états (Cendre 0-2, Braise 3-4, Flamme 5-6, Embrasement 7-8), un **cadran de 24 h** (aiguille = prochaine Aube). Pictogrammes, pas de chiffres (**[?]** Q2 : crans visibles) |
| **Loyer** | À chaque Aube : **+2 braises** ; **+3** si Krunt a dormi en zone de Corruption (cratère, Terres Ravagées). Premier Loyer : **J1 à l'Aube** |
| **Usages** | Absorption de Corruption **+1** ; Cycle Accéléré (5 m) **+2** ; Souffle du Réceptacle **+3** (Endurance pleine, +d6 de dégâts pendant 12 s) ; Signature Éthérique (passive) 0 |
| **Libération contrôlée** | 1 heure, action de Krunt, jet **VOL + Absorption, DD 13** (visible) : réussite −3, tendue −2, échec −1 et +1 Corruption, 1 naturel = Embrasement |
| **Aides** | Cyril : stabiliser (DD −2) ; Pascal : Onguent de Purge ou dosage de cendres (−1 braise par fiole) ; Taranis : un **lieu isolé** (DD −2) |
| **Seuil Flamme (5-6)** | Corruption de Krunt +1/jour ; créatures reculent (+1 cran de Crainte) ; Tension +1 la première fois |
| **Seuil Embrasement (7-8)** | À chaque combat ou stress : VOL DD 14, échec = Débordement (zone 5 m, chaleur 1d6) |
| **Embrasement** (9+ ou 1 naturel) | Libération non contrôlée : 3d6 de zone, +2 Corruption à Krunt, +1 aux alliés, Tension +1, Braise ramenée à 3, **Vacance** d'une scène, marque `embrasement` (Région). Les Marques de Pacte (progression) montent à chaque Embrasement |
| **Budget** | Journée normale : +2 Loyer, −3 libération = −1 net ; Krunt peut dépenser environ 1 braise par jour sans danger |
| **Gage** (soupape, **[?]** Q2) | Un allié prend 1 braise par serment libre (−1 Endurance max jusqu'au repos long, `loyauté`) ; refuser ne coûte rien, l'absence de Gage durcit la libération (DD +1) |
| **Registre** | Horloge du Flux (la Dette du Flux), pas le pacte : chaque Embrasement ajoute une ligne ; 6 lignes = mandat de Bris |
| **Vocabulaire** | « **Saturation** » est réservé au seuil de Corruption 19-24 [L Livre II] ; l'événement de trame (deux Embrasements en 7 jours) s'appelle **Embrasement général** **[?]** |

**Corruption de départ de Krunt** : 12 à 16 (pacte avec entité non reconnue +3, rite interdit +2 à +4, Nécro-animation +5, cendres brutes) [L Livre II ch. 7]. Montée : +1/jour à partir de Flamme, +2 par Embrasement. Un Embrasement par semaine atteint le seuil 19-24 en 4 à 6 semaines **[à tester]**.

### 4.4 L'entité par paliers (E0 à E7) et les fins

| # | Quand | Indice | Qui | DD |
|---|---|---|---|---|
| E0 | J1 | Krunt chaud ; la Tension se récupère mieux près de lui | donné | n/a |
| E1 | J2 à J5 | **La Corruption baisse autour de lui** ; les créatures corrompues le fuient | Cyril ou Pascal | 14 |
| E2 | Semaines 1-2 | Ce n'est pas de la Corruption mais de la **chaleur de phœnix** ; recoupement Pascal x Cyril | Pascal + Cyril | 16 |
| E3 | Semaine 2 | **Le Ravin** : cratère calciné, phœnix tué ; les cendres du cratère = celles de Krunt. Recoupement Taranis x Pascal | Taranis + Pascal | 17 |
| E4 | Près du **J14** | **La conviction** : une vague de « je dois rentrer » traverse les trois, sans contrainte ; le chemin du retour s'ouvre ; rappel de la cinquième expédition | Taranis + Cyril | 17 |
| E5 | Semaines 3-4 | **Le Gardien** parle (Langue du Pacte, rêve commun) : « rendu à l'origine » | recrue B ou les trois à la table | 19 |
| E6 | Semaine 4+ | La décision : le Gardien teste la compréhension | les trois | 20 |
| E7 | Fin d'arc | Ce que le Nord stocke (A, B ou C [L Atlas]) | choix de krunt | n/a |

E5 et E6 sont indisponibles avant la semaine 3 (pas de jet avant). **Fins (sort de l'entité)** : (1) *Délivrer* (finir le cycle chez un phœnix vivant ; Braise à 0, plus de pouvoirs) ; (2) *Contenir* (sceau runique ; Braise bloquée à 4 ; Krunt Veilleur) ; (3) *Exploiter* (bombe de purification ; mort de Krunt) ; (4) *Laisser faire* (Krunt marche vers le Nord) ; (5) *L'Écho allié* (pacte consenti : la Braise devient un Foyer, ressource). **Axe distinct** : le **choix du joueur envers Krunt** (aider, abandonner, livrer) ; un joueur peut finir sur une fin différente dans son monde (**[?]** Q12).

---

## 5. Système de clans et d'honneur

### 5.1 Principe : chaque clan a son honneur

Les livres ne prévoient pas de sanction de clan pour « abandon d'un inconnu » ; ils prévoient : des **obligations universelles** (défendre un membre en danger direct, ne pas agir contre les intérêts fondamentaux du clan) [L Livre V ch. 2 §3] ; une **échelle d'exclusion** (Désaveu discret, Mise à l'écart DD +3, Exclusion formelle, Exil [L Livre I ch. 9 §VII.c]) ; la **pression de clan** (désavantage, jet de Volonté ; résistances répétées = risque d'exclusion [L Livre I ch. 9 §V.b]). Krunt : chaque clan a **son** honneur. J'attache donc la sanction à l'**honneur propre** de chaque clan, jamais à une punition arbitraire. Rien n'est inventé en dehors des jauges existantes :

- **Honneur** du personnage (0 à 10, jamais affiché en chiffres [L Livre I ch. 1 §9] : Paria 0-1, Suspect 2-3, Reconnu 4-6, Estimé 7-8, Légendaire 9-10) ;
- **réputation de faction** (−60 à +100, paliers Banni / Hostile / Méfiant / Inconnu / Connu / Estimé / Allié / Intime, dérivée du journal, `mecaniques/04` §4) ; l'exclusion de Livre I s'y projette : Désaveu discret = Méfiant, Mise à l'écart = Hostile (DD +3), Exclusion formelle = Banni, Exil = Banni + Marque ;
- **Marques** (traces négatives permanentes, `mecaniques/04` §4.5) et **Dettes** (§4.6).

### 5.2 Les trois types de clans [?]

Lecture de krunt à confirmer : « certains clans [ont un but de donneur] donc il faut accepter de faire la mission qui lui est attribuée ».

| Type | Définition | Règle |
|---|---|---|
| **D, donneur d'ordres** | Le clan (ou la guilde, ou l'ordre) attribue des missions : contrats, défis, serments, missions de Passeur | **Accepter** la mission attribuée. **Refuser ou ignorer** = **faute d'honneur du clan** : réputation chez ce clan −8 (propagation aux alliés ×0,25), Honneur −1 si la faute est publique, Marque `refus_d_ordre` à la deuxième faute. L'acceptation seule ne rapporte rien ; la mission réussie rapporte (chasse de Contrat honorée +6 [`mecaniques/04` §4.4]) |
| **L, gardien de légende** | Le clan conserve une tradition ; ses **anciens** (Archivistes, Conseil, Cercle) connaissent le lien du cycle avec le phœnix ; ses **jeunes** l'ignorent | **Savoir** est un **énorme avantage**, **ignorer** est une faute **seulement après le premier contact avec un ancien** (§5.4) |
| **A, autre** | Le clan a un honneur propre mais n'attribue pas de mission (honneur personnel) ou monétise | Faute d'honneur propre à lister (table) ; pas de mission obligatoire |

### 5.3 Table clan par clan (clans réellement impliqués)

Noms et devises : StoryForge (Livre V). Les rôles « gardien de légende », les délais et les formes de sanction sont des propositions **[P]** ; ce qui n'est pas dans les livres est marqué **[INV]**. Aucun nom de clan n'est inventé.

| Clan / structure | Type | Qui | Ce qu'il exige | Ce qui le fâche (faute d'honneur) | Avantage lié au phœnix | Délai et forme de la sanction | Levée |
|---|---|---|---|---|---|---|---|
| **Lames Franches** (clan 2). « Nul ne nous commande. Nul ne nous possède. » [L] | **A** (honneur personnel : aucun maître permanent, Capitaines Fractals élus pour une mission ; « un contrat injuste est nul »), avec dépositaires du rite funéraire **[INV]** | Krunt3 | Qu'on ne **retienne** jamais personne, même mort (« une lame ne doit jamais être liée à vie ») ; que le contrat soit libre | Retenir les morts (Rappelés) ; obéir aveuglément ; briser le Code de la Lame Libre. *Refuser une mission injuste n'est pas une faute.* Les Lames ne punissent pas l'abandon d'un tiers | Les anciens (**Cercle de Fer**, Maîtres de Duel) connaissent le rite et **savent qu'il copie le cycle du phœnix** **[INV]**. **Savoir** permet de plaider « filtre, pas possession » devant le Cercle (DD 20, `06` §5.2) et de requalifier la faute. Un jeune qui ignorait l'origine du rite qu'il a inversé fâche les anciens | **Variable**. Premier signe : semaine 1 (un Capitaine Fractal refuse un contrat). Si la possession des morts est **confirmée** : le Cercle de Fer convoque un « Code Brisé » ; réputation → Hostile ; réseaux de mercenaires fermés ; pas de marque infamante [L Livre V ch. 2 §2] | **Délier** les Rappelés ; faire juger l'affaire par le Cercle de Fer (précédent) |
| **Sceau Pourpre** (clan 1). « Un serment scellé vaut plus qu'une armée. » [L] | **L** (Archivistes de Loi, Hauts Scellaires : **garants de l'Accord des Cycles Normaux** [L Livre V ch. 8]) + **D** ponctuel (Rapport de Témoin, citation par un Juge de Serment) | Cyril, Pascal | Qu'un serment tenu le reste (« l'émotion ne justifie jamais la rupture d'un serment ») ; le Rapport de Témoin | Rompre un serment prêté (public : Exécuteurs Mandatés) ; **refuser le Rapport de Témoin demandé** ; ignorer une citation. Aider un homme que le clan doit juger = **conflit d'obligations** (Livre V ch. 2 §4) | **Savoir** que l'Accord des Cycles Normaux touche le cycle des phœnix **[INV]** donne accès aux Archives de Loi, **DD −2** avec les Archivistes, **Récit exemplaire +8** ; un jeune Sceau qui **ignorait** que l'Accord protège ce cycle déçoit les anciens (Désaveu discret) | **Lent**. Premier signe : lettre d'un Juge de Serment, **semaine 2** (J14). Citation → Désaveu discret → Mise à l'écart → Exclusion formelle (aussi grave qu'une perte de citoyenneté [L]). Remettre le Rapport accélère l'Arbitre du Flux (J30 → J20) ; le refuser = Mise à l'écart. Soupçon de complot entre Cyril et Pascal : DD +2 de réhabilitation tant qu'ils restent ensemble | Faire certifier l'aide comme « serment tenu » ; contester le mandat du Flux en droit ; réhabilitation formelle écrite |
| **Navigateurs Gris** (clan 10). « Là où la route meurt, nous avançons encore. » [L] | **D** (missions de Passeur : « La Route Impossible », un prix non monétaire, ramener une information) + **L** (Cercle des Boussoles Éteintes, « mémoire vivante » [L]) | Taranis | Que celui qui connaît la route ne laisse **personne sur une route qu'il a ouverte** ; ramener l'information demandée ; « celui qui connaît la route commande » | Abandonner le groupe en terre des Navigateurs ; refuser un rôle de Passeur ; garder une carte pour soi | Le Cercle garde la mémoire de la **cinquième expédition vers le Nord** (retour par conviction collective) **[INV]** pour les Navigateurs ; **savoir** que le phœnix migre vers le Nord et que la route Nord est celle de l'entité fait de Taranis un Passeur reconnu (**Honneur +1**, accès aux « routes alternatives rares ») ; l'ignorer, quand un ancien du Cercle l'interroge, est une faute | **Rapide, discrète, en terre du clan**. Boussole voilée = « disparu » 7 jours (J7), puis **désaveu** (J14) : cartes « vives » volontairement fausses, caches vidées, Vigies muettes ; Boussole éteinte (exclusion du réseau) après plusieurs semaines. Perte du bonus d'exploration et de survie | Rapporter l'information demandée ; faire acte de Passeur pour d'autres ; **La Route Impossible** devient la carte du chemin vers le Nord |
| **Frères de l'Épreuve** (ordre des Îles des Serments, Atlas région 6 ; fiche à ajouter à StoryForge) | **D** (Gardien d'île : épreuves, défis ; « refus de défi = −1 Honneur » [L Livre II, Atlas]) | Krunt3 (ordre) | Qu'on prouve sa valeur ; qu'on accepte le défi lancé et enregistré à la Salle des Défis | **Refuser un défi** ; fuir une épreuve. Un Gardien peut lancer un défi à Krunt3 pour qu'il prouve sa valeur **sans** la technique | Aucun lien établi par les livres. Piste **[INV]** : le Gardien d'île sait pourquoi la troisième espèce de rang III n'est pas chassée (l'Atlas dit que les Frères « refusent d'expliquer pourquoi ») | **Immédiate pour le défi** : −1 Honneur (publique, tablette jamais effacée) ; **Désaveu discret** puis Mise à l'écart si le refus se répète | Relever le défi ; faire juger par le Gardien (« juge en dernier ressort ») |
| **Guilde Martiale** (guilde 2). « La guerre est un métier. La victoire, une clause. » [L] | **D** (contrats ; **Code de Clause** : pas de changement de camp sans dissolution formelle) | Krunt3, Pascal | Honorer le contrat de garnison ouvert pour eux ; neutralité envers les tiers non contractants | **Déserter** un contrat ; changer de camp sans dissolution ; refuser le contrat attribué ; « mourir inutilement est une faute professionnelle » | Aucun (« l'héroïsme non payé est une erreur comptable »). Un phœnix n'est qu'un objet de contrat | **Fixe : 7 jours** (J7) de délai de grâce, puis **mise à prix interne** (Exécuteurs de Clause : exécution, bannissement ou mise à prix [L]). C'est l'unique échéance à date fixe | Dissolution formelle du contrat ; clause juridique (« La Clause Impossible » : une semaine) |
| **Guilde de Chasse** (guilde 5) | **D** (Conseil des Primes, contrats, clause de **rapport d'anomalie** [L hook du Contrat Empoisonné]) | Taranis | Honorer le contrat en cours (la lettre de contrat est dans son bagage) ; rapporter toute « anomalie » dans la zone | Abandonner un contrat ; **taire une anomalie** (le cratère) | Elle ne sait rien du mécanisme [L Atlas ch. 14]. **Savoir** donne un **levier** (le Contrat Phœnix anonyme, « la Guilde n'a pas officiellement refusé de l'émettre » [L]) ; Taranis peut aussi se voir offrir un silence acheté (`silence_acheté`, Honneur −1 si accepté) | **1 à 2 semaines** : primes retirées, certification suspendue, contrats refusés. En Marches, c'est la guilde locale : immédiate | Rapporter l'anomalie, ou rendre le contrat |
| **Marchands Libres** (guilde 1). « L'or n'a pas de patrie. » [L] | **A** (ne punit pas : **monétise**) | Cyril | Rembourser | Ne pas rembourser le Compte ouvert (« un ruiné inspire l'exemple ») | Aucun | **2 à 3 semaines** : le retour est financé par un prêt qui empire ; Poids-Noirs si la dette est ignorée | Rembourser ; acheter un Gage (monétiser la dette) |
| **Sentinelles du Pacte** (ordre [INV], fiche `03` §3.4) | **D** procédural (Veilles, « nommer le Passant ») | Pascal | Nommer l'arrivant et ce qu'il porte ; ne pas abandonner une Veille | **Abandonner une Veille** : Honneur −3 (fiche `03`, Livre I §9) ; laisser traverser sans nommer. Krunt est un « seuil ambulant » : un Guetteur doit le **nommer** | Aucun lien établi. Les Sans-Relève connaissent les seuils non inscrits au Registre | **Procédurale** : Veille Longue, puis rappel formel (semaines) | Prendre une Veille ; nommer Krunt devant témoin |
| **Pierres Hautes** (clan 9, dominant des Hautes Terres ; **pas** le clan de Pascal) | **L** (« la pierre est une mémoire » ; Conseil des Roches Anciennes, Gardiens de Crête) | PNJ du monde de Pascal (région d'adoption) | Lenteur, serment tenu « par les arrière-petits-enfants » | Un natif des Hautes Terres qui **ignore** la légende | Les Hautes Terres considèrent tuer un phœnix comme « un acte héroïque absurde : ils comprennent rapidement que c'était stupide » [L Atlas ch. 14 §3] : ils **connaissent la légende**. **Savoir** : réputation +, refuges fortifiés | **Lent** (« le Conseil ne se presse pas ») ; fermeture de refuges | Se faire instruire par un ancien (voir §5.4) |

**Hors table** (pas des clans du groupe, mais ils réagissent à la Braise et à la mort d'un phœnix [L Atlas ch. 14 §3]) : Veilleurs Sylvestres et Forêts Totémiques (crime contre la nature), Théocraties (sacrilège), Cités Libres (profit légitime). **Ordre du Flux** : pas un clan à rejoindre ; il ne sanctionne pas l'abandon, il réclame une **dette** (§3).

### 5.4 Règle de la Légende du Cycle (l'avantage phœnix)

La connaissance « le cycle du phœnix a un lien avec ce qui arrive » est une **Marque positive de connaissance**, `legende_cycle`, par personnage et par clan de type L :

| État | Comment on l'obtient | Effet |
|---|---|---|
| **Ignorée** (départ des jeunes) | par défaut | Aucune faute **tant qu'aucun ancien n'a posé la question** |
| **Entrevue** | E1 ou E2 (la Corruption baisse ; la chaleur de phœnix) | Peut être présentée à un ancien comme une intuition (jet de Persuasion ou de Connaissance, **visible**) |
| **Sue** | enseignée par un ancien (quête « Veillée d'instruction »), ou découverte E3 | Avantage plein |

- **Avant le premier contact avec un ancien** : on ne peut que gagner. Si le joueur **va au-devant** et dit la légende le premier : **Récit exemplaire +8** chez le clan (`mecaniques/04` §4.4), Honneur +1 une fois, DD social −2 avec les anciens, accès à une archive du clan.
- **Premier contact avec un ancien** : l'**Appel du Clan** (J14 en général, ou l'arrivée d'un émissaire). L'ancien pose la question. Si `legende_cycle` est **Ignorée** : **faute d'honneur du clan** (réputation −6 chez les anciens, **Désaveu discret** dans leur cercle), **droit de rattrapage** : une quête de **Veillée d'instruction** (l'ancien raconte), qui la lève sans autre coût. Si le joueur **refuse** l'instruction : Honneur −1 et Marque `legende_ignoree`.
- **Pas de punition arbitraire** : tout passe par une réputation de faction, l'Honneur, une Marque. La faute n'existe que **si** l'ancien est en scène (pas de jet sans condition remplie).
- **Variante par clan** : Lames Franches (rite), Sceau Pourpre (Accord), Navigateurs Gris (Cercle), Pierres Hautes (Conseil). Les trois autres types n'ont pas de légende.

### 5.5 Deux logiques de sanction, nommées séparément

| Logique | Déclencheur | Clans |
|---|---|---|
| **(a) Abandon** (décision de krunt : le clan sanctionne ceux qui **abandonnent Krunt**) | Départ du groupe, serment d'aide rompu, compagnon laissé | Navigateurs Gris (abandonner le groupe), Sceau Pourpre (serment rompu), Sentinelles (Veille abandonnée) ; Loup : l'Honneur du Loup chute « s'il abandonne un allié » [L Livre VI] |
| **(b) Absence** (pression du clan qui rappelle) | Appel du Clan sans réponse, contrat non honoré | Guilde Martiale (désertion), Guilde de Chasse (contrat), Frères (défi), Marchands (compte) |
| **(c) Ignorance de la légende** | Premier contact ancien sans `legende_cycle` | Clans de type L (§5.4) |

**Horloge.** *Clans à échéance fixe* (Guilde Martiale : J7) : date fixe, **pas de hasard**. *Autres* : un **jet visible hebdomadaire** pour savoir si le clan agit (DD 18, −1 par semaine d'absence, −2 par Appel du Clan sans réponse) **[?]**. Le Gardien du Nord, lui, **ne sanctionne pas** : il laisse partir.

---

## 6. Les trois autres joueurs en PNJ dans le solo de chacun

Décision de krunt : « chaque joueur aura son personnage, et pas un autre ». Les trois autres personnages apparaissent dans le monde de chaque joueur en **personnages non joueurs**. Cette règle **remplace** « Ne pas créer de copies PNJ » de `mecaniques/06` §2, corrigé en conséquence.

### 6.1 Ce que cela veut dire

- **Contrôle** : le joueur ne contrôle que **son** personnage. Les trois autres sont conduits par le jeu (scripts + règles de comportement) ; ils ne sont **pas** pilotés par les autres joueurs réels (pas de réseau temps réel).
- **Identité commune** : nom, clan, devise, École, Posture, métier, fiche v2 de départ, « fil » (ce qui les fait tenir : le serment de Cyril, la Blessure de Pascal, la dette de Taranis).
- **Krunt3** est PNJ dans les trois mondes des autres joueurs (comme à la table, où le MJ joue ses PNJ) : brasero visible au-dessus de lui.

### 6.2 Arrivée

Le Filet prend ~10 personnes et en dépose 4 au cratère **à la table** (J0). **En solo**, le joueur arrive seul (ou avec Krunt3 PNJ, en transe jusqu'à J2) et les trois autres sont **dispersés** (06 §4.5 : « campés à une ou deux journées ») : ils arrivent **entre J3 et J10**, selon un calendrier de base modulé par le monde (±2 jours, tiré de la graine du monde, jet visible si besoin) :

| PNJ | Arrivée de base | Pourquoi |
|---|---|---|
| **Taranis** | **J3** | Connaît la route, cherche les traces ; il trouve le camp le premier |
| **Pascal** | **J5** | Alerté par la lumière du cratère ; arrive avec ses fioles |
| **Cyril** | **J8** | Arrive le plus tard (soin des blessés sur la route) ; le Serment le retient |

Quand le joueur **est** l'un des trois, son personnage arrive à J0 ; les deux autres suivent le calendrier ci-dessus. Les « repartis » (conviction dès J1) et les « morts » (cairns) sont des PNJ génériques originaux **[INV]**.

### 6.3 Ce qu'ils savent

- À l'arrivée : **leur lentille au palier E0 / 0**, rien de plus. Ils ne connaissent pas le Rappel.
- Ils ne savent que ce que **le journal de CE monde** a enregistré (ce qu'ils ont vu, entendu, reçu). Un indice trouvé par le joueur n'est connu d'eux qu'**après** un partage (confiance, dette).
- Ils portent leur lentille : un PNJ Cyril peut obtenir E1 ; un PNJ Pascal le palier 3 ; un PNJ Taranis le palier 1 (§3.4, règle solo / table). Obtenir leur aide a un **prix** (confiance, faveur, temps), jamais un jet caché.

### 6.4 Comment ils diffèrent d'un monde à l'autre

Selon les **marques** du monde : Loyauté, Compassion, Cruauté, Abandon, Dettes ; selon la **Braise** (un PNJ a peur d'un Krunt en Flamme) ; selon l'**honneur de son clan** (§5) : un PNJ Taranis peut partir au J14 (conviction + désaveu des Navigateurs) dans un monde où il est maltraité, rester dans un autre. Trois états : **compagnon**, **allié réticent**, **parti**. Le **comportement** est donc : aide à la libération de la Braise (stabiliser, doser, lieu isolé, §4.3) si la confiance est suffisante ; refus ou départ sinon. Les **horloges de clan** de chaque PNJ courent dans chaque monde.

### 6.5 Ce qui reste commun et mémoire du monde

- **Commun** : l'identité, la fiche de départ, le fil, les faits fondateurs (J0, le Filet, le Flux), le calendrier macro (J7, J14, J30, J60), les antagonistes, les couches de vérité.
- **Propre à chaque monde** : les indices obtenus, l'attitude, les Dettes entre PNJ et joueur, la fin.
- **Mémoire du monde** : chaque PNJ est une cible de marques (portée « personnage », `mecaniques/06` §3.2) ; ses réactions viennent du journal. Un geste cruel du joueur se sait : le PNJ Cyril s'en souvient.
- **La table recoupe** : les recoupements E2, E4, E5 (Pascal x Cyril, Taranis x Cyril…) sont ceux des **vrais joueurs** à la séance de JDR ; leurs PNJ n'y substituent pas. Aucun recoupement automatique entre mondes.
- **Coût de production** : les trois PNJ utilisent la fiche v2 simplifiée, 2 à 3 animations et des dialogues courts ; pas de recrues A et B avant l'alpha.

---

## 7. Chronologie canonique J0 à J60

**J0 = la nuit du Rappel.** `T-` = avant J0.

| Quand | Événement | Source |
|---|---|---|
| ~150 ans | Purge des Sept Lignées ; la huitième famille échappe au Flux | [L Livre V ch. 8] |
| T-12 ans | Cinquième expédition vers le Nord, retour par conviction collective | [L Atlas ch. 12] |
| T-11 mois | Un jeune phœnix est tué en Absorption aux Ravins de Keth ; le Gardien se branche sur l'Écho | [INV] |
| T-4 mois | Le Voile dénonce la lignée au Flux | [P] |
| T-6 semaines | Les boussoles des Navigateurs dérivent vers les Ravins | [P] |
| T-3 semaines | Un convoi de vingt personnes « disparaît » (il s'est caché) | [L Atlas] |
| T-40 j | Début de l'Audit de la Saison Rouge | [L Atlas] |
| **T-18 j** | Visite d'audit à la ferme : « aucune irrégularité » (neuf jours avant le Bris) | [P] |
| **T-9 nuits** | **Bris de Stagnation** par le Flux ; Krunt3 absent (mission signée du Gardien d'île) | [P] |
| **T-9 à T0** | **La Veillée** : les Neuf Nuits (Krunt veille, achète à Dureth cendres et Codex). *Avant* J0 uniquement | [P] |
| **J0 (nuit)** | **Le Rappel** ; Krunt3 devient réceptacle ; le Filet prend ~10 personnes | [P] |
| J1 (Aube) | Premier Loyer (+2 braises) ; Krunt3 reprend connaissance (joué en solo) ; survie : eau, abri, feu | [P] |
| J2 | Première manifestation visible de Krunt3 ; premier partage de provisions | [P] |
| **J3 à J10** | **Arrivée des trois autres en PNJ** (Taranis J3, Pascal J5, Cyril J8 ; ±2 j) ; à la table, ils sont au cratère dès J0 | §6 |
| J3-J4 | Première libération contrôlée ; première chasse (chef de meute + éclaireurs) | [P] |
| J4-J5 | Poste 7 (Ourse de Fer) ; piste du convoi | [L Atlas] |
| **J7** | Fin du délai de la **Guilde Martiale** (échéance fixe) ; Boussole voilée des Navigateurs ; premier jet d'horloge pour les clans sans échéance | §5 |
| J9 | Les Rappelés stagnent (sans réemployer « Neuf Nuits ») | [P] |
| J10 | Arrivée de la recrue B (Langue du Pacte), hors démo | [P] |
| **J14** | Vague de conviction (E4) ; premier départ libre ; **premier Appel du Clan** : contact avec les anciens (**Légende du Cycle**, §5.4) ; désaveu des Navigateurs ; lettre du Sceau | §4, §5 |
| ~J21 | Premier Embrasement probable si la Braise n'est pas libérée | [P] |
| J20 ou J30 | **Arbitre du Flux** : J20 si le Rapport de Témoin est remis, sinon J30 | [P] |
| J30 à J60 | Poursuite par les Théocraties (rumeur, inquisiteur) | [P] |
| **J60** | Mandat de Bris contre les Rappelés si aucune restitution ; appel d'offres de la Route du Nord | [L Atlas] |

---

## 8. La démo : Krunt seul

Cadre : **une zone** (Marches Frontalières : cratère des Ravins de Keth, un camp, la piste vers le Poste 7), **une chasse** (premier boss), **trois quêtes de plateforme**. Un seul héros animé en entier : **Krunt3** (Danse Rouge, deux lames courtes). Jours **J1 à J4**, solo. Les trois autres n'apparaissent pas ; l'arrivée est annoncée par un **teaser**. Braise **affichée** seulement (pas de libération jouable). Dés visibles dans les moments de réaction (créatures, dressage). Pas de mort définitive.

| # | Jour | Étape | Mode | Contenu |
|---|---|---|---|---|
| 1 | Prologue | **La perte et le Rappel** | Images fixes (3 à 5 min) | La ferme, les siens, la Veillée, le Rappel, le Filet. Le dernier plan : le cratère |
| 2 | J1 Aube | **Réveil au cratère** | Exploration | Krunt3 reprend connaissance, brasero et cadran de 24 h **affichés** (Braise à Braise après le Loyer +2), chaleur, la Tension se récupère mieux près de lui (E0). Tutoriel : eau, abri |
| 3 | J1 | **Quête de plateforme 1 : eau et herbes** | Plateforme (récolte) | Descendre dans le ravin ; Corruption du cratère (VOL DD 13, jet visible) ; rapporter eau et herbes. La survie est la première boucle |
| 4 | J1 nuit | **Première nuit : la voix** | Dialogue | La voix de braises, noms des morts (en réalité en grande partie la sienne). Le lieu de repos fixe le Loyer de J2 : dormir au cratère (+3 braises) ou au bord du ravin (+2) ; la Braise reste affichée, sans jeu |
| 5 | J2 | **Quête de plateforme 2 : le camp** | Plateforme (récolte et abri) | Rassembler bois, pierre, peaux ; **Camp provisoire** (Ancrage 0). Premier geste du joueur qui dépose une marque (6 gestes de `mecaniques/06` §3.3) |
| 6 | J2-J3 | **Traque** | Traque 3/4 | Suivre les traces de la meute (carnet de pistage, jetons de connaissance) ; première réaction du monde : les créatures reculent à la Flamme (cran de Crainte, **dé visible**) |
| 7 | J3 | **Première libération (cinématique)** | Cinématique | La Braise baisse ; une libération contrôlée racontée (pas de jeu ; en alpha, jet VOL DD 13 visible). Les trois aides (stabiliser, doser, trouver un lieu isolé) sont **évoquées**, non jouées : ce sont celles des autres personnages, encore absents |
| 8 | J3 soir | **Quête de plateforme 3 : le cairn** | Plateforme (exploration) | Un tombé mort (cairn) : provisions, insigne de clan, lettre. Choix de **prendre ou non** (Profanateur du Cairn, marque `respect` ou `sacrilège`) |
| 9 | J4 | **Première chasse : le Maître des Trotteurs** | Chasse (2 à 4 min) | Dorgane (chef de meute, CR 4) et 4 éclaireurs Alizade [roster : cro02, cro01] ; deux phases, brisure, deux lames. Krunt3 **seul** (K propre au personnage, caché au joueur). Le Souffle du Réceptacle peut être activé : la Braise monte **visiblement** de +3 |
| 10 | J4 | **L'Alizade blessé : un choix** | Dialogue + dé visible | Achever ou laisser fuir ou soigner : marques Cruauté / Clémence / Compassion (espèce et famille) ; l'Alizade peut devenir **familier-démo** (dressage à 3 phases simplifiées) |
| 11 | J4 soir | **Retour au camp : le Récit** | Dialogue | Clan de démonstration (voir Q27) : Consignation pré-remplie (6 leçons), 1 Appel du Clan **scripté** (Cercle de Fer : un Capitaine Fractal refuse un contrat, premier signe). **Un seul choix** : partager ou non les provisions avec un tombé blessé |
| 12 | J4 nuit | **Teaser : ils arrivent** | Cinématique (30 s) | Trois signes : un signe de piste des Gris sur une pierre (Taranis), la lumière d'une lanterne de Guetteur (Pascal), un sceau de cire au bord du ravin (Cyril). Le brasero de Krunt3 s'allume un peu plus. Titre. « Ils arrivent. » |

**Plafonds de démo** [P] : PNJ nommés : 4 (le tombé blessé, Dorgane, un Cicatrisé de Rang (clan Porteurs de Cicatrices) **[?]**, la voix de la famille dans le prologue) ; lieux : 3 (cratère, camp, ravin) ; jets de découverte : 3 (E1 « la Corruption baisse », « traces de meute », et la lecture du cairn) ; marques : 6 gestes, 2 espèces (Alizade et canidés), plus `loyauté`, `compassion`, `abandon` ; boss : 1 ; écriture : prologue + 8 à 12 dialogues courts. **Hors démo** : libération jouable, Gage, horloges de clan autres que le premier signe, indices à recoupement, les trois autres personnages, recrues A et B, Poste 7 (seulement mentionné), diplomatie et joute.

**Ce que la démo ne montre pas** : pas de Poste 7 (distance et temps), pas de Dureth, pas de Flux ni de Voile (le premier signe du Flux est dans le journal du prologue : le dossier « en examen »).

---

## 9. Questions ouvertes (dédupliquées, avec ma proposition)

Les contradictions que je ne peux pas trancher sont ici, pas tranchées. Ordre : trame, clans, fiches, règles et jeu.

**A. Trame**

| # | Question | Proposition |
|---|---|---|
| Q1 | Confirmer le nom du rite (**Veillée**) et de la technique (**le Rappel**) ; le retrait de l'ancien nom est acquis | Garder ces deux noms |
| Q2 | Coût du pacte : **Braise seule** ou **Braise + Gage** ? Montrer les crans (pictogrammes) ? | Braise + Gage optionnel ; crans visibles, chiffres cachés ; Gage hors démo |
| Q3 | Les cinq fins et les deux axes (choix envers Krunt ; sort de l'entité) ; adopter la fin 5 « Écho allié » | Oui |
| Q4 | Lecture du Gardien : G1, G2 ou G3 ? | G3 (respecte l'Atlas, garde les fins ouvertes) |
| Q5 | Talents : choisis, hasard ou « deux appelés, un tombé » ? Taranis est-il le tombé choisi ? | Mixte ; Taranis choisi par le Gardien |
| Q6 | Entité : confirmer **Écho + Gardien** ; ambiguïté « maudit ou non » gardée jusqu'à E2 | Oui |
| Q7 | Jusqu'où va la vérité sur l'antagoniste (Flux, plus Voile, plus Maison) ; nom de la Maison | Couches 1 et 2 ; couche 3 en fin d'arc ; nom (Arkhen, Vosel) au moment venu |
| Q8 | Les Rappelés : sept, cinq, un seul revenu, ou aucun ? | Famille de cinq ; un seul vraiment revenu |
| Q9 | Le Rappelé « revenu » : mère ou enfant ? | Un enfant (le thème : ce qu'on refuse de perdre) |
| Q10 | Le phœnix tué aux Ravins de Keth alors que le seul contrat de l'Atlas vise les Îles Brûlantes | Second contrat ; juvénile (pas un migrateur) |
| Q11 | Le rite funéraire des Lames Franches est inventé : l'ajouter à StoryForge (Livre V clan 2) ? | Oui, une demi-page sous le nom de la Veillée |
| Q12 | Voies et fins : un joueur peut-il finir sur une fin différente de celle d'un autre dans la même table ? | Oui (« un monde, quatre histoires ») |

**B. Clans et honneur**

| # | Question | Proposition |
|---|---|---|
| Q13 | Lecture de krunt à confirmer : certains clans sont **donneurs d'ordres** (refuser la mission attribuée = faute d'honneur) | Oui, tel que la table du §5.3 |
| Q14 | Quels clans sont **gardiens de la légende du phœnix** (Lames Franches, Sceau Pourpre, Navigateurs Gris, Pierres Hautes) ? Les livres ne le disent pas (sauf Hautes Terres : « acte héroïque absurde ») | Ces quatre ; à valider clan par clan |
| Q15 | La faute d'ignorance n'existe qu'**après** le premier contact avec un ancien ; droit de rattrapage (quête de Veillée d'instruction) | Oui |
| Q16 | Horloges : échéance fixe pour la Guilde Martiale ; jet visible hebdomadaire DD 18 (−1/semaine) pour les autres | Oui |
| Q17 | Ordre de Pascal : **Sentinelles du Pacte** (à créer, [INV]) ou Culte des Ancêtres Veilleurs (canonique, sans fiche) ? *Non tranché par krunt* | Sentinelles du Pacte, avec point de correspondance vers Culte des Ancêtres Veilleurs / Gardiens de Crête |

**C. Fiches**

| # | Question | Proposition |
|---|---|---|
| Q18 | Régions : Îles des Serments, Déserts Rouges, Cœur Impérial, Hautes Terres ; bonus des Déserts Rouges : « réduction de fatigue » (Livre IX) ou « endurance réduite » (Livre II) ? | Les quatre régions ; retenir le Livre IX, noter l'écart |
| Q19 | `region-elem` : supprimer ou garder comme affinité facultative hors canon ? | Affinité facultative |
| Q20 | Danse Rouge pour Krunt3 (« Deux Lames » ; Ours + Danse Rouge = tension créative [L Livre VI]) ; sprite : peau hâlée rougie, barbe gardée | Oui |
| Q21 | Krunt3 : tank ou fer de lance ? | Fer de lance (la simulation rejouée confirme) |
| Q22 | Mana de départ : Livre VI (6/6/8/6) ou Livre I (2) ? | Livre VI |
| Q23 | Bagage de Taranis : contenu de `08` ; boussole éteinte liée à l'entité ? | Contenu de `08` ; boussole sans lien avec l'entité pour la démo |
| Q24 | Pascal : *Flanc Coordonné* conservé ? Kit offensif ou K_perso = 10 ? | Conservé ; K_perso 10-14, pas de kit |
| Q25 | Soin de Cyril à 4 Mana ? Éclats de départ (30/120/90/60) et Honneur (4/4/5/6) ? | Oui aux deux |
| Q26 | **Rang V** d'École : niveau 16 (`04` §5.3) ou niveau 20 (Livre X) ? | Hors campagne (le tableau s'arrête au rang IV) ; ou abaisser le seuil |

**D. Règles et jeu**

| # | Question | Proposition |
|---|---|---|
| Q27 | **Clan de démonstration** : Lames Franches (le clan de Krunt3) ou Porteurs de Cicatrices (`mecaniques/05` §6 : la Consignation = le journal, sans ancrage régional) ? | Lames Franches comme clan du héros ; un Cicatrisé PNJ prête la Consignation (aucun nom de clan inventé) |
| Q28 | Combien de joueurs réels ? Que faire des recrues A et B ? | Quatre joueurs ; recrues PNJ, hors démo ; la Langue du Pacte avant la Gardienne |
| Q29 | Arrivée des trois PNJ en solo : J3, J5, J8 (±2 j) ? Les PNJ répliquent-ils les choix des vrais joueurs via le journal ? | Calendrier de base oui ; **pas de réplique automatique** : seul le MJ importe un choix à la table |
| Q30 | Modèle C (deux barres), régénération d'Endurance 2/s, 3 Jetons de Connaissance ; durée du boss 2 à 4 min ; K propre à chaque personnage (20/18/16/10, caché) ; mode « sans hasard » et relances | Oui à tout ; relances par Jetons de Connaissance |

**Constats de cohérence non tranchés (à lister pour mémoire).** `mecaniques/01` donne K = 20, facteur 0,65 et un tempo de 2,5 s ; `07` §8 donne K_perso et kd par-dessus : à aligner (M6 de la revalidation). Liste unique des marques avec colonne « démo / alpha / plus tard » : à écrire (M3). Nuit des Sept Brasiers : datée de deux façons dans le Livre V (4e âge ou fin du 2e âge) : écart de livre, non tranché. « Karma » : mot absent du Livre I, à ne pas afficher.
