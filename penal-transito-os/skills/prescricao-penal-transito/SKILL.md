---
name: prescricao-penal-transito
description: "Use para cronologia e cálculo reexecutável de prescrição em crime de trânsito, exigindo todos os marcos, trânsitos por sujeito e versão temporal."
---

# Prescrição penal de trânsito

> Camada C6. Guidance only; a análise e os controles são executados pelo agente e exigem revisão do advogado.

## Entrada e fontes

Receber polo, crime CTB e data/versão do fato, pena em abstrato ou aplicada, circunstâncias e decisões que a alteram, nascimento/idade relevante, recebimento da denúncia, sentença/publicação, recursos, trânsito **por sujeito**, causas de suspensão/interrupção e documentos que comprovam cada marco. Consultar triagem e índice privado de conflitos. Sem cronologia íntegra, só cenários rotulados 🟡; nunca declarar prescrição virtual consumada.

Ler `context/ctb-penal-transito.md` no tipo e pena pertinentes; `context/codigo-penal-disposicoes-gerais.md:157-199` (CP 107/109/115) e `context/codigo-penal-complemento-ctr2.md:15-25,273-351` (CP 10, 110–114/116–119). Verificar inciso e parágrafo efetivos; CP 115 tem redação de 2025, exigindo versão histórica em fatos/decisões anteriores 🟡. CPP 61–62 **não têm texto no corpus** 🟡: bloqueiam minuta de extinção dependente; não completá-los por memória. Conferir CPP 798 em `context/cpp-complemento-ctr2.md:1085-1103` só quando contagem processual for pertinente, sem confundir prazo material e processual.

## Método

1. Fixar espécie de prescrição alegada e regime temporal aplicável; não converter automaticamente pena abstrata em aplicada antes dos marcos exigidos. Para concurso, examinar CP 119 por crime; para multa, examinar CP 114 e remissão, sem misturar com pena corporal.
2. Construir tabela cronológica `evento → data/hora se relevante → documento/trecho → sujeito afetado → efeito alegado → fundamento local → incerteza`. Separar recebimento, sentença, publicação, recursos e trânsitos da defesa/acusação. Registrar intervalo inicial/final e operação aritmética.
3. Aplicar CP 109 à faixa pertinente; só reduzir por idade quando idade, marco e versão do CP 115 estiverem comprovados. Verificar CP 116 (inclusive IV, ANPP), Lei 9.099 art. 89 §6º (`context/lei-9099-jecrim.md:185`), CP 117 e, para pena restritiva cumulativa, CP 109 parágrafo único e CP 118 (`context/codigo-penal-disposicoes-gerais.md:177–193`; `context/codigo-penal-complemento-ctr2.md:315–347`), com efeitos pessoais e prova de cada causa. Não presumir reincidência, revogação ou trânsito.
4. Recalcular cenários alternativos quando marco, quantum ou versão forem 🟡, explicitando hipótese e resultado condicional; se a diferença afetar o resultado, bloquear conclusão categórica. Não tratar prescrição virtual/antecipada como fato consumado.

## Saída e travas

Entregar tabela e memória reexecutável `norma/versão → pena base → faixa → redução → início → pausas/interrupções → fim → resultado condicional`, mais pendências e eventual minuta cabível **somente** se a base normativa integral e os marcos forem demonstrados. Sem CPP 61–62 textual, não redigir ato de extinção que deles dependa. Sem prova de data, trânsito, idade ou versão, não afirmar extinção nem prazo fatal. Não gerir execução penal/LEP; encaminhar a questão fora do recorte. Estado: `MINUTA PARA REVISÃO HUMANA`, `PENDENTE DE PROVA`, `PENDENTE DE FONTE`, `BLOQUEADO` ou `FORA DO RECORTE`. Dados na pasta privada por matéria, sem envio externo. Suporte: luis@sbroggio.io.

Executar em chamada direta `anti-alucinacao-penal-transito` (fatos/proveniência), `validador-penal-transito` (dispositivo, trecho, versão, data, alcance, operação) e `suprema-corte-penal-transito` R1 polo/fase/marcos, R2 tipo/temporalidade, R3 prova/precedentes, R4 forma/prazo/cálculo/limite. Registrar achados; controle faltante bloqueia entrega como pronta. Guidance only.
