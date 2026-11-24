---
tipo: cópia de contexto (pesquisa do Igor, texto integral)
original: Drive ATIVOS › 20 Clientes › CLI-004 Guto Bebidas › 03 Entregas › Automação
link: https://docs.google.com/document/d/1UCC4ZZxLbpB6pluhWg3IL9vMgZsM7x-1oOTdttKA72U/edit
copiado: 24/11/2026
regra: cópia integral; sem contato, CPF, CNPJ, senha nem acesso. Afirmações marcadas "verificar" pelo autor precisam de conferência no texto oficial antes de ir para proposta ou contrato
---

Ativos Tecnologia · Automação Comercial · Guto Bebidas · 23/11/2026

# SDR de IA no WhatsApp para a Guto Bebidas

Plano de implantação, o que o seu mapa acerta e o que falta. Seu mapa acerta o fluxo de conversa, mas faltam três frentes antes do go-live, e são justamente as que podem derrubar o projeto: o canal, as regras do negócio e a operação pós-lançamento. Os diagramas seguem o sistema do repositório diagram-design; a tabela completa de implantação e o registro de riscos estão nas seções 6 e 9.

**Seu mapa está incompleto, não errado.** O fluxo receptivo → triagem → cardápio → valores → humano é o mesmo que as plataformas de mercado usam. Faltam três frentes antes do go-live: a escolha do canal (API oficial ou conexão não oficial), as regras do negócio, incluindo a idade mínima obrigatória para bebida alcoólica, e a operação pós-lançamento.

**Em 7 dias, o realista é um piloto controlado** com preço vindo só do banco de dados, verificação de idade, passagem para humano e follow-up dentro da janela de 24 h. Catálogo nativo, templates de reengajamento, painel de preços para o cliente e relatórios automáticos ficam para a fase 2.

**Ressalva da pesquisa original:** as ferramentas de busca não estavam disponíveis. As regras do WhatsApp e as normas brasileiras citadas vêm de conhecimento consolidado e precisam ser conferidas no texto vigente antes de qualquer decisão contratual. O ponto mais sensível é o texto atual da Commerce Policy sobre bebidas alcoólicas.

## 1. Os sete dias do piloto

Do discovery ao go-live controlado, com humano de plantão. A fase 2 vem depois, nas semanas 2 a 6.

etapaa etapa que define o resto

O resumo do documento agrupa os dias de outro jeito (testes nos dias 4 a 6). Aqui segui o plano dia a dia da seção de recomendações.

## 2. A decisão que vem antes de tudo: o canal

A stack que a Ativos montou, o fork do Chatwoot da Fazer.ai com Baileys sobre Coolify na Hostinger, usa conexão não oficial. O README da própria Baileys diz que ela não é afiliada ao WhatsApp, que os mantenedores não aprovam usos que violem os Termos de Serviço e que desencorajam “bulk or automated messaging usage”. Para uma distribuidora que vende pelo WhatsApp, o número é o ativo principal. documentado

Recomendação do documento: no piloto, se for usar a conexão não oficial, use um número dedicado e um termo de ciência assinado, e planeje a migração para a Cloud API na fase 2. O ramo “não usar Baileys” é leitura minha do risco descrito, não uma regra do documento. O documento interno também não define se o primeiro cliente usará o número atual (app WhatsApp Business) ou um número novo; a coexistência app + Cloud API existe, mas depende de disponibilidade e de regras da Meta.

|  | Conexão não oficial (Baileys, Evolution, Z-API) | API oficial (Cloud API) |
| --- | --- | --- |
| Custo | Zero por mensagem. | Por template entregue; respostas livres dentro da janela de 24 h não são cobradas. documentado |
| Tempo para subir | Horas; conexão em cerca de 0,5 dia. heurística | 1 a 3 dias mais a verificação do negócio na Meta, de dias a \~2 semanas. heurística |
| Risco | Banimento do número comercial do cliente; o erro 463 (“account restricted”) é um modo de falha listado na documentação da Baileys. documentado | Sustentável. O Chatwoot oficial suporta a Cloud API nativamente. |
| Cuidado | Número dedicado, termo de ciência assinado, nunca disparo em massa. | Verificar o negócio, aprovar o nome de exibição e criar os templates. |

