# REPRISE : index de tout ce qui a été produit (arrêt du 2026-10-06)

**À quoi sert ce fichier.** krunt met le travail en pause pour réfléchir. Quand il redonnera ce dossier (ou ce fichier) à Claude, la consigne est : **« Lis `docs/00-REPRISE.md`, puis fais-moi un rapport complet (fichier par fichier, décisions, questions ouvertes, contradictions restantes), en étant franc. »** Tout est dans le dépôt `krunt3/crs`, branche `ccr-ac8b98b5-dozun7`.

Franchise, avant tout : krunt a lui-même jugé que la trame s'éloigne de la trame de base et se complexifie trop. À la reprise, **partir de `docs/trame/00-decisions.md` (ses mots à lui) et simplifier**, plutôt que d'enrichir les documents 02 à 10.

---

## 1. Le projet en deux phrases
Un même jeu sur deux supports : **CRS** (JDR de table / VTT, univers Palmaria, 10 livres Markdown) et **Jeu B** (jeu Android 2D pixel art, Godot 4, type Monster Hunter : exploration 3/4, quêtes de plateforme, chasses en arène à défilement), reliés par un journal d'événements PocketBase (Acte / Trace / Conséquence). Démo jouable visée : **16 mars 2028**, démo = **Krunt seul**.

