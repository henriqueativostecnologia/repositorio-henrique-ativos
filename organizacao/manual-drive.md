---
tipo: manual (procedimento padrão)
atualizado: 04/11/2026
situacao: versão 1, aguardando aprovação; depois de aprovado, uma cópia vai para o Drive em "00 Geral / 01 Manual de uso"
---

# Manual de uso do Drive ATIVOS

**Dono:** Henrique · **Atualizado:** 04/11/2026 · **Revisão:** a cada 3 meses, ou quando surgir uma área nova

## Objetivo

Fazer com que qualquer sócio saiba, sem perguntar, **onde achar** e **onde salvar** cada arquivo da ATIVOS, e que os arquivos continuem sendo da empresa mesmo que alguém saia.

## Escopo

* **Vale para:** o Drive compartilhado "ATIVOS" e todos os seus membros.
* **Não vale para:** o Drive compartilhado "Conteúdos - Ativos Tecnologia" (produção de conteúdo; tem atalho na pasta 70), o "Meu Drive" pessoal de cada um e as senhas (item 6).

## 1. Por que as pastas têm números

As pastas principais vão de **00 a 90, de dez em dez**. Cada dezena é uma **área**, e os números de dentro são as **subpastas** dessa área.

```
50 Financeiro
   51 Contas a receber e notas emitidas
   52 Contas a pagar
   53 Extratos e conciliação
```

Isso traz três vantagens:

1. **O número é o endereço.** "Está na 52" quer dizer: área 5 (Financeiro), subpasta 2 (Contas a pagar). Serve para falar no Slack, anotar no Notion ou pedir ao Claude ("salve na 12").
2. **Sobra espaço para crescer.** Uma subpasta nova do Comercial vira a 15, e nenhuma outra muda de número.
3. **A ordem é sempre a mesma.** Sem números, o Drive ordenaria por ordem alfabética e embaralharia as áreas.

O **00** fica no topo porque guarda o que vale para o Drive inteiro: este manual e o contexto para o Claude.

**Limite proposital:** no máximo 10 áreas, e no máximo 9 subpastas em cada uma. Se uma área precisar de mais, ela deve virar duas. Isso mantém tudo simples.

## 2. O mapa

| Pasta | O que guarda |
|---|---|
| **00 Geral** | 01 Manual de uso (este documento) · 02 Contexto para o Claude (documentos que explicam a ATIVOS, os serviços e as ferramentas, como o que é o MDP) |
| **10 Comercial** | 11 Prospecção · 12 Propostas enviadas · 13 Modelos de proposta e contrato · 14 Material de venda por nicho |
| **20 Clientes** | Uma pasta por cliente, com código fixo (item 4) · CLI-000 Modelo, para copiar |
| **30 Projetos internos** | Projetos da própria ATIVOS: marca, Instagram, landing page |
| **40 Processos** | 41 Catálogo de serviços · 42 Fluxos dos serviços · 43 POPs · 44 Instruções de trabalho · 45 Checklists e modelos · 49 Sugestões e rascunhos |
| **50 Financeiro** | 51 Contas a receber e notas emitidas · 52 Contas a pagar · 53 Extratos e conciliação · 54 Fechamentos e relatórios · 55 Impostos e contabilidade |
| **60 Administrativo e societário** | Contrato social, documentos da empresa, ferramentas e assinaturas |
| **70 Marca e marketing da ATIVOS** | Identidade visual e materiais da ATIVOS, com atalho para o Drive "Conteúdos" |
| **80 Treinamentos** | Cursos comprados e materiais de estudo |
| **90 Arquivo** | Clientes encerrados e projetos concluídos |

## 3. Onde salvar: guia rápido

| Tenho em mãos… | Salvo em |
|---|---|
| Uma proposta que vou enviar | 12 |
| Um contrato assinado com cliente | Pasta do cliente › 01 Contrato e cadastro |
| Fotos, logo ou briefing que o cliente mandou | Pasta do cliente › 02 Briefing e materiais do cliente |
| Um entregável (site, criativo, relatório de configuração) | Pasta do cliente › 03 Entregas › bloco correspondente |
| Relatório mensal para o cliente | Pasta do cliente › 04 Relatórios |
| Ata de reunião com cliente | Pasta do cliente › 05 Reuniões e atas |
| Nota fiscal emitida | 51 |
| Boleto ou conta a pagar | 52 |
| Extrato bancário | 53 |
| Documento que explica algo da ATIVOS para o Claude | 00 Geral › 02 Contexto para o Claude |
| Curso ou apostila | 80 |
| Ideia de melhoria num processo | 49 |
| Senha ou acesso | **Em nenhuma pasta.** Ver item 6 |

## 4. Pastas de clientes

Cada cliente recebe um **código fixo e único**, em ordem de entrada: `CLI-001`, `CLI-002`… O código **nunca muda e nunca é reaproveitado**, mesmo que o cliente saia. A lista oficial de códigos fica no repositório do Henrique (`clientes/indice.md`).

Nome da pasta: `CLI-001 Dr. Felipe (advocacia)`.

* As pastas ficam em ordem de entrada. Para achar pelo nome, use a busca do Drive.
* O mesmo código é usado no Notion, no Slack, nas tarefas e no nome dos arquivos.
* Toda pasta de cliente tem as mesmas subpastas:

```
CLI-001 Dr. Felipe (advocacia)
   01 Contrato e cadastro
   02 Briefing e materiais do cliente
   03 Entregas
      Site · Rankeamento · Tráfego · Automação · Dados   (sempre os 5; bloco não contratado fica vazio)
   04 Relatórios
   05 Reuniões e atas
```

## 5. Nome dos arquivos

