---
tipo: cópia de contexto (pesquisa do Igor, texto integral)
original: Drive ATIVOS › 20 Clientes › CLI-004 Guto Bebidas › 03 Entregas › Automação
link: https://docs.google.com/document/d/1ueIUIZqfFMH8C23--8JoaEK2y6BfwJziv7M7DGDmpqg/edit
copiado: 24/11/2026
regra: cópia integral; sem contato, CPF, CNPJ, senha nem acesso. Afirmações marcadas "verificar" pelo autor precisam de conferência no texto oficial antes de ir para proposta ou contrato
---

# SDR de IA no WhatsApp para a Guto Bebidas: plano de implantação, o que o seu mapa acerta e o que falta

Seu mapa acerta o fluxo de conversa, mas faltam três frentes antes do go-live, e são justamente as que podem derrubar o projeto: a escolha do canal (API oficial ou conexão não oficial), as regras do negócio (incluindo a idade mínima, obrigatória para bebida alcoólica) e a operação pós-lançamento. Em 7 dias, o realista é entregar um piloto controlado com preço vindo só do banco de dados, verificação de idade, passagem para humano e follow-up dentro da janela de 24h. Catálogo nativo, templates de reengajamento, painel para o cliente editar preços e relatórios automáticos ficam para a fase 2.

## TL;DR

- **Seu mapa está incompleto, não errado.** O fluxo receptivo → triagem → cardápio → valores → humano é o mesmo que as plataformas de mercado usam. Faltam quatro coisas: uma etapa de discovery (FAQ, objeções, frete, área de entrega, pagamento, horário, tom de voz), a verificação de idade, um roteiro de testes com critérios de aceite e uma rotina de pós-lançamento. Também é preciso decidir o canal antes de construir. A stack que a Ativos montou (o fork do Chatwoot da Fazer.ai com Baileys, sobre Coolify na Hostinger) usa conexão não oficial, e o README da própria biblioteca Baileys avisa que ela não é afiliada ao WhatsApp, que os mantenedores não aprovam usos que violem os Termos de Serviço e que eles desencorajam "bulk or automated messaging usage".
- **Use o banco de dados próprio como fonte de preço e fotos, não o catálogo do WhatsApp Business.** Há três motivos. Pelo CDC, a oferta suficientemente precisa obriga o fornecedor, então um preço inventado pela IA vira problema jurídico. A Commerce Policy do WhatsApp restringe a venda de álcool. E o banco permite que o cliente atualize preços sem depender da Meta. A IA deve consultar o preço por ferramenta (function calling) e nunca "lembrar" valores.
- **7 dias são suficientes para um piloto, não para o produto completo.** Dias 1–2: discovery e regras. Dias 2–4: banco, prompt e integração. Dias 4–6: testes e red teaming. Dia 7: go-live em horário reduzido ou para uma parte dos contatos, com um humano de plantão. Ficam para a fase 2 (semanas 2 a 6): migração ou validação na API oficial com templates aprovados, painel de preços para o cliente, catálogo e mensagens de produto, dashboard de métricas e relatório mensal.

## Contexto interno verificado (Drive da Ativos)

O documento interno "CLI-004 Guto Bebidas – documentação de serviços e processos" (23/11/2026) registra os seguintes pontos:

- O projeto tem três entregas em 7 dias (de 23/11 a 29/11): landing page, setup de tráfego e posicionamento digital.\[1\]
- A **Automação Comercial está "Sem prazo definido", com status "A fazer"**.\[1\]
- O SDR de IA fica com o Hugo e a infraestrutura com o Bernardo. O fluxo tem 5 passos, mais as regras de follow-up e de atendimento fora do horário.\[1\]
- Implicação: o prazo de 7 dias para o SDR é uma meta interna. O próprio documento não a formaliza, e isso reforça a recomendação de entregar um piloto, não o produto final.

A reunião de 01/10/2026 (anotações do Gemini) registra três decisões e dois problemas:

