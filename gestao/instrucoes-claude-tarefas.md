---
tipo: instrução para o Claude (de qualquer sócio)
atualizado: 25/11/2026
situacao: versão 3 (regras de quem alimenta a central, decididas em 24/11 e testadas em 25/11). A aba "Como usar" da planilha ainda tem a versão 2.1; atualizar depois deste PR
---

# Instruções para o Claude: cadastrar e atualizar tarefas no Quadro de tarefas ATIVOS

Estas instruções valem para o Claude de **qualquer sócio** da ATIVOS (Henrique, Igor, Hugo, Bernardo). Elas ficam também na aba **Como usar** da planilha, para que qualquer Claude que abra a planilha siga o mesmo padrão.

**Planilha:** Quadro de tarefas ATIVOS · Drive compartilhado ATIVOS › 00 Geral › 03 Gestão de tarefas
**Link:** https://docs.google.com/spreadsheets/d/1g7cFgksYnu7_YpPCewVUtGThya8i46XQOdmxkVNVbl4/edit
**Precisa de:** conector Google Sheets ligado na conta Claude do sócio.

## Quem alimenta a central (decisão de 24/11/2026, testada em 25/11/2026)

A central é a **planilha Quadro de tarefas ATIVOS** junto com o **app "Central ATIVOS"** (artefato do Claude: https://claude.ai/artifact/3nioLxHECBdqzmUnnAHdD5; código salvo em `apps/central-ativos/`). O app lê e grava na planilha. **Não** é o AppSheet: o AppSheet foi testado (`gestao/runbook-app-central.md`) e não é o caminho em uso. A ferramenta definitiva ainda não está decidida; no futuro, a ideia é um software próprio.

| Quem | Como alimenta | O quê |
|---|---|---|
| **Sócios (Igor, Hugo, Bernardo e o Henrique no dia a dia)** | **Pelo app** (caminho principal) | Atualizar o status das próprias tarefas e criar tarefas avulsas (uma por vez) |
| **Henrique, com o Claude dele** | Direto na planilha, seguindo estas instruções | Criar os **pacotes de tarefas** de cada cliente a partir das receitas (`servicos/README.md`), depois da **entrevista de onboarding** com o sócio que vendeu; padronizar linhas fora do padrão |
| **Claude dos outros sócios** (opção B, escolhida em 25/11/2026) | Direto na planilha, **só dentro do projeto "Central ATIVOS"** configurado com `gestao/instrucoes-claude-socios.md` | Só as tarefas do próprio sócio: atualizar status e criar tarefas avulsas. **Não** cria pacotes de cliente, não mexe em tarefa de outro sócio |
| **WhatsApp para o Henrique** | Só como exceção (ex.: sócio sem acesso ao app no momento) | O Henrique repassa ao Claude dele |

**Hábitos:** cada um atualiza as suas tarefas **no fim do dia**; revisão semanal da central na **segunda-feira**.

**Onboarding:** fica dentro do projeto de cada cliente (ex.: CLI-004-PAC Guto Bebidas), com a coluna E "Entrega ou área" = **Onboarding**. Não existe projeto separado de onboarding.

**Para o app funcionar para cada sócio:** conta Claude com o conector Google Sheets ligado e o app compartilhado com ele (o app está compartilhado com a organização ATIVOS no claude.ai). Testado pelo Henrique em 25/11; falta testar com um dos outros sócios.

**Excluir no app** não apaga a linha: marca Cancelada, anota "Excluída no app em DD/MM/AAAA (status anterior: X)" na observação e preenche Concluída em. Recuperar: Lista › Canceladas › abrir a tarefa › Restaurar tarefa.

Linhas fora do padrão (texto livre, valores fora das listas) continuam sendo padronizadas pelo Claude do Henrique, como abaixo.

### Como padronizar (Claude do Henrique)

1. Leia a aba Tarefas inteira e encontre as linhas fora do padrão (sem código, valores fora das listas, data em texto, tarefa sem verbo, linha de outro formato).
2. Para cada uma, proponha a versão padronizada **mantendo o significado**:
   * código: próximo T-XXX livre;
   * tarefa: reescrita começando com verbo, com o mesmo conteúdo;
   * valores equivalentes das listas (ex.: "urgente" → Alta, "feito" → Feito, "cancelar" → Cancelada, "Lucas" → CLI-002-PAC Lucas Melo, "Hugo e Bernardo" → duas tarefas, uma para cada);
   * datas no formato da planilha.
3. **Nunca apague informação:** o que não couber nas colunas vai para Link ou observação.
4. Na dúvida sobre o significado, **pergunte** ao Henrique.
5. Mostre ao Henrique uma tabela **antes → depois** e só grave com o "ok". Depois de gravar, releia e confirme.

**Modelo para o WhatsApp** (opcional):

```
Tarefa: (o que fazer)
Cliente ou projeto: (ex.: CLI-002 Lucas Melo, ou "interno")
Prioridade: Alta / Média / Baixa
Prazo: (se tiver)
```

**Proteções (só aviso, não bloqueiam):** abas automáticas (pessoas e Visão geral), Projetos e Listas. Todas as colunas da aba Tarefas (A a O) são livres.

**Capacidade e visual (10/11/2026):** aba Tarefas com 2.000 linhas, **sem** o formato "Tabela" do Google (ele bloqueia o texto livre e atrapalha os apps, que precisam do cabeçalho na 1ª linha e de nada por cima dos dados), Status e Prioridade em etiquetas coloridas e Visão geral com 2 gráficos. **Filtrar:** (1) aba de consulta de cada sócio (campos amarelos da linha 3: Responsável, Status, Projeto, Prazo até, Busca) ou (2) o modo de filtro geral de cada sócio na aba Tarefas (links na aba Como usar). Nunca use o funil sem estar num modo de filtro: ele muda a visão de todos.

## Como o sócio pede

Os sócios usam o **app** (acima). No Claude do Henrique, basta colar:

> Leia a aba "Como usar" da planilha Quadro de tarefas ATIVOS (link acima) e siga as "Instruções para o Claude". Quero cadastrar ou atualizar estas tarefas: …

## O que o Claude deve fazer

1. **Ler antes de escrever.** Leia as abas Como usar, Listas e Projetos, e a coluna A da aba Tarefas.
2. **Escrever só na aba Tarefas, colunas A a O.** Nunca altere as abas com nome de pessoa, a Visão geral, a Projetos nem a Listas.
3. **Nunca apagar linhas nem mudar o código de uma tarefa existente.** Tarefa cancelada ou substituída (decisão de 10/11/2026): Status = **Cancelada**, "Cancelada: motivo" ou "Substituída por T-XXX" em Link ou observação e a data em Concluída em. Cancelada aparece cinza e riscada e não conta como aberta nem como feita.
4. **Código:** o próximo número livre depois do maior código da coluna A (ex.: se o maior é T-066, a próxima é T-067). Nunca reaproveitar.
5. **Linha:** a primeira linha vazia **depois da última tarefa** da aba Tarefas. Grave com `update_values` na linha exata (ex.: `Tarefas!A340:P340`), nunca com o "acrescentar" (`append_values`): em 25/11 ele inseriu uma tarefa no meio da lista e empurrou as outras uma linha para baixo. Hoje a tarefa T-N fica na linha N+1.
6. **Preencher cada coluna assim:**

| Coluna | Regra |
|---|---|
| A Código | T-XXX, conforme o item 4 |
| B Tarefa | Começa com verbo no infinitivo e diz o resultado. Ex.: "Criar wireframe da home do site" |
| C Responsável | Exatamente um valor da lista: Henrique, Igor, Hugo ou Bernardo |
| D Projeto | Exatamente um valor da aba Projetos (cliente: CLI-002-PAC Lucas Melo; campanha: Campanha · Comércio local; setor: ATIVOS · Gestão, Comercial, Processos, Operacional, Financeiro, Administrativo, Marketing ou Treinamentos; tabela em `gestao/modelo-de-projetos.md`). Demanda avulsa sem setor claro: ATIVOS · Administrativo |
| E Entrega ou área | Exatamente um valor da coluna "Entrega ou área" da aba Listas |
| F Prioridade | Alta (trava cliente ou outras tarefas), Média ou Baixa |
| G Status | Backlog, A fazer, Fazendo, Aguardando, Revisão, Feito ou Cancelada. Tarefa nova: A fazer (se for para esta semana) ou Backlog |
| H Prazo | Data DD/MM/AAAA, se houver. Não invente prazo |
| I Estimativa | P (até 2h), M (até 4h) ou G (até 1 dia), exatamente como na lista |
| J Semana (sprint) | AAAA-SNN (semana do ano, ex.: 2026-S45) quando entrar na semana; senão, vazio |
| K Depende de | Códigos de outras tarefas, separados por vírgula |
| L Link ou observação | Link do Drive ou observação curta. Status Aguardando: diga de quem |
| M Criada em | Data de hoje (DD/MM/AAAA) |
| N Concluída em | Só quando Status = Feito ou Cancelada |
| O Tempo real (h) | Horas gastas de verdade, ao concluir (ex.: 1,5). Só com a informação do sócio; não invente |

7. **Tamanho:** cada tarefa cabe em até 1 dia. Se o pedido for maior, proponha dividir em tarefas menores antes de cadastrar.
8. **Faltou informação obrigatória** (Responsável, Projeto, Prioridade)? Pergunte ao sócio. Não adivinhe.
9. **Valor que não existe nas listas** (pessoa, projeto ou área nova)? Não crie. Avise o sócio: listas e projetos só mudam com o Henrique ou o Igor.
10. **Antes de gravar**, mostre ao sócio uma tabela com as linhas que vai incluir ou alterar e espere o "ok".
11. **Depois de gravar**, releia a planilha e confirme: códigos criados e linhas preenchidas.

## Atualizar uma tarefa existente

* Mudar status, prazo, estimativa, semana ou observação: altere só a célula pedida, na linha do código informado.
* Concluir: Status = Feito, Concluída em = data de hoje e, se o sócio informar, Tempo real (h).
* Mudar o responsável: só com o pedido do próprio responsável ou do Henrique/Igor; registre em observação "Repassada de X para Y em DD/MM".
