---
tipo: cópia de contexto (pesquisa do Igor, texto integral)
original: Drive ATIVOS › 20 Clientes › CLI-004 Guto Bebidas › 03 Entregas › Tráfego
link: https://docs.google.com/document/d/1RrAzI-YUyEzKTwUHe0gMC46oxBDYpPY-n7jsi02NPGc/edit
copiado: 24/11/2026
regra: cópia integral; sem contato, CPF, CNPJ, senha nem acesso. Afirmações marcadas "verificar" pelo autor precisam de conferência no texto oficial antes de ir para proposta ou contrato
---

# Setup de Gestão de Tráfego (Meta Ads + Google Ads) para negócio local com foco em WhatsApp — SOP de 7 dias aplicado à Guto Bebidas

Seu mapa está certo na ordem geral. O que ele deixa de fora decide o resultado. Ainda não há coleta formal de acessos e verificações, nem aprovação de orçamento e criativos pelo cliente, nem QA de tracking antes de publicar. Também falta resolver o bloqueio central do objetivo de rastrear o lead até a compra: sem a WhatsApp Business Platform (API oficial) e um CRM que registre a venda, não há como devolver "compra" à Meta ou ao Google. Para a Guto Bebidas, as regras de álcool mudam o setup desde o D1: idade mínima de 18 anos, advertências do CONAR nos criativos e risco de o catálogo de bebidas no WhatsApp ser recusado.

## TL;DR

- **Confirma:** a sequência estrutura → benchmark → estratégia → criativos → rastreio → campanhas → remarketing (Meta) e concorrentes → palavras-chave → correspondência → configuração → ativos → URL/UTMs (Google) bate com a lógica das documentações e das agências. A decisão da reunião de 23/11 de montar um "bloco único de rastreio" (GTM + GA4 + pixel + tag Google Ads + UTMs) compartilhado pelos dois canais também está correta.\[1\]\[2\]
- **Corrige:** o rastreio vem antes dos criativos ficarem prontos, não depois. A estrutura recomendada para orçamento pequeno é 1 campanha com 1 a 2 conjuntos no Meta e 1 campanha de Pesquisa com 2 a 3 grupos no Google, e não "muitos públicos". E a Evolution API, prevista para o SDR, não entrega o `ctwa_clid` oficial e impede a API de Conversões para mensagens.\[2\]
- **Falta:** D0 de contrato e acessos, verificações (empresa, domínio, anunciante Google, nome de exibição do WhatsApp), compliance de álcool, aprovação do cliente, QA de tracking, CRM com etapas e valor da venda, upload de conversões offline, rotina diária, semanal e mensal, e relatório.

## Key Findings

**Legenda usada em todo o relatório:** **[Oficial]** = documentação ou política da Meta, do Google, lei ou CONAR. **[Mercado]** = prática consolidada de agências e ferramentas. **[Opinião]** = recomendação minha para o seu caso.

**Nota de método (importante):** nesta sessão não consegui abrir as páginas oficiais da Meta e do Google para conferir o texto literal. As afirmações **[Oficial]** vêm de dois lugares. Uma parte vem dos documentos técnicos internos da Ativos no Drive (GM-03.1 CAPI, GM-09.3 Events Manager/EMQ, GM-09.4 Auditoria de mídia paga), que já citam a documentação oficial. A outra parte é conhecimento consolidado das políticas. Antes de usar como padrão da agência, reabra os links oficiais listados em Caveats.

