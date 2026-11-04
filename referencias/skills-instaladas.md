---
tipo: referência
atualizado: 04/11/2026
---

# Skills e plugins instalados na conta do Henrique

Para cada skill: **o que é**, **para que serve** e **quando usar** (com um exemplo de pedido).
Regra: toda instalação nova entra aqui no mesmo dia, por PR.

## Como o Claude escolhe a skill

1. **Automático:** cada skill tem uma descrição. O Claude lê o seu pedido, compara com as descrições e usa a que combina. Você não precisa citar o nome.
2. **Pelo nome:** para garantir, peça "use a skill process-doc", ou digite `/` e o nome.
3. **Desempate:** quando duas skills servem para o mesmo pedido, vale a tabela "Qual usar" no fim deste arquivo.

Legenda: ✅ usar · ⚠️ usar com cuidado · ❌ não usar na ATIVOS.

## 1. Básicas (já vinham ligadas na conta)

| Skill | O que é / para que serve | Quando usar (exemplo) | |
|---|---|---|---|
| docs | Documentos editáveis e compartilháveis no Claude, exportáveis para Word, PDF e Google Docs | "Escreva a política de reembolso da ATIVOS" | ✅ Padrão para documentos |
| docx | Arquivo Word (.docx) | Só quando pedir "em Word" ou mandar um .docx para editar | ✅ |
| xlsx | Planilha Excel ou CSV | "Monte uma planilha de controle de horas" | ✅ |
| pptx | Apresentação PowerPoint | "Faça uma apresentação .pptx para o cliente" | ✅ |
| pdf | Ler, juntar, separar ou criar PDF | "Extraia a tabela deste PDF" | ✅ |
| google-workspace | Criar ou editar arquivos no Google Drive (Docs, Sheets, Slides) | "Crie no Drive a planilha de clientes" | ✅ |
| skill-creator | Criar e melhorar skills próprias | "Vamos criar a skill de projetos da ATIVOS" | ✅ |
| import-memory | Importar memória de outro assistente de IA | Só se trouxer histórico de outro assistente | ⚠️ Raro |
| morning | Resumo da manhã (agenda, e-mails) | Só se pedir "meu resumo da manhã" | ⚠️ Opcional |

## 2. Plugin Operations (Anthropic) — organização e processos

| Skill | O que é / para que serve | Quando usar (exemplo) | |
|---|---|---|---|
| process-doc | Documenta um processo: fluxograma, matriz de responsabilidades (RACI) e procedimento padrão (POP) | "Documente como entregamos o Google Meu Negócio" | ✅ Principal da organização |
| runbook | Passo a passo detalhado de uma tarefa repetitiva, com o que fazer se der errado | "Crie o passo a passo de instalar o Chatwoot na VPS" | ✅ |
| process-optimization | Analisa um processo lento ou confuso e propõe melhorias | "A criação de sites está demorando, o que melhorar?" | ✅ |
| status-report | Relatório de situação com indicadores, riscos e próximos passos (verde, amarelo, vermelho) | "Status semanal dos projetos para os sócios" | ✅ |
| risk-assessment | Identifica, avalia e trata riscos (registro de riscos) | "Quais os riscos do projeto do cliente X?" | ✅ |
| capacity-plan | Carga de trabalho da equipe: cabe mais um cliente? precisa de freelancer? | "Hugo e Bernardo aguentam mais 2 clientes este mês?" | ✅ |
| change-request | Pedido formal de mudança com impacto e plano de volta | "O cliente pediu para mudar o escopo do site" | ✅ |
| vendor-review | Avalia fornecedor: custo, risco, recomendação | "Comparar duas hospedagens de VPS" | ✅ |
| compliance-tracking | Conformidade com normas (SOC 2, ISO, GDPR) | Normas estrangeiras; para LGPD, pedir direto | ❌ Por enquanto |

Conectores do plugin: Asana e Atlassian não são usados pela ATIVOS. Não conectar.

## 3. Plugin Notion (feito pela Notion) — tarefas, projetos e base de conhecimento

