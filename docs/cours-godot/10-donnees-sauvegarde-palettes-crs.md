# Module 10 : données, sauvegarde, palettes, lien avec CRS

## Objectif

Garder l'état du jeu entre les scènes et les sessions, changer les couleurs d'un personnage sans redessiner, et préparer l'échange avec CRS.

## 1. Un script toujours actif : l'autoload

Quand tu changes de scène (module 6), tout ce qui était dans l'ancienne disparaît. L'état à conserver (vie du joueur, quêtes, objets) vit dans un **autoload** : un script chargé au démarrage et toujours présent.

1. Crée `scripts/etat_jeu.gd` :

```gdscript
extends Node

var joueur := {
	"nom": "Krunt",
	"vie_max": 100,
	"pieges_max": 3,
	"corps": "A",
	"palette": {"peau": 3, "cheveux": 5, "tissus": 2},
}
var quetes := {}      # ex : {"chasse_01": "terminee"}

const FICHIER := "user://sauvegarde.json"

func sauvegarder() -> void:
	var donnees := {"version": 1, "joueur": joueur, "quetes": quetes}
	var temporaire := FICHIER + ".tmp"
	var f := FileAccess.open(temporaire, FileAccess.WRITE)
	if f == null:
		push_error("Impossible d'écrire la sauvegarde")
		return
	f.store_string(JSON.stringify(donnees, "\t"))
	f.close()
	DirAccess.rename_absolute(temporaire, FICHIER)   # écriture sûre : on remplace d'un coup

func charger() -> bool:
	if not FileAccess.file_exists(FICHIER):
		return false
	var f := FileAccess.open(FICHIER, FileAccess.READ)
	var donnees = JSON.parse_string(f.get_as_text())
	if typeof(donnees) != TYPE_DICTIONARY:
		return false
	joueur = donnees.get("joueur", joueur)
	quetes = donnees.get("quetes", quetes)
	return true
```

2. Dans **Projet > Paramètres du projet > Globals (Autoload)**, ajoute ce script avec le nom `EtatJeu`. Depuis n'importe quel script : `EtatJeu.joueur["nom"]`, `EtatJeu.sauvegarder()`.

**Pourquoi écrire dans un fichier temporaire puis renommer ?** Si le téléphone s'éteint pendant l'écriture, tu risques de perdre la sauvegarde ; avec le renommage, soit l'ancienne reste, soit la nouvelle est complète. C'est la même précaution que pour ta clé USB.

**`user://`** est le dossier de données de ton jeu, propre à chaque plateforme : Godot s'occupe de l'endroit réel (sur Android, c'est un dossier privé de l'application).

## 2. Les données du jeu en JSON

Garde les données qui changent souvent (palettes, monstres, objets) hors du code, dans `donnees/*.json`, pour les éditer sans toucher aux scripts, et pour que tes outils Forge puissent les produire.

```gdscript
func charger_json(chemin: String) -> Variant:
	var f := FileAccess.open(chemin, FileAccess.READ)
	if f == null:
		return null
	return JSON.parse_string(f.get_as_text())

# Exemple d'usage
var monstres = charger_json("res://donnees/monstres.json")
```

## 3. Changer les couleurs sans redessiner : le décalage de palette

Idée : dessiner le sprite **une fois** avec des couleurs « d'indice » (le sprite ne contient que des numéros de couleur), puis lui appliquer n'importe quelle palette au moment de l'affichage. Un même sprite sert alors à toutes les régions et tous les clans.

### Préparer le sprite

