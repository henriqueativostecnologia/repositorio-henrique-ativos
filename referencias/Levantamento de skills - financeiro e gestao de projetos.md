# Levantamento de skills e plugins: financeiro e gestão de projetos

Feito do zero em 29/10/2026, a partir das necessidades da ATIVOS, e não da lista da conta pessoal (que fica só como conferência no fim). Fontes: catálogo oficial de plugins do Claude e repositórios do GitHub. Cada item foi passado pelo `Checklist - Avaliar skill de fora.md`.

## O que a ATIVOS precisa

| Tema | Necessidade |
|---|---|
| Gestão de projetos | Abrir projeto (escopo, fases, aceite), riscos, mudança de escopo, status semanal, relatório mensal, capacidade da equipe, documentar processos |
| Financeiro | Fluxo de caixa e previsão, contas a receber (cobrança), DRE e comparação entre períodos, orçado × realizado, conciliação, fechamento do mês, propostas e contratos |
| Ferramentas | Ligar o Claude ao Google Drive, ao Notion e ao Slack |

## Resultado

### Instalar
| Pacote | Origem | Skills que importam | Observação |
|---|---|---|---|
| Finance | Anthropic (instalado) | `financial-statements`, `variance-analysis`, `reconciliation`, `close-management` | `sox-testing`, `audit-support`, `journal-entry` e `journal-entry-prep` desligadas |
| Operations | Anthropic (instalado) | `status-report`, `risk-assessment`, `change-request`, `capacity-plan`, `process-doc`, `runbook`, `process-optimization`, `vendor-review`, `compliance-tracking` | Sem Asana e Atlassian |
| Small Business | Anthropic | `cash-flow-snapshot`, `invoice-chase`, `proposal-builder`, `contract-review`, `close-month`, `month-end-prep`, `report-builder`, `smb-router` | Desligar as skills feitas para sistemas e leis dos EUA (folha, impostos, contas a pagar) e as de outras áreas (anúncios, vagas, estoque). Não conectar QuickBooks, Xero, Stripe e similares |

### Conectores (não são plugins; ligam o Claude às ferramentas)
| Conector | Para quê | Quando |
|---|---|---|
| Google Drive | Ler e organizar as pastas da ATIVOS | Antes do passo do Drive |
| Notion | Montar as tabelas de projetos e tarefas | Antes do passo do Notion |
| Slack | Status semanal e resumo dos canais | Antes do passo do Notion e Slack |

### Não instalar agora
| Item | Origem | Motivo |
|---|---|---|
| Productivity | Anthropic | Guarda tarefas numa lista própria; na sistemática, tarefa mora só no Notion |
| Plugin Notion, plugins Slack | Notion, Slack, Salesforce | Repetem os conectores (checklist itens 9 e 13) |
| Legal | Anthropic | Feito para leis dos EUA; `contract-review` do Small Business cobre o básico |
| Enterprise Search | Anthropic | Útil quando Drive, Notion e Slack já tiverem conteúdo; rever no levantamento geral |
| Product Management | Anthropic | Voltado a produto de software |
| claude-skills (pastas de projetos e finanças) | `alirezarezvani/claude-skills` (MIT, muito usada) | Projetos: centrado em Jira e Confluence, liga o conector da Atlassian (item 13). Finanças: `financial-analyst` repete o Finance; rever só se faltar previsão de caixa |
| claude-project-manager | `KirKruglov/claude-project-manager` (MIT) | Pouco testada (itens 2 e 3) e pode enviar e-mails sozinha (item 7) |
| claude-skills-kit (project-management-kit) | `KirKruglov/claude-skills-kit` (MIT) | Pouco testada (item 2). Bons modelos: usar como leitura na pmo-ativos |
| planning | `jkitchin/skillz` | Só como leitura de modelos na pmo-ativos |
| 24-finance-skills, openaccountant/skills | GitHub | Pouco testadas e voltadas a finanças pessoais ou dos EUA |

## Conclusão

- **Gestão de projetos:** Operations + a nossa skill **pmo-ativos** (feita a partir da sistemática, com ideias dos modelos do project-management-kit e da planning). Não existe pacote pronto melhor para uma agência pequena que usa Notion e Slack.
- **Financeiro:** Finance + parte do Small Business. As regras fiscais e contábeis brasileiras vêm do Henrique.
