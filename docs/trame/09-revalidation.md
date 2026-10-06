# 09 : Revalidation critique de la trame et des personnages

> **Mise à jour (2026-10-06, après la passe v3).** Document d'historique. Décisions de krunt postérieures (journal `00`) : les noms proposés pour le rite et la technique sont **rejetés** (« le rite », « la technique oubliée », [nom à définir]) ; **Braise seule**, aucun autre coût ; les trois autres joueurs arrivent **tous au cataclysme par un portail magique** (plus de calendrier étalé) ; clans : honneur propre à chacun, attributions « gardien de légende » retirées ; niveau 1 pour tous, sauf le tombé. En cas de doute, `10` prévaut.

Rédigé le 2026-10-06 par un relecteur indépendant. Périmètre relu en entier : `docs/trame/00` à `08`, `docs/mecaniques/00-vue-densemble.md` et `06-monde-vivant-memoire-et-des.md`, plus des sondages dans `docs/mecaniques/01` et `05` quand un renvoi l'exigeait. Les livres (copie de travail dans le dossier de session `livres/`) ont été interrogés par `grep -n` ; les numéros de ligne cités sont ceux de ces copies de travail (Livre I = `Livre1_ReglesCompletes.md`, etc.). Aucun autre fichier n'a été modifié.

**Légende.** **EN VIGUEUR** = valeur recommandée pour toute la trame. **CORRIGER** = document à modifier. **[L]** = fait vérifié dans un livre. **[P]** = proposition des agents. **[INV]** = invention. Les numéros « §n » renvoient aux sections des documents cités.

## Suivi de la passe v3 (2026-10-06)

La passe v3 a appliqué les corrections « haute » (§5.1) et produit le document canonique `10-trame-v3.md`. État :

