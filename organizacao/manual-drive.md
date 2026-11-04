---
tipo: manual
atualizado: 04/11/2026
situacao: versão 1, aguardando aprovação; depois de aprovado, uma cópia vai para o Drive em "00 Geral / 01 Manual de uso"
---

# Manual de uso do Drive ATIVOS

Este manual explica **onde fica cada coisa**, **onde salvar** e **por que as pastas têm números**.
Vale para todos os sócios. A versão oficial fica no repositório do Henrique; a cópia no Drive é para consulta.

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
| **20 Clientes** | Uma pasta por cliente, com código fixo (ver item 4) · CLI-000 Modelo, para copiar |
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
| Documento que explica algo da ATIVOS para o Claude | 02 (dentro de 00 Geral) |
| Curso ou apostila | 80 |
| Ideia de melhoria num processo | 49 |
| Senha ou acesso | **Em nenhuma pasta.** Ver item 6 |

Na dúvida, pergunte no Slack ou ao Claude antes de criar uma pasta nova.

## 4. Pastas de clientes

Cada cliente recebe um **código fixo e único**, em ordem de entrada: `CLI-001`, `CLI-002`… O código **nunca muda e nunca é reaproveitado**, mesmo que o cliente saia.

Nome da pasta: `CLI-001 Dr. Felipe (advocacia)`.

* As pastas ficam em ordem de entrada. Para achar pelo nome, use a busca do Drive ou digite o nome com a pasta 20 aberta.
* O mesmo código é usado no Notion, no Slack, nas tarefas e no nome dos arquivos. Assim tudo de um cliente se encontra pelo código.
* Toda pasta de cliente tem as mesmas subpastas:

```
CLI-001 Dr. Felipe (advocacia)
   01 Contrato e cadastro
   02 Briefing e materiais do cliente
   03 Entregas
      Site · Rankeamento · Tráfego · Automação · Dados   (só os blocos contratados)
   04 Relatórios
   05 Reuniões e atas
```

**Cliente novo:** copie a pasta `CLI-000 Modelo`, troque pelo próximo código livre (veja a lista de clientes) e coloque o nome.
**Cliente encerrado:** mova a pasta inteira para **90 Arquivo**, sem renomear.

## 5. Nome dos arquivos

Regra geral:

```
AAAA-MM-DD_código_tipo_descrição_v01
2026-11-04_CLI-001_proposta_pacote_v01
2026-11-30_INT_ata_reuniao-socios_v01
```

* **Data no começo:** os arquivos ficam em ordem cronológica.
* **Código:** do cliente (`CLI-001`) ou `INT` para assuntos internos.
* **Versão no final:** `v01`, `v02`… Nunca "final", "final2" ou "agora-vai".
* Sem acentos e sem espaços; use hífen dentro da descrição.

Algumas pastas podem ter regra própria (por exemplo, extratos por mês). Quando houver, ela fica escrita na própria pasta e neste manual.

## 6. Senhas e acessos

**Nunca guarde senhas em documentos, planilhas ou mensagens**, nem no Drive, nem no Slack, nem no Notion.
Senhas da ATIVOS e acessos de clientes ficam num **gerenciador de senhas** (a definir: Bitwarden ou 1Password), compartilhado só com quem precisa.

## 7. Processos (pasta 40)

A pasta 40 é a biblioteca de "como fazemos as coisas", escrita para que qualquer pessoa consiga executar.

* **Todos podem ler e usar.**
* **Para sugerir uma mudança ou um processo novo:** comente no próprio documento ou salve um rascunho na **49 Sugestões e rascunhos**.
* A versão oficial é aprovada pelo Henrique e mantida no repositório; depois é atualizada no Drive. Assim ninguém trabalha com uma versão desatualizada.

## 8. Regras rápidas

1. Não crie pastas fora do padrão. Precisa de uma nova? Peça a quem administra o Drive (Henrique ou Igor).
2. Não renomeie nem mova pastas numeradas.
3. Use sempre o código do cliente.
4. Terminou um projeto? Mova para 90 Arquivo.
5. Senha nunca vai para documento.