1. **Bebidas alcoólicas mudam o setup.** **[Oficial]** A Meta exige que anúncios de álcool sigam as leis locais e usem segmentação por idade e país compatível com elas. No Brasil isso significa 18+. O Google classifica álcool como conteúdo "restrito": os anúncios não podem ser mostrados para menores de idade nem retratar consumo excessivo. A Lei 9.294/96 restringe a propaganda de bebidas acima de 13 °GL (destilados). O CONAR (Anexo P) vale para todas as bebidas alcoólicas, inclusive cerveja, e exige cláusula de advertência ("Beba com moderação", "Se beber, não dirija", "Venda e consumo proibidos para menores de 18 anos").
2. **Risco de catálogo no WhatsApp.** **[Oficial, verificar]** A Política de Comércio do WhatsApp lista álcool entre os itens que não podem ser transacionados pelos recursos de comércio (catálogo e carrinho). A tarefa "configurar o cardápio no WhatsApp Business", atribuída ao Hugo, pode ser rejeitada ou derrubar o catálogo.\[2\]\[3\] **[Opinião]** Use o cardápio como link (landing page ou cardápio digital) ou como imagem/PDF enviado pelo SDR, e não como catálogo nativo, até confirmar.
3. **Rastreamento de WhatsApp: o estado da arte é o CTWA com a API de Conversões para Business Messaging.** **[Oficial]** O evento vai com `action_source: "business_messaging"`, `messaging_channel: "whatsapp"` e o `ctwa_clid` (ID do clique no anúncio).\[4\] O `ctwa_clid` chega pelo webhook da WhatsApp Business Platform no objeto `referral` da primeira mensagem. A janela de `event_time` é de até 7 dias, e a deduplicação usa `event_name` + `event_id` em até 48 h (doc interna GM-03.1).\[4\] **Sem a API oficial (Cloud API, BSP ou "coexistência" com o app), não existe `ctwa_clid`.** A Evolution API citada na reunião não serve para isso.\[2\]
4. **Google: o lead do WhatsApp só vira "compra" com o GCLID guardado.** **[Oficial]** O Google Ads Help (answer/15713840, citado na doc interna GM-09.4) afirma: "Starting June 15, 2026, offline conversions import and enhanced conversions for leads uploads will be migrated to the Data Manager API and blocked in the Google Ads API" (endpoint `POST https://datamanager.googleapis.com/v1/events:ingest`). Para um negócio pequeno, o caminho prático continua sendo a importação por planilha, Google Sheets ou conector de CRM. Segundo a PPC Land (Luís Rijo, 10/abr/2026, citada na GM-09.4), "enhanced conversions for web and for leads will be merged into a single on/off feature starting in June 2026".
5. **Orçamento pequeno: concentrar.** **[Oficial]** A Meta diz que o conjunto sai do aprendizado com cerca de 50 eventos de otimização em 7 dias após a última edição relevante. **[Mercado]** Com verba de negócio local, isso só acontece otimizando para *conversas*, não para *compras*. Daí 1 campanha, 1 a 2 conjuntos e 3 a 6 anúncios ativos.

## Tabela 1 — Meta Ads (Click-to-WhatsApp) · setup em 7 dias

D0 = assinatura e kickoff; D1 a D7 = dias corridos do prazo combinado (23/11 a 29/11).

