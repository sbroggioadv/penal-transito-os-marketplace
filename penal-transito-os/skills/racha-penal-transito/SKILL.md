---
name: racha-penal-transito
description: "Examina corrida, disputa, exibição ou manobra do CTB 308 com prova individual de conduta, autorização, risco e eventual resultado."
---

# Racha penal de trânsito

> C2. Guidance only; a análise e os controles são executados pelo agente e exigem revisão do advogado.

## Entrada e fontes

Receba polo, data, local/via, descrição de cada participante, autorização alegada, registros de imagem, testemunhas, laudos, risco, resultado, imputação e fase. Leia `context/ctb-penal-transito.md` art. 308 caput e §§1º–2º (199–205), art. 291 (73–88); `context/codigo-penal-disposicoes-gerais.md` arts. 13/18 (15–41) quando houver resultado. Versão histórica da redação deve ser verificada para fatos antigos.

## Procedimento

1. Classifique separadamente corrida, disputa, competição, exibição ou demonstração de perícia em manobra. Exija direção de veículo em via pública, ausência de autorização pertinente e situação concreta de risco; velocidade por si só não comprova 308.
2. Crie matriz `elemento → fato de cada agente → arquivo/trecho de prova → fundamento → objeção → estado`. Indique o que é observação e o que é inferência; não atribua conduta coletiva sem prova individual.
3. Para §1º/§2º, confira lesão grave ou morte, nexo causal e as circunstâncias de ausência de vontade ou assunção do risco do resultado. Classificação de lesão grave que dependa do CP 129 §§1º–2º fica 🟡 `PENDENTE DE FONTE`; sem laudo ou resultado comprovado, bloqueie a forma qualificada.
4. Distinga eventual imputação dolosa: se exigir atuação penal comum ou júri, encaminhe `FORA DO RECORTE` sem produzir peça desses ritos. Se conexão alterar competência, registre juízo real; para crime de menor potencial ofensivo conexo na vara comum, preserve exame próprio da Lei 9.099 art. 60, parágrafo único (`context/lei-9099-jecrim.md:17–19`). O 308 caput, com máximo textual de três anos, não vira JECRIM/transação por mera dúvida: isso requer nova capitulação comprovada.

## Saída e revisão obrigatória

Entregue matriz por agente, tese e resposta do polo, pedidos condicionados à fase, lacunas e `MINUTA PARA REVISÃO HUMANA` se houver base. Provas do cliente ficam fora do source, em pasta privada por matéria. Use só texto verbatim em `context/`, sem Jusbrasil; dispositivo/precedente sem texto é 🟡. Ao final, mesmo bloqueada, execute `anti-alucinacao-penal-transito` → `validador-penal-transito` → `suprema-corte-penal-transito` (R1 fatos/polo, R2 tipo/temporalidade, R3 prova, R4 forma). Controle ausente impede entrega como pronta.
