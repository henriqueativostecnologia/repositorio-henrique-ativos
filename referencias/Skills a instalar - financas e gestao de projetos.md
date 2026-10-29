---
tipo: referência
origem: cofre pessoal do Henrique (29/10/2026)
---

# Skills prontas a instalar: finanças e gestão de projetos

Skills da Anthropic que o Henrique já usa na conta pessoal e que servem ao financeiro e à gestão de projetos da ATIVOS. **Quem instala é uma pessoa**, em Personalização → Plugins → Descobrir (pelo catálogo oficial, que recebe as atualizações). Depois de instalar o pacote, desligar as marcadas ⏸️.

## Finanças
| Skill | Pacote | O que faz | Instalar? |
|---|---|---|---|
| `financial-statements` | Finance | Monta DRE, balanço e fluxo de caixa, comparando períodos | ✅ |
| `variance-analysis` | Finance | Orçado × realizado, explicando as diferenças | ✅ |
| `reconciliation` | Finance | Conciliação (banco × controle) | ✅ |
| `close-management` | Finance | Calendário e checklist do fechamento do mês | ✅ |
| `journal-entry` | Finance | Lançamentos contábeis com débito e crédito | ⏸️ Só se a ATIVOS fizer a contabilidade internamente |
| `journal-entry-prep` | Finance | Prepara os lançamentos do fim do mês | ⏸️ Idem |
| `cash-flow-snapshot` | Small Business | Previsão de caixa de 30, 60 e 90 dias (aceita planilha) | ✅ Depois de 30/10 |
| `invoice-chase` | Small Business | Cobrança de clientes atrasados | ✅ Depois de 30/10 |
| `business-pulse` | Small Business | Resumo de uma página do negócio | ⏸️ Depende de sistemas conectados |
| `ap-processor` | Small Business | Contas a pagar | ⏸️ Feita para sistemas americanos |

## Gestão de projetos (pacote Operations)
| Skill | O que faz | Instalar? |
|---|---|---|
| `status-report` | Status do projeto (o resumo semanal) | ✅ |
| `risk-assessment` | Riscos com probabilidade, impacto e o que fazer | ✅ |
| `change-request` | Mudança de escopo, com impacto e aprovação | ✅ |
| `capacity-plan` | "Cabe mais este projeto na equipe?" | ✅ |
| `process-doc` | Documenta um processo | ✅ |
| `process-optimization` | Acha gargalos num processo | ✅ |
| `runbook` | Passo a passo de uma tarefa que se repete | ✅ |
| `vendor-review` | Avaliar fornecedor (custo, risco, contrato) | ✅ |
| `compliance-tracking` | Acompanhar obrigações (ex.: LGPD) | ✅ |

**Small Business:** instalar só depois da revisão desse pacote na conta pessoal (30/10/2026). As skills dele dependem de uma pasta `shared/` que vem dentro do pacote.

Ao instalar, registre cada pacote numa nota deste repositório (o que faz, quando usar, quando evitar), como o Henrique faz no cofre pessoal.

## Skills de formato (já vêm com o Claude; só conferir se estão ativas)
| Skill | O que faz | Por que importa aqui |
|---|---|---|
| `xlsx` | Cria e confere planilhas, com fórmulas | Base do financeiro (DRE, caixa, conciliação) e das planilhas de projeto |
| `dataviz` | Gráficos consistentes | Relatórios financeiros e de clientes |
| `docx` e `pdf` | Documentos Word e PDF | Escopo de projeto, relatórios e propostas para o cliente |

**Lição da conta pessoal (07/10):** num pedido genérico ("analisa a situação financeira"), o Claude usou só as skills de formato e deu uma conclusão rasa. Chamando `financial-statements` e `variance-analysis` pelo nome, a conclusão mudou. Até existir um roteador nesta conta, **chame as skills de método pelo nome**.

## Também úteis para a gestão de clientes (Small Business, depois de 30/10)
| Skill | O que faz |
|---|---|
| `proposal-builder` | Monta proposta comercial a partir das anotações da conversa com o cliente |
| `contract-review` | Revisa contratos e aponta riscos, em linguagem simples |

## Skills de fora, para avaliar ao criar a pmo-ativos (não instaladas)
Encontradas em 07/10 no GitHub. Avaliar com o checklist de skills de fora antes de instalar.
| Skill | Origem | O que é | Atenção |
|---|---|---|---|
| **claude-project-manager** | `KirKruglov/claude-project-manager` (MIT, grátis) | 21 skills no padrão PMBOK 8 + ágil: TAP, EAP com Gantt, riscos, comunicação, orçamento, plano × realizado, lições aprendidas | Pouco testada (uma versão, abril/2026); pode enviar e-mails sozinha; inglês e russo |
| **planning** | `jkitchin/skillz` | Uma skill com modelos de TAP, EAP, RACI, Gantt e riscos | Boa referência de modelos |
