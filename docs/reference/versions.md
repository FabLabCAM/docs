# Versions et licences

## 0.7.2 — Profils et diagnostics

[Release et installateurs](https://github.com/FabLabCAM/core/releases/tag/v0.7.2) · [Issue #24](https://github.com/FabLabCAM/core/issues/24) · [Guide](diagnostics.md)

Correction de l'offset des contours DXF avec fermeture répétée, protection du
calcul et refus d'export d'un parcours obsolète. Préférences de diagnostic avec
journaux bornés, piles persistantes, export texte et core macOS sur demande.
Compilation de diagnostic distincte avec dSYM ; paquets normaux sans nouvelle
permission de débogage. Les autres OS conservent les rapports texte.

Le DXF réel et les tests synthétiques passent localement ; le profil des 19
formes affiche 32 415 mouvements dans l'interface. Une panique contrôlée a produit
un core ouvert dans LLDB avec ses lignes source. La version reprend aussi les
correctifs d'arcs et de modes IJ de la préversion ci-dessous ; #23 reste ouverte
pour les trois essais Mach3 encore attendus. Les contrôles de distribution sont
consignés dans les notes de release. Les correctifs SVG de 0.7.1 sont conservés ; ses paquets restent inchangés.


## 0.7.1 — Import SVG

[Release et installateurs](https://github.com/FabLabCAM/core/releases/tag/v0.7.1) ·
[Issue #26](https://github.com/FabLabCAM/core/issues/26) ·
[PR core #28](https://github.com/FabLabCAM/core/pull/28)

- Transformations imbriquées et locales appliquées avant l'inversion Y.
- Définitions et ressources inutilisées exclues du dessin importé.
- Nombres scientifiques et commandes implicites lus correctement ; erreurs
  explicites pour les chemins ou transformations invalides.
- Arcs circulaires préservés sous similitude et approximés sous transformation
  non uniforme. [Guide et limites](../guide/fichiers.md#import-svg-corrige-en-071).

Le logo signalé retrouve ses 10 contours et un encombrement de 39,5 × 39,5 mm,
sans avertissement d'import. Les régressions moteur/CLI et le contrôle visuel
sont décrits dans le [rapport QA](https://github.com/FabLabCAM/core/blob/v0.7.1/docs/qa/issue-26.md).
La validation des paquets est consignée dans les notes de release.

Cette version reprend aussi les correctifs Mach3 de 0.7.1-rc.1 détaillés ci-dessous.
Le retour sur les trois autres fichiers KO reste attendu :
[#23](https://github.com/FabLabCAM/core/issues/23) reste ouverte. La publication
ne vaut pas qualification d'une machine réelle.

## Préversion 0.7.1-rc.1 — validation Mach3

[Diagnostic Mach3](../guide/gcode.md#mach3-fichier-charge-lancement-bloque) :
subdivision des arcs dégénérés après arrondi, contrôle du rayon final nul,
préambules explicites, tolérance d'arc en pouces et distinction de G91.1/G91
dans le backplot. La [préversion est disponible](https://github.com/FabLabCAM/core/releases/tag/v0.7.1-rc.1) pour les essais Mach3 ;
ces changements sont également inclus dans la stable 0.7.1. Le
[gabarit CBPP](../examples/mach3-explicit-modes.cbpp) permet déjà de comparer
les modes des exports en 0.7.0, dont le backplot reste incorrect pour G91.1 ;
il ne corrige pas les micro-arcs dégénérés.
Le cas `lyon3.v1` est reproduit en mode IJ initial absolu et couvert par le
préambule explicite. L'utilisateur confirme le 4 novembre 2026 que la copie
ajoutant G91.1 fonctionne dans Mach3. Les trois autres KO restent à confirmer ;
la qualification reste partielle et [#23](https://github.com/FabLabCAM/core/issues/23)
reste ouverte.

## 0.7.0 — Assistant natif

[Release et installateurs](https://github.com/FabLabCAM/core/releases/tag/v0.7.0) · [Issue #20](https://github.com/FabLabCAM/core/issues/20)

- Panneau Rust/egui commun aux pages, Markdown, contexte choisi et historique local.
- Ask en lecture seule, Plan sur copie et Agent avec aperçu puis validation par lot.
- Actions dessin, Rhai, meubles, assemblages, outils, opérations et exports natifs.
- Streaming OpenAI Responses, Claude Messages, Mistral et Ollama ; coffre système,
  annulation, limites, diagnostics et refus des propositions obsolètes.
- Scripts manuels et préparation des dossiers ZIP hors du rendu graphique.
- [Guide illustré](../guide/assistant.md), mémoire, architecture et
  [QA sources](https://github.com/FabLabCAM/core/blob/v0.7.0/docs/qa/0.7.0.md).

387 tests locaux réussis sur macOS Apple Silicon et Clippy strict ; compilation vérifiée avec Rust 1.89. Mistral Small
a été testé réellement ; les trois autres fournisseurs ont des tests de protocole
locaux et restent à qualifier en conditions réelles. L’issue #20 reste ouverte
pour ce suivi. La simulation et les valeurs d’outils ne qualifient aucune CNC.

Distribution validée : tests workspace et Clippy réussis sur les trois OS,
six constructions natives macOS/Windows/Linux en ARM64 et x64. Les douze paquets
publiés ont été contrôlés : SHA-256, licences et sources requises, architectures
des dix-huit exécutables. Les installations Debian/Windows sont vérifiées en CI.
Le DMG macOS ARM64 issu de cette CI a été installé : signature ad hoc, CLI 0.7.0,
script public de la plaque (21 formes, 4 opérations) et interface réelle avec
simulation et panneau assistant vérifiés. Les 36 pages du guide passent la
construction stricte et le contrôle des liens ; six captures réelles illustrent
l’assistant. Les tests automatisés des autres plateformes ne remplacent pas une
revue graphique manuelle.
[CI](https://github.com/FabLabCAM/core/actions/runs/41858524147) ·
[Paquets](https://github.com/FabLabCAM/core/actions/runs/41858524071).

## 0.6.1 — Identifiants Rhai

[Release et installateurs](https://github.com/FabLabCAM/core/releases/tag/v0.6.1) · [Issue #19](https://github.com/FabLabCAM/core/issues/19)

- Refus des identifiants négatifs ou supérieurs à `4294967295`, seuls ou dans
  un tableau, dans toutes les fonctions Rhai qui prennent des références de formes.
- Une valeur hors plage ne peut plus désigner une autre forme par troncature.
  Le diagnostic indique la valeur fautive et la position dans le script.
- Tests de régression sur les dix fonctions concernées, les bornes, les types,
  l’atomicité du projet et de l’historique et la préservation des fichiers CLI.
- [Guide Rhai](rhai.md#identifiants-des-formes), mémoire et architecture actualisés.

Les formats et l’API des identifiants valides restent inchangés. Le script
prérempli crée du dessin ; il ne définit pas d’opérations d’usinage. L’API Rhai
n’expose pas le compositeur de meubles.

Validation : **364 tests sur macOS/Linux, 363 sur Windows**, sur les six cibles
natives, et Clippy strict. Les douze paquets ont été contrôlés : SHA-256, licences,
sources requises et architectures des exécutables. Installation Debian/Windows
vérifiée en CI ; DMG macOS ARM64, CLI installée et parcours graphique Rhai vérifiés
localement, avec une [capture réelle](rhai.md#identifiants-des-formes).
Les exemples du guide et ses 35 pages passent la construction stricte et le
contrôle des liens. [QA sources](https://github.com/FabLabCAM/core/blob/v0.6.1/docs/qa/0.6.1.md)
· [CI](https://github.com/FabLabCAM/core/actions/runs/41839539722)
· [Paquets](https://github.com/FabLabCAM/core/actions/runs/41839539374).

## 0.6.0 — Composition et assemblages

[Release et installateurs](https://github.com/FabLabCAM/core/releases/tag/v0.6.0) · [Issue #17](https://github.com/FabLabCAM/core/issues/17)

- Compositeur visuel : tablettes, séparations, cases, grilles et bacs amovibles.
- Dimensions utiles, épaisseurs individuelles, positions fixes/égales,
  duplication, répétition, suppression confirmée et annuler/rétablir.
- Huit familles orthogonales d’assemblages, défaut général et surcharges, jeu total,
  dogbone/T-bone, variantes borgnes/traversantes et contours complémentaires.
- Modèles et projets complets en schéma 2, lecture du schéma 1 et migration explicite.
- Plans, manifestes d’opérations et d’assemblages, montages verso, placement par
  épaisseur et contrôle des opérations requises avant le G-code.
- [Guide illustré et exemples](../guide/composer-meubles.md), mémoire, architecture,
  formats et [QA sources](https://github.com/FabLabCAM/core/blob/v0.6.0/docs/qa/0.6.0.md).

359 tests sur macOS/Linux (358 sur Windows), Clippy strict et compatibilité Rust 1.89.
Les six cibles natives produisent douze paquets. Les familles complémentaires sont
désactivées ; les variantes inclinées, coulisses, quincaillerie et calcul de tenue
ne sont pas inclus. Les opérations, le bridage et les retournements restent à
préparer ; aucun G-code automatique n’est livré dans les dossiers.

## 0.5.0 — Meubles paramétriques

[Release et installateurs](https://github.com/FabLabCAM/core/releases/tag/v0.5.0) · [Issue #14](https://github.com/FabLabCAM/core/issues/14)

- Espace **Meubles**, bibliothèques de modèles et de projets, assistant en quatre
  étapes et aperçus assemblé/éclaté avec repères des panneaux.
- Caissons et étagères vissés : dimensions, épaisseur, dos et tablettes. Modèles
  révisés sans modifier les meubles existants ; copie du profil CNC par projet.
- Création, édition, duplication, annulation/rétablissement, sauvegarde et
  import/export natif avec aperçu, contrôle du format et copie des doublons.
- Placement rectangulaire sur plusieurs dalles, marges, espacement et rotations ;
  refus d'un dossier partiel quand une pièce ne rentre pas.
- ZIP avec plans CB/DXF/SVG, CSV, PDF et natif facultatif ; transfert d'une dalle
  en FAO. Le profil attaché au CB contrôle l'export G-code natif et `build`.
- Commandes CLI `furniture` et [guide illustré](../guide/meubles.md), avec sept
  captures réelles et un exemple reproductible de six pièces sur trois dalles.

Les formats `.fcm-template.json` et `.fcm.json` utilisent le schéma 1. Le dessin
`.cb`, les sept crates et la licence Apache-2.0 sont conservés. Les douze paquets
couvrent macOS, Windows et Linux en x64/ARM64.

Le placement est heuristique. Les opérations, le bridage et le post-processeur
restent à préparer ; aucun G-code n'est inclus dans le ZIP. Les pièces trop
grandes, profils incomplets et analyses partielles ne sont pas présentés comme
validés. Portes, tiroirs, assemblages usinés, quincaillerie et charges admissibles
restent hors périmètre V1.


Validation complémentaire du 4 novembre 2026 : parcours graphique du DMG
Apple Silicon, export ZIP depuis le Studio, import en copie, transfert en FAO et
persistance après relance vérifiés ; les sept captures du guide proviennent du
binaire publié. [Compte rendu](https://github.com/FabLabCAM/core/blob/main/docs/qa/0.5.0.md).

## 0.4.1 — ID CNC PRO par défaut

[Release et installateurs](https://github.com/FabLabCAM/core/releases/tag/v0.4.1) · [Issue #9](https://github.com/FabLabCAM/core/issues/9)

- **ID CNC PRO - Mach3** devient le modèle de création du Studio et de la CLI.
- Initialisation d’une bibliothèque vide, sélection du profil et conservation
  des personnalisations existantes ; tests des ouvertures concurrentes.
- [Exemple JSON et guide](../guide/id-cnc-pro.md), sources, caractéristiques
  nominales et captures réelles du Studio 0.4.1 sur macOS Apple Silicon.
- Les paramètres locaux non confirmés restent absents et le rapport initial
  reste incomplet. Les profils générique et fictif restent disponibles.

Les douze paquets couvrent macOS, Windows et Linux en x64/ARM64. Le schéma JSON
reste en version 1. Cette correction complète la première machine de l’issue #9.

## 0.4.0 — Atelier des profils machine

[Release et installateurs](https://github.com/FabLabCAM/core/releases/tag/v0.4.0) · [Issue #11](https://github.com/FabLabCAM/core/issues/11)

- Nouvel espace **Profils machine · Atelier** dans le Studio : bibliothèque,
  édition, duplication et import/export JSON.
- Parcours guidé en quatre étapes, valeurs inconnues préservées, récapitulatif
  des paramètres restant à renseigner et sauvegarde des profils partiels.
- Formulaires des axes, de la broche et du G-code ; JSON avancé complet.
- Confirmation des brouillons, choix explicite pour les doublons d’import,
  refus des conflits concurrents et protection de la fermeture native macOS.
- [Guide illustré](../guide/profils-studio.md) avec neuf captures réelles ;
  documentation, index et suivi des issues actualisés.

Les profils conservent le schéma JSON 1. Le dessin `.cb`, les archives G-code
et la licence Apache-2.0 sont préservés. Les états « À configurer » et « Champs
renseignés » décrivent des paramètres, pas une qualification de machine.
La validation des programmes, la conversion et les archives restent en CLI/API.
Le profil ne sélectionne pas automatiquement le post-processeur du dessin.

Les distributions couvrent macOS, Windows et Linux en x64/ARM64. Les tests
comprennent la conservation des paramètres avancés, les imports invalides, les
écritures concurrentes, les exports sans écrasement et les archives immuables.
Les parcours graphiques illustrés ont été vérifiés sur macOS Apple Silicon.

## 0.3.0 — profils de machine et G-code

Publiée le **3 novembre 2026** · [Release et installateurs](https://github.com/FabLabCAM/core/releases/tag/v0.3.0) · [Issue #9](https://github.com/FabLabCAM/core/issues/9)

- Profils JSON et référence **Mach3 Mill** sourcée ; exemple fictif configuré.
- `fablabcam machine` : CRUD, parseur tolérant, validation ligne/colonne,
  bornes XYZ incluant les extrema d'arcs, longueurs, durées estimées et outils.
- Contrôle des codes, préambules, courses, avances et broche ; statuts explicites
  `valid`, `invalid`, `incomplete` et rapports JSON.
- Conversion compatible des formats/alias avec liste des obstacles et refus
  de toute perte de précision ; validation de la cible avant écriture.
- Archives locales versionnées : programme, instantané du profil et du rapport,
  auteur, date, SHA-256, verrouillage et contrôle d'intégrité.
- `fablabcam version` / `--version`, profils inclus dans les douze paquets,
  nouveau guide et suivi des issues/documentation.

Le [guide machine](../guide/machines.md) contient les commandes et exemples.
La fonction est accessible en CLI/API Rust. Les cycles, macros, compensations
actives et transformations non interprétés restent incomplets ; ils ne sont pas
convertis. Les captures du Studio restent celles de la v0.2.0 : son interface
n'a pas changé. Les projets `.cb` et la licence Apache-2.0 sont conservés.

Les paquets couvrent macOS, Windows et Linux, chacun en x64/ARM64. Les tests
incluent les cas valides/invalides, arcs et unités, conversions refusées,
révisions concurrentes et archives altérées. La compilation nécessite Rust 1.89+
(distributions : 1.99.1). Les rapports ne certifient aucune machine physique.

## 0.2.0 — première release publique

[Ouvrir la release](https://github.com/FabLabCAM/core/releases/tag/v0.2.0)

Cette première publication distribue le Studio, la CLI et le viewer sur macOS,
Windows et Linux, chacun en x64 et ARM64. Elle inclut le dessin 2D, les outils,
les quatre opérations d’usinage, les ponts, les post-processeurs, les scripts
Rhai, la simulation de matière et les exports d’inspection.

Les paquets contiennent des installateurs natifs et des archives portables,
avec une liste de sommes SHA-256. Les détails de validation et les éventuelles
restrictions propres à la distribution sont indiqués dans les notes de release.

Les 22 captures du Studio et la capture du backplot web ont été prises sur macOS Apple Silicon.
Elles utilisent l’exemple public de plaque et, pour certaines, une variante
avec ponts automatiques. Les dialogues système peuvent différer selon l’OS.

## Licence du projet et de la documentation

Le code FabLabCAM et cette documentation sont publiés sous **Apache License 2.0**.
Les textes complets sont disponibles dans
[core/LICENSE](https://github.com/FabLabCAM/core/blob/main/LICENSE) et
[docs/LICENSE](https://github.com/FabLabCAM/docs/blob/main/LICENSE).
Les fichiers NOTICE accompagnent les distributions.

Les dépendances conservent leurs propres licences. Les paquets incluent
`THIRD-PARTY-LICENSES.html`, les notices des polices et une archive de sources
correspondantes pour la dépendance MPL concernée. La licence du projet ne
relicencie pas automatiquement ces composants tiers.

Les dessins et scripts pédagogiques de ce guide sont créés pour FabLabCAM et
publiés avec la documentation. Les sorties G-code illustrent le comportement
du logiciel ; elles ne constituent pas une qualification d’un procédé machine.

## Dépôts

- [Produit et moteur Rust](https://github.com/FabLabCAM/core)
- [Sources du guide MkDocs](https://github.com/FabLabCAM/docs)
- [Organisation FabLabCAM](https://github.com/FabLabCAM)
