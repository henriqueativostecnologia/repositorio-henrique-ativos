---
tipo: código do app
app: Central ATIVOS (app feito pelo Claude, publicado como artefato no claude.ai)
atualizado: 13/11/2026
---

# Central ATIVOS: versões salvas do app

O app lê e grava na planilha oficial **Quadro de tarefas ATIVOS** pelos conectores Google Sheets e Google Calendar da conta de quem usa.
Link do app: https://claude.ai/artifact/3nioLxHECBdqzmUnnAHdD5

O código não guarda dados de clientes: as tarefas são lidas da planilha na hora em que o app abre.

## Versões

| Arquivo | Data | O que é |
|---|---|---|
| `central-ativos_v1_2026-11-13.html` | 13/11/2026 | **Versão aprovada pela equipe**, antes da otimização de design e funcionalidades. Abas Quadro, Agenda, Lista, Calendário (mês e dia com horários e reuniões), Projetos e Painel |

## Como voltar para uma versão salva

1. Peça ao Claude: "volte o app para a versão v1 de 13/11".
2. O Claude publica este arquivo no mesmo link do app, com as mesmas permissões (Google Sheets: `get_values`, `update_values`, `append_values`; Google Calendar: `list_calendars`, `list_events`).
3. O link continua o mesmo. Os dados não mudam, porque ficam na planilha.