| Etapa | Tarefa | Subtarefas | Entrada necessária | Entregável | Papel responsável | Tempo estimado | Ferramentas | Depende de | Critério de "pronto" |
|---|---|---|---|---|---|---|---|---|---|
| 0. Kickoff e briefing (D0–D1) | Alinhar objetivo, oferta e KPIs | Ticket médio, margem, raio de entrega, horários, mix (cerveja, destilados, gelo, carvão), sazonalidade (fim de ano, jogos), orçamento mensal de mídia, meta de conversas e vendas, quem atende o WhatsApp | Contrato assinado; formulário de briefing | Briefing + plano de mídia de 1 página com orçamento aprovado por escrito | Gestor de tráfego + cliente | 1–2 h | Formulário, Google Docs | — | Cliente aprovou orçamento, KPIs e raio por escrito (WhatsApp/e-mail) **[Mercado]** |
| 1. Acessos e ativos (D1) | Coleta de acessos | Página do FB (criar ou recuperar), Instagram profissional, conta de anúncios do cliente no Portfólio Empresarial (BM) do cliente com a Ativos como parceira, forma de pagamento do cliente, 2FA, acesso ao domínio/DNS | Logins do cliente, CNPJ, cartão | Checklist de acessos 100% verde | Cliente (concede) + gestor (valida) | 2–4 h (cliente costuma atrasar) | Meta Business Suite, Gerenciador de Negócios | 0 | Agência é parceira com acesso total à página, IG, conta de anúncios e dataset; conta de anúncios **pertence ao cliente** **[Mercado]** |
| 2. Verificações e compliance (D1–D2) | Verificar empresa, domínio e conformidade de álcool | Verificação da empresa (CNPJ); verificação de domínio (DNS TXT ou meta-tag); restrição de idade 18+ na página e no IG; revisar Política de Comércio do WhatsApp (catálogo); checklist CONAR | CNPJ, documento, DNS da LP | Empresa e domínio verificados; página 18+ | Gestor + cliente | 1 h de trabalho; verificação pode levar dias | Central de Segurança do BM | 1 | Domínio verificado no BM; idade mínima 18 configurada **[Oficial]** |
| 3. WhatsApp Business Platform (D1–D3) | Conectar o número ao anúncio e à API | Decidir entre app + coexistência ou Cloud API via BSP; criar WABA; aprovar nome de exibição; vincular número à página; ativar webhook (captura do `referral`/`ctwa_clid`); conectar ao Chatwoot/CRM | Número do cliente, acesso ao celular para OTP | Número ativo na WABA ligado à página e ao Chatwoot | Gestor + infra (Bernardo) | 3–6 h + espera de aprovação | WhatsApp Manager, BSP ou Cloud API, Chatwoot | 1, 2 | Mensagem de teste vinda de anúncio chega ao Chatwoot com `referral`/`ctwa_clid` registrado **[Oficial]** |
| 4. Benchmark (D1–D2) | Pesquisa de concorrentes | Biblioteca de Anúncios (filtrar BH, "distribuidora", "delivery de bebidas"); anotar ganchos, ofertas, formatos, CTA; perfis do Google Meu Negócio da grade de ranking (Hudsons Beer, Castelo etc.)\[1\] | Lista de concorrentes (relatório de ranking local já existe no Drive)\[1\] | Swipe file com 10–20 anúncios + 3 ângulos de comunicação | Gestor de tráfego | 2–3 h | Biblioteca de Anúncios, Drive | 0 | 3 ângulos priorizados aprovados internamente **[Mercado]** |
| 5. Estratégia e públicos (D2) | Desenhar estrutura | Objetivo Engajamento ou Vendas com local de conversão WhatsApp; 1 campanha; 1–2 conjuntos (raio de entrega + 18+, público amplo/Advantage+; opcional 1 conjunto de remarketing quando houver volume); orçamento por conjunto; nomenclatura; janela de aprendizado | Briefing, benchmark, orçamento | Documento de estrutura + mensagem de boas-vindas pré-preenchida | Gestor de tráfego | 2 h | Gerenciador de Anúncios, planilha | 0, 4 | Estrutura cabe no orçamento (≥ ~50 conversas/semana por conjunto ou consolidar) **[Mercado/Opinião]** |
| 6. Roteiro e briefing criativo (D2) | Transformar ângulos em peças | Roteiros de 3 vídeos (gancho em 3 s, oferta, CTA "chama no WhatsApp"), 3 estáticos, 3 carrosséis; texto com advertência CONAR; modelos aparentando 25+; sem consumo excessivo, direção ou menores | Benchmark, fotos e vídeos do cliente | Briefing por peça | Gestor + designer + videomaker | 2–3 h | Docs, Canva/Figma | 4, 5 | Cada peça tem gancho, oferta, CTA e advertência **[Oficial CONAR + Mercado]** |
| 7. Produção de criativos (D3–D4) | Produzir as 9 peças (lote 1) | Captação na loja (geladeira, entrega, preço); edição 9:16 e 4:5; legendas; variações de texto | Briefing, material do cliente | 9 peças nos formatos 9:16, 1:1 e 4:5 | Designer + videomaker | 1,5–2 dias | CapCut, Canva, Higgsfield | 6 | Peças revisadas contra a política de álcool da Meta e o CONAR **[Mercado]** |
| 8. Rastreio (D2–D4, em paralelo aos criativos) | Bloco único de rastreio | Pixel/dataset; GTM na LP; eventos `Contact`/`clique_whatsapp`; UTMs padrão; GA4; CAPI web; **CAPI para Business Messaging** com `LeadSubmitted` (lead qualificado) e `Purchase` (venda com valor) a partir do CRM | Acesso à LP, WABA, Chatwoot/CRM | Mapa de eventos + tags publicadas | Gestor (tracking) + Bernardo (infra) | 1 dia | GTM, GA4, Events Manager, Chatwoot, n8n/Python | 1, 3 | Eventos aparecem em Test Events e não são duplicados **[Oficial]**\[4\] |
| 9. Processo comercial no CRM (D3–D4) | Etapas do lead até a compra | Funil: conversa iniciada → qualificado → pedido → pago; campo valor da venda; etiqueta "origem: anúncio" (com `ctwa_clid`); script do SDR/atendente para marcar a venda | Chatwoot configurado, atendente treinado | Funil no CRM + rotina de marcação | Gestor + cliente (atendimento) + Hugo (SDR) | 3–4 h + treino de 30 min | Chatwoot, planilha ou CRM | 3, 8 | Atendente marca a venda com valor em 100% dos testes **[Opinião]** |
| 10. Aprovação do cliente (D5) | Aprovar criativos e textos | Enviar grade de peças; 1 rodada de ajustes; aceite formal | Peças finais | Aceite por escrito | Cliente | 0,5 dia (SLA de 24 h) | WhatsApp, Drive | 7 | "Aprovado" registrado **[Mercado]** |
| 11. QA de tracking e anúncio (D5) | Testes de ponta a ponta | Clicar no anúncio em pré-visualização ou com orçamento mínimo; conferir abertura do WhatsApp com mensagem pré-preenchida; `ctwa_clid` no CRM; evento de teste no Events Manager; UTMs no GA4 | Itens 8 e 9 prontos | Checklist de QA assinado | Gestor de tráfego | 2–3 h | Test Events, Pixel Helper, GA4 DebugView | 8, 9 | 100% dos itens do checklist OK **[Mercado]** |
| 12. Subir campanhas (D6) | Publicar | Criar campanha; 1–2 conjuntos; 6–9 anúncios; revisar política; programar início | Aprovação + QA | Campanhas ativas | Gestor de tráfego | 2 h + revisão da Meta (geralmente até 24 h) | Gerenciador de Anúncios | 10, 11 | Anúncios "Ativos", sem reprovação **[Oficial]** |
| 13. Remarketing (planejado no D6, ativa ~D14–D30) | Públicos personalizados | Engajou IG/FB 30–90 dias, visitantes da LP, quem conversou no WhatsApp; excluir compradores recentes | Volume mínimo de público | Conjunto de remarketing | Gestor | 1 h | Públicos do Gerenciador | 12 | Público com tamanho suficiente para entregar **[Mercado]** |
| 14. Entrega D7 | Relatório de setup | Prints das estruturas, mapa de eventos, acessos, próximos passos, expectativa de aprendizado (2–4 semanas) | Tudo acima | Relatório de entrega + reunião de 30 min | Gestor + cliente | 1–2 h | Looker Studio, Docs | 12 | Cliente assina o aceite do setup **[Mercado]** |

