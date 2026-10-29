---
tipo: método
tema: gestão de projetos
versão: 1 (29/10/2026)
origem: conversa no cofre pessoal do Henrique; base para a skill pmo-ativos
---

# Sistemática de gestão de projetos da ATIVOS

Como a ATIVOS organiza clientes, projetos, rotinas e tarefas, e qual o papel de cada ferramenta (Notion, Slack, Claude, Google Drive e Todoist).

---

## 1. O ponto de partida: o que a ATIVOS vende

A ATIVOS tem **três linhas de serviço**, e elas não funcionam do mesmo jeito:

| Linha de serviço | O que inclui | Tipo de trabalho |
|---|---|---|
| **Posicionamento digital** | Landing page comercial, otimização do Google Meu Negócio, sustentação do site | **Projeto de implantação** (começo, meio e fim) + **rotina mensal** (sustentação) |
| **Marketing digital** | Gestão de anúncios (Instagram, Facebook, Google), criação de criativos (fotos, vídeos, carrosséis), otimização das campanhas | **Rotina mensal** |
| **Automação comercial** | IA no WhatsApp (triagem), follow-up automático, agendamentos | **Projeto de implantação** (configurar e testar) + **rotina mensal** (acompanhar e ajustar) |

O serviço "de rua" para comércio local (Google Meu Negócio + landing page) é uma versão menor da primeira linha.

**Por que isso importa:** projeto e rotina se controlam de jeitos diferentes. **Projeto** se mede por **prazo e entrega** ("a página foi entregue no dia combinado?"). **Rotina** se mede por **regularidade e resultado do mês** ("as campanhas rodaram o mês todo? quantos contatos geraram?"). Misturar os dois numa lista só é o que faz uma agência perder o controle.

---

## 2. O modelo: projetos + rotinas, organizados por cliente

É um **modelo híbrido leve**: o essencial do PMBOK (escopo, fases, aceite) para os projetos e o essencial do ágil (quadro Kanban, ciclos curtos) para o dia a dia.

| Peça | Para que serve | Exemplo |
|---|---|---|
| **Cliente** | Reúne tudo de um cliente num lugar só | Um cliente com 3 serviços contratados |
| **Serviço contratado** | Cada linha de serviço que o cliente comprou, com valor, início e situação | "Marketing digital, mensal, desde 01/11" |
| **Projeto de implantação** | Tudo que tem começo e fim. Tem **escopo**, **fases com marcos** e **aceite do cliente** | "Implantar landing page e Google Meu Negócio" |
| **Rotina mensal** | Tudo que se repete todo mês, sempre no mesmo ciclo: **planejar → executar → otimizar → relatório** | "Anúncios de novembro" |
| **Tarefa** | A menor unidade de trabalho, com responsável e prazo | "Criar 3 carrosséis dos veículos novos" |
| **Quadro de tarefas (Kanban)** | Mostra o trabalho de **todos os clientes** num quadro só | Colunas: A fazer · Fazendo · Esperando o cliente · Em revisão · Feito |
| **Status semanal** (interno) | Uma vez por semana: o que andou, o que travou, próximos passos | Resumo de sexta-feira no Slack |
| **Relatório mensal** (para o cliente) | Mostrar o resultado do mês | Números das campanhas e do atendimento |
| **Mudança de escopo** | Pedido do cliente fora da proposta vira **mudança aprovada**, com prazo e preço, nunca trabalho de graça | "Quero mais 5 páginas no site" |

### As fases padrão de um projeto de implantação
1. **Abertura:** escopo combinado a partir da proposta, responsáveis, prazo, o que **não** está incluso. Nada começa sem isso aprovado.
2. **Coleta:** acessos, fotos, logotipo, informações do cliente. É onde os projetos mais atrasam: tudo que depende do cliente fica na coluna "Esperando o cliente".
3. **Produção:** construir (página, ficha do Google, automação).
4. **Revisão e aceite:** o cliente aprova por escrito.
5. **Publicação:** colocar no ar.
6. **Passagem para a rotina:** o projeto acaba e começa a rotina mensal (sustentação, acompanhamento).

### O ciclo padrão de uma rotina mensal
1. **Planejar** (início do mês): metas do mês e tarefas da rotina.
2. **Executar** (durante o mês): as tarefas no quadro.
3. **Otimizar** (meio do mês): ajustar o que não está dando resultado.
4. **Relatório** (fim do mês): resultado para o cliente e aprendizado para o próximo mês.

