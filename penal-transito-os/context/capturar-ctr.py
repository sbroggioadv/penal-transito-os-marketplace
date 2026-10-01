#!/usr/bin/env python3
"""Captura CTR: download oficial e extração literal, com tachados preservados."""
from html.parser import HTMLParser
from pathlib import Path
import re,json,hashlib
class Extrator(HTMLParser):
 def __init__(self):
  super().__init__(convert_charrefs=True);self.stack=[];self.parts=[];self.lines=[]
 def flush(self):
  if not self.parts:return
  chars=[]
  for s,flag in self.parts:
   for c in s:chars.append((c,flag))
  out=[];last=False;space=False
  for c,flag in chars:
   if c.isspace():space=True;continue
   if space and out:out.append(' ')
   space=False
   if flag!=last:out.append('~~');last=flag
   out.append(c)
  if last:out.append('~~')
  t=''.join(out).strip()
  if t:self.lines.append(t)
  self.parts=[]
 def handle_starttag(self,tag,attrs):
  if tag in ('p','div','tr','h1','h2','h3','h4','li','br'):self.flush()
  if tag in ('br','meta','link','img','input','hr'):return
  style=dict(attrs).get('style','')
  struck=tag in ('strike','s','del') or bool(re.search('text-decoration[^;]*line-through',style,re.I))
  self.stack.append((tag,struck))
 def handle_endtag(self,tag):
  if tag in ('p','div','tr','h1','h2','h3','h4','li'):self.flush()
  for i in range(len(self.stack)-1,-1,-1):
   if self.stack[i][0]==tag:self.stack=self.stack[:i];break
 def handle_data(self,data):
  if any(t in ('head','script','style') for t,_ in self.stack):return
  self.parts.append((data,any(f for _,f in self.stack)))

def parse(path):
 raw=path.read_bytes()
 try:t=raw.decode('utf-8');encoding='utf-8'
 except UnicodeDecodeError:t=raw.decode('cp1252');encoding='cp1252'
 p=Extrator();p.feed(t);p.flush()
 return p.lines,encoding,hashlib.sha256(raw).hexdigest()

import argparse,urllib.request,tempfile,concurrent.futures,subprocess,html
from datetime import date
cli=argparse.ArgumentParser(description='Captura literal CTR: Planalto e Contran/gov.br')
cli.add_argument('--destino',required=True,type=Path)
cli.add_argument('--html-dir',type=Path,help='Snapshot local de HTML/PDF; sem rede')
args=cli.parse_args();DEST=args.destino;DEST.mkdir(parents=True,exist_ok=True)
URLS={
 'ctb':'https://www.planalto.gov.br/ccivil_03/leis/l9503compilado.htm',
 'cp':'https://www.planalto.gov.br/ccivil_03/decreto-lei/del2848compilado.htm',
 'cpp':'https://www.planalto.gov.br/ccivil_03/decreto-lei/del3689compilado.htm',
 'jecrim':'https://www.planalto.gov.br/ccivil_03/leis/l9099.htm',
 'contran':'https://www.gov.br/transportes/pt-br/assuntos/transito/conteudo-contran/resolucao-no-432-de-23-de-janeiro-de-2013',
 'contran-pdf':'https://www.gov.br/transportes/pt-br/assuntos/transito/conteudo-contran/resolucoes/resolu-o-uo-432-2013c.pdf'}
temporary=tempfile.TemporaryDirectory(prefix='ctr-');SOURCE_DIR=args.html_dir or Path(temporary.name)
def sourcefile(k):return SOURCE_DIR/(k+('.pdf' if k.endswith('pdf') else '.html'))
def fetch(k):
 with urllib.request.urlopen(urllib.request.Request(URLS[k],headers={'User-Agent':'Mozilla/5.0'}),timeout=60) as r:
  assert r.status==200;sourcefile(k).write_bytes(r.read())
if not args.html_dir:
 with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:list(pool.map(fetch,URLS))
SOURCES={k:parse(sourcefile(k)) for k in URLS if not k.endswith('pdf')}
for k in SOURCES:
 raw=sourcefile(k).read_bytes().decode(SOURCES[k][1])
 raw=re.sub(r'(?is)<(head|script|style)\b[^>]*>.*?</\1>','',raw)
 raw=re.sub(r'(?s)<!--.*?-->','',raw)
 raw=re.sub(r'(?i)</?(?:p|div|tr|h[1-6]|li|br)\b[^>]*>','\n',raw)
 expected=re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>','',raw))).strip()
 actual=re.sub(r'\s+',' ',' '.join(SOURCES[k][0]).replace('~~','')).strip()
 assert expected==actual,(k,'Extração independente diverge')
print('PASS: extração independente de cinco HTMLs')
PAT=re.compile(r'^Art\.?\s*(\d+(?:\.\d{3})*)[ºo°]?(?:-([A-Z]))?(?=[.\s:–-])')
def article(line):
 m=PAT.match(line.replace('~~',''))
 return (int(m[1].replace('.','')),m[2] or '') if m else None

