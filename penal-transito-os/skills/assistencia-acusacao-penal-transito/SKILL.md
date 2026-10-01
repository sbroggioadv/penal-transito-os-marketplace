---
name: assistencia-acusacao-penal-transito
description: "Use na representação da vítima ou família em ação penal por crime de trânsito, para examinar habilitação como assistente, poderes e reparação dentro dos autos penais."
---

# Assistência da acusação em crime de trânsito

> Camada C5. Guidance only; a análise e os controles são executados pelo agente e exigem revisão do advogado.

## Entrada e fronteira

Receber identificação privada do sinistro, polo escolhido, tipo CTB imputado, fase, juízo, vínculo documental do assistido com a vítima, ação penal, pedido e decisão de admissão, manifestação do MP, prova do prejuízo e objetivo. Antes de qualquer peça, consultar a triagem e o índice privado de conflitos: oposição entre clientes no mesmo sinistro bloqueia a rota. Não assumir a função do MP nem redigir denúncia pública. Não abrir ação cível autônoma.

## Fontes locais de leitura obrigatória

- `context/ctb-penal-transito.md:73-83` (art. 291) e `:105-111` (art. 297: depósito, teto pelo prejuízo demonstrado, remissões e desconto).
- `context/cpp-complemento-ctr2.md:69` (art. 31), `:407-421` (arts. 268–273), `:535-543` (art. 387 IV), `context/codigo-penal-complemento-ctr2.md:239-241` (CP 91 I) e `context/codigo-penal-complemento-ctr2.md:77-107` (CP 49–52).
- `context/lei-9099-jecrim.md:17-19,23` (competência e conexão), `:67-69` (art. 74: título civil; renúncia apenas nas ações privada ou pública condicionada). Confirmar texto, versão, data e alcance antes de citar; endereço é localizador, não atestado de vigência.

## Procedimento

1. Distinguir ofendido, representante legal e pessoa do rol do CPP 31, verificando morte/ausência judicial e vínculo. Não habilitar familiar automaticamente. Confirmar ação pública, polo, fase e impedimento de corréu. Para JECRIM, legitimidade da vítima/assistente além do texto local permanece 🟡: não importar poderes da vara comum sem base.
2. Na vara comum, separar **pedido de admissão** de **atuação já admitida**. Conferir oitiva prévia do MP e decisão nos autos (CPP 268–273); a causa é recebida no estado em que se acha. Sem decisão, produzir somente minuta de habilitação condicionada e matriz de pendências, não praticar poderes de assistente como fato consumado.
3. Após admissão, limitar requerimento aos poderes do CPP 271 e ao ato/fase demonstrados; verificar conexão com o crime CTB e não substituir a iniciativa pública. Recurso exige a rota `recursos-penal-transito`, hipótese e marcos próprios.
4. Tratar separadamente composição do art. 74, multa reparatória CTB 297 e valor mínimo CPP 387 IV. Composição homologada gera título civil; renúncia só nas ações previstas no parágrafo único. Multa reparatória depende de prejuízo **material demonstrado**, não excede esse valor e será descontada na indenização civil. Valor mínimo exige dano e fundamento nos autos; não somar rubricas sem examinar sobreposição. O cálculo de cada pedido exige documentos, valores, nexo, data e contraditório.
5. Se infração menor foi reunida por conexão/continência no juízo comum, preservar análise de composição e transação para **a infração menor reunida** (Lei 9.099 art. 60, parágrafo único); não transferir instituto ao crime maior nem negar só pela vara comum. Para 306/308 caput, pena máxima excede art. 61: JECRIM apenas após desclassificação/nova capitulação comprovada 🟡.

## Entrega e bloqueios

Entregar matriz `pessoa → vínculo/prova → ação/juízo/fase → admissão/decisão → poder invocado → prejuízo/prova → pedido cabível → fonte/trecho → pendência`, seguida, quando possível, de minuta para revisão humana. Vínculo, admissão, fase, dano ou quantum não demonstrados bloqueiam pedido dependente. Rotular inferências e valores incertos 🟡; não inventar recibo, laudo, protocolo ou decisão. Estado: `MINUTA PARA REVISÃO HUMANA`, `PENDENTE DE PROVA`, `PENDENTE DE FONTE`, `BLOQUEADO` ou `FORA DO RECORTE`. Dados de cliente ficam apenas na pasta privada por matéria, fora do código; sem envio externo. Suporte: luis@sbroggio.io.

## Controles obrigatórios, também em chamada direta

Executar `anti-alucinacao-penal-transito` sobre existência/proveniência de cada fato, documento e citação; depois `validador-penal-transito` para dispositivo → arquivo/linha → trecho → versão/data → alcance, sem completar remissões ausentes; por fim `suprema-corte-penal-transito` R1 polo/fatos/fase/competência, R2 tipicidade/tempo, R3 prova/precedentes, R4 forma/prazo/cálculo/fronteira. Registrar resultado e pendências dos três na entrega; falha ou ausência de controle bloqueia rótulo de peça pronta. São instruções ao agente, guidance only, não prova de execução automática.