---

## 3. O papel de cada ferramenta

**Regra principal: cada coisa mora num lugar só.** Uma tarefa guardada em duas ferramentas vira duas listas desatualizadas.

| Ferramenta | Papel | O que **não** faz |
|---|---|---|
| **Notion** | **A fonte da verdade:** clientes, serviços contratados, projetos, rotinas e o quadro de tarefas | Não é lugar de conversa |
| **Slack** | **A conversa:** um canal por cliente e um canal de status | Não guarda tarefa: o que vira trabalho vai para o Notion |
| **Claude (conta da ATIVOS)** | **O assistente do gerente:** conectado ao Notion e ao Slack, monta escopo e cronograma, gera as tarefas da rotina do mês, escreve o status semanal e o relatório mensal, avisa sobre riscos e mudança de escopo | Não aprova nada sozinho: decisões e envios ao cliente passam por uma pessoa |
| **Google Drive** | **Os arquivos:** propostas, contratos, fotos, criativos, relatórios | Não controla prazo nem tarefa |
| **Todoist** | Só lista **pessoal** de cada um, ou deixa de ser usado | Não guarda tarefa de projeto |

---

## 4. Como fica no Notion

Cinco tabelas ligadas entre si:

```
Clientes
  └── Serviços contratados (linha, valor, início, situação)
        ├── Projetos de implantação (fase, prazo, responsável, aceite)
        └── Rotinas mensais (mês, situação, relatório)
              └── Tarefas (responsável, prazo, status) ← o quadro Kanban
```

- **Clientes:** nome, segmento, contato principal, link da pasta no Drive, canal no Slack.
- **Serviços contratados:** cliente, linha de serviço, valor de implantação, mensalidade, data de início, situação (ativo, pausado, encerrado).
- **Projetos:** serviço, fase atual, data de início, prazo, responsável, escopo (página), aceite do cliente (sim/não, data).
- **Rotinas:** serviço, mês, situação, link do relatório.
- **Tarefas:** projeto ou rotina, responsável, prazo, status (as colunas do quadro), prioridade.

Cada projeto e cada rotina começa de um **modelo** (template) com as tarefas padrão da sua linha de serviço.

**Plano do Notion:** o plano grátis trava em 1.000 blocos quando o espaço de trabalho tem 2 ou mais membros. Se mais de uma pessoa mexer nos projetos todo dia, o plano **Plus** (cerca de US$ 10 por membro por mês; confira o preço atual) resolve. A alternativa grátis é um único membro com a equipe como convidada (até 10).

---

## 5. Como fica no Slack

| Canal | Para quê |
|---|---|
| `#status` | Resumo semanal de todos os projetos (o Claude pode escrever o rascunho) |
| `#cli-nome-do-cliente` | Conversas, dúvidas e combinados de cada cliente |
| `#geral` | Assuntos da equipe |

**Regra:** combinou algo no Slack que vira trabalho? Vira **tarefa no Notion**.

---

## 6. Como fica no Google Drive

```
ATIVOS/
  Clientes/
    Nome do cliente/
      01 Comercial (proposta, contrato)
      02 Projetos (uma pasta por projeto)
      03 Rotinas (uma pasta por mês)
      04 Materiais do cliente (logotipo, fotos, acessos)
  Modelos/ (proposta, escopo, relatório)
  Interno/
```

O link da pasta de cada cliente fica registrado no Notion.

---

## 7. A semana do gerente de projetos

| Quando | O quê |
|---|---|
| Segunda | Olhar o quadro: prioridades da semana e o que está esperando o cliente |
| Diário | Atualizar o status das tarefas no Notion |
| Sexta | Status semanal no `#status` (com o rascunho do Claude) |
| Início do mês | Abrir as rotinas do mês a partir dos modelos |
| Fim do mês | Relatórios mensais para os clientes |

---

## 8. Próximos passos
1. Decidir o plano do Notion e montar as 5 tabelas e os modelos.
2. Criar os canais do Slack e organizar as pastas do Drive.
3. Conectar o Claude da ATIVOS ao Notion e ao Slack.
4. Abrir os dois primeiros clientes nessa estrutura.
5. Transformar esta sistemática na skill **pmo-ativos**, para o Claude seguir sozinho.
