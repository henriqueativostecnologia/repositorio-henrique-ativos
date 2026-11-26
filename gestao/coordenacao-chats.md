---
tipo: regra de coordenação entre os chats do Claude neste repositório
criado: 25/11/2026
uso: todo chat lê este arquivo no início de cada tema. O lembrete automático (.claude/hooks/lembrete-skills.sh) mostra as últimas linhas do Mural, lidas do main, a cada mensagem
---

# Coordenação entre os chats

**Por que existe:** o Henrique trabalha com mais de um chat no mesmo repositório. Sem coordenação, um chat muda uma regra ou um modelo e o outro continua usando a versão velha. Este arquivo evita isso com 3 regras: **fonte única**, **dono de cada pasta** e **mural de avisos**.

## 1. Os chats

| Chat | Para quê | Dono de (só ele altera) | Lê sempre |
|---|---|---|---|
| **Gestão** (o chat principal do Henrique) | Central de tarefas, projetos, sócios, comercial, financeiro, decisões e aprovação dos PRs | Tudo que não está nas outras linhas | Este arquivo |
| **Máquina Perfil no Google** | Criar, otimizar e manter o Perfil da Empresa no Google de cada cliente, passo a passo, e escrever os POPs desse serviço | `servicos/google-meu-negocio/` (receita e `manual/`) e `plataformas/google-perfil-da-empresa/` | Este arquivo, `CLAUDE.md`, `gestao/instrucoes-claude-tarefas.md` |
| **Prospecção** | Programas de busca | `prospeccao/` | Este arquivo |

## 2. Regras

1. **Fonte única é o `main`.** No início de cada tema, o chat traz o `main` atualizado para a sua branch (`git fetch origin main` e `git merge origin/main`). Nada de trabalhar em cima de versão velha.
2. **Cada pasta tem um dono.** Um chat não altera a pasta de outro. Se precisar de uma mudança lá, escreve um **pedido** no Mural e o chat dono faz.
3. **Mudou algo que afeta o outro chat? Aviso no Mural, no mesmo PR.** Exemplos: regra nova, decisão, modelo, POP novo, coluna ou lista da central, mudança no CLAUDE.md.
4. **Central de tarefas é a mesma para todos.** Cada chat atualiza só as tarefas da sua área, seguindo `gestao/instrucoes-claude-tarefas.md`. O chat da Máquina atualiza as tarefas com Entrega ou área = **Rankeamento**.
5. **Decisão é do Henrique, em qualquer chat.** O que ele decidir num chat vira aviso no Mural para o outro.
6. **Conflito ou dúvida:** o chat não resolve sozinho; pergunta ao Henrique.

## 3. Mural (avisos entre os chats, o mais recente no fim)

Situação: **novo** (o outro chat ainda não aplicou) ou **aplicado** (o outro chat já leu e aplicou, com data). Cada chat lê o Mural no início de cada tema e marca como aplicado o que for para ele.

| Data | De | Para | Aviso | Onde | Situação |
|---|---|---|---|---|---|
| 25/11/2026 | Gestão | Máquina | Chat da Máquina criado. Começar pelo CLI-004 Guto Bebidas, a partir da T-340 (autorização por escrito). Manual: um POP por tarefa da receita, escrito à medida que o trabalho acontece | `servicos/google-meu-negocio/`, central T-248 a T-259 e T-340 | novo |
| 25/11/2026 | Gestão | Máquina | Regras oficiais do Google salvas (todas as políticas e diretrizes da lista oficial). Pontos do Guto: bebida alcoólica só com loja física (confirmada); nada de bebida na seção Produtos; sem post de oferta; nome igual ao da placa | `plataformas/google-perfil-da-empresa/oficial/README.md` | novo |
| 25/11/2026 | Gestão | Máquina | Anotações do curso do Henrique (até o módulo 04, aula 06; o curso tem mais de 16 módulos) no Drive, 80 Treinamentos › Curso SEO Google Meu Negócio. 4 dicas do curso contrariam a regra oficial: serviços como produtos (não para bebida), post de oferta (não para bebida), palavra-chave no nome (nunca) e capa feita por IA (preferir foto real) | Drive | novo |
| 26/11/2026 | Gestão | Máquina | Central com 2 colunas novas: Q Descrição (obrigatória quando o nome não se explica) e R Prazo original (nunca alterar) (regras em `gestao/instrucoes-claude-tarefas.md`). As descrições das tarefas de Rankeamento do Guto (T-248 a T-259) ficam com a Máquina, junto com os POPs | `gestao/instrucoes-claude-tarefas.md` | novo |
| 26/11/2026 | Gestão | Máquina | Revisão dos sócios (26/11): T-098 (CLI-001 Dr. Felipe) virou "Verificar se o Dr. Felipe já tem perfil no Google e pegar o acesso de administrador" (ele provavelmente já tem perfil). Tarefas de perfil do CLI-001 e do CLI-003 seguem pelo modelo antigo até a revisão pelas receitas v2 | Central, T-097 a T-102 e T-142 a T-147 | novo |
| 26/11/2026 | Gestão | Máquina | Contexto pronto no Drive: (1) **Ficha do cliente CLI-004 Guto Bebidas** (loja física, endereço, canais, cardápio, regras de bebida, o que falta pedir) em CLI-004 › 02 Briefing e materiais do cliente; (2) **planilha do cardápio** com 233 itens e preços de 25/11, na mesma pasta; (3) **resumo dos materiais do curso** (13 arquivos, segurança das 7 skills e 10 conflitos com a regra oficial) em 80 Treinamentos › Curso SEO Google Meu Negócio. As skills do curso não estão instaladas: instalar só depois do checklist de `referencias/` | Drive | novo |
| 26/11/2026 | Gestão | Máquina | Decisão do Henrique: o perfil do CLI-004 Guto Bebidas será criado pela **conta de agência (organização) do perfil Maestro** no Perfil da Empresa no Google, já criada para gerenciar os perfis dos clientes. Não depende de liberar o serviço no Workspace da ATIVOS. Regra de terceiros: o Guto fica como proprietário (transferir para o e-mail dele) e a autorização por escrito (T-340) vem antes de criar | Ficha do Guto no Drive | novo |
| 26/11/2026 | Gestão | Máquina | **Leia primeiro `servicos/google-meu-negocio/contexto-inicial.md`**: mapa de tudo sobre o Perfil no Google (decisões, regras oficiais, curso e materiais no Drive, fontes da ATIVOS e situação do Guto). 26/11: o Guto autorizou por escrito (T-340 Feito) | `servicos/google-meu-negocio/contexto-inicial.md` | novo |
