# Module 12 : projet, la première chasse

## Objectif

Assembler tout le cours dans un seul prototype jouable : une chasse complète, sur ton téléphone.

## Le périmètre : volontairement minuscule

Une chasse, c'est :
- **un héros** (krunt) jouable en plateforme, avec saut, attaque, pose de piège ;
- **une arène longue** de quelques écrans ;
- **un monstre** avec ses états (patrouille, traque, charge, récupération, fuite, assommé) ;
- **un piège** ;
- **un HUD** : vie, pièges restants ;
- **des commandes tactiles** ;
- **une musique** (SoundForge) ;
- **une défaite et une victoire**, même simples (un texte à l'écran, un retour au début).

Pas de monde, pas de quête, pas de lien avec CRS, pas de création de personnage. Tout cela vient ensuite, quand cette chasse est **amusante**.

## L'ordre de travail

Chaque étape est jouable avant la suivante, avec des carrés de couleur si besoin.

1. **Le héros court et saute** sur un sol (module 4). Réglé jusqu'à ce que ce soit agréable.
2. **L'arène** (modules 5) : un long sol avec trois plateformes, une caméra.
3. **Le monstre** qui avance vers le héros (module 8, version minimale : seulement TRAQUE).
4. **Le combat** : le héros frappe, le monstre perd de la vie, le monstre frappe, le héros en perd (module 7).
5. **Les états** du monstre, un par un, en les testant à chaque ajout (module 8).
6. **Le piège** (module 8).
7. **Le HUD et les commandes tactiles** (module 9).
8. **Les vrais sprites** à la place des carrés (module 3), puis les effets (module 11).
9. **L'export sur téléphone** et le protocole de test (module 11).

**Règle** : si une étape te prend plus du double du temps prévu, **coupe**, ne repousse pas. Un monstre à quatre états qui est amusant vaut mieux qu'un monstre à dix états qui ne l'est pas.

## Critères de réussite

Le projet est terminé quand toutes ces cases sont cochées :

- [ ] Le jeu se lance sur ton téléphone depuis un APK.
- [ ] Il tient la cadence visée dans le pire moment du combat (note la valeur mesurée).
- [ ] Un joueur qui n'a jamais vu le jeu comprend quoi faire en trente secondes.
- [ ] Le combat est **lisible** : on voit venir les attaques du monstre.
- [ ] On peut gagner et on peut perdre.
- [ ] Un deuxième monstre peut s'ajouter **sans réécrire** le code (juste une nouvelle scène avec d'autres réglages).
- [ ] Deux personnes de ton entourage ont joué et tu as noté leurs remarques.

## Ce que tu auras prouvé

- **Le cœur du jeu est amusant**, ou il ne l'est pas. Dans les deux cas, tu le sauras avant d'avoir construit le reste.
- **La taille des personnages** (HD ou rétro) est tranchée par un vrai test, pas par une image.
- **Les effets que ton téléphone supporte** sont connus.
- **Ton pipeline** (PixelForge, Godot, téléphone) fonctionne de bout en bout.

## Après la première chasse

Dans cet ordre, en gardant chaque ajout jouable :
1. un deuxième monstre (même scène, autres réglages et attaques) ;
2. le mode **exploration en vue 3/4** et le passage vers la chasse (module 6) ;
3. la **création de personnage** avec palettes (module 10) ;
4. la **sauvegarde** ;
5. le **premier lien avec CRS** (module 10, journal d'événements).

## Quand tu es bloqué

Avec une session Claude Code dans Termux (le dépôt est la source commune), donne-lui :
- le **message d'erreur exact** de la console de Godot, en entier ;
- le **script concerné** (il est dans `scripts/`) ;
- ce que tu **attendais** et ce qui se passe.

Avec ces trois éléments, une aide précise est possible ; sans eux, elle ne peut que deviner.