def block(k,n,suffix=''):
 lines=SOURCES[k][0];starts=[i for i,l in enumerate(lines) if article(l)==(n,suffix)]
 assert starts,(k,n,suffix,'ausente')
 start=starts[0];end=next((i for i in range(start+1,len(lines)) if article(lines[i]) and article(lines[i])!=(n,suffix)),len(lines))
 return lines[start:end]

def trim_end_headings(ls):
 # Remove apenas títulos estruturais finais do artigo seguinte.
 while ls and (re.match(r'^(?:CAPÍTULO|Se[cç][aã]o|TÍTULO|LIVRO)',ls[-1]) or (len(ls)>1 and re.match(r'^(?:CAPÍTULO|Se[cç][aã]o|TÍTULO|LIVRO)',ls[-2]))):ls=ls[:-1]
 return ls

def keys_range(k,lo,hi,lastsuffix='Z'):
 keys=[]
 for l in SOURCES[k][0]:
  a=article(l)
  if a and lo<=a[0]<=hi and (a[0]!=hi or a[1]<=lastsuffix) and a not in keys:keys.append(a)
 return keys
records=[]
def write(name,title,k,ls,note,keys):
 marked=[]
 for l in ls:
  if re.match(r'^(?:Art\.|§|Parágrafo|[IVXLCDM]+\s*[-–])',l) and re.search(r'\(?[Rr]evogad[oa](?: pela|\))',l) and '~~' not in l:l='~~'+l+'~~'
  marked.append(l)
 body='\n\n'.join(marked)+'\n'
 assert '\ufffd' not in body and not re.search(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x80-\x9f]',body)
 assert re.sub(r'\s+',' ',body.replace('~~','')).strip()==re.sub(r'\s+',' ',' '.join(ls).replace('~~','')).strip()
 enc,sha=SOURCES[k][1:]
 header=f'''# {title}

- **Fonte oficial:** {'Contran — Ministério dos Transportes (gov.br)' if k=='contran' else 'Planalto — Presidência da República'}.
- **URL:** {URLS[k]}
- **Data da captura:** {date.today().strftime('%d/%m/%Y')}.
- **HTTP:** 200.
- **SHA-256 do HTML:** `{sha}`.
- **Decodificação:** {enc} estrita; saída UTF-8.
- **Método:** download direto com urllib.request; HTMLParser (stdlib), sem reescrita por modelo. Entidades HTML decodificadas e espaços/quebras de layout normalizados. Tags/links removidos com seu texto preservado; scripts, estilos e head técnico excluídos. Tachados da fonte convertidos em `~~texto~~`; dispositivos com marcadores literais de revogação adicionalmente tachados. Sem normalização Unicode NFC/NFD nem correção editorial.
- **Escopo:** {note}
- **Reprodução:** `python3 capturar-ctr.py --destino /tmp/ctr-recaptura`; fonte pode mudar.

---

'''
 (DEST/name).write_text(header+body,encoding='utf-8')
 records.append({'arquivo':name,'fonte':k,'artigos':[str(n)+('-'+s if s else '') for n,s in keys],'caracteres_corpo':len(body),'sha256_corpo':hashlib.sha256(body.encode()).hexdigest(),'linhas_tachadas':sum('~~' in l for l in marked)})

def whole(name,title,k,keys,note):
 ls=[]
 for n,s in keys:ls+=trim_end_headings(block(k,n,s))
 write(name,title,k,ls,note,keys)
ctbkeys=[(n,'') for n in (1,2,3,165)]+[(165,'A'),(165,'B'),(276,''),(277,'')]+keys_range('ctb',291,312,'B')
assert all((n,'') in ctbkeys for n in range(291,313)) and (312,'A') in ctbkeys and (312,'B') in ctbkeys
whole('ctb-penal-transito.md','CTB — Lei nº 9.503/1997, compilado: recorte penal e alcoolemia','ctb',ctbkeys,'Arts. 1º–3º, 165, 165-A, 165-B, 276, 277 e 291–312-B integrais; intercalares incluídos. Redações e notas incorporadas na página compilada, inclusive Leis 13.546/2017, 14.071/2020 e posteriores. Sem reconstrução manual de versões anteriores omitidas pela fonte.')
cpkeys=[(n,'') for n in (13,18,33,44,59,68,77,78,79,80,81,107,109,115)]
whole('codigo-penal-disposicoes-gerais.md','Código Penal — disposições gerais selecionadas','cp',cpkeys,'Arts. 13, 18, 33, 44, 59, 68, 77–81, 107, 109 e 115 integrais.')
# Em recortes de parágrafo, delimitar antes do próximo parágrafo, mantendo penas.
PP=re.compile(r'^§\s*(\d+)[ºo°]?(?:\s*-\s*([A-Z]))?(?=[.\s–-])')
def partial(n,pars):
 ls=block('cp',n);out=[];active=True;selected=[]
 for l in ls:
  # Epígrafes que antecedem parágrafos omitidos não pertencem ao caput.
  if not selected and l in ('Caso de diminuição de pena','Lesão corporal de natureza grave'):
   active=False
  m=PP.match(l.replace('~~',''))
  if m:
   key=(int(m[1]),m[2] or '');active=key[0] in pars and not key[1]
   if active:selected.append(key[0])
  if active:out.append(l)
 assert set(selected)==set(pars),(n,selected)
 # Epígrafes da próxima seção podem preceder o marcador do próximo parágrafo.
 # Remove títulos finais conhecidos, sem reescrever os dispositivos.
 while out and out[-1].startswith(('Caso de diminuição','Lesão corporal de natureza grave','Violência Doméstica','Feminicídio')):out.pop()
 return out
