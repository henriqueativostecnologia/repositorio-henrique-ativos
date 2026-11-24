---
tipo: cópia de contexto (pesquisa do Igor, texto integral)
original: Drive ATIVOS › 20 Clientes › CLI-004 Guto Bebidas › 03 Entregas › Tráfego (também em PDF)
link: https://docs.google.com/document/d/1JmxaWIdFunQfHE5XsfEJDLAha22lovoMNhbW29cO-lg/edit
copiado: 24/11/2026
regra: cópia integral; sem contato, CPF, CNPJ, senha nem acesso. Afirmações marcadas "verificar" pelo autor precisam de conferência no texto oficial antes de ir para proposta ou contrato
---

Ativos Tecnologia · Gestão de Tráfego · Guto Bebidas · 23/11/2026

# Meta Ads e Google Ads com rastreamento via WhatsApp

SOP de 7 dias aplicado à Guto Bebidas. Seu mapa está certo na ordem geral; o que ele deixa de fora decide o resultado. Os diagramas seguem o sistema do repositório diagram-design. As tabelas completas, a rotina recorrente e as regras de álcool estão nas seções 6 a 8.

**O que o mapa deixa de fora decide o resultado.** Falta coleta formal de acessos e verificações, aprovação de orçamento e criativos pelo cliente e QA de tracking antes de publicar.

**O bloqueio central:** sem a WhatsApp Business Platform (API oficial) e um CRM que registre a venda, não há como devolver “compra” à Meta ou ao Google. A Evolution API prevista para o SDR não entrega o `ctwa_clid` oficial e impede a API de Conversões para mensagens.

**Álcool muda o setup desde o D1:** idade mínima de 18 anos, advertências do CONAR nos criativos e risco de o catálogo de bebidas no WhatsApp ser recusado.

**Nota de método da pesquisa original:** as páginas oficiais da Meta e do Google não foram abertas. As afirmações oficiais vêm dos documentos técnicos internos da Ativos (GM-03.1, GM-09.3, GM-09.4) e de conhecimento consolidado das políticas. Reabra os links oficiais antes de usar como padrão da agência.

## 1. Os dias do setup

D0 é a assinatura e o kickoff; D1 a D7 são dias corridos do prazo combinado (23/11 a 29/11). O prazo é viável se o cliente liberar os acessos no D1 e aprovar no D5. Não é “aquecimento” da conta: o aprendizado de verdade começa após a publicação, no D6, e leva semanas. oficial opinião

etapao dia que decide o resto

Aprovações da Meta, do Google, da verificação de empresa e do Perfil da Empresa podem passar do D7. Combine com o cliente que a entrega do D7 é “setup pronto e campanhas publicadas ou em revisão”.

## 2. Do clique à venda: o rastreamento

Dois caminhos se encontram no CRM. No Meta, o clique carrega o `ctwa_clid` até o WhatsApp oficial. No Google, a landing guarda o GCLID e o botão do WhatsApp leva um código curto que o CRM associa a ele. Quando o atendente marca “pedido pago” com valor, uma automação devolve a compra às duas plataformas, e o relatório cruza o investimento por canal com as vendas do CRM. oficial mercado

**Decisão do D1:** troque a premissa da Evolution API, para o número que recebe anúncios, por Cloud API ou coexistência, e conecte ao Chatwoot. Pela reunião de 23/11, o Hugo assume o SDR de IA e o Bernardo a infraestrutura de dados, então a troca de conector cabe a eles. Sem isso, o diferencial “rastrear até a compra” não se sustenta. opinião

Meta

- O evento vai com `action_source: "business_messaging"`, `messaging_channel: "whatsapp"` e o `ctwa_clid`. oficial
- O `ctwa_clid` chega pelo webhook da WhatsApp Business Platform, no objeto `referral` da primeira mensagem.
- `event_time` de até 7 dias; deduplicação por `event_name` + `event_id` em até 48 h (doc interna GM-03.1).
- Dois eventos de negócio: `LeadSubmitted` (lead qualificado) e `Purchase` (venda com `value` e `currency: BRL`, até 7 dias após a conversa), com `event_id` igual ao ID do pedido.
- **Sem a API oficial** (Cloud API, BSP ou coexistência com o app), não existe `ctwa_clid`.

