---
name: triagem-penal-transito
description: "Classifica polo, conflito entre sessões, competência, tipo CTB, fase e regime temporal de alcoolemia antes de qualquer peça penal de trânsito."
---

# Triagem penal de trânsito

**Guidance only:** triagem documenta condições; não decide competência judicial nem substitui revisão humana. Para toda saída jurídica, concluir com `anti-alucinacao-penal-transito`, `validador-penal-transito` e `suprema-corte-penal-transito` R1→R4; se chamada dentro do master, os controles finais podem ser executados uma vez sobre a saída consolidada, com registro explícito.

## Identificar caso e polo

Receber sinistro, data/local, pessoas e cliente, polo da **defesa** ou da **vítima/família**, vínculo/mandato desta, condutor, imputação, objetivo, urgência, prisão/liberdade, fase, ato/decisão/intimação, datas do fato e do exame e documentos reais. Consultar obrigatoriamente o índice de matérias na pasta privada, inclusive registros de sessões anteriores. Comparar sinistro, data e partes; se houver defesa e assistência em lados opostos do mesmo caso, **BLOQUEADO** e nenhuma peça. Se o índice estiver inacessível, registrar `PENDENTE DE PROVA` de conflito e impedir rota dependente. Não assumir legitimidade de familiar pelo parentesco: verificar vínculo, representação e admissão quando cabível (`context/cpp-complemento-ctr2.md`, arts. 268–273; conferir trecho).

## Competência e rito antes do mérito

Registrar **juízo efetivo comprovado**, ato de distribuição/declínio, tipo e pena aplicável, fase, conexão/continência e eventual nova capitulação. Lei 9.099, art. 60 (`context/lei-9099-jecrim.md:17–19`) respeita conexão e continência; art. 61 (`:23`) define menor potencial ofensivo pela pena máxima até dois anos. Na reunião por conexão/continência perante juízo comum, preservar exame de transação penal e composição dos danos civis **para a infração de menor potencial ofensivo reunida** (art. 60, parágrafo único, `:19`), sem prometer cabimento concreto. Exemplo a testar: 302 + 304 conexos não elimina automaticamente a análise do 304. Composição e transação têm requisitos distintos; conferir Lei 9.099 arts. 74 e 76, além de CTB 291 §1º I–III (`context/ctb-penal-transito.md:73–83`).

CTB 306 e 308 caput têm pena máxima de três anos (`context/ctb-penal-transito.md:177–179,199–201`): **vara comum para a imputação original**. Cogitar JECRIM somente diante de desclassificação/nova capitulação para infração de menor potencial ofensivo **comprovada nos autos** 🟡; sem isso, não oferecer rito sumaríssimo ou transação como decorrência do 306/308. Se juízo/competência/declínio não estiverem comprovados, marcar 🟡 e bloquear minuta cujo rito ou prazo dependa da escolha. No JECRIM, verificar rito e recursos da Lei 9.099; na vara comum, os do CPP. Não transferir automaticamente CPP 396-A ou prazos CPP 593/600 ao JECRIM.

## Versão temporal e fronteiras

Para alcoolemia, registrar separadamente **data do fato e data do exame**. Ambas até **17/08/2026**: Resolução Contran 432/2013 histórica. Ambas desde **18/08/2026**: Resolução 1.031/2026. Âncora da revogação e início de vigência geral: `context/contran-1031-2026-texto-extraivel.md:289–296`; o art. 14/Anexo III tem início específico em 60 dias e o Anexo III é imagem 🟡. Datas cruzadas ou retroatividade benéfica (CP 2º, parágrafo único, `context/codigo-penal-complemento-ctr2.md:21`) exigem revisão jurídica 🟡; não escolher automaticamente uma resolução nem aplicar a 432 a fato posterior. Sem data ou exame documentado, bloquear cálculo/conclusão dependente.

Separar crime CTB de multa/suspensão administrativa; possível dolo/júri sai deste produto, sem construir peça de júri. Parcela externa: penal comum/júri → `criminal-adv-os`; administrativo de trânsito → `transito-adv-os`, como referências opcionais, sem exigir instalação ou oferecer cross-sell. LEP, ação cível autônoma e atuação como MP, juiz ou perito também saem. Reparação pedida **na ação penal** permanece possível no recorte, sujeita a prova e fundamento. Não inventar processo, teste, laudo ou decisão.

## Saída

Entregar quadro **questão → fato/prova/arquivo → fundamento e linha → estado → pendência/etapa bloqueada**; indicar polo, índice consultado, competência real ou 🟡, conexão, versão temporal, tipo/ramo e destino instalado. Sem prova crítica, somente mapa de pendências. Finalizar pela cadeia de três controles sem afirmar execução simulada.
