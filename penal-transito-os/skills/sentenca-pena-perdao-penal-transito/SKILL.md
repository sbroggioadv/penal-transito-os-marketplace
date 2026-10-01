---
name: sentenca-pena-perdao-penal-transito
description: "Use para examinar sentença, dosimetria, substituição, multa reparatória, valor mínimo e perdão judicial em crime de trânsito, com ramos separados por polo."
---

# Sentença, pena e perdão no CTB

> Camada C6. Guidance only; a análise e os controles são executados pelo agente e exigem revisão do advogado.

## Entradas e escolha do ramo

Receber polo único, tipo CTB e redação na data do fato, sentença ou pedido em formação, capitulação, prova, agravantes/atenuantes/majorantes, antecedentes comprovados, pena aplicada, prejuízo documentado e objetivo. Consultar triagem e índice privado de conflitos. Selecionar **um** ramo: (A) memória de dosimetria/substituição, (B) multa reparatória CTB 297 e valor mínimo CPP 387 IV, ou (C) perdão judicial. Defesa pode requerer; assistência admitida pode examinar e se manifestar dentro do poder processual, sem sentenciar pelo juiz.

## Fontes locais

- `context/ctb-penal-transito.md:73-87,105-130,137-168,177-206,227-237`: CTB 291/297/298, tipos pertinentes 302–303/306/308, 312-A/B. CTB 299/300 e 310-A vetados não são fundamentos ativos.
- `context/codigo-penal-disposicoes-gerais.md:45-106,157-176` e `context/codigo-penal-complemento-ctr2.md:77-107,125-229,239-241,353`: CP 33/44/59/61–71/49–52/91 I/107 IX/120, nos trechos efetivos. Ler os dispositivos integrais antes de usar uma faixa; não inferir conteúdo de título ou remissão.
- `context/codigo-penal-121-129-recortes.md:15-41`: CP 121 §5º e 129 §8º; `context/cpp-complemento-ctr2.md:535-543`: CPP 387 IV. CP 121 §6º e 129 §§1º–2º não constam completos 🟡; dependência bloqueada.

## Ramo A — pena e substituição

Montar cálculo reexecutável: tipo e faixa legal **da versão aplicável**, pena-base e fatos comprovados, agravantes/atenuantes sem dupla contagem, majorantes/minorantes e resultado; separar suspensão/proibição de dirigir, prestação de serviços e penas do CP. Indicar operação numérica, prova e fundamento em cada etapa. Aplicar CTB 291 §4º (`context/ctb-penal-transito.md:87`): na pena-base segundo CP 59, dar atenção especial à culpabilidade, circunstâncias e consequências comprovadas. CTB 312-A condiciona o conteúdo da atividade **quando** houver substituição, não cria cabimento por si. Para fato anterior à Lei 14.071/2020, vigência/redação do 312-B 🟡 deve ser comprovada antes de aplicá-lo.

Em CTB 302 §3º e 303 §2º, o **texto** de 312-B declara inaplicável CP 44 I ✅ local (`ctb:237`), cujo inciso I traz a hipótese de cabimento por pena/natureza (`codigo-penal-disposicoes-gerais.md`, art. 44). Expor **duas leituras 🟡** em ambos os polos: (1) sem essa porta legal, a substituição pelo art. 44 ficaria afastada; (2) leitura literal defensiva contrária, segundo a qual dispensar o inciso I não proíbe substituir. Não chamar nenhuma delas de efeito literal pacificado; precedente/solução dependem de D2 e revisão jurídica. Não estender 312-B a outro tipo.

## Ramo B — reparação dentro da ação penal

Separar multa reparatória CTB 297, limitada ao prejuízo material demonstrado e com cálculo por remissão ao CP 49 §1º, do valor mínimo CPP 387 IV e do efeito CP 91 I. Demonstrar nexo, documentos, valor de cada rubrica e risco de sobreposição; registrar que CTB 297 §3º manda descontar a multa da indenização civil. Sem prejuízo/quantum provado, não calcular nem prometer reparação. Ação cível autônoma está fora do produto.

## Ramo C — perdão

Examinar CP 121 §5º/129 §8º, CP 107 IX/120 e remissão CTB 291, sempre vinculando consequências concretas provadas ao requisito textual. A ponte interpretativa CTB 291 → perdão e eventual precedente seguem 🟡 até confirmação; súmula/tema somente número e 🟡. Parentesco e sofrimento alegado não geram perdão automático. CTB 300 vetado não serve de fundamento. O ato de conceder é judicial; defesa pede, assistência se manifesta nos limites de sua admissão.

## Entrega e controles

Entregar memória/matriz ou minuta condicionada do ramo escolhido, com `etapa → fato/prova → artigo/linha/trecho → versão → operação → conclusão/🟡`, cálculos reproduzíveis e argumentos dos dois polos quando houver controvérsia. Falta de quantum, prova, antecedente ou versão temporal bloqueia cálculo dependente; sem sentença, não afirmar pena aplicada. Para 306, 302 §3º ou 303 §2º, auditar prova de álcool/substância com `embriaguez-alcoolemia-penal-transito`, observando datas do fato e do exame (432/1.031). Estado: `MINUTA PARA REVISÃO HUMANA`, `PENDENTE DE PROVA`, `PENDENTE DE FONTE`, `BLOQUEADO` ou `FORA DO RECORTE`. Dados privados por matéria, fora do repo; sem envio externo. Suporte: luis@sbroggio.io.

Executar, inclusive em chamada direta, `anti-alucinacao-penal-transito` para fatos/fontes, `validador-penal-transito` para texto/remissões/tempo/alcance e `suprema-corte-penal-transito` R1 polo/fase, R2 tipo/versão, R3 prova/precedentes, R4 forma/prazo/cálculo/fronteira. Registrar achados dos três; pendência impeditiva impede saída como pronta. Guidance only, sem afirmar enforcement automático.
