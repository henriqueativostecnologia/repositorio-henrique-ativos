---
tipo: instrução para o Claude (de qualquer sócio)
atualizado: 05/11/2026
situacao: versão 1; copiada em 05/11/2026 para a aba "Como usar" da planilha (seção "Instruções para o Claude")
---

# Instruções para o Claude: cadastrar e atualizar tarefas no Quadro de tarefas ATIVOS

Estas instruções valem para o Claude de **qualquer sócio** da ATIVOS (Henrique, Igor, Hugo, Bernardo). Elas ficam também na aba **Como usar** da planilha, para que qualquer Claude que abra a planilha siga o mesmo padrão.

**Planilha:** Quadro de tarefas ATIVOS · Drive compartilhado ATIVOS › 00 Geral › 03 Gestão de tarefas
**Link:** https://docs.google.com/spreadsheets/d/1g7cFgksYnu7_YpPCewVUtGThya8i46XQOdmxkVNVbl4/edit
**Precisa de:** conector Google Sheets ligado na conta Claude do sócio.

## Quem edita o quê (atualizado em 09/11/2026)

A planilha é o **esboço da central de tarefas** (até o Notion). Para ser prático para todos:

* **Cada sócio cadastra e atualiza as suas tarefas livremente**, do jeito mais prático (texto livre, sem se preocupar com o padrão). As listas de seleção só sugerem valores; não bloqueiam.
* **O Claude do Henrique padroniza depois**, quando o Henrique pedir, **sem alterar o conteúdo**.
* Tarefas também podem chegar pelo WhatsApp ao Henrique, que repassa ao Claude.

### Como padronizar (Claude do Henrique)

1. Leia a aba Tarefas inteira e encontre as linhas fora do padrão (sem código, valores fora das listas, data em texto, tarefa sem verbo, linha de outro formato).
2. Para cada uma, proponha a versão padronizada **mantendo o significado**:
   * código: próximo T-XXX livre;
   * tarefa: reescrita começando com verbo, com o mesmo conteúdo;
   * valores equivalentes das listas (ex.: "urgente" → Alta, "feito" → Feito, "Lucas" → CLI-002-PAC Lucas Melo, "Hugo e Bernardo" → duas tarefas, uma para cada);
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

**Proteções (só aviso, não bloqueiam):** colunas auxiliares O a R da aba Tarefas, abas automáticas (pessoas e Visão geral), Projetos e Listas. As colunas A a N da aba Tarefas são livres.

## Como o sócio pede

Basta colar no chat do Claude:

> Leia a aba "Como usar" da planilha Quadro de tarefas ATIVOS (link acima) e siga as "Instruções para o Claude". Quero atualizar estas tarefas: … (no Claude do Henrique, também cadastrar)

## O que o Claude deve fazer

1. **Ler antes de escrever.** Leia as abas Como usar, Listas e Projetos, e a coluna A da aba Tarefas.
2. **Escrever só na aba Tarefas, colunas A a N.** Nunca altere as colunas O a R (auxiliares), as abas com nome de pessoa, a Visão geral, a Projetos nem a Listas.
3. **Nunca apagar linhas nem mudar o código de uma tarefa existente.** Tarefa cancelada: Status = Feito e "Cancelada: motivo" em Link ou observação.
4. **Código:** o próximo número livre depois do maior código da coluna A (ex.: se o maior é T-066, a próxima é T-067). Nunca reaproveitar.
5. **Linha:** a primeira linha vazia da aba Tarefas (coluna B vazia).
6. **Preencher cada coluna assim:**

| Coluna | Regra |
|---|---|
| A Código | T-XXX, conforme o item 4 |
| B Tarefa | Começa com verbo no infinitivo e diz o resultado. Ex.: "Criar wireframe da home do site" |
| C Responsável | Exatamente um valor da lista: Henrique, Igor, Hugo ou Bernardo |
| D Projeto | Exatamente um valor da aba Projetos (cliente com código e nome, ex.: CLI-002-PAC Lucas Melo). Sem projeto: INT-000 |
| E Entrega ou área | Exatamente um valor da coluna "Entrega ou área" da aba Listas |
| F Prioridade | Alta (trava cliente ou outras tarefas), Média ou Baixa |
| G Status | Backlog, A fazer, Fazendo, Aguardando, Revisão ou Feito. Tarefa nova: A fazer (se for para esta semana) ou Backlog |
| H Prazo | Data DD/MM/AAAA, se houver. Não invente prazo |
| I Estimativa | P (até 2h), M (até 4h) ou G (até 1 dia), exatamente como na lista |
| J Semana (sprint) | AAAA-SNN (semana do ano, ex.: 2026-S45) quando entrar na semana; senão, vazio |
| K Depende de | Códigos de outras tarefas, separados por vírgula |
| L Link ou observação | Link do Drive ou observação curta. Status Aguardando: diga de quem |
| M Criada em | Data de hoje (DD/MM/AAAA) |
| N Concluída em | Só quando Status = Feito |

7. **Tamanho:** cada tarefa cabe em até 1 dia. Se o pedido for maior, proponha dividir em tarefas menores antes de cadastrar.
8. **Faltou informação obrigatória** (Responsável, Projeto, Prioridade)? Pergunte ao sócio. Não adivinhe.
9. **Valor que não existe nas listas** (pessoa, projeto ou área nova)? Não crie. Avise o sócio: listas e projetos só mudam com o Henrique ou o Igor.
10. **Antes de gravar**, mostre ao sócio uma tabela com as linhas que vai incluir ou alterar e espere o "ok".
11. **Depois de gravar**, releia a planilha e confirme: códigos criados e linhas preenchidas.

## Atualizar uma tarefa existente

* Mudar status, prazo, estimativa, semana ou observação: altere só a célula pedida, na linha do código informado.
* Concluir: Status = Feito e Concluída em = data de hoje.
* Mudar o responsável: só com o pedido do próprio responsável ou do Henrique/Igor; registre em observação "Repassada de X para Y em DD/MM".