## Tabela 2 — Google Ads (Rede de Pesquisa local) · setup em 7 dias

| Etapa | Tarefa | Subtarefas | Entrada necessária | Entregável | Papel responsável | Tempo estimado | Ferramentas | Depende de | Critério de "pronto" |
|---|---|---|---|---|---|---|---|---|---|
| 0. Acessos e conta (D1) | Conta, MCC e faturamento | Criar ou acessar a conta do cliente; vincular à MCC da Ativos; pagamento do cliente; iniciar **verificação do anunciante** | Login Google do cliente, CNPJ, cartão | Conta vinculada à MCC | Cliente + gestor | 1–2 h + verificação (pode levar dias) | Google Ads, MCC | Briefing Meta (0) | Conta ativa com faturamento; verificação enviada **[Oficial]** |
| 1. Compliance de álcool (D1) | Checar política "Álcool" | Política Google para o Brasil; palavras e textos sem apelo a consumo excessivo; excluir menores (padrão da política); revisar LP (aviso 18+) | Política, LP | Checklist de compliance | Gestor | 1 h | Central de Políticas | 0 | LP e textos sem violações óbvias **[Oficial]** |
| 2. Análise de concorrentes (D1–D2) | Leilão e mensagens | Buscar termos em BH (anônimo); Centro de Transparência de Anúncios; anotar títulos, ofertas, extensões; comparar com GMB (ranking local do Drive) | Lista de concorrentes | Quadro de ofertas e USPs | Gestor | 1–2 h | Centro de Transparência de Anúncios, SERP | 0 | 3 diferenciais definidos **[Mercado]** |
| 3. Palavras-chave (D2) | Pesquisa e agrupamento | Planejador (BH + raio); clusters: "distribuidora de bebidas [bairro/perto de mim]", "delivery de bebidas/cerveja", "gelo/carvão", marca; lista de negativas (emprego, atacado de outra cidade, "como fazer", grátis) | Acesso à conta | Planilha com 2–3 grupos e 30–60 termos + negativas | Gestor | 2–3 h | Planejador de palavras-chave | 0 | Cada grupo tem intenção única **[Mercado]** |
| 4. Correspondências (D2) | Definir tipos | Frase e exata no início; ampla só com lance inteligente e dados de conversão; negativas no nível da conta | Planilha da etapa 3 | Lista final por tipo | Gestor | 1 h | Google Ads Editor | 3 | Sem sobreposição relevante entre grupos **[Mercado]** |
| 5. Rastreio (D2–D4, bloco único) | Conversões e consentimento | Auto-tagging ON; Google tag via GTM; conversão primária "clique no WhatsApp" na LP; captura e persistência do GCLID na LP, enviado ao WhatsApp/CRM (ID curto na mensagem pré-preenchida); Enhanced Conversions (toggle único); vincular GA4; banner de consentimento (LGPD/Consent Mode) | GTM, LP, CRM | Ações de conversão primárias e secundárias configuradas | Gestor + Bernardo | 0,5–1 dia | GTM, GA4, Google Ads | 0 | Tag Assistant OK; conversão de teste registrada **[Oficial]** |
| 6. Configuração da campanha (D3) | Campanha de Pesquisa | Só Rede de Pesquisa (desmarcar Display e parceiros); local "presença" (não "interesse"); raio de entrega; programação no horário de atendimento do WhatsApp; orçamento diário; lance inicial Maximizar cliques com limite de CPC **ou** Maximizar conversões | Itens 3, 4 e 5 | Campanha em rascunho | Gestor | 1–2 h | Google Ads | 3–5 | Revisão cruzada feita por outra pessoa **[Mercado]** |
| 7. Anúncios e ativos (D3–D4) | RSAs e ativos | 2 RSAs por grupo (15 títulos, 4 descrições); sitelinks; frases de destaque; ativo de local (vincular o Perfil da Empresa); ativo de chamada; imagens; logo | Fotos do cliente, GMB verificado | Anúncios em rascunho | Gestor + designer (imagens) | 2–3 h | Google Ads | 6, GMB (Henrique) | Força do anúncio "Boa" ou "Excelente" **[Oficial]** |
| 8. URL final e UTMs (D4) | Padronizar | Final URL = LP; sufixo de URL com UTMs; testar o redirecionamento do botão para wa.me com GCLID/ID | LP no domínio final | Template de rastreamento | Gestor | 30 min | Google Ads, GA4 | 5 | Sessões com `google / cpc` no GA4 **[Mercado]** |
| 9. Aprovação do cliente + QA (D5) | Aceite e testes | Aprovar textos; teste de clique real; conferir conversão e GCLID no CRM | Itens 5–8 | Checklist de QA + aceite | Cliente + gestor | 1–2 h | Tag Assistant | 5–8 | Todos os testes OK **[Mercado]** |
| 10. Campanha no ar (D6) | Publicar | Ativar; acompanhar a revisão (álcool pode ficar "Qualificado (limitado)") | QA OK | Campanha ativa | Gestor | 30 min + revisão (geralmente ~1 dia útil) | Google Ads | 9 | Status "Qualificado" com impressões **[Oficial]** |
| 11. Conversões offline (D7 → rotina) | Fechar o loop | Planilha ou Sheets com GCLID, data e valor da venda; importação programada (diária ou semanal); a médio prazo, conector de CRM/Data Manager API | CRM com GCLID e valor | Ação "Venda WhatsApp (offline)" | Gestor + atendimento do cliente | 2 h de setup + 15 min/semana | Google Ads (Uploads), Sheets | 5, CRM | Primeira importação aceita sem erro **[Oficial]** |

