# Maintaining FabLabCAM documentation

Architecture: MkDocs Material, static French documentation, GitHub Pages.
Document the released product rather than proposed capabilities. Keep examples,
installation asset names, supported targets and the version in mkdocs.yml aligned
with the public core release. Preserve .cb support and Apache-2.0 notices.

Screenshots must come from the real application with synthetic public examples.
Do not publish private paths, user projects, credentials or old product branding.
Use docs/examples/plaque.rhai and record the version and capture platform.
Update reference/fonctionnalites.md when adding or changing product features.

Validation: install requirements.txt with Python 3.12; run mkdocs build --strict;
verify internal links and assets; run changed CLI/Rhai examples against the
matching core version. Visually inspect representative pages before publishing.
Keep workflow actions pinned to full commits. Pull requests never deploy Pages.
Document limitations and actual test coverage. Do not claim machine validation
from a stock simulation. Keep commits small and explain the intent of changes.