| # | Correction | État | Où |
|---|---|---|---|
| H1 | Bandeaux d'obsolescence | **fait** (01 à 08, plus `mecaniques/06`) | en tête de chaque document |
| H2 | Ordre de Krunt3 = Frères de l'Épreuve, Juge-mentor = Gardien d'île | **fait** | 01, 02, 04, 05 ; `10` §3.2 |
| H3 | Pacte : Prix des Noms supprimé, Braise, marques, rite renommé | **fait** | 05 (§0, §2, §3, §6), 06, 08 ; `10` §4 |
| H4 | Fiches de 04 : Taranis (métier, région, attributs, Résonance), Pascal (ordre, cuir, bombe), Éclats | **fait** (§9 marqué obsolète et valeurs corrigées) | 04 |
| H5 | Pascal au Sceau Pourpre ; Honneur alignés | **fait** | 03 |
| H6 | Table de sanction « abandon / absence » | **fait** : une ligne par clan, avec le nouvel honneur propre à chaque clan | `10` §5 ; pointeurs dans 02, 05, 06 |
| H7 | Règle des trois autres en solo, voie solo / voie table | **fait** : ils apparaissent en PNJ (décision de krunt, plus « PNJ tombés originaux ») | `10` §3.4 et §6 ; `mecaniques/06` corrigé |
| H8 | 07 rejoué avec les fiches 08 | **fait** pour Taranis et Pascal (script mis à jour, §12 de 07). **Non appliqué** : K_perso et soin à 4 Mana sur 08 (questions `10` Q25 et Q30) | 07, `outils/simu_combat.py` |
| H9 | Affirmations fausses sur les livres | **fait** (guillemets Marches, arbitre à Aurath, convoi, contrat de phœnix annotés) | 02, 03, 05, 06 ; `10` §3.5 |
| H10 | Chronologie canonique | **fait** (visite d'audit à T-18 jours : le doublon T-9 jours de 05 est corrigé) | `10` §7 ; 05 §6, 06 §5.5 |

Moyennes et basses : rang V (M4), Neuf Nuits et feu rituel (M5), « chez lui » de Taranis (M8), verrous de jet (M10), PRE de Pascal et palettes (B1) : **faites**. Renommer « Saturation » (M1), table unique des marques (M3), K / kd de `mecaniques/01` (M6), clan de démonstration (M7) : **proposés dans `10`, non tranchés** (questions).

## 0. Verdict en douze lignes

1. **La trame tient debout** : l'antagoniste (Ordre du Flux, couches de vérité), l'entité en étages (Écho, Gardien, Krunt), le coût en Braise et les fiches v2 sont cohérents entre eux **à condition de lire 06 et 08 comme prioritaires sur 04 et 05**. Rien ne l'écrit encore en tête des documents anciens.
2. **Dette principale : les documents 03, 04 et 05 contiennent des valeurs que 06 et 08 ont remplacées**, sans bandeau d'obsolescence : le prix par l'oubli de noms et l'ancien nom du rite (05), Ordre du Jugement = Flux (05), fiches JSON de 04 §9 (Taranis Espion et aux Marches, Pascal Culte des Ancêtres, Éclats, Défense), Pascal en Pierres Hautes (03 §2.5, §11). Un lecteur qui prend 04 §9 pour les fiches importe des valeurs fausses.
3. **Deux décisions de krunt sont violées** quelque part : *Ordre de Krunt3 = Frères de l'Épreuve* (05 le traite encore comme Ordre du Jugement = Flux) et *retrait de l'ancien coût du pacte et du rite qui portait son nom* (05 en est plein ; 06 renomme le rite, mais le nom de remplacement reste à confirmer).
4. **Une décision est détournée sans que personne ne le signale** : krunt dit que le clan sanctionne **ceux qui abandonnent Krunt** ; 02 §5 et 05 §5 construisent surtout une sanction pour **absence prolongée** (désertion, Appel du Clan sans réponse). Les deux logiques coexistent sans être distinguées (section 1, ligne 29).
5. **Les livres sont bien cités dans l'ensemble** (trente-trois affirmations sondées, environ vingt-cinq exactes, section 3), avec trois erreurs réelles : une citation d'Atlas inexistante (« personne n'y est chez soi »), un arbitre disparu placé aux Marches alors que l'Atlas le place à Aurath, et des Résonances de départ qui contredisent la règle du Livre VI. Plus un écart non signalé : le phœnix tué « aux Ravins de Keth » ne s'accorde pas avec le seul contrat de phœnix de l'Atlas (cible : Îles Brûlantes).
6. **Le point faible n'est pas la cohérence, c'est le périmètre** : la trame ajoute à la démo une jauge à crans, un cadran de 24 h, un mini-jeu de libération, trois échelles de découverte, quatre horloges de clan, deux recrues et quatorze nouvelles marques. Pour un développeur seul sur 75 semaines, **seule une tranche verticale minimale est réaliste** (section 4.4).
7. **Un angle mort de conception** : 05 §4.4 et 06 §2.4 font agir les trois autres personnages **dans** le monde de chaque joueur (stabiliser, doser, trouver un lieu), alors que `mecaniques/06` §2 interdit les copies PNJ et que 06 §1.6 renvoie les recoupements à la table. Il faut dire qui remplit ces rôles dans une partie solo (question 26).
8. **Les simulations de 07 et les fiches de 08 ne se parlent pas** : 07 simule le Taranis de 04 (AGI 12, Vitalité 9, bagage potions/piège/huile) alors que 08 a changé les attributs, la Vitalité et le contenu du bagage. Les conclusions de 07 sur le bagage (« vaut 21 points de victoire ») et sur Taranis premier des dégâts doivent être rejouées.
9. **Les règles de création ont été bien appliquées** (42 points, Vitalité 4+END, PA, limites) ; deux écarts mineurs : une somme à 41 dans 08 §2 (coquille) et un rang V atteint au niveau 16 dans 04 §5.3 alors que le Livre X le place au niveau 20.
10. **Le tank** : 07 conclut proprement que Krunt3 (Double Lame, cuir) ne tient pas la première ligne ; 04 et 05 continuent de lui prêter un rôle de tank (« Le Vase », Provocation). À aligner sur « fer de lance ».
11. **La mémoire du monde et les dés visibles sont compatibles avec la trame**, sauf un point : 05 §1.4 prévoit qu'un jet visible puisse échouer « parce que le monde ne répond pas encore », ce qui casse la promesse de dés honnêtes.
12. **Prochaine étape recommandée** : trancher les 8 questions de tête (section 5.2), puis appliquer en une passe les corrections « haute » (section 5.1) avant d'écrire la moindre scène.

---

## 1. Tableau des contradictions entre les documents 02 à 08

Les valeurs EN VIGUEUR sont choisies pour respecter dans l'ordre : (1) les décisions de krunt (`00-decisions.md`), (2) les livres, (3) le document le plus récent et le plus complet. Quand la valeur n'est pas décidée, la colonne le dit.

| # | Sujet | Ce que disent les documents | EN VIGUEUR (recommandé) | CORRIGER |
|---|---|---|---|---|
| 1 | **Ordre de Krunt3** | 01 §1 et 02 §5 : « Ordre du Jugement ». 03 §3.2 : Frères de l'Épreuve. 04 en-tête : Frères ; **mais** 04 §3.2 (tableau) : « Ordre du Flux (Arbitres) » et 04 §9.1 : `ordre-philo` « Dettes et correction (Arbitres du Flux) » avec `ordre-nom` Frères. 05 §1.2 C1/C2, §1.5 palier 6, §5.5, §7.2 n°10 : Ordre du Jugement = Arbitre du Flux, « Juge-mentor » qui a éloigné Krunt3. 08 : Frères, surnom « Ordre du Jugement » | **Frères de l'Épreuve** ; « Ordre du Jugement » = surnom. Le Juge-mentor devient un **Gardien d'île des Frères** (mandaté ou trompé par le Flux) ; le lien Krunt3-Flux passe par la loyauté ou la dette, pas par l'appartenance | **05** (indices, palier 6, §5.5, §7.2 n°10), **04** §3.2 et §9.1, **02** §5 voie 3, **01** §1 et §4 |
| 2 | **Ordre de Pascal** | 03 §3.4 : Sentinelles du Pacte [INV] ; 04 §3.2 et §9.4 : Culte des Ancêtres Veilleurs ; 05 §5.5 : Gardiens Sylvestres ou Veilleurs du Flux ; 08 §5 : Sentinelles du Pacte, repli Culte des Ancêtres | **Non tranché par krunt** (00 ne le cite pas). Recommandé : Sentinelles du Pacte ajoutées à StoryForge **avec point de correspondance** vers Culte des Ancêtres Veilleurs et Gardiens de Crête | **04** (§3.2, §9.4), **05** §5.5 |
| 3 | **Clan de Pascal** | 03 §2.5, §5.3, §10, §11 et compte rendu n°4 : option A **Pierres Hautes** recommandée. 04, 05, 06, 08 : Sceau Pourpre | **Sceau Pourpre** (décision de krunt), région Hautes Terres, « adoption par serment » (08 §3.1) | **03** (§2.5, §5.3 matrice, §10, §11 ligne `Pascal;clan-nom`, compte rendu) |
| 4 | **Région de Taranis** | 03 §2.3 : Déserts Rouges ; 04 §3.2 et §9.2 : **Marches Frontalières** ; 05 §4.2 : « Steppes du Vent » non résolu ; 08 : Déserts Rouges | **Déserts Rouges** (Atlas région 9 ; Livre V l.382, Atlas l.1341 « steppe rocailleuse… saisons des vents ») | **04** (§3.2, §4.5, JSON §9.2), **05** §4.2 et §7.2 n°7 |
| 5 | **Taranis est-il « chez lui » aux Marches ?** | 02 §4 : « aucun clan ne protège » ; 04 §4.5 : « les Marches sont ses terres » ; 05 §4.2 : chez lui côté clan et guilde, pas côté naissance ; 06 §4.3 : « chez lui dans les Marches » ; 08 : non né aux Marches | Chez lui **côté clan et guilde** (Livre V l.369-395 : Navigateurs Gris et Guilde de Chasse y dominent), **étranger côté naissance**. « Aucun clan ne protège » ne vaut que pour les trois autres | **02** §4, **04** §4.5, **06** §4.3 |
| 6 | **Métier de Taranis** | 01 : Espion/Infiltrateur ; 04 §4.2 et §9.2 : Espion principal + Chasseur-Pisteur secondaire ; 05 §1.5, §3.2 : « pisteur-espion », « archer-espion » ; 08 : Chasseur-Pisteur + Cartographe | **Chasseur-Pisteur (★1) + Cartographe (★1)** (décision) | **04** (§4.2, §7.2, JSON), **05** (palier 1, §3.2 libellés) |
| 7 | **École de Krunt3** | 03/04/08 : Danse Rouge ; 07 §5.3 : propose Gardien Mobile s'il doit tanker ; 05 §2.3 : allume le « Feu des Noms » avec une « école de feu, mode Sacrifice » que Krunt3 n'a pas (08 §6, [V10]) | **Danse Rouge** (non validée par krunt : question 15) ; le rite du rite est un **rite de clan**, pas une Technique d'École | **05** §2.3 (étape 3), §2.4 (« Feu de cendres vives ») |
| 8 | **École de Pascal / rôle de tank** | 04 §3.1 : Gardien Mobile pour Pascal ; 07 §5.3 : Gardien Mobile (épée, bouclier, maille) est le seul kit qui permette de tanker, proposé à Krunt3 | **Gardien Mobile pour Pascal** ; Krunt3 reste Danse Rouge, **fer de lance** | **07** §5.3 (la suggestion n'est plus à retenir), **04** §4.5 |
| 9 | **Rôle de tank de Krunt3** | 04 §4.5 : « Provocation, Vitalité 13 », « fer de lance maudit » ; 05 §3.2 : « Le Vase : celui qui porte et tient (Ours) » ; 07 §5 : « non avec Double Lame et cuir » (99 % de combats avec Krunt3 à terre) | **Fer de lance** : Provocation ponctuelle seulement, aucune combinaison Provocation + Mur de Chair + Interposition | **04** §4.5 et §6.4 n°1 (renvoyer à 07), **05** §3.2 (le « Vase » est une métaphore de trame, pas un rôle de combat : le préciser) |
| 10 | **Mana de départ** | Livre I : 2 ; Livre VI l.1508 : 6-8 ; Livre X l.1493 : 8. 03 §9.2 : « 2 ou 6, à trancher » ; 04 §4.1 et 08 §2 : 6/6/8/6 par formule [INV] ; mécaniques/00 : Livre VI | **6 / 6 / 8 / 6** (Livre VI), à confirmer par krunt (question 17) | **03** §9.2 (marquer « tranché provisoirement ») |
| 11 | **Attributs et Vitalité de Taranis** | 04 §4.1 et 07 §1.2 : 5/12/5/9/6/5, Vitalité 9 ; 08 §3.2 : 5/11/6/9/6/5, Vitalité 10 | **08** (5/11/6/9/6/5 ; Vit 10 ; Déf 19) | **04** §4.1, **07** §1.2 et tous les tableaux (rejouer) |
| 12 | **Pascal : somme d'attributs** | 08 §2 : « 42 (7/6/8/9/5/6) » = **41** ; 08 §3.2 : 7/6/8/9/5/**7** = 42 (+1 VOL) ; 04 §4.1 : 42 | 7/6/8/9/5/7 = 42 (PRE 7) | **08** §2 (coquille) |
| 13 | **Armure et Défense de Pascal** | 04 §4.1, 07 §1.2 : maille +3 et bouclier +2, Défense 19 ; 08 §3.6/§8 : cuir +2 et bouclier +2, Défense **18** (la maille exige un forgeron de niveau 8-15, Livre VIII l.1037 : niveaux 1-5 = tenue fonctionnelle) | **Défense 18** (cuir + bouclier) | **07** (kit de Pascal), **04** §4.1 et JSON §9.4 |
| 14 | **Éclats de départ** | 04 §4.2 : 100 / 80 / 150 / 250 ; 08 §3.6 : **30 / 120 / 90 / 60** [INV, aucune règle des livres] | 08 (plus cohérent avec Livre VIII ch. 9 §5) ; à simplifier si krunt veut | **04** §4.2 et JSON |
| 15 | **Honneur de départ** | 03 §9.2 : Cyril 6, Taranis 5 ; 04 §4.1 et 08 §3.2 : Krunt3 4, Taranis **4**, Cyril **5**, Pascal 6 | 4 / 4 / 5 / 6 (08) ; tous dans la fourchette 4-6 du Livre I l.1444 | **03** §9.2 et §10 (Cyril 7→6, Taranis 5) |
| 16 | **Bagage de Taranis** | 07 §1.2 : 4 potions de soin + piège à colle + huile de feu ; 08 §4 : carquois, instruments, 7 jours de rations, 2 Herbes Stabilisantes, Carnet des Routes, boussole éteinte ; **ni potions, ni piège, ni huile** | **08** (conforme au Livre VIII ; avantage Préparateur Obsessionnel) ; **7 doit rejouer la simulation** avec ce bagage | **07** §1.2, §6.1, §6.2, §8 |
| 17 | **Résonances de départ** | 04 §4.2 : Taranis « Faucon : Point Faible » ; Pascal « Ours : Interposition au jalon d'Acte II ». 08 §8 n°3 retire celle de Taranis. **Livre VI l.575-596** : une Résonance n'existe que **par changement de Posture** | **Aucune Résonance à la création** ni pour Pascal (Loup, jamais Ours) | **04** §4.2, §7.2, JSON §9.2/§9.4 (`resonance-prevue-jalon-acte-2`) |
| 18 | **Bombes de Pascal** | 04 §6.4 n°4 : Bombe de Feu de départ, bombes « à partir du niveau 5 » (Livre X) ; 08 §5.3 : niveau 4 (Livre VII l.709 « Bombes légères ») ; 07 §6.3 : trois variantes dont « bombe » niveau 5 | **Niveau 4**, aucune bombe de départ (décision de krunt) ; K_perso de Pascal = 10 à 14 | **04** §6.4 n°4 et §4.5, **07** §6.3 (retirer la variante « bombe de départ ») |
| 19 | **Pascal : Flanc Coordonné** | 08 §5.3 [V9] : gardé (lecture souple) ; décision de krunt : « juste l'attaque de base » | Gardé, **mais à confirmer** : c'est une Technique de Posture (règle de création), pas une bombe | **08** §5.3 (poser la question à krunt, n°19) |
| 20 | **Coefficients K et kd** | `mecaniques/01` l.15, 266, 751 : K = 20 (boss), 4 (meute), facteur 0,65, un seul K ; 07 §8 : K_perso 20/18/16/10, **kd** 0,29 par-dessus 0,65, tempo du chef 1 action/5 s, K élite 10, K légendaire 5 | **07 §8** pour le prototype ; mécaniques/01 à aligner ; K_perso vit dans la donnée des **monstres/jeu**, pas sur la fiche papier | **mecaniques/01**, **08** (`_extras` : ajouter `k-perso`) |
| 21 | **Soin de Cyril** | 04/08 : 1 case de Vitalité pour 2 Mana (implicite) ; 07 §6.4 : à 2 Mana, Cyril ne perd jamais en solo (100 %) | Soin à **4 Mana** ou plafond de gain de Mana du Flux (à tester) | **08** (`_extras`), **04** §6.4 |
| 22 | **Progression : rang d'École V** | 04 §1.3 : rang V « vers niveau 20-22 » (Livre X l.1512 : rang V au niveau **20**) ; 04 §5.3 : Étincelle, Graine, Pacte atteignent le rang V à 100 % avec niveau **15-16** | Ou le rang V est hors campagne, ou le tableau §5.3 s'arrête au rang IV | **04** §5.3 |
| 23 | **Profil Étincelle / PS de Pascal** | 04 §5 : Étincelle × 1,25, 0 PS ; Pascal 4 PS. 08 §4/§8 : Étincelle « tempéré » × 1,15, 1 PS ; Pascal 2 PS | **08** | **04** §5.2, §9.2/§9.4 |
| 24 | **Coût du pacte** | 05 §0 n°5, §2.6 : trois créances (Flux, Loyer de l'Écho, **Prix des Noms**) ; 06 §2 : **Braise** (jauge 8 crans + cadran 24 h) ; Registre = horloge du Flux ; 04 §5.4 : Marques de Pacte (Souffle du Réceptacle = +1 Marque et +1 Tension) ; 08 §3.5 : Dette de Sang « créancier du pacte », contenu laissé vide | **Braise** (06 §2.4) ; Prix des Noms supprimé ; Souffle du Réceptacle = +3 braises ; Marques de Pacte montent à chaque Embrasement (06 §2.4) | **05** (§0, §2.2, §2.5, §2.6, §3.1, §5.2 ligne « comment lever », §6.1, §7.2 n°4), **04** §5.4 |
| 25 | **Nom du rite, de la technique, de la nuit** | 05 (avant la passe v3) : l'ancien nom du rite, l'ancien nom de la technique, nuit = nom de l'ancienne technique (§6.2) ; 06 §0 et §5.3 n°12 : deux noms de remplacement proposés puis **rejetés** ; 00 : coût du pacte rejeté, puis retrait complet « pour l'ensemble » | Le journal 00 rejette désormais le **coût et le rite** (« pour l'ensemble ») ; **Tranché ensuite par krunt** : les deux noms proposés sont rejetés ; rite et technique restent sans nom ([nom à définir]) ; nuit = **J0** (« la nuit du rite ») | **05** (9 occurrences de l'ancien nom, supprimées à la passe v3), **08** §3.5 (cohérent) |
| 26 | **Les Neuf Nuits** | 05 §2.3 étape 2 : neuf nuits de veille **avant** le rite (T-9 à T0) ; 05 §2.6 créance 1 et §6.3 J9 : « Neuf Nuits passées » **après** J0 ; 06 : le rite = veiller neuf nuits les morts | Les Neuf Nuits sont **avant** J0 (le rite). Après J0, la limite est « J9 : les revenus stagnent » sans réemployer le mot | **05** §2.6 et §6.3 |
| 27 | **Premier Loyer / première libération** | 05 §4.4 : premier Loyer de l'Écho **J6** ; 06 §5.5 : premier Loyer **J1 à l'Aube** (+2 braises), première libération contrôlée **J3-J4** | **06 §5.5** (J1 ; libération J3-J4) | **05** §4.4 (J6), tableau de la première semaine |
| 28 | **Transport et arrivée** | 05 §6.2 : « l'Écho transporte Krunt (transe, 3 jours de marche) puis les trois autres » ; 05 §4.4 : J1 déjà sur place ; 06 §5.5 : Filet, une dizaine de personnes prises, **4 arrivent au cratère** ; Poste 7 « à une dizaine de km » et Dureth « à ~3 jours » : [INV] non signalé | Filet instantané ; arrivée J0 (nuit) / J1 (aube) ; distances Poste 7 et Dureth à marquer [P] | **05** §4.3, §4.4, §6.2 |
| 29 | **Logique de la sanction de clan** | **Décision de krunt** (brief, 02 §1) : le clan sanctionne ceux qui **abandonnent Krunt**. 02 §5 : horloge pour « si le héros **ne rentre pas** » ; 05 §5.2-5.3 : Guilde Martiale = absence (désertion, 7 jours), Navigateurs = abandonner le groupe, Sceau = serment rompu, Lames = **ne punissent pas l'abandon** mais la possession des morts ; 06 §1.6 E4 : au J14 « conviction de rentrer », le chemin du retour s'ouvre | Deux mécanismes à nommer : **(a) sanction de l'abandon** (décision), **(b) pression du clan qui rappelle** (absence). Rédiger une table : pour chaque clan, ce qu'il reproche, déclencheur (a ou b), délai | **02** §5, **05** §5.1-5.3, **06** §5.2 |
| 30 | **Hasard ou fixe dans l'horloge de sanction** | 02 §5 : « le moment est aléatoire, jet visible » ; 05 §5.1 : jet hebdomadaire DD 18 −1/semaine ; 05 §5.3 : Guilde Martiale **7 jours fixes** ; 06 §5.2 : Rapport de Témoin fait passer l'Arbitre de J30 à J20 | Jet visible pour les clans, **échéance fixe** pour la Guilde Martiale (contrat). Écrire la règle une fois | **05** §5.1 |
| 31 | **Le mot « Saturation »** | Atlas ch.13 : phase du cycle d'un phœnix ; Livre II l.3962 : seuil de Corruption 19-24 ; 02 §3 et 04 §5.4 : événement de trame (Marque de Pacte 5) ; 06 §2.4 : deux Embrasements en 7 jours = Saturation | Garder « Saturation » pour le seuil de Corruption (Livre II) ; renommer l'événement de trame (proposition : **Embrasement général**) | **02** §3, **04** §5.4, **05** §3.1, **06** §2.4 |
| 32 | **Composition de l'entité** | 02 §3 : E1 / E2 / E3 au choix ; 05 §3 : E1 (+ variante E1b) ; 06 : **E1 + E2 en couches** (Écho organe sans volonté, Gardien volonté, Krunt voix) ; décision : « peut-être les deux » | 06 §1.2 | **05** §3 (renvoi explicite à 06, les points 3.1 et 3.2 sont remplacés) |
| 33 | **Pourquoi ces trois** | 05 §3.2 : les trois sont des « pièces du filtre » (choisis) ; 06 §4.3 : **deux appelés (Cyril, Pascal), un tombé (Taranis)** | 06 §4.3 (recommandation, non décidée : question 4) | **05** §3.2 |
| 34 | **Fins et voies** | 02 §5 : 3 voies (aider, abandonner, livrer) ; 05 §3.3 : 4 voies (délivrer, contenir, exploiter, abandonner) ; 06 §1.7 : 5 fins (+ laisser faire, Écho allié) | Séparer l'axe **choix du joueur envers Krunt** (aider, abandonner, livrer) de l'axe **sort de l'entité** (5 fins de 06) | **02** §5, **05** §3.3 |
| 35 | **Intrigue unique ou une par joueur** | Décision : une **intrigue commune avec différences**. `mecaniques/06` §1.1 : « il n'y a pas forcément une seule intrigue : chaque joueur développe la sienne » et §6 « un monde, quatre histoires » ; 02 §5 : « chaque joueur vit son histoire dans son monde » | Intrigue **commune** (mêmes faits fondateurs, mêmes antagonistes), **différences** : lentille d'indices, clan, métier, marques, fin | **mecaniques/06** §1.1, §6 ; **mecaniques/00** « un héros ou quatre » |
| 36 | **Copies PNJ des trois autres** | `mecaniques/06` §2 : « Ne pas créer de copies PNJ ». 05 §4.4 (J1-J7) et 06 §2.4 (aides à la Braise) : Taranis, Cyril, Pascal agissent dans le monde de chaque joueur | À trancher (question 26). Recommandation : des **PNJ « tombés » originaux** tiennent les trois rôles (traceur, soigneur, dosage) ; les vrais personnages se recoupent à la table | **05** §4.4, **06** §2.4 et §4.5, **mecaniques/06** §2 |
| 37 | **Marches : ordre actif** | 03 §3.4 : Sentinelles du Pacte occupent la case « — » des Marches ; 05 §4.2 dernier point : « l'Ordre du Jugement/Sentinelles n'y a pas de siège » | Cohérent avec 03 si l'ordre est adopté (sinon « — ») | **05** §4.2 |
| 38 | **Spécialités de guilde** | 03 §4 et 08 : Guerre contractuelle / Capitaineries de défense / Crédit, dette et voies commerciales ; 04 §9.1-9.4 : spécialités du VTT (« Administration de la guerre », « Commerce, contrats, économie ») | **03/08** | **04** JSON |
| 39 | **Arbitre disparu** | Atlas l.676 : un arbitre senior **du Sceau de l'Équilibre** a disparu à Aurath (Cœur Impérial) ; 05 §5.2 : déclencheur du Sceau Pourpre = « arbitre disparu **dans les Marches** » ; 05 §7.1 n°5 : « attribué au Sceau Pourpre dans le Livre V » (introuvable) | Le Sceau de l'Équilibre (Atlas) et le Sceau Pourpre (Livre V) restent deux entités ; l'arbitre disparu est à Aurath | **05** §5.2, §7.1 n°5 |
| 40 | **Démo : héros jouable et clan** | `mecaniques/00` point 10 et `05` §6 : clan de démonstration **Porteurs de Cicatrices**, un seul héros ; 02 §7 : arrivée, premier choix, première chasse ; aucun document ne dit **quel** des quatre est jouable | À trancher (question 27) ; le clan de démonstration doit être celui du héros jouable (Navigateurs Gris pour Taranis) ou le héros doit être celui du clan de démo | **mecaniques/00**, **mecaniques/05** §6, **02** §7 |
| 41 | **Liste des marques** | 05 §2.6 : `rite_interdit`, `necro_animation`, `dette_du_flux`, `nom_perdu`, `fil_de_sang`, `phoenix_tue`, `loyaute`, `compassion`, `abandon` ; 06 §5.3 n°9 : retire `nom_perdu`, ajoute 8 ; `mecaniques/06` §3.3 : 6 gestes pour la démo | Une table unique, avec une colonne « démo / alpha / plus tard » | **05** §2.6, **06** §5.3 |
| 42 | **Éléments (`region-elem`)** | 03 §6 : à supprimer ou requalifier en « affinité » ; 04 §3.2 : « conservées dans region-elem (Wu Xing) » ; 08 §3.1 : « Affinité d'origine, hors livres » (Vent, Métal, Terre) | **Affinité facultative**, non canonique ; Krunt3 vide | **04** §3.2 (énoncé inexact) |
| 43 | **Palettes** | 08 §0 : « 26 à 30 couleurs » ; §9.6 : Taranis 24, Cyril 26, Pascal en-tête 26 mais calcul **23** | Chiffres recalculés | **08** §0 et §9.6 |

---

## 2. Vérification des décisions de krunt (`00-decisions.md` et brief)

Statuts : **R** respectée partout ; **P** partielle (appliquée dans les documents récents, pas dans les anciens) ; **V** violée ; **O** ouverte (krunt n'a pas encore tranché ce que les agents proposent).

| # | Décision | Statut | Où elle est respectée / violée |
|---|---|---|---|
| D1 | Krunt est le héros, maudit, réceptacle d'une entité | **P** | 02, 05, 06, 08 le posent. 06 §1.3-1.4 affirme que « la malédiction n'existe pas comme telle » : cohérent avec D17 (« peut-être ne le maudit pas ») mais à garder comme **hypothèse que la table découvre**, pas comme vérité d'auteur |
| D2 | D'autres personnes du continent transportées vers Krunt (les trois joueurs, éventuellement recrues) | **R** | 05 §3.2, 06 §4 (Filet, tombés, recrues) |
| D3 | Ils peuvent aider (karma positif) ou abandonner ; **le clan sanctionne s'ils partent** | **P** | Voir ligne 29 : la sanction est surtout construite pour l'absence (02 §5, 05 §5). Ligne 29 du tableau |
| D4 | Survie difficile, terres hostiles | **R** | 02 §5, 05 §4.4 (eau, rations, J1-J7), 06 §2.4 (la Braise dépend du lieu de repos) |
| D5 | Découverte de liens et d'amitiés entre les trois, même entre clans rivaux | **R** | 03 §5.3, 05 §5.4, 06 §4.4. Les recoupements E2-E4 imposent de se parler |
| D6 | Antagoniste = ordre ou pays crédible, pas découvrable trop vite → **Ordre du Flux validé** | **R** (choix) / **P** (cohérence) | 05 est cohérent en interne (8 paliers, freins §1.4). **Violation de D9** à l'intérieur (voir ligne 1) : le « Juge-mentor » et l'Ordre du Jugement = Flux |
| D7 | Technique oubliée = A + B + C | **R** | 05 §2 (cycle des phœnix, Nécrotechnie/Mage Noir niv. 23-30, rite des Lames). Le rite C est **inventé** (le Livre V ne dit rien : 05 §7.1 n°1 le dit) |
| D8 | « Tourne mal » = pacte à payer, coût d'utilisation | **R** | 06 §2 (Braise : chaque usage monte la jauge ; Loyer quotidien) |
| D9 | Ordre de Krunt3 = **Frères de l'Épreuve** ; « Ordre du Jugement » surnom | **V** | 05 (C1/C2, palier 6, §5.5, §7.2 n°10), 04 §3.2 tableau et §9.1 `ordre-philo`, 02 §5, 01. Respectée par 03, 04 (en-tête), 08 |
| D10 | Pascal reste Sceau Pourpre (comme Cyril) | **V** (03) | 03 §2.5, §5.3, §10, §11, compte rendu recommandent Pierres Hautes. 04, 05, 06, 08 respectent |
| D11 | Sprite de Krunt3 à refaire (pas de hache à deux mains) | **R** | 08 §9.2 (deux lames courtes). Reste ouvert : peau rouge ou hâlée, barbe [V11] |
| D12 | Taranis = Chasseur-Pisteur + Cartographe (plus Espion) | **V** (04, 05) | 04 §4.2, §7.2, JSON §9.2 (Espion principal) ; 05 §1.5 et §3.2 (libellés « pisteur-espion », « archer-espion »). Respectée par 03 (rang 1), 06, 08 |
| D13 | Régions de l'Atlas, **sans surnoms** | **P** | 08 respecte. 03 §12 n°4 garde les noms du VTT comme « noms vernaculaires » (c'est un surnom) ; 04 §3.2/§9.2 met Taranis aux Marches ; 05 §4.2 laisse « Steppes du Vent » |
| D14 | Lieu d'arrivée : Marches Frontalières | **R** | 02 §4, 05 §4 (Ravins de Keth), 06 |
| D15 | Ancien coût du pacte (oubli de noms) rejeté, puis retrait complet du rite qui portait ce nom | **P** puis **R** après la passe v3 | 06 remplace le coût par la Braise ; **05 n'était pas mis à jour** (9 occurrences de l'ancien nom) : fait à la passe v3. 06 renommait le rite : nom **rejeté** par krunt, rite sans nom |
| D16 | Krunt3 = krunt, jouable ; PNJ pendant les phases de JDR ; un autre MJ pourra prendre la suite | **P** | 08 §3.1 le dit. **Rien n'est dit** sur la façon dont Krunt3 est joué en solo par krunt **et** vu comme PNJ dans trois mondes (06 §2.4 mentionne seulement le brasero au-dessus d'un PNJ) |
| D17 | Entité peut-être écho de phœnix **et** Gardien ; peut-être **ne maudit pas** Krunt | **R** | 06 §1 (quatre étages), 08 §3.5 (Réceptacle rédigé neutre) |
| D18 | Talents des trois : choisis ou hasard ? à développer | **O** | 06 §4 propose « deux appelés, un tombé » ; krunt n'a pas tranché |
| D19 | Taranis part avec un bagage de départ | **P** | 08 §4 le fait ; **07 simule un autre bagage** (ligne 16) |
| D20 | Pascal : juste l'attaque de base avant ses bombes | **P** | 08 §5.3 OK ; 04 §6.4 n°4 propose encore une bombe de départ ; 07 §6.3 la teste ; Flanc Coordonné gardé (ligne 19) |
| D21 | Essais d'équilibrage / tank | **R** | 07 répond : pas de tank avec Double Lame ; K_perso ; modèle C. À répercuter (lignes 9, 11, 20) |
| D22 | Structure solo : une intrigue commune avec différences (statistiques, métier…) | **P** | 06 §1.6 (lentilles) l'applique. `mecaniques/06` §1.1 et §6 la contredisent (ligne 35) |
| D23 | Les fiches sont des essais : ne pas les suivre à la lettre | **R** | 04 et 08 recalculent depuis les règles ; 08 remplace 04 §9 |
| D24 | Noms de StoryForge (= livres) font foi ; ordres inconnus : proposer les plus proches, ajouter si besoin avec points de correspondance | **P** | 03 §3 propose pour chaque ordre inconnu une liste de proches, puis **crée** Sentinelles du Pacte [INV] : permis par la décision, mais le « point de correspondance » (équivalent canonique de repli) n'est donné qu'en 08 §5 (Culte des Ancêtres). Invention d'une fiche de 13 lignes : à valider avant StoryForge |
| D25 | Contexte : un monde par joueur, mémoire du monde, dés visibles, démo aux Marches | **P** | Voir section 4 |

**Bilan** : 2 violations nettes (D9, D12) et 2 partielles lourdes (D10 dans 03, D15 dans 05), toutes **dues à des documents qui n'ont pas été relus après les décisions**. Aucune décision n'est contredite par 06 ou 08.

---

## 3. Vérification contre les livres

Échantillon de 30 affirmations présentées comme venant des livres, vérifiées par `grep -n` dans les copies de travail. **Exact** = le livre dit bien cela ; **Faux** = le livre dit autre chose ou rien ; **Extrapolation** = le livre dit quelque chose de proche, le document en tire plus.

| # | Affirmation (document) | Verdict | Lieu dans les livres |
|---|---|---|---|
| 1 | Tableau région/clan/guilde/ordre (03 §2.1, 05 §4.2, 08 §3.1) | **Exact** | Livre V l.369-395 (tableau §5) ; Marches : Navigateurs Gris / Guilde de Chasse / « — » ; Îles : « — » / Guilde Martiale / Frères de l'Épreuve |
| 2 | Devises des trois clans (03 §5.1) et des Pierres Hautes | **Exact** (point final près) | Livre V l.419 (Sceau Pourpre), l.487 (Lames Franches), l.965 (Navigateurs Gris), l.906 (Pierres Hautes) |
| 3 | « Huitième famille » non résolue de la Purge des Sept Lignées (05 §1.1) | **Exact** | Livre V l.1991-2002 ; Accord des Cycles Normaux certifié par le Sceau Pourpre : même passage |
| 4 | Rituels du Flux : Rite de Restitution, Bris de Stagnation, Droit de Correction des Arbitres (05 §1.1) | **Exact** | Livre V l.1625-1627 |
| 5 | Nécrotechnie interdite universellement par l'Ordre du Flux (05 §1.1, 03 §3.2) | **Exact** | Livre VI l.1254 |
| 6 | Mage Noir niv. 23 « Lecture spectrale », 24 « Fusion intentionnelle », 25 « Scellement runique noir », **30 « Déverrouillage Nécromancie »** (05 §2.1) | **Exact** ; « Nécromancie » n'apparaît dans le Livre VII **qu'à ce niveau 30** | Livre VII l.2751-2792 |
| 7 | Ours + Danse Rouge = « tension créative : ancrage contre vitesse » (08 §6, 04 §1.2) | **Exact** | Livre VI l.1490-1500 |
| 8 | Danse Rouge : Double Lame, Flux, tabou « Perdre le contrôle de soi », *Fuite Tranchante* rang I, *Transe Écarlate* rang V (« tu ne peux pas te défendre ») (08 §6) | **Exact** | Livre VI l.704-715 |
| 9 | Techniques de Loup et d'Ours, Honneur du Loup (« chute s'il abandonne un allié ») (04 §1.2, §7.1) | **Exact** | Livre VI l.337-400 |
| 10 | Une Résonance ne s'acquiert que **par changement de Posture** ; gratuite, une fois par session (04 §1.2, §4.2) | **Exact** dans la règle, **violé par 04** qui donne des Résonances à Taranis et à Pascal | Livre VI l.575-596 |
| 11 | Création : 42 points, 3 à 12, Vitalité 4+END, Endurance 10, Honneur 4-6, Mana 2 × rang | **Exact** | Livre I l.1399-1457 ; Mana 6-8 : Livre VI l.1508 ; Mana 8 au niveau 1 : Livre X l.1493 |
| 12 | Wu Xing : Tigre Blanc = Métal/Ouest, Phœnix = Terre/Centre « DISPARU » (03 §6) | **Exact** | Livre I l.1292-1296 |
| 13 | Tension et Forge **collectives** ; « ni karma, ni jauge cachée » (03 §9, 02 §5) | **Exact** | Livre I l.530-534 et l.342, l.721 |
| 14 | Corruption : pacte avec entité non reconnue +3, rituel interdit +2 à +4, Nécro-animation +5 ; seuils Marque 8-12, Emprise 13-18, Saturation 19-24, Transgression 25+ ; Onguent de Purge −2 (05 §2.6) | **Exact** | Livre II l.3799-3805, l.3904-3991, l.4122 |
| 15 | Techniques liées au phœnix (*Absorption de Corruption*, *Cycle Accéléré* rayon 5 m, *Signature Éthérique*) (05 §3.1) | **Exact** | Livre VI l.1405-1409 |
| 16 | Phœnix en Absorption : −1 Corruption/jour dans 5 km ; Tension : +1 dé de récupération à moins de 100 m ; effet « disparaît dès que le phœnix part » (05 §3.1, 06 §1.1) | **Exact** | Atlas l.2762-2766 |
| 17 | « Le phœnix filtre comme un rein » ; juvénile : « quelques hectares » (06 §1.1) | **Exact** | Atlas l.2652, l.2668 |
| 18 | Cinquième expédition, il y a douze ans, conviction collective de rentrer ; hypothèse C, le Gardien qui « utilise les phœnix comme interface » (06 §1.1) | **Exact** | Atlas l.2591, l.2611 |
| 19 | Poste 7, Ourse de Fer (« neutralité absolue, facture tout »), Dureth « Carrefour des Refusés », Ravins de Keth, Route du Nord (« dans deux mois ») (02 §4, 05 §4) | **Exact** | Atlas l.1190-1226 |
| 20 | Îles des Serments : Frères de l'Épreuve, Gardien par île « juge en dernier ressort », Salle des Défis, nuit chez le Fennak des Glaces ; +1 END ; « refus de défi = −1 Honneur » (03 §3.2, 08 §9.2) | **Exact** | Atlas l.1077-1111, l.1097 ; Livre II l.2381 |
| 21 | Lames Franches alliées de la Guilde Martiale et des Navigateurs Gris (03 §5.3, 05 §5.4) | **Extrapolation** : la **fiche** du clan donne « Guildes Martiales, Confréries Vagabondes » ; les Navigateurs Gris n'apparaissent que dans le **Bloc de la Liberté Martiale** | Livre V l.503-505 contre l.1920 et l.1935 (03 §12 n°12 le signale correctement) |
| 22 | Marchands Libres alliés du Sceau Pourpre **et** des Navigateurs Gris ; Guilde Martiale alliée des Marchands Libres, des Lames, du Sceau (03 §4) | **Exact** | Livre V l.1418 et l.1446 |
| 23 | Alliances de l'Ordre du Flux (05 §1.3 : allié du Sceau Pourpre, ennemi du Voile Noir ; 03 §3.2 : « ennemi naturel d'un Lame Franche ») | **Exact pour le Sceau et le Voile** ; **« ennemi naturel des Lames » est une déduction** (le Livre V ne donne **aucune** hostilité Flux/Lames : l'ennemi des Lames Franches de l'ordre n°2 est celui des **Ordres Prophétiques**). Utile et non exploité : le Flux est **allié des Maisons Anciennes**, ce qui appuie la couche 3 de 05 (la Maison manipule le Flux) | Livre V l.1629 (Flux : alliés Sceau Pourpre, Maisons Anciennes ; hostilités Porte-Flammes, Voile Noir) ; l.1655 (Ordres Prophétiques : ennemis Lames Franches, Voile Noir) |
| 24 | Équipement par niveau de statut (« niveaux 1-5 : outils de base, arme simple, tenue fonctionnelle ») ; 6 PA, ≤ 2 Majeurs, ≤ 3 mineurs, gain ≤ +4 ; synergie Forgeron d'Armures / Ingénieur Méthodique ; Mage Blanc / Canal Stable −1 PA ; Canal Stable exige « Karma ≥ +3 » (08 §3.5-3.6) | **Exact** | Livre VIII l.108-150, l.279-283, l.1037 |
| 25 | Alchimiste : bombes légères au niveau 4, alchimiques au niveau 8 (08 §5.3) ; Mage Blanc : 1 soins mineurs DD 8, 4 régénération, 6 soins graves, 8 soins de groupe, 12 purification des malédictions (04 §1.3) | **Exact** | Livre VII l.709-713 ; l.2608+ (tableau Mage Blanc) |
| 26 | Marches : « **personne n'y est chez soi** » (02 §4, 03 §5.3 cité comme Atlas) | **Faux comme citation** : l'Atlas dit « n'appartiennent à personne complètement… chaque acteur présent a une raison de ne pas vouloir de témoin » (05 §4.1 cite correctement cette seconde phrase) | Atlas l.1151 |
| 27 | Convoi disparu des Ravins de Keth = source des cendres d'un phœnix tué (05 §1.2 C6, 06 E3) | **Faux / non étayé** : le hook de l'Atlas dit que le convoi s'est **caché volontairement** et que quelqu'un à Dureth a été payé pour signaler la « disparition » ; aucun phœnix | Atlas l.1208, l.1218-1220 |
| 28 | Contrat Phœnix anonyme : Guilde de Chasse « n'a pas officiellement refusé » (05 §1.1) | **Exact**, mais le contrat de l'Atlas vise « une créature de rang IV, **région est, première Île des Brûlantes** » : le phœnix tué aux Ravins de Keth (nord) n'est **pas** celui-ci | Livre V l.1522 ; Atlas l.2844-2846 |
| 29 | « La quantité de Corruption portée est visible pour quelqu'un qui sait quoi mesurer » (05 §3.1, appliqué à Krunt) | **Extrapolation** : la phrase de l'Atlas concerne un **phœnix à sa mort**, pas un hôte humain | Atlas l.2672 |
| 30 | Arbitre senior disparu = Sceau Pourpre aux Marches (05 §5.2, §7.1 n°5) | **Faux** : arbitre du **Sceau de l'Équilibre**, à Aurath, Cœur Impérial. Le Livre V ne le mentionne pas | Atlas l.676 |
| 31 | Date de la Nuit des Sept Brasiers (05 §7.1 n°4) | **Exact** : le Livre V la place au 4e Âge (l.231) et la fiche des Cendres Liées à la fin des Guerres Sans Nom (l.800) | Livre V l.231 et l.800 |
| 32 | « Ancien Faucon » avantage unique, Briseurs de Serments (04 §4.4, 05 §5.2) | **Inventions** : absentes du Livre VIII (04 le marque « unique ») et du Livre V (05 ne le marque pas) | Livre VIII l.462-472 (unique = validé par le MJ) ; absent du Livre V |
| 33 | Déserts Rouges, avantage « réduction de fatigue » (03 §2.3) | **Exact selon Livre IX**, **contredit par Livre II** (« Survie extrême ; endurance **réduite** ») : écart entre livres non signalé | Livre IX l.745 contre Livre II l.2384 |

