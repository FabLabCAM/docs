# Référence de la ligne de commande

`fablabcam help` affiche l’aide de la version installée. Les commandes suivantes
sont celles de la version 0.5.0. Les chemins contenant des espaces doivent être
placés entre guillemets. Dans PowerShell, préfixez par `./` un exécutable présent
dans le dossier courant.

## Choisir une commande

| Besoin | Commande |
|---|---|
| Identifier la version | `version` ou `--version` |
| Profils, validation et archives G-code | [`machine`](../guide/machines.md) |
| Modèles, meubles, placement et dossier ZIP | [`furniture`](../guide/meubles.md) |
| Inventorier un dessin `.cb` | `info` |
| Lister une bibliothèque de styles | `styles` |
| Convertir un dessin | `convert` |
| Rejouer les opérations enregistrées | `build` |
| Calculer une opération directe depuis le dessin | `gcode` |
| Exécuter un script | `script` |
| Simuler la matière | `sim` |
| Créer un aperçu web du projet | `web` |
| Relire et tracer le G-code | `plot` |

## Exemples reproductibles

```sh
fablabcam info plaque.cb
fablabcam build plaque.cb -o plaque.nc
fablabcam sim plaque.cb --res 0.5 --at 1.0
fablabcam plot plaque.nc -o trajectoires.html
fablabcam web plaque.cb -o projet.html
fablabcam convert plaque.cb plaque.svg
fablabcam script plaque.rhai -o nouveau.cb
```

Les fichiers sont disponibles dans le [tutoriel](../guide/premier-projet.md).
La commande `web` produit une page navigable d’inspection ; elle ne publie rien
sur Internet et ne remplace pas l’éditeur natif. `plot` relit le programme G-code.

## Aide complète de la version 0.5.0

```text
fablabcam — FAO 2,5D en Rust (dessins XML .cb, DXF et SVG)

USAGE
  fablabcam version                              version du produit
  fablabcam furniture help                       modèles, meubles et dossiers de fabrication
  fablabcam machine help                         profils, validation et archives G-code
  fablabcam info   <fichier.cb>
  fablabcam styles <styles.xml>
  fablabcam gcode  <fichier.cb> --op <profile-outside|profile-inside|profile-on|pocket|drill> [options]
  fablabcam convert <entrée.(cb|dxf|svg)> <sortie.(cb|dxf|svg)>      conversion de dessins
  fablabcam web    <projet.cb|dxf|svg|demo|demo-dessin> -o page.html [--select a,b]    page « studio » navigable (captures)
  fablabcam sim    <projet.cb|demo> [--res 0.2] [--at 1.0]       simulation de matière (chrono, volume, gouges)
  fablabcam script <script.rhai> [projet.cb] [-o sortie.cb]   exécute un script Rhai (dessin, outils, opérations)
  fablabcam build  <projet.cb> [-o programme.nc] [--post def.cbpp] [--macros '$o=1;$x=2']   G-code des opérations du projet (outils + liste)
  fablabcam plot   <fichier.cb|programme.nc> [options de gcode pour un .cb] [options de tracé] -o trace.svg|trace.html
  fablabcam-view   <fichier.cb|programme.nc> [mêmes options]   fenêtre interactive (zoom, Z, animation)

OPTIONS de gcode
  --layer <nom>       ne traiter que ce calque (défaut : tous)
  --styles <fichier>  bibliothèque de styles (tests/fixtures/styles-demo.xml)
  --style <nom>       style à appliquer (défaut : le style de base)
  --tool <mm>         diamètre d'outil
  --depth <z>         profondeur cible (négative)
  --step <mm>         incrément de passe
  --stock <z>         altitude de la surface du brut
  --clearance <z>     plan de dégagement
  --feed <mm/min>     avance de coupe
  --plunge <mm/min>   avance de plongée
  --speed <tr/min>    vitesse de broche
  --tabs <méthode>    none | auto | outer | inner : languettes de maintien (profils)
  --tab-width <mm>    --tab-height <mm>   --tab-distance <mm>   --tab-style triangle|square|skip
  --lead-in <type>    none | spiral | tangent   (--lead-out : tangent | none)
  --angle <deg>       angle de spirale (0 = un incrément de profondeur par tour)
  --radius <mm>       rayon des arcs tangents
  --cut-order <o>     depth | level   (ordre des passes des poches)
  --milling <sens>    climb | conventional | mixed   (défaut : climb)
  --spindle <sens>    cw | ccw   (M3 / M4 ; le sens de fraisage en dépend)
  --overcut           surcoupe dans les coins intérieurs des profils
  --finish <mm>       distance de la passe de finition des poches (0 = aucune)
  --finish-all        finition à chaque niveau au lieu du seul niveau final
  --final-step <mm>   incrément de la dernière passe en profondeur
  --crossover <f>     transition max. entre anneaux, fraction du diamètre (0 = aucune)
  --stepover-feed <v> avance des transitions
  --no-canned         expanser les perçages (pas de G81/G83)

OPTIONS de plot  (relit le G-code et trace la vue de dessus : couleur = profondeur Z, flèches = sens
                  de parcours, pointillés = rapides, points orange = plongées ; profil Z en bas)
  --no-rapids  --no-arrows  --no-plunges   masquer ces éléments
  --color <c>         z (défaut) | type
  --z-range <a,b>     n'afficher que les passes entre les altitudes a et b
  --title <texte>     titre de l'image
  (-o trace.html : page interactive autonome — pan/zoom, animation, survol ; ?at=0.5 dans l'URL)

POCHES  Les formes contenues dans une autre sont traitées comme des îlots.
  -o <fichier>        écrire le G-code dans un fichier (défaut : sortie standard)
```

