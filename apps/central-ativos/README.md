---
tipo: código do app
app: Central ATIVOS (app feito pelo Claude, publicado como artefato no claude.ai)
atualizado: 25/11/2026
---

# Central ATIVOS: versões salvas do app

O app lê e grava na planilha oficial **Quadro de tarefas ATIVOS** pelos conectores Google Sheets e Google Calendar da conta de quem usa.
Link do app: https://claude.ai/artifact/3nioLxHECBdqzmUnnAHdD5

O código não guarda dados de clientes: as tarefas são lidas da planilha na hora em que o app abre.

## Versões

| Arquivo | Data | O que é |
|---|---|---|
| `central-ativos_v1_2026-11-13.html` | 13/11/2026 | **Versão aprovada pela equipe**, antes da otimização de design e funcionalidades. Abas Quadro, Agenda, Lista, Calendário (mês e dia com horários e reuniões), Projetos e Painel |
| `central-ativos_v2_2026-11-25.html` | 25/11/2026 | **Versão testada pelo Henrique em 25/11** (substituída pela v3). Inclui o design otimizado de 13/11 e: (1) na Lista, "Ordenar por Prazo ou Código"; (2) Excluir marca a tarefa como Cancelada e anota na observação a data e o status anterior, preenchendo "Concluída em"; (3) "Desfazer" logo após excluir e "Restaurar tarefa" em Lista › Canceladas; (4) tarefa nova gravada sempre na primeira linha vazia depois da última, com conferência antes e depois (o "acrescentar" do Google inseriu a T-338 no meio da lista em 25/11; corrigido) |
| `central-ativos_v3_2026-11-26.html` | 26/11/2026 | Igual à v2 mais o status **Pausada**: não conta como aberta (some do Quadro, da Agenda, dos atrasos e do Painel) e tem o filtro "Pausadas" na Lista. Primeiro uso: as 42 tarefas do CLI-002 Lucas Melo |
| `central-ativos_v4_2026-11-26.html` | 26/11/2026 | **Versão no ar.** v3 mais: campo **Descrição** (coluna Q) no formulário; **prazo original e remarcações** (colunas R, S e T): o cartão mostra "↻ +N d" quando o prazo escorregou, o formulário mostra "Prazo original · +N dias · remarcada N vezes", e o app percebe prazo mudado direto na planilha e soma a remarcação; tarefa nova grava na primeira linha vazia (A:T) |

## Como voltar para uma versão salva

1. Peça ao Claude: "volte o app para a versão v1 de 13/11" (ou v2 de 25/11).
2. O Claude publica este arquivo no mesmo link do app, com as mesmas permissões (Google Sheets: `get_values`, `update_values`, `append_values` (a v2 não usa mais o `append_values`, mas a permissão continua declarada); Google Calendar: `list_calendars`, `list_events`).
3. O link continua o mesmo. Os dados não mudam, porque ficam na planilha.
