# Suivi des issues et de la documentation

Cette page relie les changements publiés à leur issue, à leur guide et à leurs
notes de version. Les demandes en cours restent visibles dans les
[issues GitHub de core](https://github.com/FabLabCAM/core/issues) ; une demande
ouverte n'est pas une fonction disponible.

Résolu : [#23 — lancement dans Mach3](https://github.com/FabLabCAM/core/issues/23).
Le 6 novembre 2026, l'utilisateur confirme que les fichiers régénérés avec
0.7.1-rc.1 fonctionnent sur Mach3. Les correctifs de mode IJ et d'arcs dégénérés
sont [inclus dans la stable 0.7.1](https://github.com/FabLabCAM/core/releases/tag/v0.7.1).
Voir le [diagnostic et ses limites](../guide/gcode.md#mach3-fichier-charge-lancement-bloque).

| Version | Issue | Livraison | Documentation |
|---|---|---|---|
| [0.7.3](versions.md#073-compatibilite-des-fournisseurs) | [#20 — assistant](https://github.com/FabLabCAM/core/issues/20) | GPT-4.1 mini corrigé ; Ollama partiellement qualifié, issue ouverte | [Guide](../guide/assistant.md#compatibilite-des-fournisseurs-en-073) |
| [0.7.2](versions.md#072-profils-et-diagnostics) | [#24 — profil et diagnostics](https://github.com/FabLabCAM/core/issues/24) | Régressions DXF, protection des calculs, rapports persistants, export texte et core macOS sur demande | [Diagnostics](diagnostics.md), [index](fonctionnalites.md) |
| [0.7.1](versions.md#071-import-svg) | [#26 — import SVG](https://github.com/FabLabCAM/core/issues/26) | Transformations, ressources et nombres scientifiques corrigés ; logo vérifié | [Guide](../guide/fichiers.md#import-svg-corrige-en-071), [versions](versions.md#071-import-svg) |
| [0.7.0](versions.md#070-assistant-natif) | [#20 — assistant](https://github.com/FabLabCAM/core/issues/20) | Panneau natif, modes et actions validées ; qualification réelle des autres fournisseurs encore ouverte | [Guide illustré](../guide/assistant.md), [index](fonctionnalites.md) |
| [0.6.1](versions.md#061-identifiants-rhai) | [#19 — identifiants Rhai](https://github.com/FabLabCAM/core/issues/19) | Refus des références hors plage, atomicité et régressions | [Scripts](rhai.md#identifiants-des-formes), [index](fonctionnalites.md) |
| [0.6.0](versions.md#060-composition-et-assemblages) | [#17 — compositeur et assemblages](https://github.com/FabLabCAM/core/issues/17) | Éléments, cases, bacs, huit familles d’assemblages et modèles complets | [Guide](../guide/composer-meubles.md), [CLI](cli.md), [index](fonctionnalites.md) |
| [0.5.0](versions.md#050-meubles-parametriques) | [#14 — mobilier de FabLab](https://github.com/FabLabCAM/core/issues/14) | Modèles, meubles, assistant, découpe et dossiers de fabrication | [Guide illustré](../guide/meubles.md), [CLI](cli.md), [index](fonctionnalites.md) |
| [0.4.1](versions.md#041-id-cnc-pro-par-defaut) | [#9 — première machine](https://github.com/FabLabCAM/core/issues/9) | ID CNC PRO - Mach3 comme modèle par défaut et exemple | [Guide ID CNC PRO](../guide/id-cnc-pro.md), [Atelier](../guide/profils-studio.md) |
| [0.4.0](versions.md#040-atelier-des-profils-machine) | [#11 — Atelier et création guidée](https://github.com/FabLabCAM/core/issues/11) | Création, édition, duplication et import/export JSON dans le Studio | [Guide illustré](../guide/profils-studio.md), [raccourcis](raccourcis.md), [index](fonctionnalites.md) |
| [0.3.0](versions.md#030-profils-de-machine-et-g-code) | [#9 — gestion du G-code par machine](https://github.com/FabLabCAM/core/issues/9) | Profils JSON, validation, statistiques, conversion compatible, archives | [Guide machine](../guide/machines.md), [CLI](cli.md), [architecture](developpement.md) |
| [0.2.0](versions.md#020-premiere-release-publique) | Première publication | Studio, CLI, viewer et six cibles OS/architecture | [Installation](../installation.md), [index complet](fonctionnalites.md) |

## Complément assistant #20

En préparation : [division Ollama](../guide/assistant.md#division-ollama-correctif-en-preparation)
par outil natif simplifié, sans changement des paquets 0.7.3. La qualification
du catalogue complet reste ouverte.

Le correctif de compatibilité des fournisseurs est inclus dans 0.7.3 ;
voir les [résultats et limites](../guide/assistant.md#compatibilite-des-fournisseurs-en-073).
L’issue reste ouverte jusqu’à validation des critères restants.

## Complément diagnostics #24

Le 6 novembre 2026, l’utilisateur ne reproduit plus le crash des profils après
les derniers correctifs. L’issue #24 reste résolue. Le
[guide core dump](diagnostics.md#core-dump-sur-macos) précise le parcours dans
**FabLabCAM Diagnostic 0.7.3**, les préconditions, l’armement par session,
la récupération du fichier et la conservation du binaire avec son `dSYM`.
Un calcul réussi ne produit pas de core ; cette vérification de la compilation
et de l’interface n’est pas une nouvelle capture de panne.

## Limites de la livraison #9

L'analyse distingue les programmes valides, invalides et incomplets. Les cycles,
macros, transformations et compensations actives non interprétés sont signalés.
La conversion est limitée aux changements de format et alias compatibles ; elle
ne prétend pas traduire tous les dialectes. Le profil de référence concerne Mach3
Mill ; LinuxCNC, GRBL, Turn et la cinématique multiaxe restent des extensions futures.
La prévisualisation existante reste accessible avec `plot` et le viewer.

## Signaler une anomalie

Indiquez la version (`fablabcam version`), l'OS et l'architecture, les étapes,
le résultat attendu/observé et un exemple minimal. Pour `machine`, joignez le
rapport JSON et un profil expurgé des données privées. Les paramètres locaux
et macros ne doivent pas être présumés identiques entre deux installations.
Les vulnérabilités suivent [SECURITY.md](https://github.com/FabLabCAM/core/blob/main/SECURITY.md).

## Règle de maintien du guide

Chaque PR modifiant une fonction utilisateur doit mettre à jour sa procédure,
les exemples, l'index, les limites et les notes de version avec un lien d'issue.
Une capture est renouvelée si son interface change ; sa version d'origine reste
indiquée. Les exemples CLI sont exécutés contre le binaire documenté.

La CI construit MkDocs en mode strict et contrôle les liens internes, ancres,
rapports JSON et références de téléchargement avec `scripts/check_site.py`.

Avant publication : vérification des paquets,
contrôles CI, puis déploiement GitHub Pages depuis `main`. Les notes anciennes
restent accessibles. Le [processus de release](https://github.com/FabLabCAM/core/blob/v0.7.2/docs/releasing.md)
détaille l'ordre des vérifications et la clôture des issues après publication.