**Erreurs de livres relevées par les agents et confirmées** : renvoi « 30 Métiers dans le Livre 1 » (Livre VI l.145, c'est le Livre VII) ; Karma du Livre VIII sans équivalent dans le Livre I ; deux noms pour la Nécrotechnie/Nécromancie.

**À corriger dans les documents** : n°26 (retirer les guillemets), n°27-28 (annoter l'écart d'Atlas ou déplacer le phœnix), n°30, n°10, n°32, n°29 (marquer [P]).

---

## 4. Cohérence avec le jeu

### 4.1 Les décisions de gameplay face à la trame et aux fiches

| Décision de jeu | Cohérence avec la trame et les fiches | Écart à corriger |
|---|---|---|
| **Dés visibles aux moments de réaction du monde** (`mecaniques/06` §4) | Les jets de découverte (05 §1.5, 06 §1.6), la libération de la Braise (DD 13 visible, 06 §2.4) et les réactions des créatures aux crans de Braise s'y insèrent. **Compatible** | 05 §1.4 n°2 : un 20 naturel peut échouer parce que « le monde ne répond pas encore ». C'est un **verrou masqué par un dé** : à remplacer par **pas de jet tant que la condition n'est pas remplie** (afficher « rien à trouver pour l'instant ») |
| **Mémoire du monde par marques** | La Braise, la dette du Flux, `abandon`, `loyauté` se décrivent en marques. **Compatible** | Le catalogue de marques de la trame est passé de 6 gestes (démo) à ~17 étiquettes à cibles Région/Faction/Monde (ligne 41). `mecaniques/06` §7 recommande « espèce et famille seulement » : la trame y déroge |
| **Un monde par joueur (solo)** | Le journal PocketBase est la jonction (06 §1.6). Les lentilles et les recoupements « à la table » sont compatibles | 05 §4.4 / 06 §2.4 : les trois autres personnages agissent dans le monde (ligne 36). Krunt3 est à la fois **héros** (monde de krunt) et **PNJ** (trois autres mondes) : c'est **quatre vues de la Braise** à produire (HUD joueur, brasero PNJ) |
| **Intrigue commune avec différences** | La trame est commune (même antagoniste, même entité, mêmes échéances). Les différences sont : lentille, clan, métier, fin | **Chaque indice a un talent assigné** (05 §1.5 : palier 1 Taranis, 2 Cyril/Pascal, 3 Pascal, 4 Sceau, 5 Krunt3, 6 Taranis/Krunt3). Un joueur Pascal en solo ne peut atteindre les paliers 1, 5, 6 que par un PNJ. **Règle à poser** : chaque indice a une **voie solo coûteuse** (PNJ, prix, dette) et une **voie table** (recoupement) |
| **Survie** | 05 §4.4 donne une boucle J1-J7 et 06 lie la Braise au lieu de repos. **Compatible**, et c'est le meilleur moteur de la trame | Les provisions ne sont pas comptées dans les fiches (08 : « ce qu'il porte ») sauf le bagage de Taranis : **un seul personnage survit à J10 sans ravitaillement**. Le jeu doit donc rendre la survie gagnable avec « ce qu'on porte » |
| **Modèle de dégâts C (deux barres)** | 07 le recommande (spirale 8 % à 2 End/s) et retient 2 End/s | 04 (Vitalité 13 cases, simulation) est calculé en **modèle A** ; 04 §5.4 (*Souffle du Réceptacle* « Endurance pleine, +d6 pendant 3 rounds ») est un effet de **tour par tour** : à réécrire en temps réel (durée en secondes, coût en braises) |
| **Coefficient K** | 07 : K = 20 chef, 4 éclaireurs, **plus kd** (0,29 pour un chef qui agit toutes les 5 s) | `mecaniques/01` : K = 20, facteur 0,65, un tempo d'attaque toutes les 2,5 s : **9 fois trop dur** selon 07 §7.3. Le **K_perso** (20/18/16/10) fait que le même chef est deux fois plus court pour Pascal que pour Krunt3 : acceptable en solo, mais **à ne pas montrer** (le monstre est le même pour la table) |
| **Pas de mort définitive** | Aucun document n'en parle en contradiction. La Braise a une conséquence de « Vacance » (06 §2.4) | Les « revenus » sont des morts revenus : la mort est le thème, pas la règle de jeu. Pas de conflit |
| **Honneur jamais en chiffres** | La Braise cache aussi ses chiffres (06 §2.4) ; krunt peut montrer les crans | Cyril : « Nom Respecté » exige Honneur ≥ 5 (08 §3.5) : le seuil est par construction un état affiché, pas un chiffre. OK |
| **Tension collective** (Livre I) | 02, 04, 06 y ajoutent +1 par Embrasement ou par Souffle | **En solo, la Tension « collective » n'est portée que par un joueur** : à décider si c'est la jauge du monde de ce joueur (recommandé) |
| **Différences de statistiques entre joueurs** | 04 §5 (profils Roc, Étincelle, Graine, Pacte) les rendent explicites | À simplifier pour la démo : les profils ne jouent qu'au-delà du niveau 5 |