Dans PixelForge, exporte une version « indexée » du sprite : chaque pixel a une valeur de **rouge** égale à son numéro de couleur (0, 1, 2... jusqu'à 15 ou 31), le vert et le bleu n'ont pas d'importance, la transparence est conservée. Convention utile : 0 à 3 pour la peau, 4 à 7 pour les cheveux, 8 à 11 pour les tissus, 12 à 15 pour le métal.

### La palette

Une image de **16 pixels de large** (32 si tu vas jusqu'à 32 couleurs), avec **une ligne par palette**. Chaque pixel de la ligne est la couleur d'un indice.

### Le shader

Sur le `Sprite2D` (ou `AnimatedSprite2D`), crée un `ShaderMaterial` avec ce shader :

```glsl
shader_type canvas_item;

uniform sampler2D palette : filter_nearest;
uniform int ligne = 0;

void fragment() {
	vec4 c = texture(TEXTURE, UV);
	float indice = floor(c.r * 255.0 + 0.5);
	ivec2 taille = textureSize(palette, 0);
	vec2 uv_palette = vec2((indice + 0.5) / float(taille.x), (float(ligne) + 0.5) / float(taille.y));
	vec4 couleur = texture(palette, uv_palette);
	COLOR = vec4(couleur.rgb, c.a);
}
```

Pour changer de palette depuis un script :

```gdscript
$AnimatedSprite2D.material.set_shader_parameter("ligne", 3)
```

Si plusieurs personnages utilisent le même matériau, active **Local to Scene** (dans la ressource du matériau) pour que chacun ait sa propre palette.

**Conditions à respecter** *(à tester : c'est l'un des premiers essais à faire)* : les sprites indexés doivent être importés en **Lossless**, avec le filtre **Nearest** et sans mipmaps ; sinon les indices sont déformés et les couleurs sortent faussées.

**Pourquoi c'est précieux pour toi** : tes palettes par région, par clan et par personnage deviennent de simples lignes d'une image. Et une palette est une donnée : StoryForge ou CharForge peuvent la fournir.

## 4. Exporter un personnage pour CRS

Le format d'échange le plus simple est un petit fichier JSON. Proposition de départ (à adapter à ce que CharForge contient réellement) :

```json
{
  "version": 1,
  "id": "krunt",
  "nom": "Krunt",
  "corps": "A",
  "palette": {"peau": 3, "cheveux": 5, "tissus": 2},
  "statistiques": {"FOR": 0, "AGI": 0, "END": 0, "ESP": 0, "VOL": 0, "PRE": 0},
  "metier": "",
  "ecole": "",
  "modifie_le": "2026-10-04T18:00:00"
}
```

Le champ `modifie_le` est essentiel : il te permettra, plus tard, de savoir quelle version est la plus récente quand tu synchronises. Ajoute-le à **tout** ce que tu sauvegardes dès maintenant.

Pour l'écrire :

```gdscript
func exporter_personnage() -> void:
	var perso := EtatJeu.joueur.duplicate(true)
	perso["version"] = 1
	perso["modifie_le"] = Time.get_datetime_string_from_system(true)
	var f := FileAccess.open("user://personnage_export.json", FileAccess.WRITE)
	f.store_string(JSON.stringify(perso, "\t"))
	f.close()
```

Pour que le fichier soit accessible depuis ton téléphone (pas seulement dans le dossier privé de l'application), il faudra passer par le sélecteur de fichiers d'Android : à prévoir et à tester tôt, car l'accès aux dossiers publics a des règles strictes depuis Android 11.

## 5. Parler à PocketBase : le journal d'événements

Pour que la table et le jeu se répercutent l'un dans l'autre, le plus simple est un **journal d'événements** : chaque côté **ajoute** des événements dans une collection PocketBase (`evenements`), l'autre côté les lit et les applique. Chaque événement contient : un type, un sujet, des données, la source (`jeu` ou `table`), une date.

Le jeu **doit rester jouable sans réseau** : si l'envoi échoue, l'événement est mis dans une file locale et renvoyé plus tard.

```gdscript
func envoyer_evenement(type: String, sujet: String, donnees: Dictionary) -> void:
	var requete := HTTPRequest.new()
	add_child(requete)
	requete.request_completed.connect(_on_envoye.bind(requete))
	var corps := JSON.stringify({
		"type": type, "sujet": sujet, "donnees": donnees,
		"source": "jeu", "date": Time.get_datetime_string_from_system(true),
	})
	var url := "http://192.168.1.10:8090/api/collections/evenements/records"   # ton serveur
	var erreur := requete.request(url, ["Content-Type: application/json"], HTTPClient.METHOD_POST, corps)
	if erreur != OK:
		requete.queue_free()
		# mettre l'événement dans une file locale ici

func _on_envoye(resultat: int, code: int, _entetes: PackedStringArray, _corps: PackedByteArray, requete: HTTPRequest) -> void:
	requete.queue_free()
	if resultat != HTTPRequest.RESULT_SUCCESS or code >= 300:
		pass   # échec : remettre dans la file locale
```

**Attention** *(à vérifier)* : Android peut bloquer le trafic HTTP non chiffré. Si l'appel vers ton serveur local échoue sur le téléphone alors qu'il marche sur PC, c'est la première chose à regarder. Les solutions sont d'autoriser explicitement ce trafic dans l'export, ou de passer en HTTPS.

**Les conflits** : si la table et le jeu modifient le même personnage non joueur, la règle la plus simple est « l'événement le plus récent gagne », avec les anciens conservés dans le journal.

## Exercice

1. Crée l'autoload `EtatJeu`. Sauvegarde, ferme le jeu, relance, charge : retrouves-tu ton état ?
2. Crée un sprite indexé de test (même un carré à quatre couleurs d'indice) et trois palettes ; change de palette avec une touche.
3. Exporte un personnage en JSON et relis-le avec un éditeur de texte.
4. Envoie un événement de test à ton PocketBase depuis le PC, puis coupe le réseau et vérifie que le jeu ne plante pas.

## Erreurs fréquentes

- **Couleurs fausses avec le shader** : l'import des sprites n'est pas en Lossless et Nearest.
- **`null` en chargeant un fichier** : mauvais chemin (`res://` pour les fichiers du jeu, `user://` pour les sauvegardes).
- **Le jeu se fige à l'envoi réseau** : appeler l'API de manière bloquante. Utilise toujours `HTTPRequest` (asynchrone) et jamais une boucle qui attend.

## Pour aller plus loin

Documentation : « Singletons (Autoload) », « Saving games », « Making HTTP requests », « Shading language », et la documentation de l'API REST de PocketBase.
