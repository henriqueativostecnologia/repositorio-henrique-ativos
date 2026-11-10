---
tipo: modelo de gestão
atualizado: 10/11/2026
situacao: versão inicial aprovada; será ajustada com a experiência dos 3 primeiros clientes e as lições aprendidas
---

# Modelo de projetos e de tarefas da ATIVOS

**Tudo aqui é ponto de partida.** Prazos, estimativas, tamanhos de tarefa e rituais serão revistos com o que aprendermos nos primeiros projetos. Cada ajuste entra neste arquivo, com a data.

## Modelo geral: híbrido

* **Macro (projeto):** fases e portões, para controlar o começo e o fim de cada projeto.
* **Micro (dia a dia):** sprints de 1 semana, que se replanejam toda segunda.

```
PORTFÓLIO (todos os projetos)
 └─ PROJETO       CLI-001-PAC · INT-001…            fases e portões
     └─ ENTREGA   Site · Rankeamento · Tráfego…      EAP padrão do serviço
         └─ TAREFA   T-024 "Criar wireframe da home" cabe em 1 dia
             └─ checklist dentro da tarefa
```

**Ciclo do projeto:** Iniciação → **G0** → Planejamento → Execução em sprints → **Aceite** → Operação ou Encerramento.

## Decisões iniciais (05/11/2026)

| # | Tema | Decisão |
|---|---|---|
| 1 | Modelo | Híbrido: fases e portões no macro, sprints no micro |
| 2 | Sprint | 1 semana, de segunda a sexta. Código da semana: `2026-S45` |
| 3 | Rituais | Planejamento na segunda (30 min) · atualização diária por escrito no Google Chat · revisão e retrospectiva na sexta (30 min) |
| 4 | Status | Backlog · A fazer · Fazendo · Aguardando (cliente ou terceiro) · Revisão · Feito · Cancelada (não será feita ou foi substituída; incluída em 10/11/2026) |
| 5 | Limite | No máximo 3 tarefas em "Fazendo" por pessoa |
| 6 | Tamanho | Uma tarefa cabe em até 1 dia; se for maior, divide |
| 7 | Estimativa | P (até 2h) · M (até 4h) · G (até 1 dia) |
| 8 | Portões | **G0:** contrato, acessos e briefing completos · **Aceite:** cliente aprova por escrito. A Infraestrutura de Dados mantém os seus 7 portões |
| 9 | Códigos | Projeto de cliente `CLI-001-SIGLA Nome` (ex.: `CLI-002-PAC Lucas Melo`) (PAC pacote, POS posicionamento, TRA tráfego, AUT automação, DAD dados) · interno `INT-00X` · tarefa `T-XXX`, nunca reaproveitado |

## Projetos internos fixos

| Código | Projeto |
|---|---|
| INT-000 | Rotina e administrativo (o que não pertence a nenhum projeto) |
| INT-001 | Estruturação da ATIVOS (organização, Drive, processos, ferramentas, gestão) |
| INT-002 | Posicionamento digital da ATIVOS (marca, design system, Instagram, landing page) |

## Onde ficam as tarefas

* **Agora:** planilha **Quadro de tarefas ATIVOS**, no Drive em `00 Geral › 03 Gestão de tarefas` (https://docs.google.com/spreadsheets/d/1g7cFgksYnu7_YpPCewVUtGThya8i46XQOdmxkVNVbl4/edit). Abas: Como usar · Tarefas (lista única, a única que se edita) · uma aba por sócio (automática) · Visão geral (automática) · Projetos · Listas.
* **Decisão de 10/11/2026:** a planilha passa a ser a central oficial (ferramentas só Google: Sheets, Chat e Drive). Próximos passos visuais: Linha do tempo (Inserir › Linha do tempo), depois Looker Studio e AppSheet se fizer falta. Notion fica como opção futura.

## Visões

| Visão | Para quem | Onde, na planilha |
|---|---|---|
| Minhas tarefas | Cada sócio | Aba com o nome da pessoa |
| Visão macro (pessoa × status, atrasadas, alta prioridade, por projeto) | Henrique e Igor | Visão geral |
| Aguardando cliente | Henrique e comercial | Filtro Status = Aguardando na aba Tarefas |
| Atrasadas | Todos | Linhas vermelhas na aba Tarefas |

## Skills que entram no modelo

| Momento | Skill |
|---|---|
| G0 (início do projeto) | risk-assessment |
| Planejamento de segunda | capacity-plan |
| Pedido fora do escopo | change-request |
| Revisão de sexta | status-report |
| Atualização diária | mensagem no Google Chat (a skill standup é do Slack; não serve por enquanto) |

## A medir para ajustar o modelo

* Tempo real de cada tipo de tarefa contra a estimativa (coluna O "Tempo real (h)" da planilha; base para os prazos padrão de cada serviço).
* Tarefas que ficaram em "Aguardando" e por quanto tempo (atraso causado pelo cliente).
* Lições aprendidas de cada projeto, registradas no encerramento.
