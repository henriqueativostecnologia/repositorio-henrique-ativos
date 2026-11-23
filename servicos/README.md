---
tipo: índice das receitas de serviço
atualizado: 23/11/2026
base: primeiro cliente do pacote, CLI-004 Guto Bebidas (venda de 23/11/2026)
---

# Receitas de serviço (onboarding padrão)

Uma **receita** é a lista completa de tarefas de um serviço, na ordem, com **responsável, dia, dependência e "pronto quando"**. Todo cliente novo recebe as tarefas da receita de cada serviço que comprou, e é assim que a central de tarefas é montada.

## Como ler os prazos

* **D0:** dia da venda (contrato assinado).
* **D1:** dia da reunião de início, quando o cliente começa a mandar acessos e materiais. Os prazos das receitas contam a partir daqui.
* Dias **corridos**, para bater com o que foi vendido ("7 dias", "15 dias").
* Uma tarefa que depende do Google ou da Meta (verificação, aprovação de modelo de mensagem) tem prazo **combinado com o cliente**, porque não depende de nós.

## Prazos de venda (decididos em 23/11/2026, a partir da venda do CLI-004 Guto Bebidas)

| Serviço | Prazo | Receita |
|---|---|---|
| Início e fim (vale para todo cliente) | D0 a D1, e o fim no último dia de cada entrega | `inicio-e-fim/receita.md` |
| Landing page | 7 dias | `landing-page/receita.md` |
| Google Meu Negócio (SEO, AEO, GEO) | 7 dias (entrega: perfil preenchido e verificação pedida) | `google-meu-negocio/receita.md` (*a escrever: aguarda as anotações do curso do Henrique*) |
| Tráfego pago (Meta Ads e Google Ads, com o bloco de rastreio) | 7 dias | `trafego-pago/receita.md` |
| Automação comercial (SDR de IA e infraestrutura) | 15 dias | `automacao-comercial/receita.md` |
| Recorrência mensal (o que o cliente paga todo mês) | todo mês, depois das entregas | `recorrencia-mensal/receita.md` |

## Quem é dono de cada serviço

| Serviço | Dono (responde pelo prazo) | Também trabalham |
|---|---|---|
| Início e fim | Henrique | Todos |
| Landing page | Bernardo | Hugo (pesquisa, wireframe e copy), Henrique (SEO da página) |
| Google Meu Negócio | Henrique (inclusive no painel e no GBP Check) | Hugo (copy da descrição e dos posts) |
| Tráfego pago | Igor | Design e videomaker (criativos), Bernardo (instalação técnica no site) |
| Automação comercial | Hugo (SDR) | Bernardo (servidor, banco do cardápio, CRM, deploy) |

## Regras

* As receitas **não dependem do que já foi feito** num cliente: listam tudo. O status de cada cliente fica na central de tarefas.
* Ao terminar cada cliente, a tarefa **FI-07 Lições aprendidas** atualiza a receita (por PR).
* Valores: a tabela oficial ainda não existe. O valor do CLI-004 Guto Bebidas está em `clientes/indice.md`, como **valor negociado, não é tabela oficial**.
* Fontes: documentação do CLI-004 Guto Bebidas (`referencias/cli-004-guto-documentacao-servicos-v0.md`), plano de 7 dias do Igor (`google-meu-negocio/referencias/plano-7-dias-igor-v0.md`) e ajuda oficial do Google, da Meta e do WhatsApp (links em cada receita).
* O modelo antigo (`pacote/eap-padrao.md`, v1 de 09/11) fica como histórico de horas até as receitas ganharem estimativa de horas.
