#!/usr/bin/env python3
"""Confere integridade da captura CTR2 e marcadores CTR/CTR2."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parent
manifest = json.loads((ROOT / 'manifesto-captura-ctr2.json').read_text(encoding='utf-8'))
control = re.compile(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x80-\x9f]')
count = 0
for path in ROOT.iterdir():
    if path.is_file() and path.suffix in ('.md', '.json', '.py'):
        text = path.read_text(encoding='utf-8')
        assert not control.search(text), f'controle: {path}'
        assert '\ufffd' not in text, f'U+FFFD: {path}'
        count += 1
for record in manifest['anexos']:
    path = ROOT / record['arquivo']
    assert path.is_file(), path
    data = path.read_bytes()
    if 'sha256_arquivo' in record:
        assert hashlib.sha256(data).hexdigest() == record['sha256_arquivo'], path
        assert len(data) == record['bytes'], path
    else:
        text = data.decode('utf-8')
        if record['arquivo'].startswith('contran-1031'):
            body = text.split('```text\n', 1)[1].rsplit('```\n', 1)[0]
        else:
            body = text.split('\n---\n\n', 1)[1]
        assert len(body) == record['caracteres_corpo'], path
        assert hashlib.sha256(body.encode()).hexdigest() == record['sha256_corpo'], path
for marker in ('DONE', 'DONE-CTR2'):
    assert (ROOT / marker).read_bytes() == b'', marker
print(f'PASS: {count} textos UTF-8, controles=0, U+FFFD=0, hashes={len(manifest["anexos"])} e marcadores vazios')