- **Decisões:**
  - adotar o **fork do Chatwoot mantido pela Fazer.ai**, "com conexões nativas para o WhatsApp via Baileys, ausentes na API oficial da Meta";\[2\]
  - usar **Coolify** em **VPS Hostinger KVM2**;\[2\]
  - ter uma VPS por cliente, para isolar falhas.\[2\]
- **Problemas registrados na mesma reunião:**
  - credenciais root e de acesso foram compartilhadas em grupo de mensagens, e o cofre de senhas ficou para depois;\[2\]
  - a VPS antiga tem "chave vazada".\[2\]

  Os dois pontos são relevantes para a segurança e para a LGPD (seção d).

## Tabela de implantação

Legenda de evidência: **[D]** = prática documentada em fonte oficial, lei ou documentação de fornecedor; **[H]** = heurística de mercado ou opinião deste relatório. Os tempos são estimativas **[H]** para uma equipe de 2 a 3 pessoas e um cliente pequeno.

| Etapa | Tarefa | Subtarefas | Entrada necessária | Entregável | Papel responsável | Tempo estimado | Ferramentas | Depende de | Critério de "pronto" |
|---|---|---|---|---|---|---|---|---|---|
| 0. Decisão de canal | Escolher API oficial (Cloud API) ou conexão não oficial (Baileys/Evolution/Z-API) | Avaliar o risco de banimento do número; verificar se o número atual usa o app WhatsApp Business; checar se a coexistência app + API está disponível; estimar o custo por template | Número do cliente, acesso ao Meta Business Manager do cliente, apetite a risco | Decisão registrada e assinada pelo cliente (termo de ciência de risco, se for não oficial) | Dev/infra + sócio comercial | 0,5 dia (decisão); verificação de negócio na Meta: de dias a ~2 semanas [H] | Meta Business Manager, WhatsApp Manager, Chatwoot (inbox "WhatsApp Cloud" via embedded signup [D])\[3\] | — | Canal escolhido, número definido, cliente ciente por escrito dos riscos |
| 1. Discovery | Mapear o atendimento atual | Ler 50–100 conversas reais do WhatsApp do cliente; cronometrar o tempo de resposta atual; mapear quem atende, em que horário e como passa o pedido para a entrega | Exportação de conversas (com autorização) e entrevista de 1h com o dono e o atendente | Mapa "como é hoje" (jornada + gargalos) | Especialista em IA + atendimento | 0,5–1 dia | Planilha, export do WhatsApp, Google Docs | 0 | Pelo menos 50 conversas lidas e 5 jornadas típicas descritas |
| 1. Discovery | Levantar FAQ e objeções | Top 30 perguntas; objeções (preço, frete, demora, "tá gelada?", troco); gatilhos de desistência | Conversas do passo anterior + entrevista | Base de FAQ com respostas aprovadas pelo dono | Especialista em IA | 0,5 dia | Planilha/Notion | Mapa atual | Cada FAQ com resposta validada pelo cliente |
| 1. Discovery | Regras de negócio | Área de entrega (bairros ou CEPs, raio); frete por faixa; pedido mínimo; formas de pagamento (Pix, cartão na entrega, troco); horário; política de troca/casco; **idade mínima de 18 anos**; prazo de entrega; estoque | Dono do negócio | "Documento de regras" versionado (fonte única para o prompt e o banco) | Especialista em IA + cliente | 0,5 dia | Google Docs | Mapa atual | Todas as regras com valor numérico ou lista fechada, sem "depende" |
| 1. Discovery | Tom de voz e persona | Nome do atendente virtual; grau de informalidade; uso de emojis; palavras proibidas; se informa que é IA | Exemplos de mensagens de que o dono gosta | Guia de tom (1 página) + 10 exemplos de diálogo "ideal" | Especialista em IA | 0,25 dia | Docs | FAQ | Dono aprova os 10 exemplos |
| 1. Discovery | Métricas de sucesso e linha de base | Definir as metas: tempo da 1ª resposta, % de conversas que viram pedido, % de passagem para humano, pedidos fora do horário | Dados do "como é hoje" | Scorecard com a linha de base | Especialista em IA + comercial | 0,25 dia | Planilha | Mapa atual | Linha de base medida e metas acordadas |
| 2. Dados | Modelar o banco do cardápio | Tabelas de produto (SKU, nome, categoria, volume, preço, promoção, ativo/inativo, url_foto, teor alcoólico), frete por bairro, horário | Lista de produtos e preços do cliente; fotos | Esquema + carga inicial | Dev/infra | 0,5–1 dia | Postgres/Supabase na VPS, ou Google Sheets como fonte no piloto | Regras de negócio | 100% dos SKUs ativos com preço e foto; consulta testada |
| 2. Dados | Fotos e artes | Padronizar as imagens (JPEG/PNG, peso baixo); hospedar com URL estável | Fotos do cliente ou do fornecedor | Pasta/bucket com as imagens nomeadas por SKU | Design + dev | 0,5 dia | Storage S3-compatível / MinIO / CDN | Esquema | Toda foto ≤ 5 MB (limite de imagem da Cloud API [D]) e carregando no WhatsApp |
| 2. Dados | Atualização pelo cliente | Piloto: o cliente edita uma planilha e um sync leva ao banco. Fase 2: painel simples (NocoDB/Appsmith) com log de alterações | Pessoa do cliente responsável pelo preço | Procedimento "como alterar preço" (1 página) | Dev/infra | Piloto: 0,5 dia; painel: 2–3 dias (fase 2) | Google Sheets + n8n; NocoDB | Esquema | Cliente altera um preço e o bot responde o novo valor em ≤ 5 min |
| 3. Agente | Prompt de sistema | Papel, objetivo, limites; fluxo em estados (saudação → triagem → idade → oferta → carrinho → endereço/frete → pagamento → resumo → passagem para humano); regras "nunca" (inventar preço, prometer prazo fora da regra, vender a menor, falar de assuntos fora do escopo) | Documento de regras, guia de tom, FAQ | Prompt versionado (v1) no Git | Especialista em IA | 1 dia | LLM (GPT, conforme decisão interna de 08/10), Git\[4\] | Discovery | Prompt revisado por um segundo membro; passa no smoke test |
| 3. Agente | Ferramentas (function calling) | `buscar_produto`, `consultar_preco`, `calcular_frete(bairro)`, `enviar_foto(sku)`, `montar_resumo`, `transferir_humano(motivo)` | Banco pronto | Workflows/endpoints | Dev/infra + especialista em IA | 1 dia | n8n, API do Chatwoot | Banco | Preço e frete sempre vêm de ferramenta (zero preço "de memória" nos testes) |
| 3. Agente | Base de conhecimento | FAQ e políticas em texto curto, por tópico (RAG ou injeção no prompt, conforme o tamanho) | FAQ aprovada | KB versionada | Especialista em IA | 0,5 dia | Vetorial (pgvector) ou só o prompt | FAQ | Cada pergunta da FAQ respondida corretamente em teste |
| 3. Agente | Verificação de idade | Pergunta de confirmação de maioridade antes de ofertar álcool; recusa padrão; registro do aceite; instrução ao entregador para conferir documento na entrega | Regra jurídica + cliente | Trecho de fluxo + checklist do entregador | Especialista em IA + cliente | 0,25 dia | Prompt + campo no CRM | Prompt | 100% dos casos-limite "sou menor" recusados nos testes |
| 4. Integração | Infraestrutura na VPS | Coolify; Chatwoot; n8n; Postgres; HTTPS; firewall; usuários sem root; cofre de senhas | VPS (já contratada)\[2\] | Ambiente de produção + homologação | Dev/infra | 1 dia | Hostinger KVM2, Coolify, Docker\[2\] | 0 | Serviços com HTTPS, acesso por chave SSH, senhas fora de grupos de chat |
| 4. Integração | Conectar o WhatsApp | Oficial: app Meta, WABA, número, webhook, token permanente. Não oficial: pareamento por QR em número dedicado | Decisão da etapa 0 | Inbox ativa no Chatwoot | Dev/infra | 0,5 dia (não oficial); 1–3 dias + verificação (oficial) [H] | Chatwoot, Meta Developer | Decisão de canal | Mensagem de teste ida e volta, mídia incluída |
| 4. Integração | Passagem para humano | Regra: bot desliga ao transferir; etiqueta "pedido_pronto"; notificação ao atendente; resumo estruturado do pedido; volta ao bot após resolver | Quem atende do lado do cliente | Fluxo de transferência documentado | Dev + atendimento | 0,5 dia | Chatwoot (status open/pending, etiquetas, atribuição [D])\[3\] | Inbox | Humano recebe o resumo completo em < 1 min; bot não responde depois de transferir |
| 4. Integração | Fora do horário e follow-up | Mensagem de horário; aceitar pedido para agendar ou não (regra do cliente); follow-up único em até ~1–2h e no máximo ~20h após a última mensagem do cliente (dentro da janela de 24h) | Regras de horário | Workflows de follow-up | Dev + especialista em IA | 0,5 dia | n8n (cron), Chatwoot | Inbox | Nenhum follow-up livre enviado com mais de 24h da última mensagem do usuário |
| 5. Testes | Roteiro de testes funcional | 40–60 casos: pedidos simples, combinados, produto inexistente, sem estoque, fora da área, troco, mudança de pedido no meio, áudio, foto enviada pelo cliente, mensagens picadas | Prompt v1 + banco | Planilha de casos com resultado esperado | Especialista em IA + atendimento | 1 dia | Planilha, número de teste | Integração | ≥ 90% de aprovação; 100% nos casos críticos (preço, idade, transferência) [H] |
| 5. Testes | Red teaming | Tentativas de desconto falso ("o outro atendente me deu 50%"), injeção de prompt ("ignore as instruções"), pedido por menor, ofensa, pedido de assunto fora do escopo, pedido de dados de outro cliente | Prompt v1 | Relatório de vulnerabilidades + correções | Especialista em IA | 0,5 dia | Planilha; opcional promptfoo | Testes funcionais | Nenhuma falha crítica aberta |
| 5. Testes | UAT com o cliente | Dono e atendente conversam com o bot por 1–2 dias como clientes | Bot em homologação | Ata de aceite + lista de ajustes | Cliente + especialista em IA | 1 dia | WhatsApp | Red team | Aceite por escrito |
| 6. Go-live | Lançamento controlado | Ligar em horário ou volume limitado; humano de plantão; plano de rollback (desligar o bot com 1 clique) | Aceite | Bot em produção + runbook | Dev/infra + atendimento | 0,5 dia | Chatwoot, Coolify | UAT | 48h sem incidente crítico |
| 6. Go-live | Monitoramento e logs | Uptime do webhook e dos containers; alerta de queda de sessão (crítico no não oficial); logs de conversa e de chamadas de ferramenta; custo de tokens | Infra | Painel e alertas | Dev/infra | 0,5 dia | Uptime Kuma, logs do Coolify, Grafana (fase 2) | Infra | Alerta testado (derrubar o serviço gera aviso em < 5 min) |
| 6. Go-live | Backup | Dump diário do Postgres (Chatwoot + cardápio) fora da VPS; teste de restauração | Infra | Rotina de backup | Dev/infra | 0,25 dia | Backup do Coolify para S3 | Infra | Restauração testada 1 vez |
| 7. LGPD | Base legal e transparência | Aviso na 1ª mensagem (quem trata os dados, finalidade, link da política); base legal (execução de contrato para o pedido; consentimento/opt-in para promoções); prazo de retenção; contrato de operador (Ativos) com o cliente (controlador) | Modelo jurídico | Política de privacidade curta + cláusula de DPA no contrato | Sócio/jurídico | 0,5 dia | Docs | Discovery | Aviso ativo e contrato assinado |
| 8. Pós-lançamento | Revisão de conversas | Diária na semana 1 (amostra de 20–30 conversas); semanal depois; classificar erros por tipo | Logs | Planilha de erros + backlog de ajustes | Especialista em IA | 1h/dia (sem. 1); 2h/sem. depois | Chatwoot, planilha | Go-live | Toda falha crítica corrigida em ≤ 24h |
| 8. Pós-lançamento | Ajuste de prompt e regressão | Versionar o prompt; rodar novamente o roteiro de testes a cada mudança | Backlog | Prompt vN + changelog | Especialista em IA | 2–4h/semana | Git, planilha de testes | Revisão | Nenhuma regressão nos casos críticos |
| 8. Pós-lançamento | Relatório ao cliente | Semanal no 1º mês, mensal depois: conversas, pedidos passados ao humano, conversão, tempo de 1ª resposta, atendimentos fora do horário, principais dúvidas, ajustes feitos | Métricas | Relatório de 1 página | Especialista em IA + comercial | 1–2h por relatório | Looker Studio / planilha | Monitoramento | Entregue na data combinada |
| Fase 2 | API oficial + templates | Verificar o negócio; aprovar o nome de exibição; criar templates utility (status do pedido) e marketing (reengajamento, com opt-in) | Decisão de canal | Templates aprovados | Dev/infra + especialista em IA | 1–2 semanas (inclui a espera da Meta) [H] | WhatsApp Manager | Etapa 0 | Templates aprovados e testados |
| Fase 2 | Catálogo / mensagens de produto | Avaliar se a Commerce Policy permite os itens; se sim, sincronizar o catálogo pela Commerce Manager API | Política vigente | Catálogo ou decisão de não usar | Dev/infra | 2–3 dias | Commerce Manager | API oficial | Itens aprovados pela Meta, ou decisão documentada de não usar |

