---
tipo: memória interna (fontes oficiais e casos reais)
assunto: canal do WhatsApp para clientes que vendem bebida alcoólica (base: CLI-004 Guto Bebidas)
coletado: 24/11/2026, páginas abertas no dia
uso: consulta interna; não vai para a pauta. Usar ao decidir o canal do WhatsApp de cada cliente e se o SDR pode fechar pedido
---

# WhatsApp: regras oficiais e casos reais (24/11/2026)

Regra de trabalho (Henrique, 24/11/2026): afirmar risco **só com base em fonte ou caso concreto**. Onde não há caso, dizer "não encontrei".

## Decisão em vigor

* **Fase 1 do CLI-004 Guto Bebidas (Igor, 24/11/2026):** WhatsApp Business (app) + UAZAPI + Chatwoot. A API oficial fica como possibilidade para depois.
* **Rastreio até a venda:** a ATIVOS tem infraestrutura própria para isso (Henrique, 24/11/2026).
* **Disparo em massa:** a ATIVOS não faz (Henrique, 24/11/2026).

## 1. Política de mensagens do WhatsApp Business

Fonte: https://whatsappbusiness.com/policy/ (atualizada em 23/09/2026).

| Trecho original | Tradução |
|---|---|
| "Alcohol and tobacco" (lista de Regulated Verticals) | Álcool é "vertical regulada" |
| "You are prohibited from messaging about any Regulated Verticals on the WhatsApp Business App." | Proibido enviar mensagem sobre vertical regulada pelo **app** WhatsApp Business |
| "You are prohibited from providing any commerce experiences to buy or sell goods or services that are Regulated Verticals" | Proibido catálogo, carrinho e outras experiências de compra para esses itens |
| "Alcohol – Allowed Countries: … Brazil …" / "Messaging may not be sent to people under 18 years of age." | No Brasil, mensagem sobre álcool é permitida **pela Plataforma (API oficial)**, nunca para menores de 18 |
| "If you use or operate a service which utilizes WhatsApp in violation of our terms or policies, such as messaging people at scale in an unauthorized manner, we have the right to limit or remove your access to WhatsApp for Business." | Violação pode levar a acesso limitado ou removido |
| "WhatsApp may use both automated processing techniques and human review teams … as well as reported messages" | Fiscalização por sistema automático, revisão humana e denúncias |

## 2. Violações da WhatsApp Business Platform (API oficial)

Fonte: https://developers.facebook.com/documentation/business-messaging/whatsapp/policy-enforcement-violations

| Trecho original | Tradução |
|---|---|
| "ALCOHOL: Businesses may not transact in the sale of alcohol. Examples: … Alcoholic beverages" | Empresas não podem **transacionar a venda** de bebida alcoólica, nem pela API oficial |

Leitura: falar sobre o produto pode (pela API, com 18+); fechar a venda pelo WhatsApp é violação. Liga com a decisão 3 do de-para (o SDR pode fechar pedido?). Pede parecer jurídico ou consulta à Meta.

## 3. Termos de Serviço do WhatsApp (versão geral)

Fonte: https://www.whatsapp.com/legal/terms-of-service (em vigor desde 04/01/2021).

| Trecho original | Tradução |
|---|---|
| "(e) involve sending illegal or impermissible communications such as bulk messaging, auto-messaging, auto-dialing, and the like" | Proibido mensagem em massa, mensagem automática e discagem automática |
| "You must not … through automated or other means, access, use … our Services in impermissible or unauthorized manners" | Proibido acesso automatizado não autorizado |

## 4. O que dizem os fornecedores das conexões não oficiais

| Fonte | Trecho |
|---|---|
| UAZAPI (https://uazapi.dev/) | "Sim, até utilizando a API oficial, há possibilidade de banimento da conta pelo WhatsApp. O WhatsApp bane contas principalmente quando é verificada a prática de SPAM. […] Se não houver denúncias, as chances de você ser banido usando a API são quase zero. Porém, atenção: se seu número for novo e você começar a mandar muitas mensagens, você será banido rapidamente." |
| Baileys (https://github.com/WhiskeySockets/Baileys) | "This project is not affiliated […] with WhatsApp […]. We discourage any stalkerware, bulk or automated messaging usage." |

## 5. Casos reais encontrados (relatos de usuários no GitHub da Baileys)

| Caso | O que aconteceu |
|---|---|
| https://github.com/WhiskeySockets/Baileys/issues/1925 | 10 números banidos ao postar em grupos pelo bot |
| https://github.com/WhiskeySockets/Baileys/issues/2850 | Banimento por envio em massa |
| https://github.com/WhiskeySockets/Baileys/issues/935 | Número novo banido em poucas horas |
| https://github.com/WhiskeySockets/Baileys/discussions/2663 | Número novo, conectado de VPS, banido ao parear; banimento temporário (voltou no app) |
| https://github.com/WhiskeySockets/Baileys/issues/2707 | Bloqueio temporário (erro 463) |

## Conclusão (só fato)

| Pergunta | Resposta |
|---|---|
| Mensagem sobre bebida pelo app WhatsApp Business é permitida? | Não (fonte 1) |
| Automatizar o app por conexão não oficial é permitido? | Não (fonte 3) |
| Fechar a venda de bebida pelo WhatsApp é permitido? | Não, nem pela API oficial (fonte 2) |
| Há caso concreto de punição por falar de bebida ou atender no receptivo? | Não encontrado em 24/11/2026 |
| Padrões dos casos reais de banimento | Spam, envio em massa, postagem em grupos e número novo; parte foi temporária |
| Situação do Guto | Número antigo, só receptivo, sem disparo: fora desses padrões |