## Tabela 3 — Rotina recorrente do gestor (pós-setup)

| Frequência | Tarefa | O que olhar / fazer | Critério de ação | Fonte |
|---|---|---|---|---|
| Diária (10–15 min por cliente) | Checagem de saúde | Gasto vs. orçamento, anúncios reprovados, conta ou pagamento com problema, conversas recebidas, tag/dataset com erro | Reprovou → corrigir no mesmo dia; gasto 0 → investigar | **[Mercado]** |
| Diária | Qualidade das conversas | Amostra de conversas no Chatwoot: tempo de resposta, SDR respondendo certo, conversas de menores ou fora do raio | Tempo de resposta > 5 min → alinhar atendimento | **[Opinião]** |
| Diária / a cada 2 dias | Marcação de vendas no CRM | Garantir que toda venda tem valor e origem | Venda sem origem → cobrar o atendimento | **[Opinião]** |
| Semanal (1–2 h) | Otimização Meta | CPA por conversa, CTR, frequência, CPM; pausar anúncios fracos só após ~3–7 dias com gasto relevante; sem edições grandes durante o aprendizado | Frequência > 3 ou CTR caindo → novos criativos | **[Oficial + Mercado]** |
| Semanal | Otimização Google | Relatório de termos de pesquisa → negativas; parcela de impressões perdida (orçamento vs. ranking); horários e dias | Termo irrelevante com gasto → negativar | **[Oficial + Mercado]** |
| Semanal | Envio de conversões | CAPI Business Messaging (automático) e upload offline do Google | Upload com erro → corrigir na semana | **[Oficial]** |
| Semanal | Report curto ao cliente | Conversas, custo por conversa, vendas atribuídas, receita, 3 próximos passos | — | **[Mercado]** |
| Quinzenal | Ciclo de criativos | 2–4 peças novas (variações dos vencedores + 1 ângulo novo) | Criativo vencedor com fadiga | **[Mercado]** |
| Mensal (2–3 h) | Relatório e reunião | Investimento, conversas, vendas, ROAS real (CRM), CAC, comparação com o mês anterior, testes do próximo mês | Mudança de estratégia só com dados de 30 dias | **[Mercado]** |
| Mensal | Auditoria de tracking | Eventos, deduplicação, EMQ, GCLID no CRM, UTMs "Unassigned" no GA4 | Gap anormal Meta vs. CRM → investigar | **[Mercado]** |
| Mensal | Estratégia de lance (Google) | Ao acumular conversões suficientes, migrar para Maximizar conversões ou CPA desejado | ~15+ conversões/30 dias como referência | **[Oficial/Mercado]** |
| Trimestral | Revisão de oferta e sazonalidade | Calendário (Carnaval, jogos, verão, fim de ano), revisar raio e orçamento | — | **[Opinião]** |