## Prática documentada versus heurística: o que sustenta cada parte do plano

**Documentado [D]** (verifique o texto vigente; a Meta muda as regras com frequência):

- **Janela de atendimento de 24h.** Dentro de 24h após a última mensagem do usuário, a empresa envia mensagens livres. Fora dela, só templates aprovados. A documentação de integração do Chatwoot descreve o cenário típico: o cliente escreve na sexta à noite e, na segunda de manhã, "the agent cannot reply because the 24-hour window has expired".\[3\]
- **Cobrança por mensagem desde 1º/07/2025.** O modelo de cobrança da Cloud API passou de "por conversa" para "por mensagem de template entregue". Há três categorias: marketing, utility e authentication. Mensagens de serviço (respostas livres dentro da janela) não são cobradas, e templates utility enviados dentro de uma janela aberta também ficaram gratuitos.
- **Opt-in e escalada para humano.** A WhatsApp Business Messaging Policy exige opt-in antes de a empresa iniciar contato. Também exige caminhos de escalada claros (agente humano, telefone, e-mail ou loja) em experiências automatizadas.
- **Restrição a "AI Providers".** A atualização dos termos da WhatsApp Business Solution, anunciada em outubro de 2025 e vigente desde 15/01/2026, proíbe provedores cuja funcionalidade principal seja IA de uso geral. Bots de atendimento ou venda de um negócio específico continuam permitidos. Por isso o prompt deve recusar assuntos fora do escopo.
- **Limites de envio.** Os limites para mensagens iniciadas pela empresa sobem por degraus (historicamente 250 → 1K → 10K → 100K → ilimitado), condicionados à qualidade (verde, amarela ou vermelha). Em 2025 a Meta passou a aplicar o limite por portfólio de negócios. Isso só importa para templates e campanhas, não para o atendimento receptivo.
- **Mídia e produtos.** Imagens em JPEG/PNG de até 5 MB. Mensagens multiproduto com até 30 itens.
- **Chatwoot.** Tem inbox "WhatsApp Cloud" com embedded signup e estados de conversa open, pending, resolved e snoozed, que servem para o desenho da passagem bot → humano.\[3\]
- **Baileys.** O README da Baileys, biblioteca usada por Evolution API e pelo fork da Fazer.ai, diz textualmente que o projeto "is not affiliated, associated, authorized, endorsed by, or in any way officially connected with WhatsApp". Diz também que os mantenedores não aprovam usos "that violate the Terms of Service of WhatsApp", e sua documentação lista o erro 463 ("account restricted") como um modo de falha.\[3\]

