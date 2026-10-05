#!/usr/bin/env python3
"""Valide donnees/monstres/*.json : unicité des noms et des traits, interdits, ressemblance avec les anciens noms
(donnees/monstres/correspondance.json) et avec une liste de noms de monstres de franchises connues (liste ci-dessous).
Usage : python3 outils/valider_monstres.py"""
import json, glob, os, re, sys, difflib, unicodedata
D = os.path.join(os.path.dirname(__file__), '..', 'donnees', 'monstres')
SUFFIXES = ('rak', 'drak', 'var', 'vor', 'ark', 'akh', 'thak', 'avar', 'onak', 'duragon')
# Noms de monstres de franchises connues, à ne jamais approcher (liste non exhaustive, comparaison approximative).
FRANCHISE = """rathalos rathian teostra kushala daora zinogre namielle velkhana tigrex nargacuga barioth paolumu legiana deviljho
uragaan gypceros pukei kutku qurupeco tzitzi jagras velociprey velocidrome genprey iodrome kulu baggi hypnocatrice garuga seregios
gigginox brachydios nergigante valstrax alatreon fatalis akantor ukanlos lagiacrus astalos diablos monoblos plesioth lagombi
anjanath tobikadachi zamtrios odogaron radobaan dodogama bazelgeuse barroth jyuratodus tzitzi rajang mizutsune zinogre
glavenus lunastra kirin gore magala shagaru magala chameleos amatsu xeno jiiva behemoth kelbi aptonoth felyne palico
cutting popo gargwa rhenoplos remobra apceros kulve taroth lao shen ceanataur nakarkos shogun ceanataur khezu basarios
gravios cephadrome seltas nerscylla rathalos yian garuga zinogre""".split()
def norm(s):
    s = unicodedata.normalize('NFD', s.lower())
    return re.sub(r'[^a-z]', '', ''.join(c for c in s if unicodedata.category(c) != 'Mn'))
def main():
    corr = json.load(open(os.path.join(D, 'correspondance.json')))
    anciens = {k: norm(v['ancien_nom'].split(' — ')[0].replace('-Duragon', '')) for k, v in corr.items()}
    recs = []
    for f in sorted(glob.glob(os.path.join(D, '*.json'))):
        if os.path.basename(f) in ('correspondance.json','migration_cle_id.json'): continue
        for r in json.load(open(f)): r['_f'] = os.path.basename(f); recs.append(r)
    err = []
    names = {}; traits = {}
    for r in recs:
        n = r.get('nouveau_nom', '')
        nn = norm(n)
        if nn in names: err.append(f"nom en double : {n} ({r['id']} / {names[nn]})")
        names[nn] = r['id']
        tk = r.get('apparence', {}).get('trait_cle', '')
        if tk in traits: err.append(f"trait_cle en double : {tk} ({r['id']} / {traits[tk]})")
        traits[tk] = r['id']
        if not r.get('nom_conserve'):
            if nn.endswith(SUFFIXES): err.append(f"suffixe interdit : {n} ({r['id']})")
            a = anciens.get(r['id'])
            if a:
                s = difflib.SequenceMatcher(None, nn, a).ratio()
                if s > 0.6: err.append(f"trop proche de l'ancien nom ({s:.2f}) : {n} ({r['id']})")
        for fr in FRANCHISE:
            if len(nn) >= 4 and (difflib.SequenceMatcher(None, nn, fr).ratio() > 0.72 or (len(fr) >= 6 and (fr in nn or nn in fr))):
                err.append(f"proche d'un nom de franchise ({fr}) : {n} ({r['id']})")
        for k in ('id', 'nouveau_nom', 'sous_titre', 'rang', 'cr', 'apparence', 'familier', 'element_principal'):
            if k not in r: err.append(f"champ manquant {k} : {r.get('id')}")
        if r.get('familier', {}).get('possible') and not r['familier'].get('roles'):
            err.append(f"familier sans rôles : {r['id']}")
    print(len(recs), 'monstres,', len(err), 'problèmes')
    for e in err: print(' -', e)
    return 1 if err else 0
if __name__ == '__main__': sys.exit(main())