## Details

### (a) O que confirma o seu mapa

- **Ordem página → BM → benchmark → estratégia → criativos → campanhas → remarketing** é o fluxo que a Meta usa nos cursos de anúncios para negócios locais e que as agências usam como SOP. **[Mercado]**
- **Mínimo de 3 vídeos, 3 fotos e 3 carrosséis** é um primeiro lote razoável.\[2\]\[3\] A Meta recomenda variar formatos para os posicionamentos (Reels/Stories 9:16 e Feed 4:5). Nove peças bastam para 1 a 2 conjuntos. **[Mercado]**
- **Google: concorrentes → palavras-chave → correspondência → rede de pesquisa, raio, horário e orçamento → ativos → URL/UTMs** está correto para negócio local. Raio, horário e só a Rede de Pesquisa são boas práticas das ferramentas do Google. **[Oficial/Mercado]**
- **"Bloco único de rastreio"**: correto. As anotações do Gemini da reunião de 23/11/2026 registram que "Henrique Horta estabeleceu prazos fixos de 7 dias para tráfego pago, Google Meu Negócio e landing pages, além de 15 dias para automação comercial com agente SDR" e que "ficou decidido unificar o rastreamento do Google Ads em um bloco único com GTM e Analytics". GTM, GA4, pixel, tag do Google Ads e UTMs são infraestrutura compartilhada, configurada uma vez e usada pelos dois canais. **[Mercado]**
- **Prazo de 7 dias para o setup:** viável, desde que o cliente libere acessos no D1 e aprove no D5.\[2\] Não é "aquecimento" da conta. O aprendizado de verdade começa após a publicação (D6) e leva semanas. **[Oficial: fase de aprendizado; Opinião: comunicar isso ao cliente]**

### (b) O que corrige

1. **"Aquecimento de conta" ≠ aprendizado.** Na reunião, o prazo de 7 dias foi descrito como período em que "a Meta tateia o público".\[2\] **[Oficial]** O aprendizado só começa quando o conjunto entrega, e a referência é ~50 eventos de otimização em 7 dias. Com verba local, otimize para *conversas* (volume alto). Só passe a otimizar para *compras* quando houver dezenas de vendas por semana enviadas pela CAPI. **[Opinião]**
2. **O rastreio não é a etapa 6, depois dos criativos.** Ele roda em paralelo, de D2 a D4, porque depende de infraestrutura (WABA, webhook, CRM) que leva mais tempo que os criativos. **[Mercado]**
3. **A Evolution API não serve para rastrear leads de anúncio.** É uma integração não oficial: não recebe o `referral`/`ctwa_clid` oficial, não permite enviar eventos à CAPI de Business Messaging e traz risco de banimento do número.\[4\] Para o rastreio, use Cloud API (direto ou via BSP) ou a coexistência do app WhatsApp Business com a plataforma. **[Oficial: requisitos da CAPI/WABA; Opinião: avaliação de risco]**
4. **"Estratégia e públicos" com muitos públicos.** Com orçamento pequeno, fragmentar em interesses pulveriza o aprendizado. Prefira raio + 18+ com público amplo e deixe o criativo segmentar. **[Mercado]**
5. **Remarketing no D7.** Ele só ganha escala depois de 2 a 4 semanas de público acumulado. Planeje no setup e ative quando houver tamanho. **[Mercado]**
6. **Google sem conversão configurada.** O seu mapa do Google só tem "site e UTMs".\[3\] Sem conversão primária (clique no WhatsApp) e sem GCLID no CRM, não há lance inteligente nem atribuição de venda. **[Oficial]**
7. **Performance Max no início: não.** Sem histórico de conversões e com verba pequena, o PMax tende a gastar em inventário de baixa intenção (Display, YouTube). Comece com Pesquisa e reavalie depois de ~30 conversões. **[Mercado/Opinião]**

