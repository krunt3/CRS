# Mécaniques 04 : Diplomatie, joutes verbales, intrigue et réputation (Jeu B)

Statut : brouillon de conception, à relire par krunt. Les chiffres marqués **(à tester)** sont des valeurs de départ, pas des vérités. Ce domaine n'a aucun équivalent dans les jeux de chasse de référence : tout est à créer, donc le risque de coût est le plus élevé de tous les domaines (voir §11).

Références : L1 = Livre I (Règles complètes), L2 = Livre II (Maître du Jeu), L4 = Atlas, L5 = Histoire et politique, L8 = Supplément du Joueur. Les numéros de chapitre suivent l'état actuel des livres (voir `docs/audit/notes-lecture-livres.md` pour les renvois cassés).

---

## 1. Ce que disent les livres

### 1.1 Les conflits sociaux (L1 ch. 9)

Principes : « la fiction d'abord », l'enjeu d'un conflit social est la réputation, la position et la parole (pas la Vitalité), et les conséquences durent (une défaite ne s'efface pas au repos). Moteur identique au reste du jeu : **d20 + Attribut + Compétence contre DD**.

| Échelle | Définition | Durée à la table |
|:--|:--|:--|
| Scène sociale | Un échange où l'issue est incertaine (négocier sous tension, convaincre un opposant, résister à une accusation) | Quelques jets |
| Duel verbal | Joute structurée, en manches, avec ressource, public et condition de fin | Une scène |
| Intrigue | Guerre d'information en 4 phases, à l'échelle de semaines | Un arc |
| Pression politique | État continu qui modifie DD et options (clan, institution, public) | Permanent |

**Positions d'entrée** (L1 ch. 9 §I.b) : Favorable DD 10, Neutre DD 15, Hostile DD 20, Fermé (pas de jet, se contourne). La position bouge pendant la scène. Les enjeux sont à deux niveaux : **déclarés** (définissent le DD) et **cachés** (définissent ce que la réussite coûte vraiment). Révéler un enjeu caché : jet d'Esprit DD 15 (DD 20 acteur chevronné).

**Attributs** : Présence (agir sur l'autre), Volonté (tenir sous pression), Esprit (lire, analyser, manipuler par l'information). La Force n'est un argument que dans les cultures qui l'acceptent (Hautes Terres Claniques, Îles des Serments). **Autorité sociale = Présence + Honneur**, quand la position sociale est elle-même l'argument.

