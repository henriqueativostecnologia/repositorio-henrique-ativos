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

### Passo 3: trocar a aba lida pelo app (o AppSheet pega a 1ª aba, "Como usar")
```
1. Data › + › em "Suggestions", clicar só em: Add Table "Tarefas" (não adicionar Henrique, Igor, Hugo, Bernardo nem Visão geral: são abas automáticas).
2. Na janela "Create a new table": conferir planilha TESTE e aba Tarefas; deixar marcados Updates e Adds e DESMARCAR Deletes (tarefa nunca se apaga; vira Cancelada). Add to app.
3. Data › Como usar › ⋮ › Delete (tira a tabela do app; a aba continua na planilha).
4. Views (ícone de celular) › Como usar › More › Delete (artigo "Delete a view"). SAVE.
```
**Resultado esperado:** Data mostra só "Tarefas"; o app abre a lista agrupada por status (ex.: "A fazer 41"). O AppSheet reconhece sozinho Código como chave (Key) e as colunas com lista como Enum.
**Se falhar:** erro "The data for this view Como usar cannot be found" = faltou apagar a view "Como usar" (item 4). O círculo vermelho no topo mostra a mensagem do erro; enquanto houver erro, o SAVE fica bloqueado.

### Passo 4: conferir as colunas (Data › Tarefas)
```
1. Tipos esperados: Código Text (Key ✓); Tarefa, Semana, Depende de Text; Responsável, Projeto, Entrega ou área, Prioridade, Status, Estimativa Enum; Prazo, Criada em, Concluída em Date; Link ou observação LongText; Tempo real (h) Decimal.
2. Status (lápis › Values): o AppSheet só traz os valores já usados nas tarefas. Deixar exatamente: Backlog, A fazer, Fazendo, Aguardando, Revisão, Feito, Cancelada (nesta ordem).
3. Entrega ou área: conferir as 11 opções da aba Listas (Site, Rankeamento, Tráfego, Automação, Dados, Comercial, Financeiro, Organização, Marca e conteúdo, Administrativo, Escopo).
4. Prazo (lápis): apagar Initial value TODAY() e desligar Require (regra: nunca inventar prazo).
5. SAVE.
```
**Resultado esperado:** sem erros (sinal verde no topo).
**Se falhar:** opção faltando numa lista = adicionar em Values, escrita igual à aba Listas.

### Passo 5: testar ida e volta (app ↔ planilha)
```
1. Antes: em Criada em e Concluída em, desligar Require (tarefas antigas não têm essas datas). Criada em mantém Initial value TODAY(); Concluída em fica sem Initial value.
2. No app: abrir uma tarefa › lápis › mudar o Status › Save. Conferir na planilha (o Claude confere pela planilha).
3. Na planilha: mudar o Status de volta. No app: botão de sincronizar (seta circular) › conferir.
```
**Resultado esperado:** a mudança aparece dos dois lados (testado em 10/11/2026 com a T-015: ida e volta OK).
**Se falhar:** "This entry is required" ao salvar = alguma coluna está com Require ligado sem precisar (desligar em Data › coluna › Data Validity › Require?).

### Passo 6: filtros (slices) das telas
```
Data › passe o mouse em Tarefas › + › Create a new slice › Slice Name › Row filter condition › "Create a new expression" (não usar as sugestões em linguagem comum) › colar › conferir o ✓ verde › Save. Nomes sem acento.
```
| Slice | Row filter condition |
|---|---|
| Atrasadas | `AND(ISNOTBLANK([Prazo]), [Prazo] < TODAY(), NOT(IN([Status], LIST("Feito", "Cancelada"))))` |
| Hoje | `OR(AND([Prazo] = TODAY(), NOT(IN([Status], LIST("Feito", "Cancelada")))), [Status] = "Fazendo")` |
| Amanha | `AND([Prazo] = WORKDAY(TODAY(), 1), NOT(IN([Status], LIST("Feito", "Cancelada"))))` |
| Ontem | `AND([Status] = "Feito", [Concluída em] = WORKDAY(TODAY(), -1))` |
| Esta semana | `AND([Semana (sprint)] = CONCATENATE(YEAR(TODAY()), "-S", RIGHT(CONCATENATE("0", ISOWEEKNUM(TODAY())), 2)), [Status] <> "Cancelada")` |
| Proxima semana | `AND([Semana (sprint)] = CONCATENATE(YEAR(TODAY() + 7), "-S", RIGHT(CONCATENATE("0", ISOWEEKNUM(TODAY() + 7)), 2)), [Status] <> "Cancelada")` |

