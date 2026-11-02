# FabLabCAM — documentation

Guide français de FabLabCAM Studio, ses outils CLI et son moteur CAO/FAO 2.5D.

- Site : https://fablabcam.github.io/docs/
- Produit : https://github.com/FabLabCAM/core
- Version documentée : **0.2.0**
- Licence : **Apache-2.0** (voir LICENSE).

## Développement local

```sh
python3.12 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/mkdocs serve
.venv/bin/mkdocs build --strict
```

Sous Windows, utiliser `.venv\Scripts\python` et `.venv\Scripts\mkdocs`.
Les captures sont prises dans le vrai Studio ; l'exemple reproductible est dans
`docs/examples/`. Les modifications de `main` sont publiées par GitHub Actions
sur GitHub Pages. Une pull request construit le site sans le publier.
