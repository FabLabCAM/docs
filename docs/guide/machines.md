# Profils de machine, validation et archives G-code

Depuis **FabLabCAM 0.3.0**, `fablabcam machine` permet d'importer, vérifier,
convertir et archiver des programmes avec un profil de machine. Cette fonction
réalise l'[issue #9](https://github.com/FabLabCAM/core/issues/9). Elle s'utilise
par **CLI ou API Rust** ; elle n'ajoute pas de panneau dans le Studio.

## Essayer avec les fichiers publics

Téléchargez dans un même dossier :

- [mach3-mill-demo.json](../examples/machines/mach3-mill-demo.json) : **machine fictive**, limites et origines de démonstration ;
- [machine-valid.nc](../examples/machines/machine-valid.nc) : programme synthétique avec un arc ;
- [machine-invalid.nc](../examples/machines/machine-invalid.nc) : dépassement X et code interdit ;
- [mach3-mill.json](../examples/machines/mach3-mill.json) : référence à configurer pour votre installation.

```sh
fablabcam version
fablabcam machine validate machine-valid.nc --profile mach3-mill-demo.json
fablabcam machine stats machine-valid.nc --profile mach3-mill-demo.json
fablabcam machine validate machine-invalid.nc --profile mach3-mill-demo.json
```

Le premier fichier donne `status: "valid"`, des bornes de **[0, 0, 0] à
[10, 10, 5] mm**, un trajet de coupe d'environ **30,708 mm**, un trajet rapide
 de **15 mm** et l'outil **1**. Le second signale le dépassement X à la ligne 3
et `G123` à la ligne 4. Les rapports complets produits par la CLI sont disponibles :
[rapport valide](../examples/machines/valid-report.json),
[rapport invalide](../examples/machines/invalid-report.json).

`stats` renvoie le même rapport que `validate` : les statistiques restent ainsi
accompagnées de leur statut et des avertissements.

!!! warning "Un profil d'exemple ne décrit pas votre machine"
    Renseignez les courses, vitesses, origines et réglages de votre installation.
    Le profil de référence ne les invente pas : sans ces données, son rapport
    reste incomplet. Aucun de ces exemples ne constitue un programme qualifié
    pour un usinage réel.

## Créer et gérer les profils

```sh
fablabcam machine profile init atelier.json
```

Éditez ce JSON dans votre éditeur. Donnez-lui un `id` stable, par exemple
`fraiseuse-atelier`, puis renseignez les réglages. L'ID accepte lettres ASCII,
chiffres, tiret et souligné, sur 1 à 80 caractères. Le schéma est versionné
(`schema_version: 1`) et les propriétés inconnues sont refusées.

| Groupe | Contenu et unités |
|---|---|
| Identité | `id`, `name`, `description`, `location`, `machine_kind` |
| Contrôleur | `controller.name`, `version`, `dialect`, `postprocessor` et liens `sources` |
| Axes | `axes.X` à `axes.C` : `kind` linéaire/rotatif, `min`, `max`, `max_feed` ; mm et mm/min, ou degrés et degrés/min |
| Vitesses | `max_feed_mm_min`, `rapid_mm_min`, `acceleration_mm_s2` |
| Repères | `initial_position_mm`, `work_offsets_mm` pour G54–G59, `positive_directions` |
| Broche | `spindle.min_rpm`, `max_rpm`, `directions` (`cw`, `ccw`) |
| Modes initiaux | `defaults.units`, `plane`, `distance`, `arc_distance`, `feed_mode`, `work_offset` |
| Modèle sémantique | `semantics`: `mach3_mill` ou `rs274_mill` ; définit le sens des codes, indépendamment du nom commercial du contrôleur |
| Dialecte | `gcodes` et `mcodes` : listes `allow` et `deny` ; une interdiction l'emporte |
| Format | Numéros N (`optional`, `required`, `forbidden`), décimales, commentaires, ASCII, majuscules, longueur de ligne, en-tête `%`, terminaisons M2/M30 |
| Atelier | `safety.safe_z_mm`, positions de parking/changement, `required_preamble`, autorisation des hélices, interdiction des rapides sous le Z de sécurité |
| Outils | Mode de changement, nombre de positions, comportement M6, refroidissement, table diamètre/longueur/type |