**Resultado esperado:** Preview data mostra só as tarefas do filtro (teste em 10/11/2026: Atrasadas = T-085, T-097, T-113, T-126).
**Atenção:** na virada do ano, a semana ISO pode pertencer ao ano anterior ou seguinte (ex.: 01/01/2027 é a semana 53 de 2026); conferir o filtro de semana nessa época.

### Passo 7: telas (views)
```
Views (ícone de celular) › + ao lado de Primary navigation › Create a new view › View name, For this data (o slice), View type deck, Sort by Prazo Ascending, Group by Responsável › SAVE.
```

### Passo 8: cada sócio ver as próprias tarefas (User Settings)
```
1. Data › User Settings › Option 1 (lápis): Name Pessoa · Type Enum · Values Todos, Henrique, Igor, Hugo, Bernardo · Show? ligado · Initial value:
   SWITCH(USEREMAIL(), "<e-mail do Henrique>", "Henrique", "<e-mail do Igor>", "Igor", "<e-mail do Hugo>", "Hugo", "<e-mail do Bernardo>", "Bernardo", "Todos")
   (os e-mails institucionais estão no app; não guardamos e-mails aqui)
2. Em cada slice, acrescentar ao AND: OR(USERSETTINGS("Pessoa") = "Todos", [Responsável] = USERSETTINGS("Pessoa"))
3. Slice novo "Da pessoa": AND([Status] <> "Cancelada", OR(USERSETTINGS("Pessoa") = "Todos", [Responsável] = USERSETTINGS("Pessoa")))
4. Views "Por status" e "Calendário": For this data = Da pessoa. SAVE.
```
**Resultado esperado:** quem abre vê só as suas tarefas; menu ☰ › Settings › Pessoa = Todos mostra a equipe (testado em 10/11/2026: Atrasadas do Henrique = T-097; Todos = 4 tarefas; Por status sem o bloco Cancelada).

### Passo 9: tarefa nova pré-preenchida e código automático
```
Data › Columns › lápis da coluna › Auto Compute › Initial value:
- Código: CONCATENATE("T-", RIGHT(CONCATENATE("000", NUMBER(MID(INDEX(SORT(Tarefas[Código], TRUE), 1), 3, 4)) + 1), 3))
- Responsável: IF(USERSETTINGS("Pessoa") = "Todos", "", USERSETTINGS("Pessoa"))
- Status: "Backlog"
```
**Resultado esperado:** o + do app abre a tarefa com o próximo código (testado: T-232), o nome de quem cria e Backlog.
**Atenção:** a partir da T-999 o código passa a ter 4 dígitos; rever a fórmula nessa época.

### Passo 10: botões rápidos "Concluir" e "Começar"
```
Behavior › Actions › + New Action (uma por vez):

CONCLUIR
- Action name: Concluir
- For a record of this table: Tarefas
- Do this: Data: set the values of some columns in this row
- Set these columns: Status = "Feito"; Concluída em = TODAY()
- Position: Prominent (botão no topo da tarefa aberta)
- Display name: vazio · Action icon: check
- Behavior › Only if this condition is true: NOT(IN([Status], LIST("Feito", "Cancelada")))

COMEÇAR
- Action name: Começar
- For a record of this table: Tarefas
- Do this: Data: set the values of some columns in this row
- Set these columns: Status = "Fazendo"
- Position: Prominent · Display name: vazio · Action icon: play
- Behavior › Only if this condition is true: IN([Status], LIST("Backlog", "A fazer", "Aguardando"))

SAVE.
```
**Resultado esperado:** tarefa aberta mostra os botões só quando faz sentido (tarefa Cancelada ou Feita não mostra Concluir).
**Position:** Primary = botão flutuante; Prominent = topo da tarefa (o que usamos); Inline = ao lado de uma coluna; Hide = escondido.

### Passo 11: trocar a planilha de TESTE pela oficial
```
Data › Tables › cartão Tarefas › Storage › Source Path: escolher "Quadro de tarefas ATIVOS" (a oficial) · Worksheet Name/Qualifier: Tarefas · SAVE.
NÃO clicar em "Copy Data to New Source" (copia os dados para outro lugar).
```
**Resultado esperado:** Source Id muda para o endereço da planilha oficial (DocId=1g7cFgks…). Telas, filtros e botões continuam funcionando, porque a estrutura das duas planilhas é igual (feito em 10/11/2026).