### 4.2 Ce qui est trop ambitieux pour un développeur seul

Temps disponible : **1 050 à 1 800 h** (`mecaniques/00`), dont les outils. Le document `mecaniques/00` refuse de chiffrer un total ; la trame y ajoute, **sans chiffrage**, les chantiers suivants.

| Chantier ajouté par la trame | Pourquoi c'est lourd | Verdict |
|---|---|---|
| **La Braise** (06 §2.4) : jauge à 8 crans, cadran de 24 h, Loyer à l'Aube, libération par jet avec aides (Cyril, Pascal, Taranis), Embrasement, Vacance, seuils de Flamme, effets sur créatures et PNJ | Un système UI + un calendrier de survie + un mini-jeu de jet visible + des états à sauvegarder + 8 marques. **Au moins aussi lourd que le Bastion minimal** | **Alpha**. En démo : afficher le brasero de Krunt3 (PNJ) comme **ambiance**, sans libération jouable |
| **Deux échelles de découverte** (05 §1.5 : 8 paliers ; 06 §1.6 : E0-E7) × 3 lentilles × 4 mondes | ~16 indices, chacun avec jets, contre-lectures, verrous de temps, passerelles de rattrapage. **C'est le mur d'écriture** de `mecaniques/04` (aucun total donné) | **Démo : paliers 0-2 et E0-E2 seulement** (un indice par lentille). Le reste = table |
| **Horloges de clan** (4 clans × 2 vitesses + 3 guildes) | Chaque clan a un premier signe, un délai, une sanction, une levée (05 §5.2-5.3 + 06 §5.2) | **Démo : une seule horloge** (Guilde Martiale J7) ; le reste est écrit mais inactif |
| **Cinq fins × entité + voies** (06 §1.7) | Chaque fin exige des conditions, marques et scènes | **Hors démo** ; garder les 5 comme canevas de MJ |
| **Recrues A et B + dizaine de tombés** (06 §4.5, 04 §8) | Deux personnages, deux fiches, des scènes, des sprites | **Hors démo** ; trois PNJ « tombés » génériques suffisent |
| **Quatre personnages jouables** avec sprites profil + 3/4, variante porteur B et C, quatre palettes (08 §9) | PixelLab et retouches : plusieurs dizaines de générations plus animations (marche, attaque, esquive, soin, tir, lancer) × 4 | **Démo : un seul héros animé en entier**, les trois autres en PNJ à 2-3 animations |
| **K_perso et 13 tests (T1-T13, ≥ 8 testeurs × 3 essais)** (07 §9) | Un protocole de laboratoire pour un projet à un seul développeur | **Démo : T1, T2, T4, T5, T6** sur 4 à 5 testeurs |
| **Survie complète** (eau, rations, abri, météo, chasse) + **trois modes de jeu** (Traque, plateforme, chasse) | Déjà le cœur du jeu | **Garder**, mais comme une boucle réduite : eau + abri + un événement météo |
| **Sanction par jet hebdomadaire** + horloge du Flux + Rapport de Témoin | Systèmes de campagne | **Hors démo** |
| **Nouveaux contenus StoryForge** (Sentinelles du Pacte, Frères de l'Épreuve, rite des Lames, ordres sans fiche, spécialités de guilde, correspondances Wu Xing, 14 modifications d'ordres, 13 changements de VTT en 03 §12-13) | Du travail d'outillage et d'écriture avant tout code de jeu | À répartir : **StoryForge** = noms et correspondances (rapide) ; **VTT** = ses listes déroulantes seulement après la démo |