**Heurística [H]:**

- tamanhos de amostra (50–100 conversas no discovery, 40–60 casos de teste);
- metas de 90% de aprovação nos testes;
- follow-up único dentro da janela;
- uma VPS por cliente;
- tempos por etapa;
- o uso de planilha como fonte de preço no piloto.

São práticas comuns em agências e em guias de plataformas como Blip, Zenvia, Wati, Respond.io e Kommo, mas não são norma.

## (a) O que confirma o seu mapa

- **O fluxo de 5 passos é o padrão do mercado.** Receptivo → triagem → demonstração → preço e fechamento → humano é como as plataformas de atendimento conversacional estruturam bots de venda. Faz sentido o humano entrar no momento do pedido fechado, porque preparar, embalar e entregar é trabalho físico.\[1\] [H, com base em D para a escalada a humano]
- **O banco de dados do cardápio separado do prompt está certo.** O preço deve ser consultado, não memorizado. Isso protege contra alucinação e contra o art. 30 do CDC (oferta suficientemente precisa obriga o fornecedor). [D para o CDC; H para a arquitetura]
- **VPS própria com Coolify é viável** para um cliente pequeno, e o isolamento por cliente reduz o efeito de uma falha.\[2\] [H]
- **Testes e treino antes do lançamento** e a regra de horário de atendimento estão alinhados à prática.\[1\] [H]
- **Follow-up de quem some** é legítimo desde que respeite a janela de 24h ou use template aprovado com opt-in. [D]