Les erreurs de commande sont écrites sur stderr. Pour `machine validate` et
`machine stats`, le rapport JSON reste sur stdout : 0 valide, 1 invalide, 2
incomplet. La commande d’aide générale est `help` ; `machine help` et
`machine --help` donnent l’aide du nouveau module.
Le paramètre `--at` est une fraction de longueur de parcours, pas une durée.

## Viewer natif

`fablabcam-view programme.nc` ouvre un programme existant. Avec un dessin `.cb`,
fournissez aussi les options de génération, par exemple `--op profile-outside`.
Le viewer permet le zoom, les filtres en Z et l’animation. Pour éditer un projet
et ses opérations, utilisez `fablabcam-studio-ui projet.cb`.

## Paramètres plus avancés que le panneau Studio

La CLI expose notamment le picage par `--step`, la désactivation des cycles par
`--no-canned`, le sens de fraisage mixte, les avances de transition et des options
de rendu du backplot. Les options de `gcode` ne modifient pas le projet `.cb`.
Gardez vos commandes dans un script si vous devez reproduire exactement le résultat.

## Commandes de machine

Voir le [guide complet](../guide/machines.md) pour les profils JSON, rapports,
conversions et archives. L’aide du module est reproductible :

```text
fablabcam machine — profils et contrôle statique de G-code

  machine profile init <sortie.json>                 ID CNC PRO - Mach3 à configurer
  machine profile add|update <profil.json> --store <dossier>
  machine profile list --store <dossier>
  machine profile show|delete <id> --store <dossier>
  machine parse <programme.nc>
  machine validate|stats <programme.nc> --profile <profil.json>
  machine convert <programme.nc> --from <source.json> --to <cible.json> -o <sortie.nc>
  machine archive add <id> <programme.nc> --profile <profil.json> --author <nom> --store <dossier>
  machine archive list <id> --store <dossier>
  machine archive show <id> <révision> --store <dossier>
  machine archive export <id> <révision> --store <dossier> -o <sortie.nc>

Rapports JSON : stdout. Codes de sortie : 0 succès, 1 erreur/validation invalide,
2 analyse incomplète ou conversion refusée. Les sorties existantes ne sont pas écrasées.
Les profils du magasin se consultent/exportent avec profile show ; --profile lit un fichier.
```

## Commandes de meubles

```sh
fablabcam furniture template cabinet -o caisson.fcm-template.json
fablabcam furniture new caisson.fcm-template.json -o caisson.fcm.json --width 700
fablabcam furniture validate caisson.fcm.json
fablabcam furniture plan caisson.fcm.json
fablabcam furniture pack caisson.fcm.json -o fabrication.zip
```

`template shelving` crée une étagère. `new` accepte également `--depth`,
`--height`, `--thickness`, `--shelves` et `--profile`. Les sorties existantes sont
refusées. Un projet conserve son modèle et son profil CNC, indépendamment du
catalogue local du Studio. `plan` écrit le placement JSON sur stdout ; `pack`
crée un dossier géométrique sans G-code. Importez le natif dans **Meubles** pour
l'éditer dans l'interface. Voir le [guide meubles](../guide/meubles.md).

Pour un `.cb` associé à une machine par le module Meubles, `build` vérifie aussi
les opérations calculées et l'analyse du programme avec le profil attaché. Un
rapport incomplet ou invalide bloque l'écriture du G-code.