**Cinq résultats** (contexte social) : 20 naturel (changement de position et information favorable qui se répand, gain d'Honneur possible) ; réussite nette ; **réussite tendue** (objectif atteint à un prix : concession, délai, contrepartie, témoin gênant ; « un accord obtenu sous tension crée toujours une dette, une attente ou un témoin ») ; échec (la position se ferme, la tentative a été vue) ; 1 naturel (échec retentissant). Jet opposé : actif d20 + PRE + compétence contre défenseur d20 + VOL + compétence ; égalité : le défenseur garde sa position.

**Duel verbal** (L1 ch. 9 §III) :

- Ressource : **Composure = Volonté + Esprit**. 0 : « perd pied » (plus d'offensives). À −Volonté : cède (accepte les termes, se contredit, ou part). Récupération complète après un repos court. **1 point d'Honneur dépensé = récupère Volonté en Composure**, visiblement (« les témoins le notent »).
- Initiative : d20 + Présence + Esprit. Une manœuvre par manche : l'attaquant déclare, le défenseur répond, résolution, les rôles s'inversent.
- Manœuvres offensives : Pression directe (PRE, inflige PRE÷4), Dévoilement (ESP, ESP÷3 si la cible ne peut pas réfuter), Appel à l'Honneur (Autorité sociale : la cible doit céder sur sa position ou sur son Honneur), Retournement (ESP, ESP÷4 et état EXPOSÉ), Isolement (PRE, désavantage aux réponses jusqu'à la fin de la manche suivante), Silence weaponisé (VOL, opposé : le premier qui parle perd 3 Composure).
- Manœuvres défensives : Tenir sa position (VOL, réduit la perte de VOL÷4, sans jet), Redirection (ESP, DD adverse +3 jusqu'à la manche suivante), Appel au public (PRE, Honneur intact quel que soit le résultat), Concession tactique (récupère ESP÷4, crée EN DETTE), Rupture (met fin au duel, coût d'Honneur régional).
- États sociaux : EXPOSÉ (désavantage aux offensives), ISOLÉ, DÉSTABILISÉ (≥ 50 % de Composure perdue en une manche : désavantage à la défense suivante), ENGAGÉ (déclaration irréversible : contredire coûte de l'Honneur), EN DETTE (contrepartie due, définie plus tard).
- Fin : −VOL de Composure, condition narrative remplie, rupture, ou intervention d'un tiers. Le résultat entre dans la « mémoire sociale » de la région.

**Intrigue** (L1 ch. 9 §IV) : 4 phases (Identification, Infiltration, Manipulation, Résolution) ; chaque phase réussie réduit le DD final : 4/4 −6, 3/4 −3, 2/4 standard, 1/4 +3, 0/4 +6 et l'adversaire est prévenu. Information = **Secrets** (valeur, fragilité, exposition), utilisables en Révéler / Menacer / Manœuvrer. **Réseau** = nœuds (position, fiabilité, coût), non chiffré. **Exposition** = 4 niveaux cachés (Faible, Modérée, Élevée, Critique), réduite en couvrant les traces, en passant par un intermédiaire (coûte un nœud) ou en laissant le temps passer.

**Pressions** (L1 ch. 9 §V) : clan (désavantage aux actions contraires au clan, résistance VOL), institutionnelle (désavantage aux actes illégaux, résistance ESP ou PRE), publique (DD +3 ou désavantage dans la région, pas de jet de résistance). Résistance par la Volonté : DD 10 légère, 15 modérée, 20 forte, 25 totale ; l'échec = cède partiellement (temporise, ne choisit pas).

**Conséquences** (L1 ch. 9 §VII) : mémoire sociale (« règle de la précédence » : la position de départ de chaque PNJ intègre ce qu'il a entendu), dettes (faveur, dette de sang, pacte d'intérêts, compte ouvert), exclusion en 4 niveaux (désaveu discret, mise à l'écart DD +3, exclusion formelle désavantage, exil), escalade avec une table d12 de signes avant-coureurs.

**Variations régionales** (L1 ch. 9 §VIII), reprises au §3.4.

### 1.2 L'Honneur (L1 ch. 1 §9, ch. 2 §8 ; L2 ch. 1)

- Une seule jauge systémique, **0 à 10**, « mémoire que le monde conserve de vous ». Pas de karma. Valeur connue du MJ seul ; le joueur perçoit par les réactions. Règle d'or : « ne jamais montrer les chiffres, montrer les conséquences ».
- Seuils : 0–1 Paria, 2–3 Suspect, 4–6 Reconnu (départ de tous les PJ, origine ±1), 7–8 Estimé (contrats rares, Posture Légendaire requise), 9–10 Légendaire (consulté, « chaque échec coûte double »).
- Aucun bonus chiffré direct : l'Honneur agit par **pression sociale** (haut : attentes et surveillance ; bas : méfiance, blocages).
- Variations indicatives : acte conforme au code régional +1 ; courage public reconnu +2 ; victoire honorable +1 ; parole tenue dans l'adversité +1 ; compromis douteux −1 ; humiliation ou trahison −2 ; transgression ouverte −3 à −5.
- Dans les conflits (L1 ch. 9 §VI) : rompre un accord signé −2 à −4 ; mentir sous serment (révélé) −2 à −5 ; contrainte physique en contexte diplomatique −1 à −3 ; agir contre son clan sans vote −1 à −4 ; fuir un duel rituel −2 à −5 ; trahir un informateur −1 à −3 et perte d'un nœud. Gains : tenir sa parole à prix élevé +1 à +3 ; gagner un duel devant un public influent +1 à +2 ; se révéler à son détriment par principe +1 à +3 ; protéger quelqu'un d'une pression injuste +1 à +2 ; tenir une annonce sans excuse +1. Les gains sont **locaux** (« la réputation voyage moins vite que les gens »).
- L2 ch. 2 : modificateur de DD social selon l'Honneur **dans la région** : 8–10 −3 ; 6–7 −1 ; 4–5 0 ; 2–3 +2 ; 0–1 +5 ; négatif +8 ou impossible. L'Honneur est « portatif » mais lu à travers la grille de la région ; −1 à −2 de perception si l'origine est en tension avec la région. Une région nouvelle ne connaît pas le personnage (Honneur nominal, réputation locale à zéro) ; première visite sans malus pour méconnaissance du code, malus à la deuxième.
- Le Retour au Clan est « le principal moment de mouvement de l'Honneur » (L1 ch. 4).

### 1.3 Les cinq axes culturels (L8 ch. 5)

| Axe | Valeurs | Impacts chiffrés ou nommés dans L8 |
|:--|:--|:--|
| 1 Combat | Devoir / Nécessité / Expression | Devoir : refuser un combat justifié −1 à −2 Honneur, bravoure ouvre des opportunités. Nécessité : fuir n'est pas un malus. Expression : bonus aux démonstrations spectaculaires, attire rivaux et autorités |
| 2 Mort | Sacrée / Pragmatique / Redoutée | Sacrée : tabous sur les corps (métiers de récupération, Forge). Pragmatique : aucune contrainte. Redoutée : décisions défensives coûteuses en Honneur |
| 3 Magie | Sacrée / Outil / Suspecte | Sacrée : magie sauvage mal vue, bonus d'Honneur au respect des protocoles. Outil : acceptation large. Suspecte : surveillance, enquêtes, restrictions d'accès |
| 4 Autorité | Légitime / Contractuelle / Rejetée | Légitime : bonus en milieu institutionnel, désobéir est une faute. Contractuelle : les accords priment les titres. Rejetée : conflits avec les forces officielles, solidarité interne |
| 5 Étranger | Hospitalité sacrée / Méfiance pragmatique / Rejet culturel | Méfiance : DD +1 avec les inconnus. Hospitalité : protection automatique des hôtes (exploitable). Rejet : zones fermées |

### 1.4 Les factions (L5 ; L4)

- **14 clans** (valeur fondamentale), **7 guildes** (métier), **8 ordres** (croyance), **ordres secrets** (Voile Noir, Masques de Verre, Chroniqueurs Oubliés, Fraternité des Sources, Morts de Velhor). On peut cumuler un clan, une guilde et un ordre : obligations contradictoires = source de tension (L5 ch. 2 §1). Obligations universelles d'un clan : défendre un membre en danger, ne pas agir contre ses intérêts fondamentaux, transmettre les valeurs.
- **Blocs d'influence** (L5 ch. 7) : Ordre Légal (Sceau Pourpre, Maisons Anciennes, Ordre du Flux, Archivistes Stellaires), Liberté Martiale (Lames Franches, Guilde Martiale, Navigateurs Gris), Nature, Commerce, Savoir, plus une zone grise (Cendres Liées, Porteurs de Cicatrices, Masques Brisés, Marches Frontalières). L2 ch. 9 donne une autre découpe en 6 blocs de régions (Ordre, Économique, Traditionnel, Mystique, Instable, Zone Noire), avec tensions Ordre contre Traditionnel (la loi écrite contre le serment oral).
- **Table des alliances et tensions** (14 clans, alliés et ennemis nommés) : reprise en données au §4.3.
- **Trois conflits latents** (route commerciale du Nord, Sanctuaire Scellé, Guildes et Failles) et **cinq conflits majeurs** (Trois Blocus, Purge des Sept Lignées, Guerre des Savoirs Brûlants, Crise des Failles Créées, Chute de la Confédération du Fleuve), chacun avec un « non-résolu » exploitable en quête.
- **Atlas** : chaque région a des Tensions actives et 3 Hooks ★. Régions exploitées ici : Cœur Impérial (Audit de la Saison Rouge, Contrat Incomplet, hooks Certification Impossible, Disparition de l'Arbitre, Passage par Geln), Cités Libres Marchandes (Guerre des Prix, Contrat de la Guilde de Chasse, hooks Clause Cachée, Trou du Réseau, Entrepôt Neutre), Hautes Terres Claniques (Vendetta de Cent Ans entre Dorvann et Kelrath, Contrat Extérieur, hooks Serment des Personnages, Vieille du Col, Mémoire Manquante).

### 1.5 La Trinité de Progression (L1 ch. 4 §7)

Toute chasse significative produit **simultanément** un **Acte** (le moment narratif), une **Trace** (marque visible et permanente : objet, cicatrice, titre) et une **Conséquence** (coût social : obligation, porte fermée, ennemi). Elle vaut aussi pour l'échec et pour les actes sociaux (négocier un passage plutôt que combattre). Qualité des matériaux selon la façon de vaincre : rapide Standard, long combat Supérieure, faiblesse élémentaire Élémentaire, parties rares préservées Rare, fuite de la créature aucun matériau et Tension +2.

### 1.6 Conflits entre livres rencontrés (une ligne chacun)

- Honneur : 0–10 (L1, L2 ch. 2) contre −25/+25 (L8) contre seuils « >25 » et « >15 » (L2, Royaumes de l'Ombre) : **conflit résolu par l'option 4** (0–10, 5 seuils). Les seuils de L2 pour les Royaumes de l'Ombre sont à réécrire (proposition : >25 devient ≥ 9, >15 devient ≥ 7).
- Réputation Publique, Honneur de Clan, Infamie (L8) contre « une seule jauge » (L1) : **conflit résolu par l'option 4** : l'Honneur reste la seule jauge morale ; la réputation devient une mémoire **par faction** dérivée du journal (§4), l'Infamie devient des **Marques** (Traces négatives, §4.5). Karma supprimé.
- Étiquettes d'Honneur : L1 (Paria, Suspect, Reconnu, Estimé, Légendaire) contre L2 (Vénéré, Respecté, Reconnu, Discret, Suspect) : **conflit résolu par l'option 4** : étiquettes de L1 et modificateurs de DD de L2 rattachés aux 5 seuils (§3.2).
- Attributs : L8 (Charisme, Sagesse, Intelligence) contre L1 : **conflit résolu par l'option 1** (PRE, VOL, ESP).
- L1 donne 42 points avec plage 3 à 12 à la création : valeur retenue pour les calculs de départ.
- « Sceau de l'Équilibre » (L4, ordre administratif du Cœur Impérial) contre « Clan du Sceau Pourpre » (L5) : deux entités à traiter séparément dans les données jusqu'à décision de krunt (question 9).
- Honneur visible ou masqué (L2 se contredit) : **choix de conception** : chiffre masqué, approximations affichées (§3.3).

---

## 2. Traduction en jeu vidéo : principes

| Règle du JDR | Devient | Pourquoi |
|:--|:--|:--|
| d20 + attribut + compétence contre DD | Marge M calculée, puis **barre de Tempo** (une tape) ou résultat automatique | Un jet caché est opaque au tactile ; une tape reste un geste de jeu, avec les mêmes probabilités |
| MJ qui lit l'Honneur et la région | Fonction `lecture_honneur(honneur, région, origine)` + tables de données | Le jeu doit être déterministe et testable |
| Enjeux cachés | Données `enjeu_cache` révélables par Lecture (Esprit) | C'est la vraie profondeur tactique de la joute |
| Public et témoins | Jauge de **Faveur** de 1 à 3 groupes d'assesseurs | Rend l'audience lisible et fait jouer les axes culturels |
| Réseau, Secrets, Exposition | Cartes de Secrets, contacts, jauge d'alerte à 4 icônes, rattachés aux quêtes | Pas de mini-jeu séparé : l'intrigue est une chaîne de quêtes (§5.6) |
| Honneur sans chiffre | Jamais de barre : attitudes de PNJ, prix, accès, rumeurs | Fidèle à L1 et L2, et plus simple à dessiner |
| Récit joué devant les anciens | Scène de composition de récit (§6) | C'est le cœur émotionnel du Retour au Clan |
| MJ qui improvise des dilemmes | Dilemmes écrits, étiquetés, à choix sans bonne réponse | Pas de MJ : tout est écrit d'avance |

Ce qui est **supprimé** : la Force comme jet social générique (remplacée par un tag « démonstration de puissance » valide seulement dans certaines cultures), le Réseau comme ressource narrative flottante (devient une liste de contacts à coûts écrits), la mise en scène improvisée des enjeux cachés. Ce qui est **automatisé** : le calcul des DD, des modificateurs d'Honneur et de région, la mémoire sociale, la propagation de réputation.

**Contraintes d'écran** (écran 360 px de haut, paysage supposé 640 x 360 ou plus large) : boutons d'action de 64 px de haut minimum, texte de dialogue en 2 lignes de 14 à 16 px de corps, au plus 4 choix visibles, jamais de saisie libre, tout geste faisable au pouce, aucune minuterie sur les choix (le Tempo est le seul élément à timing, et il a un mode automatique).

---

## 3. L'Honneur, la région et la lecture sociale

### 3.1 Valeurs retenues

Honneur entier 0 à 10, départ 5 (4 à 6 selon origine, ±1), stocké par personnage jouable. Jamais affiché en chiffre. Variations par événement du journal, bornées à ±5 par acte (borne de L8 reprise), arrondies, appliquées une seule fois par événement.

### 3.2 Seuils et modificateurs (à tester)

| Honneur | État | Modif. DD social (L2, rattaché) | Effets de jeu |
|:--|:--|:--:|:--|
| 9–10 | Légendaire | −3 | Consulté par les chefs ; **toute perte d'Honneur et de réputation est doublée** ; Appel à l'Honneur gratuit ; surveillance : un PNJ de faction « témoin » apparaît dans les scènes publiques |
| 7–8 | Estimé | −2 | Contrats rares ; PNJ partagent des infos ; Posture Légendaire possible ; Appel à l'Honneur disponible |
| 4–6 | Reconnu | 0 | Neutre. Position de départ normale |
| 2–3 | Suspect | +2 | Prix durcis (+10 % chez les factions « honorables »), infos qui circulent mal, une manœuvre offensive de moins en main |
| 0–1 | Paria | +5 | Portes fermées, clans refusent, certaines techniques d'École verrouillées ; les PNJ hostiles refusent la joute (position Fermée) ; seuls Voile Noir, Marches et zone grise commercent |

Autorité sociale (pour Appel à l'Honneur) = PRE + Honneur, soit 8 à 22 sur l'échelle de départ. Contrat avec L2 (« 8–10 : −3 ») : l'écart avec le seuil 7–8 à −2 est volontaire, pour garder 5 paliers.

**Lecture régionale** : `honneur_perçu = honneur + decalage_origine_région` où `decalage` vaut 0 par défaut, −1 ou −2 si l'origine du personnage est en tension avec la région (L2 ch. 2), +1 si région alliée au bloc d'origine ; borné 0 à 10. La réputation locale d'une région nouvelle démarre à 0 (« inconnu »), sauf propagation entre alliés (§4.4).

### 3.3 Comment le joueur le perçoit sans chiffre

1. **Première réplique de PNJ** : 5 variantes d'accueil par PNJ important, indexées sur le seuil perçu (une ligne chacune ; voir l'exemple L1 : « le forgeron t'a offert du thé »).
2. **Cadre du portrait** dans les dialogues : trait discret, 5 teintes (invisible en Reconnu). Optionnel (réglage Accessibilité).
3. **Onglet « Ce qu'on dit de vous »** dans le carnet : 3 rumeurs textuelles par région visitée, générées depuis le journal (§4). Aucune valeur.
4. **Signaux de monde** : prix, escortes, portes fermées, convocations.
5. **Confirmation avant dépense d'Honneur** : « Cela se saura. » (dépense de Composure, mensonge sous serment, rupture d'accord).

### 3.4 Codes régionaux jouables (L1 ch. 9 §VIII, traduits)

| Région | Effet sur la joute | Faute impardonnable (Honneur) | Axes dominants |
|:--|:--|:--|:--|
| Cœur Impérial | Cartes **Preuve** et **Procédure** : +2 à la marge ; les arguments émotionnels (Appel au public) −2 | Agir hors cadre institutionnel : −3 si découvert | Autorité Légitime, Magie Suspecte |
| Provinces Nobles | Autorité sociale compte double ; roturier : −1 à la marge de Pression | Exposer une Maison sans en porter les conséquences : −3 | Autorité Légitime |
| Cités Libres Marchandes | Concession tactique ne crée pas EN DETTE si l'accord est écrit ; chaque clause signée devant témoins = état ENGAGÉ | Rompre un accord signé : −2 à −4 | Autorité Contractuelle, Méfiance Pragmatique |
| Hautes Terres Claniques | **Démonstration de puissance** valide ; une joute peut se conclure en **duel physique** (passage en arène, §5.4) si les assesseurs le jugent nécessaire ; l'absence de position est une faute | Neutralité déclarée face à un conflit du clan : −2 à −3 | Combat Devoir, Mort Sacrée, Autorité Légitime, Hospitalité |
| Îles des Serments | **Le défi ne se refuse pas** : refus sans raison valide −2 à −5 ; défaite honorable +1 | Refuser un défi public | Combat Devoir |
| Déserts Rouges | **Silence** : manœuvre Silence à coût nul et +2 ; perdre le calme (Composure ≤ 0 en public) −2 | Perdre son calme | Méfiance Pragmatique |
| Royaumes de l'Ombre | Dévoilement trop tôt : −2 de marge et l'adversaire gagne un Secret ; le non-dit compte | Exposer son réseau ou un contact : −3 et perte du nœud | Autorité Rejetée |
| Théocraties Sacrées | Cartes **Doctrine** : un argument « hérétique » échoue automatiquement (marge −10) | Contredire officiellement la doctrine | Magie Sacrée, Autorité Légitime |

Les 12 autres régions : codes à écrire (question 8).

### 3.5 Effets des axes culturels dans le jeu (à tester)

Chaque personnage jouable a un **profil de 5 valeurs** (une par axe), tiré de son origine, modifiable à la création et par évolution narrative (L8 ch. 6). Chaque assesseur, chaque PNJ et chaque région a le même profil. Quand le joueur joue une carte, celle-ci porte 0 à 2 **étiquettes d'axe** (par exemple « Combat:Devoir » sur Démonstration de puissance). Réaction de l'assesseur : accord (+1 Faveur), neutre, désaccord (−1 Faveur). Cas particuliers :

- Axe 1 Devoir : refuser un combat/duel justifié coûte −1 Honneur (−2 aux Îles) ; Expression : +1 Faveur sur toute carte « spectaculaire », mais +1 Tension (attire l'attention).
- Axe 2 Sacrée : cartes « profiter des morts » (récolte, Forge sur un corps de PNJ) bloquées ou −1 Honneur ; Redoutée : choix de retraite coûteux en Honneur pour les PNJ de ce profil.
- Axe 3 Suspecte : une Technique d'École utilisée devant l'assesseur ajoute +1 Exposition ou lance une Enquête ; Sacrée : +1 Honneur quand le protocole est suivi (choix « suivre le rite » dans un dialogue).
- Axe 4 Légitime : Honneur peut commander d'obéir contre son intérêt (option verrouillée à bas profil) ; Contractuelle : une promesse écrite pèse plus qu'un titre.
- Axe 5 Méfiance pragmatique : DD +1 avec les inconnus (L8) ; Hospitalité : un hôte accueilli ne peut être attaqué par le clan, mais l'hospitalité crée une **obligation de réciprocité** (voir hook « Serment des Personnages »).

---

## 4. Réputation par faction

### 4.1 Principe

L'Honneur est la mémoire globale ; la **réputation de faction** est la mémoire d'une structure précise (Pierres Hautes, Marchands Libres, Administration des Pratiques, Voile Noir…). Elle est **dérivée du journal d'événements** : on peut la reconstruire à tout moment en rejouant les événements (donc pas de triche, pas de désynchronisation avec la table). Elle ne remplace pas la Trinité : chaque Conséquence peut produire un `rep_delta`.

### 4.2 Échelle et paliers (à tester)

Réputation entière de **−60 à +100** par couple (personnage, faction). Départ 0. Les gains au-dessus de 59 exigent l'Honneur requis par la faction (colonne « portail »).

| Palier | Valeur | Prix d'achat | Prix de vente matériaux | Contrats (rang max) | Accès | Quêtes et services |
|:--|:--:|:--:|:--:|:--|:--|:--|
| Banni | ≤ −40 | refus | refus | aucun | zones de la faction : arrestation ou attaque (exclusion formelle ou exil) | quêtes « Traque » contre le joueur, prime |
| Hostile | −39 à −15 | ×1,40 | ×0,70 | aucun | restreint, escorte imposée (mise à l'écart : DD +3) | demandes de réparation (amendes, restitutions) |
| Méfiant | −14 à −1 | ×1,15 | ×0,90 | ◆ | accès public seulement (désaveu discret) | PNJ coupent court |
| Inconnu | 0 à 14 | ×1,00 | ×1,00 | ◆ à ◆◆ (CR ≤ 4) | public | quêtes d'entrée |
| Connu | 15 à 34 | ×0,97 | ×1,03 | ◆◆ (CR ≤ 9) | locaux de faction | informations d'entrée, quêtes de faction niveau 1 |
| Estimé | 35 à 59 | ×0,92 | ×1,08 | ◆◆◆ (CR ≤ 15) | boutique rare, archives publiques | quêtes de faction niveau 2, PNJ partagent infos |
| Allié | 60 à 84 | ×0,85 | ×1,15 | ◆◆◆◆ | quartiers privés, équipement de faction, refuge | quêtes de faction niveau 3, soutien dans les joutes (un Appui PNJ) |
| Intime | 85 à 100 | ×0,80 | ×1,20 | tous, contrats d'héritage | conseil, sceau, rôle d'**Ambassadeur de clan** au Bastion | quêtes de fin d'arc ; obligations aussi plus lourdes (le monde exige) |

Portail d'Honneur : Sceau Pourpre, Maisons Anciennes, Pierres Hautes, Ordre du Flux, Guilde Martiale : Honneur ≥ 4 pour Estimé, ≥ 7 pour Allié. Marchands Libres, Mille Voix, Navigateurs Gris : aucun portail. Voile Noir et Masques de Verre : pas de palier affiché, remplacés par des **Dettes** (§4.6).

Correspondance avec l'exclusion de L1 : Désaveu discret (Méfiant), Mise à l'écart (Hostile, DD +3), Exclusion formelle (Banni, désavantage dans la zone d'influence), Exil (Banni plus Marque d'infamie, zone interdite). Un acte de réhabilitation écrit (quête) est la seule voie de retour au-dessus de Hostile.

### 4.3 Données de faction (extrait, issu de L5 ch. 7 §2)

```json
{
  "id": "pierres_hautes", "type": "clan", "bloc": "traditionnel",
  "regions": ["hautes_terres_claniques"],
  "valeurs": {"patience": 2, "serment_tenu": 2, "protection_vulnerables": 2,
              "ostentation": -2, "improvisation_flamboyante": -1, "recit_modeste": 1},
  "ton_prefere": {"sobre": 1.5, "modeste": 1.5, "fier": 0.5, "eloquent": 0.8},
  "portail_honneur": {"estime": 4, "allie": 7},
  "allies": ["maisons_anciennes", "guilde_martiale"],
  "tensions": ["lames_franches", "maree_profonde"],
  "mefiants": ["mille_voix"]
}
```

| Faction | Alliés | Tensions |
|:--|:--|:--|
| Sceau Pourpre | Maisons Anciennes, Ordre du Flux | Lames Franches, Voile Noir |
| Lames Franches | Guilde Martiale, Navigateurs Gris | Sceau Pourpre, Maisons Anciennes |
| Mille Voix | Marchands Libres, Ordres Prophétiques | Maisons Anciennes, Voile Noir |
| Pierres Hautes | Maisons Anciennes, Guilde Martiale | Lames Franches, Marée Profonde |
| Cendres Liées | Clans Ancestraux, Veilleurs Sylvestres | Sceau Pourpre, Voile Noir |
| Porteurs de Cicatrices | Guilde de Chasse, Soigneurs | (aucune) |

Les 14 lignes complètes sont dans L5 ch. 7 §2 : à importer par script dans `donnees/factions.json`.

### 4.4 Formules (à tester)

```
delta = base_evenement * poids_faction[type_evenement]
        * (1.25 si temoins >= 3) * (0.5 si temoins == 0, "acte non témoigné")
        * (2 si honneur >= 9 et delta < 0)          # "chaque échec coûte double"
rep_faction += clamp(round(delta), -15, +15)         # plafond par événement
propagation : allies de la faction  += round(delta * 0.25)   # "les régions alliées partagent leurs infos"
              tensions de la faction += round(-delta * 0.15)
decroissance : rumeurs négatives (source = Réputation publique) reviennent de 1 point vers 0 tous les 10 jours de jeu ;
               Traces (titres, Marques) ne décroissent jamais
région nouvelle : rep = 0 (inconnu), puis propagation depuis les régions alliées déjà visitées
```

Exemples de `base_evenement` : chasse de Contrat honorée +6 chez le mandant ; chasse de Nécessité réussie +4 chez le clan protégé ; gagner une joute publique +5 ; promesse rompue au mandant −8 (et l'Honneur −2) ; trahir un informateur −10 au Voile Noir (et nœud perdu) ; Récit exemplaire +8 chez le clan, voir §6.

### 4.5 Marques (ex-Infamie)

Une **Marque** est une Trace négative permanente (« Briseur de serment », « Profanateur du Cairn », « Délateur »). Effets : plafonne la réputation des factions qui y sont sensibles (par exemple Briseur de serment : Hautes Terres et Îles des Serments plafonnées à Méfiant) ; ne se retire que par une quête de rédemption (L8 ch. 8). Remplace l'Infamie 0–10 de L8 sans ajouter de jauge.

### 4.6 Dettes, Secrets, Contacts

- **Dette** (L1 ch. 9 §VII.b) : `{id, creancier, type: faveur|dette_de_sang|pacte|compte_ouvert, gravite 1-3, origine_evenement, echeance_jours?, etat: active|reclamee|honoree|rompue}`. Une dette réclamée devient une quête à échéance ; rompue : Honneur −2 à −4 selon le type et nouvelle Marque possible. Pas de jauge : un écran liste.
- **Secret** : `{id, sujet, valeur 1-3, fragilite_jours, exposition: inconnue|soupconnee|connue, usages: [reveler, menacer, manoeuvrer]}`.
- **Contact (nœud de Réseau)** : `{id, nom, position, fiabilite 1-3, cout_texte, etat: actif|compromis|perdu}`. Activer un nœud coûte toujours quelque chose d'écrit.

### 4.7 Écran « Mémoires » (carnet)

Liste des factions rencontrées : icône, nom, **palier en mots** (pas de valeur numérique), ce qu'il débloque (une ligne), bandeau « Dette en cours » ou « Marque ». Détail : historique des 5 derniers événements (lignes du journal). Onglet « Ce qu'on dit de vous » (rumeurs par région).

---

## 5. Les joutes verbales (système tactile)

### 5.1 Vue d'ensemble

Une **Joute** est une confrontation tour par tour, jouable en 2 à 4 minutes, jamais plus de 8 manches en moyenne. Tout le temps de réflexion est libre ; le seul geste chronométré est la tape du Tempo (désactivable). Trois idées structurent l'écran : **Aplomb** (ressource, Composure de L1), **Faveur** (le public), **Pression** (le contexte).

### 5.2 Écran de joute (360 px de haut)

```
+--------------------------------------------------------------+ y=0
| [Portrait PJ 64]  APLOMB ######----  17/17      Faveur  (-)--o--(+)   |
|  etats: EXPOSE                                   [assesseurs 3 x 24px]|
| [Portrait PNJ 64] APLOMB ########--  21/21   Pression: [!!.] clan   |  y=72
+--------------------------------------------------------------+
|   Bulle de l'adversaire (2 lignes) + icone d'INTENTION (couleur)    |  y=148
|   Bulle du joueur apres choix (2 lignes)                            |
+--------------------------------------------------------------+
| [Carte 1 ] [Carte 2 ] [Carte 3 ] [Carte 4 ]      [Lecture 2] [Nom] |  y=260
|  144x64     144x64     144x64     144x64          Appui  Rupture    |
+--------------------------------------------------------------+ y=360
```

- **Aplomb** : barre qui se vide de gauche à droite ; passé 0 apparaît une zone rouge de longueur Volonté (la zone « perd pied », L1). Valeur numérique en petit : l'Aplomb est une jauge de scène, pas l'Honneur.
- **Faveur** : curseur de −5 à +5 (agrégat des assesseurs), détail au toucher long. Chaque assesseur est une pastille (hostile, tiède, favorable).
- **Pression** : 0 à 3 icônes selon le type (clan, institution, publique) ; intensité 0 à 3 correspondant à Légère/Modérée/Forte/Totale (DD 10/15/20/25).
- **Intention** : l'adversaire affiche l'icône de sa prochaine manœuvre (couleur : rouge Présence, bleu Esprit, vert Volonté) **seulement si le joueur a utilisé une Lecture** ; sinon une icône « ? » (voir 5.3).
- Boutons de 144 x 64 px pour les cartes (zone de toucher ≥ 44 dp), jamais plus de 4 cartes en main.

### 5.3 Boucle d'une manche

1. **Initiative** : celui dont `PRE + ESP` est le plus haut commence en attaquant (égalité : le défenseur du conflit, tradition de L1). La manche suivante les rôles s'inversent.
2. **Phase Attaque** (le joueur attaque) : choisir une carte offensive parmi la main, éventuellement consulter la Lecture, éventuellement invoquer un Appui.
3. **Phase Réplique** (le PNJ attaque) : l'icône d'intention est affichée si lue ; le joueur choisit une réponse parmi 4 boutons fixes (Tenir, Rediriger, Appel au public, Concession) ou Rupture.
4. **Tempo** : barre de 1,2 s avec fenêtre colorée ; une tape. Les jets du PNJ sont de vrais d20 tirés d'une graine enregistrée dans le journal (reproductibilité pour les tests).
5. **Résolution** (animation 1,5 s) : dégâts d'Aplomb, état social, changement de Faveur, texte.
6. **Épreuve de Tenue** tous les 3 manches si Pression ≥ 1 : marge VOL + compétence contre DD de la Pression ; échec = une carte de la main est grisée pour la manche suivante (« cède partiellement : temporise »).
7. **Fin** : voir 5.7.

**Lecture** : le joueur dispose de `floor(ESP / 4)` jetons de Lecture par joute (ESP 9 : 2). Un jeton au choix : révéler l'intention du PNJ pour la manche, **ou** révéler un enjeu caché (une ligne du PNJ passe de « ? » à son texte), **ou** révéler la Faille du PNJ (attribut faible : ses réponses sont −2 de marge contre les manœuvres de l'attribut visé). C'est l'usage de l'Esprit comme attribut de lecture (L1).

### 5.4 Cartes de manœuvre (le « Répertoire »)

Le joueur arrive avec un **Répertoire** de 8 cartes maximum (4 en main, pioche déterministe : cartes possédées dans un ordre fixé par l'ordre de sélection, pas de hasard). Toutes les manœuvres de L1 existent ; les coûts de recharge remplacent le coût de ressource que le livre ne définit pas.

| Carte | Attribut | Effet de base (valeurs de L1, ×k) | Recharge | Étiquettes |
|:--|:--:|:--|:--:|:--|
| Pression directe | PRE | Aplomb adverse −`floor(PRE/4)`×k | 1 | Combat si « démonstration » |
| Dévoilement | ESP | −`floor(ESP/3)`×k si la cible ne peut pas réfuter ; révèle un enjeu | 2 | Preuve |
| Appel à l'Honneur | PRE+Hon. | La cible choisit : céder sur la position ou perdre de l'Honneur ; −`floor((PRE+Hon.)/6)`×k sinon | 3 | Autorité |
| Retournement | ESP | −`floor(ESP/4)`×k et **EXPOSÉ** | 2 | Preuve |
| Isolement | PRE | Désavantage (marge −4) à toutes les réponses jusqu'à la fin de la manche suivante ; Faveur −1 chez la cible | 3 | Public |
| Silence | VOL | Opposé : le premier à parler perd 3×k Aplomb (6) | 2 | Déserts +2 |
| Preuve (carte d'objet) | ESP | +2 de marge, consommée ; issue d'un Secret ou d'un document | usage unique | Procédure |
| Démonstration de puissance | FOR | Pression directe ×1,25, valide seulement où l'axe Combat est Devoir/Expression, −1 à −3 Honneur ailleurs | 3 | Combat |

**Réponses fixes** (les quatre boutons du bas) :

| Réponse | Attribut | Effet de base | Contre favorable |
|:--|:--:|:--|:--|
| Tenir sa position | VOL | Réduit la perte d'Aplomb de `floor(VOL/4)`×k, minimum 1 par coup ; sans jet | Pression directe (réduction ×2) ; ×0,5 contre Dévoilement |
| Redirection | ESP | Marge adverse −3 pour sa manœuvre actuelle | Dévoilement, Retournement |
| Appel au public | PRE | Pas de réduction d'Aplomb, mais Honneur et Faveur inchangés quoi qu'il arrive ; +1 Faveur sur succès | Isolement, Appel à l'Honneur |
| Concession tactique | — | Récupère `floor(ESP/4)`×k Aplomb ; état EN DETTE (dette narrative écrite dans le journal) | Silence (évite la perte de 6) |
| Rupture | — | Fin immédiate ; coût d'Honneur régional (§3.4) | — |

**Recalibrage k = 2 (à tester)** : les divisions de L1 (PRE÷4 et ESP÷3 avec attributs 3 à 12) donnent 1 à 4 points par coup contre une Composure de 12 à 24, donc 10 à 15 manches. Multiplier par k = 2 vise 5 à 8 manches ; à ajuster par prototype.

### 5.5 Résolution chiffrée

```
DD_pos        = 10 (Favorable), 15 (Neutre), 20 (Hostile) ; Fermé = pas de joute
DD_duel       = 10 + VOL_defenseur + competence_defenseur           # moyenne du d20 adverse, L1 jet oppose
DD_eff        = DD_duel (ou DD_pos pour une scene simple) + mod_honneur(§3.2) + mod_code(§3.4) + mod_pression
                + 3 (Redirection adverse) + 1 (Meffiance pragmatique, inconnu)
M (marge)     = Attribut + Competence + Bonus - DD_eff
Bonus         = Preuve +2, Appui +1 a +3, Avantage +4, Desavantage -4
                (Avantage/Desavantage approximent "lancer deux fois" ; sert aussi a Isolement et aux Pressions)
P(reussite)   = clamp(5 * (21 + M), 5, 95) %                        # equivalent exact du d20
```

Fenêtres du Tempo (largeur de la barre = 100 %) :

| Zone | Largeur | Condition (équivalent d20) | Effet |
|:--|:--:|:--|:--|
| Éclat (crit.) | 5 % au centre de la zone nette | 20 naturel | Dégâts ×1,5 ; chance d'Honneur +1 ; l'info favorable se répand : +1 réputation chez le public |
| Net | `P(réussite) − tendue − 5` | marge ≥ 5 | Dégâts pleins, aucun coût |
| Tendue | 25 % (ou moins si P < 25) | marge de 0 à 4 (option 8) | Dégâts pleins, **plus un coût écrit** : dette, témoin gênant, ou Faveur −1 |
| Échec | le reste | marge < 0 | Aucun dégât ; l'attaquant perd 1 Faveur ; la tentative est vue |
| Dérapage | 5 % au bord | 1 naturel | Aplomb du joueur −`dégâts/2`, état EXPOSÉ, information défavorable exposée |

Mode **Auto** (réglage d'accessibilité et mode lent) : pas de tape, résultat selon la marge (M ≥ 5 net, 0 à 4 tendue, < 0 échec) avec un tirage seedé pour Éclat et Dérapage. Risque assumé (voir Q3) : un joueur adroit réalise plus de succès que le d20 sur de grandes fenêtres et moins sur de petites ; la fenêtre minimale de 5 % et une vitesse qui monte avec le DD (1,2 s à DD ≤ 15, 0,9 s à DD ≥ 25) limitent la dérive.

**Dégâts d'Aplomb** = `base_manœuvre` × (1,5 Éclat, 1 Net/Tendue, 0 Échec) × (1,25 contre une Faille lue) × (0,5 si la réponse adverse est un contre favorable). Perte d'Aplomb ≥ 50 % de l'Aplomb de départ en une manche : état DÉSTABILISÉ (marge −4 à la défense suivante).

**Dépense d'Honneur** (bouton « Nom ») : −1 Honneur, +VOL Aplomb ; une seule fois par joute ; visible par les assesseurs (Faveur −1 chez les profils Autorité Rejetée ou Expression). Confirmation obligatoire.

### 5.6 Les trois attributs, l'origine, le clan, l'Honneur : récapitulatif d'intervention

| Élément | Intervient dans | Détail chiffré |
|:--|:--|:--|
| Présence | Attaque : Pression, Isolement, Appel au public ; Initiative | Dégâts PRE÷4 ; Tempo de ces cartes |
| Volonté | Aplomb de départ, Tenir, Silence, Épreuves de Tenue, dépense d'Honneur | Aplomb = VOL + ESP ; zone « perd pied » de longueur VOL |
| Esprit | Aplomb de départ, Dévoilement, Retournement, Redirection, Lecture | Jetons = ESP÷4 ; dégâts ESP÷3 ou ÷4 |
| Origine | Profil des 5 axes, Honneur de départ ±1, décalage de lecture de la région | §3.2, §3.5 |
| Clan / faction | Palier de réputation : DD du PNJ de la faction, accès à l'**Appui** de faction, cartes exclusives (« Sceau » du Sceau Pourpre, « Chœur » des Mille Voix, « Pierre » des Pierres Hautes) | Palier ≥ Allié : +1 carte au Répertoire ; membre affilié : +2 de marge sur les arguments typiques du clan (inspiré des « avantages mécaniques » de L5) |
| Honneur | DD (§3.2), accès à Appel à l'Honneur, dépense d'Aplomb, double perte à 9–10 | §3.2 |
| Compétence sociale | Marge | 0 à 5 selon le métier (niveau du métier ÷ 6, arrondi bas) |

### 5.7 Fin de joute et conséquences

Fin : Aplomb ≤ −VOL (cède), condition narrative (exemple : 3 assesseurs sur 4 convaincus), Rupture, ou tiers (un PNJ arbitre intervient, événement scripté). Un écran de **Conséquences** montre la **Trinité** : l'Acte (une phrase), la Trace (titre, objet, cicatrice sociale), la Conséquence (dette, porte fermée, ennemi) ; les variations d'Honneur ne sont **pas** affichées en chiffres (§3.3). États ENGAGÉ et EN DETTE persistent dans le journal jusqu'à résolution narrative ; l'Aplomb revient à 100 % après un repos (une nuit de jeu).

### 5.8 Aides : alliés, familiers, factions

- **Autre personnage jouable (Appui)** : un seul Appui par joute, choisi avant la joute parmi les PJ présents. Trois formes : **Témoigner** (ESP : apporte une carte Preuve, +2 de marge à une carte), **Se tenir derrière** (VOL : la prochaine perte d'Aplomb est réduite de `floor(VOL_allié/4)`×k), **Parler à ma place** (PRE : une carte jouée avec les stats de l'allié, mais son Honneur est en jeu). Chaque forme coûte une des manches de l'allié (il ne peut plus être Appui pendant 3 manches).
- **Familier** : une action par joute, réservée aux familiers dont l'état de relation est Dressée (fiable à 100 %) ou Habituée (70 % : sinon incident, Faveur −1, Honneur −1 si public). Sauvage : refusé. Selon le rôle déjà défini dans le roster :

| Rôle du familier | Action dans la joute | Limites |
|:--|:--|:--|
| éclaireur | Révèle un enjeu caché, sans jeton de Lecture | Une fois |
| pisteur | Révèle la Faille du PNJ ou localise un Secret (en quête d'intrigue) | Hors joute |
| signal | +1 Faveur chez un assesseur au choix (la présence d'un animal impressionne ou attendrit) | Régions à axe Magie Suspecte : −1 |
| assistant de combat / monture | Démonstration de puissance sans coût d'Honneur (+25 % à Pression) | Seulement Hautes Terres, Îles, Provinces ; ailleurs −1 à −3 Honneur |
| bête de somme / transport | Présent ou caution : sert d'offre en Négociation (équivaut à une concession gratuite) | Une fois |

Exemples pour la démo : Alizade (conditionné, éclaireur) comme révélateur d'enjeu ; Dorgane (affectif, assistant de combat) pour la démonstration de puissance dans les Hautes Terres ; Charivari (signal) pour l'appel au public.
- **Faction** : palier Allié ou plus : un PNJ de la faction vient en Appui (une carte supplémentaire en main) ; palier Hostile : un assesseur de plus est défavorable d'office.

### 5.9 Variantes (5)

| Variante | Cadre | Condition de victoire | Ressources spéciales | Durée visée |
|:--|:--|:--|:--|:--:|
| **Négociation** | Table de contrat, 2 camps, 3 à 4 clauses | Somme des clauses ≥ +3 ; l'autre camp quitte à ≤ −3 | Curseurs de clause −2 à +2 ; chaque succès déplace une clause d'un cran (tendue : un cran, plus un coût) ; concessions échangeables | 4 à 6 manches |
| **Procès / jugement** | 3 à 5 assesseurs, un accusateur et un défenseur | Majorité des assesseurs convaincus à la fin (ou Aplomb adverse ≤ 0) | Faveur par assesseur ; cartes Preuve issues du journal (par exemple « témoin du Cairn ») | 6 à 8 manches |
| **Défi d'honneur** | Rituel reconnu par une région ; peut finir en duel physique | Aplomb adverse ≤ 0, ou accord des assesseurs ; refuser coûte −2 à −5 Honneur | Étiquettes Combat ; passage en arène (§5.10) si les assesseurs le décident | 4 à 6 manches |
| **Interrogatoire** | Un interrogateur, un détenu ; rôle du joueur au choix (interrogateur ou interrogé) | Interrogateur : révéler 3 nœuds de Vérité ; interrogé : tenir 6 manches sans en révéler plus de 1 | Nœuds de Vérité (3 à 5 fragments cachés) ; Dévoilement les ouvre | 5 à 7 manches |
| **Persuasion de PNJ** | Scène sociale simple, sans jauge | 1 à 3 tapes de Tempo contre DD de position | Aucun Aplomb ; échec = position se ferme, coût écrit | 20 à 40 s |

**Passage en arène** : si le défi d'honneur doit se conclure en combat (Hautes Terres, L1 ch. 9 §VIII), la scène se charge dans l'arène latérale en mode « duel rituel » (pas de monstre, règles de Livre III, Vitalité plutôt que Composure). Hors démo.

### 5.10 États sociaux dans l'interface

EXPOSÉ, ISOLÉ, DÉSTABILISÉ, ENGAGÉ, EN DETTE : pictogrammes 16 x 16 sous le portrait, avec libellé au toucher long. EXPOSÉ social et EXPOSÉ de combat (L1 ch. 7, effet différent) sont deux états séparés dans les données (`social.expose` contre `combat.expose`).

---

## 6. Intrigue et pression politique : traduction

L'intrigue n'est pas un mini-jeu : c'est une **chaîne de quêtes** (exploration en 3/4, plateforme de profil pour l'infiltration, dialogues) qui s'achève par une joute.

| Phase L1 | Forme de jeu | Jets remplacés |
|:--|:--|:--|
| Identification | Quête d'exploration et de dialogues : collecter des Secrets (3 à 5 cartes) | Lectures d'Esprit : conditions d'obtention de la carte |
| Infiltration | Niveau de plateforme de profil (discrétion) ou dialogue avec identité sociale | Seuil d'**alerte** à 4 icônes (œil) |
| Manipulation | Dialogue à choix : utiliser un Secret en Révéler / Menacer / Manœuvrer (effets différents) | Marge simple |
| Résolution | Joute finale | DD de départ modifié par la table de L1 : 4/4 phases −6, 3/4 −3, 2/4 0, 1/4 +3, 0/4 +6 et adversaire prévenu (Aplomb adverse +20 %) |

**Exposition** : exception volontaire à « ne jamais montrer les chiffres » : un jeu d'infiltration a besoin d'un retour visible. Elle apparaît comme 4 icônes d'œil (Faible, Modérée, Élevée, Critique), sans valeur numérique. Conséquences : Élevée, le PNJ cible prend des dispositions (une carte offensive en moins en joute finale) ; Critique, la faction fait un mouvement public (quête de réaction forcée). Réduire l'Exposition : un intermédiaire (consomme un contact), couvrir ses traces (séquence de dialogue), laisser du temps (−1 niveau par 7 jours de jeu sans action visible).

**Pressions** (clan, institution, publique) : icônes de Pression en joute (§5.2) et malus de DD hors joute (public : DD +3 dans la région ; institution : désavantage aux actes illégaux ; clan : désavantage contre les intérêts du clan, jusqu'à ce que le joueur réussisse une Épreuve de Tenue).

**Signes d'escalade** (table d12 de L1) : exécutée à chaque « tick de tension régionale » (une fois par 3 jours de jeu avec une tension active). Chaque ligne produit un événement mineur (message, rumeur, PNJ qui évite le joueur) avec un drapeau `escalade_n`. À 3 signes sans réaction, une quête de crise est déclenchée. Hors démo.

---

## 7. Le Retour au Clan (Récolte, Récit, Rituel) comme scène de jeu

### 7.1 Place dans la boucle

Quatrième temps de la Boucle de Chasse. Obligatoire, jamais sauté, mais **court** : 3 à 5 minutes au total. Se joue au hameau ou au Bastion, dans l'exploration en 3/4 puis en écrans dédiés.

### 7.2 Ce que la chasse envoie (télémétrie de combat)

La chasse (arène latérale) écrit un enregistrement `compte_rendu_chasse` à la fin ; le Retour en tire les **Faits** racontables.

```json
{
  "chasse_id": "ch_2028_0012", "creature": "dorgane", "type_designation": "contrat",
  "mandant": "pierres_hautes", "region": "hautes_terres_claniques",
  "duree_s": 412, "phases_atteintes": 2, "fuite_creature": false,
  "defaite_par": ["usure"],                   // rapide | usure | elementaire | rare_preservee | fuite
  "faiblesse_elementaire_exploitee": false, "parties_rares_intactes": ["cornes"],
  "etat_creature_a_la_fin": "effondree",
  "coups_encaisses_pour_allie": [{"par": "pj2", "pour": "pj4", "n": 1}],
  "coup_decisif": "pj3", "plan_echoue_puis_adapte": true,
  "familiers_utilises": ["alizade"], "territoire_respecte": true,
  "tension_delta": 0
}
```

### 7.3 Les trois temps

**Récolte** (45 à 60 s) : écran de matériaux. Qualité calculée à partir de `defaite_par` (table de L1 : Standard, Supérieure, Élémentaire, Rare ; fuite : aucun matériau, Tension +2, le Retour devient une scène de mauvaise nouvelle). Le joueur répartit les lots par glisser-déposer entre **le mandant**, **l'offrande du clan**, **la Forge personnelle** (5 emplacements max). Le métier Dépeceur (L7) débloque 1 emplacement et un lot « Rare » supplémentaire ; les parties que le mandant avait exigées (clause de contrat) sont marquées d'un sceau. Impact : réputation du mandant et Honneur (offrande des restes : +1 Honneur dans les cultures Mort Sacrée).

**Récit** (90 à 120 s) : la scène centrale. Le PNJ évaluateur (l'ancien, le mandant) demande « Racontez. ». Le joueur compose :
1. **Choisit 3 faits** parmi ceux qui sont proposés (jusqu'à 6, tirés du compte rendu) ; chaque fait a une étiquette (cohésion, protection, faiblesse exploitée, parties rares préservées, rapidité, patience, plan échoué, sacrifice, coup décisif).
2. **Choisit un ton** : Modeste, Sobre, Fier, Éloquent.
3. **Peut omettre ou embellir** (embellir ajoute un fait **faux** de valeur +2 mais crée un Secret : si un témoin existe, découverte à la prochaine visite : Honneur −2 et réputation −10 chez le clan).
Les réactions sont montrées en gestes (3 sprites d'animation : hochement, silence, détournement) et en lignes de texte. Aucune valeur affichée.

**Rituel** (30 à 45 s) : variante régionale, une décision. Hautes Terres : **veillée** (le récit complet est entendu : un fait de plus est évalué mais le ton est figé) ou **offrande des restes** ; Cités Libres : **signature** du compte rendu devant témoins (ENGAGÉ sur ce qui a été dit) ; Cœur Impérial : **dépôt aux Archives** (procédure : la précision prime sur le ton) ; Mille Voix : **chant public** (récit retransmis : réputation à large échelle mais déformable). La **forge cérémonielle** (L1 ch. 5, +2 d'Honneur collectif au lieu de +1) est proposée si une pièce de Forge est possible.

### 7.4 Formule du Récit (à tester)

```
valeur_fait(f, clan)   = clan.valeurs[f.etiquette]               # -2 a +2
ton_mult(ton, clan)    = clan.ton_prefere[ton]                    # 0.5 a 1.5
score_recit            = somme(valeur_fait * ton_mult) sur les 3 faits
                         + 1 si offrande conforme + 1 si rituel respecte
                         - 3 si fait faux decouvert
delta_honneur          = clamp(round(score_recit / 2), -3, +3)    # Retour = principal mouvement d'Honneur
delta_rep_clan         = round(score_recit * 2.5)                 # -15 a +15
delta_rep_mandant      = +6 si clauses du contrat honorees, -8 sinon
```

### 7.5 Comment la manière de chasser change la réaction

| Manière (télémétrie) | Hautes Terres (Pierres Hautes) | Cités Libres (Marchands Libres) | Cœur Impérial (Archives) |
|:--|:--|:--|:--|
| Rapide (tuée avant épuisement) | Respect neutre : « Efficace. » | Apprécié : coût bas, délais respectés | Neutre ; la procédure compte plus |
| Long combat d'usure | **+** : patience = preuve de sérieux | Neutre : retard facturé | Neutre |
| Faiblesse élémentaire exploitée | + : intelligence de la chasse | + : matériaux Élémentaires, meilleur prix | + : savoir utile, archivé |
| Parties rares préservées | + : respect du corps ; ++ si exigées | **++** : valeur marchande | + si clause de contrat |
| Fuite de la créature | − : honte, clan en attente | − : contrat non rempli | − : défaillance au registre |
| Coup pris pour un allié | **++** (protection des vulnérables) | Neutre | Neutre |
| Récit arrogant (Fier) | **−** (humilité valorisée) | + (confiance affichée) | − |
| Territoire respecté (créature en état Territoire, partie éloignée plutôt que tuée) | + si le clan la considère protégée ; − si menace | − (non rentable) | Selon décret |

### 7.6 Sortie : Trinité et journal

À la fin, une **carte de Trinité** (illustrée, un sprite d'estampille) : Acte (phrase issue du compte rendu), Trace (titre ou objet : par exemple « Porte-Fardeau », forge de la corne), Conséquence (dette de réciprocité, nouvelle quête, rivalité de clan). Écrit dans le journal (§9).

---

## 8. Système de dialogues à choix

### 8.1 Choix technique

Fichiers JSON par scène (`donnees/dialogues/<id>.json`), lus par un **runner maison** Godot (200 à 300 lignes) plutôt qu'un addon : on garde la main sur drapeaux, journal et export vers StoryForge. Textes dans des tables de localisation (`fr.csv`) : le JSON ne contient que des clés.

### 8.2 Structure de données

```json
{
  "id": "aurath_audit_01", "version": 3, "region": "coeur_imperial",
  "noeuds": {
    "n01": {
      "locuteur": "inspecteur_orsane", "texte": "aurath_audit_01.n01",
      "variantes_accueil": {"paria": "n01_p", "suspect": "n01_s", "reconnu": "n01", "estime": "n01_e", "legendaire": "n01_l"},
      "conditions": [{"flag": "w.audit_lance", "valeur": true}],
      "choix": [
        {"id": "c1", "texte": "aurath_audit_01.c1", "etiquettes": ["autorite:legitime"],
         "requiert": [{"stat": "ESP", "min": 8}, {"honneur_band_min": "reconnu"}],
         "cout": {"honneur": 0},
         "effets": [
           {"set_flag": "c.{pj}.a_menti_audit", "valeur": true},
           {"ajoute_secret": "secret_faux_registre"},
           {"honneur_delta": -1, "visible": false, "raison": "mensonge_institution"}
         ],
         "suite": "n02a"},
        {"id": "c2", "texte": "aurath_audit_01.c2", "effets": [{"lance_joute": "joute_audit_01"}], "suite": "fin_joute"}
      ]
    }
  },
  "fins": {"libre": {"journal": "evt_audit_libre"}, "enregistre": {"journal": "evt_audit_enreg"}}
}
```

Types d'effets pris en charge : `set_flag`, `incr_flag`, `rep_delta {faction, delta}`, `honneur_delta {delta, visible:false}`, `tension_delta`, `ajoute_secret`, `ajoute_dette`, `ajoute_contact`, `donne_objet`, `lance_joute`, `lance_quete`, `etat_social`, `journal {acte, trace, consequence}`, `marque {id}`.

### 8.3 Drapeaux

Espaces de noms : `w.` monde (partagés entre les 4 personnages), `c.<pj>.` personnage, `q.<quete>.` quête, `f.<faction>.` faction. Valeurs booléennes, entières ou chaînes. Règles : un drapeau n'est écrit que par un effet ; une condition lit sans effet ; un journal de modifications est conservé (pour rejouer).

### 8.4 Lecture des conditions

Conditions disponibles : drapeau, statistique minimale, bande d'Honneur (via la lecture régionale), palier de réputation, objet, Secret, Dette, Marque, famille de familier (Dressée/Habituée), profil d'axe. Les choix bloqués apparaissent grisés avec la cause **sans chiffre** (« Vous manquez de poids ici », « On vous connaît mal »).

### 8.5 Flux de données vers le journal PocketBase

Collections proposées (voir aussi les autres domaines pour `chasses`) :

| Collection | Champs principaux |
|:--|:--|
| `evenements` | `id`, `joueur`, `personnage`, `date_jeu`, `date_reelle`, `type` (chasse, joute, dialogue, quete, retour, rituel), `region`, `acte` (texte + ids), `trace` (json), `consequence` (json), `honneur_delta` (int, masqué côté joueur), `rep_deltas` (liste), `flags_set`, `temoins` (liste d'ids PNJ), `graine_rng`, `visible_table` (bool), `version_schema` |
| `reputations` | `personnage`, `faction`, `valeur`, `palier`, `derniere_maj`, `source_evenements` (ids) |
| `dettes` | voir §4.6 |
| `secrets` | voir §4.6 |
| `contacts` | voir §4.6 |
| `marques` | `personnage`, `marque_id`, `evenement_id`, `levee` (bool) |
| `etat_dialogues` | `personnage`, `scene_id`, `noeud`, `drapeaux_locaux` |

**Règle** : le journal est la seule source de vérité pour l'Honneur et la réputation ; les tables `reputations` sont des caches recalculables. Un événement n'est jamais modifié, seulement complété par un événement correctif. `visible_table` permet au MJ humain de lire le journal et de décider quelles Conséquences reviennent à la table (principe de L1 : « le monde change parce que vous y avez existé »).

---

## 9. Exemples complets de scènes jouables (chiffrés)

Convention : PJ-A « Diplomate » : PRE 10, VOL 8, ESP 9 ; compétence sociale 3 (niveau de métier 18 ÷ 6) ; Honneur 5 ; Aplomb 17 ; Lecture 2. PJ-B « Chasseur » : PRE 6, VOL 9, ESP 7 ; compétence 1 ; Honneur 5 ; Aplomb 16 ; Lecture 1. Facteur k = 2.

### 9.1 Scène 1 : L'Audit de la Saison Rouge (Cœur Impérial, Aurath) : Interrogatoire à rôle inversé

**Ancrage** (L4) : l'Administration des Pratiques audite les utilisateurs de magie ; visites nocturnes, certains ont disparu. Hook lié : « La Disparition de l'Arbitre ». Région : Cœur Impérial (code : procédure, Preuve +2, émotion −2).

**Situation** : le joueur (PJ-A) est convoqué au Bureau des Pratiques, au sixième cercle (étrangers). Il est inscrit comme chasseur, mais il a hébergé et caché Mère Ysaut, guérisseuse d'Éther non enregistrée (contact, fiabilité 2). L'inspecteur Orsane (PNJ inventé) veut un nom : **enjeu déclaré** = « mise à jour des registres » ; **enjeu caché** = il doit rendre un nom avant la fin de la saison (quota), n'importe lequel (révélable par Dévoilement/Lecture). Tension en jeu : l'Honneur contre l'efficacité (L1 ch. 9 §VI).

| PNJ | PRE | VOL | ESP | Compétence | Aplomb | Position | Faille | Postures (cycle) |
|:--|:--:|:--:|:--:|:--:|:--:|:--:|:--|:--|
| Orsane | 9 | 10 | 11 | 3 | 21 | Hostile (DD pos 20) | Quota (Pression × 1,25 s'il est lu) | Dévoilement, Pression, Retournement, Dévoilement |

DD_duel du joueur contre Orsane = 10 + 10 + 3 = 23. Modificateurs : Honneur 5 (0) ; code impérial : Preuve +2 ; Pression institutionnelle intensité 2 (DD +3 sur les actes illégaux). Variante : **Interrogatoire**, joueur interrogé : doit tenir **6 manches** en révélant au plus 1 des 3 nœuds de Vérité (N1 : « l'hébergement » ; N2 : « le nom de Mère Ysaut » ; N3 : « le lien avec l'arbitre disparu »).

**Répertoire du joueur** : Pression directe, Dévoilement, Retournement, Silence ; Preuve « Certificat de transit en règle » (+2) ; réponses fixes.

**Manche type** (valeurs de dégâts calculées avec k = 2) :

| Manche | Attaquant | Action | Marge et résultat | Effet |
|:--:|:--|:--|:--|:--|
| 1 | Orsane (initiative : PRE+ESP 20 contre 19) | Dévoilement : « Vous avez logé quelqu'un cette semaine. » (ESP 11 → `floor(11/3)`×2 = 6) | Joueur choisit **Redirection** (marge Orsane −3) ; jet d20 d'Orsane tombe en Tendue | Aplomb joueur −6 → 11 ; Redirection transforme l'issue en Tendue : Orsane obtient un état EN DETTE inversé (il doit une courtoisie) |
| 2 | Joueur | **Lecture** (jeton 1/2) : enjeu caché révélé (« quota »). **Retournement** : DD 23, M = 9 + 3 + 2 (Preuve) − 23 = −9 → P = 60 % ; Tempo : fenêtre nette 30 %, tendue 25 % | Tape en Net : −`floor(9/4)`×2 = −4 ; Orsane EXPOSÉ | Aplomb Orsane 21 → 17 ; Faveur +1 (le greffier note) |
| 3 | Orsane | Pression directe (PRE 9 → `floor(9/4)`×2 = 4) | Joueur **Tenir** (contre favorable, ×2 : réduction `floor(8/4)`×2×2 = 8, borné par min 1) | Aplomb joueur : −1 (11 → 10) |
| 4 | Joueur | **Dévoilement** sur le quota (cible ne peut réfuter) : 6 ; M = 9 + 3 − 23 + 5 (Avantage car EXPOSÉ) = −6 → P = 75 % ; Tendue | Aplomb Orsane 17 → 11 ; coût de la Tendue : « le greffier a tout entendu » (témoin) | Faveur −1 |
| 5 | Orsane | Retournement, joueur choisit **Concession tactique** (sacrifier un nom mineur : un guide non enregistré, pas Ysaut) | Récupère `floor(9/4)`×2 = 4 ; état EN DETTE ; **Honneur −1** (trahir un informateur : −1 à −3) | Aplomb joueur 14 |
| 6 | Joueur | **Silence** (opposé) : première parole perd 6 | Orsane parle en premier (Pression de quota) | Aplomb Orsane 11 → 5 ; DÉSTABILISÉ |
| 7 | Orsane | Rupture ou Compromis scripté : « Nous noterons que l'audit est clos pour vous, sous réserve d'un nom. » | Joueur gagne si Aplomb Orsane ≤ 0 ou 3 nœuds protégés | Fin |

**Issues** (Trinité) :

| Issue | Condition | Acte | Trace | Conséquence | Réputation et Honneur |
|:--|:--|:--|:--|:--|:--|
| **Libre** | Ysaut protégée, aucun nom donné | Audit tenu sans trahir | Titre « Parole tenue » (+1 Honneur chez Pratiques inconnues) | Orsane garde une dette envers le joueur ; Administration des Pratiques surveille | Honneur +1, Pratiques +4, Marchands Libres +2 (alliés) |
| **Libre au prix d'un nom mineur** | Concession (manche 5) | Un guide sacrifié | Dette (« compte ouvert ») : le guide revient | Perte d'un contact (Passage par Geln : plus de guide fiable) | Honneur −1, Pratiques +3 |
| **Enregistrement forcé** | Aplomb joueur ≤ 0 à la manche 7 | Défaite | Fiche d'enregistrement (Trace négative légère) | Pratiques : audit annuel obligatoire ; Ysaut disparue ou fuit | Honneur −1 (Compromis douteux), Pratiques −2 |
| **Détention** | Cède à −8 | Capitulation | Aucune | Quête d'évasion ou de défense | Honneur −2, Pratiques −8, Voile Noir +4 (aide) |

**Secret** potentiel : si le joueur a menti (carte « faux registre »), le Secret est créé : Orsane peut le Menacer plus tard.

### 9.2 Scène 2 : Les Hautes Terres Claniques : Défi d'honneur à la Vallée des Serments

**Ancrage** (L4) : hook « Le Serment des Personnages ». En entrant par la passe tenue, le groupe a accepté l'hospitalité du clan Vorath ; le clan réclame maintenant une réciprocité dangereuse (battre les troupeaux d'un col occupé par une créature). Refuser fermerait les passes Vorath. Tension active liée : la Vendetta de Cent Ans (Dorvann, Kelrath) rend les autres clans méfiants.

**Variante** : Défi d'honneur sous forme de jugement devant le Conseil des Anciens. Le Gardien des Mémoires (porte-parole des morts, valeur légale) interroge : « Avez-vous honoré l'hospitalité ? » Le joueur veut réduire l'obligation (négocier une réciprocité moindre) sans offenser.

| Assesseur | Faveur de départ | Axes | Effet |
|:--|:--:|:--|:--|
| Ancien Brann (Vorath) | −1 | Combat Devoir, Mort Sacrée, Autorité Légitime, Méfiance pragmatique | DD +1 (Étranger) ; adore les cartes Combat |
| Ancienne Tessa (neutre) | 0 | Combat Nécessité, Autorité Contractuelle, Hospitalité | Apprécie les arguments de réciprocité écrite |
| Gardien Orvak (mémoires) | −1 | Mort Sacrée, Autorité Légitime, Magie Sacrée | Exige des Preuves (inscriptions du Cairn) ; Dévoilement −2 s'il est « sans témoin » |

Adversaire : Gardien Orvak (PRE 8, VOL 11, ESP 10, compétence 2, Aplomb 21, Position Hostile). DD_duel = 10 + 11 + 2 = 23. Honneur perçu du joueur : 7 (« guerrier fiable ») dans cette région → −2 (L2 : Estimé). Si l'origine du joueur est en tension (Cités Libres, Autorité Contractuelle opposée aux clans), −1 supplémentaire.

**Cartes clés** : **Démonstration de puissance** (valide ici, ×1,25) avec Dorgane en Appui (Combat Devoir : +1 Faveur chez Brann) ; **Preuve : inscription du Cairn** (+2) ; **Appel à l'Honneur** (Autorité sociale 10 + 7 = 17 ; −`floor(17/6)`×2 = −4 ou choix de céder) ; **Silence** (valorisé : la lenteur est preuve de sérieux). Réponse « Appel au public » moins efficace (L1 : pas de position publique neutre : « l'absence de position est une faute »).

**Règle locale** : à la manche 6, si Faveur ≤ −2 et Aplomb du joueur ≥ 50 %, les assesseurs proposent la **conclusion physique** : si le joueur accepte, passage en duel rituel (hors démo : résolution par une dernière tape de Tempo à DD 20 comme « duel abrégé »). Refuser : −2 Honneur (Neutralité = faute).

**Issues** :

| Issue | Condition | Acte | Trace | Conséquence | Réputation et Honneur |
|:--|:--|:--|:--|:--|:--|
| **Quittance** | Faveur ≥ +2 à la fin et Aplomb Orvak ≤ 0 | Réciprocité réduite à une escorte | Titre « Hôte entendu » | Vorath accorde passage ; Dorvann se méfie (alliés/tensions) | Honneur +2 (gagner un duel verbal devant un public influent +1 à +2), Vorath +8, Pierres Hautes +3, Dorvann −2 |
| **Dette acceptée** | Faveur ≥ 0, Aplomb joueur ≥ 5 | Compromis | Dette « faveur » envers Vorath | Quête du col, à échéance 7 jours | Honneur 0, Vorath +4 |
| **Dette de sang** | Faveur < 0 ou Aplomb joueur ≤ 0 | Défaite honorable | Marque temporaire « Hôte redevable » | Quête obligatoire dangereuse, sans négociation ; refus = Briseur de serment | Honneur +1 (défaite honorable valorisée), Vorath +2, plafond Méfiant si refus |
| **Fuite du Conseil** | Rupture | Rupture publique | Marque « Briseur de serment » | Passes Vorath fermées au groupe | Honneur −3, Vorath −15, Hautes Terres Méfiant |

### 9.3 Scène 3 : Les Cités Libres : La Clause Cachée (Négociation au Bureau des Signes)

**Ancrage** (L4) : hook « La Clause Cachée » : copie d'un vieux contrat « égarée » aux archives de la Ligue ; un employé payé pour qu'elle reste introuvable. Tension : La Guerre des Prix (deux membres votants de la Ligue sont parties prenantes).

**Variante** : Négociation. Le joueur négocie avec le courtier Vauzel (PNJ inventé, Marchands Libres) pour obtenir la copie **légalement** (le mandant est signataire) sans que la Ligue ne reconnaisse de dette. 4 clauses à fixer :

| Clause | Départ | Intérêt du joueur | Intérêt de Vauzel (caché) |
|:--|:--:|:--|:--|
| Accès | 0 | Copie intégrale | Retarder de 6 mois |
| Prix | 0 | Moins de 200 pièces | Marge pour un tiers |
| Garantie | 0 | Dépôt en Entrepôt Neutre | Empêcher que la copie sorte |
| Exclusivité | 0 | Aucune | Garder une exclusivité sur la route du nord |

| PNJ | PRE | VOL | ESP | Compétence | Aplomb | Position | Faille |
|:--|:--:|:--:|:--:|:--:|:--:|:--:|:--|
| Vauzel | 8 | 8 | 12 | 4 | 20 | Neutre (DD pos 15) | « Rompre un accord signé » : il tient à son nom ; si ENGAGÉ, ses réponses −2 |

DD_duel = 10 + 8 + 4 = 22. Honneur 5 (0). Les Cités Libres : la parole devant témoins est inviolable : chaque clause fixée devant le greffier du Bureau est ENGAGÉE (aucun retour).

**Règle de Négociation** : chaque succès déplace une clause d'un cran vers le joueur (−2 à +2, +2 = totalement favorable) ; la **Tendue** déplace d'un cran **et** crée une contrepartie écrite (la clause adverse recule d'un cran) ; l'Échec recule d'un cran vers l'adversaire. Concession tactique = un cran offert sur une clause mineure en échange d'un cran gagné sur une autre (pas de coût d'Honneur ici). Victoire : somme ≥ +3 ; à ≤ −3 le courtier se retire (nouvelle joute impossible pendant 3 jours).

**Révélations** : une Lecture ou Dévoilement sur « Garantie » révèle que Vauzel a été payé par le Bureau pour retarder (preuve par un reçu) : carte Secret « Reçu de paiement » (valeur 2, fragilité 5 jours). Utilisation : Menacer (clause Accès +2 immédiat, mais Marchands Libres −3 et un ennemi) ou Révéler (scandale : réputation Ligue −10, Mille Voix +4).

**Issues** :

| Issue | Condition | Acte | Trace | Conséquence | Réputation et Honneur |
|:--|:--|:--|:--|:--|:--|
| Copie obtenue proprement | Somme ≥ +3, aucun Secret utilisé | Accord signé devant témoins | Titre « Signataire sûr » | Dette reconnue réduite ; la Ligue note le nom du joueur | Honneur +1, Marchands Libres +6 |
| Copie par chantage | Secret Menacer | Obtenue par la menace | Secret à risque ; Dette « compte ouvert » | Vauzel cherche à neutraliser le levier ; Ligue se méfie | Honneur −1 (compromis douteux), Marchands Libres −3, Mille Voix +2 |
| Copie par scandale | Secret Révéler | Mise à nu publique | Trace « Dénonciateur » | Quête : protection du témoin ; Ligue déstabilisée | Honneur +1 (se révéler à son détriment par principe, si le joueur s'expose), Ligue −10 |
| Échec | Somme ≤ −3 | Courtier se retire | Aucune | Quelqu'un attend à la sortie (hook « L'Entrepôt Neutre ») | Honneur 0, Marchands Libres −1 |

### 9.4 Scène 4 (mini) : Passage par Geln (Persuasion de PNJ)

Un guide non enregistré demande un prix élevé et un transport secret. Position Neutre (DD 15). PJ-B : PRE 6, compétence 1, Honneur 5 : M = 6 + 1 − 15 = −8 → P = 65 %. Fenêtre : Net 35 %, Tendue 25 %, Éclat 5 %, Dérapage 5 %. Tendue : accord obtenu, mais le colis est lourd : (Dette de faveur + Exposition +1 à l'entrée). Net : prix baissé de 25 %. Échec : la position se ferme (prix ×1,5, un autre guide à trouver). Aucun Aplomb ; durée 20 s. Illustre le coût le plus bas de contenu : 6 lignes de texte.

---

## 10. Données et interfaces : récapitulatif

### 10.1 Écrans

| Écran | Rôle | Éléments clés | États principaux |
|:--|:--|:--|:--|
| Dialogue à choix | Scènes parlées, zones d'exploration | Bulle 2 lignes, 4 choix, portrait avec cadre d'Honneur facultatif | affichage, choix, effet, fin |
| Préparation de joute | Avant une joute | Répertoire (8 cartes), Lecture, Appui, familier, rappel des enjeux déclarés | éditer, valider |
| Joute | §5.2 | Aplomb, Faveur, Pression, cartes, Tempo | intro, manche (attaque/réplique), Tempo, résolution, épreuve de tenue, fin |
| Conséquences | Après toute joute et tout Retour | Carte de Trinité : Acte, Trace, Conséquence | affichage, continuer |
| Retour au Clan | §7 | Récolte (glisser-déposer), Récit (3 faits et ton), Rituel (choix) | trois étapes séquentielles |
| Mémoires (carnet) | §4.7 | Factions, paliers en mots, Dettes, Secrets, Contacts, rumeurs | lecture seule |
| Réglages d'accessibilité | Joute | Tempo auto, vitesse lente, cadre d'Honneur, taille du texte | toujours disponible |

### 10.2 Transitions de la joute

`EXPLORATION → PRÉPARATION → INTRO → [MANCHE → TEMPO → RÉSOLUTION → ÉPREUVE_TENUE?]* → FIN → CONSÉQUENCES → EXPLORATION`. Une Rupture saute directement à FIN. Un tiers (événement) peut insérer INTERVENTION avant FIN.

### 10.3 Modèle de données de joute

```json
{
  "id": "joute_audit_01", "variante": "interrogatoire", "region": "coeur_imperial",
  "role_joueur": "interroge", "manches_max": 8,
  "pnj": "inspecteur_orsane",
  "pnj_stats": {"PRE": 9, "VOL": 10, "ESP": 11, "competence": 3, "aplomb": 21,
                "position": "hostile", "faille": "quota",
                "cycle": ["devoilement", "pression", "retournement", "devoilement"]},
  "assesseurs": [{"id": "greffier", "faveur": 0, "axes": {"autorite": "legitime", "magie": "suspecte"}}],
  "pression": {"type": "institution", "intensite": 2},
  "enjeux": {"declare": "mise_a_jour_registres", "cache": "quota_a_remplir"},
  "noeuds_verite": ["hebergement", "nom_ysaut", "lien_arbitre"],
  "fins": {"libre": "evt_audit_libre", "enregistre": "evt_audit_enreg", "detention": "evt_audit_det"}
}
```

Gabarit de PNJ de joute par rang (valeurs de départ, à tester) :

| Niveau de PNJ | Attributs principaux | Compétence | Aplomb | Position typique |
|:--|:--:|:--:|:--:|:--|
| Commun | 5 à 6 | 1 | 10 à 12 | Favorable ou Neutre |
| Notable | 7 à 8 | 2 | 14 à 16 | Neutre |
| Expert | 9 à 10 | 3 | 18 à 21 | Neutre ou Hostile |
| Chef | 10 à 11 | 4 | 22 à 24 | Hostile |
| Maître | 12 | 5 | 26 à 30 | Hostile |

### 10.4 Courbe d'équilibrage de départ (à tester)

Objectif : un joueur moyen (PRE/VOL/ESP 8, 9, 9 ; compétence 2) gagne ~75 % des joutes de son niveau, ~45 % contre un niveau au-dessus, ~15 % contre deux niveaux au-dessus ; durée médiane 6 manches ; moins de 10 % des joutes se terminent par Rupture. Indicateurs de télémétrie à enregistrer : durée de joute, nombre de manches, usage de Lecture, taux de Tempo auto, répartition des issues, usage de la dépense d'Honneur.

---

## 11. Coût de production réaliste et ce qu'il faut couper

### 11.1 Estimation (une seule personne avec l'aide de l'IA ; heures de krunt, hors temps d'attente d'outils)

| Poste | Démo | Version complète | Remarques |
|:--|:--:|:--:|:--|
| Moteur de joute (logique, données, tests sans interface) | 30 h | 45 h | Calculs et règles très déterministes : se testent bien en script |
| Interface de joute (écran, cartes, jauges, barre de Tempo, animations) | 45 h | 65 h | Le poste le plus risqué : lisibilité sur 360 px |
| Assets d'interface pixel art (cadres, 16 icônes d'état et de manœuvre, jauges) | 15 h | 30 h | Via PixelForge, avec nettoyage manuel |
| Portraits et expressions (PJ x4 et PNJ clés, 3 expressions chacun) | 15 h | 50 h | À grouper avec le domaine personnages |
| Runner de dialogues, conditions, effets, localisation | 30 h | 40 h | Le même runner sert partout dans le jeu |
| Réputation (données, formules, carnet, hooks prix et contrats) | 15 h | 30 h | Dépend du journal et de la boutique |
| Retour au Clan (scène, télémétrie, composition du Récit, rituel) | 30 h | 45 h | Une scène à habiller par clan |
| Journal PocketBase (collections, synchro, export StoryForge/CharForge) | 20 h | 35 h | Partagé avec les autres domaines |
| Équilibrage et essais | 15 h | 40 h | À étaler |
| **Total technique** | **~215 h** | **~380 h** | Soit de 9 à 15 semaines à 14–24 h par semaine pour la démo |
| Écriture (démo : ~10 000 mots ; complet : 120 000 à 180 000 mots) | 30 h | 400 h et plus | Le vrai mur : voir ci-dessous |

Répartition du texte de la démo : bibliothèque générique des manœuvres (11 manœuvres x 3 tons x 2 voix x 2 variantes ≈ 130 lignes, 2 500 mots), 2 joutes uniques (≈ 1 200 mots chacune : intro, 3 postures, enjeux, issues), 1 Retour au Clan (≈ 1 500 mots : 8 faits x 3 réactions et rituel), 2 hubs de dialogue (≈ 3 000 mots).

**Réduction du coût d'écriture (principal levier)** : les joutes se construisent sur un **gabarit** : le texte d'une manche est composé à partir de la manœuvre, du ton et d'un petit nombre de « sujets » du PNJ (3 mots-clés), plus une réplique unique par PNJ et par phase. On passe d'environ 150 lignes à 40 lignes par joute.

### 11.2 À couper pour la démo (16 mars 2028)

| À garder | À couper ou reporter |
|:--|:--|
| Le runner de dialogues et les drapeaux | L'intrigue en 4 phases (garder uniquement un Secret et une Exposition à 2 niveaux dans une quête) |
| **Une** joute complète (Défi d'honneur en Hautes Terres, scène 9.2) | Procès à 5 assesseurs, Interrogatoire, Négociation à 4 clauses (garder la Persuasion) |
| Persuasion de PNJ (scène 9.4) | Appui d'un autre personnage et de la faction |
| **Un seul** familier en aide (éclaireur) | Les 5 rôles de familier |
| Réputation sur **3 factions** (Pierres Hautes, Vorath, Marchands Libres) avec paliers 1 à 5 | Propagation entre alliés, Marques, Dettes complexes (garder une dette par scène) |
| **Un** Retour au Clan (Pierres Hautes) : Récolte, Récit à 3 faits, Rituel (veillée) | 14 clans et leurs rituels propres, forge cérémonielle |
| Honneur en données, aucune barre, 5 phrases d'accueil sur 3 PNJ | Cadre de portrait par seuil, rumeurs générées |
| Journal : `evenements` seulement, avec Trinité | Collections `secrets`, `contacts`, `marques` |
| Tempo en mode Auto **et** en mode barre | Duel physique en fin de joute, signes d'escalade (d12) |

Ce périmètre tient dans ~120 à 150 h de technique et ~25 h d'écriture, soit un budget compatible avec la contrainte (14 à 24 h par semaine).

### 11.3 Feuille de route par versions

| Version | Contenu | Cible indicative |
|:--|:--|:--|
| v0.1 (démo) | §11.2 | 16 mars 2028 |
| v0.2 | Scène 9.1 (Audit) en Interrogatoire, Négociation (9.3), Appui d'un PJ, 5 rôles de familier, Dettes et Secrets | printemps 2028 |
| v0.3 | Propagation de réputation, Marques, intrigue en 4 phases sur 2 régions, Retour au Clan pour 4 clans | été 2028 |
| v0.4 | Procès, duel physique en conclusion de défi, signes d'escalade, rumeurs générées | automne 2028 |
| v1.0 | Codes des 20 régions, 14 clans, 7 guildes, ordres secrets en dettes, escalade complète | à décider |

---

## 12. Questions ouvertes (à trancher par krunt)

1. **Quatre personnages jouables : une joute à plusieurs ?** Si les quatre sont joués par quatre joueurs en même temps, la joute (1 contre 1) devient un spectacle pour trois. *Recommandation* : joute individuelle, les autres en Appui (une action chacun). Si le jeu est solo, le « personnage joué » est choisi au début de chaque quête.
2. **Réputation par personnage ou par groupe ?** *Recommandation* : par personnage (cohérent avec origines et clans différents), avec 50 % du delta partagé aux compagnons présents (la table de L1 parle d'Honneur collectif sans le définir).
3. **Tempo (barre) ou calcul pur ?** La barre ajoute de l'adresse et rend les attributs moins déterminants. *Recommandation* : proposer les deux, **Auto par défaut** à la démo pour rester fidèle aux statistiques, barre activable ; et mesurer.
4. **Le chiffre d'Honneur est-il affiché ?** L2 se contredit. *Recommandation* : jamais affiché ; cinq paliers en mots dans le carnet seulement si krunt veut de la lisibilité (option « Reflets », désactivée par défaut).
5. **La réputation de faction remplace-t-elle l'Honneur régional de L2 ?** *Recommandation* : oui : l'Honneur reste global, la mémoire régionale vit dans la réputation de faction (évite un champ Honneur par région).
6. **Infamie et Marques** : accepter de remplacer l'Infamie de L8 par des Marques ? *Recommandation* : oui, pas de jauge supplémentaire.
7. **L'intrigue en 4 phases, avec Exposition visible ?** C'est la partie la plus chère. *Recommandation* : la couper de la démo ; à terme, la réaliser comme chaîne de quêtes plutôt que comme système.
8. **Codes régionaux** : L1 n'en décrit que 8 sur 20 régions. Qui écrit les 12 autres ? *Recommandation* : un gabarit de code (4 lignes : faute impardonnable, effet de joute, axes, particularité), généré en brouillon par script, relu par krunt, une région par version.
9. **« Sceau de l'Équilibre » (Atlas) contre « Sceau Pourpre » (L5)** : même institution ou deux ? *Recommandation* : deux entités liées (l'ordre administratif et le clan juridique), à confirmer.
10. **Enjeu d'échelle (honnêteté)** : ce système est le plus gros pari du jeu (aucune référence, 100 000 mots de texte à terme, interface dense sur 360 px). *Recommandation* : ne pas viser l'ensemble ; livrer le Retour au Clan et une joute, **juger du plaisir** avant de produire la suite ; si la joute ne plaît pas, les dialogues à choix et la réputation suffisent à porter l'univers.
11. **Duel physique à l'issue d'un défi** : valide pour les Hautes Terres et les Îles, mais ce serait un mode de plus. *Recommandation* : hors démo ; une seule tape de Tempo comme duel abrégé en attendant.
12. **Langues et ton du texte** : les joutes exigent des répliques courtes (≤ 90 caractères par ligne pour 2 lignes). *Recommandation* : fixer cette contrainte dans StoryForge dès le premier brouillon.

---

## 13. Ponts avec les autres domaines

- **Chasses (arènes latérales)** : produire le `compte_rendu_chasse` du §7.2 (durée, manière de vaincre, parties rares intactes, coups pris pour un allié, fuite, état de la créature) ; sans lui, le Récit n'a pas de faits.
- **Journal PocketBase / outils** : collections du §8.5 et export JSON pour CharForge/StoryForge ; schéma de `evenements` commun à tous les domaines.
- **Personnages et progression** : Honneur de départ, profil des 5 axes, compétence sociale (niveau de métier ÷ 6), Autorité sociale ; métiers à statut social (Dépeceur, Ambassadeur) ; Posture Légendaire à Honneur ≥ 7.
- **Familiers et dressage** : états Sauvage/Habituée/Dressée et rôles (éclaireur, pisteur, signal, assistant, bête de somme) comme conditions et effets en joute.
- **Économie, boutique et contrats** : lecture de la réputation de faction pour les prix, le rang maximal des contrats et l'accès aux boutiques rares.
- **Monde et quêtes** : Tensions actives et hooks de l'Atlas comme source de scènes ; tick de tension régionale et signes d'escalade.
- **Bastion** : Ambassadeur de clan (Ancrage 13), Quartier Diplomatique (activité Négocier), Salle du Conseil (scène politique majeure).
- **Interface et direction artistique** : cadres, icônes d'état et de manœuvre, portraits à 3 expressions, lisibilité à 360 px (règle des 64 px de zone de toucher).