Les bornes, Z de sécurité et positions sont dans le **repère machine**.
`work_offsets_mm.G54: [10, 20, 0]` place l'origine G54 à ces coordonnées machine.
Un `X1 Y2` absolu dans ce repère correspond donc à `X11 Y22` machine.
`initial_position_mm` décrit la position au début du programme ; ce n'est pas
un ordre de déplacement. `null` signifie inconnu, jamais zéro implicite.

La table d'outils, l'accélération, le parking et la position de changement sont
conservés comme métadonnées. Ils n'ajoutent pas de mouvement et ne servent pas
à simuler une cinématique. Les axes rotatifs peuvent être décrits, mais leurs
mouvements rendent l'analyse incomplète.

Le magasin est un dossier local que vous choisissez :

```sh
fablabcam machine profile add atelier.json --store magasin
fablabcam machine profile list --store magasin
fablabcam machine profile show fraiseuse-atelier --store magasin
fablabcam machine profile update atelier.json --store magasin
fablabcam machine profile delete fraiseuse-atelier --store magasin
```

`add` refuse un ID existant ; `update` exige qu'il existe. `delete` retire le
profil courant et conserve les instantanés des archives. `--profile` lit un
fichier JSON ; pour exporter un profil enregistré, redirigez `profile show`
vers un nouveau fichier. Aucun service ni base de données n'est nécessaire.

## Lire un rapport

Les champs principaux sont `status`, `limits_checked`, `diagnostics` et
`statistics`. Chaque diagnostic fournit `severity` (`error`, `warning`, `info`),
`code`, `line`, `column`, `word` et `message`. Les positions sont comptées à
partir de 1, les colonnes en caractères.

| Statut | Signification | Code de sortie |
|---|---|---|
| `valid` | Conforme au profil dans le modèle statique pris en charge | 0 |
| `invalid` | Au moins une erreur : code interdit, course, syntaxe, préambule… | 1 |
| `incomplete` | Configuration, mouvement, durée ou construction non interprétée | 2 |

Le rapport JSON est toujours écrit sur **stdout**, même lorsqu'une validation
échoue. Les erreurs de commande ou de lecture de fichier sont écrites sur
stderr avec le code 1. Pour conserver le rapport :

```sh
fablabcam machine validate machine-valid.nc --profile mach3-mill-demo.json > rapport.json
```

`limits_checked` est vrai lorsque les courses XYZ, avances maximales d'axe et
globale, et bornes de broche sont configurées. `statistics.complete` concerne
le modèle statique ; les données déjà calculées restent consultables lorsqu'il
est faux. Une erreur ou un mouvement non interprété arrête l'accumulation des
trajectoires suivantes pour éviter d'afficher de fausses bornes.

### Ce qui est contrôlé

- Syntaxe littérale et nombres finis, doublons de mots/groupes modaux, formats et commentaires.
- Listes blanche/noire des G/M-codes, axes, outils et refroidissement configurés.
- Préambule avant le premier mouvement, en-tête et fin de programme.
- G0/G1 et arcs G2/G3, plans G17/G18/G19, rayon R signé, IJK absolus/relatifs et hélices.
- Extrema des arcs, courses XYZ, avances globales et par axe, broche et sens de rotation.
- Unités G20/G21 (alias G70/G71 uniquement avec `semantics: mach3_mill`), G90/G91, avances G93/G94/G95.
- Origines G54–G59 configurées ; G53 pour les mouvements linéaires absolus.

La liste blanche peut reconnaître davantage de codes que le moteur n'en
interprète. **Cycles G73/G81–G89, macros, sous-programmes, expressions,
compensations actives, transformations, palpage et référencement rendent le
rapport incomplet.** Ils ne sont ni exécutés ni supprimés silencieusement.
Le parseur poursuit l'examen des lignes suivantes et conserve leurs diagnostics.

