# FabLabCAM — du dessin au parcours d’outil

**FabLabCAM 0.2.0** est un atelier de CAO/FAO 2.5D, libre sous licence
Apache-2.0. Dessinez une pièce, définissez vos outils, préparez les opérations,
inspectez le résultat et exportez le G-code.

[Installer FabLabCAM](installation.md){ .md-button .md-button--primary }
[Créer votre première plaque](guide/premier-projet.md){ .md-button }

[![FabLabCAM Studio et le projet de plaque](assets/screenshots/01-interface.png)](assets/screenshots/01-interface.png)

## Trois façons de travailler

| Composant | Usage |
|---|---|
| **Studio** | Interface graphique : dessin, outils, usinage, brut et simulation |
| **CLI `fablabcam`** | Conversion, génération, scripts Rhai, simulation et exports web |
| **Viewer `fablabcam-view`** | Inspection interactive d’un G-code existant |

Le projet natif utilise l’extension **`.cb`**. Les échanges de dessin utilisent
DXF et SVG. Les quatre opérations disponibles sont **profil, poche, perçage et
gravure**. La vue 3D représente la matière calculée par la simulation ; ce
n’est pas un modeleur de solides ni une FAO multiaxe.

## Un parcours guidé

1. [Installer](installation.md) la version adaptée à votre ordinateur.
2. [Ouvrir la plaque d’exemple](guide/premier-projet.md).
3. [Découvrir le dessin](guide/dessin.md) et [la table d’outils](guide/outils.md).
4. [Configurer l’usinage](guide/operations.md), puis [simuler](guide/simulation.md).
5. [Exporter et contrôler le G-code](guide/gcode.md).

L’[index des fonctionnalités](reference/fonctionnalites.md) relie chaque famille
fonctionnelle à sa procédure et à une capture. Toutes les captures du Studio
proviennent de la version 0.2.0 sur macOS Apple Silicon, avec un dessin créé pour
ce guide. Les dialogues système et polices peuvent varier selon l’OS.

!!! info "Première version publique"
    Le guide décrit les fonctions implémentées et leurs [limites connues](reference/depannage.md).
    Les exemples servent à apprendre le logiciel. Les réglages de coupe et le
    programme machine doivent être adaptés à votre équipement et au bridage.
