# Module 13 : animation et hitbox, le cours complet

Pour le Jeu B. Complète le module 7 (code du combat). Ici : **comment concevoir** les animations et les zones de coup, et **combien d'images** ça coûte.

Honnêteté : le code GDScript de ce cours n'est pas testé (Godot n'est pas installable dans l'environnement où je travaille). Les chiffres d'images et de durées sont des ordres de grandeur issus de guides publics (liens en fin de module), pas des règles.

---

## Partie 1. Les bases de l'animation d'un sprite

### 1.1 Une animation, c'est une suite d'images jouées à une cadence

- Une **image** (frame) est un dessin fixe.
- Une **animation** est une liste d'images avec une durée par image.
- En rétro, on joue souvent à **8 à 12 images par seconde** pour l'animation, même si le jeu tourne à 60 images/s. Ce n'est pas un défaut : c'est ce qui donne le style « pixel art ».

### 1.2 Les animations dont un héros d'action a besoin

| Famille | Exemples | Images typiques (6 à 8 par cycle) |
|---|---|---|
| Déplacement | repos, marche, course, saut (montée, sommet, descente), réception | 4 à 8 chacune |
| Combat | attaque légère, attaque lourde, esquive, garde, coup reçu, mort | 5 à 8 chacune |
| Interaction | ramasser, ouvrir, porter un objet (l'œuf), poser un piège, boire | 4 à 6 chacune |
| Déplacement spécial | grimper, escalader, nager | 4 à 8 chacune |

### 1.3 Anatomie d'une attaque (à retenir absolument)

Une attaque a **trois phases**. Elles décident de la sensation de jeu **et** de la hitbox.

1. **Préparation** (anticipation) : le corps recule, l'arme se lève. Le joueur voit le coup venir. Durée plus longue pour une arme lourde.
2. **Active** : l'arme traverse. **C'est la seule phase où la zone de coup existe.** Très courte (1 à 2 images).
3. **Récupération** : retour à la position neutre. Le personnage ne peut pas encore agir : c'est ce qui crée le risque et l'équilibre entre armes.

Exemple pour une attaque lourde à 6 images : 3 de préparation, 1 active (tenue un peu plus longtemps pour « porter »), 2 de récupération.

Règle pratique : **arme lourde = longue préparation et longue récupération. Arme légère = les deux courtes.** C'est ainsi qu'on différencie les armes sans dessiner plus.

### 1.4 Les principes qui comptent en pixel art à peu d'images

- **Anticipation** : toujours au moins une image de préparation, sinon le coup paraît sortir de nulle part.
- **Étirement et pose clé** : sur peu d'images, chaque image doit être une pose très lisible. Dessiner les poses clés d'abord, remplir ensuite.
- **Image tenue** : prolonger l'image d'impact de quelques centièmes de seconde donne du poids (le « hit stop », module 7).
- **Silhouette lisible** : à 64 px de haut, on lit la pose par la silhouette. Une arme qui sort de la silhouette se voit, une arme collée au corps non.
- **Cohérence entre images** : mêmes couleurs (palette partagée), même épaisseur de contour, même position des pieds au sol.

---

## Partie 2. Mettre les animations dans Godot

### 2.1 Deux outils

| Outil | Pour quoi | Limite |
|---|---|---|
| `AnimatedSprite2D` | Jouer une suite d'images (la plupart des animations de héros) | Ne change que le sprite |
| `AnimationPlayer` | Animer **n'importe quelle propriété** dans le temps : le sprite, mais aussi l'activation d'une hitbox, la position d'une zone, un son, une particule | Plus de réglages |

Conseil pour toi : **`AnimationPlayer` pour les animations de combat**, parce qu'il synchronise images, hitbox et sons sur la même ligne de temps. `AnimatedSprite2D` suffit pour marche, repos, saut.

### 2.2 Feuilles de sprites (spritesheet)

Les images PixelLab arrivent en images séparées ou en planche. Dans Godot :

1. Importe la planche, avec **Filter = Nearest** (module 1, sinon les pixels se floutent).
2. `Sprite2D` : règle `Hframes` et `Vframes` (nombre de colonnes et de lignes), puis anime la propriété `frame`.
3. Ou `AnimatedSprite2D` : « SpriteFrames » > « Ajouter des images depuis une planche ».

### 2.3 Un modèle de scène pour un personnage

```
Heros (CharacterBody2D)
├── Visuel (Node2D)            ← c'est lui qu'on retourne (scale.x = -1)
│   ├── Sprite (Sprite2D)
│   └── ZoneCoup (Area2D)      ← la hitbox, disabled au départ
│       └── CollisionShape2D
├── Corps (CollisionShape2D)   ← collision avec le décor
├── Hurtbox (Area2D)           ← zone vulnérable
│   └── CollisionShape2D
└── Animations (AnimationPlayer)
```

Mettre la hitbox **dans** le nœud retourné fait que le miroir (regard à gauche) marche tout seul.

### 2.4 Activer la hitbox pendant les bonnes images

Dans l'`AnimationPlayer` :

1. Crée l'animation `attaque_legere`, longueur 0,5 s par exemple.
2. Piste « Property » sur `Visuel/Sprite:frame` : une valeur par image.
3. Piste « Property » sur `Visuel/ZoneCoup/CollisionShape2D:disabled` : `true` au début, `false` **seulement** sur la ou les images actives, puis `true` de nouveau.
4. Si Godot signale une erreur « flushing queries », règle le mode de rappel de l'`AnimationPlayer` sur **Physics** *(à vérifier selon la version)*.

Ainsi la zone de coup suit **exactement** ce que tu vois à l'écran.

### 2.5 Une zone de coup par image : le cas de la queue qui balaie

Pour un grand coup d'arme qui traverse l'écran, une seule boîte immobile ne suffit pas. Anime aussi `position` et `scale` de la `CollisionShape2D` image par image : la boîte suit la lame. Les arcs de balayage se décomposent en 2 ou 3 boîtes successives.

---

## Partie 3. La hitbox, le cours

### 3.1 Rappel des trois zones

| Zone | Rôle | Taille |
|---|---|---|
| **Corps** (collision) | Bloque contre le décor | Petite, souvent un rectangle ou une capsule sur les pieds et le torse |
| **Hurtbox** | Là où le personnage **peut être touché** | Plus petite que le dessin |
| **Hitbox** | Là où une attaque **fait mal** | Suit la lame ou le coup, seulement pendant les images actives |

### 3.2 Pourquoi la hurtbox est plus petite que le dessin

Le joueur doit avoir l'impression que **les coups le frôlent** plutôt qu'il est touché « à travers sa cape ». À 64 px de haut, une hurtbox typique : ≈ 18 × 44 px, centrée sur le torse, sans les bras ni l'arme.

C'est ta question « hitbox fidèle au sprite » : la bonne pratique en jeu d'action est **le contraire**. Fidèle au dessin donne un jeu injuste. On reste cohérent visuellement en gardant la **hitbox d'attaque** fidèle à l'arme (elle doit couvrir ce qui est dessiné), et la **hurtbox du joueur** un peu plus petite que le corps.

> Décision recommandée pour le Jeu B : hitbox d'attaque fidèle à l'arme sur les images actives ; hurtbox de défense plus petite que le corps ; une seule hurtbox par personnage au début.

### 3.3 Les trois méthodes pour définir les hitbox, du plus simple au plus précis

1. **Une boîte fixe par attaque** : simple, bon pour démarrer. Une attaque = une boîte active sur 1 à 2 images.
2. **Une boîte par image active** : elle suit la lame. Faisable avec l'`AnimationPlayer`. C'est la cible pour tes armes principales.
3. **Plusieurs boîtes par image** (tête, corps, queue d'un monstre) : pour les boss. Chaque partie a sa hurtbox propre, ce qui permet des points faibles.

### 3.4 Hitbox selon l'arme, sans dessiner plus

Idée clé pour tes nombreuses armes : **ne dessine pas une animation par arme, dessine une animation par famille d'arme**, et règle les différences dans les nombres.

| Famille | Animations de base | Ce qui change d'une arme à l'autre (sans nouveau dessin) |
|---|---|---|
| Épée, hache, masse (une main) | 2 attaques + 1 combo | dégâts, portée de la boîte, durée de préparation |
| Armes lourdes (espadon, grand marteau) | 1 attaque lourde + 1 attaque tournoyante | long délai, grande boîte, recul |
| Lance, pique | 1 coup droit + 1 balayage | portée longue, boîte étroite |
| Arc, arbalète | tirer, bander, viser | cadence, projectile |
| Magie, outils | lancer, soigner, utiliser | effets en particules, pas dans le sprite |

Les **effets** (trace de lame, éclairs, éclats) se font avec des particules ou un petit sprite séparé : ils ne font pas grossir le nombre d'images du héros.

### 3.5 Le « game feel » en une page

- **Hit stop** : arrêt de l'image 50 ms au contact.
- **Recul** du touché, **clignotement** blanc.
- **Tremblement d'écran** léger, **son** synchronisé avec l'image d'impact.
- **Fenêtre d'annulation** : permettre d'enchaîner une attaque ou une esquive vers la fin de la récupération.
- **Invincibilité courte** après un coup reçu (module 7).

---

## Partie 4. Le budget d'images : tes chiffres

Tu estimes 500 images pour le héros, peut-être 800. Voici le détail, pour savoir où il part.

### 4.1 Une estimation honnête, par vue

Hypothèse : cycles de 6 images (peut descendre à 4 pour les actions courtes).

| Bloc | Animations | Images |
|---|---|---|
| Déplacement (repos, marche, course, saut ×3, réception) | 8 | ≈ 45 |
| Grimper, escalader | 2 | ≈ 14 |
| Interaction (ramasser, porter l'œuf, piège, boire, ouvrir) | 6 | ≈ 32 |
| Réactions (coup reçu, garde, esquive, mort) | 4 | ≈ 22 |
| Combat par famille d'arme × 5 familles (≈ 4 animations de 6) | 20 | ≈ 120 |
| **Total par vue de profil** | **40** | **≈ 233** |

Pour la vue 3/4, quatre directions dont l'une par miroir, ce qui multiplie par 3 environ les animations qui changent selon la direction. En pratique les animations de combat et les déplacements sont refaits en 3/4 ; l'escalade, elle, n'existe qu'en plateforme. Hypothèse prudente : ≈ 60 à 70 % du coût de la vue de profil, par direction dessinée.

**Ordre de grandeur final : 500 à 800 images par personnage jouable, sur deux vues.** Ton estimation est donc réaliste, pas exagérée.

### 4.2 Le chiffre qui compte vraiment : ×4 personnages

Si les quatre personnages ont chacun leurs animations : 2 000 à 3 200 images. Avec PixelLab qui anime, c'est un travail de **génération et de tri**, pas de dessin. Mais **chaque image générée doit être vérifiée** (palette, cohérence, pieds au sol). Le goulot sera ce tri.

### 4.3 Comment limiter sans perdre le style

1. **Cycles courts** : 4 à 6 images. Le rétro l'assume.
2. **Animations partagées par famille d'arme** (3.4).
3. **Quatre personnages = un squelette commun** si les corps ont les mêmes proportions : on réutilise les animations et on change l'habillage par la palette (swap de palette, module 10 du cours). Plus ils se ressemblent par la taille, plus on partage.
4. **Mêmes animations vue de profil et 3/4** quand c'est possible (marche, repos).
5. **Squelette pour les boss** (pièces découpées animées dans Godot) : peu d'images, mémoire faible.

### 4.4 Squelette ou image par image pour le héros ?

| | Image par image (PixelLab, 6–8 images) | Squelette (pièces découpées) |
|---|---|---|
| Aspect | Pixel art pur, plus lisible | Plus fluide, un peu « marionnette » |
| Travail par arme | Nouvelle série d'images | Changer une pièce (l'arme) |
| Cohérence en IA | À vérifier image par image | Les pièces ne bougent pas : très cohérent |
| Coût | Moyen à élevé | Faible une fois le squelette fait |

Piste que tu évoques et que je trouve bonne : **un squelette pour les mouvements et l'IA pour améliorer les images clés**. À tester avec PixelLab au premier mois d'abonnement : une marche et une attaque, dans les deux modes, et comparer au rendu.

---

## Exercices

1. Dessine ou génère 6 images d'une attaque de l'épée. Note : quelles images sont la préparation, l'active, la récupération ?
2. Monte-les dans un `AnimationPlayer` et active la hitbox seulement sur l'image active.
3. Colle une boîte de collision visible (Debug > Collision Shapes visibles) et regarde si elle correspond à ce que tu vois.
4. Remplace l'épée par une lance : change **seulement** les nombres (portée, délais). La lance paraît-elle différente ?

## Erreurs fréquentes

- Hitbox active toute l'animation : les coups touchent pendant la préparation.
- Hurtbox égale au dessin : les coups paraissent injustes.
- Oublier la **récupération** : le combat n'a plus de risque.
- Hitbox oubliée dans le miroir : elle reste à droite quand le héros regarde à gauche.
- Dessiner une série d'images par arme au lieu d'une par famille : le budget explose.

---

## Ressources (à consulter, liens trouvés par recherche, non vérifiés en profondeur)

- GDQuest, « Handling mêlée attacks and damage with hitboxes and hurtboxes » (Godot 4) : https://www.gdquest.com/library/hitbox_hurtbox_godot4/
- Documentation officielle Godot, « 2D sprite animation » : https://docs.godotengine.org/en/4.3/tutorials/2d/2d_sprite_animation.html
- Forum Godot, « How to animate 2D hitboxes and hurtboxes? » : https://forum.godotengine.org/t/how-to-animate-2d-hitboxes-and-hurtboxes/58826
- Vidéo (anglais), « How to Make Accurate Animated Collision & Hitboxes in Godot 4 » : https://www.youtube.com/watch?v=kamZRN54TNY
- Principes d'animation adaptés au pixel art : https://www.sprite-ai.art/guides/animation-principles
- Nombre d'images par animation : https://www.sprite-ai.art/blog/sprite-animation-frames
- Comment animer le pixel art (marche, repos, attaques) : https://www.sprite-ai.art/guides/how-to-animate-pixel-art
