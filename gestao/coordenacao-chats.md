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