## 3. Como a conversa funciona por dentro

O cliente vê cinco passos, os do seu mapa. Por trás da linha de visibilidade, o preço e o frete só saem de ferramenta (`function calling`): a IA consulta, nunca “lembra” valores. Pelo art. 30 do CDC, a oferta suficientemente precisa obriga o fornecedor, então um preço inventado pela IA vira problema jurídico. documentado

O cardápio que o SDR usa é o do banco de dados, não o catálogo do WhatsApp Business: a Commerce Policy restringe a venda de álcool e itens podem ser reprovados. O banco também deixa o cliente atualizar preços sem depender da Meta. As ferramentas (`consultar_preco`, `calcular_frete`, `enviar_foto`, `montar_resumo`, `transferir_humano`) são as da tabela de implantação.

## 4. Plano de implantação, dia a dia

Doze tarefas, seguindo o plano dia a dia do documento. Barras na mesma coluna rodam em paralelo. Em coral, a decisão de canal e o go-live.

tarefadecisão ou marcofase 2, semanas 2 a 6

Os tempos por etapa são estimativas heurística para uma equipe de 2 a 3 pessoas e um cliente pequeno. A verificação de negócio na Meta, de dias a \~2 semanas, é um prazo que sai do controle da equipe se o canal oficial for escolhido. O documento CLI-004 registra a Automação Comercial como “Sem prazo definido”, com status “A fazer”: os 7 dias são uma meta interna, e é por isso que a entrega é um piloto. interno

## 5. O que fica no piloto e o que vai para a fase 2

O piloto entrega o necessário para vender com segurança. A fase 2 traz o que depende da API oficial e da política da Meta, além do painel e das métricas.

**Critério para cobrar a fase 2:** 2 semanas de piloto com zero erro de preço, zero venda a menor e transferência ao humano funcionando, mais o relatório com a linha de base comparada.

A marca de risco está no canal não oficial: o banimento do número é o risco que pode derrubar o piloto. A venda a menor, de gravidade crítica, é tratada no cartão de idade.

## 6. Riscos e restrições

Dez riscos, com gravidade, evidência e mitigação como no documento. Só o de queda da VPS ou da sessão é heurística; o de vazamento de credenciais vem dos documentos internos. Os demais citam fonte oficial, lei ou documentação de fornecedor, e todos precisam de conferência no texto vigente.

| Risco | Gravidade | Evidência | Mitigação |
| --- | --- | --- | --- |
| Banimento do número por uso de conexão não oficial (Baileys/Evolution/Z-API) | Alta | documentado README da Baileys: não afiliada, alerta contra violar os ToS e desencoraja "bulk or automated messaging usage"; erro 463 "account restricted" | Número dedicado no piloto; termo de ciência; migrar para a Cloud API; nunca fazer disparo em massa (o próprio README da Baileys pede "Do not spam people with this") |
| Commerce Policy do WhatsApp restringe a venda de álcool | Alta (precisa de verificação jurídica e da política vigente) | documentado Commerce Policy da Meta/WhatsApp | Não depender do catálogo nativo; vender por conversa com banco próprio; validar o texto vigente antes de escalar com a API oficial |
| Venda a menor de idade | Crítica | documentado ECA art. 243 (Lei 13.106/2015) | Pergunta de idade + recusa + conferência de documento na entrega + registro |
| Preço ou promoção inventada pela IA | Alta | documentado CDC art. 30 (oferta vincula) | Preço só via ferramenta; teste de red team "desconto falso"; resumo final gerado do banco |
| Mensagens fora da janela de 24h sem template | Média | documentado Regras da Cloud API | Follow-up só dentro da janela; templates na fase 2 |
| Mensagens promocionais sem opt-in | Média | documentado Business Messaging Policy; LGPD | Coletar opt-in explícito para promoções; descadastro fácil |
| Publicidade de bebida (mensagens promocionais) | Média | documentado Lei 9.294/1996 e Anexo A do Código do CONAR (bebidas alcoólicas) | Nada de apelo a menores; frase de advertência ("beba com moderação") em peças promocionais; revisão jurídica dos templates de marketing |
| Política de IA de uso geral (termos vigentes desde 15/01/2026) | Baixa para este caso | documentado Termos da WhatsApp Business Solution | Bot restrito ao negócio; recusar assuntos fora do escopo |
| Vazamento de dados / credenciais | Alta | interno root compartilhado em grupo e "chave vazada" na VPS antiga\[2\] | Cofre de senhas; SSH por chave; rotação de credenciais; não reutilizar a VPS antiga; comunicar incidente em 3 dias úteis se houver |
| Queda da VPS ou da sessão sem alerta | Média | heurística | Uptime Kuma + alerta no WhatsApp/Slack do time; mensagem de contingência |

