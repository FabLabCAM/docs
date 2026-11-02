# Versions et licences

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