### 4.3 Budget de contenu raisonnable pour la démo (propositions, à ajuster par krunt)

Cadre : zone des Marches (Ravins de Keth, Poste 7), un héros, un chef de meute + 4 éclaireurs (Dorgane, Alizade), un seul Retour au Clan, une joute, 4 Écoles et 3 Métiers, Bastion minimal (`mecaniques/00` point 10). **Ce que la trame doit livrer au plus**, pour ne pas dépasser :

| Poste | Plafond de démo |
|---|---|
| Personnage jouable | **1** (recommandation : Taranis, voir question 27) |
| PNJ nommés | **4** : Krunt3 (en transe/éveillé), l'Ourse de Fer, un guetteur ou « tombé », un courtier de Dureth |
| Lieux | **3** : cratère d'arrivée, camp / lieu isolé, Poste 7 (Dureth seulement mentionné) |
| Jours de jeu | **J1 à J4** (arrivée, premier Loyer, première chasse, rencontre du Poste 7) |
| Jets de découverte | **3** (E1 « la Corruption baisse », palier 1 « pas de traces de créature », E2 optionnel) |
| Marques déposées | **6 gestes, 2 espèces** (`mecaniques/06` §8 n°5) plus `loyauté`, `compassion`, `abandon` |
| Braise | **affichage seul** ; première libération en cinématique ou en dialogue |
| Choix final | **un seul** : partager ou non les provisions (02 §7) ; pas d'abandon complet |
| Boss | **1** (chef + 4 éclaireurs), durée 2 à 4 min, K = 20 ou K_perso |
| Écriture | prologue (3 à 5 min) + 8 à 12 dialogues courts ; le reste = canevas de table |

