# Inventaire des applications Forge (état au 2026-10-05)

Rédigé d'après le récit vocal de krunt. Les mentions « à confirmer » sont mes inférences, pas des affirmations de krunt.

| Application | Rôle | État annoncé par krunt | À faire | Priorité |
|---|---|---|---|---|
| **PorteForge** | Portail d'accès à toutes les applications ; importe des données en base | Déjà fonctionnelle | Claude l'étend au fur et à mesure des besoins d'import (monstres, livres) | continu |
| **CharForge** | Fiches de personnage, bestiaire, familiers/élevage | Terminée « demain ou après-demain », pas à 100 % | Refonte d'interface en cours avec l'autre session (krunt et elle) | en cours |
| **MapForge** | Cartes vue 3/4, jeu et CRSVTT | Pas faite | **Probablement inutile** : voir `docs/analyse-editeurs-cartes.md` | à trancher |
| **LevelForge** | Niveaux | Pas faite | Même question que MapForge | à trancher |
| **SceneForge** | Scénarios pour le CRSVTT : scènes, personnages, lieux, musiques assemblés en trame de MJ | Première ébauche, 60 à 70 % | Compléter si besoin ; ne doit pas devenir grosse | faible |
| **MindForge** | « Deuxième cerveau » | Finalisée | Usage par krunt | — |
| **DBForge** | Sauvegarde hors ligne et transfert vers le serveur en ligne | Prochaine grosse application | Réglages du serveur (basculer vers un NAS si le portable lâche), saisie graphique de la base ; peu complexe | **haute** |
| **QuickForge** (« quelques forges ») | Calculatrice du MJ en session VTT | Pour plus tard, sera sûrement intégrée au CRSVTT | — | plus tard |
| **ReaderForge** | Lire, modifier, annoter des PDF et des fichiers Markdown | Moins utile (krunt passe par Claude pour relire les PDF et travaille en Markdown) | Peut-être une interface PC | faible |
| **StoryForge** | Récit/canon | Finie | — | — |
| **PixelForge** | Pixel art | Finalisée ; trois choses à intégrer (voir le journal mémoire de l'autre session) | Format « Perso 3/4 32×48 », taille de sprite à la création d'un document, lien avec ConfyUI (local, à la manière de PixelLab) | **haute** |
| **SketchForge** | Dessin standard, portraits | Pour usage personnel ; pas nécessaire au jeu | Peut-être ConfyUI en local | faible |
| **InkForge** | Dessin vectoriel | Finalisée ; plus nécessaire | — | — |
| **SoundForge** | Musique | Finalisée à 80 % ; deux versions (Android, PC plus performante) | Revoir l'interface PC (quelques jours à une semaine max), puis éprouver | moyenne |
| **LightForge** | Retouche photo (type Lightroom/Photoshop) | Fonctionnelle, sans IA | IA locale plus tard (ConfyUI, intégration de Claude pour des commandes comme « ouvre la main ») ; pas pour la démo | plus tard |
| **VideoForge** | Montage vidéo léger (fondus, zoom, ralentis, texte, glisser-déposer) | Pas faite | Simple : enregistrement d'écran du téléphone puis montage léger ; pas un After Effects | faible |
| **CRSVTT** | Plateforme de JDR en ligne | Pas faite | Après la démo du jeu ; ce sera l'application la plus complexe | après la démo |
| **RPG solo (Jeu B)** | Le jeu vidéo | Après les outils | La démo d'abord | après outils |

## Calendrier annoncé par krunt
Environ **6 semaines** pour finir les logiciels (vers la mi-novembre 2026), puis le jeu, qui est « le dur ». Le CRSVTT est une création longue après la démo.

## Définition de « fini » proposée pour les outils (à valider)
Une application est « finie » pour cette phase si elle sait **alimenter ou lire ce dont le jeu a besoin** : monstres et familiers (CharForge), sprites et palettes (PixelForge), musique (SoundForge), journal et sauvegarde (DBForge), lecture du canon (StoryForge). Tout le reste (aperçu 3D, générateur de noms, LightForge IA, VideoForge, MapForge/LevelForge) passe après la démo.