write('codigo-penal-121-129-recortes.md','Código Penal — arts. 121 e 129, recortes expressos','cp',partial(121,{3,4,5})+partial(129,{6,7,8}),'Art. 121 somente caput (com pena), §§ 3º, 4º e 5º; art. 129 somente caput (com pena), §§ 6º, 7º e 8º. Parágrafos intercalares 8º-A e demais excluídos.',[(121,''),(129,'')])
cppkeys=[(28,'A'),(41,''),(158,''),(159,'')]+[(n,'') for n in range(301,311)]+[(312,''),(319,'')]+[(n,'') for n in range(321,351)]+[(n,'') for n in range(395,398)]+[(n,'') for n in (581,593,600)]
whole('cpp-penal-transito.md','CPP — ANPP, prova, flagrante, cautelares, fiança e recursos','cpp',cppkeys,'Arts. 28-A, 41, 158, 159, 301–310, 312, 319, 321–350, 395–397, 581, 593 e 600 integrais; somente esses artigos, sem 158-A–158-F e 310-A.')
jeckeys=keys_range('jecrim',60,92)
assert all((n,'') in jeckeys for n in range(60,93))
whole('lei-9099-jecrim.md','Lei nº 9.099/1995 — arts. 60–92','jecrim',jeckeys,'Arts. 60–92 integrais, inclusive o intercalar 90-A presente na fonte. Não há art. 81-A nessa página.')
# PDF contém resolução integral e anexos I/II ausentes do HTML.
pdftext=subprocess.check_output(['pdftotext','-layout','-nopgbrk',str(sourcefile('contran-pdf')),'-']).decode('utf-8')
assert '\ufffd' not in pdftext and not re.search(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x80-\x9f]',pdftext)
assert 'ANEXO I' in pdftext and 'ANEXO II' in pdftext and '2,00' in pdftext
sha=hashlib.sha256(sourcefile('contran-pdf').read_bytes()).hexdigest()
body='```text\n'+pdftext.rstrip()+'\n```\n'
header=f'''# Resolução Contran nº 432/2013 — integral, com anexos I e II (histórica)

- **Fonte oficial:** Contran — Ministério dos Transportes (gov.br).
- **URL:** {URLS['contran-pdf']}
- **Página oficial de apoio:** {URLS['contran']}
- **Data da captura:** {date.today().strftime('%d/%m/%Y')}.
- **HTTP:** 200.
- **SHA-256 do PDF:** `{sha}`.
- **Método:** download direto; `pdftotext -layout -nopgbrk` (Poppler), sem OCR e sem reescrita por modelo; saída UTF-8 estrita. Espaçamento e layout da extração preservados em bloco textual, inclusive colunas da tabela do Anexo I. Quebras de página omitidas pela opção declarada. Sem normalização Unicode NFC/NFD.
- **Escopo:** resolução integral: preâmbulo, arts. 1º–14, signatários, Anexo I (tabela) e Anexo II (sinais e termo).
- **Situação:** captura histórica solicitada. Revogada pela Resolução Contran nº 1.031/2026, art. 15; conferir nota de vigência no INDICE.md. O bloco abaixo preserva o PDF original, sem inserir tachados editoriais nas colunas.

---

'''
(DEST/'contran-432-2013-integral.md').write_text(header+body,encoding='utf-8')
records.append({'arquivo':'contran-432-2013-integral.md','fonte':'contran-pdf','artigos':[str(n) for n in range(1,15)],'anexos':['I','II'],'caracteres_corpo':len(body),'sha256_corpo':hashlib.sha256(body.encode()).hexdigest()})
manifest={'captura':date.today().isoformat(),'fontes':{k:{'url':u,'http':200,'encoding':SOURCES[k][1] if k in SOURCES else 'PDF: pdftotext UTF-8','sha256_fonte':hashlib.sha256(sourcefile(k).read_bytes()).hexdigest(),'bytes_fonte':sourcefile(k).stat().st_size} for k,u in URLS.items()},'anexos':records}
(DEST/'manifesto-captura.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(records,ensure_ascii=False,indent=2))