### 4.4 Questions de jeu que la trame ne résout pas

1. **Qui joue Krunt3 en solo ?** krunt est son propre héros dans son monde, PNJ dans les trois autres : trois versions de la même scène.
2. **Le chef de meute est « trivial pour la table » (07 §0 n°1)** : si la table utilise K = 2-4 et le jeu K = 20 avec kd, **la même fiche donne deux expériences**. À écrire sur chaque fiche (colonne « table » / colonne « jeu »).
3. **Les fiches 08 portent des « _extras » que le VTT ne lit pas** (compétences, Marques, profil, k-perso). Aucun chemin d'import n'est testé ; 03 §13 prévoit 13 modifications du VTT. À ne pas lancer avant la démo.
4. **Le karma** : 02 §5 le définit comme « marques + Honneur » ; 04 §1.4 n°5 et 08 §3.5 lisent « Karma ≥ +3 » comme « Honneur ≥ 5 ». Cohérent mais fragile : le mot « karma » n'existe pas dans le Livre I (l.342). Ne pas l'afficher au joueur.

---

## 5. Corrections et questions

### 5.1 Liste priorisée des corrections à appliquer

**Priorité haute** (empêchent d'écrire la suite sans erreur)

| # | Correction | Documents | Lignes du tableau |
|---|---|---|---|
| H1 | **Bandeau d'obsolescence** en tête de 03, 04 et 05 : « 06 et 08 remplacent les passages suivants ». Éviter qu'un lecteur importe 04 §9 | 03, 04, 05 | tout |
| H2 | **05** : retirer « Ordre du Jugement = Arbitre du Flux », réécrire le « Juge-mentor » (Gardien d'île des Frères), corriger C1/C2, palier 6, §5.5, §7.2 n°10 | 05 | 1 |
| H3 | **05** : appliquer 06 §5.3 (créance 3 supprimée, créance 2 = Braise, marques, renommage du rite après réponse à la question 1) ; supprimer « Prix des Noms » | 05 | 24, 25 |
| H4 | **04** : tableau §3.2 (Taranis Marches, Pascal Culte, Krunt3 Flux) et JSON §9.1-9.4 marqués obsolètes ; Taranis Chasseur-Pisteur + Cartographe ; supprimer Résonances de départ ; Pascal sans bombe de départ | 04 | 1, 2, 4, 6, 13, 14, 15, 17, 18, 38 |
| H5 | **03** : Pascal Sceau Pourpre (§2.5, §5.3, §10, §11, compte rendu) ; valeurs d'Honneur alignées | 03 | 3, 15 |
| H6 | **Sanction** : écrire la table « abandon vs absence » (une ligne par clan et par guilde) et l'inscrire dans 02 §5, 05 §5, 06 §5.2 | 02, 05, 06 | 29, 30 |
| H7 | **Parties solo** : poser la règle de rôle des trois autres (PNJ « tombés » originaux) et la règle « chaque indice a une voie solo » ; corriger `mecaniques/06` §1.1, §2, §6 | mecaniques/06, 05, 06 | 35, 36 |
| H8 | **07 ↔ 08** : rejouer les simulations avec le Taranis de 08 (AGI 11, END 6, Vit 10, bagage de 08), la Défense 18 de Pascal, et l'absence de Résonance ; reporter K_perso et soin 4 Mana sur 08 ; réécrire le *Souffle du Réceptacle* en temps réel | 07, 08, 04 | 11, 13, 16, 20, 21 |
| H9 | **Livres** : retirer « personne n'y est chez soi » entre guillemets ; corriger « arbitre disparu aux Marches » ; annoter l'écart du phœnix tué (Atlas : contrat vers les Îles Brûlantes) | 02, 03, 05, 06 | 5, 39 |
| H10 | **Chronologie canonique** J0 à J30 (section 6 ci-dessous) à reporter dans 05 §6.3 et 06 §5.5 | 05, 06 | 25, 26, 27, 28 |

**Priorité moyenne**

| # | Correction | Documents |
|---|---|---|
| M1 | Renommer l'événement de trame « Saturation » (proposition : **Embrasement général**) et supprimer le doublon Marques de Pacte / Embrasements dans 04 §5.4 | 02, 04, 05, 06 |
| M2 | Unifier voies et fins (axe du choix, axe du sort de l'entité) | 02 §5, 05 §3.3, 06 §1.7 |
| M3 | Choisir une **table unique des marques** avec colonne « démo / alpha / plus tard » | 05 §2.6, 06 §5.3, mecaniques/06 |
| M4 | 04 §5.3 : rang V atteint au niveau 16 contre Livre X l.1512 (niveau 20) | 04 |
| M5 | Neuf Nuits avant J0 uniquement ; réécrire l'allumage du feu comme rite de clan (08 [V10]) | 05 §2.3, §2.6, §6.3 |
| M6 | Aligner K / kd / tempo de `mecaniques/01` sur 07 §8 (ou renvoyer vers 07) | mecaniques/01 |
| M7 | Démo : désigner le héros jouable et le clan de démonstration (Porteurs de Cicatrices contre clan du héros) | mecaniques/00, mecaniques/05, 02 §7 |
| M8 | « Chez lui » de Taranis : nuance côté clan / naissance | 02 §4, 04 §4.5, 06 §4.3 |
| M9 | Appuyer la couche 3 de 05 sur l'alliance canonique Flux / Maisons Anciennes (Livre V l.1629) ; marquer « ennemi naturel des Lames » (03 §3.2) comme déduction | 05, 03 |
| M10 | Jets de verrou de temps : ne pas proposer le jet (dés honnêtes) | 05 §1.4 |
| M11 | StoryForge : cinq fiches à prévoir (Frères de l'Épreuve, Sentinelles du Pacte ou repli, rite funéraire des Lames, Culte des Ancêtres, Veilleurs du Flux, Porte-Cendres) avec points de correspondance | 03 §12 |
| M12 | Taranis Loup + Souffle Long : combinaison **non listée** au tableau de compatibilité (Souffle Long est listé pour le Faucon, Livre VI l.1496) ; l'écrire comme choix assumé | 08 §3.3 |

**Priorité basse**

| # | Correction | Documents |
|---|---|---|
| B1 | Coquille PRE 6→7 de Pascal ; palettes (23 contre 26) | 08 §2, §9.6 |
| B2 | Marquer [P] « Briseurs de Serments », « Ancien Faucon », distances Poste 7/Dureth | 04, 05 |
| B3 | « Quantité de Corruption visible » : [P] | 05 §3.1 |
| B4 | Écart Livre II / Livre IX sur le bonus des Déserts Rouges | 03 §2.3 |
| B5 | Erreur de renvoi Livre VI → « Livre 1 » : à corriger dans le livre lui-même | Livre VI l.145 |
| B6 | `region-elem` : retirer l'énoncé inexact « conservées dans region-elem » | 04 §3.2 |

### 5.2 Questions restant à trancher par krunt (dédupliquées)

**A. Trame**

| # | Question | Recommandation |
|---|---|---|
| 1 | Le retrait de l'ancien nom porte-t-il sur le **coût** seul ou aussi sur le **nom du rite** ? | **Répondu par krunt** : sur l'ensemble (coût et rite) ; les deux noms de remplacement proposés sont **rejetés** : rite et technique sans nom |
| 2 | Coût du pacte : Braise seule ? Montrer les crans à l'écran ? | **Tranché par krunt : Braise seule.** Crans visibles (pictogrammes), chiffres cachés : à confirmer |
| 3 | Lecture du Gardien : G1 protecteur, G2 geôlier, G3 régulateur ? | **G3** (respecte l'Atlas, garde les fins ouvertes) |
| 4 | Talents : choisis, hasard ou **mixte (« deux appelés, un tombé »)** ? Taranis est-il « le tombé choisi » ? | Mixte, Taranis choisi par le Gardien |
| 5 | Entité : confirmer **Écho (étage 1) + Gardien (étage 2)** ; ambiguïté « maudit ou non » gardée jusqu'au palier E2 ? | Oui |
| 6 | Jusqu'où va la vérité sur l'antagoniste : Flux seul (couche 1), plus Voile Noir (couche 2), plus Maison Ancienne (couche 3) ? Nom de la Maison ? | Couches 1 et 2 ; couche 3 réservée à la fin d'arc ; nom à choisir dans l'Atlas (Arkhen, Vosel) quand on y arrive |
| 7 | Les revenus : sept, un seul revenu, ou aucun ? Taille de la famille ? | Famille réduite (5), **un seul vraiment revenu**, les autres en échos |
| 8 | Le phœnix tué (il y a 11 mois, aux Ravins de Keth) est-il acceptable alors que le seul contrat de phœnix de l'Atlas vise les Îles Brûlantes ? | Oui, en le présentant comme un **second contrat** ; juvénile (pas un migrateur) |
| 9 | Le rite funéraire des Lames Franches est inventé : l'ajouter à StoryForge (Livre V, clan 2) ? | Oui, une demi-page sous le nom retenu à la question 1 |
| 10 | Logique de sanction : l'**abandon** (décision) ou l'**absence** (pression du clan qui rappelle), ou les deux ? | **Les deux**, nommés séparément (ligne 29) |
| 11 | Voies et fins : adopter deux axes (choix envers Krunt ; sort de l'entité) et la fin 5 « Écho allié » ? | Oui |

**B. Fiches**

| # | Question | Recommandation |
|---|---|---|
| 12 | Ordre de Pascal : Sentinelles du Pacte (à créer) ou Culte des Ancêtres Veilleurs ? | Sentinelles du Pacte, avec point de correspondance vers Culte des Ancêtres Veilleurs / Gardiens de Crête |
| 13 | Régions : Îles des Serments, Déserts Rouges, Cœur Impérial, Hautes Terres ? Taranis aux Marches ? | Les quatre ; Taranis en Déserts Rouges |
| 14 | `region-elem` : supprimer ou garder comme « affinité » facultative ? | Garder comme affinité facultative, hors canon |
| 15 | Danse Rouge pour Krunt3 (« Deux Lames ») ; sprite : peau rouge franche ou hâlée ; barbe ? | Danse Rouge ; hâlée rougie ; barbe gardée |
| 16 | Krunt3 : tank ou fer de lance ? | Fer de lance (07). Un vrai tank exigerait Épée et Bouclier et prendrait l'école de Pascal |
| 17 | Mana de départ : Livre VI (6/6/8/6) ou Livre I (2) ? | Livre VI |
| 18 | Bagage de Taranis : contenu de 08 (rations, instruments, carnet) avec ou sans les potions, piège et huile de 07 ? La boussole réagit-elle à l'entité ? | Contenu de 08 + 2 potions (pour la simulation) ; boussole **sans** lien avec l'entité pour la démo |
| 19 | Pascal : *Flanc Coordonné* conservé ? Kit offensif ou K_perso = 10 ? | Conservé ; K_perso 10-14, pas de kit |
| 20 | Soin de Cyril à 4 Mana ? | Oui |
| 21 | Éclats de départ (30/120/90/60) et Honneur (4/4/5/6) ? | Oui |

**C. Règles et jeu**

| # | Question | Recommandation |
|---|---|---|
| 22 | Modèle C, régénération d'Endurance 2/s, 3 Jetons de Connaissance : confirmés ? | Oui |
| 23 | Durée du boss en solo : 2 à 4 min ou 5 à 8 min ? | 2 à 4 min pour la démo |
| 24 | K propre à chaque personnage (20/18/16/10) dans la donnée du jeu ? | Oui, caché au joueur |
| 25 | Mode « sans hasard » et relances (Points de Destin ou Jetons) ? | Mode « sans hasard » oui ; relances par Jetons de Connaissance |
| 26 | Parties solo : les trois autres personnages apparaissent-ils ? | Non : PNJ « tombés » originaux ; les quatre vrais personnages se recoupent à la table |
| 27 | **Démo** : quel héros jouable et quel clan de démonstration ? | **Remplacé : décision de krunt, démo = Krunt seul** (Lames Franches, son propre clan, aucune sanction de clan dans la démo). Ancienne proposition : **Taranis** (Navigateurs Gris, guide des Marches, bagage, arc) ; Krunt3 PNJ ; Krunt3 jouable après la démo |
| 28 | Combien de joueurs réels et que faire des recrues A et B ? | Quatre joueurs ; recrues PNJ, hors démo (Langue du Pacte avant la Gardienne) |

---

## 6. Chronologie canonique proposée (à reporter dans 05 §6.3 et 06 §5.5)

Une seule table, sans la contradiction de la ligne 26. Les jours sont relatifs à **J0 = la nuit du rite**.

| Quand | Événement | Source |
|---|---|---|
| T-11 mois | Un jeune phœnix est tué en Absorption (lieu : Ravins de Keth, [INV]) ; le Gardien se branche sur l'Écho | 05 §6.1, 06 §5.5 |
| T-3 semaines | Un convoi de vingt personnes « disparaît » aux Ravins de Keth ; il s'est caché | Atlas l.1208, l.1218 |
| T-4 mois | Le Voile dénonce la lignée au Flux | 05 §6.1 [P] |
| T-40 j | Début de l'Audit de la Saison Rouge (fausse piste) | Atlas l.663 |
| T-9 j | Visite d'audit à la ferme | 05 [P] |
| T-9 nuits | Bris de Stagnation par le Flux ; Krunt3 absent (mission signée) | 05 [P] |
| **T-9 à T0 (le rite)** | Les **Neuf Nuits** : Krunt veille, achète les cendres et le Codex à Dureth | 05 §2.3 |
| **J0 (nuit)** | **Le rite** ; Krunt3 devient réceptacle ; le Filet prend ~10 personnes, **4 arrivent au cratère** | 05 §6.2, 06 §5.5 |
| J1 (Aube) | Premier Loyer (+2 braises) ; survie : eau, abri, feu | 06 §5.5 |
| J2 | Réveil de Krunt3, première manifestation ; premier partage de provisions | 05 §4.4 |
| J3-J4 | Première libération contrôlée ; premier chef de meute | 06 §5.5 |
| J4-J5 | Poste 7, Ourse de Fer ; piste du convoi | 05 §4.4 |
| J7 | Fin du délai de la Guilde Martiale (échéance fixe) ; premier jet d'horloge de clan | 05 §5.3 |
| J9 | Les revenus « stagnent » (sans réemployer « Neuf Nuits ») | 05 §6.3 |
| J10 | Arrivée de la recrue B (hors démo) | 06 §5.5 |
| J14 | Vague de conviction (E4) : premier départ libre ; premier Appel du Clan ; désaveu des Navigateurs | 06 §1.6, 05 §5.2 |
| ~J21 | Premier Embrasement probable si la Braise n'est pas libérée | 06 §5.5 |
| J20 ou J30 | Arbitre du Flux : J20 si le Rapport de Témoin est remis, sinon J30 | 06 §5.2 |
| J60 | Mandat de Bris contre les revenus si aucune restitution ; appel d'offres de la Route du Nord | 05 §6.3, Atlas l.1206 |

---

## Compte rendu (5 lignes)

1. **Couvert** : 43 lignes de contradictions entre 02 et 08 ; 25 décisions de krunt vérifiées (2 violées, 4 partielles lourdes) ; 33 affirmations de livres sondées avec numéros de ligne ; cohérence jeu et budget de démo ; 28 questions dédupliquées ; chronologie canonique.
2. **Faible** : je n'ai pas relu `mecaniques/01`, `03`, `04` et `05` en entier (sondages sur K et la démo) ; les chiffres de 07 sont des simulations non rejouées sur les fiches 08.
3. **Recommandation 1** : poser un bandeau d'obsolescence sur 03, 04 et 05 et appliquer les corrections « haute » H2 à H5 en une seule passe.
4. **Recommandation 2** : trancher d'abord les questions 1, 10, 26 et 27 (rite, sanction, rôle des autres en solo, héros de la démo), car elles conditionnent tout le reste.
5. **Recommandation 3** : réduire la démo à un héros, J1-J4, trois jets de découverte, la Braise en affichage seul et un seul choix ; le reste est du matériau de table.