Google

- O lead do WhatsApp só vira “compra” com o GCLID guardado. O GTM lê o GCLID, grava num cookie, e o botão gera a mensagem pré-preenchida com um código curto (ex.: “Pedido #G7K2”). mercado
- Para um negócio pequeno, o caminho prático é a importação por planilha, Google Sheets ou conector de CRM.
- O Google Ads Help (answer/15713840, citado na GM-09.4) afirma que, a partir de 15/06/2026, a importação de conversões offline migra para a Data Manager API e fica bloqueada na Google Ads API. oficial Como essa data já passou, confirme o estado atual.
- Segundo a PPC Land (Luís Rijo, 10/04/2026, citada na GM-09.4), as enhanced conversions para web e para leads viram um único liga/desliga a partir de junho de 2026.

## 3. Meta Ads, dia a dia

Doze tarefas do setup. Barras na mesma coluna rodam em paralelo. Em coral, o que está fora do seu controle: as verificações e a revisão da plataforma.

tarefafora do seu controlepode passar do D7

O Gantt agrupa o benchmark e a estratégia (M5) e os roteiros e a produção dos criativos (M6). O remarketing é planejado no D6 e só ativa por volta do D14 ao D30, quando houver tamanho de público; por isso fica fora do Gantt. A verificação de empresa e de domínio pode levar dias. mercado

## 4. Google Ads, dia a dia

O rastreio (G6) é o mesmo bloco único do Meta: configurado uma vez e usado pelos dois canais.

tarefafora do seu controlepode passar do D7

A verificação do anunciante pode levar dias, e álcool pode ficar “Qualificado (limitado)” na revisão, de cerca de 1 dia útil. As conversões offline (G12) começam no D7 e viram rotina semanal. oficial

## 5. Estrutura de campanha para orçamento pequeno

Concentrar é a regra: a Meta diz que o conjunto sai do aprendizado com cerca de 50 eventos de otimização em 7 dias após a última edição relevante. oficial Com verba de negócio local, isso só acontece otimizando para conversas, não para compras. mercado

Meta

- 1 campanha, 1 conjunto principal e um 2º só se o orçamento suportar \~50 conversas por semana em cada. mercado opinião
- 6 a 9 anúncios no lançamento e 3 a 6 ativos. Testes de criativo dentro do mesmo conjunto, trocando 2 a 4 peças a cada 2 semanas.
- Orçamento: o mínimo que gere volume de conversas. Se o custo por conversa no benchmark for R$ 5–15, R$ 30–50 por dia por conjunto é um piso realista.

Google

- 1 campanha de Pesquisa, 2 a 3 grupos, correspondência de frase e exata, raio de entrega e horário do atendimento. mercado opinião
- Comece com Maximizar cliques com teto de CPC ou Maximizar conversões; migre para CPA desejado com \~15+ conversões em 30 dias.
- **Performance Max no início: não.** Sem histórico e com verba pequena, ele tende a gastar em inventário de baixa intenção. Reavalie depois de \~30 conversões. mercado

Volume criativo realista: lote inicial de 9 peças (3 vídeos, 3 estáticos, 3 carrosséis) e depois 2 a 4 novas a cada 2 semanas, de 6 a 8 por mês, priorizando variações do vencedor. mercado

## 6. Álcool: quem regula o quê

As regras mudam o setup desde o D1. Confirme o texto literal de cada uma antes de escalar: a pesquisa original não abriu as páginas oficiais.

| Fonte | O que diz | O que muda no setup |
| --- | --- | --- |
| Meta (anúncios) | Anúncios de álcool seguem as leis locais e usam segmentação por idade e país compatível. No Brasil, 18+. oficial | 18+ nos conjuntos (a Meta pode impor automaticamente); página e Instagram com restrição de idade. |
| Google Ads | Álcool é conteúdo “restrito”: não pode ser mostrado a menores nem retratar consumo excessivo. oficial | Textos sem apelo a consumo excessivo; aviso 18+ na landing page. |
| Lei 9.294/96 | Restringe a propaganda de bebidas acima de 13 °GL (destilados). oficial | Atenção redobrada nos criativos de destilados. |
| CONAR, Anexo P | Vale para todas as bebidas alcoólicas, inclusive cerveja, e exige cláusula de advertência: “Beba com moderação”, “Se beber, não dirija”, “Venda e consumo proibidos para menores de 18 anos”. oficial | Advertência em todas as peças, modelos adultos (aparentando 25+), nada de consumo excessivo, direção ou menores. |
| Política de Comércio do WhatsApp | Lista álcool entre os itens que não podem ser transacionados por catálogo e carrinho. oficial verificar | O cardápio vira link (landing ou cardápio digital) ou imagem/PDF enviado pelo SDR, não catálogo nativo, até confirmar. opinião |

A tarefa “configurar o cardápio no WhatsApp Business”, atribuída ao Hugo, pode ser rejeitada ou derrubar o catálogo. Confirme a política antes de montar o catálogo nativo. A coluna “O que muda no setup” é minha síntese do documento.

## 7. Rotina recorrente do gestor

Depois do setup, doze tarefas por frequência: da checagem diária de 10 a 15 minutos por cliente ao relatório mensal de 2 a 3 horas.

| Frequência | Tarefa | O que olhar / fazer | Critério de ação | Fonte |
| --- | --- | --- | --- | --- |
| Diária (10–15 min por cliente) | Checagem de saúde | Gasto vs. orçamento, anúncios reprovados, conta ou pagamento com problema, conversas recebidas, tag/dataset com erro | Reprovou → corrigir no mesmo dia; gasto 0 → investigar | mercado |
| Diária | Qualidade das conversas | Amostra de conversas no Chatwoot: tempo de resposta, SDR respondendo certo, conversas de menores ou fora do raio | Tempo de resposta > 5 min → alinhar atendimento | opinião |
| Diária / a cada 2 dias | Marcação de vendas no CRM | Garantir que toda venda tem valor e origem | Venda sem origem → cobrar o atendimento | opinião |
| Semanal (1–2 h) | Otimização Meta | CPA por conversa, CTR, frequência, CPM; pausar anúncios fracos só após \~3–7 dias com gasto relevante; sem edições grandes durante o aprendizado | Frequência > 3 ou CTR caindo → novos criativos | oficial + mercado |
| Semanal | Otimização Google | Relatório de termos de pesquisa → negativas; parcela de impressões perdida (orçamento vs. ranking); horários e dias | Termo irrelevante com gasto → negativar | oficial + mercado |
| Semanal | Envio de conversões | CAPI Business Messaging (automático) e upload offline do Google | Upload com erro → corrigir na semana | oficial |
| Semanal | Report curto ao cliente | Conversas, custo por conversa, vendas atribuídas, receita, 3 próximos passos | — | mercado |
| Quinzenal | Ciclo de criativos | 2–4 peças novas (variações dos vencedores + 1 ângulo novo) | Criativo vencedor com fadiga | mercado |
| Mensal (2–3 h) | Relatório e reunião | Investimento, conversas, vendas, ROAS real (CRM), CAC, comparação com o mês anterior, testes do próximo mês | Mudança de estratégia só com dados de 30 dias | mercado |
| Mensal | Auditoria de tracking | Eventos, deduplicação, EMQ, GCLID no CRM, UTMs "Unassigned" no GA4 | Gap anormal Meta vs. CRM → investigar | mercado |
| Mensal | Estratégia de lance (Google) | Ao acumular conversões suficientes, migrar para Maximizar conversões ou CPA desejado | \~15+ conversões/30 dias como referência | oficial/mercado |
| Trimestral | Revisão de oferta e sazonalidade | Calendário (Carnaval, jogos, verão, fim de ano), revisar raio e orçamento | — | opinião |

Atribuição nunca bate 100%: espere diferença entre Meta, Google e CRM. O número de decisão é a venda registrada no CRM. A doc interna GM-09.3 cita o Varos Industry Benchmark (2024, via EasyInsights): a Meta reporta em média 26% mais conversões que as ferramentas de análise, por conversões modeladas e atribuição por último evento. É benchmark de mercado, não lei.

## 8. Tabelas completas por canal

As dez colunas por tarefa, lidas direto do arquivo. D0 é a assinatura e o kickoff; D1 a D7 são os dias corridos do prazo. Tempos são de mercado e opinião para uma equipe enxuta.

Meta Ads, Click-to-WhatsApp (15 etapas)

| Etapa | Tarefa | Subtarefas | Entrada necessária | Entregável | Papel responsável | Tempo estimado | Ferramentas | Depende de | Critério de "pronto" |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0. Kickoff e briefing (D0–D1) | Alinhar objetivo, oferta e KPIs | Ticket médio, margem, raio de entrega, horários, mix (cerveja, destilados, gelo, carvão), sazonalidade (fim de ano, jogos), orçamento mensal de mídia, meta de conversas e vendas, quem atende o WhatsApp | Contrato assinado; formulário de briefing | Briefing + plano de mídia de 1 página com orçamento aprovado por escrito | Gestor de tráfego + cliente | 1–2 h | Formulário, Google Docs | — | Cliente aprovou orçamento, KPIs e raio por escrito (WhatsApp/e-mail) mercado |
| 1. Acessos e ativos (D1) | Coleta de acessos | Página do FB (criar ou recuperar), Instagram profissional, conta de anúncios do cliente no Portfólio Empresarial (BM) do cliente com a Ativos como parceira, forma de pagamento do cliente, 2FA, acesso ao domínio/DNS | Logins do cliente, CNPJ, cartão | Checklist de acessos 100% verde | Cliente (concede) + gestor (valida) | 2–4 h (cliente costuma atrasar) | Meta Business Suite, Gerenciador de Negócios | 0 | Agência é parceira com acesso total à página, IG, conta de anúncios e dataset; conta de anúncios **pertence ao cliente** mercado |
| 2. Verificações e compliance (D1–D2) | Verificar empresa, domínio e conformidade de álcool | Verificação da empresa (CNPJ); verificação de domínio (DNS TXT ou meta-tag); restrição de idade 18+ na página e no IG; revisar Política de Comércio do WhatsApp (catálogo); checklist CONAR | CNPJ, documento, DNS da LP | Empresa e domínio verificados; página 18+ | Gestor + cliente | 1 h de trabalho; verificação pode levar dias | Central de Segurança do BM | 1 | Domínio verificado no BM; idade mínima 18 configurada oficial |
| 3. WhatsApp Business Platform (D1–D3) | Conectar o número ao anúncio e à API | Decidir entre app + coexistência ou Cloud API via BSP; criar WABA; aprovar nome de exibição; vincular número à página; ativar webhook (captura do `referral`/`ctwa_clid`); conectar ao Chatwoot/CRM | Número do cliente, acesso ao celular para OTP | Número ativo na WABA ligado à página e ao Chatwoot | Gestor + infra (Bernardo) | 3–6 h + espera de aprovação | WhatsApp Manager, BSP ou Cloud API, Chatwoot | 1, 2 | Mensagem de teste vinda de anúncio chega ao Chatwoot com `referral`/`ctwa_clid` registrado oficial |
| 4. Benchmark (D1–D2) | Pesquisa de concorrentes | Biblioteca de Anúncios (filtrar BH, "distribuidora", "delivery de bebidas"); anotar ganchos, ofertas, formatos, CTA; perfis do Google Meu Negócio da grade de ranking (Hudsons Beer, Castelo etc.)\[1\] | Lista de concorrentes (relatório de ranking local já existe no Drive)\[1\] | Swipe file com 10–20 anúncios + 3 ângulos de comunicação | Gestor de tráfego | 2–3 h | Biblioteca de Anúncios, Drive | 0 | 3 ângulos priorizados aprovados internamente mercado |
| 5. Estratégia e públicos (D2) | Desenhar estrutura | Objetivo Engajamento ou Vendas com local de conversão WhatsApp; 1 campanha; 1–2 conjuntos (raio de entrega + 18+, público amplo/Advantage+; opcional 1 conjunto de remarketing quando houver volume); orçamento por conjunto; nomenclatura; janela de aprendizado | Briefing, benchmark, orçamento | Documento de estrutura + mensagem de boas-vindas pré-preenchida | Gestor de tráfego | 2 h | Gerenciador de Anúncios, planilha | 0, 4 | Estrutura cabe no orçamento (≥ \~50 conversas/semana por conjunto ou consolidar) mercado/opinião |
| 6. Roteiro e briefing criativo (D2) | Transformar ângulos em peças | Roteiros de 3 vídeos (gancho em 3 s, oferta, CTA "chama no WhatsApp"), 3 estáticos, 3 carrosséis; texto com advertência CONAR; modelos aparentando 25+; sem consumo excessivo, direção ou menores | Benchmark, fotos e vídeos do cliente | Briefing por peça | Gestor + designer + videomaker | 2–3 h | Docs, Canva/Figma | 4, 5 | Cada peça tem gancho, oferta, CTA e advertência oficial conar + mercado |
| 7. Produção de criativos (D3–D4) | Produzir as 9 peças (lote 1) | Captação na loja (geladeira, entrega, preço); edição 9:16 e 4:5; legendas; variações de texto | Briefing, material do cliente | 9 peças nos formatos 9:16, 1:1 e 4:5 | Designer + videomaker | 1,5–2 dias | CapCut, Canva, Higgsfield | 6 | Peças revisadas contra a política de álcool da Meta e o CONAR mercado |
| 8. Rastreio (D2–D4, em paralelo aos criativos) | Bloco único de rastreio | Pixel/dataset; GTM na LP; eventos `Contact`/`clique_whatsapp`; UTMs padrão; GA4; CAPI web; **CAPI para Business Messaging** com `LeadSubmitted` (lead qualificado) e `Purchase` (venda com valor) a partir do CRM | Acesso à LP, WABA, Chatwoot/CRM | Mapa de eventos + tags publicadas | Gestor (tracking) + Bernardo (infra) | 1 dia | GTM, GA4, Events Manager, Chatwoot, n8n/Python | 1, 3 | Eventos aparecem em Test Events e não são duplicados oficial\[4\] |
| 9. Processo comercial no CRM (D3–D4) | Etapas do lead até a compra | Funil: conversa iniciada → qualificado → pedido → pago; campo valor da venda; etiqueta "origem: anúncio" (com `ctwa_clid`); script do SDR/atendente para marcar a venda | Chatwoot configurado, atendente treinado | Funil no CRM + rotina de marcação | Gestor + cliente (atendimento) + Hugo (SDR) | 3–4 h + treino de 30 min | Chatwoot, planilha ou CRM | 3, 8 | Atendente marca a venda com valor em 100% dos testes opinião |
| 10. Aprovação do cliente (D5) | Aprovar criativos e textos | Enviar grade de peças; 1 rodada de ajustes; aceite formal | Peças finais | Aceite por escrito | Cliente | 0,5 dia (SLA de 24 h) | WhatsApp, Drive | 7 | "Aprovado" registrado mercado |
| 11. QA de tracking e anúncio (D5) | Testes de ponta a ponta | Clicar no anúncio em pré-visualização ou com orçamento mínimo; conferir abertura do WhatsApp com mensagem pré-preenchida; `ctwa_clid` no CRM; evento de teste no Events Manager; UTMs no GA4 | Itens 8 e 9 prontos | Checklist de QA assinado | Gestor de tráfego | 2–3 h | Test Events, Pixel Helper, GA4 DebugView | 8, 9 | 100% dos itens do checklist OK mercado |
| 12. Subir campanhas (D6) | Publicar | Criar campanha; 1–2 conjuntos; 6–9 anúncios; revisar política; programar início | Aprovação + QA | Campanhas ativas | Gestor de tráfego | 2 h + revisão da Meta (geralmente até 24 h) | Gerenciador de Anúncios | 10, 11 | Anúncios "Ativos", sem reprovação oficial |
| 13. Remarketing (planejado no D6, ativa \~D14–D30) | Públicos personalizados | Engajou IG/FB 30–90 dias, visitantes da LP, quem conversou no WhatsApp; excluir compradores recentes | Volume mínimo de público | Conjunto de remarketing | Gestor | 1 h | Públicos do Gerenciador | 12 | Público com tamanho suficiente para entregar mercado |
| 14. Entrega D7 | Relatório de setup | Prints das estruturas, mapa de eventos, acessos, próximos passos, expectativa de aprendizado (2–4 semanas) | Tudo acima | Relatório de entrega + reunião de 30 min | Gestor + cliente | 1–2 h | Looker Studio, Docs | 12 | Cliente assina o aceite do setup mercado |

Google Ads, Rede de Pesquisa local (12 etapas)

| Etapa | Tarefa | Subtarefas | Entrada necessária | Entregável | Papel responsável | Tempo estimado | Ferramentas | Depende de | Critério de "pronto" |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0. Acessos e conta (D1) | Conta, MCC e faturamento | Criar ou acessar a conta do cliente; vincular à MCC da Ativos; pagamento do cliente; iniciar **verificação do anunciante** | Login Google do cliente, CNPJ, cartão | Conta vinculada à MCC | Cliente + gestor | 1–2 h + verificação (pode levar dias) | Google Ads, MCC | Briefing Meta (0) | Conta ativa com faturamento; verificação enviada oficial |
| 1. Compliance de álcool (D1) | Checar política "Álcool" | Política Google para o Brasil; palavras e textos sem apelo a consumo excessivo; excluir menores (padrão da política); revisar LP (aviso 18+) | Política, LP | Checklist de compliance | Gestor | 1 h | Central de Políticas | 0 | LP e textos sem violações óbvias oficial |
| 2. Análise de concorrentes (D1–D2) | Leilão e mensagens | Buscar termos em BH (anônimo); Centro de Transparência de Anúncios; anotar títulos, ofertas, extensões; comparar com GMB (ranking local do Drive) | Lista de concorrentes | Quadro de ofertas e USPs | Gestor | 1–2 h | Centro de Transparência de Anúncios, SERP | 0 | 3 diferenciais definidos mercado |
| 3. Palavras-chave (D2) | Pesquisa e agrupamento | Planejador (BH + raio); clusters: "distribuidora de bebidas \[bairro/perto de mim\]", "delivery de bebidas/cerveja", "gelo/carvão", marca; lista de negativas (emprego, atacado de outra cidade, "como fazer", grátis) | Acesso à conta | Planilha com 2–3 grupos e 30–60 termos + negativas | Gestor | 2–3 h | Planejador de palavras-chave | 0 | Cada grupo tem intenção única mercado |
| 4. Correspondências (D2) | Definir tipos | Frase e exata no início; ampla só com lance inteligente e dados de conversão; negativas no nível da conta | Planilha da etapa 3 | Lista final por tipo | Gestor | 1 h | Google Ads Editor | 3 | Sem sobreposição relevante entre grupos mercado |
| 5. Rastreio (D2–D4, bloco único) | Conversões e consentimento | Auto-tagging ON; Google tag via GTM; conversão primária "clique no WhatsApp" na LP; captura e persistência do GCLID na LP, enviado ao WhatsApp/CRM (ID curto na mensagem pré-preenchida); Enhanced Conversions (toggle único); vincular GA4; banner de consentimento (LGPD/Consent Mode) | GTM, LP, CRM | Ações de conversão primárias e secundárias configuradas | Gestor + Bernardo | 0,5–1 dia | GTM, GA4, Google Ads | 0 | Tag Assistant OK; conversão de teste registrada oficial |
| 6. Configuração da campanha (D3) | Campanha de Pesquisa | Só Rede de Pesquisa (desmarcar Display e parceiros); local "presença" (não "interesse"); raio de entrega; programação no horário de atendimento do WhatsApp; orçamento diário; lance inicial Maximizar cliques com limite de CPC **ou** Maximizar conversões | Itens 3, 4 e 5 | Campanha em rascunho | Gestor | 1–2 h | Google Ads | 3–5 | Revisão cruzada feita por outra pessoa mercado |
| 7. Anúncios e ativos (D3–D4) | RSAs e ativos | 2 RSAs por grupo (15 títulos, 4 descrições); sitelinks; frases de destaque; ativo de local (vincular o Perfil da Empresa); ativo de chamada; imagens; logo | Fotos do cliente, GMB verificado | Anúncios em rascunho | Gestor + designer (imagens) | 2–3 h | Google Ads | 6, GMB (Henrique) | Força do anúncio "Boa" ou "Excelente" oficial |
| 8. URL final e UTMs (D4) | Padronizar | Final URL = LP; sufixo de URL com UTMs; testar o redirecionamento do botão para wa.me com GCLID/ID | LP no domínio final | Template de rastreamento | Gestor | 30 min | Google Ads, GA4 | 5 | Sessões com `google / cpc` no GA4 mercado |
| 9. Aprovação do cliente + QA (D5) | Aceite e testes | Aprovar textos; teste de clique real; conferir conversão e GCLID no CRM | Itens 5–8 | Checklist de QA + aceite | Cliente + gestor | 1–2 h | Tag Assistant | 5–8 | Todos os testes OK mercado |
| 10. Campanha no ar (D6) | Publicar | Ativar; acompanhar a revisão (álcool pode ficar "Qualificado (limitado)") | QA OK | Campanha ativa | Gestor | 30 min + revisão (geralmente \~1 dia útil) | Google Ads | 9 | Status "Qualificado" com impressões oficial |
| 11. Conversões offline (D7 → rotina) | Fechar o loop | Planilha ou Sheets com GCLID, data e valor da venda; importação programada (diária ou semanal); a médio prazo, conector de CRM/Data Manager API | CRM com GCLID e valor | Ação "Venda WhatsApp (offline)" | Gestor + atendimento do cliente | 2 h de setup + 15 min/semana | Google Ads (Uploads), Sheets | 5, CRM | Primeira importação aceita sem erro oficial |

## 9. O seu mapa, comparado com a pesquisa

Confirma

- Página → BM → benchmark → estratégia → criativos → campanhas → remarketing é o fluxo dos cursos da Meta e das agências. mercado
- Mínimo de 3 vídeos, 3 fotos e 3 carrosséis é um primeiro lote razoável; 9 peças bastam para 1 a 2 conjuntos. mercado
- No Google, concorrentes → palavras-chave → correspondência → Rede de Pesquisa, raio, horário e orçamento → ativos → URL/UTMs está correto para negócio local. oficial mercado
- O “bloco único de rastreio” é correto: GTM, GA4, pixel, tag do Google Ads e UTMs são infraestrutura compartilhada. mercado
- Prazo de 7 dias para o setup é viável, com acessos no D1 e aprovação no D5.

Corrige

- **“Aquecimento de conta” não é aprendizado.** O aprendizado começa quando o conjunto entrega, com \~50 eventos em 7 dias. Otimize para conversas e só passe a compras com dezenas de vendas por semana via CAPI. oficial opinião
- **O rastreio não é a etapa 6.** Ele roda em paralelo, de D2 a D4, porque depende de WABA, webhook e CRM. mercado
- **A Evolution API não serve** para rastrear leads de anúncio: não recebe o `referral`/`ctwa_clid` oficial, não envia eventos à CAPI e traz risco de banimento. Use Cloud API (direta ou via BSP) ou coexistência.
- **Muitos públicos** pulverizam o aprendizado: prefira raio + 18+ com público amplo. mercado
- **Remarketing no D7:** só ganha escala após 2 a 4 semanas de público. Planeje no setup, ative com tamanho.
- **Google sem conversão configurada:** o mapa só tem “site e UTMs”. Sem conversão primária e GCLID no CRM, não há lance inteligente nem atribuição de venda. oficial
- **Performance Max no início: não.**

Falta

- **D0 de contrato e acessos:** acessos com a conta de anúncios do cliente, a agência como parceira, pagamento no nome do cliente e 2FA. mercado
- **Verificações que podem estourar o prazo:** empresa e domínio (Meta), anunciante (Google), nome de exibição do WhatsApp e Perfil da Empresa. O plano do Google Meu Negócio da Guto Bebidas alerta que a análise do vídeo pode levar até 5 dias úteis, e o cartão-postal até 14. oficial
- **Compliance de álcool:** 18+ nos conjuntos, página e IG com restrição de idade, advertência do CONAR em todas as peças. oficial
- **CRM e definição de “venda”:** etapas, campo de valor, quem marca e quando. Sem isso, “rastrear até a compra” não existe. opinião
- **Envio da venda às plataformas:** CAPI Business Messaging (`Purchase` com valor, até 7 dias após a conversa) e importação offline do Google (GCLID + valor). oficial
- **QA de tracking** com checklist assinado antes de publicar, e **aprovação formal** do cliente de orçamento (D0), criativos (D5) e entrega (D7). mercado
- **LGPD:** aviso de privacidade na landing, banner de consentimento, base legal para enviar telefone com hash às plataformas, retenção e exclusão no CRM. oficial mercado
- **Rotina e relatório** (seção 7). mercado

Primeiras ações

1. **Hoje (D1):** troque a Evolution API por Cloud API ou coexistência no número que recebe anúncios e conecte ao Chatwoot. opinião
2. **Hoje (D1):** confirme a Política de Comércio do WhatsApp sobre álcool antes de montar o catálogo nativo. Plano B: cardápio por link ou imagem.
3. **D1:** dispare em paralelo todas as verificações (empresa, domínio, anunciante Google, nome de exibição, Perfil da Empresa). São os únicos passos fora do seu controle. mercado
4. **D2 a D4:** feche o bloco único de rastreio com dois eventos de negócio, `LeadSubmitted` e `Purchase`, e um processo de marcação no CRM.
5. **D5:** QA com checklist e aceite do cliente. **D6:** publicar. **D7:** relatório de setup e reunião explicando que as próximas 2 a 4 semanas são de aprendizado.
6. **Padronize** as três tabelas como template da Ativos para os próximos clientes, trocando apenas o bloco de compliance por segmento, como decidido na reunião. opinião

## 10. Ressalvas e fontes

- **Fontes oficiais não abertas na pesquisa:** as políticas de álcool da Meta (transparency.meta.com) e do Google (support.google.com/adspolicy/answer/6012382), a Política de Comércio do WhatsApp, a documentação da Conversions API for Business Messaging, a Lei 9.294/96 e o Anexo P do CONAR. Confirme o texto literal, sobretudo: se o Brasil aparece explicitamente com 18+, a lista atual de eventos aceitos para Business Messaging e o alcance da proibição de álcool no catálogo do WhatsApp.
- **Limiares numéricos** (\~50 eventos em 7 dias na Meta; \~15 conversões em 30 dias no Google) são referências das plataformas e mudam com o tempo. O Google hoje diz que não há mínimo estrito e só recomenda volume.
- **Tempos estimados** são de mercado e opinião para uma equipe enxuta.
- **Escolhas minhas nesta página:** quais tarefas agrupei nos Gantts, o que ficou em coral e a escolha dos diagramas. O conteúdo vem do documento.

Fontes do documento (o original as lista só como “Google Drive”; descrevi cada uma pelo ponto em que é citada): \[1\] Google Drive (relatório de ranking local), \[2\] [Google Drive (reunião de 23/11)](https://drive.google.com/open?id=1GiH5aDcNG4_EaHPE3JhzQJd_J8PjfcEk-OOo3nkzT9w), \[3\] [Google Drive (CLI-004)](https://drive.google.com/open?id=1hh_yUJtKQfaVLVzPpHH9bVd4fpHJAx9kzsXN2WfYWzs), \[4\] [Google Drive (GM-03.1, CAPI)](https://drive.google.com/open?id=1p5xEOlAvcpD_4sivXz-Y1gLfLnWLvqe-jdJ_H6Mnzok), \[5\] [Google Drive (LGPD)](https://drive.google.com/open?id=1wOe-ipXDQPOd_xUnJppHlYWOR6sGAppfACdTZefu6cY).

Diagramas no sistema de design do repositório cathrynlavery/diagram-design (licença MIT): Steps, Architecture, Gantt e Tree, com as cores do tema desta página e textos em português. Verificação: os cinco diagramas passaram no self_check e no verify_geometry do repositório.