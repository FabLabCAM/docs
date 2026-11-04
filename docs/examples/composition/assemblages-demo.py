"""Generate and validate the eight supported joint families with FabLabCAM 0.6.0.

Usage: python3 assemblages-demo.py /path/to/fablabcam new-output-directory
The output directory must not exist; no user documents are replaced.
"""
import copy
import json
from pathlib import Path
import subprocess
import sys
import zipfile

cli = str(Path(sys.argv[1]).resolve())
out = Path(sys.argv[2]).resolve()
out.mkdir(parents=True, exist_ok=False)

def run(*args):
    result = subprocess.run([cli, *map(str, args)], capture_output=True, text=True)
    if result.returncode:
        raise RuntimeError(result.stderr or result.stdout)
    return result.stdout

run('furniture', 'template', 'cabinet', '-o', out / 'base.fcm-template.json')
run('furniture', 'new', out / 'base.fcm-template.json', '-o', out / 'base.fcm.json',
    '--columns', 1, '--rows', 1)
base = json.loads((out / 'base.fcm.json').read_text())
results = []
for kind in ('butt', 'tabs', 'box', 'dado', 'rabbet', 'half_lap', 'mortise_tenon', 'tongue_groove'):
    doc = copy.deepcopy(base)
    doc['data']['id'] = 'demo-' + kind
    doc['data']['name'] = 'Démonstration ' + kind
    composition = doc['data']['dimensions']['composition']
    settings = dict(kind=kind, clearance=0.2, engagement=8.0, width=20.0,
                    count=3, blind=(kind == 'mortise_tenon'), relief='dogbone')
    composition['joints'] = {'SUP--C1-0-lo': settings}
    native = out / (kind + '.fcm.json')
    native.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + '\n')
    run('furniture', 'validate', native)
    run('furniture', 'pack', native, '-o', out / (kind + '.zip'))
    with zipfile.ZipFile(out / (kind + '.zip')) as package:
        assert package.testzip() is None
        operations = json.loads(package.read('operations.json'))
        (out / (kind + '-operations.json')).write_text(json.dumps(operations, indent=2) + '\n')
        results.append(dict(kind=kind, native_valid=True, files=len(package.namelist()),
                            reverse_setups=sum(n.endswith('-verso.cb') for n in package.namelist())))
(out / 'results.json').write_text(json.dumps(results, indent=2) + '\n')
print(json.dumps(results, indent=2))