## 2. Décisions de krunt (résumé ; le détail et ses mots exacts sont dans `docs/trame/00-decisions.md`)
- Krunt3 = krunt = le héros, jouable par lui ; PNJ pendant les phases de JDR (un autre MJ pourra prendre le relais). Les fiches sont des **essais**, pas à suivre à la lettre.
- Au jeu : chaque joueur joue **son seul personnage**, en solo, dans un monde ouvert, **intrigue commune avec des différences** ; les trois autres **apparaissent comme PNJ** dans son monde. Ils arrivent **tous au moment du cataclysme, par un portail magique**.
- Le monde se souvient des actes (Marques) ; il y aura des jets de dés dans le jeu (réactions, dressage, persuasion), pas dans le combat.
- Antagoniste : **Ordre du Flux** (vérité en couches). Krunt3 : **Frères de l'Épreuve** (« Ordre du Jugement » = surnom). Pascal : **Sceau Pourpre** (clan) ; son ordre est **non tranché** (voir §6). Taranis : **Chasseur-Pisteur + Cartographe**, part avec un bagage de départ. Pascal : seulement l'attaque de base avant ses bombes.
- **« Quittance des Noms » supprimée** (coût et rite). **« La Veillée » et « le Rappel » rejetés** aussi : le rite et la technique restent sans nom. Coût du pacte : **la Braise seule, pas de Gage**.
- **Clans** : chaque clan a son propre honneur et sa propre façon de penser ; la légende du phœnix : les anciens la connaissent, les jeunes non ; les clans qui protègent ou étudient le phœnix sont dans les livres, à appuyer dans la recherche **StoryForge** (case ouverte, rien d'inventé).
- Rôles « **deux appelés, un tombé par accident** » gardés (modifiable). Après le cataclysme, tous recommencent à zéro, sauf le tombé (Taranis, niveau supérieur proposé : 3).
- Phœnix « plus » (contrat aux Ravins de Keth, etc.) : **reporté**, hors trame immédiate.
- Régions : celles de l'Atlas, sans surnoms. Lieu d'arrivée : Marches Frontalières (session en cours).
- Règles (10 conflits des livres) : options proposées dans le formulaire « Cadrage Forge », pas toutes tranchées (voir §5).

## 3. Index des fichiers du dépôt

### 3.1 Audit des livres (`docs/audit/`)
| Fichier | Contenu |
|---|---|
| `notes-lecture-livres.md` | notes détaillées livre par livre (10 livres) |
| `synthese-livres.md` | verdict, **10 décisions de règles à trancher**, points solides, risques (noms Monster Hunter, Dragons Anciens) |
Limite à garder en tête : le Livre III (Bestiaire, 35 000 lignes) a été analysé par script, pas lu mot à mot ; 8 autres livres de krunt n'ont jamais été vus.

### 3.2 Monstres
| Fichier | Contenu |
|---|---|
| `docs/design-monstres.md` | règles de création des nouveaux monstres (nom neuf, trait unique, ≤ 8,7 m pour un sprite de boss) |
| `docs/roster-monstres.md` | roster lisible (272 entrées dont 106 familiers, 6 petits assistants) |
| `donnees/monstres/*.json` | 12 familles : crochues, ailees_a, ailees_b, terrestres, leviathans, cramponnees, cuirassees, fauves, dragons, phoenix, chasse, sociales |
| `donnees/monstres/correspondance.json` | lien nouveau id ↔ ancienne fiche (**usage interne uniquement**, ne jamais publier) |
| `donnees/monstres/migration_cle_id.json` | ancien slug → nouveau cle_id pour CharForge |
| `outils/valider_monstres.py` | validateur (0 problème au dernier passage) |
À noter : 17 familiers sans DD ; les Dragons Anciens sont traités en cinématiques (pas de sprite de boss).

### 3.3 Mécaniques du jeu (`docs/mecaniques/`)
`00-vue-densemble`, `01-chasse-et-combat`, `02-bastion-forge-artisanat`, `03-ecoles-metiers-arbres`, `04-diplomatie-joutes-reputation`, `05-clan-monde-economie-familiers`, `06-monde-vivant-memoire-et-des` (Marques, attitudes, dés visibles). Elles adaptent les livres en mécaniques de jeu vidéo. La règle « pas de PNJ copies » du 06 a été remplacée par la décision « les trois autres sont des PNJ ».

### 3.4 Applications et outils
| Fichier | Contenu |
|---|---|
| `docs/applications-forge.md` | inventaire des applications Forge et leur état |
| `docs/analyse-editeurs-cartes.md` | MapForge/LevelForge face à Godot / LDtk / Tiled (protocole de test LDtk d'une journée) |
| `donnees/test-cartes/` | kit de test CC0 32×32 (tuiles, sprites, entités, aperçu) |
| `outils/mesure_sprite.py`, `outils/simu_combat.py` | mesure de sprites ; simulation de combat (modèles de dégâts) |

### 3.5 Trame (`docs/trame/`) ; **à simplifier à la reprise**
| Fichier | Statut |
|---|---|
| `00-decisions.md` | **fait foi** : journal des décisions de krunt |
| `10-trame-v3.md` | trame consolidée la plus récente (prémisse, 4 personnages, Flux, Braise, clans, PNJ, chronologie, démo, questions ouvertes) |
| `01`…`09` | versions intermédiaires : persos, trame v1 (« Le Réceptacle »), correspondance aux livres, équilibrage, antagoniste, entité/pacte, essais de simulation, fiches v2 + briefs de sprites, revalidation (43 contradictions). Plusieurs portent un bandeau « remplacé par 10 » |

### 3.6 Documents des sessions précédentes (non retravaillés ici)
`docs/livres-crs-vers-jeu-b.md`, `bible-graphique.md`, `etude-jeux-reference.md`, `generation-procedurale.md`, `prompts-personnages.md`, `test-pixellab.md`, `docs/cours-godot/00…13` (cours Godot), `donnees/palette_*.json` (palettes chasseur-wyverne).

### 3.7 Hors dépôt (non conservés, à ne pas compter dessus)
- **Formulaire « Cadrage Forge »** (artifact claude.ai, version 11) : https://claude.ai/artifact/39FAb3YXejMvPcmQ1kGRJr ; il contient les réponses aux sections règles, mécaniques, zones/chasses/quêtes, et des **beats de la trame marqués « à revoir »**, qui ne reflètent **pas** encore les dernières décisions (rite sans nom, Braise seule, arrivée par le portail, démo Krunt seul). Source HTML et exports de la base : dans le répertoire temporaire de la session, perdus à la fin du conteneur.
- **L'export RTDB de krunt** contient des clés API et des e-mails : jamais copié ni commité. Si un export a été partagé, **renouvelle les clés** (Anthropic, Gemini, Mistral, PixelLab).

## 4. Chiffres de calendrier
Environ 49 semaines depuis le début du développement ; encore ~6 semaines sur les outils, puis ~69 semaines pour le jeu, à 14–24 h/semaine (le formulaire contient encore h_hours = 6, incohérent avec ça).

## 5. Règles : état
10 conflits entre livres (attributs/jauges, niveaux, dégâts, Honneur, Forge, rangs, phases, tendue, métiers, éléments) : options proposées (voir `audit/synthese-livres.md` et le formulaire). Les essais du `07` suggèrent un modèle à deux jauges (modèle C), non tranché. Résultats à rejouer si les fiches changent.

## 6. Questions ouvertes (pour la reprise)
1. Quels clans fonctionnent par **missions attribuées** (« donneurs d'ordres ») ? Les livres ne le disent que pour les guildes et les Frères de l'Épreuve.
2. Quels clans **protègent ou étudient le phœnix** ? Recherche à faire dans StoryForge.
3. **Pascal** : krunt a dit « sentinelles des ancêtres » ; les livres donnent le **Culte des Ancêtres Veilleurs** ; « Sentinelles du Pacte » est une invention de Claude.
4. **Taranis** est-il bien le « tombé » ? Quel niveau (3 proposé) ?
5. **Mana de départ** : 6/6/8/6 (Livre VI) ou 2 (Livre I) ?
6. Le portail est-il « le Filet » ? Où sont les trois autres juste après ?
7. Crans de la Braise visibles à l'écran ?
8. Nom du rite et de la technique : à définir (aucun pour l'instant).
9. Phœnix (juvénile ou migrant, second contrat…) : reporté.
10. Équilibrage : Herbe Stabilisante peut-être trop forte en solo (12 % → 41 % de victoires) ; Krunt3 équipement/sprite (double lames vs kit tank).
Le `10-trame-v3.md` §9 liste ~30 questions détaillées avec propositions.

## 7. Attentes extérieures
Test LDtk vs Godot (kit prêt) · PixelLab : sprites (Krunt3 en premier, puis Pascal, Cyril, Taranis) · intégration du roster dans CharForge (autre session) · ajouts à StoryForge (ordres, points de correspondance, recherche phœnix/clans) · liste des régions de l'app à aligner sur l'Atlas.

## 8. Contraintes constantes
Réponses en français, honnêtes, désaccord assumé. Aucune PR sans demande. Aucun identifiant de modèle IA dans les fichiers du dépôt. Aucune clé ni e-mail dans le dépôt.