## (b) O que corrige

1. **A ordem "cardápio no WhatsApp Business → testes" deve virar "regras e dados → prompt → testes".** O cardápio que o SDR usa é o do banco, não o catálogo do app. O catálogo nativo do WhatsApp para bebida alcoólica está exposto à Commerce Policy, que restringe a venda de álcool, e itens podem ser reprovados. Use o banco + `enviar_foto(sku)` como fonte principal e trate o catálogo como opcional na fase 2.
2. **A infraestrutura não começa pela VPS, começa pela decisão de canal.** A conexão não oficial (Baileys) tem custo zero por mensagem e sobe em horas, mas arrisca o banimento do número comercial do cliente, que é o ativo principal de uma distribuidora que vende pelo WhatsApp. A API oficial custa por template e exige verificação, mas é sustentável.
   - Recomendação: no piloto, se for usar a conexão não oficial, use um **número dedicado** e um termo de ciência assinado.
   - Planeje a migração para a Cloud API na fase 2. O Chatwoot oficial suporta a Cloud API nativamente, e a migração entre o oficial e o fork é uma troca de imagem Docker, segundo o material da comunidade registrado na reunião de 01/10.\[2\]
3. **"Valores e fechamento" deve incluir frete, área de entrega, pagamento e um resumo confirmado pelo cliente antes da passagem ao humano.** Sem isso o humano refaz a triagem e o ganho de tempo some.
4. **"Testes e treino" sem critério de pronto vira loop infinito.** Defina o roteiro de casos, os casos críticos com 100% de aprovação e o aceite do cliente.
5. **O follow-up "respeitoso e com controle" precisa de regra numérica:** 1 tentativa dentro da janela de 24h e nenhum envio livre fora dela. O reengajamento depois de 24h só com template e opt-in, na fase 2 se o canal for oficial.

