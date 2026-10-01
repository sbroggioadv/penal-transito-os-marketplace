#!/usr/bin/env python3
"""Reproduz os recortes CTR2 a partir de snapshots oficiais baixados."""
from html.parser import HTMLParser
from pathlib import Path
import argparse
import hashlib
import html
import json
import re
import shutil
import subprocess


class Extrator(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.parts = []
        self.lines = []

    def flush(self):
        if not self.parts:
            return
        chars = [(char, flag) for part, flag in self.parts for char in part]
        out = []
        last = False
        space = False
        for char, flag in chars:
            if char.isspace():
                space = True
                continue
            if space and out:
                out.append(' ')
            space = False
            if flag != last:
                out.append('~~')
                last = flag
            out.append(char)
        if last:
            out.append('~~')
        line = ''.join(out).strip()
        if line:
            self.lines.append(line)
        self.parts = []

    def handle_starttag(self, tag, attrs):
        if tag in ('p', 'div', 'tr', 'h1', 'h2', 'h3', 'h4', 'li', 'br'):
            self.flush()
        if tag in ('br', 'meta', 'link', 'img', 'input', 'hr'):
            return
        style = dict(attrs).get('style', '')
        struck = tag in ('strike', 's', 'del') or bool(re.search('text-decoration[^;]*line-through', style, re.I))
        self.stack.append((tag, struck))

    def handle_endtag(self, tag):
        if tag in ('p', 'div', 'tr', 'h1', 'h2', 'h3', 'h4', 'li'):
            self.flush()
        for i in range(len(self.stack)-1, -1, -1):
            if self.stack[i][0] == tag:
                self.stack = self.stack[:i]
                break

    def handle_data(self, data):
        if any(tag in ('head', 'script', 'style') for tag, _ in self.stack):
            return
        self.parts.append((data, any(flag for _, flag in self.stack)))


def sha(data):
    return hashlib.sha256(data).hexdigest()


def parse(path):
    raw = path.read_bytes()
    try:
        text = raw.decode('utf-8')
        encoding = 'utf-8'
    except UnicodeDecodeError:
        text = raw.decode('cp1252')
        encoding = 'cp1252'
    parser = Extrator()
    parser.feed(text)
    parser.flush()
    return parser.lines, encoding, sha(raw)


ART = re.compile(r'^Art\.?\s*(\d+(?:\.\d{3})*)[ºo°]?(?:-([A-Z]))?(?=[.\s:–-])')


def article(line):
    match = ART.match(line.replace('~~', ''))
    return (int(match[1].replace('.', '')), match[2] or '') if match else None


def keys(lines):
    result = []
    for line in lines:
        key = article(line)
        if key and key not in result:
            result.append(key)
    return result


def block(lines, key):
    starts = [i for i, line in enumerate(lines) if article(line) == key]
    assert starts, f'Artigo ausente: {key}'
    start = starts[0]
    end = next((i for i in range(start+1, len(lines)) if article(lines[i]) and article(lines[i]) != key), len(lines))
    result = lines[start:end]
    while result and (re.match(r'^(?:CAPÍTULO|Se[cç][aã]o|TÍTULO|LIVRO)', result[-1]) or (len(result) > 1 and re.match(r'^(?:CAPÍTULO|Se[cç][aã]o|TÍTULO|LIVRO)', result[-2]))):
        result = result[:-1]
    return result


URLS = {
    'cp': 'https://www.planalto.gov.br/ccivil_03/decreto-lei/del2848compilado.htm',
    'cpp': 'https://www.planalto.gov.br/ccivil_03/decreto-lei/del3689compilado.htm',
    'antt': 'https://anttlegis.antt.gov.br/action/ActionDatalegis.php?acao=abrirTextoAto&cod_menu=7145&cod_modulo=420&desItem=&desItemFim=&nomeTitulo=codigos&numeroAto=00001031&orgao=CONTRAN%2FMT&seqAto=000&tipo=RES&valorAno=2026',
    'contran-pdf': 'https://www.gov.br/transportes/pt-br/assuntos/transito/conteudo-contran/resolucoes/resolucao10312026.pdf',
}
CP = {1, 2, 10, 82, 91, 108} | set(range(45, 53)) | set(range(60, 72)) | set(range(110, 115)) | set(range(116, 121))
CPP = {28, 31, 38, 63, 271, 282, 283, 311, 317, 318, 320, 387, 394, 396, 399, 798} | set(range(69, 92)) | set(range(155, 185)) | set(range(268, 274)) | set(range(313, 317)) | set(range(400, 406)) | set(range(563, 621)) | set(range(647, 668))


def run(source_dir, destino):
    destino.mkdir(parents=True, exist_ok=True)
    records = []
    sources = {}
    for key, wanted in (('cp', CP), ('cpp', CPP)):
        path = source_dir / f'{key}.html'
        lines, encoding, source_hash = parse(path)
        available = keys(lines)
        missing = sorted(wanted - {number for number, _ in available})
        assert not (set(missing) - ({611} if key == 'cpp' else set())), f'{key}: artigos ausentes {missing}'
        selected = [item for item in available if item[0] in wanted or (key == 'cpp' and item[0] == 158 and item[1] in 'ABCDEF') or (key == 'cpp' and item == (396, 'A'))]
        chunks = []
        for item in selected:
            chunks.extend(block(lines, item))
        marked = []
        for line in chunks:
            if re.match(r'^(?:Art\.|§|Parágrafo|[IVXLCDM]+\s*[-–])', line) and re.search(r'\(?[Rr]evogad[oa](?: pela|\))', line) and '~~' not in line:
                line = '~~' + line + '~~'
            marked.append(line)
        body = '\n\n'.join(marked) + '\n'
        assert '\ufffd' not in body and not re.search(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x80-\x9f]', body)
        assert re.sub(r'\s+', ' ', body.replace('~~', '')).strip() == re.sub(r'\s+', ' ', ' '.join(chunks).replace('~~', '')).strip()
        name = f'codigo-penal-complemento-ctr2.md' if key == 'cp' else 'cpp-complemento-ctr2.md'
        title = 'Código Penal — dispositivos complementares CTR2' if key == 'cp' else 'Código de Processo Penal — dispositivos complementares CTR2'
        header = f'''# {title}

- **Fonte oficial:** Planalto — Presidência da República.
- **URL:** {URLS[key]}
- **Data da captura:** 01/10/2026.
- **HTTP:** 200.
- **SHA-256 do HTML:** `{source_hash}`.
- **Decodificação:** {encoding} estrita; saída UTF-8.
- **Método:** download direto; HTMLParser (stdlib), sem reescrita por modelo. Entidades HTML decodificadas e espaços/quebras de layout normalizados. Tags/links removidos com seu texto preservado; scripts, estilos e head técnico excluídos. Tachados da fonte convertidos em `~~texto~~`; dispositivos com marcadores literais de revogação adicionalmente tachados. Sem normalização Unicode NFC/NFD nem correção editorial.
- **Escopo:** artigos listados no manifesto CTR2; blocos integrais conforme a página compilada. Não equivale a uma linha do tempo legislativa.
- **Reprodução:** `python3 capturar-ctr2.py --fontes /tmp/ctr2-sources --destino /tmp/ctr2-recaptura`.

---

'''
        (destino / name).write_text(header + body, encoding='utf-8')
        records.append({'arquivo': name, 'fonte': key, 'artigos': [str(n) + ('-' + suffix if suffix else '') for n, suffix in selected], 'caracteres_corpo': len(body), 'sha256_corpo': sha(body.encode()), 'linhas_tachadas': sum('~~' in line for line in marked)})
        sources[key] = {'url': URLS[key], 'http': 200, 'encoding': encoding, 'sha256_fonte': source_hash, 'bytes_fonte': path.stat().st_size}
    antt = source_dir / 'antt.html'
    antt_raw = antt.read_bytes()
    antt_lines, antt_encoding, antt_hash = parse(antt)
    assert all(any(article(line) == (n, '') for line in antt_lines) for n in range(1, 17))
    sources['antt'] = {'url': URLS['antt'], 'http': 200, 'encoding': antt_encoding, 'sha256_fonte': antt_hash, 'bytes_fonte': len(antt_raw)}
    pdf = source_dir / 'doui.pdf'
    pdf_raw = pdf.read_bytes()
    assert pdf_raw.startswith(b'%PDF-')
    pdf_name = 'contran-1031-2026-integral.pdf'
    shutil.copyfile(pdf, destino / pdf_name)
    pdf_text = subprocess.run(['pdftotext', '-layout', '-nopgbrk', str(pdf), '-'], check=True, capture_output=True).stdout.decode('utf-8')
    assert all(re.search(rf'Art\. {n}\.', pdf_text) for n in range(10, 17))
    assert all(f'ANEXO {roman}' in pdf_text for roman in ('I', 'II', 'III'))
    assert 'Fica revogada a Resolução Contran nº 432' in pdf_text
    assert '\ufffd' not in pdf_text
    # O Anexo III é imagem no PDF oficial. O PDF preserva integralmente as páginas.
    text_body = pdf_text.rstrip() + '\n'
    text_name = 'contran-1031-2026-texto-extraivel.md'
    header = f'''# Resolução Contran nº 1.031/2026 — texto extraível e fonte integral

- **Fonte oficial principal:** Diário Oficial da União, PDF publicado no portal gov.br, edição 155-B, seção 1 - Extra B, 18/08/2026.
- **URL do PDF integral:** {URLS['contran-pdf']}
- **Cópia integral:** [{pdf_name}]({pdf_name}); 20 páginas, incluindo os Anexos I, II e III.
- **Fonte oficial de conferência:** ANTTlegis, arts. 1º–16 e link para anexos: {URLS['antt']}
- **Data da captura:** 01/10/2026.
- **HTTP:** 200 em ambas as fontes.
- **SHA-256 do PDF:** `{sha(pdf_raw)}`.
- **SHA-256 do HTML ANTTlegis:** `{antt_hash}`.
- **Método:** download direto; `pdftotext -layout -nopgbrk` (Poppler), sem reescrita por modelo; saída UTF-8 estrita. Sem normalização Unicode NFC/NFD nem correção editorial.
- **Limite da camada textual:** as páginas 12–20, que contêm o Anexo III, são imagens no PDF e não produzem texto normativo por `pdftotext`; consulte a cópia integral para ler esse anexo. Esta camada não é transcrição integral nem OCR verificado.
- **Vigência:** arts. 1º–13, 15 e 16 desde 18/08/2026; art. 14 e alteração do Anexo da Resolução nº 985/2022 após 60 dias da publicação (art. 16, I).
- **Reprodução:** `python3 capturar-ctr2.py --fontes /tmp/ctr2-sources --destino /tmp/ctr2-recaptura`.

---

```text
'''
    (destino / text_name).write_text(header + text_body + '```\n', encoding='utf-8')
    sources['contran-pdf'] = {'url': URLS['contran-pdf'], 'http': 200, 'encoding': 'PDF: pdftotext UTF-8', 'sha256_fonte': sha(pdf_raw), 'bytes_fonte': len(pdf_raw)}
    records.extend([
        {'arquivo': pdf_name, 'fonte': 'contran-pdf', 'paginas': 20, 'anexos': ['I', 'II', 'III'], 'bytes': len(pdf_raw), 'sha256_arquivo': sha(pdf_raw)},
        {'arquivo': text_name, 'fonte': 'contran-pdf', 'artigos': [str(n) for n in range(1, 17)], 'anexos_textuais': ['I', 'II'], 'anexo_iii': 'apenas imagem no PDF integral', 'caracteres_corpo': len(text_body), 'sha256_corpo': sha(text_body.encode())},
    ])
    manifest = {'captura': '2026-10-01', 'fontes': sources, 'anexos': records, 'limites': ['CPP art. 611 não consta no HTML compilado consultado; não reconstruído.', 'Anexo III da Resolução 1.031/2026 preservado no PDF integral; camada textual sem OCR verificado.']}
    (destino / 'manifesto-captura-ctr2.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    return sources, records


if __name__ == '__main__':
    cli = argparse.ArgumentParser()
    cli.add_argument('--fontes', type=Path, required=True)
    cli.add_argument('--destino', type=Path, required=True)
    args = cli.parse_args()
    sources, records = run(args.fontes, args.destino)
    print(json.dumps({'fontes': sources, 'anexos': records}, ensure_ascii=False, indent=2))
