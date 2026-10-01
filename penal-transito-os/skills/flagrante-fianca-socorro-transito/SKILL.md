---
name: flagrante-fianca-socorro-transito
description: "Examina flagrante, socorro, fiança e liberdade em crime de trânsito, com pedido da defesa ou análise limitada da assistência."
---

# Flagrante, fiança e socorro no trânsito

> Camada C3. Atue pelo advogado do polo indicado. Controle por instrução (guidance only); nenhuma soltura, prisão ou decisão é produzida pelo plugin.

## Entrada e trava de polo

Receba tipo CTB e data do fato, polo, fase e urgência, APF integral, horários de prisão/comunicações/custódia, decisão judicial, elementos do socorro, prova de risco, antecedentes documentados e situação atual. Consulte o índice privado de matérias por sinistro, data e partes antes de atuar; polos opostos no mesmo sinistro bloqueiam a rota. Dados e peças ficam apenas na pasta privada da matéria. Se faltar APF, decisão ou prova que sustente uma conclusão, marque 🟡 e entregue pedido de documento, sem minuta dependente.

## Leitura obrigatória e matriz

1. Identifique qual crime CTB foi imputado e se houve prisão efetiva, mera condução, intimação ou ordem posterior. Separe o que o APF registra do relato da parte e da inferência jurídica. Para data antiga, confira a redação aplicável: a compilação atual não prova sozinha o texto histórico.
2. Leia `context/ctb-penal-transito.md:135` (CTB 301). A prestação de pronto e integral socorro exige prova concreta; o texto especial impede prisão em flagrante **e** exigência de fiança nessas condições. Não estenda o efeito a qualquer crime, prisão por outro fundamento, cautelar posterior ou alegação não comprovada. Ausência de socorro provado não prova automaticamente crime nem autoriza prisão.
3. Antes da matriz de fiança, leia `context/ctb-penal-transito.md:73-83` (CTB 291 §§1º–2º) e `context/lei-9099-jecrim.md:23,51,55` (arts. 61, 69 e parágrafo único). No 303 com hipótese do CTB 291 §1º I–III, o §2º exige inquérito policial: não aplique o art. 69 p.u. só pela pena máxima; a sobreposição entre 291 §2º e 69 p.u. fica 🟡 para revisão jurídica. Nos demais casos, teste se a imputação é de menor potencial ofensivo e se houve termo circunstanciado e encaminhamento imediato ao Juizado ou compromisso de comparecimento: nessas condições, não se impõe flagrante nem se exige fiança. Sem prova do termo/compromisso, marque 🟡. Para imputações de 306, 302 §3º ou 303 §2º, audite a prova de álcool/substância por `embriaguez-alcoolemia-penal-transito`, conforme datas do fato e do exame (regimes 432/1.031). Leia `context/cpp-penal-transito.md:93-176` (CPP 301–310), `context/cpp-complemento-ctr2.md:423-444` (282–283), `:447-532` (311/313–318-B), e `context/cpp-penal-transito.md:177-228` (312/319/321). Verifique hipótese de flagrante, sequência e horário do auto, comunicação, audiência, fundamento da decisão, necessidade e adequação de cautelares. A redação de CPP 310 contém alterações de 2025/2026: cheque data do ato e vigência histórica antes de alegar prazo ou nulidade.
4. Para fiança, leia `context/cpp-penal-transito.md:229-367` (CPP 322–350). Separe competência policial/judicial, pena máxima do tipo imputado, impedimentos, valor e situação econômica. Não prometa fiança nem trate pagamento como condição universal de liberdade. Para HC, leia `context/cpp-complemento-ctr2.md:979-1083` (CPP 647–667): identifique coação à locomoção, autoridade, prova pré-constituída e pedido compatível; não use HC como resposta genérica a qualquer irregularidade.
5. Defesa: escolha entre relaxamento, liberdade com ou sem fiança, revisão de cautelar ou HC **apenas** quando hipótese, prova e juízo forem identificados. Assistência: analise legalidade do ato e prova no limite de sua legitimidade/fase; não fale como MP, autoridade policial ou julgador, nem formule prisão como consequência automática de oposição ao pedido defensivo.

## Saída

Entregue quadro `evento/hora → documento/linha → fato confirmado ou alegado → dispositivo/trecho → consequência possível → lacuna`, seguido de opção processual condicionada, pedido do polo e argumentos contrários relevantes. Status: `MINUTA PARA REVISÃO HUMANA`, `PENDENTE DE PROVA`, `PENDENTE DE FONTE`, `BLOQUEADO` ou `FORA DO RECORTE`. Bloqueie peça pronta quando o fundamento depender de APF, decisão, socorro ou vigência ausente. Distinguir prisão penal de infração e procedimento administrativo de trânsito.

Ao final, execute `anti-alucinacao-penal-transito` → `validador-penal-transito` → `suprema-corte-penal-transito` em R1 fatos/polo/fase/competência, R2 tipicidade e tempo, R3 prova e citações, R4 forma/prazo/limites. Corrija ou retire trechos reprovados; se algum controle não existir ou não executar, marque revisão pendente e não entregue minuta como revisada. Suporte: luis@sbroggio.io.
