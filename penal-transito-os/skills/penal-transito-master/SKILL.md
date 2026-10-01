---
name: penal-transito-master
description: "Coordena a demanda penal de trânsito da defesa ou da vítima, seleciona a skill CTB pertinente e exige triagem, guard, validador e revisão R1 a R4."
---

# Master — caso penal de trânsito

**Guidance only:** chamadas de skills são instruções ao agente, sem enforcement por hook. Não declarar revisão executada sem saída real de cada controle.

## Entrada e percurso

Receber cliente/polo, sinistro e imputação, datas do fato e de exame, fase/ato, juízo efetivo, conexão ou continência, objetivo, documentos e pendências. Não pedir de novo o que já está documentado. Executar `triagem-penal-transito` antes de escolher rito ou produtora. Conferir índice privado entre sessões. Sem acesso ao índice, polo livre de conflito não está comprovado. Sem competência real, bloquear peça cujo rito ou prazo dependa dela.

Percurso: **triagem → matriz fato/prova/fundamento/versão temporal → skill especializada pertinente → anti-alucinacao-penal-transito → validador-penal-transito → suprema-corte-penal-transito R1→R4 → entrega**. Ler `skills/<nome>/SKILL.md` antes de acionar destino. O master coordena e não redige, por conta própria, peça da skill ausente. Saída de pendências também passa pelos três controles. Chamada direta de produtora e wrapper devem fazer o mesmo; `/penal-transito-revisar` não é pré-requisito para revisar.

## Rotas específicas do rol

| Objeto CTB | Skill |
|---|---|
| Homicídio/lesão culposos | `homicidio-lesao-culposos-transito` |
| Alcoolemia penal | `embriaguez-alcoolemia-penal-transito` |
| Corrida/manobra de risco | `racha-penal-transito` |
| Fuga/omissão de socorro | `fuga-omissao-socorro-transito` |
| Habilitação/entrega | `habilitacao-entrega-veiculo-transito` |
| Velocidade/inovação artificiosa | `velocidade-inovacao-artificiosa-transito` |
| Flagrante/fiança/socorro | `flagrante-fianca-socorro-transito` |
| Suspensão/proibição de dirigir penal | `suspensao-proibicao-dirigir-penal` |
| JECRIM/transação/sursis processual/ANPP | `acordos-penais-transito` |
| Assistência da vítima | `assistencia-acusacao-penal-transito` |
| Resposta/instrução/memoriais do polo | `atuacao-processual-penal-transito` |
| Sentença/pena/perdão | `sentenca-pena-perdao-penal-transito` |
| Prescrição | `prescricao-penal-transito` |
| Recursos | `recursos-penal-transito` |

O rol é mapa, não prova de que uma skill já está instalada. Se destino faltar, indicar dependência sem improvisar seu mérito. Só penal de trânsito e processo ligado ao crime CTB: separar JARI/CETRAN/CNH administrativo, penal comum/júri, LEP, ação cível autônoma e papéis de MP/juiz/perito. Parcela externa: penal comum/júri → `criminal-adv-os`; administrativo de trânsito → `transito-adv-os`, como referências opcionais, sem exigir instalação ou oferecer cross-sell. Preservar assistência e reparação **dentro** da ação penal.

## Entrega

Usar apenas texto literal de `context/`; precedente/súmula/tema sem inteiro teor verificado recebe número e 🟡, sem tese atribuída. Distinguir fato, inferência e pedido; indicar prova e linhas da norma, argumento contrário e cálculo reproduzível quando houver. Registrar resultados reais do guard, validador e R1, R2, R3, R4. Fechar em `MINUTA PARA REVISÃO HUMANA`, `PENDENTE DE PROVA`, `PENDENTE DE FONTE`, `BLOQUEADO` ou `FORA DO RECORTE`, com próxima providência. Não declarar ato externo consumado sem documento.
