"""Validate local links, catalog boundaries, source fingerprints and privacy patterns."""
import csv
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
errors = []
files = [p for p in ROOT.rglob('*') if p.is_file() and '.git' not in p.relative_to(ROOT).parts and '__pycache__' not in p.parts]
patterns = {
    'private-key': r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',
    'provider-key': r'\b(?:sk-proj-|sk-ant-|ghp_|github_pat_|AIza)[A-Za-z0-9_-]{20,}',
    'identity-number': r'\b\d{6}-[1-8]\d{6}\b',
    'absolute-home-path': r'/Users/[^\s\"\']+',
    'gmail-internal-link': r'https://mail\.google\.com/',
}
for p in files:
    if p.name == 'validate_portfolio.py':
        continue
    try:
        text = p.read_text(encoding='utf-8')
    except UnicodeDecodeError:
        errors.append(f'Unexpected binary: {p.relative_to(ROOT)}')
        continue
    for label, expression in patterns.items():
        if re.search(expression, text):
            errors.append(f'{label}: {p.relative_to(ROOT)}')
    if p.suffix == '.md':
        for link in re.findall(r'\]\(([^)]+)\)', text):
            if urlsplit(link).scheme or link.startswith('#'):
                continue
            rel = unquote(link.split('#')[0])
            if rel and not (p.parent / rel).exists():
                errors.append(f'Broken relative link in {p.relative_to(ROOT)}: {rel}')
catalog = json.loads((ROOT / 'evidence/repositories.json').read_text())
assert len(catalog) == len({r['name'] for r in catalog})
assert all(r['url'].startswith('https://github.com/estona815/') for r in catalog)
assert sum(r['is_fork'] for r in catalog) == 1
for row in json.loads((ROOT / 'samples/source-manifest.json').read_text()):
    actual = hashlib.sha256((ROOT / row['published_path']).read_bytes()).hexdigest()
    if actual != row['export_sha256']:
        errors.append('Sample SHA mismatch: ' + row['published_path'])
for row in csv.DictReader((ROOT / 'evidence/public-claims.csv').open(encoding='utf-8')):
    if not row['immutable_source_url'].startswith('https://'):
        errors.append('Public claim missing URL')
if errors:
    raise SystemExit('\n'.join(errors))
print(json.dumps({'status':'PASS','files':len(files),'public_repositories':len(catalog),'relative_links':'PASS','source_hashes':'PASS','selected_privacy_patterns':'PASS'},ensure_ascii=False))
