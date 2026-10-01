---
name: anti-alucinacao-penal-transito
description: "Confere existência e proveniência de fatos, documentos, eventos, citações e precedentes em qualquer entrega penal de trânsito, bloqueando invenções."
---

# Guard anti-alucinação penal de trânsito

**Guidance only:** controle por instrução, sem garantia mecânica de hook. Receber saída real, documentos e fontes. Se não houver minuta, auditar somente a matriz ou pendência recebida; não inventar minuta para simular revisão. Esta skill cuida de existência/proveniência; teor, versão e alcance normativo são do `validador-penal-transito`.

Para cada afirmação, numerar e classificar: fato comprovado, declaração atribuída, texto normativo, inferência, proposta ou pendência. Registrar documento/arquivo, página ou trecho, emissor e data quando houver. Declaração do cliente não prova laudo, teste, certificado de etilômetro, valor medido/considerado, sinais, prisão, fiança, denúncia, intimação, decisão, trânsito ou admissão do assistente. Distinguir ausência de documento de prova da inexistência do evento.

Conferir citações no texto literal de `context/`, preservando negadores, incisos, números e ressalvas. Citação literal inexata vira paráfrase identificada ou é removida. **Nunca** fabricar laudo, resultado de teste, testemunho, perícia, cadeia de custódia, precedente ou número de processo. Súmula/tema sem inteiro teor oficial e situação verificados: registrar somente número e **🟡**, sem atribuir tese. Não usar Jusbrasil nem importar conteúdo de outros plugins.

Para cálculo, exigir dados, unidade, datas e fórmula; não converter mg/L, dg/L, valor medido e considerado por estimativa própria. Para representação e conflito, exigir índice privado e documentos de vínculo/mandato/admissão; não expor dossiê no source ou serviço externo sem autorização.

Entregar matriz **ID → afirmação/tipo → suporte/trecho → estado → correção ou bloqueio**. Fato ou fonte inventada essencial gera `BLOQUEADO`; material ausente gera `PENDENTE DE PROVA` ou `PENDENTE DE FONTE`. Passar a versão efetiva ao validador e à Suprema Corte na cadeia, sem chamadas recursivas se já estiver atuando como parte dela.