## 7. Contexto interno verificado no Drive

- O documento **CLI-004 Guto Bebidas** (23/11/2026) registra três entregas em 7 dias, de 23/11 a 29/11: landing page, setup de tráfego e posicionamento digital. A **Automação Comercial está “Sem prazo definido”, com status “A fazer”**. O SDR de IA fica com o Hugo e a infraestrutura com o Bernardo; o fluxo tem 5 passos, mais as regras de follow-up e de atendimento fora do horário. interno
- A **reunião de 01/10/2026** decidiu adotar o fork do Chatwoot da Fazer.ai, “com conexões nativas para o WhatsApp via Baileys, ausentes na API oficial da Meta”, usar Coolify em VPS Hostinger KVM2 e ter uma VPS por cliente, para isolar falhas. interno
- A mesma reunião registrou dois problemas: **credenciais root e de acesso compartilhadas em grupo de mensagens**, com o cofre de senhas deixado para depois, e uma **VPS antiga com “chave vazada”**. Os dois pontos pesam na segurança e na LGPD. interno

## 8. O que é documentado e o que é heurística

A Meta muda as regras com frequência: verifique o texto vigente de cada item documentado.

Documentado

- **Janela de 24 h:** dentro dela, mensagens livres; fora, só templates aprovados.
- **Cobrança por mensagem desde 1º/07/2025:** marketing, utility e authentication; respostas de serviço dentro da janela não são cobradas.
- **Opt-in e escalada para humano:** a Business Messaging Policy exige opt-in e caminhos claros de escalada em experiências automatizadas.
- **Provedores de IA de uso geral** estão proibidos desde 15/01/2026; bots de um negócio específico seguem permitidos. Por isso o prompt recusa assuntos fora do escopo.
- **Limites de envio** sobem por degraus conforme a qualidade, e só importam para templates e campanhas.
- **Mídia:** JPEG/PNG de até 5 MB; multiproduto com até 30 itens.
- **Chatwoot:** inbox “WhatsApp Cloud” com embedded signup e estados open, pending, resolved e snoozed.
- **Baileys:** não afiliada ao WhatsApp; erro 463 como modo de falha.

Heurística

- Tamanhos de amostra: 50 a 100 conversas no discovery, 40 a 60 casos de teste.
- Meta de 90% de aprovação nos testes, com 100% nos casos críticos.
- Follow-up único dentro da janela.
- Uma VPS por cliente.
- Tempos por etapa.
- Planilha como fonte de preço no piloto.

São práticas comuns em agências e em guias de plataformas como Blip, Zenvia, Wati, Respond.io e Kommo, mas não são norma.

## 9. Tabela completa de implantação

As 29 etapas do documento, com as dez colunas, lidas direto do arquivo. Tempos e metas numéricas são heurísticas, não benchmarks publicados.

Abrir a tabela (29 etapas, da decisão de canal à fase 2)