## (c) O que falta

- **Discovery formal.** Faltam o mapeamento do atendimento atual, a FAQ, as objeções, o documento de regras (frete, área, pedido mínimo, pagamento, troco, casco, horário, estoque) e o guia de tom. É a etapa que mais costuma faltar e a que mais determina a qualidade. [H]
- **Verificação de idade.** Pergunta de maioridade antes de ofertar álcool, recusa padrão e conferência de documento pelo entregador. O art. 243 do ECA (redação da Lei 13.106/2015) tipifica como crime vender, fornecer ou entregar bebida alcoólica a criança ou adolescente, com pena de detenção de 2 a 4 anos e multa. A IA não elimina a responsabilidade do estabelecimento; a conferência física na entrega é o controle que de fato funciona. [D para a lei; H para o desenho]
- **Métricas e linha de base:**
  - tempo da 1ª resposta;
  - taxa de resolução sem humano para dúvidas;
  - taxa de conversão (conversa → pedido passado ao humano → pedido entregue);
  - taxa e motivo da passagem para humano;
  - pedidos fora do horário;
  - erros de preço (meta: zero);
  - recusas por idade.
- **Operação:**
  - monitoramento de queda (especialmente da sessão no não oficial);
  - backup fora da VPS com teste de restauração;
  - logs de chamadas de ferramenta;
  - controle de custo de tokens;
  - runbook de desligar o bot;
  - cofre de senhas.