### (c) O que falta

- **D0 de contrato e acessos:** checklist de acessos com a conta de anúncios do cliente, a agência como parceira, pagamento no nome do cliente e 2FA. **[Mercado]**
- **Verificações que podem estourar o prazo:** verificação da empresa e do domínio (Meta), verificação de anunciante (Google), nome de exibição do WhatsApp e verificação do Perfil da Empresa no Google. O plano de 7 dias do Google Meu Negócio da Guto Bebidas, no Drive, alerta que "a análise do vídeo pode levar até 5 dias úteis, e o cartão-postal até 14". **[Oficial]**
- **Compliance de álcool:** 18+ nos conjuntos (a Meta pode impor automaticamente), página e IG com restrição de idade, advertência do CONAR em todas as peças, modelos adultos e nada de associar bebida a direção. **[Oficial]**
- **CRM e definição de "venda":** etapas, campo de valor, quem marca e quando. Sem isso, "rastrear até a compra" não existe. **[Opinião]**
- **Envio da venda às plataformas:** CAPI Business Messaging (`Purchase` com `value` e `currency: BRL`, até 7 dias após a conversa)\[4\] e importação offline do Google (GCLID + valor). **[Oficial]**
- **QA de tracking com checklist assinado** antes de publicar. **[Mercado]**
- **Aprovação formal do cliente** de orçamento (D0), criativos (D5) e entrega (D7). **[Mercado]**
- **LGPD:** aviso de privacidade na LP, banner de consentimento, base legal para enviar telefone com hash às plataformas, e retenção e exclusão no CRM.\[5\] **[Oficial: LGPD; Mercado: implementação]**
- **Rotina e relatório** (Tabela 3). **[Mercado]**

### Arquitetura de rastreamento recomendada (Guto Bebidas)

1. **Anúncio CTWA (Meta)** → o cliente abre o WhatsApp com mensagem pré-preenchida → o webhook da Cloud API recebe o `referral` com `ctwa_clid`, ID do anúncio e campanha → o Chatwoot cria o contato com "origem: Meta / anúncio X". **[Oficial]**
2. **Anúncio Google (Pesquisa)** → LP → o GTM lê o GCLID e grava num cookie → o botão do WhatsApp gera mensagem pré-preenchida com um código curto (ex.: "Pedido #G7K2") → o CRM associa o código ao GCLID. **[Mercado]**
3. **Atendente/SDR marca "Pedido pago" com valor** → automação (n8n/Python) envia:
   - Meta: `Purchase` via CAPI com `action_source: business_messaging`, `messaging_channel: whatsapp`, `ctwa_clid`, `value`, `currency: BRL` e `event_id` = ID do pedido.\[4\]
   - Google: conversão offline (GCLID + horário + valor), por planilha ou API.
4. **Relatório** cruza investimento por canal com vendas do CRM, o ROAS real. **[Opinião]**

### Estrutura de campanha recomendada para orçamento pequeno