| Etapa | Tarefa | Subtarefas | Entrada necessária | Entregável | Papel responsável | Tempo estimado | Ferramentas | Depende de | Critério de "pronto" |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0. Decisão de canal | Escolher API oficial (Cloud API) ou conexão não oficial (Baileys/Evolution/Z-API) | Avaliar o risco de banimento do número; verificar se o número atual usa o app WhatsApp Business; checar se a coexistência app + API está disponível; estimar o custo por template | Número do cliente, acesso ao Meta Business Manager do cliente, apetite a risco | Decisão registrada e assinada pelo cliente (termo de ciência de risco, se for não oficial) | Dev/infra + sócio comercial | 0,5 dia (decisão); verificação de negócio na Meta: de dias a \~2 semanas heurística | Meta Business Manager, WhatsApp Manager, Chatwoot (inbox "WhatsApp Cloud" via embedded signup documentado)\[3\] | — | Canal escolhido, número definido, cliente ciente por escrito dos riscos |
| 1. Discovery | Mapear o atendimento atual | Ler 50–100 conversas reais do WhatsApp do cliente; cronometrar o tempo de resposta atual; mapear quem atende, em que horário e como passa o pedido para a entrega | Exportação de conversas (com autorização) e entrevista de 1h com o dono e o atendente | Mapa "como é hoje" (jornada + gargalos) | Especialista em IA + atendimento | 0,5–1 dia | Planilha, export do WhatsApp, Google Docs | 0 | Pelo menos 50 conversas lidas e 5 jornadas típicas descritas |
| 1. Discovery | Levantar FAQ e objeções | Top 30 perguntas; objeções (preço, frete, demora, "tá gelada?", troco); gatilhos de desistência | Conversas do passo anterior + entrevista | Base de FAQ com respostas aprovadas pelo dono | Especialista em IA | 0,5 dia | Planilha/Notion | Mapa atual | Cada FAQ com resposta validada pelo cliente |
| 1. Discovery | Regras de negócio | Área de entrega (bairros ou CEPs, raio); frete por faixa; pedido mínimo; formas de pagamento (Pix, cartão na entrega, troco); horário; política de troca/casco; **idade mínima de 18 anos**; prazo de entrega; estoque | Dono do negócio | "Documento de regras" versionado (fonte única para o prompt e o banco) | Especialista em IA + cliente | 0,5 dia | Google Docs | Mapa atual | Todas as regras com valor numérico ou lista fechada, sem "depende" |
| 1. Discovery | Tom de voz e persona | Nome do atendente virtual; grau de informalidade; uso de emojis; palavras proibidas; se informa que é IA | Exemplos de mensagens de que o dono gosta | Guia de tom (1 página) + 10 exemplos de diálogo "ideal" | Especialista em IA | 0,25 dia | Docs | FAQ | Dono aprova os 10 exemplos |
| 1. Discovery | Métricas de sucesso e linha de base | Definir as metas: tempo da 1ª resposta, % de conversas que viram pedido, % de passagem para humano, pedidos fora do horário | Dados do "como é hoje" | Scorecard com a linha de base | Especialista em IA + comercial | 0,25 dia | Planilha | Mapa atual | Linha de base medida e metas acordadas |
| 2. Dados | Modelar o banco do cardápio | Tabelas de produto (SKU, nome, categoria, volume, preço, promoção, ativo/inativo, url_foto, teor alcoólico), frete por bairro, horário | Lista de produtos e preços do cliente; fotos | Esquema + carga inicial | Dev/infra | 0,5–1 dia | Postgres/Supabase na VPS, ou Google Sheets como fonte no piloto | Regras de negócio | 100% dos SKUs ativos com preço e foto; consulta testada |
| 2. Dados | Fotos e artes | Padronizar as imagens (JPEG/PNG, peso baixo); hospedar com URL estável | Fotos do cliente ou do fornecedor | Pasta/bucket com as imagens nomeadas por SKU | Design + dev | 0,5 dia | Storage S3-compatível / MinIO / CDN | Esquema | Toda foto ≤ 5 MB (limite de imagem da Cloud API documentado) e carregando no WhatsApp |
| 2. Dados | Atualização pelo cliente | Piloto: o cliente edita uma planilha e um sync leva ao banco. Fase 2: painel simples (NocoDB/Appsmith) com log de alterações | Pessoa do cliente responsável pelo preço | Procedimento "como alterar preço" (1 página) | Dev/infra | Piloto: 0,5 dia; painel: 2–3 dias (fase 2) | Google Sheets + n8n; NocoDB | Esquema | Cliente altera um preço e o bot responde o novo valor em ≤ 5 min |
| 3. Agente | Prompt de sistema | Papel, objetivo, limites; fluxo em estados (saudação → triagem → idade → oferta → carrinho → endereço/frete → pagamento → resumo → passagem para humano); regras "nunca" (inventar preço, prometer prazo fora da regra, vender a menor, falar de assuntos fora do escopo) | Documento de regras, guia de tom, FAQ | Prompt versionado (v1) no Git | Especialista em IA | 1 dia | LLM (GPT, conforme decisão interna de 08/10), Git\[4\] | Discovery | Prompt revisado por um segundo membro; passa no smoke test |
| 3. Agente | Ferramentas (function calling) | `buscar_produto`, `consultar_preco`, `calcular_frete(bairro)`, `enviar_foto(sku)`, `montar_resumo`, `transferir_humano(motivo)` | Banco pronto | Workflows/endpoints | Dev/infra + especialista em IA | 1 dia | n8n, API do Chatwoot | Banco | Preço e frete sempre vêm de ferramenta (zero preço "de memória" nos testes) |
| 3. Agente | Base de conhecimento | FAQ e políticas em texto curto, por tópico (RAG ou injeção no prompt, conforme o tamanho) | FAQ aprovada | KB versionada | Especialista em IA | 0,5 dia | Vetorial (pgvector) ou só o prompt | FAQ | Cada pergunta da FAQ respondida corretamente em teste |
| 3. Agente | Verificação de idade | Pergunta de confirmação de maioridade antes de ofertar álcool; recusa padrão; registro do aceite; instrução ao entregador para conferir documento na entrega | Regra jurídica + cliente | Trecho de fluxo + checklist do entregador | Especialista em IA + cliente | 0,25 dia | Prompt + campo no CRM | Prompt | 100% dos casos-limite "sou menor" recusados nos testes |
| 4. Integração | Infraestrutura na VPS | Coolify; Chatwoot; n8n; Postgres; HTTPS; firewall; usuários sem root; cofre de senhas | VPS (já contratada)\[2\] | Ambiente de produção + homologação | Dev/infra | 1 dia | Hostinger KVM2, Coolify, Docker\[2\] | 0 | Serviços com HTTPS, acesso por chave SSH, senhas fora de grupos de chat |
| 4. Integração | Conectar o WhatsApp | Oficial: app Meta, WABA, número, webhook, token permanente. Não oficial: pareamento por QR em número dedicado | Decisão da etapa 0 | Inbox ativa no Chatwoot | Dev/infra | 0,5 dia (não oficial); 1–3 dias + verificação (oficial) heurística | Chatwoot, Meta Developer | Decisão de canal | Mensagem de teste ida e volta, mídia incluída |
| 4. Integração | Passagem para humano | Regra: bot desliga ao transferir; etiqueta "pedido_pronto"; notificação ao atendente; resumo estruturado do pedido; volta ao bot após resolver | Quem atende do lado do cliente | Fluxo de transferência documentado | Dev + atendimento | 0,5 dia | Chatwoot (status open/pending, etiquetas, atribuição documentado)\[3\] | Inbox | Humano recebe o resumo completo em \< 1 min; bot não responde depois de transferir |
| 4. Integração | Fora do horário e follow-up | Mensagem de horário; aceitar pedido para agendar ou não (regra do cliente); follow-up único em até \~1–2h e no máximo \~20h após a última mensagem do cliente (dentro da janela de 24h) | Regras de horário | Workflows de follow-up | Dev + especialista em IA | 0,5 dia | n8n (cron), Chatwoot | Inbox | Nenhum follow-up livre enviado com mais de 24h da última mensagem do usuário |
| 5. Testes | Roteiro de testes funcional | 40–60 casos: pedidos simples, combinados, produto inexistente, sem estoque, fora da área, troco, mudança de pedido no meio, áudio, foto enviada pelo cliente, mensagens picadas | Prompt v1 + banco | Planilha de casos com resultado esperado | Especialista em IA + atendimento | 1 dia | Planilha, número de teste | Integração | ≥ 90% de aprovação; 100% nos casos críticos (preço, idade, transferência) heurística |
| 5. Testes | Red teaming | Tentativas de desconto falso ("o outro atendente me deu 50%"), injeção de prompt ("ignore as instruções"), pedido por menor, ofensa, pedido de assunto fora do escopo, pedido de dados de outro cliente | Prompt v1 | Relatório de vulnerabilidades + correções | Especialista em IA | 0,5 dia | Planilha; opcional promptfoo | Testes funcionais | Nenhuma falha crítica aberta |
| 5. Testes | UAT com o cliente | Dono e atendente conversam com o bot por 1–2 dias como clientes | Bot em homologação | Ata de aceite + lista de ajustes | Cliente + especialista em IA | 1 dia | WhatsApp | Red team | Aceite por escrito |
| 6. Go-live | Lançamento controlado | Ligar em horário ou volume limitado; humano de plantão; plano de rollback (desligar o bot com 1 clique) | Aceite | Bot em produção + runbook | Dev/infra + atendimento | 0,5 dia | Chatwoot, Coolify | UAT | 48h sem incidente crítico |
| 6. Go-live | Monitoramento e logs | Uptime do webhook e dos containers; alerta de queda de sessão (crítico no não oficial); logs de conversa e de chamadas de ferramenta; custo de tokens | Infra | Painel e alertas | Dev/infra | 0,5 dia | Uptime Kuma, logs do Coolify, Grafana (fase 2) | Infra | Alerta testado (derrubar o serviço gera aviso em \< 5 min) |
| 6. Go-live | Backup | Dump diário do Postgres (Chatwoot + cardápio) fora da VPS; teste de restauração | Infra | Rotina de backup | Dev/infra | 0,25 dia | Backup do Coolify para S3 | Infra | Restauração testada 1 vez |
| 7. LGPD | Base legal e transparência | Aviso na 1ª mensagem (quem trata os dados, finalidade, link da política); base legal (execução de contrato para o pedido; consentimento/opt-in para promoções); prazo de retenção; contrato de operador (Ativos) com o cliente (controlador) | Modelo jurídico | Política de privacidade curta + cláusula de DPA no contrato | Sócio/jurídico | 0,5 dia | Docs | Discovery | Aviso ativo e contrato assinado |
| 8. Pós-lançamento | Revisão de conversas | Diária na semana 1 (amostra de 20–30 conversas); semanal depois; classificar erros por tipo | Logs | Planilha de erros + backlog de ajustes | Especialista em IA | 1h/dia (sem. 1); 2h/sem. depois | Chatwoot, planilha | Go-live | Toda falha crítica corrigida em ≤ 24h |
| 8. Pós-lançamento | Ajuste de prompt e regressão | Versionar o prompt; rodar novamente o roteiro de testes a cada mudança | Backlog | Prompt vN + changelog | Especialista em IA | 2–4h/semana | Git, planilha de testes | Revisão | Nenhuma regressão nos casos críticos |
| 8. Pós-lançamento | Relatório ao cliente | Semanal no 1º mês, mensal depois: conversas, pedidos passados ao humano, conversão, tempo de 1ª resposta, atendimentos fora do horário, principais dúvidas, ajustes feitos | Métricas | Relatório de 1 página | Especialista em IA + comercial | 1–2h por relatório | Looker Studio / planilha | Monitoramento | Entregue na data combinada |
| Fase 2 | API oficial + templates | Verificar o negócio; aprovar o nome de exibição; criar templates utility (status do pedido) e marketing (reengajamento, com opt-in) | Decisão de canal | Templates aprovados | Dev/infra + especialista em IA | 1–2 semanas (inclui a espera da Meta) heurística | WhatsApp Manager | Etapa 0 | Templates aprovados e testados |
| Fase 2 | Catálogo / mensagens de produto | Avaliar se a Commerce Policy permite os itens; se sim, sincronizar o catálogo pela Commerce Manager API | Política vigente | Catálogo ou decisão de não usar | Dev/infra | 2–3 dias | Commerce Manager | API oficial | Itens aprovados pela Meta, ou decisão documentada de não usar |