- **LGPD:**
  - aviso de privacidade na 1ª interação;
  - definição de papéis (o cliente é o controlador, a Ativos é a operadora);
  - contrato de tratamento de dados;
  - retenção das conversas;
  - plano de incidente. A Resolução CD/ANPD nº 15/2024 fixa 3 dias úteis para comunicar incidente relevante. A Resolução CD/ANPD nº 2/2022 dá regime simplificado a agentes de pequeno porte, mas não os dispensa da segurança e da transparência.
- **Procedimento de atualização de preços pelo cliente,** com dono definido e tempo de propagação.
- **Rotina pós-lançamento e relatório,** inclusive o versionamento do prompt e a regressão.
- **Transparência sobre ser IA.** Não encontrei obrigação legal específica no Brasil hoje, mas é boa prática e reduz risco reputacional. [H]

## (d) Riscos e restrições legais e de política do WhatsApp

| Risco | Gravidade | Evidência | Mitigação |
|---|---|---|---|
| Banimento do número por uso de conexão não oficial (Baileys/Evolution/Z-API) | Alta | [D] README da Baileys: não afiliada, alerta contra violar os ToS e desencoraja "bulk or automated messaging usage"; erro 463 "account restricted" | Número dedicado no piloto; termo de ciência; migrar para a Cloud API; nunca fazer disparo em massa (o próprio README da Baileys pede "Do not spam people with this") |
| Commerce Policy do WhatsApp restringe a venda de álcool | Alta (precisa de verificação jurídica e da política vigente) | [D] Commerce Policy da Meta/WhatsApp | Não depender do catálogo nativo; vender por conversa com banco próprio; validar o texto vigente antes de escalar com a API oficial |
| Venda a menor de idade | Crítica | [D] ECA art. 243 (Lei 13.106/2015) | Pergunta de idade + recusa + conferência de documento na entrega + registro |
| Preço ou promoção inventada pela IA | Alta | [D] CDC art. 30 (oferta vincula) | Preço só via ferramenta; teste de red team "desconto falso"; resumo final gerado do banco |
| Mensagens fora da janela de 24h sem template | Média | [D] Regras da Cloud API | Follow-up só dentro da janela; templates na fase 2 |
| Mensagens promocionais sem opt-in | Média | [D] Business Messaging Policy; LGPD | Coletar opt-in explícito para promoções; descadastro fácil |
| Publicidade de bebida (mensagens promocionais) | Média | [D] Lei 9.294/1996 e Anexo A do Código do CONAR (bebidas alcoólicas) | Nada de apelo a menores; frase de advertência ("beba com moderação") em peças promocionais; revisão jurídica dos templates de marketing |
| Política de IA de uso geral (termos vigentes desde 15/01/2026) | Baixa para este caso | [D] Termos da WhatsApp Business Solution | Bot restrito ao negócio; recusar assuntos fora do escopo |
| Vazamento de dados / credenciais | Alta | [Interno] root compartilhado em grupo e "chave vazada" na VPS antiga\[2\] | Cofre de senhas; SSH por chave; rotação de credenciais; não reutilizar a VPS antiga; comunicar incidente em 3 dias úteis se houver |
| Queda da VPS ou da sessão sem alerta | Média | [H] | Uptime Kuma + alerta no WhatsApp/Slack do time; mensagem de contingência |

