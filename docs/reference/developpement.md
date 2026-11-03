# Architecture, compilation et contribution

## Séparation des composants

```text
Studio graphique / CLI / Viewer
            ↓
     Projet et historique
            ↓
  Modèle géométrique → calcul FAO → G-code
                                      ↓
                         Backplot et simulation
```

| Crate Rust | Responsabilité |
|---|---|
| `fablabcam-geom` | Géométrie, contours et opérations géométriques |
| `fablabcam-model` | Modèle de document et lecture XML `.cb` |
| `fablabcam-cam` | Calcul des parcours et génération/post-traitement G-code |
| `fablabcam-backplot` | Relecture et visualisation des trajectoires |
| `fablabcam-studio` | Projet, édition, historique, outils, persistance et scripts |
| `fablabcam-cli` | Commandes testables et programme `fablabcam` |
| `fablabcam-view` | Studio egui et viewer natif |

Le projet conserve les formes, outils, opérations et brut. Les éditions passent
par l’historique ; les parcours calculés peuvent être invalidés puis recalculés.
Les interfaces ne constituent pas le modèle de données. Les tests de géométrie,
de profondeur et de persistance protègent les comportements partagés.

## Compiler le produit

```sh
git clone https://github.com/FabLabCAM/core.git
cd core
git checkout v0.3.0
cargo build --locked --release --workspace
cargo test --locked --workspace
cargo clippy --workspace --all-targets -- -D warnings
```

Installez Rust 1.89 ou supérieur et les outils de compilation de votre OS. Le workflow de
release utilise **Rust 1.99.1** et **Python 3.12**. Linux a besoin des en-têtes
X11/Xcursor/Xi/Xrandr, xkbcommon, Wayland, OpenGL et de `pkg-config`.
Les commandes et dépendances exactes sont dans le
[workflow de paquets](https://github.com/FabLabCAM/core/blob/v0.3.0/.github/workflows/packages.yml).

Les exécutables résultants sont `fablabcam`, `fablabcam-view` et
`fablabcam-studio-ui` (`.exe` sur Windows). Les tests ne doivent pas être
remplacés par la seule ouverture du Studio.

## Reproduire les paquets

Le workflow construit nativement les six architectures, exécute les tests,
compile les binaires optimisés puis assemble les distributions. Il collecte
les licences via `cargo-about`, les notices des polices et les sources des
dépendances qui le nécessitent. Le code de packaging est dans
[`packaging/`](https://github.com/FabLabCAM/core/tree/v0.3.0/packaging).

Les installateurs Windows sont créés avec NSIS ; macOS utilise les outils de
bundle et DMG du système ; Linux utilise `dpkg-deb`. Les archives incluent les
mêmes trois exécutables et notices. Le workflow de construction n’a pas de
permission de publication de release.

## Maintenir cette documentation

```sh
git clone https://github.com/FabLabCAM/docs.git
cd docs
python3.12 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/mkdocs serve
.venv/bin/mkdocs build --strict
```

Sous Windows, les commandes de l’environnement se trouvent dans `.venv\Scripts`.
La navigation est dans `mkdocs.yml`. Les pages sont dans `docs/`, les captures
dans `docs/assets/screenshots/`, les exemples dans `docs/examples/`.

Une pull request vérifie la construction sans publier. Après intégration dans
`main`, GitHub Actions déploie le site sur GitHub Pages. Les actions sont épinglées
par leur commit et les permissions d’écriture Pages sont limitées au déploiement.

Lors d’une nouvelle fonctionnalité, mettez à jour la procédure, une capture réelle,
les exemples concernés et l’[index des fonctionnalités](fonctionnalites.md).
Documentez les hypothèses et limites. Les commits doivent rester ciblés, avec
un message décrivant le changement ; une fonctionnalité annoncée doit être
vérifiable dans la version documentée.

Le module `fablabcam_cam::gcode::machine` porte le modèle pur de validation ;
`fablabcam_studio::gcode_store` porte les profils et révisions sur disque.
Le [suivi des issues](suivi.md) et les [versions](versions.md) relient chaque
fonction livrée à sa documentation.
