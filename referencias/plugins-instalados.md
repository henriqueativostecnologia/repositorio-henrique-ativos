# Plugins instalados nesta conta

Registro de cada pacote: o que faz, quando usar e quando evitar. Quem instala e liga ou desliga é uma pessoa, em Personalização → Plugins.

Lição da conta pessoal: num pedido genérico o Claude usa só as skills de formato (planilha, documento) e a análise fica rasa. **Chame as skills de método pelo nome** (ver `Skills a instalar - financas e gestao de projetos.md`).

## Finance (Anthropic), instalado em 29/10/2026

| Skill | Situação | Quando usar |
|---|---|---|
| `financial-statements` | ligada | DRE, balanço e fluxo de caixa, comparando períodos |
| `variance-analysis` | ligada | Orçado × realizado, explicando as diferenças |
| `reconciliation` | ligada | Conciliação (banco × controle) |
| `close-management` | ligada | Calendário e checklist do fechamento do mês |
| `journal-entry`, `journal-entry-prep` | desligadas | Só se a ATIVOS passar a fazer a contabilidade internamente |
| `sox-testing`, `audit-support` | desligadas | Regras de auditoria dos EUA; não se aplicam |

**Quando evitar:** regras fiscais e contábeis brasileiras. O método da skill serve, mas a parte fiscal vem do conhecimento do Henrique.

## Operations (Anthropic), instalado em 29/10/2026

| Skill | Quando usar |
|---|---|
| `status-report` | Status semanal dos projetos (`#status` no Slack) |
| `risk-assessment` | Riscos com probabilidade, impacto e resposta |
| `change-request` | Mudança de escopo pedida pelo cliente, com prazo, preço e aprovação |
| `capacity-plan` | "Cabe mais este projeto na equipe?" |
| `process-doc`, `runbook` | Documentar um processo ou uma tarefa que se repete |
| `process-optimization` | Achar gargalos num processo |
| `vendor-review` | Avaliar fornecedor (custo, risco, contrato) |
| `compliance-tracking` | Acompanhar obrigações (LGPD, prazos fiscais) |

**Quando evitar:** o pacote traz conectores de Asana e Atlassian, que a ATIVOS não usa e não serão conectados. Notion e Slack, que também vêm no pacote, são os da sistemática.

## Ainda não instalados

- **Small Business:** depois de 30/10/2026, só as skills úteis (ver a lista de skills a instalar).