## Recomendações: o que fazer em 7 dias e o que vai para a fase 2

**Dentro dos 7 dias (piloto):**

1. **Dia 1:** decisão de canal (com termo de ciência) + entrevista de discovery + leitura de conversas.
2. **Dia 2:** documento de regras, FAQ, guia de tom e carga do banco (produtos, preços, fotos, frete por bairro).
3. **Dias 3–4:** prompt v1, ferramentas no n8n, conexão com o Chatwoot, passagem para humano, mensagem fora do horário, follow-up dentro da janela.
4. **Dia 5:** roteiro de testes + red teaming + correções.
5. **Dia 6:** UAT com o dono e o atendente + aviso LGPD + backup e alertas.
6. **Dia 7:** go-live controlado, com humano de plantão e revisão diária na semana seguinte.

**Fase 2 (semanas 2–6):**

- migração ou validação na API oficial com templates (utility para status do pedido; marketing com opt-in para reengajamento);
- painel de preços com log;
- catálogo nativo, se a política permitir;
- dashboard de métricas e relatório mensal automatizado;
- transcrição de áudio;
- integração com o PDV ou estoque;
- rastreio de origem dos leads (anúncios de clique para WhatsApp), em conexão com o trabalho de Meta Ads do Igor.\[1\]

**Critério para cobrar a fase 2 do cliente:** 2 semanas de piloto com zero erro de preço, zero venda a menor e transferência ao humano funcionando, mais o relatório com a linha de base comparada.

## Ressalvas

- **Não consegui acessar a web nesta pesquisa.** As ferramentas de busca não estavam disponíveis, e o subagente também não conseguiu abrir as páginas oficiais da Meta, do Planalto ou da ANPD. As regras do WhatsApp citadas (janela de 24h, cobrança por mensagem desde 1º/07/2025, opt-in, escalada para humano, termos sobre IA de uso geral vigentes desde 15/01/2026, limites de envio, mídia de 5 MB, multiproduto até 30 itens) e as normas brasileiras vêm de conhecimento consolidado, mas **precisam ser conferidas no texto vigente antes de qualquer decisão contratual**. O ponto mais sensível é o texto atual da Commerce Policy sobre bebidas alcoólicas.
- As únicas fontes lidas diretamente nesta sessão foram:
  - os documentos internos da Ativos (doc CLI-004 Guto Bebidas; anotações da reunião de 01/10/2026);
  - a documentação do Chatwoot (inbox WhatsApp Cloud, estados de conversa, cenário da janela de 24h);
  - o README da biblioteca Baileys.
- Os tempos por etapa e as metas numéricas são heurísticas de implantação, não benchmarks publicados.
- O documento interno não define se o primeiro cliente usará o número atual (app WhatsApp Business) ou um número novo. Isso muda a viabilidade: a coexistência app + Cloud API existe, mas depende de disponibilidade e de regras da Meta.

## Fontes

1. [Google Drive](https://drive.google.com/open?id=1hh_yUJtKQfaVLVzPpHH9bVd4fpHJAx9kzsXN2WfYWzs)
2. [Google Drive](https://drive.google.com/open?id=183JuHHEFKEHh_rZbC0EC8DbqsaKmbmBcW9JeT_ADekM)
3. Context7
4. Google Drive