| Skill / comando | O que é / para que serve | Quando usar (exemplo) | |
|---|---|---|---|
| tasks:setup | Monta um quadro de tarefas no Notion | Uma vez, ao montar o controle de tarefas | ✅ |
| create-task | Cria uma tarefa no quadro do Notion | "Crie a tarefa: Hugo, wireframe do site, até sexta" | ✅ |
| database-query | Consulta um banco de dados do Notion | "Quais tarefas do Bernardo vencem esta semana?" | ✅ |
| create-page / create-database-row | Cria página ou linha no Notion | "Crie a página do projeto do cliente X" | ✅ |
| search / find | Busca páginas no Notion | "Onde está a ata da reunião de segunda?" | ✅ |
| notion-meeting-intelligence | Prepara reunião: material interno e pauta | "Prepare a reunião de alinhamento com o cliente X" | ✅ |
| notion-knowledge-capture | Transforma uma conversa em página de wiki, decisão ou FAQ | "Registre no Notion a decisão que tomamos agora" | ✅ |
| notion-research-documentation | Junta informações de várias páginas num relatório | "Resuma tudo o que temos sobre tráfego pago" | ✅ |
| notion-spec-to-implementation, tasks:plan, tasks:build, tasks:explain-diff | Transformam especificações em tarefas de programação | Feitas para desenvolvimento de software | ❌ |

## 4. Plugin Slack (feito pela Salesforce, dona do Slack) — comunicação

| Skill / comando | O que é / para que serve | Quando usar (exemplo) | |
|---|---|---|---|
| summarize-channel | Resume um canal | "Resuma o canal #projetos de hoje" | ✅ |
| channel-digest | Resumo de vários canais de uma vez | "O que aconteceu no Slack esta semana?" | ✅ |
| find-discussions | Acha conversas sobre um assunto | "Onde falamos do orçamento do cliente X?" | ✅ |
| standup | Monta a sua atualização diária a partir do que você fez no Slack | "Meu standup de hoje" | ✅ |
| draft-announcement | Prepara um aviso; só vira rascunho no Slack depois da sua aprovação | "Aviso para a equipe sobre o novo padrão de pastas" | ✅ |
| slack-messaging / slack-search | Regras de escrita e de busca usadas pelas outras | Usadas automaticamente | ✅ |

## 5. Skills avulsas (.zip) — financeiro e comercial

Situação em 04/11/2026: **enviadas ao Henrique, aguardando instalação.**

| Skill | O que é / para que serve | Quando usar (exemplo) | |
|---|---|---|---|
| close-management | Roteiro e controle do fechamento mensal (ordem das tarefas, pendências) | "Vamos fechar outubro" | ✅ |
| reconciliation | Conciliação bancária e de contas, com classificação das diferenças | "Concilie o extrato de outubro com os lançamentos" | ✅ |
| financial-statements | DRE, balanço e fluxo de caixa com comparação entre períodos | "Monte a DRE de outubro x setembro" | ✅ Revisar o formato brasileiro |
| variance-analysis | Orçado x realizado, explicando cada diferença | "Por que gastamos mais que o previsto?" | ✅ |
| cash-flow-snapshot | Previsão de caixa para 30, 60 e 90 dias | "Como fica o caixa até janeiro?" | ✅ |
| invoice-chase | Lembretes de cobrança no tom certo; só envia com o seu "pode enviar" | "Quem está em atraso? Prepare as cobranças" | ✅ |
| proposal-builder | Proposta comercial com escopo, preço e prazo; não inventa preço | "Monte a proposta de tráfego pago para a imobiliária X" | ✅ |

## Qual usar (desempate)

| Pedido | Usar | Não usar |
|---|---|---|
| Documento para ler, compartilhar ou assinar | docs | docx (só se pedir Word) |
| Arquivo que fica no Google Drive | google-workspace | docs |
| Tarefa, quadro, sprint, página de projeto | Notion | planilha |
| Procedimento padrão (POP) ou responsabilidades (RACI) | process-doc | runbook |
| Passo a passo técnico de uma tarefa repetitiva | runbook | process-doc |
| Relatório de situação de projetos | status-report | — |
| Riscos de um projeto | risk-assessment (até existir a skill própria de projetos) | — |
| Fechamento do mês | close-management (ela chama as outras quando precisa) | — |
