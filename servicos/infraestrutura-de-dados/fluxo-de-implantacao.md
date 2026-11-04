---
tipo: modelo de serviço
servico: Infraestrutura de Dados (rastreamento) para e-commerce
versao: rascunho v0 · 04/11/2026
situacao: prazos propostos, aguardando aprovação do Igor; documento oficial ainda será feito
origem: "Mapa da operação de e-commerce" (loja fictícia, sem dados de cliente)
---

# Infraestrutura de Dados: do contrato assinado à entrega

Sete sprints. Cada sprint termina num **portão**: o sprint seguinte só começa com ele aprovado.
Prazos em dias úteis (d.u.). Relógio do contrato: 5 d.u. Relógio da implementação: começa no G0, cerca de 30 d.u. (S1 a S6).

## Sequência

| Sprint | O que acontece | Prazo | Depende do cliente |
|---|---|---|---|
| S0 Contrato e acessos | Contrato, termo de tratamento de dados (DPA) e acessos | 5 d.u. | 100% dos acessos · DPA assinado |
| S1 Diagnóstico | Levantamento da medição atual | 5 d.u. | Dor nomeada · logins de leitura |
| S2 Plano de medição | Plano de medição para aprovação | 5 d.u. | Faturamento · ferramenta de consentimento (CMP) · aceite do plano |
| S3 Implementação do tracking | Tudo construído em ambiente de teste; nada publicado | 10 d.u. | Dev da loja: dataLayer, DNS do sGTM, webhook · gestor de tráfego: ação de conversão no Google Ads |
| S4 QA e publicação | Testes e publicação, com parada humana antes de publicar (o Igor aprova e publica) | 5 d.u. + janela | 1 pedido real pago · janela combinada |
| S5 Dados no MDP (em paralelo, do S1 ao fim do S4) | **Mídia:** tenant, Google Ads e Meta, dbt até o `fct_daily_campaigns`. **Pedidos:** conector da loja, export do GA4 para o BigQuery (1 dataset por cliente) | +10 d.u. se a loja não for Shopify | Token de leitura dos pedidos · acesso de Editor no GA4 |
| S6 Painel, alertas e entrega | Painel no ar, alertas, relatório e aceite | 5 d.u. | Aprovar o relatório · aceite por escrito |
| Operação recorrente | Acompanhamento contínuo (mensalidade) | Contínua | — |

**Desvio possível, NO-BUILD no G2:** se a medição já está boa, pula direto para o S6.

**As duas trilhas só se juntam no S6.** Ele começa quando a publicação foi feita (G4) e os números do MDP foram conferidos (G5). Um S5 atrasado segura a entrega, mesmo com o tracking pronto.

## O que fecha cada portão

| Portão | Fecha quando | Quem aprova |
|---|---|---|
| G0 | Contrato e DPA assinados, e 100% dos acessos obrigatórios em mãos: GTM, GA4, Google Ads, Meta e pedidos da loja. Liga o relógio da implementação | Henrique confere, Igor confirma |
| G1 | Diagnóstico com cada fato etiquetado e o radar de alertas criado | Igor |
| G2 | Plano aprovado pelo cliente e re-medição com GO (ou NO-BUILD, que pula para o S6) | Cliente e Igor |
| G3 | Tudo construído no ambiente de teste, nada publicado, revisão adversarial sem bloqueio | Igor |
| G4 | QA sem item crítico, pauta da parada humana aprovada, publicação feita e versão de volta anotada | Igor; gestor ou dono quando tocar campanha, consentimento ou faturamento |
| G5 | Mídia batendo com as plataformas e pedidos batendo com o painel da loja na mesma semana fechada | Dev de dados e Igor |
| G6 | Painel no ar, alertas ligados, relatório entregue e aceite do cliente por escrito | Cliente |

## Notas (04/11/2026)

* **Dev de dados:** Hugo, ainda a confirmar no documento oficial.
* **MDP:** Marketing Data Platform da ATIVOS. Mais contexto virá da pasta de contexto do Drive.
* **Operação recorrente:** existe mensalidade depois da entrega (impacto no financeiro).
* **Prazos:** propostas deste serviço, aguardando aprovação do Igor.
