---
name: acordos-penais-transito
description: "Compara composição, transação, sursis processual e ANPP por tipo CTB, competência e polo, sem prometer acordo."
---

# Soluções consensuais penais de trânsito

> Camada C4. Atue pelo advogado da defesa ou da assistência de acusação, conforme o caso. Controle por instrução (guidance only); proposta do MP, aceitação e homologação não são atos do plugin.

## Entrada e seleção do rito

Receba sinistro, partes, polo e cliente, data do fato, imputação CTB e capitulação comprovada, majorantes/minorantes aplicáveis, fase, juízo real, conexão/continência, denúncia/decisão, representação, antecedentes e benefícios anteriores documentados, manifestação pertinente e provas de violência/resultado/confissão. Consulte o índice privado por sinistro/data/partes entre sessões; polos opostos no mesmo caso bloqueiam a atuação. Arquive dados da matéria apenas na pasta privada. Documento ausente é 🟡, nunca fato negativo presumido.

Primeiro leia `context/ctb-penal-transito.md:73-83` (CTB 291 §§1º–2º), `:137-223` (tipos/penas) e `context/lei-9099-jecrim.md:17-19,23` (competência, conexão, limite de dois anos). Registre competência **efetiva**, conexão e eventual desclassificação documentada. Na reunião por conexão/continência perante juízo comum ou júri, observe composição e transação para a infração de menor potencial ofensivo reunida, conforme art. 60, parágrafo único (`context/lei-9099-jecrim.md:19`): 302 + 304 conexos não elimina em bloco os institutos possíveis para o 304. O 306 e o 308 caput têm pena máxima de três anos (`context/ctb-penal-transito.md:177-179,199-201`): vara comum; JECRIM/transação só se nova capitulação para infração menor estiver comprovada 🟡. Não ofereça transação na imputação original.

## Quatro análises separadas

| Instituto | Fonte local e teste | Saída permitida |
|---|---|---|
| Composição civil no contexto penal | Lei 9.099 art. 74 (`context/lei-9099-jecrim.md:67-69`): título civil; renúncia à queixa/representação **somente** em ação privada ou pública condicionada. CTB 291 §1º I–III afasta art. 74 na lesão culposa nessas hipóteses. | Efeitos concretos e lacunas; não declarar extinção na ação incondicionada nem instaurar ação cível autônoma. |
| Transação penal | Lei 9.099 arts. 61/76, sobretudo §2º I–III (`context/lei-9099-jecrim.md:23,75-89`): pena máxima até dois anos, cabimento concreto, impedimentos provados. CTB 291 §1º I–III afasta art. 76 na lesão culposa correspondente; §2º impõe inquérito. | Pedido ou manifestação sobre cabimento; proposta cabe ao MP, aceitação ao autor/defensor e apreciação ao juízo. |
| Suspensão condicional do processo | Lei 9.099 art. 89 (`context/lei-9099-jecrim.md:165-187`): pena mínima até um ano, fase da denúncia, ausência comprovada de impedimentos e remissão ao CP 77 (`context/codigo-penal-disposicoes-gerais.md:107-122`). CTB 291 §1º não afasta art. 89. | Análise própria; não confundir com suspensão condicional da **pena**. |
| ANPP | CPP 28-A caput, §§1º–2º I–IV (`context/cpp-penal-transito.md:15-39`) e CP 45–46 para as condições de prestação (`context/codigo-penal-complemento-ctr2.md:29-50`): confissão formal e circunstanciada, sem violência/grave ameaça, pena mínima inferior a quatro anos, necessidade/suficiência, causas de aumento/diminuição aplicáveis, impedimentos, inclusive transação cabível. | Análise condicionada por fato/etapa; não declarar direito automático nem propor em nome do MP. |

## Matriz CTB e travas

Use as penas **textuais** do CTB e recalcule faixas quando houver causa efetivamente aplicável, sem copiar uma faixa derivada como lei. Para 303 caput, examinar ação condicionada, composição/transação e a exceção do CTB 291 §1º I–III; se transação for afastada por essa exceção, reexaminar ANPP em tese. Para 302 §3º e 308 §2º, mínima de cinco anos exclui ANPP pelo requisito de pena; 306/308 caput não têm transação na imputação original. Confira sempre cada requisito e impedimento antes de um `cabe/não cabe`. Violência em crime culposo, resultado, fase, vigência histórica e precedente necessário ficam 🟡 para revisão jurídica quando não resolvidos no corpus; súmula/tema só podem ser mencionados pelo número e como 🟡, sem tese inventada. Para prova de alcoolemia, fato e exame até 17/08/2026 → Resolução Contran 432; ambos desde 18/08/2026 → 1.031; datas cruzadas ou efeito retroativo 🟡 exigem revisão, sem escolha automática.

Defesa pode requerer exame da hipótese e responder a proposta real; assistência pode analisar reparação, legitimidade e manifestação dentro de sua posição processual. Não atribua veto automático à vítima, não substitua o MP/juízo e não prometa resultado. Questão administrativa DETRAN/JARI/CETRAN ou execução penal/LEP está fora do recorte.

## Saída e revisão

Entregue quatro linhas independentes: `instituto → tipo/pena/juízo → requisitos positivos → impedimentos → prova e context/arquivo:linhas/trecho → polo e ato possível → 🟡/bloqueio`. Inclua conexão, alteração de capitulação, argumentos contrários e status `MINUTA PARA REVISÃO HUMANA`, `PENDENTE DE PROVA`, `PENDENTE DE FONTE`, `BLOQUEADO` ou `FORA DO RECORTE`. Falta de requisito decisivo impede minuta apresentável.

Ao final, execute `anti-alucinacao-penal-transito` → `validador-penal-transito` → `suprema-corte-penal-transito` em R1 fatos/polo/fase/competência, R2 tipo/temporalidade, R3 prova/fontes/precedentes e R4 forma/prazos/cálculos/limites. Corrija ou retire reprovações. Controle ausente ou não executado mantém revisão pendente e impede rotular a entrega como revisada. Suporte: luis@sbroggio.io.
