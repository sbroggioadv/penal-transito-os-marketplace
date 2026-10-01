---
name: recursos-penal-transito
description: "Use para selecionar recurso, razões ou contrarrazões em crime CTB pelo juízo real, decisão, polo, legitimidade e ciência comprovados."
---

# Recursos penais de trânsito

> Camada C6. Guidance only; a análise e os controles são executados pelo agente e exigem revisão do advogado.

## Entrada e seleção obrigatória

Receber polo, tipo CTB, decisão/acórdão integral, juízo **real**, eventual conexão/declínio/desclassificação, fase, data e prova de ciência de cada legitimado, recurso do MP, admissão do assistente e objetivo. Consultar triagem e índice privado de conflitos. Primeiro determinar se a decisão veio do JECRIM/turma recursal ou da vara comum; só então escolher apelação, RESE, embargos, razões ou contrarrazões. Não atribuir à vítima prazo, ciência ou legitimidade apenas por vínculo familiar.

## Fontes locais por ramo

- **JECRIM:** `context/lei-9099-jecrim.md:17-19,23,129-139,143-145,149` (arts. 60–61, 82–83). Art. 82: apelação de rejeição da denúncia/queixa ou sentença à turma, interposição em **dez dias** da ciência, **razões e pedido na própria petição**, resposta em dez dias. Art. 83: embargos por obscuridade, contradição ou omissão em cinco dias da ciência, com efeito interruptivo no prazo recursal (`context/lei-9099-jecrim.md:145,149`). Não levar CPP 593/600 para este ramo. Legitimidade recursal da vítima/assistente no juizado 🟡 sem fundamento consolidado no corpus: bloquear recurso dela até comprovação de hipótese, status e ciência.
- **Vara comum:** `context/cpp-complemento-ctr2.md:407-421,823-831,857-900,1085-1103` (CPP 271, 584 §1º, 593, 598–600, 798) e `context/cpp-penal-transito.md:393-477` (CPP 581/593/600). Conferir CPP 574–620 artigo a artigo no corpus. **CPP 382 ausente 🟡:** bloquear embargos contra sentença da vara comum até captura; CPP 619–620 tratam de acórdão. **CPP 611 ausente 🟡:** não suprir por memória. Para recurso da vítima, confrontar CPP 271/584 §1º/598, existência de recurso do MP, admissão quando exigida, decisão atacada e ciências específicas; não presumir prazo supletivo nem transportar dispositivo fora da hipótese.
- **Excepcionais:** CPP 637, CF 102 III/105 III, CPC recursal e regras locais não estão textuais 🟡. Entregar somente mapa de fontes e fatos pendentes; bloquear minuta de RE/REsp ou agravo, prazo e endereçamento. Súmula/tema apenas número e 🟡, sem enunciado/tese reconstruído ou reexame factual disfarçado.

## Procedimento

1. Registrar `decisão → juízo/rito → polo e qualidade → hipótese legal → ciência/prova → prazo/fonte → ato desejado`. Se houver conexão, conferir o juízo da decisão; a reunião de infração menor na vara comum mantém análise dos institutos do art. 60, parágrafo único, mas não define sozinha o recurso. Para 306/308 caput, JECRIM apenas se desclassificação/nova capitulação para infração menor estiver provada 🟡.
2. Isolar dispositivo, fundamento e sucumbência ligados ao crime CTB. Escolher uma rota de recurso ou resposta do polo, sem redigir simultaneamente polos contrários. Para assistência, validar poderes e admissão na rota `assistencia-acusacao-penal-transito`.
3. Calcular prazo só com ciência individual comprovada, evento inicial, regra textual aplicável e eventuais embargos/suspensões demonstrados. Mostrar operação e data como cenário condicionado a revisão humana; se marco faltar, apresentar pendência, não data fatal.
4. Montar matriz `ponto recorrido → erro alegado → fato/prova dos autos → artigo/trecho/versão → pedido`, preservando limites de cognição e prova existente. Contrarrazões respondem argumentos reais, não recurso hipotético.
5. Caso adverso obrigatório: apelação de sentença JECRIM calculada pelos cinco dias do CPP 593 ou razões em oito dias do CPP 600 → **bloquear e refazer** sob Lei 9.099 art. 82. Vítima no JECRIM sem legitimidade textual/ciência → apenas pendências.

## Saída e controles

Entregar seleção motivada e uma minuta condicionada quando fonte, legitimidade, ato e prazo forem demonstrados; caso contrário, matriz de pendências 🟡. Não afirmar protocolo, decisão, admissibilidade ou êxito. Sem fonte textual de norma excepcional, nenhum recurso excepcional pronto. Estado: `MINUTA PARA REVISÃO HUMANA`, `PENDENTE DE PROVA`, `PENDENTE DE FONTE`, `BLOQUEADO` ou `FORA DO RECORTE`. Dados de cliente em pasta privada por matéria, sem envio externo. Suporte: luis@sbroggio.io.

Executar `anti-alucinacao-penal-transito` sobre documentos/fatos/citações, `validador-penal-transito` sobre artigo → arquivo/linha → trecho → versão/data → alcance e `suprema-corte-penal-transito` R1 polo/fase/competência, R2 tipo/tempo, R3 prova/precedentes, R4 legitimidade/forma/prazo/fronteira. Registrar achados dos três inclusive em chamada direta; ausência bloqueia peça pronta. Guidance only, sem enforcement automático presumido.
