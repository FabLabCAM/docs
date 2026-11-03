# FabLabCAM — du dessin au parcours d’outil

**FabLabCAM 0.4.1** est un atelier de CAO/FAO 2.5D, libre sous licence
Apache-2.0. Dessinez une pièce, définissez vos outils, préparez les opérations,
inspectez le résultat et exportez le G-code.

[Installer FabLabCAM](installation.md){ .md-button .md-button--primary }
[Créer votre première plaque](guide/premier-projet.md){ .md-button }

[![FabLabCAM Studio et le projet de plaque](assets/screenshots/01-interface.png)](assets/screenshots/01-interface.png)

## Trois façons de travailler

| Composant | Usage |
|---|---|
| **Studio** | Interface graphique : dessin, outils, usinage, brut, simulation et profils machine |
| **CLI `fablabcam`** | Génération, scripts, simulation, profils de machine, validation et archives G-code |
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
fonctionnelle à sa procédure et à une capture. Les captures du dessin proviennent de la version 0.2.0 ; celles de l’Atelier
proviennent des versions 0.4.0 et 0.4.1. Elles sont prises sur macOS Apple Silicon
avec des exemples publics créés pour ce guide. Les dialogues système et polices peuvent varier selon l’OS.

!!! info "Nouveau dans la v0.4.1"
    [ID CNC PRO - Mach3](guide/id-cnc-pro.md) devient le modèle par défaut du Studio
    et de la CLI, avec un exemple JSON sourcé et des paramètres locaux à compléter.

!!! info "Atelier des profils machine"
    [Créez et modifiez vos profils machine dans l’Atelier du Studio](guide/profils-studio.md),
    avec un parcours guidé et des échanges JSON. La [validation G-code](guide/machines.md) reste disponible en CLI.
    Consultez les [notes de version](reference/versions.md) et le [suivi des issues](reference/suivi.md).

!!! info "Guide du produit"
    Le guide décrit les fonctions implémentées et leurs [limites connues](reference/depannage.md).
    Les exemples servent à apprendre le logiciel. Les réglages de coupe et le
    programme machine doivent être adaptés à votre équipement et au bridage.
