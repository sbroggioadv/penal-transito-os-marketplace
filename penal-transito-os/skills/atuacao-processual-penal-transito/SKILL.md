---
name: atuacao-processual-penal-transito
description: "Use para resposta da defesa, instrução ou memoriais dos polos em ação penal por crime CTB, escolhendo primeiro competência e rito reais."
---

# Atuação processual penal de trânsito

> Camada C5. Guidance only; a análise e os controles são executados pelo agente e exigem revisão do advogado.

## Entrada

Receber polo único, capitulação e data do fato, denúncia/citação, juízo e decisão de competência, conexão/continência, fase, intimações e ciências, atos já praticados, autos e prova efetiva. Consultar triagem e índice privado de conflitos antes de usar dados. Defesa pode preparar resposta; assistência só atua dentro dos poderes e da admissão provados. Não assumir papel de MP, juiz ou perito. Fora do recorte: ação penal comum sem nexo CTB, júri por dolo e contencioso administrativo de trânsito.

## Fontes e seleção do rito

Ler `context/ctb-penal-transito.md:73-83` (CTB 291) e o dispositivo CTB do tipo concreto. Conferir competência, art. 60 e seu parágrafo único e art. 61 em `context/lei-9099-jecrim.md:17-19,23`; processo reunido no juízo comum preserva transação/composição **da infração menor**, sem deslocar o crime maior. 306/308 caput seguem vara comum pela pena máxima de três anos (`context/ctb-penal-transito.md:177-179,199-201`); JECRIM só se nova capitulação para infração menor estiver provada 🟡. Declínio, conexão e competência real exigem autos, nunca presunção.

- **JECRIM comprovado:** ler `context/lei-9099-jecrim.md:95-127` (arts. 77–81). A denúncia oral é ato do MP quando cabível; a citação no termo e ciência da audiência constam do art. 78. A defesa responde **oralmente antes** do recebimento da denúncia na audiência (art. 81); seguem instrução, debates e sentença. Não aplicar CPP 396-A por automatismo.
- **Vara comum comprovada:** ler `context/cpp-penal-transito.md:369-392` (arts. 395–397) e `context/cpp-complemento-ctr2.md:553-627` (arts. 394/399–405), inclusive `context/cpp-complemento-ctr2.md:577-585` (arts. 396/396-A). Confrontar cada fase, decisão, prazo e ato com os autos; não transportar o roteiro comum ao JECRIM.
- **Prova e assistência:** conferir CPP 155–159/160–184 no corpus local (`context/cpp-penal-transito.md` e `context/cpp-complemento-ctr2.md`) e CPP 268–273 em `context/cpp-complemento-ctr2.md:407-421`; ausência de trecho integral ou prova concreta 🟡 bloqueia alegação dependente.

## Execução por ato

1. Fixar numa ficha: juízo real, tipo e eventual desclassificação, rito, polo, ato, fase, ciência e prazo demonstrados. Se qualquer ponto mudar, refazer a seleção antes da peça. Não criar prazo por memória.
2. Para **resposta**, aceitar somente polo defesa; distinguir JECRIM oral pré-recebimento de resposta escrita do rito comum. Relacionar imputação, elemento do tipo, fato controvertido, prova existente, pedidos de prova e fonte jurídica. Ausência de denúncia/citação ou de fase impede minuta conclusiva.
3. Para **instrução**, elaborar perguntas e requerimentos ligados a elemento CTB e prova identificada, separados para defesa e assistência admitida; não fabricar testemunha, exame, cadeia de custódia, medição ou certificado. Indicar contraditório e prova faltante. Para 306, 302 §3º ou 303 §2º, rotear a prova de álcool/substância a `embriaguez-alcoolemia-penal-transito` com datas do fato e do exame (432/1.031).
4. Para **memoriais/debates**, escolher o ato permitido na fase real; oferecer matriz `elemento CTB → alegação de cada polo → documento/trecho → contraprova → conclusão condicionada`. Não redigir alegação da vítima como MP; se atuação como assistente estiver pendente, entregar somente análise privada e pedido de regularização.
5. Testar adversarialmente: 302 + 304 conexos na vara comum mantém análise de institutos da infração menor (Lei 9.099 art. 60, parágrafo único); 306/308 caput sem nova capitulação não ganham rito JECRIM nem transação.

## Saída

Entregar seleção fundamentada de competência/rito e uma única peça ou roteiro do ato pedido, com polo, cronologia, prova, fontes locais por artigo/linha, pendências e revisão humana. Bloquear minuta dependente de juízo, capitulação, ciência, fase ou prova não demonstrados. Selar artigo sem texto ou versão histórica não capturada 🟡; nunca usar peça penal genérica como substituto. Estado: `MINUTA PARA REVISÃO HUMANA`, `PENDENTE DE PROVA`, `PENDENTE DE FONTE`, `BLOQUEADO` ou `FORA DO RECORTE`. Dados de cliente em pasta privada por matéria, sem publicação ou envio externo. Suporte: luis@sbroggio.io.

## Controles obrigatórios, inclusive chamada direta

Aplicar `anti-alucinacao-penal-transito` (existência e proveniência de fatos/provas/citações), `validador-penal-transito` (artigo, parágrafo, arquivo/linha, trecho, origem, data e alcance) e `suprema-corte-penal-transito` R1 polo/fase/competência, R2 tipo/temporalidade, R3 prova/precedentes, R4 forma/prazo/cálculo/limites. Registrar achados e bloquear peça dita pronta se controle ou dado indispensável faltar. Guidance only: a instrução não comprova execução automática.