## 10. O seu mapa, comparado com a pesquisa

Confirma

- **O fluxo de 5 passos é o padrão do mercado.** O humano entra no pedido fechado porque preparar, embalar e entregar é trabalho físico. heurística
- **Banco de dados do cardápio separado do prompt.** O preço é consultado, não memorizado; protege contra alucinação e contra o art. 30 do CDC. documentado
- **VPS própria com Coolify** é viável para um cliente pequeno, e o isolamento por cliente reduz o efeito de uma falha. heurística
- **Testes e treino antes do lançamento** e a regra de horário de atendimento. heurística
- **Follow-up de quem some** é legítimo dentro da janela de 24 h ou com template aprovado e opt-in. documentado

Corrige

- A ordem “cardápio no WhatsApp Business → testes” vira **regras e dados → prompt → testes**; o catálogo nativo é opcional na fase 2.
- A infraestrutura **começa pela decisão de canal**, não pela VPS.
- “Valores e fechamento” inclui **frete, área de entrega, pagamento e um resumo confirmado** pelo cliente antes de passar ao humano; sem isso o humano refaz a triagem.
- “Testes e treino” precisa de **critério de pronto**: roteiro, casos críticos com 100% e aceite do cliente.
- O follow-up ganha **regra numérica**: 1 tentativa dentro das 24 h, nenhum envio livre fora delas; reengajamento só com template e opt-in, na fase 2.

