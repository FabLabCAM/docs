"""Check generated internal URLs, anchors and the current release references."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import json
import re
import yaml

root = Path(__file__).resolve().parents[1]
site = root / 'site'
class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.ids, self.links = set(), []
        self.feed(path.read_text(encoding='utf-8'))
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.add(attrs['id'])
        for key in ('href', 'src'):
            if key in attrs:
                self.links.append(attrs[key])

pages = {p.resolve(): Page(p) for p in site.rglob('*.html')}
errors = []
for path, page in pages.items():
    for link in page.links:
        url = urlsplit(link)
        if url.scheme or url.netloc or link.startswith('data:'):
            continue
        relative = unquote(url.path)
        if relative.startswith('/docs/'):
            target = site / relative.removeprefix('/docs/')
        elif relative.startswith('/'):
            target = site / relative.lstrip('/')
        elif relative:
            target = path.parent / relative
        else:
            target = path
        target = target.resolve()
        if target.is_dir():
            target /= 'index.html'
        if not target.exists():
            errors.append(f'{path.relative_to(site)}: missing {link}')
        elif url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
            errors.append(f'{path.relative_to(site)}: missing anchor {link}')
version = str(yaml.safe_load((root / 'mkdocs.yml').read_text())['extra']['product_version'])
for path in (root / 'docs/examples/machines').glob('*-report.json'):
    if json.loads(path.read_text())['analyzer_version'] != version:
        errors.append(f'{path.name}: analyzer version differs from {version}')
installation = (root / 'docs/installation.md').read_text()
for found in re.findall(r'releases/(?:tag|download)/v([\d.]+)', installation):
    if found != version:
        errors.append(f'installation: stale release {found}, expected {version}')
if f'**FabLabCAM {version}**' not in (root / 'docs/index.md').read_text():
    errors.append('index: version differs from mkdocs.yml')
if errors:
    raise SystemExit('\n'.join(errors))
print(f'{len(pages)} HTML pages checked; internal URLs, anchors and version {version} consistent.')
