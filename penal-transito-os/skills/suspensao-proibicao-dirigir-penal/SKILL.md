---
name: suspensao-proibicao-dirigir-penal
description: "Distingue cautelar, pena e descumprimento penal de dirigir em caso CTB, para defesa ou assistência."
---

# Suspensão e proibição penal de dirigir

> Camada C3. Atue pelo advogado do polo identificado. Controle por instrução (guidance only); o plugin não impõe, revoga nem cumpre decisão judicial.

## Entrada

Registre sinistro, partes, polo, tipo CTB, data do fato, fase, decisão/título integral, intimação, prazo, documentos de habilitação, certidão de trânsito em julgado quando alegado, atos de entrega e prova de eventual direção/descumprimento. Consulte o índice privado entre sessões e bloqueie atuação em polos opostos do mesmo sinistro. Guarde os dados somente na pasta privada da matéria. Sem título, ciência ou prova necessária, marque 🟡 e não gere pedido ou imputação categórica dependente.

## Separe três naturezas

1. **Pena penal:** leia `context/ctb-penal-transito.md:89-95` (CTB 292–293) e `:103` (296). Identifique condenação, imposição isolada/cumulativa, duração, reincidência realmente comprovada e trânsito. O CTB 293 §§1º–2º disciplina intimação para entrega e início da penalidade nas condições expressas; não transforme fase de investigação em cumprimento de pena.
2. **Cautelar penal:** leia `context/ctb-penal-transito.md:97-99` (CTB 294) e `context/cpp-complemento-ctr2.md:423-444,447-533` (CPP 282–283/311/313–318-B/320), além de `context/cpp-penal-transito.md:177-222` (CPP 312/319). Identifique pedido/representação, decisão motivada, necessidade, adequação, contraditório e situação atual. O recurso em sentido estrito do CTB 294, parágrafo único, exige decisão enquadrável, legitimidade, ciência e prazo verificados; o texto do CTB 294 parágrafo único diz expressamente "sem efeito suspensivo" (`context/ctb-penal-transito.md:99`). Não confunda proibição de se ausentar do país do CPP 320 com suspensão da habilitação.
3. **Infração penal por descumprimento:** leia `context/ctb-penal-transito.md:193-197` (CTB 307). Faça matriz separada para violação de suspensão/proibição e para não entrega após prazo do CTB 293 §1º. Exija ato de suspensão/proibição fundamentado no CTB, ciência quando relevante e conduta demonstrada; ausência documental 🟡 impede afirmar consumação. Se a suspensão violada tiver origem administrativa, a imputação **penal** do 307 continua no recorte: exponha 🟡 as duas leituras possíveis de "imposta com fundamento neste Código" — abrangência ou não de título administrativo — para ambos os polos, sem resolver a controvérsia sem fonte e revisão jurídica. Só o processo administrativo de suspensão, multa e defesa perante DETRAN/JARI/CETRAN ficam `FORA DO RECORTE`.

## Análise do polo e limites

Defesa: teste tipicidade, fundamento, proporcionalidade, duração, ciência e revogação/substituição cabível. Assistência: identifique admissão/legitimidade processual, prova e pedido que pode formular sem assumir papel do MP ou do juiz. Para qualquer fundamento, registre `artigo/parágrafo → context/arquivo:linhas → trecho → redação/data → alcance → fato comprovado`. Texto compilado atual não comprova automaticamente vigência na data do fato.

O cumprimento nesta skill abrange só CTB 293 §§1º–2º, 295 (`context/ctb-penal-transito.md:101`) e 307 parágrafo único. Não gerencie execução penal/LEP ou outros atos posteriores ao trânsito; encaminhe esses atos à ferramenta própria. Não prometa restituição ou suspensão por mera alegação.

## Saída e revisão

Entregue tabela `natureza → título/fase → prova → regra e trecho → pedido/resposta do polo → pendência`, cronologia de intimação e atos, argumentos contrários e status `MINUTA PARA REVISÃO HUMANA`, `PENDENTE DE PROVA`, `PENDENTE DE FONTE`, `BLOQUEADO` ou `FORA DO RECORTE`. Lacuna impeditiva exclui minuta apresentável.

Ao final, execute `anti-alucinacao-penal-transito` → `validador-penal-transito` → `suprema-corte-penal-transito` em R1 fatos/polo/fase/competência, R2 tipicidade/tempo, R3 prova/citações e R4 forma/prazo/limites. Corrija ou retire o reprovado; dependência não disponível mantém revisão pendente e impede rotular a minuta como revisada. Suporte: luis@sbroggio.io.