Falta

- **Discovery formal:** atendimento atual, FAQ, objeções, documento de regras (frete, área, pedido mínimo, pagamento, troco, casco, horário, estoque) e guia de tom. heurística
- **Verificação de idade:** pergunta de maioridade, recusa padrão e conferência de documento pelo entregador. O art. 243 do ECA tipifica como crime vender, fornecer ou entregar bebida alcoólica a menor, com detenção de 2 a 4 anos e multa; a conferência física na entrega é o controle que de fato funciona. documentado
- **Métricas e linha de base:** tempo da 1ª resposta, resolução sem humano, conversão, passagem para humano, pedidos fora do horário, erros de preço (meta: zero) e recusas por idade.
- **Operação:** monitoramento de queda, backup fora da VPS com teste de restauração, logs de ferramenta, custo de tokens, runbook de desligar o bot e cofre de senhas.
- **LGPD:** aviso na 1ª interação, papéis (cliente controlador, Ativos operadora), contrato de tratamento, retenção e plano de incidente. A Resolução CD/ANPD nº 15/2024 fixa 3 dias úteis para comunicar incidente relevante.
- **Atualização de preços pelo cliente,** com dono e tempo de propagação definidos.
- **Rotina pós-lançamento e relatório,** com versionamento do prompt e regressão.
- **Transparência sobre ser IA:** não há obrigação legal específica encontrada, mas é boa prática. heurística

