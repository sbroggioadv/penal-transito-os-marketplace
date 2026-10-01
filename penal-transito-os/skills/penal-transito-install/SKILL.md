---
name: penal-transito-install
description: "Configura o penal-transito-os para o advogado criminalista da defesa ou da vítima, com pasta privada, índice de matérias e primeiro uso, sem analisar um caso na instalação."
---

# Instalação — penal de trânsito

**Guidance only:** estas instruções não substituem verificação de acesso, sigilo ou conflito. A instalação não produz conclusão jurídica. Suporte: **luis@sbroggio.io**.

## Passo 0 — pasta privada

Orientar o advogado a criar ou selecionar sua pasta **CoWork OS** privada fora do source e de repositório compartilhado: Windows `C:\CoWork OS`; Mac, pasta `CoWork OS` na pasta do usuário. Confirmar caminho e autorização de acesso antes de gravar. Não vasculhar pastas nem mover documentos sem pedido. Se faltar acesso, entregar configuração na conversa como pendente, sem fingir persistência.

Manter uma pasta por matéria e cliente. Criar, na pasta privada, um **índice de matérias** que permita consultar sessões futuras: identificador do sinistro, data, partes envolvidas, cliente assistido, polo (defesa ou vítima/família), caminho da pasta e estado de conflito. Usar somente os identificadores necessários; não guardar autos nem exemplos identificáveis no plugin. Antes de acrescentar matéria, ler o índice existente, confrontar sinistro/data/partes e impedir atuação em polos opostos do mesmo caso. Não substituir o exame ético de conflito por mera coincidência de nomes. Se o índice não puder ser lido, a análise do novo caso fica pendente.

## Configurar

Perguntar uma coisa por vez. Para listas fechadas, usar `AskUserQuestion` com no máximo quatro opções; se indisponível, oferecer alternativas numeradas e não alegar que houve botões. Nome, OAB, cidade e caminho aceitam texto livre.

1. Caminho da pasta privada e acesso concedido.
2. Papel: **advogado da defesa**, **advogado da vítima/família**, **a definir**, **outro**. O polo é escolhido por matéria, não globalmente; outro papel não autoriza atuar como MP, juiz ou perito.
3. Primeiro objetivo: **triagem de caso**, **revisão de material**, **conhecer fluxos**, **a definir**.
4. Tom: **objetivo**, **didático**, **técnico**. Nenhuma escolha desliga guard, validador ou R1→R4.

Mostrar resumo e pedir **confirmar**, **corrigir** ou **não salvar**. Persistir apenas perfil/preferências e índice privado se houver confirmação e acesso real; reconciliar arquivos preexistentes, sem sobrescrever ou criar registro de caso fictício. Registrar o caminho efetivamente usado. Nunca recolher acervo de cliente na instalação.

## Primeiro uso

Orientar `/penal-transito-master` com cliente, polo, fato CTB, data do fato e de eventual exame, fase, juízo, objetivo e documentos disponíveis, em pasta privada. Conferir presença das skills de triagem e dos três controles antes de anunciar o fluxo como disponível. A triagem consulta o índice **em cada caso**, inclusive entre sessões. Dados jurídicos permanecem na matéria privada; não enviar documentos a serviço externo sem autorização específica. Não prometer sincronização ou publicação não comprovada.