- **Meta [Mercado/Opinião]:** 1 campanha (Engajamento ou Vendas → WhatsApp), 1 conjunto principal com raio de entrega e 18+ e público amplo, e um 2º conjunto opcional só se o orçamento suportar ~50 conversas/semana em cada. Use 6 a 9 anúncios no lançamento e mantenha 3 a 6 ativos. Faça testes de criativo dentro do mesmo conjunto, trocando 2 a 4 peças a cada 2 semanas. Orçamento: o mínimo que gere volume de conversas; se o custo por conversa no benchmark for R$ 5–15, R$ 30–50/dia por conjunto é um piso realista.
- **Google [Mercado/Opinião]:** 1 campanha de Pesquisa, 2 a 3 grupos (distribuidora/perto de mim · delivery de bebidas/cerveja · gelo/carvão/marca), correspondência de frase e exata, raio de entrega, horário do atendimento. Comece com Maximizar cliques com teto de CPC ou Maximizar conversões. Migre para CPA desejado com ~15+ conversões em 30 dias.
- **Volume criativo realista por ciclo [Mercado]:** lote inicial de 9 peças; depois 2 a 4 novas a cada 2 semanas (6 a 8 por mês), priorizando variações do vencedor (novo gancho nos 3 primeiros segundos, nova oferta, novo formato).

## Recommendations

1. **Hoje (D1):** troque a premissa da Evolution API, *para o número que recebe anúncios*, por Cloud API ou coexistência e conecte ao Chatwoot. Pela reunião de 23/11, "o Hugo assume a implementação e o treinamento do SDR de IA no WhatsApp, enquanto o Bernardo é responsável pela infraestrutura de dados", com o SDR "utilizando modelo em Python"; a troca de conector cabe a eles. Sem isso, o diferencial "rastrear até a compra" que vocês venderam não se sustenta. **[Opinião, decisiva]**
2. **Hoje (D1):** confirme a Política de Comércio do WhatsApp sobre álcool antes de o Hugo montar o catálogo nativo. Plano B: cardápio por link ou imagem. **[Opinião]**
3. **D1:** dispare em paralelo todas as verificações (empresa, domínio, anunciante Google, nome de exibição, GMB). São os únicos passos fora do seu controle. **[Mercado]**
4. **D2–D4:** feche o "bloco único de rastreio" com dois eventos de negócio, `LeadSubmitted` (lead qualificado) e `Purchase` (venda com valor), e um processo de marcação no CRM. **[Opinião]**
5. **D5:** QA com checklist e aceite do cliente. **D6:** publicar. **D7:** relatório de setup e reunião explicando que as próximas 2 a 4 semanas são de aprendizado. **[Mercado]**
6. **Padronize** as três tabelas acima como template da Ativos para os próximos clientes, que foi a decisão da reunião.\[2\]\[3\] Troque apenas o bloco de compliance por segmento. **[Opinião]**

## Caveats

- **Verificação de fontes:** as políticas de álcool (Meta: transparency.meta.com → Padrões de Publicidade → Álcool; Google: support.google.com/adspolicy/answer/6012382), a Política de Comércio do WhatsApp, a doc da Conversions API for Business Messaging (developers.facebook.com), a Lei 9.294/96 (planalto.gov.br) e o Anexo P do CONAR não foram abertos nesta sessão. Confirme o texto literal, sobretudo: (i) se o Brasil aparece explicitamente com 18+; (ii) a lista atual de eventos aceitos para Business Messaging; (iii) o alcance da proibição de álcool no catálogo do WhatsApp.
- **Limiares numéricos** (~50 eventos/7 dias na Meta; ~15 conversões/30 dias no Google) são referências das plataformas que mudam com o tempo. O Google hoje diz que não há mínimo estrito e só recomenda volume.
- **Tempos estimados** são de mercado e opinião para uma equipe enxuta. Aprovações (Meta, Google, verificação de empresa, GMB) podem passar do D7. Combine com o cliente que a entrega do D7 é "setup pronto e campanhas publicadas ou em revisão".
- **Atribuição nunca bate 100%:** espere diferença entre Meta, Google e CRM. O número de decisão é a venda registrada no CRM. A doc interna GM-09.3 cita o Varos Industry Benchmark (2024, via EasyInsights): "Meta reports 26% higher conversions on average compared to analytics tools, due to modeled conversions and last-event attribution". É benchmark de mercado, não lei.

## Fontes

1. Google Drive
2. [Google Drive](https://drive.google.com/open?id=1GiH5aDcNG4_EaHPE3JhzQJd_J8PjfcEk-OOo3nkzT9w)
3. [Google Drive](https://drive.google.com/open?id=1hh_yUJtKQfaVLVzPpHH9bVd4fpHJAx9kzsXN2WfYWzs)
4. [Google Drive](https://drive.google.com/open?id=1p5xEOlAvcpD_4sivXz-Y1gLfLnWLvqe-jdJ_H6Mnzok)
5. [Google Drive](https://drive.google.com/open?id=1wOe-ipXDQPOd_xUnJppHlYWOR6sGAppfACdTZefu6cY)
