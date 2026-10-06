# Trame 03 : correspondance entre les fiches des quatre personnages, les livres et StoryForge

> **Remplacé en partie par `10-trame-v3.md` (passe v3, 2026-10-06).** Ce document est un brouillon antérieur aux décisions de krunt. Corrections en vigueur, appliquées dans le corps du texte : **Pascal reste au clan Sceau Pourpre** (décision de krunt : l'option A, Pierres Hautes, est abandonnée, l'option B est retenue) ; **Taranis est Chasseur-Pisteur + Cartographe** (et non Espion) ; régions de l'Atlas **sans surnoms** ; Honneur de départ 4 / 4 / 5 / 6 ; Mana de départ provisoirement 6 / 6 / 8 / 6 (Livre VI, `10` Q22). Les fiches à jour sont dans `08-fiches-v2-et-sprites.md` et `10` §2.


Rédigé le 2026-10-06. Règle de krunt : **les noms de StoryForge (= les livres) font foi, l'application du VTT s'adapte.**
Sources lues : fiches du VTT extraites de la base (Krunt3, Taranis, Cyril, Pascal), Livres I, II, IV (Atlas), V, VI, VII, IX, `docs/mecaniques/00 à 06`, `docs/trame/01` et `02`.

**Légende.** **[L]** = ce que disent les livres (avec livre et lieu). **[P]** = proposition de Claude, à valider par krunt. **[INV]** = invention sans appui dans les livres. Une valeur du VTT est dite **OK** (existe telle quelle dans les livres), **À AJUSTER** (existe, mais le libellé, la valeur ou la spécialité diffère), **ABSENTE** (n'existe pas : remplacer ou créer).

---

## 0. Verdict en dix lignes

| Champ de la fiche VTT | Verdict | Détail court |
|---|---|---|
| Régions d'origine (Plaines Franches, Steppes du Vent, Terres du Sceau, Cols Fortifiés) | **4 ABSENTES** | Aucune n'est dans l'Atlas (20 régions). Remplacées par : Îles des Serments, Déserts Rouges, Cœur Impérial, Hautes Terres Claniques (§2). |
| Clans (Lames Franches, Navigateurs Gris, Sceau Pourpre) | **OK** | Les trois existent ; devises exactes (à un point final près). Pascal reste au Sceau Pourpre (décision de krunt). |
| Guildes (Martiale, de Chasse, Marchands Libres) | **OK** | Les trois existent (Livre V ch. 4). Seules les **spécialités** « Administration de la guerre » et « Commerce, contrats, économie » sont à reformuler (§4). |
| Ordres (Ordre du Jugement, Sentinelles du Pacte) | **2 ABSENTS** | Jugement → **Frères de l'Épreuve** (canon). Sentinelles du Pacte → **fiche d'ordre à créer** (§3). |
| Éléments Wu Xing (Vent, Métal, Terre) | **2 OK + 1 à convertir** | Métal et Terre sont des éléments Wu Xing ; **Vent n'est pas Wu Xing** (c'est une affinité de Forge et une École mystique) (§6). |
| Écoles (Deux Lames, Arc Précis, Lame Droite) | **3 ABSENTES** | Noms de StoryForge les plus proches : Danse Rouge, Souffle Long, Flux Tranchant (§7). |
| Postures (Loup, Ours) | **OK** | Deux des quatre Postures naturelles (Livre VI ch. 4). |
| Métiers (Espion / Infiltrateur, Mage Blanc, Alchimiste) | **OK** | Trois des 30 Métiers (Livre VII). Doublon « Espion » à lever (§8). |
| Étoiles, jauges, attributs | **À RAMENER AUX RÈGLES** | 42 points (3 à 12), Vitalité = 4 + END, Endurance 10, Honneur de départ 4 à 6, Tension et Forge **collectives** (§9). |
| Équipement | **Hors livres** | « sabre laser », « adamentium », objet « Légendaire » à la création, système de poids : à remplacer (§9). |

---

## 1. Les quatre fiches telles qu'elles sont dans le VTT

| | Krunt3 | Taranis | Cyril | Pascal |
|---|---|---|---|---|
| Région / élément | Plaines Franches / — | Steppes du Vent / Vent | Terres du Sceau / Métal | Cols Fortifiés / Terre |
| Clan | Lames Franches | Navigateurs Gris | Sceau Pourpre | Sceau Pourpre |
| Guilde (spécialité) | Guilde Martiale (Administration de la guerre) | Guilde de Chasse (Contrats de chasse, formation) | Marchands Libres (Commerce, contrats, économie) | Guilde Martiale (Administration de la guerre) |
| Ordre (philosophie) | Ordre du Jugement (Justice et loi) | — | — | Sentinelles du Pacte (Protection des frontières) |
| École / Posture | Deux Lames / Ours | Arc Précis / Loup | Lame Droite / Loup | Lame Droite / Loup |
| Métier | Espion / Infiltrateur | Espion / Infiltrateur | Mage Blanc | Alchimiste (3 étoiles) |
| Attributs | FOR 5, AGI 5, END 3, ESP 3, VOL 5, PRE 6 (total 27) | 10 partout (défaut) | 10 partout | 10 partout |
| Jauges (vit / end / mana / hon / ten / forge) | 20 / 20 / 20 / 4 / 1 / 0 | 15 / 15 / 10 / 5 / 0 / 0 | 20 / 20 / 20 / 7 / 0 / 0 | 11 / 13 / 9 / 5 / 0 / 0 |

Remarque technique : la base contient **deux familles de clés d'attributs** (`attr-for`… à 10 par défaut, et `attr_for`… pour Krunt3 seulement). L'application lit probablement la première : les attributs saisis de Krunt3 sont donc ignorés (voir §13).

---

## 2. Les régions d'origine (point 1)

### 2.1 Ce que disent les livres
- **[L]** L'Atlas décrit **20 régions** (Livre IV, « Les Régions du Monde », puis Terres Inconnues). Le tableau d20 d'origine est dans le Livre II ch. 4 §4 ; Livre IX ch. 2 en reprend les bonus. **Aucune des quatre régions du VTT n'y figure** : « Plaines Franches », « Steppes du Vent », « Terres du Sceau » et « Cols Fortifiés » sont des noms propres à l'application.
- **[L]** Les éléments ne sont **pas** des attributs de région dans les livres (voir §6) : `region-elem` est une invention du VTT.
- **[L]** Livre V §5 : tableau d'affiliation régionale (indicatif ; un clan d'une autre région est possible mais « implique une rupture culturelle qu'il faut jouer »). Extrait utile :

| Région | Clan dominant | Guilde présente | Ordre actif |
|---|---|---|---|
| Cœur Impérial | Sceau Pourpre | Marchands Libres | Ordre du Flux |
| Hautes Terres Claniques | Pierres Hautes | Guilde Martiale | Culte des Ancêtres |
| Îles des Serments | — | Guilde Martiale | Frères de l'Épreuve |
| Marches Frontalières | Navigateurs Gris | Guilde de Chasse | — |
| Déserts Rouges | — | Guilde de Chasse | Ordre du Sable |
| Archipels Nomades | Navigateurs Gris | Navigateurs | — |

- **[L]** Contrainte de trame (docs/trame/02 §4) : les **terres hostiles d'arrivée sont les Marches Frontalières** (démo). **[P]** Donc **aucun des quatre héros ne devrait avoir les Marches pour origine** : ils y sont des étrangers déplacés par le phénomène (sinon l'un d'eux serait « chez lui » et la prémisse perd de sa force). Les Marches ne sont retenues qu'en candidate de secours.

### 2.2 Krunt3 : « Plaines Franches » (clan Lames Franches, Guilde Martiale, Ordre du Jugement)

Particularité **[L]** : les Lames Franches n'ont « ni territoire fixe, ni capitale » (Livre V clan 2) : aucune région ne peut être « leur » région d'origine. Il faut une région où la **Guilde Martiale** est présente et où l'absence de clan dominant laisse la place.

| Rang | Région candidate | Justification (livres) | Réserves |
|---|---|---|---|
| **1** | **Îles des Serments** (Atlas Région 6 ; Livre II d20 n° 6) | Table V §5 : clan « — » (libre pour les Lames), **Guilde Martiale**, ordre **Frères de l'Épreuve**. Livre VI §5 : école martiale favorable en région 6. Valeur « l'épreuve acceptée », « Refus de défi = −1 Honneur » : colle au duelliste libre. Bonus **+1 END** (seul bonus d'attribut avec Hautes Terres). Région **isolée, accès par mer uniquement** : « la famille détruite » y est discrète et tardive à découvrir. | Froid et insulaire (le sprite « peau rouge » n'y est pas lié). |
| 2 | Hautes Terres Claniques (Atlas Région 4) | Guilde Martiale présente ; Culte des Ancêtres Veilleurs (les morts « votent encore » : écho au rite funéraire de la piste C) ; Vallée des Serments. Bonus +1 VOL. | Clan dominant **Pierres Hautes = ennemi des Lames Franches** (Livre V §2, ligne 9). Et Pascal y est mieux placé (§2.5). |
| 3 | Archipels Nomades (Atlas Région 14) | Livre V clan 2 : alliés des Lames = « Confréries Vagabondes », structure de cette région ; « autorité rejetée ». | Pas de Guilde Martiale dans la table ; Livre IX : tension avec les Îles. |

**Recommandation [P] : Îles des Serments.** Changement de fiche : `region` = « Îles des Serments », `region-elem` = vide (voir §6) ; bonus d'origine +1 END appliqué.

### 2.3 Taranis : « Steppes du Vent » (Navigateurs Gris, Guilde de Chasse, Vent)