Regra geral:

```
AAAA-MM-DD_código-nome_tipo_descrição_v01
```

| Situação | Exemplo |
|---|---|
| Arquivo de cliente | `2026-11-04_CLI-001-felipe_contrato_pacote_v01` |
| Arquivo de cliente | `2026-11-10_CLI-002-lucas-melo_relatorio_mensal_v01` |
| Arquivo interno | `2026-11-30_INT_ata_reuniao-socios_v01` |

* **Data no começo:** os arquivos ficam em ordem cronológica.
* **Código e nome curto do cliente:** acha pelo código ou pelo nome, mesmo fora do Drive (baixado ou enviado por WhatsApp). Para assuntos internos, use `INT`.
* **Versão no final:** `v01`, `v02`… Nunca "final", "final2" ou "agora-vai".
* Sem acentos e sem espaços; use hífen dentro de cada parte.

Algumas pastas podem ter regra própria (por exemplo, extratos por mês). Quando houver, ela fica escrita neste manual.

## 6. Senhas e acessos

**Nunca guarde senhas em documentos, planilhas ou mensagens**, nem no Drive, nem no Slack, nem no Notion.
Senhas da ATIVOS e acessos de clientes ficam num **gerenciador de senhas** (a definir: Bitwarden ou 1Password), compartilhado só com quem precisa.

## 7. Quem faz o quê (matriz de responsabilidades)

R = executa · A = responde pelo resultado · C = é consultado · I = é informado

| Atividade | R | A | C | I |
|---|---|---|---|---|
| Salvar arquivos nas pastas certas | Quem produziu o arquivo | Quem produziu | — | — |
| Abrir pasta de cliente novo | Henrique | Henrique | Igor | Todos (Slack) |
| Arquivar cliente encerrado | Henrique | Henrique | Igor | Todos |
| Criar, renomear ou apagar uma pasta numerada | Henrique ou Igor | Henrique | Sócios | Todos |
| Sugerir mudança num processo (pasta 40) | Qualquer sócio | Dono do método do bloco | Henrique | — |
| Aprovar e publicar a versão oficial de um processo | Henrique (com o Claude) | Henrique | Dono do método | Todos |
| Incluir ou remover membros do Drive | Henrique ou Igor | Igor | Sócios | Todos |
| Revisar este manual | Henrique | Henrique | Sócios | Todos |

## 8. Procedimentos

### 8.1 Salvar um arquivo
1. Procure o tipo do arquivo no guia rápido (item 3).
2. Dê o nome no padrão do item 5.
3. Salve na pasta indicada. Não crie subpastas novas.

### 8.2 Abrir a pasta de um cliente novo
* **Quando:** contrato assinado.
1. Pegue o próximo código livre na lista de clientes.
2. Copie a pasta `CLI-000 Modelo` dentro da 20 e renomeie: `CLI-00X Nome curto (nicho)`.
3. Não apague nenhuma subpasta: todo cliente tem a mesma estrutura. Bloco não contratado fica vazio.
4. Avise no Slack o código e o nome do cliente.
* **Resultado:** pasta pronta, com o mesmo código no Notion e nas tarefas.

### 8.3 Encerrar um cliente
1. Confira se o contrato e os relatórios finais estão nas pastas.
2. Mova a pasta inteira para **90 Arquivo**, sem renomear.
3. Avise no Slack.

### 8.4 Pedir uma pasta nova
1. Explique no Slack o que vai ser guardado e por que não cabe em nenhuma pasta existente.
2. Henrique ou Igor decide e cria, usando o próximo número livre da área.
3. O manual é atualizado.

### 8.5 Mudar um processo (pasta 40)
1. Comente no documento ou salve um rascunho na **49 Sugestões e rascunhos**.
2. O Henrique revisa com o dono do método.
3. A versão oficial é atualizada no repositório e depois no Drive.

## 9. Exceções

| Situação | O que fazer |
|---|---|
| O arquivo serve para dois clientes | Salve no cliente principal e coloque um atalho no outro (botão direito › Organizar › Adicionar atalho) |
| O arquivo não se encaixa em nenhuma pasta | Salve provisoriamente em 00 Geral e pergunte no Slack; não crie pasta por conta própria |
| Prospect que ainda não fechou | Fica em 11 Prospecção ou 12 Propostas. Só ganha código CLI quando assinar o contrato |
| Cliente que volta depois de encerrado | Mantém o mesmo código. A pasta volta de 90 Arquivo para 20 Clientes |
| O cliente mandou senha por e-mail ou WhatsApp | Coloque no gerenciador de senhas e apague a mensagem. Nunca salve no Drive |
| Arquivo pessoal salvo por engano no Drive ATIVOS | Mova para o seu "Meu Drive" |
| Material de produção de conteúdo (vídeos brutos, artes) | Fica no Drive "Conteúdos". O entregável final vai para a pasta do cliente |
| Alguém de fora dos sócios precisa de acesso | Compartilhe só a pasta necessária. Se for frequente, criamos um Drive separado para o Financeiro |

## 10. Como saber se está funcionando

| Indicador | Meta | Como medir |
|---|---|---|
| Arquivos fora do padrão de nome | Nenhum nas pastas de clientes | Conferência mensal do Henrique |
| Pastas criadas fora do padrão | Nenhuma | Conferência mensal |
| Tempo para achar um arquivo | Menos de 1 minuto | Percepção dos sócios na revisão trimestral |

## 11. Documentos relacionados

* Lista de clientes e códigos: `clientes/indice.md` (repositório do Henrique)
* Catálogo de serviços: `servicos/catalogo.md`
* Estrutura da ATIVOS: `organizacao/estrutura.md`
