#!/usr/bin/env python3
"""Mesure un ou plusieurs sprites PNG (images d'une animation) pour vérifier
qu'ils respectent la bible graphique : taille réelle du personnage, marges,
couleurs, pixels propres, stabilité d'une image à l'autre.

Usage :
    python3 mesure_sprite.py image1.png [image2.png ...] [--case 128] [--hauteur 64]

    --case     taille attendue de la case carrée (ex. 128). Facultatif.
    --hauteur  hauteur attendue du personnage en pixels (ex. 64). Facultatif.

Nécessite Pillow : pip install pillow
"""
import sys
from PIL import Image


def charger(chemin):
    im = Image.open(chemin).convert("RGBA")
    return im


def boite_opaque(im):
    """Boîte englobante des pixels visibles (alpha > 0)."""
    alpha = im.getchannel("A")
    return alpha.point(lambda a: 255 if a > 0 else 0).getbbox()


def couleurs_opaques(im):
    px = im.load()
    w, h = im.size
    ens = set()
    semi = 0
    for y in range(h):
        for x in range(w):
            r, g, b, a = px[x, y]
            if a == 255:
                ens.add((r, g, b))
            elif a > 0:
                semi += 1
    return ens, semi


def agrandi_par(im):
    """Détecte un agrandissement entier (ex. sprite de 32 px agrandi x4 en 128 px)."""
    w, h = im.size
    for k in range(8, 1, -1):
        if w % k or h % k:
            continue
        petit = im.resize((w // k, h // k), Image.NEAREST)
        retour = petit.resize((w, h), Image.NEAREST)
        if retour.tobytes() == im.tobytes():
            return k
    return 1


def main(argv):
    fichiers, case, hauteur = [], None, None
    i = 0
    while i < len(argv):
        if argv[i] == "--case":
            case = int(argv[i + 1]); i += 2
        elif argv[i] == "--hauteur":
            hauteur = int(argv[i + 1]); i += 2
        else:
            fichiers.append(argv[i]); i += 1
    if not fichiers:
        print(__doc__)
        return 1

    lignes, toutes_couleurs, hauteurs, bas = [], set(), [], []
    premiere = None
    for f in fichiers:
        im = charger(f)
        bb = boite_opaque(im)
        if bb is None:
            print(f"{f} : image entièrement transparente")
            continue
        l, t, r, b = bb
        hauteur_px, largeur_px = b - t, r - l
        marge_bas = im.height - b
        cols, semi = couleurs_opaques(im)
        k = agrandi_par(im)
        hauteurs.append(hauteur_px)
        bas.append(b)
        toutes_couleurs |= cols
        if premiere is None:
            premiere = cols
        hors_premiere = len(cols - premiere)
        pct = 100.0 * hauteur_px / im.height
        lignes.append((f, im.size, hauteur_px, largeur_px, pct, marge_bas, len(cols), semi, k, hors_premiere))

    print(f"{'fichier':28} {'case':>9} {'haut.':>5} {'larg.':>5} {'%case':>6} {'marge bas':>9} {'coul.':>5} {'semi-transp.':>12} {'agrand.':>7} {'coul. hors img 1':>16}")
    for (f, size, h, w, pct, mb, nc, semi, k, hors) in lignes:
        print(f"{f[-28:]:28} {size[0]}x{size[1]:<4} {h:>5} {w:>5} {pct:>5.0f}% {mb:>9} {nc:>5} {semi:>12} {'x'+str(k):>7} {hors:>16}")

    print()
    if not lignes:
        return 1
    print("Résumé")
    print(f"  Images mesurées : {len(lignes)}")
    print(f"  Hauteur du personnage : de {min(hauteurs)} à {max(hauteurs)} px (écart {max(hauteurs)-min(hauteurs)})")
    print(f"  Position des pieds (bas) : de {min(bas)} à {max(bas)} px (écart {max(bas)-min(bas)})")
    print(f"  Couleurs distinctes sur l'ensemble : {len(toutes_couleurs)}")
    verdicts = []
    if hauteur is not None:
        ecart = abs(sum(hauteurs) / len(hauteurs) - hauteur)
        verdicts.append(("Hauteur attendue %d px (±%d)" % (hauteur, max(4, hauteur // 16)), ecart <= max(4, hauteur // 16)))
    if case is not None:
        verdicts.append(("Case de %d px" % case, all(l[1] == (case, case) for l in lignes)))
    verdicts.append(("Aucun pixel semi-transparent", all(l[7] == 0 for l in lignes)))
    verdicts.append(("Aucun agrandissement caché", all(l[8] == 1 for l in lignes)))
    verdicts.append(("Pieds stables (écart <= 2 px)", max(bas) - min(bas) <= 2))
    verdicts.append(("Hauteur stable (écart <= 4 px)", max(hauteurs) - min(hauteurs) <= 4))
    verdicts.append(("Au plus 32 couleurs sur l'ensemble", len(toutes_couleurs) <= 32))
    print()
    for texte, ok in verdicts:
        print(f"  [{'OK' if ok else 'À VOIR'}] {texte}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