| Rang | Région candidate | Justification | Réserves |
|---|---|---|---|
| **1** | **Déserts Rouges** (Atlas Région 9) | Atlas : biome « **steppe rocailleuse** … saisons des **vents** » (littéralement une steppe à vent) ; Guilde de Chasse présente (V §5) ; école « De Chasse » favorable en région 9 (Livre VI §5) ; avantage « survie extrême, réduction de fatigue » [L Livre IX l.745 ; **le Livre II dit « endurance réduite »** : écart entre livres, non tranché, `10` Q18] ; passages de contrebande (Passage Bas de Tyr) : terrain d'un Navigateur Gris et d'un pisteur. | Clan dominant « — » (les Navigateurs Gris, « clan des marges », y sont un étranger plausible). Ordre local : Ordre du Sable (Livre V, Livre II) ou « Ordres du Silence » (Livre IX) : **conflit entre livres**. |
| 2 | Marches Frontalières (Atlas Région 7) | **Correspondance parfaite au tableau V §5** : Navigateurs Gris + Guilde de Chasse + ordre « — ». | Lieu d'arrivée de la trame : Taranis serait chez lui (contraire à la prémisse). À réserver si krunt veut un guide local. |
| 3 | Archipels Nomades (Atlas Région 14) | Navigateurs Gris dominants ; « +1 mobilité, avantage esquive » : bon pour un archer. | Guilde de Chasse absente (guilde « Navigateurs »). Mer : éloigné des steppes. |

**Recommandation [P] : Déserts Rouges.** `region` = « Déserts Rouges ».

### 2.4 Cyril : « Terres du Sceau » (Sceau Pourpre, Marchands Libres, Métal)

| Rang | Région candidate | Justification | Réserves |
|---|---|---|---|
| **1** | **Cœur Impérial** (Atlas Région 1) | **Correspondance parfaite** : clan dominant **Sceau Pourpre**, guilde **Marchands Libres**, ordre du Flux ; « Légitimité légale », avantage « autorités, +1 Réputation ». « Terres du Sceau » est de toute évidence cette région sous un autre nom. | Livre II / IX donnent « Sceau de l'Équilibre » comme structure, Livre V l'Ordre du Flux : **conflit entre livres**. Désobéissance publique = −1 Honneur automatique. |
| 2 | Cités Libres Marchandes (Atlas Région 3) | Marchands Libres présents ; « la parole donnée », avantage négociation. | Clan dominant Mille Voix (pas Sceau) ; Cyril serait en rupture culturelle. |
| 3 | Provinces Nobles (Atlas Région 2) | Marchands Libres présents ; Maisons Anciennes, **alliées du Sceau** (Livre V). | Clan dominant Maisons Anciennes ; moins « serment ». |

**Recommandation [P] : Cœur Impérial.** Aucun conflit d'obligations à jouer (c'est un Sceau chez le Sceau) : bon point d'ancrage pour que ses sanctions de clan soient lourdes (Livre V §2 : exclusion du Sceau « aussi dommageable qu'une perte de citoyenneté »).

### 2.5 Pascal : « Cols Fortifiés » (Sceau Pourpre, Guilde Martiale, Sentinelles du Pacte, Terre)

| Rang | Région candidate | Justification | Réserves |
|---|---|---|---|
| **1** | **Hautes Terres Claniques** (Atlas Région 4) | Atlas : les Hautes Terres s'ouvrent par **trois passes tenues par des clans** ; Atlas Routes §3 : « Col de l'Éperon » ; Cairn de Mûrn au Col de Mûrn. Guilde Martiale présente (V §5). Clan **Pierres Hautes** (« Gardiens de Crête, défenseurs des cols », « Sentinelle des Cols » comme archétype de PJ). Élément Terre (« pierre ») cohérent. | Clan dominant Pierres Hautes : voir option B ci-dessous. Tension régionale Hautes Terres / Cœur Impérial (Livre IX) : mine pour Pascal-Cyril si Pascal reste Sceau. |
| 2 | Cœur Impérial | Si Pascal reste **Sceau Pourpre** : Guilde Martiale alliée du Sceau (Livre V Guilde 2). | « Cols » disparaît ; doublon de région avec Cyril. |
| 3 | Marches Frontalières | Frontière par excellence ; Sentinelles du Pacte y trouvent leur place d'ordre (§3). | Lieu d'arrivée de la trame (§2.1). |

**Cohérence à deux options [P]** (clan, région, guilde, ordre doivent aller ensemble, Livre V §5) :
- **Option A (écartée par krunt, conservée pour mémoire)** : région Hautes Terres Claniques + clan **Pierres Hautes** + Guilde Martiale + ordre **Sentinelles du Pacte** (créé). Cohérent à 100 % avec le profil « Terre, cols, frontières, défense » ; sort Pascal du doublon Sceau Pourpre avec Cyril, ce qui donne au groupe quatre clans différents sur trois ; **ennemis des Lames Franches comme Cyril** (tension partagée).
- **Option B (retenue par krunt)** : garder Sceau Pourpre (« adoption par serment » aux Hautes Terres), région Cœur Impérial ou Hautes Terres (rupture culturelle à jouer, permise par V §5), Guilde Martiale, Sentinelles du Pacte.

---

## 3. Les ordres inconnus (point 2)