### Passo 12: publicar (deploy)
```
Manage › Deploy › Deployment Check › Run deployment check › se estiver tudo OK: Move app to deployed state.
```
(artigos 10104495 Deploy: The Essentials e 10104389 Perform a deployment check)

### Passo 13: painel "Quadro" (colunas lado a lado)
```
1. Data › Slices: Col A fazer, Col Fazendo, Col Aguardando, Col Revisao
   AND([Status] = "<status>", OR(USERSETTINGS("Pessoa") = "Todos", [Responsável] = USERSETTINGS("Pessoa")))
2. UX › Views › New View (uma por coluna): A fazer, Fazendo, Aguardando, Revisão · For this data = slice da coluna · deck · Position ref · Sort Prazo · Group Responsável.
3. Tela "Por status" › Position menu (para caber o Quadro na barra de baixo).
4. New View: Quadro · dashboard · Position last · View entries: A fazer, Fazendo, Aguardando, Revisão, todas em Tall · Use tabs in mobile view ligado.
```
**Resultado esperado:** no computador, 4 colunas lado a lado; no celular, 4 abas no topo (artigo 10106384 Dashboard view type: tamanhos Large, Small, Tall, Wide; no celular o tamanho é ignorado).

### Passo 14: cores nos cartões (Format Rules)
```
UX › Format Rules › New Format Rule:
- Atrasada: For this data Tarefas · condição AND(ISNOTBLANK([Prazo]), [Prazo] < TODAY(), NOT(IN([Status], LIST("Feito", "Cancelada")))) · colunas Código e Tarefa · ícone exclamation (⚠) · texto vermelho
- Alta: For this data Tarefas · condição [Prioridade] = "Alta" · coluna Código · ícone flag · texto laranja · Bold
Highlight color: deixar sem cor (fundo colorido polui o quadro).
```

### Passo 14e: prazo à direita nos cartões
```
UX › Views › A fazer, Fazendo, Aguardando, Revisão › Summary column = Prazo
Calendário › Description = Tarefa (sem isso o calendário mostra só o código)
```

### Passo 14f: cor por pessoa no calendário
```
Data › Tarefas › Add Virtual Column:
- Nome: Cor · Type: Color
- App formula: SWITCH([Responsável], "Henrique", "Green", "Igor", "Blue", "Hugo", "Orange", "Bernardo", "Purple", "Black")
- Type Details › Values: Green, Blue, Orange, Purple, Black (obrigatório: sem a lista o app não roda)
UX › Views › Calendário › Category = Cor
```
**Resultado esperado:** Henrique verde, Igor azul, Hugo laranja, Bernardo roxo, sem responsável preto.

### Passo 15: marca da ATIVOS (Theme & Brand)
```
Settings › Theme & Brand (ou UX › Brand):
- Theme: Light
- Primary color: Custom #1F2329 (grafite da marca; alternativa: azul do brilho #2F6FDE)
- App logo: símbolo "A" quadrado, até 196 x 196 px e 500 KB
- Launch image: símbolo grande, mínimo 600 x 600 px
```
Fonte: artigo 10106612 (Style: The Essentials). O arquivo do logo não fica no repositório.

### Passos seguintes
A preencher durante a montagem: escolher só a aba Tarefas, tipos das colunas, telas (views), filtros por pessoa, ações de mudar status e sincronização imediata ("Delayed Sync" desligado, artigo 10108301).

## Verificação
- [ ] Uma tarefa alterada no app aparece na planilha em poucos segundos.
- [ ] Uma tarefa alterada na planilha aparece no app depois de sincronizar.
- [ ] Cada sócio vê as telas com as suas tarefas.

## Problemas comuns
| O que aparece | Causa provável | O que fazer |
|---|---|---|
| Error "app did not load" no celular simulado | Erro de configuração pendente | Clicar no círculo vermelho do topo, ler a mensagem e corrigir |
| App mostra o texto da aba "Como usar" | O AppSheet pegou a 1ª aba da planilha | Passo 3 |
| "version ... is not runnable" e erro "Column Type 'Color' must have a list of allowed values" | Coluna Cor sem a lista de cores | Passo 14f: preencher Values |
| Cores das pessoas trocadas no calendário | Fórmula da coluna Cor desatualizada | Colar de novo a fórmula do passo 14f |
| Lixeiras aparecendo nas tarefas | Deletes ficou marcado | Data › Tarefas › configurações da tabela: desmarcar Deletes |

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
