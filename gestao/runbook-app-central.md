---
tipo: runbook (passo a passo técnico)
atualizado: 10/11/2026
situacao: rascunho, sendo escrito durante a primeira montagem (teste)
---

# Runbook: montar o app "Central de tarefas ATIVOS" no AppSheet

**Dono:** Henrique · **Frequência:** quando for montar ou remontar o app (teste, troca para a planilha oficial, novo app) · **Última execução:** 10/11/2026 (teste, em andamento)

## Para que serve

Criar o app de tarefas do dia a dia (telas Atrasadas, Hoje, Amanhã, Ontem, Esta semana, Próxima semana, Calendário e Por status) em cima da planilha Quadro de tarefas ATIVOS, sem mudar a planilha. Fonte oficial de cada passo: `plataformas/appsheet/oficial/` (número do artigo indicado em cada passo).

## Pré-requisitos

- [ ] Conta Google Workspace da ATIVOS (Business Standard inclui o AppSheet Core).
- [ ] Planilha com a aba **Tarefas** "limpa": cabeçalho na 1ª linha, sem o formato "Tabela", sem gráficos ou botões por cima (artigo 10099416, Make an AppSheet-friendly spreadsheet).
- [ ] No teste: usar a cópia **TESTE - Quadro de tarefas ATIVOS (app AppSheet)**, na pasta 00 Geral › 03 Gestão de tarefas. Só depois de aprovado, trocar para a planilha oficial.

## Procedimento

### Passo 1: preparar a cópia de teste
```
Drive › 00 Geral › 03 Gestão de tarefas › cópia da planilha com o nome "TESTE - Quadro de tarefas ATIVOS (app AppSheet)"
```
**Resultado esperado:** cópia criada (feita pelo Claude em 10/11/2026).
**Se falhar:** Arquivo › Fazer uma cópia, na mesma pasta.

### Passo 2: criar o app a partir da planilha (artigo 11980957, Create apps: The Essentials)
```
1. Entrar em https://www.appsheet.com com a conta da ATIVOS.
2. My apps › Create › App › Start with existing data.
3. App name: Central de tarefas ATIVOS (categoria: deixar como está).
4. Choose your data › Google Sheets › escolher a planilha TESTE.
```
**Resultado esperado:** o AppSheet monta um app automático e abre o editor.
**Se falhar:** se aparecer aviso de que o administrador precisa liberar o AppSheet ou o Google Drive para o domínio, liberar no Admin do Google Workspace (o artigo 11980957 avisa que o Drive precisa estar habilitado para o domínio).

### Passos seguintes
A preencher durante a montagem: escolher só a aba Tarefas, tipos das colunas, telas (views), filtros por pessoa, ações de mudar status e sincronização imediata ("Delayed Sync" desligado, artigo 10108301).

## Verificação
- [ ] Uma tarefa alterada no app aparece na planilha em poucos segundos.
- [ ] Uma tarefa alterada na planilha aparece no app depois de sincronizar.
- [ ] Cada sócio vê as telas com as suas tarefas.

## Problemas comuns
| O que aparece | Causa provável | O que fazer |
|---|---|---|
| A preencher durante o teste | | |

## Como desfazer
O app não altera a estrutura da planilha. Para desfazer: apagar o app em My apps. No teste, a planilha oficial nunca é tocada.

## A quem recorrer
| Situação | Quem | Como |
|---|---|---|
| Bloqueio de permissão do domínio | Administrador do Google Workspace da ATIVOS | Painel Admin |
| Dúvida de configuração | Claude do Henrique | Chat, com print da tela |

## Histórico
| Data | Quem | Observação |
|---|---|---|
| 10/11/2026 | Henrique (com o Claude) | Primeira montagem, em teste |