### 3.1 Ce que disent les livres
- **[L]** Livre V ch. 5 : **8 ordres** détaillés : Ordre du Flux, Ordres Prophétiques, Ordre du Sable, Archivistes Stellaires, Cultes Syncrétiques, Gardiens Sylvestres, Marées Profondes, Ordre Dogmatique. Ch. 6 : ordres secrets (**Voile Noir**, **Masques de Verre**, et trois factions de l'ombre : Chroniqueurs Oubliés, Fraternité des Sources, Morts de Velhor).
- **[L]** Mais le tableau V §5 et le Livre II citent aussi, **sans fiche**, des ordres : **Frères de l'Épreuve**, Culte des Ancêtres (Veilleurs), Veilleurs du Flux, Porte-Cendres. Ce sont des structures décrites dans l'Atlas (région par région), non dans la liste des 8 ordres : incohérence interne à signaler (§14).
- **[L]** Ni « Ordre du Jugement » ni « Sentinelles du Pacte » n'existent. (« Jugement Scellé » est une École martiale ; « Pacte » apparaît dans « Guerre des Pactes Brisés », Pactes mineurs, etc.)

### 3.2 « Ordre du Jugement » (justice et loi), pour Krunt3

| Rang | Ordre canonique | Ce qui correspond | Ce qui ne correspond pas |
|---|---|---|---|
| **1** | **Frères de l'Épreuve** (Confrérie des Îles des Serments ; Atlas Région 6, Livre II ch. 4, tableau V §5) | « Seuls ceux qui ont prouvé leur valeur peuvent **juger** la valeur des autres » ; chaque île a un **Gardien, « juge en dernier ressort des conflits »** ; la Salle des Défis enregistre et tranche ; ordre « ni religieux ni militaire » ; favorable aux écoles martiales (Livre VI §5) ; **Guilde Martiale** présente. Va avec la région 1 de Krunt3. | « Loi » écrite : ici la justice est celle de l'épreuve, pas du code. Pas de fiche dans Livre V ch. 5. |
| 2 | Ordre du Flux (V ch. 5, ordre 1) | **Arbitres du Flux : juges itinérants avec Droit de Correction** ; punit « ce qui persiste au-delà de son cycle » : c'est **exactement** l'ordre qui punira la résurrection de la famille de Krunt (Livre VI : nécrotechnie « interdite universellement par l'Ordre du Flux »). | Allié du **Sceau Pourpre** ; **« ennemi naturel d'un Lame Franche » est une déduction [P]** : le Livre V ne donne aucune hostilité Flux/Lames (le Flux est aussi allié des Maisons Anciennes) ; morale « non humaine » : pas un ordre qu'on rejoint par choix de duelliste. À utiliser comme **force qui jugera Krunt**, pas comme son ordre. |
| 3 | Ordre Dogmatique (V ch. 5, ordre 8) | « Loi Sacrée », Purificateurs. | Fanatique, hostile aux clans libres ; incompatible avec Lames Franches. |

Structures de justice d'appoint (pas des ordres) : **Juges de Serment** (clan Sceau Pourpre), **Vallée des Serments** (Atlas, Hautes Terres : « il n'y a pas de tribunal, pas de loi écrite », des anciens, du feu).

**Verdict [P] : pas de nouvel ordre pour le « Jugement ».** `ordre-nom` = **Frères de l'Épreuve** ; `ordre-philo` = « Juger par l'épreuve : seuls ceux qui ont prouvé leur valeur jugent les autres » (reprise Atlas). « Ordre du Jugement » peut subsister comme **surnom populaire** dans les dialogues. Et dans la trame 02 (§5, voie 3 « Livrer Krunt à l'Ordre du Jugement ») : remplacer par **Frères de l'Épreuve** (jugement par l'épreuve) ou **Ordre du Flux** (Arbitres, jugement de correction) selon l'effet voulu.
Ironie à exploiter **[P]** : un Lame Franche (« Un contrat injuste est nul ») qui appartient à un ordre de juges : tension de rôle naturelle pour Krunt3, qui devient lui-même l'objet du jugement.

### 3.3 « Sentinelles du Pacte » (protection des frontières), pour Pascal

| Rang | Ordre / structure canonique | Correspondance | Insuffisance |
|---|---|---|---|
| 1 | Gardiens Sylvestres (V ch. 5, ordre 6) | Ordre martial, **défense d'un territoire**, ligne de défense visible (Veilleurs Sylvestres). | Frontière **naturelle** (forêt), pas politique ; morale « harmonie » pas « pacte ». |
| 2 | Frères de l'Épreuve | Ordre martial, favorable aux Martiales, Guilde Martiale. | Ordre insulaire de l'épreuve, aucun rôle de frontière (et déjà pris par Krunt3). |
| 3 | Culte des Ancêtres Veilleurs (Hautes Terres) | Les « Veilleurs » légitiment les serments devant les ancêtres ; passes tenues par les clans. | Religion commune, pas un ordre armé de frontière. |
| (clan, pas ordre) | Pierres Hautes (« Gardiens de Crête ») | Défenseurs des cols : c'est l'**équivalent clanique**. | C'est un clan. |
| (métier, pas ordre) | Sentinelle d'Honneur, Gardien des Accords (Livre VII, bloc 4) | « Garantie morale des pactes ». | Ce sont des **Métiers**. |

**Verdict [P] : aucun ordre canonique ne convient** (la frontière politique sous pacte n'est tenue que par des clans et des métiers). La table V §5 donne **« — » comme ordre actif aux Marches Frontalières** (et aux Failles, Archipels, Terres Sans Nom) : un emplacement existe. **Fiche d'ordre à ajouter à StoryForge** ci-dessous. Elle est **[INV]**, construite avec les briques du Livre V (Guerre des Pactes Brisés du Sceau Pourpre, Gardiens de Crête des Pierres Hautes, Cols de l'Atlas).

### 3.4 Fiche d'ordre à ajouter à StoryForge : Sentinelles du Pacte [INV]

> *« Ce qui est tenu au seuil n'a pas à l'être au cœur. »*

| Champ | Valeur |
|---|---|
| **Statut** | Ordre n° 9 (hors des 8 de Livre V ch. 5) ; fiche synthétique « usage MJ ». À placer en Livre V ch. 5 ou en annexe « Ordres régionaux » (avec Frères de l'Épreuve). |
| **Nature** | Ordre de garde des **Seuils** : passages (cols, gués, défilés), postes et lignes tracés par des **Pactes de frontière** entre régions, clans ou royaumes. Il ne gouverne pas : il **veille** que ce qui franchit le seuil soit nommé et réponde de ce qu'il apporte (armées, créatures, Corruption, objets interdits, personnes sous ban). |
| **Doctrine (les Trois Veilles)** | 1. Nul ne passe sans être nommé. 2. Qui franchit répond de ce qu'il porte. 3. La veille ne s'abandonne pas : on la passe, on ne la quitte pas. |
| **Origine** | Après la **Guerre des Pactes Brisés** (fondatrice du Sceau Pourpre, Livre V), les traités de frontière existaient sur parchemin mais **personne ne les tenait physiquement** : le Sceau n'a pas d'armée. Des **Gardiens de Crête** (Pierres Hautes) sans bastion à tenir et des **Exécuteurs mandatés** du Sceau en disponibilité jurèrent de tenir les seuils sous pacte. L'ordre en est resté hybride : moitié serment juridique, moitié garde de montagne. |
| **Organisation** | **Le Registre des Seuils** (conseil : tient la liste des passages sous pacte ; une frontière qui n'y est pas inscrite n'est pas protégée) · **Les Guetteurs** (postes fixes, cols, gués ; isolés des années) · **Les Porte-Sceaux** (liaison avec le Sceau Pourpre ; délivrent et vérifient les laissez-passer) · **Les Veilleurs de Marche** (patrouilles mobiles dans les zones sans gouvernement, notamment les Marches Frontalières) · **Les Sans-Relève** (vétérans liés par vœu à un poste unique, jamais relevés ; cellule d'élite qui connaît les seuils non inscrits au Registre). |
| **Rituels** | **Nomination du Passant** (nommer à voix haute l'arrivant et ce qu'il porte, devant témoin) · **Scellement de Seuil** (fermeture d'un passage pour une saison ou pour toujours) · **Veille Longue** (une nuit sans relève après la perte d'un poste). |
| **Région** | Ordre actif des **Marches Frontalières** (case « — » du tableau V §5) ; présence secondaire aux **Cols des Hautes Terres Claniques** (Atlas Routes §3) et au **Passage Bas de Tyr** (Déserts Rouges). |
| **Alliés** | Sceau Pourpre (les pactes sont son œuvre) ; Pierres Hautes (Gardiens de Crête) ; Guilde Martiale (contrats de garnison) ; Guilde de Chasse (pression des créatures aux marges). |
| **Tensions** | Navigateurs Gris (« nous tracerons les routes, nous ne déciderons pas de leur usage » contre « nul ne passe sans être nommé » : les Gris ouvrent des passages que les Sentinelles voudraient fermer) ; guildes des Marches qui vivent de la contrebande ; Lames Franches (aucun seuil ne s'impose à une lame sans consentement ; pas d'hostilité structurelle). |
| **Ennemis** | **Voile Noir** (identités fausses, passages secrets : son réseau vit des seuils non inscrits) ; **Masques de Verre** (identités alternatives certifiées, donc faux noms au poste). |
| **Utilisation MJ** | Morale **procédurale** : ils n'ont pas de morale du bien, ils ont des registres. Ils ne mentent pas, ils omettent. Un Guetteur ne laisse pas passer un inconnu même mourant ; il le nomme, l'enregistre, puis le soigne si le Registre le permet. |
| **Avantage mécanique (PJ affilié)** | Passage reconnu aux postes sous pacte ; accès consultable au Registre des Seuils ; Avantage dans les négociations aux avant-postes. **Contrainte** : aider un poste en détresse n'est pas facultatif ; abandonner une Veille = transgression ouverte du code (Honneur −3, Livre I §9). |
| **Écoles / Métiers favorables** | Écoles martiales d'Ancrage (Gardien Mobile, Mur Vivant) ; métiers Sentinelle d'Honneur, Gardien des Accords, Cartographe (les Sentinelles connaissent mieux les seuils que les cartographes officiels). |
| **Conflits canoniques** | **La Fermeture du Col des Muets** (un Scellement de Seuil décidé par le Registre coupa une vallée de ses vivres ; la Guilde Martiale fut mandatée pour la rouvrir, le Sceau Pourpre arbitra, les Sentinelles refusèrent de se déjuger). **Le Poste sans Registre** (un poste tenu depuis cent ans pour un pacte inscrit nulle part ; on ne sait ni qui l'a signé ni ce qu'il retient). |
| **Hooks de quête** | ★ **Le Seuil Sans Nom** : l'endroit où le phénomène a jeté les héros est un **seuil sous pacte que le Registre croyait scellé** ; quelqu'un a traversé sans être nommé, et plusieurs. Les Sentinelles veulent savoir par où. · ★ **La Relève qui ne vient pas** : un poste (par exemple le Guetteur « Veille-Fumée » de la campagne) n'a pas reçu de relève depuis un an ; ce qu'il garde demande une réponse que le Registre refuse de donner. · ★ **Le Laissez-passer Falsifié** : un Porte-Sceau découvre un pacte réécrit ; le Voile Noir a un Porte-Sceau dans son réseau. · ★ **Le Pacte que Personne ne se Rappelle** : les Sans-Relève savent ce que retient une frontière inscrite nulle part ; ils ne le diront qu'à qui accepte de prendre une Veille. |
| **Lien avec la trame du Réceptacle** | Pascal, Sentinelle : pour son ordre, un phénomène qui fait **traverser des inconnus sans passer aucun seuil** est une violation du principe de base. Quant à Krunt, « un pacte à payer » résonne avec le nom de l'ordre (**le pacte** comme vocabulaire commun). Un Guetteur peut être le **premier témoin** et le premier à exiger que Krunt soit « nommé ». |

### 3.5 Fiche d'ordre à compléter : Frères de l'Épreuve (lacune de Livre V) [L + P]

**[L]** (Atlas Région 6, Livre II ch. 4 §4, Livre V §5) : Confrérie qui gouverne les **Îles des Serments** ; « ni religieux ni militaire » ; Gardien par île, juge en dernier ressort ; épreuves d'initiation (nuit en plein air dans le territoire d'un Fennak des Glaces) ; Salle des Défis (tablettes jamais effacées) ; Bastion rang II ; ils exportent des « personnes formées » ; **refus de défi = −1 Honneur** ; Guilde Martiale présente.
**[P]** à ajouter à StoryForge (Livre V n'en donne ni alliés ni ennemis) :

| Champ | Valeur proposée |
|---|---|
| Alliés | Hautes Terres Claniques (alliance de régions, Livre IX) ; Guilde Martiale ; Lames Franches (honneur personnel, contrat accepté). |
| Tensions | Archipels Nomades (tension de régions, Livre IX) ; Sceau Pourpre (le jugement par l'épreuve contredit la loi écrite) ; Ordre Dogmatique (vérité unique contre vérité éprouvée). |
| Ennemis | Aucun déclaré ; le **Défi Sans Réponse** (Atlas) est une scission interne. |
| Hooks | Ceux de l'Atlas (L'Épreuve Impossible, Le Défi des Personnages, La Tablette Manquante) + ★ **Le Défi à Krunt** : un Gardien lance un défi à Krunt3 pour qu'il prouve sa valeur **sans** la technique ; refuser = honte (−1 Honneur). |

---

## 4. Les guildes (point 3)

**[L]** Livre V ch. 4 : **7 guildes** : Marchands Libres, Guilde Martiale, Artisans d'Éther, Navigateurs, Guilde de Chasse, Ports Unifiés, Guilde des Soigneurs. Les trois guildes du VTT existent.

| Guilde du VTT | Existe ? (Livre V) | Spécialité du VTT | Spécialité canonique | Verdict |
|---|---|---|---|---|
| **Guilde Martiale** (Guilde 2) | **Oui**, « La guerre est un métier. La victoire, une clause. » Fondateur Arkhavel le Comptable de Guerre ; Directoire des Lames, **Maîtres de Contrat**, **Capitaineries** (siège, escarmouche, défense urbaine, annihilation ciblée, contre-insurrection), **Officiers-Loges** (discipline, soldes, recrutement), Exécuteurs de Clause. Code de Clause : pas de changement de camp sans dissolution formelle. | « Administration de la guerre » | **Guerre contractuelle** : contrats, clauses, unités mercenaires. | **OK** pour la guilde ; **À AJUSTER** la spécialité. « Administration de la guerre » est proche des **Officiers-Loges** (soldes, discipline, recrutement) : à garder comme sous-spécialité. [P] Krunt3 : « Guerre contractuelle (Officiers-Loges : discipline et soldes) » ; Pascal : « Capitaineries de défense (garde, siège) ». |
| **Guilde de Chasse** (Guilde 5) | **Oui**, « Une créature morte rapporte. Une créature vivante apprend. » Conseil des Primes, Contremaîtres, Certificateurs, **Formateurs de Terrain**, Archivistes de Chasse. | « Contrats de chasse, formation » | Émet les contrats, **forme** les nouveaux membres, certifie les techniques. | **OK** tel quel (correspondance exacte). |
| **Marchands Libres** (Guilde 1) | **Oui**, « L'or n'a pas de patrie. » Comptoir Central, **Syndics de Route**, Banquiers de Dette, Courtiers Gris, Poids-Noirs. | « Commerce, contrats, économie » | **Crédit, dette, approvisionnement stratégique, voies commerciales.** | **OK** pour la guilde ; spécialité **À AJUSTER** (« Crédit, dette et voies commerciales ») : le mot « contrats » est le terrain de la Guilde Martiale. |

Remarque [L] : le Livre V dit que la Guilde Martiale est **alliée des Lames Franches ET du Sceau Pourpre** (Guilde 2, « Alliances ») et que les **Marchands Libres sont alliés du Sceau Pourpre ET des Navigateurs Gris** (Guilde 1). Ces deux guildes sont les **ponts** de §5.3.
Remarque [L] : Livre V Guilde 2 : « impossibilité de changer de camp sans dissolution formelle » (Code de Clause), alors que Lames Franches : « un contrat injuste est nul ». Krunt3 porte cette contradiction dans sa fiche (clan Lames + Guilde Martiale) : c'est un défaut de rôle **voulu**, à jouer.

---

## 5. Clans, devises et relations entre clans (point 7)

### 5.1 Clans et devises

| Clan du VTT | Existe ? | Devise VTT | Devise canonique | Verdict |
|---|---|---|---|---|
| Lames Franches (Livre V clan 2) | Oui | « Nul ne nous commande. Nul ne nous possède. » | Identique | **OK** |
| Navigateurs Gris (clan 10) | Oui | « Là où la route meurt, nous avançons encore. » | Identique | **OK** |
| Sceau Pourpre (clan 1) | Oui | « Un serment scellé vaut plus qu'une armée » | « Un serment scellé vaut plus qu'une armée. » | **OK** (ajouter le point final) |
| Pierres Hautes (clan 9) [option A Pascal] | Oui | — | « La montagne ne fuit pas l'orage. Elle l'endure, puis elle demeure. » | à saisir si option A |

### 5.2 Ce que disent les livres sur les rivalités concernées

| Relation | Source [L] |
|---|---|
| **Sceau Pourpre vs Lames Franches** : ennemis structurels | Livre V clan 1 : Ennemis = « Clan des Lames Franches (refus structurel de l'autorité) ». Clan 2 : Ennemis = « Clan du Sceau Pourpre (serments contraignants) ». Table V ch. 7 §2 (ligne 1 et 2). |
| Pierres Hautes vs Lames Franches : ennemis | Clan 9 : « Clan des Lames Franches (guerre mobile) ». |
| Lames Franches + Guilde Martiale + Navigateurs Gris : même **Bloc de la Liberté Martiale** | V ch. 7 §1 : « refus de toute autorité imposée sans consentement renouvelable ». |
| Sceau Pourpre dans le **Bloc de l'Ordre Légal** (avec Maisons Anciennes, Ordre du Flux, Archivistes) | V ch. 7 §1. |
| Navigateurs Gris : ennemis Voile Noir, Ordres Prophétiques | Clan 10. |
| Guilde Martiale : alliée des **deux** clans rivaux | Guilde 2 : « Alliances : Marchands Libres, Lames Franches, Sceau Pourpre ». |
| Marchands Libres : alliés du Sceau Pourpre **et** des Navigateurs Gris | Guilde 1. |
| Conflit d'obligations entre clans | V ch. 2 §4 : « un personnage affilié aux deux en position impossible ». |
| Exclusions asymétriques | V ch. 2 §2 : exclusion du Sceau = perte de citoyenneté ; exclusion des Lames = « rupture de contrat… pas de marque infamante ». |
| Pacte qui tourne mal / nécromancie | Livre VI ch. 11 : nécrotechnie interdite par l'Ordre du Flux (allié du Sceau), les Théocraties et la Confédération des Clans Ancestraux ; prix : « rupture de tous les liens claniques si la pratique est confirmée ». |

### 5.3 Ce que cela donne pour des amitiés entre clans rivaux (matrice des quatre personnages)

Hypothèse de départ (option B, retenue) : Krunt3 = Lames Franches ; Taranis = Navigateurs Gris ; Cyril = Sceau Pourpre ; Pascal = Sceau Pourpre (l'option A, Pierres Hautes, est abandonnée ; les lignes ci-dessous qui y renvoient sont des variantes).

| Paire | Relation de clan [L] | Ponts possibles [L/P] | Tension à jouer |
|---|---|---|---|
| Krunt3 – Taranis | **Alliés** (même Bloc Liberté Martiale ; Lames : « Navigateurs Gris » alliés dans la table V ch. 7) | Les deux acceptent un contrat qui se renouvelle, pas une loi | Aucune : c'est **l'amitié facile** du groupe (le pont vers les autres). |
| Krunt3 – Cyril | **Rivaux structurels** (Lames vs Sceau) ; **doublement** : Cyril est **Mage Blanc**, Krunt3 va devenir ce que le Mage Noir est (Livre VII ch. 2 : « Mage Noir + Mage Blanc : incompatibilité doctrinale totale ») | **Guilde Martiale** alliée du Sceau et des Lames ; les **Marchands Libres** de Cyril sont alliés du Sceau et des Navigateurs Gris (donc de Taranis) ; hook « La Lame sans Choix » (Livre V clan 2 : contrat valide selon le Sceau, nul selon le Code des Lames) | Cyril aide un homme que son clan doit juger : **conflit d'obligations** (V ch. 2 §4). Sanction du Sceau : lourde. |
| Krunt3 – Pascal | Rivaux (Lames vs Sceau Pourpre) | **Guilde Martiale commune dans le VTT** : le seul lien déjà inscrit sur les fiches de deux rivaux ; Pascal est Sentinelle (serment de veille), Krunt3 est devenu un « seuil » ambulant | Pascal tient une frontière, Krunt3 en est une. |
| Taranis – Cyril | Pas d'hostilité ; **Marchands Libres alliés des Navigateurs Gris** (Guilde 1) | Contrats de route, convois (Marches : « Route du Nord ») | Les Gris refusent « les chemins prédestinés » ; Cyril « les serments scellés » : philosophies opposées, **amitié sans obligation**. |
| Taranis – Pascal | Aucune relation écrite | Sentinelles du Pacte ↔ Navigateurs Gris : frontières contre passages (tension dans la fiche §3.4) | Taranis ouvre les routes que Pascal doit fermer. |
| Cyril – Pascal | Même clan : le Sceau Pourpre (frères de serment ; un seul des deux a prêté un serment d'aide) | Serment commun ; Mage Blanc + Alchimiste = synergie naturelle (Livre VII, fiche Mage Blanc : « Alchimiste, potions complémentaires ») | Doublons de clan : intérêts alignés ; le contraste vient du métier, de l'École et de la région. |

**Mécanismes d'amitié (appuyés sur les livres) [P]**
1. **Serment d'amitié à la Vallée des Serments** (Atlas, Hautes Terres) : les serments inter-claniques y sont prononcés devant témoins, les serments brisés jugés « sans loi écrite » ; la décision de rester ensemble peut s'y sceller : un lien que le Sceau Pourpre est tenu de reconnaître.
2. **« Les seuls à n'avoir aucun intérêt » (hook V clan 1, Le Juge Disparu)** : les héros, étrangers aux conflits locaux, sont les seuls en qui chaque clan peut avoir confiance : excellent motif pour que des rivaux travaillent ensemble.
3. **Survie plutôt que politique** : les Marches « n'appartiennent à personne complètement » et « chaque acteur présent a une raison de ne pas vouloir de témoin » (Atlas, Régions) : l'appartenance clanique n'y protège pas les trois étrangers (Taranis, lui, est chez lui côté clan et guilde) ; les rivalités s'y suspendent.
4. **Asymétrie des sanctions** (Livre V §2) : si Cyril aide Krunt3, il risque l'exclusion du Sceau (« aussi dommageable qu'une perte de citoyenneté ») ; si Krunt3 aide Cyril, les Lames n'ont qu'une rupture de contrat. Deux amis, deux risques inégaux : ressort dramatique.
5. **Le Flux comme arbitre commun** : l'Ordre du Flux est allié du Sceau, ennemi du Voile Noir, **juge de la nécrotechnie** ; il est l'adversaire que Cyril et Krunt3 finissent par avoir en commun.

Signature de sanction par clan (pour l'horloge « tôt ou tard » de la trame, d'après Livre V) **[P]** : **Lames Franches** : un **Cercle de Fer** convoque, aucune marque infamante, perte des réseaux de mercenaires. **Navigateurs Gris** : les **Vigies du Brouillard** coupent les routes alternatives et les réseaux de frontière. **Sceau Pourpre** : **Exécuteurs Mandatés**, invalidation d'un statut légal, perte d'accès aux archives. **Pierres Hautes** : retrait des refuges fortifiés, « lenteur » (le Conseil des Roches ne se presse pas).

---

## 6. Les éléments Wu Xing de l'application (point 4)

### 6.1 Ce que disent les livres
- **Wu Xing** (Livre I ch. 3 §4.6, Livre IX glossaire) : **Bois, Feu, Terre, Métal, Eau**. Utilisés pour les **Postures Légendaires** : Dragon Azur = Bois/Est ; Oiseau Vermillon = Feu/Sud ; **Tigre Blanc = Métal/Ouest** (« tranchant, structure, loi ») ; Tortue Noire = Eau/Nord ; **Phœnix = Terre/Centre (DISPARU)**. Et pour les cycles de Forge (Livre I ch. 5 §12).
- **Affinités élémentaires de Forge** (Livre I ch. 5) : **Feu, Eau, Terre, Vent, Foudre** (« Métal » n'y figure que dans « créature Métal/Foudre »).
- **Écoles mystiques** (Livre VI ch. 9) : Eau (Marées Liées), Feu (Cendres Vives), **Vent (Voies Hautes)**, Foudre (Fil Céleste), **Terre (Fondations)**, Éther pur, Âme, Cosmique.
- **Aucun** livre n'attribue un élément à une **région d'origine** : `region-elem` n'existe pas.

### 6.2 Correspondance

| Élément VTT | Personnage | Dans les livres ? | Équivalent canonique | Proposition [P] |
|---|---|---|---|---|
| **Vent** | Taranis | **Oui, mais pas comme Wu Xing** : affinité de Forge (plumes de créature Vent), **École mystique Voies Hautes (Vent)**. | Vent = affinité d'objets et d'école, **pas un élément de personnage**. | 1. **Conserver « Vent »** comme **affinité** du personnage (lien Souffle Long / chasse aux créatures Vent) ; 2. si l'on veut un élément Wu Xing : **Bois** (Dragon Azur, Est ; croissance, patience : « le vent soufflant de l'Est ») : la conversion déjà adoptée par docs/mecaniques/02 (« Bois = Vent »). |
| **Métal** | Cyril | **Oui, Wu Xing** | **Tigre Blanc = Métal, Ouest, « tranchant, structure, loi »** | **OK, très cohérent** : Sceau Pourpre (loi) et Flux Tranchant (tranchant). Posture Légendaire future : Tigre Blanc. |
| **Terre** | Pascal | **Oui, Wu Xing** | **Phœnix = Terre, Centre, DISPARU** ; École Fondations ; affinité Forge (carapace) la plus rare depuis la disparition du Phœnix | **OK** et **chargé de sens** : l'élément Terre est le seul sans Gardien (Livre I §4.6) ; Pascal est directement relié au mystère du Phœnix de la trame (piste A). |
| — | Krunt3 | — | — | **Laisser vide.** [P] Option de trame : « **Centre vacant** » : le trou laissé par le Phœnix, qui révèle un Terre latent quand l'entité se manifeste. |

**Changement de fiche.** `region-elem` devient **« affinité d'origine »** ou est supprimé ; le **lien** région → élément n'est qu'une convention d'application. [P] Si l'on la garde, la dériver du tableau suivant (proposition, aucune base dans les livres) :

| Région (Atlas) | Élément (convention [INV]) |
|---|---|
| Cœur Impérial | Métal |
| Hautes Terres Claniques | Terre |
| Déserts Rouges | Vent (steppe, « saisons des vents ») |
| Îles des Serments | Eau (ou vide) |

---

## 7. Écoles et postures (point 5)

### 7.1 Ce que disent les livres
- **Livre VI** : 14 Écoles martiales (une arme chacune), 8 mystiques, 7 techniques, écoles interdites (non accessibles à la création : Nécrotechnie, Manipulation Mémorielle, Corruption Dirigée, Pactes Abyssaux Profonds). **Aucune école ne s'appelle « Deux Lames », « Arc Précis » ni « Lame Droite ».** Les noms d'École de l'application décrivent l'arme ; ceux des livres décrivent une doctrine.
- **4 Postures naturelles** : **Loup**, Faucon, **Ours**, Félin (Livre VI ch. 4 ; Livre I ch. 3 §4.2). Les deux du VTT existent.
- Une seule école principale ; martiales mutuellement incompatibles (VI ch. 1).

### 7.2 Écoles : correspondances classées

| Fiche | École VTT | Rang | École canonique | Pourquoi |
|---|---|---|---|---|
| Krunt3 | Deux Lames | **1** | **Danse Rouge** (Double Lame · mode FLUX) | Double arme = « Deux Lames » ; tabou « **Perdre le contrôle de soi** » : écho direct de la possession ; Transe Écarlate ; jeu de mots avec le sprite « peau rouge ». Mode Flux (mobilité) un peu éloigné de la posture Ours (Ancrage) : tension créative. |
| Krunt3 | | 2 | **Mutation** (Hache-Épée · FLUX) | Sprite : **hache à deux mains** ; tabou « s'enfermer dans une seule forme » (le réceptacle change de forme). |
| Krunt3 | | 3 | **Coup Final** (Grande Lame · ANCRAGE) | Cohérent avec l'Ours (Ancrage, tenir) et avec l'exemple chiffré de docs/mecaniques/03 ; mais arme ≠ « Deux Lames ». |
| Taranis | Arc Précis | **1** | **Souffle Long** (Arc · mode RITUEL) | Seule école d'arc ; « Voir avant d'être vu » ; technique rang V « Flèche du Silence » (armure ignorée). |
| Taranis | | 2 | **Rafale** (Arbalète Légère · FLUX) | Si krunt veut un tireur mobile. Pas « arc » mais « Précis » et mobile. |
| Cyril | Lame Droite | **1** | **Flux Tranchant** (Épée Longue · FLUX) | « Lame droite » = épée longue ; tabou « briser volontairement le flux » ; Sceau Pourpre est dans les clans favorables aux Martiales (VI §5). |
| Cyril | | 2 | **Gardien Mobile** (Épée & Bouclier · ANCRAGE) | « Protéger et frapper » : cohérent avec Mage Blanc (soin). |
| Pascal | Lame Droite | **1** | **Gardien Mobile** (Épée & Bouclier · ANCRAGE) | **Différencie** Pascal de Cyril (deux « Lame Droite » identiques = doublon) ; mode Ancrage = Pierres Hautes et Sentinelles (« tenir position ») ; tabou « abandonner un allié protégé ». |
| Pascal | | 2 | **Mur Vivant** (Lance · ANCRAGE) | « Tenir la ligne » ; tabou « rompre la ligne » (miroir de la Veille). |

**Remarque : école mystique en seconde couche [L]** (« Une école mystique et une martiale peuvent coexister… dans des limites définies par Clan, Guilde, Ordre », VI ch. 1) : Cyril (Mage Blanc) peut recevoir plus tard **Fondations** (Terre, « Renforcement » d'armure d'un allié) ou **École du Flux** (Éther) ; **jamais Cendres Vives** (interdit « soins directs »).
**Tabou [L]** : chaque école a un tabou ; en jeu c'est une règle (docs/mecaniques/03 §5.4).

### 7.3 Postures et techniques de posture
| Fiche | Posture | Valeur dans les livres | Techniques (Livre VI ch. 4) | Verdict |
|---|---|---|---|---|
| Taranis, Cyril, Pascal | **Loup** (« Cohésion · Meute · Sacrifice collectif ») | Existe | Appel de Meute, Flanc Coordonné, Présence Rassurante, Sacrifice de Meute (2 End chacune) | **OK** |
| Krunt3 | **Ours** (« Protection · Absorption · Ancrage ») | Existe ; « utilise sa Vitalité comme ressource tactique » | Interposition, Ancrage, Provocation, Mur de Chair (2 End) | **OK** ; **cohérent avec la trame** (il encaisse la malédiction ; Q4 du questionnaire : « tenir la ligne »). |

Précautions [L] : (1) la technique « **Ancrage** » (Ours) porte le même nom que le **mode de Mana Ancrage** et que l'École 14 « Ancrage (Arbalète Lourde) » : à préfixer dans les données (`pos_ours_t2`). (2) Doublon de nom de technique Félin/Coup Final (« Frappe Décisive »), déjà signalé en docs/mecaniques/03. (3) `tech-ecole` et `tech-posture` du VTT sont des **libellés de sélection** de technique, pas les noms d'école : les remplir avec la technique de rang I de l'école canonique (ex. Danse Rouge : *Fuite Tranchante*).

---

## 8. Les métiers (point 6)

**[L]** Livre VII : 30 métiers en 5 blocs. Les trois du VTT existent : **Espion / Infiltrateur** (Social & Politique, p. 143 ; « collecteur de vérités interdites », variantes agent de cour, infiltrateur urbain, éclaireur secret, occulte, éthérique), **Mage Blanc** (Magie & Arcanes, p. 155 ; « gardien de l'équilibre vital »), **Alchimiste** (Artisans / Techniques, p. 35). Aucun n'est à renommer.

| Fiche | Métier | Verdict | Remarques [L] / propositions [P] |
|---|---|---|---|
| Krunt3 | Espion / Infiltrateur | **OK** | **Atout de trame [L]** : « Espion + **Mage Noir** : efficacité maximale, surveillance accrue » (VII ch. 2 §2). Le Mage Noir **niv. 30 débloque la Nécromancie** (VII, Mage Noir) ; Livre VII lie « Espion/Infiltrateur » au **Mage Noir** pour « usage discret ». [P] Laisser le **métier secondaire vide** pour le **Mage Noir par jalon narratif** après la tentative. Candidats si l'on veut un métier plus martial pour un Ours : Dépeceur, Instructeur (la synergie Instructeur « avec n'importe quel métier »). |
| Taranis | Espion / Infiltrateur | **OK mais doublon** avec Krunt3 | [P] Candidats classés : **1.** Chasseur-Pisteur + Cartographe (Livre VII : Cartographe donne « accès et voies secrètes » à l'Espion ; Cartographes Gris des Navigateurs ; Guilde de Chasse) ; **2.** garder Espion/Infiltrateur et ajouter Cartographe en secondaire (variante « Éclaireur secret ») ; **3.** Trappeur Élémentaire (créatures Vent, lien Forge). Équilibrage du groupe : deux espions = redondant. |
| Cyril | Mage Blanc | **OK** | Synergies [L] : Médecin, Instructeur, Sentinelle d'Honneur, Artisan d'Éther, **Alchimiste** (Pascal). **Tension [L]** : « **Mage Noir + Mage Blanc : incompatibilité doctrinale totale** » : c'est le noyau du conflit Cyril-Krunt3 une fois Krunt3 maudit. |
| Pascal | Alchimiste (3 ★) | **OK**, mais **3 étoiles à la création est incorrect** | Livre I ch. 3 §3.2 / §7 étape 6 : on commence à **★ 1 (Apprenti)**. ★★★ (Maître) = jalon narratif fort (« le clan te reconnaît »). Synergies : Herboriste, Artisan d'Éther, Médecin, Mage Blanc (via Cyril), Chasseur-Pisteur. Variantes : médicale, martiale, naturelle, éthérique, **interdite** (mutagènes) : un pont vers « ce que l'entité demande ». |

Points [L] à connaître : (a) **2 métiers max** sans pénalité ; (b) le **Livre VI dit « 30 Métiers détaillés dans le Livre 1 »** alors qu'ils sont au **Livre VII** (renvoi erroné) ; (c) deux systèmes de niveau coexistent : **3 étoiles** (Livre I) et **30 niveaux avec paliers 5/10/…/30** (Livre VII) : docs/mecaniques/03 §6 les relie ; (d) école « interdite » à la création : Livre I (étape 5) l'admet, Livre VI ch. 11 §3 le refuse (§14).

---

## 9. Étoiles, jauges, attributs, équipement et champs annexes

### 9.1 Règles de création [L] (Livre I ch. 3 §7 et ch. 2)
- **42 points** à répartir sur FOR, AGI, END, ESP, VOL, PRE ; **min 3, max 12** ; bonus d'origine ensuite. Les attributs valent **1 à 20** (au-delà : rare).
- **Vitalité max = 4 + END** (7 à 16 cases) ; **Endurance max = 10** à la création ; **Mana de départ = 2 × rang** (rang I = 2) selon Livre I, mais Livre VI : 6 à 8 (docs/mecaniques/03 : 6 pour le rang I) : **tranché provisoirement à 6 / 6 / 8 / 6, à confirmer par krunt** (`10` Q22) ; **Honneur de départ 4 à 6** (« Reconnu »), ±1 selon l'origine.
- **Forge** (0 à 40, paliers de 10) et **Tension** : **jauges COLLECTIVES** (portées par le groupe).
- 12 points de compétence + 2 (École) + 2 (Métier) + 1 (Posture), 3 max par compétence.
- Une seule jauge systémique pour la réputation : **l'Honneur** (« ni karma, ni jauge cachée parallèle », Livre I §8) : le « karma » de la trame = Honneur + marques.

### 9.2 Écarts

| Champ | Valeur(s) VTT | Règle canonique | Verdict |
|---|---|---|---|
| Attributs Krunt3 | 5/5/3/3/5/6 = **27** | 42 points, min 3 | **15 points non répartis**. À compléter (équilibrage : voir docs/trame/04). Bonus +1 END (Îles). |
| Attributs Taranis, Cyril, Pascal | 10 partout = **60** | 42 points, max 12 | **18 points de trop** ; ce sont des valeurs par défaut (fiches de test). À remplacer. |
| `attr-*` / `attr_*` | Deux familles de clés | — | À unifier côté VTT. |
| `gauge-vit` | 20 / 15 / 20 / 11 | 4 + END | Krunt3 (END 3 +1 = 4) : **8** ; autres : selon END final (END 7 → 11). |
| `gauge-end` | 20 / 15 / 20 / 13 | 10 | **10** pour tous. |
| `gauge-mana` | 20 / 10 / 20 / 9 | 2 (L I, rang I) ; 6 (docs/mecaniques/03) | **2 ou 6** ; à trancher avant import. |
| `gauge-hon` | 4 / 5 / **7** / 5 | 4 à 6 à la création | **Cyril : 5** (v2 ; 7 = « Estimé » n'est pas autorisé au départ) ; **Taranis : 4**, **Pascal : 6** (v2, `08` §3.2). Krunt3 (4) : bas, cohérent avec Lames Franches (honneur « personnel » ; ouvert au malheur). |
| `gauge-ten` | 1 (Krunt3) / 0 | **Collective**, 0 au départ | Passer au niveau **groupe** ; supprimer des fiches. |
| `gauge-forge` | 0 | **Collective**, 0 au départ | idem. |
| `m1-stars-val` | Pascal : 3 | ★1 à la création | **1**. |
| Équipement Pascal | « sabre laser » 1d20 ; « adamentium » ; « Boulet » *Légendaire*, Vitesse −2 ; 5 000 Éclats | Livre I ch. 5 : un seul objet **Légendaire** par forgeron (Forge palier 40) ; matériaux issus de créatures (cinq affinités) ; **pas de matériau « adamantium »** dans les livres ; l'**Éclat** est la monnaie du monde (Livre IX glossaire) | **ABSENT** (science-fiction ; nom de métal inventé ; objet légendaire interdit à la création). Remplacer par l'**arme de l'école** (épée et bouclier : Gardien Mobile) en qualité **Standard** ; revoir le budget d'Éclats. |
| Système de **poids** (`weight-*`, `capacity-max`, `arm-*-poids`) | présent | Livre I : pas de règle de charge (FOR : « port de charges » seulement) ; docs/mecaniques/02 : « pas de gestion de poids » | **ABSENT** des livres ; à retirer ou à documenter. |
| `tl-*` (Temps Libre) | 5 cases | Livre I ch. 6 §3 : **5 activités** (Repos complet, Travail de Forge, Activité sociale ou politique, Rien de particulier, Action risquée ou visible) | **OK** |
| `snap1…4` (Snapshot) | Pascal : snap2 « le respect », snap3 « rien » | Livre I ch. 2 §11 : 4 lignes : *Où sommes-nous ? · Ce que le monde me doit · Ce que je dois au clan · Prochaine intention* | **OK** ; hook : « Ce que je dois au clan : rien » est exactement le profil de celui qui **abandonnera** le clan (sanction à venir). |

---

## 10. Fiche par fiche : ce qui doit changer

### Krunt3 (le héros)
| Champ | Avant | Après (recommandé) | Statut |
|---|---|---|---|
| region | Plaines Franches | **Îles des Serments** | remplacer |
| region-elem | — | (vide) | conserver vide |
| clan-nom / devise | Lames Franches / devise | idem | OK |
| guilde-nom / spec | Guilde Martiale / Administration de la guerre | idem / **Guerre contractuelle (Officiers-Loges : discipline et soldes)** | ajuster la spécialité |
| ordre-nom / philo | Ordre du Jugement / Justice et loi | **Frères de l'Épreuve** / « Juger par l'épreuve » | remplacer |
| ecole / tech-ecole | Deux Lames | **Danse Rouge** (alt. Mutation, Coup Final) / *Fuite Tranchante* | remplacer |
| posture / tech-posture | Ours | Ours / *Interposition* | OK |
| m1-nom | Espion / Infiltrateur (★ non fixé) | Espion / Infiltrateur ★1 ; M2 vide (Mage Noir par jalon) | OK |
| attr | 27 pts | 42 pts, END +1 (origine Îles), min 3 | compléter |
| gauge | 20/20/20/4/1/0 | Vit 4 + END ; End 10 ; Mana 2 (ou 6) ; Hon 4 ; collectives hors fiche | corriger |

### Taranis
| Champ | Avant | Après | Statut |
|---|---|---|---|
| region / elem | Steppes du Vent / Vent | **Déserts Rouges** / Vent comme affinité (ou Bois) | remplacer ; élément à requalifier |
| clan | Navigateurs Gris (devise exacte) | idem | OK |
| guilde | Guilde de Chasse / Contrats de chasse, formation | idem | OK |
| ordre | — | — (valide : aucun ordre actif aux Marches) | OK |
| ecole | Arc Précis | **Souffle Long** (alt. Rafale) / *Tir Ciblé* | remplacer |
| posture | Loup | Loup / *Appel de Meute* | OK |
| m1 | Espion / Infiltrateur | **Chasseur-Pisteur** + Cartographe (ou Espion + Cartographe) | existe ; doublon à lever |
| attr / jauges | 10 partout ; 15/15/10/5 | 42 pts (5/11/6/9/6/5) ; Vit 10, End 10, Mana 6, Hon 4 (v2) | corriger |

### Cyril
| Champ | Avant | Après | Statut |
|---|---|---|---|
| region / elem | Terres du Sceau / Métal | **Cœur Impérial** / Métal (Tigre Blanc, Ouest) | remplacer la région ; élément OK |
| clan / devise | Sceau Pourpre | idem (+ point final) | OK |
| guilde | Marchands Libres / Commerce, contrats, économie | idem / **Crédit, dette et voies commerciales** | ajuster la spécialité |
| ordre | — | — (option : Ordre du Flux, à ne pas imposer) | OK |
| ecole | Lame Droite | **Flux Tranchant** / *Première Vague* | remplacer |
| posture | Loup | Loup | OK |
| m1 | Mage Blanc | Mage Blanc ★1 | OK |
| gauge-hon | 7 | **5** (v2) | corriger |
| attr / jauges | 10 partout ; 20/20/20 | 42 pts ; Vit 4+END ; End 10 ; Mana 2/6 | corriger |

### Pascal
| Champ | Avant | Après | Statut |
|---|---|---|---|
| region / elem | Cols Fortifiés / Terre | **Hautes Terres Claniques** / Terre (Phœnix, Centre) | remplacer la région ; élément OK |
| clan / devise | Sceau Pourpre | **Sceau Pourpre** (décision de krunt ; l'option Pierres Hautes est abandonnée) | décidé |
| guilde | Guilde Martiale / Administration de la guerre | idem / **Capitaineries de défense (garde, siège)** | ajuster la spécialité |
| ordre / philo | Sentinelles du Pacte / Protection des frontières | **Sentinelles du Pacte** (fiche §3.4) / « Veiller les seuils : nul ne passe sans être nommé » | créer dans StoryForge |
| ecole | Lame Droite | **Gardien Mobile** (alt. Mur Vivant) / *Garde Haute* | remplacer |
| posture | Loup | Loup | OK |
| m1 / étoiles | Alchimiste / ★★★ | Alchimiste ★1 | corriger les étoiles |
| equipement | sabre laser, adamentium, Boulet Légendaire, 5 000 Éclats | arme d'école (épée, qualité Standard) ; budget de départ à fixer | remplacer |
| attr / jauges | 10 partout ; 11/13/9/5 | 42 pts ; Vit 4+END ; End 10 ; Mana 6 ; Hon 6 (v2) | corriger |

---

## 11. Tableau de correspondance prêt à importer (champ VTT → valeur canonique)

Format : `personnage ; champ VTT ; valeur actuelle ; valeur canonique ; action ; source`. Les valeurs en **gras** sont celles qui font foi ; « (alt.) » = candidate 2 ; « [INV] » = à créer dans StoryForge.

```
personnage;champ;valeur_actuelle;valeur_canonique;action;source
Krunt3;region;Plaines Franches;Îles des Serments;remplacer;Atlas Région 6 / Livre II ch.4 d20 n°6
Krunt3;region-elem;—;;vide;Livre I ch.3 §4.6 (aucun élément de région)
Krunt3;clan-nom;Lames Franches;Lames Franches;ok;Livre V clan 2
Krunt3;clan-devise;Nul ne nous commande. Nul ne nous possède.;Nul ne nous commande. Nul ne nous possède.;ok;Livre V clan 2
Krunt3;guilde-nom;Guilde Martiale;Guilde Martiale;ok;Livre V Guilde 2
Krunt3;guilde-spec;Administration de la guerre;Guerre contractuelle (Officiers-Loges : discipline et soldes);ajuster;Livre V Guilde 2
Krunt3;ordre-nom;Ordre du Jugement;Frères de l'Épreuve;remplacer;Atlas Région 6 / Livre V §5
Krunt3;ordre-philo;Justice et loi;Juger par l'épreuve : seuls ceux qui ont prouvé leur valeur jugent les autres;remplacer;Atlas Région 6
Krunt3;ecole;Deux Lames;Danse Rouge (alt. Mutation, Coup Final);remplacer;Livre VI ch.8 École 4
Krunt3;tech-ecole;Deux Lames;Fuite Tranchante;remplacer;Livre VI ch.8 École 4 rang I
Krunt3;posture;Ours;Ours;ok;Livre VI ch.4 §4
Krunt3;tech-posture;Ours;Interposition;ajuster;Livre VI ch.4 §4
Krunt3;m1-nom;Espion / Infiltrateur;Espion / Infiltrateur (★1; M2 réservé Mage Noir);ok;Livre VII p.143
Krunt3;attr-total;27;42 (min 3, max 12, END +1 origine Îles);compléter;Livre I ch.3 §7
Krunt3;gauge-vit;20;4 + END;recalculer;Livre I ch.2 §4
Krunt3;gauge-end;20;10;corriger;Livre I ch.3 §7
Krunt3;gauge-hon;4;4;ok;Livre I ch.3 §7
Krunt3;gauge-ten;1;(collective, 0);supprimer de la fiche;Livre I ch.2 §3
Krunt3;gauge-forge;0;(collective, 0);supprimer de la fiche;Livre I ch.2 §3
Taranis;region;Steppes du Vent;Déserts Rouges (alt. Marches Frontalières);remplacer;Atlas Région 9 / Livre V §5
Taranis;region-elem;Vent;Vent (affinité) ou Bois (Wu Xing);requalifier;Livre I ch.5 affinités / Livre VI ch.9 École 3
Taranis;clan-nom;Navigateurs Gris;Navigateurs Gris;ok;Livre V clan 10
Taranis;clan-devise;Là où la route meurt, nous avançons encore.;Là où la route meurt, nous avançons encore.;ok;Livre V clan 10
Taranis;guilde-nom;Guilde de Chasse;Guilde de Chasse;ok;Livre V Guilde 5
Taranis;guilde-spec;Contrats de chasse, formation;Contrats de chasse, formation;ok;Livre V Guilde 5
Taranis;ordre-nom;—;—;ok (aucun);Livre V §5 (Marches : ordre « — »)
Taranis;ecole;Arc Précis;Souffle Long (alt. Rafale);remplacer;Livre VI ch.8 École 12
Taranis;tech-ecole;Arc Précis;Tir Ciblé;remplacer;Livre VI École 12 rang I
Taranis;posture;Loup;Loup;ok;Livre VI ch.4 §2
Taranis;tech-posture;Loup;Appel de Meute;ajuster;Livre VI ch.4 §2
Taranis;m1-nom;Espion / Infiltrateur;Chasseur-Pisteur (+ Cartographe);remplacer (recommandé);Livre VII bloc 2 et 3
Taranis;gauge-hon;5;4;corriger (v2, 08 §3.2);Livre I ch.3 §7
Cyril;region;Terres du Sceau;Cœur Impérial;remplacer;Atlas Région 1 / Livre V §5
Cyril;region-elem;Métal;Métal (Tigre Blanc, Ouest);ok;Livre I ch.3 §4.6
Cyril;clan-nom;Sceau Pourpre;Sceau Pourpre;ok;Livre V clan 1
Cyril;clan-devise;Un serment scellé vaut plus qu'une armée;Un serment scellé vaut plus qu'une armée.;ok;Livre V clan 1
Cyril;guilde-nom;Marchands Libres;Marchands Libres;ok;Livre V Guilde 1
Cyril;guilde-spec;Commerce, contrats, économie;Crédit, dette et voies commerciales;ajuster;Livre V Guilde 1
Cyril;ordre-nom;—;—;ok (option Ordre du Flux);Livre V §5
Cyril;ecole;Lame Droite;Flux Tranchant (alt. Gardien Mobile);remplacer;Livre VI ch.8 École 2
Cyril;tech-ecole;Lame Droite;Première Vague;remplacer;Livre VI École 2 rang I
Cyril;posture;Loup;Loup;ok;Livre VI ch.4 §2
Cyril;m1-nom;Mage Blanc;Mage Blanc (★1);ok;Livre VII p.155
Cyril;gauge-hon;7;5;corriger (v2, 08 §3.2);Livre I ch.3 §7 (4 à 6)
Pascal;region;Cols Fortifiés;Hautes Terres Claniques;remplacer;Atlas Région 4 / Livre V §5
Pascal;region-elem;Terre;Terre (Phœnix, Centre);ok;Livre I ch.3 §4.6
Pascal;clan-nom;Sceau Pourpre;Sceau Pourpre;ok (décision de krunt);Livre V clan 1
Pascal;clan-devise;Un serment scellé vaut plus qu'une armée;Un serment scellé vaut plus qu'une armée.;ok (point final);Livre V clan 1
Pascal;guilde-nom;Guilde Martiale;Guilde Martiale;ok;Livre V Guilde 2
Pascal;guilde-spec;Administration de la guerre;Capitaineries de défense (garde, siège);ajuster;Livre V Guilde 2
Pascal;ordre-nom;Sentinelles du Pacte;Sentinelles du Pacte [INV];créer dans StoryForge;fiche §3.4
Pascal;ordre-philo;Protection des frontières;Veiller les seuils : nul ne passe sans être nommé;ajuster;fiche §3.4
Pascal;ecole;Lame Droite;Gardien Mobile (alt. Mur Vivant);remplacer;Livre VI ch.8 École 3
Pascal;tech-ecole;Lame Droite;Garde Haute;remplacer;Livre VI École 3 rang I
Pascal;posture;Loup;Loup;ok;Livre VI ch.4 §2
Pascal;m1-nom;Alchimiste;Alchimiste;ok;Livre VII p.35
Pascal;m1-stars-val;3;1;corriger;Livre I ch.3 §3.2 et §7 étape 6
Pascal;arme-nom;sabre laser;Épée (arme de l'école, qualité Standard);remplacer;Livre I ch.5 / Livre VI École 3
Pascal;arm-pieds-etat;Légendaire;Standard;corriger;Livre I ch.5 (1 seul Légendaire, Forge palier 40)
Pascal;arm-pieds-mat;adamentium;(matériau d'affinité du Livre I ch.5);remplacer;Livre I ch.5
Pascal;eclats;5000;(budget de départ à fixer);à fixer;Livre IX glossaire (Éclats = monnaie)
```

---

## 12. Points à ajouter ou modifier dans StoryForge

**À ajouter**
1. **Ordre « Sentinelles du Pacte »** (fiche §3.4) : fiche d'ordre complète + case « Ordre actif » des **Marches Frontalières** (le « — » du tableau V §5) ; alliés/ennemis/hooks ci-dessus.
2. **Fiche « Frères de l'Épreuve »** au niveau des 8 ordres de Livre V ch. 5 (alliés, tensions, hooks : §3.5) ; la mentionner dans le tableau V §5 comme ordre à fiche.
3. **Fiches des ordres cités mais non détaillés** (cohérence Livre V) : Culte des Ancêtres (Veilleurs), Veilleurs du Flux, Porte-Cendres (au moins une fiche synthétique chacun).
4. **Alias** « Ordre du Jugement » → Frères de l'Épreuve (surnom) ; « Plaines Franches », « Steppes du Vent », « Terres du Sceau », « Cols Fortifiés » → conservés comme **noms vernaculaires** (sous-régions ou surnoms locaux), pas comme régions.
5. **Spécialités de guilde** (champ « domaine » par guilde) : Guilde Martiale (contrats de guerre ; Officiers-Loges ; Capitaineries), Guilde de Chasse (contrats, formation), Marchands Libres (crédit, dette, voies commerciales).
6. **Table de correspondance Wu Xing** : étendre la table des Postures Légendaires avec les **affinités de Forge** (Vent, Foudre) et des **conversions** (Bois = Vent, Métal = Foudre, docs/mecaniques/02) pour résoudre les trois systèmes d'éléments.
7. **Éléments des régions** : champ **optionnel** `affinite` (convention [INV], §6.2) ; ne pas le présenter comme canon.
8. **Fiche « Technique oubliée »** (liaison trame) : Nécrotechnie (Livre VI ch. 11) = Nécromancie (Livre VII, Mage Noir niv. 30) : même chose sous deux noms ; relier à Ordre du Flux (hostile), Théocraties, Confédération des Clans Ancestraux et à la piste du Phœnix (Atlas ch. 13).

**À modifier**
9. Tableau V §5 : Marches Frontalières, ordre actif « — » → **Sentinelles du Pacte** (si krunt l'adopte) ; Îles des Serments, clan « — » → mention « Lames Franches (présence libre) ».
10. Déserts Rouges : unifier **Ordre du Sable** (Livre V, II) et « Ordres du Silence » (Livre IX).
11. Cœur Impérial : unifier **Ordre du Flux** (Livre V) et « Sceau de l'Équilibre » (Livre II, IX).
12. Livre V clan 2 (Lames Franches) : ajouter **Navigateurs Gris** aux alliés (la table V ch. 7 les donne, la fiche non). 
13. Livre VI : renvoi « Métiers dans le Livre 1 » → **Livre VII** ; écoles interdites « accessibles » (Livre I étape 5) à aligner avec Livre VI ch. 11 §3 (« non accessibles à la création »).
14. Livre VI ch. 3 vs ch. 9 : **Voies Hautes** mode Rituel ou Flux (ch. 3 : Rituel ; ch. 9 : Flux).

---

## 13. Modifications à faire dans l'application du VTT pour suivre StoryForge

1. **Remplacer la liste des régions d'origine** par les **20 régions de l'Atlas** (ou, au minimum, les quatre régions retenues ici) ; stocker en plus un alias vernaculaire facultatif. Ajouter le **bonus d'origine** (+1 END Îles, +1 VOL Hautes Terres) appliqué automatiquement.
2. **Remplacer la liste des écoles** (Deux Lames, Arc Précis, Lame Droite…) par les **14 martiales + 8 mystiques + 7 techniques** de Livre VI (noms de StoryForge) ; verrouiller « interdites » à la création.
3. **Listes d'ordres** : les 8 ordres de Livre V + Frères de l'Épreuve + Sentinelles du Pacte (si adoptés) + ordres secrets (Voile Noir, Masques de Verre) en « non sélectionnables à la création ».
4. **Liste des guildes** : les 7 de Livre V, avec spécialité **tirée de StoryForge** (champ en lecture seule, plus de texte libre).
5. **Cohérence région → clan → guilde → ordre** : afficher un **avertissement** (non bloquant) si le choix ne suit pas le tableau V §5 (« rupture culturelle à jouer »).
6. **Devises** : alimentées par le clan sélectionné (lecture seule).
7. **Éléments** : remplacer `region-elem` par un champ **affinité** (Bois, Feu, Terre, Métal, Eau + Vent, Foudre) clairement séparé de la région.
8. **Attributs** : une seule famille de clés (`attr_*`), **42 points, min 3, max 12**, calcul des attributs secondaires ; supprimer les valeurs par défaut à 10.
9. **Jauges** : Vitalité = 4 + END ; Endurance 10 ; Mana = f(rang) ; Honneur 4 à 6 ; **Tension et Forge déplacées au niveau du groupe**.
10. **Métiers** : étoiles ★1 à la création ; limite à 2 métiers ; liste des 30 de Livre VII ; contrôle des synergies/tensions (Mage Blanc + Mage Noir, Espion + Sentinelle).
11. **Équipement** : retirer « sabre laser » et « adamentium » ; qualités par **Standard / Supérieure / Élémentaire / Rare** (Livre I ch. 5), un seul **Légendaire** par forgeron ; retirer ou documenter le système de poids ; monnaie « Éclats » (Livre IX) avec budget de départ.
12. **Techniques** (`tech-ecole`, `tech-posture`) : listes déduites de l'école et de la posture (rang I) plutôt que texte libre.
13. **Snapshot et Temps Libre** : conserver (ils sont canoniques) ; ajouter les libellés des 4 lignes du Snapshot sur l'écran.

---

## 14. Incohérences entre livres rencontrées pendant ce travail

| # | Incohérence | Où |
|---|---|---|
| 1 | Ordres cités comme « ordre actif » sans fiche : Frères de l'Épreuve, Culte des Ancêtres, Veilleurs du Flux, Porte-Cendres (Livre V annonce **8 ordres**) | Livre V §5 et ch. 5 ; Livre II ; Atlas |
| 2 | Déserts Rouges : Ordre du Sable / Ordres du Sable / **Ordres du Silence** | Livre V, II, IX |
| 3 | Cœur Impérial : **Ordre du Flux** ou **Sceau de l'Équilibre** | Livre V ; Livre II, IX |
| 4 | Cités Libres Marchandes : Cultes Syncrétiques ou **Ligue des Signes Dorés** | Livre V, IX ; Livre II |
| 5 | Trois systèmes d'éléments : Wu Xing (Bois, Feu, Terre, Métal, Eau) ; affinités de Forge (Feu, Eau, Terre, Vent, Foudre) ; écoles mystiques « alignées sur les cinq éléments » (Eau, Feu, Vent, Foudre, Terre) ; « Métal » seulement par « Métal/Foudre » | Livre I ch. 3, ch. 5 ; Livre VI ch. 9 ; Livre IX |
| 6 | Voies Hautes : mode Rituel (ch. 3) ou Flux (ch. 9) | Livre VI |
| 7 | Écoles interdites choisissables à la création (Livre I) ou non (Livre VI ch. 11) | Livre I ch. 3 §7 ; Livre VI |
| 8 | Renvoi « 30 Métiers dans le Livre 1 » (c'est le Livre VII) | Livre VI ch. 1 |
| 9 | Nécrotechnie (Livre VI) et Nécromancie (Livre VII) : deux noms pour la même pratique | Livre VI ch. 11 ; Livre VII |
| 10 | Mana de départ : 2 × rang (Livre I) contre la table de docs/mecaniques/03 (6 au rang I) | Livre I ; docs |
| 11 | Étoiles (3) et niveaux (30) pour un même métier | Livre I ch. 3 ; Livre VII |
| 12 | « Karma » (trame, Livre II : corruption karmique) contre « il n'y a ni karma, ni jauge cachée » (Livre I ch. 2 §8) | Livre I ; Livre II |
| 13 | Table d'origine (d20) annoncée dans Livre I ch. 3 §4 mais absente de ce chapitre (déjà dans l'audit) | Livre I ; docs/audit |

---

## Compte rendu (5 lignes)

1. **Couvert** : les 4 personnages champ par champ ; régions (4 absentes → Îles des Serments, Déserts Rouges, Cœur Impérial, Hautes Terres), ordres (Jugement → Frères de l'Épreuve ; **fiche complète créée pour Sentinelles du Pacte**), guildes (les 3 existent), éléments, écoles/postures, métiers, relations de clans (matrice, ponts, mécanismes d'amitié), tableau importable, listes StoryForge et VTT.
2. **Faible** : attributs, jauges et valeurs de départ ne sont ramenés qu'aux **règles** (la répartition fine des 42 points et l'équilibrage relèvent de docs/trame/04) ; la fiche des Sentinelles du Pacte et les alliés/ennemis des Frères de l'Épreuve sont **inventés** (marqués [INV] / [P]) ; les éléments par région sont une convention sans appui des livres ; numéros de ligne approximatifs (livres lus en copie de travail).
3. **Recommandation 1** : adopter les quatre régions de l'Atlas ci-dessus (aucun héros n'est originaire des Marches : c'est leur terre d'arrivée) et traiter les noms du VTT comme des surnoms.
4. **Recommandation 2** : Krunt3 → **Frères de l'Épreuve** ; Pascal **reste au Sceau Pourpre** (décision de krunt, en remplacement de la recommandation Pierres Hautes) + **Sentinelles du Pacte** à créer dans StoryForge (ou repli, `10` Q17) ; Pascal et Cyril partagent le clan mais ne partagent ni école ni région (4 écoles, 4 régions distinctes).
5. **Recommandation 3** : corriger côté VTT les listes déroulantes (régions, écoles, ordres, guildes) et les règles de création (42 points, Vitalité 4 + END, Tension et Forge collectives, ★1) avant d'importer le tableau §11 ; ponts d'amitié entre rivaux : Guilde Martiale (Krunt3-Pascal), Marchands Libres (Cyril-Taranis), bloc Liberté Martiale (Krunt3-Taranis).
