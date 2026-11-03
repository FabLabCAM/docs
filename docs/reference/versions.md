# Versions et licences

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