M6 est incomplet par défaut car les macros locales peuvent déplacer la machine.
Ne réglez `tools.m6_preserves_position` à `true` qu'après vérification de leur
comportement. M0/M1 ont une durée opérateur inconnue. Les unités de G4 dépendent
d'un réglage contrôleur : sa durée reste partielle.

### Statistiques et durée

Les bornes et longueurs sont en mm, la durée en secondes, et `tools` contient
les numéros T sélectionnés. La durée suppose une vitesse constante et la vitesse
rapide du profil ; elle exclut accélération, jerk et latences. Après un changement
d'unités ou de mode d'avance, fournissez un nouveau F. En G93, F est requis à
chaque mouvement ; G95 exige une broche active.

Sur un arc, le contrôle de vitesse d'axe utilise une borne conservatrice : il
peut refuser un arc court dont la vitesse théorique maximale n'est pas atteinte.
Aucun rapport ne remplace une simulation de collision ou une qualification du
contrôleur et du bridage.

## Convertir vers un profil compatible

Pour reproduire cet exemple, téléchargez [cible.json](../examples/machines/cible.json),
un contrôleur fictif exigeant des numéros N et des commentaires point-virgule.
Le [résultat converti](../examples/machines/converti.nc) est fourni pour comparaison.

```sh
fablabcam machine convert machine-valid.nc --from mach3-mill-demo.json --to cible.json -o converti.nc
```

La conversion adapte les commentaires et la numérotation, normalise les mots,
explicite les modes initiaux et remplace les alias G70/G71 par G20/G21.
Les deux profils doivent utiliser les mêmes origines et la même position initiale.
Le modèle `semantics` doit correspondre au sens des codes du contrôleur ; les
modèles livrés couvrent le fraisage RS274, pas les cycles de tournage.
Elle refuse les programmes invalides/incomplets, les codes rejetés par la cible,
les valeurs que sa précision arrondirait et les messages opérateur `MSG`.

Elle ne réalise pas de translation de repère, de conversion mm/pouces, de
transformation d'arc IJK, d'expansion de cycles ou de réécriture de macros.
Le rapport fournit `source_report`, `target_report` et une liste `unsupported`.
Un refus retourne 2 et ne crée pas le fichier ; un chemin de sortie existant
est toujours refusé. Aucun profil GRBL ou LinuxCNC validé n'est livré à ce stade.

## Archiver et retrouver une révision

```sh
fablabcam machine archive add plaque machine-valid.nc --profile mach3-mill-demo.json --author FabLab --store magasin
fablabcam machine archive list plaque --store magasin
fablabcam machine archive show plaque 1 --store magasin
fablabcam machine archive export plaque 1 --store magasin -o plaque-revision-1.nc
```

Chaque `add` crée une nouvelle révision et conserve le programme exact, le profil
utilisé et le rapport. Les métadonnées portent auteur, date Unix UTC, machine,
statut et empreintes SHA-256. Un programme invalide ou incomplet peut être archivé :
son statut reste visible. Le succès d'`archive add` signifie que l'archive a été
créée, pas que son programme est valide.

Les écritures concurrentes sont verrouillées. Les lectures vérifient l'intégrité ;
une révision altérée est refusée. Les empreintes ne constituent pas une signature
contre quelqu'un capable de modifier également le manifeste. Le magasin est
local ; sauvegardez-le comme vos projets. Une modification ou suppression du
profil courant ne change pas les révisions déjà créées.

## Source du profil Mach3

Le profil se fonde sur le [manuel officiel Using Mach3Mill 1.84-A2, chapitre 10](https://www.machsupport.com/wp-content/uploads/2013/02/Mach3Mill_1.84.pdf).
Il vise **Mill**, pas Turn, et ne certifie pas la version R3.043.066. Les codes
G74/G76 et G10 L20 proposés dans l'issue ne sont pas validés pour ce profil.
Les commentaires retenus sont parenthèses, `//` et lignes `%` ; le point-virgule
reste désactivé sans vérification locale. Les macros utilisateur doivent être
ajoutées explicitement au profil et restent non interprétées.

Voir aussi l'[API et la décision d'architecture](https://github.com/FabLabCAM/core/blob/v0.3.0/docs/machine-gcode.md)
et les [notes de version](../reference/versions.md).
