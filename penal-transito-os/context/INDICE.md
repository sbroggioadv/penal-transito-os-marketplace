# Índice — CTR · corpus penal de trânsito

Captura literal em 01/10/2026, exclusivamente de fontes oficiais. A lane CTR2 complementa os recortes com Planalto, ANTTlegis e o PDF do DOU no portal gov.br; `manifesto-captura-ctr2.json` registra os hashes e limites da captura complementar. Os cabeçalhos dos novos arquivos registram fonte, URL, data, método, codificação e SHA-256.

## Anexos

| Anexo | Escopo | Caracteres do corpo |
| --- | --- | ---: |
| [ctb-penal-transito.md](ctb-penal-transito.md) | CTB compilado: 1º–3º, 165, 165-A, 165-B, 276, 277, 291–312-B, inclusive 310-A, 312-A e 312-B | 20143 |
| [codigo-penal-disposicoes-gerais.md](codigo-penal-disposicoes-gerais.md) | CP: 13, 18, 33, 44, 59, 68, 77–81, 107, 109, 115 | 12692 |
| [codigo-penal-121-129-recortes.md](codigo-penal-121-129-recortes.md) | CP: 121 caput e §§ 3º–5º; 129 caput e §§ 6º–8º | 1411 |
| [cpp-penal-transito.md](cpp-penal-transito.md) | CPP: 28-A, 41, 158, 159, 301–310, 312, 319, 321–350, 395–397, 581, 593, 600 | 39280 |
| [lei-9099-jecrim.md](lei-9099-jecrim.md) | Lei nº 9.099/1995: 60–92, inclusive 90-A | 16519 |
| [contran-432-2013-integral.md](contran-432-2013-integral.md) | Resolução Contran nº 432/2013: preâmbulo, arts. 1º–14, assinaturas e Anexos I e II | 27372 |

### Complemento CTR2

| Anexo | Escopo | Integridade |
| --- | --- | --- |
| [contran-1031-2026-integral.pdf](contran-1031-2026-integral.pdf) | Resolução Contran nº 1.031/2026 integral, arts. 1º–16 e Anexos I–III, inclusive páginas de imagem do Anexo III | SHA-256 no manifesto CTR2 |
| [contran-1031-2026-texto-extraivel.md](contran-1031-2026-texto-extraivel.md) | Camada textual do PDF oficial; Anexo III exige leitura no PDF, pois suas páginas são imagens | SHA-256 do corpo no manifesto CTR2 |
| [codigo-penal-complemento-ctr2.md](codigo-penal-complemento-ctr2.md) | CP: temporalidade, pena, reparação, dosimetria e prescrição, inclusive arts. 1º–2º, 10, 49–52, 61–67 e 91 | SHA-256 do corpo no manifesto CTR2 |
| [cpp-complemento-ctr2.md](cpp-complemento-ctr2.md) | CPP: competência, prova, cautelares, assistência, instrução, nulidades, recursos, HC e prazos, inclusive arts. 63, 268–273, 271, 387, 584, 598 e 798 | SHA-256 do corpo no manifesto CTR2 |

**Vigência da 432:** REVOGADA pela Resolução Contran nº 1.031/2026, art. 15, vigente desde 18/08/2026 por força do art. 16, II. O anexo da 432 serve só para fatos anteriores a 18/08/2026. A alteração do Anexo da Resolução nº 985/2022 pelo art. 14 da 1.031 segue a vacatio específica de 60 dias do art. 16, I. A análise de eventual retroatividade benéfica permanece questão jurídica de caso concreto.

## Método e limites

- O [script de captura](capturar-ctr.py) foi adaptado do `PLAYBOOK/templates/capturar-planalto.py`. O template elimina o conteúdo HTML tachado; a adaptação preserva os tachados em `~~texto~~` e marca dispositivos que trazem literalmente a indicação de revogação. O texto tachado não deve ser lido como vigente.
- HTML baixado diretamente com `urllib.request`, HTTP 200, e extraído com `html.parser.HTMLParser`. Entidades HTML decodificadas; espaços e quebras de layout normalizados; etiquetas e links removidos, preservando seu texto. `head`, scripts e estilos excluídos. Sem correção editorial nem normalização Unicode NFC/NFD. A comparação mecânica entre a extração do parser e outra extração por remoção de tags passou nas cinco páginas HTML completas.
- A Resolução nº 432/2013 foi extraída do [PDF oficial](https://www.gov.br/transportes/pt-br/assuntos/transito/conteudo-contran/resolucoes/resolu-o-uo-432-2013c.pdf) com `pdftotext -layout -nopgbrk`, sem OCR, preservando o layout da tabela. As quebras de página foram omitidas pela opção declarada. A [página oficial da resolução](https://www.gov.br/transportes/pt-br/assuntos/transito/conteudo-contran/resolucao-no-432-de-23-de-janeiro-de-2013) também foi consultada, mas o PDF foi usado porque inclui os Anexos I e II.
- **Vigência:** a Resolução nº 432/2013 é histórica. O art. 15 da [Resolução Contran nº 1.031/2026](https://www.gov.br/transportes/pt-br/assuntos/transito/conteudo-contran/resolucoes/resolucao10312026.pdf), publicada em 18/08/2026, a revogou; o art. 16, II, fixou vigência na publicação para esse dispositivo. O anexo de 2013 não é apresentado como regra atual.
- O CTB é a página **compilada** do Planalto, com redações e notas nela presentes, inclusive alterações das Leis nº 13.546/2017, 14.071/2020 e posteriores. Redações históricas que a página não reproduz não foram reconstruídas. `VETADO` é mantido como tal. O arquivo não equivale a linha do tempo legislativa completa.
- Os recortes do CP 121/129 omitem os demais parágrafos e as epígrafes associadas a eles. A Lei nº 9.099/1995 tem art. 90-A na fonte consultada; não há art. 81-A nessa página. O CPP inclui art. 28-A; não inclui os intercalares 158-A–158-F, 310-A ou 396-A, que não foram pedidos.
- O SHA-256 do HTML identifica o download, mas o HTML do Planalto pode mudar em elementos fora dos artigos. Na recaptura desta execução, os hashes dos corpos de cinco anexos permaneceram iguais; o do CP 121/129 mudou apenas pela retirada das duas epígrafes fora do recorte. O PDF permaneceu com o mesmo SHA-256. Compare `sha256_corpo` para o texto normativo extraído.
- Esta captura não é juízo de aplicabilidade a fatos concretos, constitucionalidade ou atualização futura. Consulte o diploma vigente antes de usar o texto em peça.

## Reprodução e validação

```sh
python3 context/capturar-ctr.py --destino /tmp/ctr-recaptura
rg -P '[\x00-\x08\x0B\x0C\x0E-\x1F\x80-\x9F]' context
python3 - <<'PYCODE'
from pathlib import Path
for arquivo in Path('context').iterdir():
    if arquivo.is_file():
        texto = arquivo.read_text(encoding='utf-8')
        assert '\ufffd' not in texto, arquivo
print('PASS: UTF-8 estrito e ausência de U+FFFD')
PYCODE
```

A busca `rg` deve retornar vazia (código 1, sem ocorrências). `DONE` é marcador vazio de conclusão desta captura, não aprovação jurídica do plugin.
