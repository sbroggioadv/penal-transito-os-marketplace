# Penal Trânsito OS

`penal-transito-os` · versão 0.1.0 · Luis Sbroggio · suporte: **luis@sbroggio.io**.

Plugin para o advogado criminalista que atua na **defesa do acusado** ou na **assistência de acusação da vítima/família** em matéria penal de trânsito. A versão contém **20 skills em 6 camadas e 17 comandos**.

## Uso e controles

Execute `/penal-transito-install` para configurar a pasta privada e o índice de matérias; use `/penal-transito-master` para conduzir a demanda. As skills e os comandos exigem triagem, guard de fatos e fontes, validação normativa e revisão R1→R4. Essas chamadas são orientações para o agente: o hook `SessionStart` apenas informa a presença do plugin e **não executa** validação jurídica ou revisão automática. O advogado deve conferir as saídas e os controles efetivamente executados.

## Recorte

- Crimes de trânsito do CTB 291–312-B e prova penal relacionada ao art. 277, do flagrante aos recursos, com reparação da vítima **dentro da ação penal**.
- Polo escolhido por matéria, com índice privado para impedir atuação em lados opostos do mesmo sinistro. Dados de clientes ficam separados por matéria, fora do repositório e de qualquer pacote de distribuição.
- Ficam fora do produto o processo administrativo de multas/CNH, o processo penal comum independente do CTB, o júri de homicídio doloso, a execução penal/LEP, a ação cível autônoma e os papéis de Ministério Público, juiz e perito.
- Normas só podem ser usadas a partir do texto literal em `context/`. Artigo sem texto permanece 🟡 e não sustenta conclusão. Súmula ou tema sem inteiro teor validado permanece identificado apenas pelo número e 🟡. Não usar Jusbrasil como fonte.
- Para fatos e exames até **17/08/2026**, examinar a Resolução Contran 432/2013 como regime histórico; para ambos desde **18/08/2026**, examinar a Resolução Contran 1.031/2026. Datas cruzadas e retroatividade exigem análise jurídica específica 🟡.
- Toda futura skill de mérito deve fechar chamando `anti-alucinacao-penal-transito`, `validador-penal-transito` e `suprema-corte-penal-transito`. A presença dessas chamadas precisará ser verificada em cada caminho. Cada `SKILL.md` deve ter no máximo **11.004 bytes UTF-8**, medidos com `wc -c`.

## Estrutura

```text
.claude-plugin/plugin.json
.claude-plugin/marketplace.json
hooks/hooks.json
context/
skills/ (20 skills)
commands/ (17 comandos)
LICENCA
README.md
```

O `marketplace.json` do source aponta para `./`. A cópia de `context/` preserva os textos, índices e manifestos de captura; ela não prova vigência, completude ou aplicação ao caso concreto. Uso sujeito à [LICENCA](LICENCA) e à revisão humana do advogado.