## 11. Ressalvas e fontes

- **A pesquisa original não acessou a web.** As regras do WhatsApp (janela de 24 h, cobrança por mensagem desde 1º/07/2025, opt-in, escalada para humano, termos sobre IA de uso geral, limites de envio, mídia de 5 MB, multiproduto) e as normas brasileiras vêm de conhecimento consolidado. Precisam ser conferidas no texto vigente antes de qualquer decisão contratual, sobretudo a Commerce Policy sobre bebidas alcoólicas.
- **Fontes lidas diretamente na pesquisa:** os documentos internos da Ativos (CLI-004 Guto Bebidas e as anotações da reunião de 01/10/2026), a documentação do Chatwoot e o README da biblioteca Baileys.
- **Tempos por etapa e metas numéricas** são heurísticas de implantação, não benchmarks publicados.
- **Em aberto:** o documento interno não define se o primeiro cliente usará o número atual (app WhatsApp Business) ou um número novo, e isso muda a viabilidade da API oficial.
- **Escolhas minhas nesta página:** a ramificação “não usar Baileys” do fluxograma, a marca de risco do story map e a escolha dos diagramas. O conteúdo vem do documento.

Fontes do documento: \[1\] [Google Drive (CLI-004)](https://drive.google.com/open?id=1hh_yUJtKQfaVLVzPpHH9bVd4fpHJAx9kzsXN2WfYWzs), \[2\] [Google Drive (reunião de 01/10/2026)](https://drive.google.com/open?id=183JuHHEFKEHh_rZbC0EC8DbqsaKmbmBcW9JeT_ADekM), \[3\] documentação do Chatwoot e README da Baileys (via Context7), \[4\] Google Drive (decisão interna de 08/10 sobre o LLM).

Diagramas no sistema de design do repositório cathrynlavery/diagram-design (licença MIT): Steps, Flowchart, Service blueprint, Gantt e Story map, com as cores do tema desta página e textos em português. Verificação: os cinco diagramas passaram no self_check e no verify_geometry do repositório, e o blueprint também no verificador próprio do tipo (linha de visibilidade, grade de etapas e rótulos).