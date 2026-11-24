---
tipo: cópia de contexto (pesquisa do Igor, texto integral)
original: Drive ATIVOS › 40 Processos › 42 Fluxos dos serviços
link: https://docs.google.com/document/d/1iN8B1CJZory54Tu1eYiJUCK35ee88v_Dv5ZvlWchmr4/edit
copiado: 24/11/2026
regra: cópia integral; sem contato, CPF, CNPJ, senha nem acesso. Afirmações marcadas "verificar" pelo autor precisam de conferência no texto oficial antes de ir para proposta ou contrato
---

# Operação padrão da agência: fluxo de 7 dias, rotinas por papel, ficha de tarefa e ferramentas

Para escalar sem quebrar, a agência deve tratar cada pacote como um produto com relógio próprio. O prazo de 7 dias passa a contar do **D1 = dia em que o último acesso crítico chega**, e não da assinatura. Cada serviço ganha uma definição de pronto escrita por produto. O trabalho em andamento fica limitado por pessoa (o quadro de vocês já fixa máximo de 3 tarefas em "Fazendo"), e as entradas de clientes novos são escalonadas pela capacidade real medida em horas.\[1\] Pontuação individual de tarefas e rankings entre sócios não devem ser adotados: a evidência sobre métricas viradas em metas (Lei de Campbell, "Goals Gone Wild", Wells Fargo) mostra que esse caminho gera maquiagem de números, e a gamificação só melhora o clima quando é voluntária.

## TL;DR

- **Fluxo:** os ciclos de 7 dias de vocês são viáveis, mas só se o relógio começar no D1 = acessos recebidos e se o "pronto" de cada produto for definido de forma honesta. GMN pronto = "perfil preenchido e verificação pedida", porque o Google pode levar até 5 dias úteis para analisar o vídeo. Tráfego pronto = "campanha no ar com rastreio validado", porque a otimização da Meta só começa depois da fase de aprendizado. O SDR de IA não cabe em 7: as anotações da reunião de 23/11/2026 registram que "Henrique Horta estabeleceu prazos fixos de 7 dias para tráfego pago, Google Meu Negócio e landing pages, além de 15 dias para automação comercial com agente SDR".
- **Rotina:** com 4 sócios (Henrique, Igor, Hugo e Bernardo) acumulando papéis e saindo para vender na rua, o gargalo é a troca de contexto, não a falta de ferramenta. A rotina recomendada usa blocos de foco por cliente pela manhã, daily de 15 minutos com horário fixo, uma janela de comunicação com clientes, planejamento semanal na segunda e revisão na sexta. Nenhuma reunião de 3 a 4 horas.
- **Medição e ferramentas:** meçam fluxo da equipe (lead time por pacote, entregas no prazo, retrabalho por rodada de aprovação, tempo real versus estimado), não pontos individuais. A planilha "Quadro de tarefas ATIVOS" já tem a estrutura certa: parem de trocar de ferramenta (Notion → Sheets/AppSheet em um mês) e consolidem Google Workspace, Chatwoot e WhatsApp por 90 dias.

## Como este relatório foi feito (leia antes)

- **Material interno lido:** a ata e a transcrição da reunião de 23/11/2026 (prazos, preços, divisão de papéis);\[2\] o documento "CLI-004 Guto Bebidas – documentação dos serviços e processos v01"; o "Plano de 7 dias do perfil" do GMN; a planilha "Quadro de tarefas ATIVOS" (v2, 10/11/2026); a reunião de 08/10/2026 (Kanban no Notion, pacotes, pagamento 50/50);\[3\] e o "Checklist de onboarding do novo cliente" do curso Profissão GMN com IA.\[1\]\[4\]\[5\]\[6\]\[7\]
- **Fontes externas sem conferência ao vivo:** nesta sessão eu não tinha busca na web aberta. As fontes externas (Scrum Guide, Kanban Guide, APA, Leroy, Campbell, CFPB e outras) aparecem como referências bibliográficas conhecidas, com URL quando é estável. Em cada caso indico o que é dado primário, revisão, entrevista ou opinião. Antes de publicar esse material para terceiros, abram os links e confiram o texto literal.
- **Fontes brasileiras:** não consegui localizar e verificar URLs específicas do Sebrae, RD Station, Operand ou mLabs sobre onboarding de agência. As únicas fontes brasileiras usadas são o material interno de vocês e o curso de GMN já presente no Drive, que cita um guia do Sebrae RN.\[4\]
- **Etiquetas usadas em cada recomendação:**
  - **[Comprovada/documentada]**: há fonte primária, acadêmica ou guia oficial.
  - **[Opinião/heurística]**: prática de mercado ou julgamento meu, sem evidência controlada.

## Key Findings

1. **A base que vocês já têm é boa; o que falta é estabilidade.** O quadro em Sheets já tem o essencial:
   - tarefa que começa com verbo;\[1\]
   - tamanho máximo de 1 dia;\[1\]
   - estimativa P/M/G (até 2h, até 4h, até 1 dia);\[1\]\[2\]
   - sprint semanal (2026-S45);\[1\]
   - WIP máximo de 3 tarefas por pessoa;\[1\]
   - status "Aguardando" com o nome de quem trava;\[1\]
   - coluna de tempo real.\[1\]

   Isso está alinhado com Kanban e com a Lei de Little. O problema aparece no próprio quadro: as tarefas T-001 a T-059 de três clientes foram canceladas e substituídas em 09/11, e a ferramenta mudou de Notion para Sheets/AppSheet em um mês.\[1\] A cada troca, o histórico de tempo real (o dado mais valioso para precificar) recomeça do zero.
2. **O prazo de 7 dias tem dois passos que vocês não controlam.**
   - **Verificação do GMN:** o documento "2026-11-23_CLI-004-guto-bebidas_plano-7-dias-google-meu-negocio_v01" registra, com base na ajuda do Google: "A verificação é o único passo que o Google controla: a análise do vídeo pode levar até 5 dias úteis, e o cartão-postal até 14". O mesmo documento sugere "combinar com o cliente que a entrega do D7 é 'perfil preenchido e verificação pedida'".
   - **Fase de aprendizado da Meta:** a documentação oficial da Marketing API diz que edições significativas fazem o conjunto de anúncios voltar à fase de aprendizado. Os status possíveis são LEARNING, SUCCESS e FAIL.\[8\] A regra clássica de cerca de 50 eventos de otimização em 7 dias está na Central de Ajuda da Meta, mas a API hoje expõe limites "dinâmicos", então tratem o número como aproximado.\[8\]

   Conclusão: o D7 de tráfego é o setup no ar, não o resultado otimizado.
3. **Há contradições internas que impedem padronizar.**
   - O documento do Guto atribui GMN/SEO ao Henrique, mas o painel lateral do mapa coloca o Hugo como quem faz palavras-chave, e o plano de 7 dias do GMN põe o Igor para operar o painel: na tarefa T1 ("Acesso e propriedade", prazo D1, "Quem: Igor com o cliente"), "o cliente convida o Igor em Configurações > Pessoas e acesso, como administrador ou proprietário... Nunca senha compartilhada".
   - O SDR aparece com 15 dias na ata de 23/11, mas o pedido deste relatório fala em ciclos de 7 dias para os três produtos.\[2\]\[6\]
   - O documento do Guto define o cronograma de "segunda 23/11 a domingo 29/11", o que inclui o fim de semana.\[7\]
   - Tags do Google Ads (GTM, Analytics, pixel) foram descritas só para Meta. Esse ponto as anotações da reunião de 23/11 já resolveram: "Ficou decidido unificar o rastreamento do Google Ads em um bloco único com GTM e Analytics".

   Antes de qualquer automação, resolvam essas quatro linhas.
4. **O maior risco operacional é a troca de contexto.**
   - **Quem acumula o quê:** Igor faz tráfego, vende na rua e opera o GMN. Hugo faz SDR, SEO, copy e raspagem de leads. Bernardo faz landing page, infraestrutura, Chatwoot e posts.\[6\]\[7\]
   - **O que dizem os estudos:** a pesquisa sobre troca de tarefas (Rubinstein, Meyer e Evans, 2001, resumida pela APA, que fala em perda de até 40% do tempo produtivo) e sobre "resíduo de atenção" (Leroy, 2009) indica que alternar clientes a cada hora custa caro.
   - **O que isso significa na prática:** a rotina precisa agrupar trabalho por cliente e por tipo.
5. **Gamificar a entrega é a ideia mais arriscada da lista.** A ata de 23/11 atribui ao Igor "pesquisar gamificar o fluxo de trabalho".\[6\] A evidência recomenda cautela:
   - a revisão de Hamari, Koivisto e Sarsa (2014) encontrou efeitos positivos, porém dependentes de contexto e de quem participa;
   - Mollick e Rothbard (2014) mostraram que o jogo só melhora o afeto de quem consente em jogar;
   - a Lei de Campbell e o caso Wells Fargo mostram o que acontece quando um indicador vira meta com consequência.

   Em uma sociedade de 4 sócios, ranking interno é uma forma de criar conflito societário.

## (a) Fluxo padrão de ponta a ponta: da venda fechada ao pós-entrega

**Convenções:**
- **D-x:** antes do relógio começar.
- **D1:** dia em que o último acesso crítico foi recebido.
- **Dias úteis:** de segunda a sexta. **[Opinião/heurística]**: prazo corrido com fim de semana cria horas extras invisíveis e contradiz o sprint "segunda a sexta" do próprio quadro.\[1\]

**Papéis (como estão hoje; confirmar):**
- **GC** = Gestor de contas/operações (Henrique);
- **TR** = Tráfego (Igor);
- **IA** = Automação/SDR (Hugo);
- **LP** = Landing page/infra (Bernardo);
- **SEO** = SEO/copy (Hugo, apoio do Henrique).

| Fase | Etapa | Responsável | Prazo típico | Saída / critério de pronto | Evidência |
|---|---|---|---|---|---|
| 0. Venda | Proposta com escopo fechado por produto, prazo em dias úteis contados do D1, o que NÃO está incluso e cláusula "Google/Meta não garantem posição nem prazo" | Quem vendeu (Igor/Henrique) | D-3 a D-1 | Contrato assinado e 50% pagos no cartão (regra definida em 08/10)\[3\] | Regra de pagamento: interna. Cláusula de não garantia: checklist do curso GMN, cláusula 10 **[Documentada, fonte interna]**\[5\] |
| 0. Venda → Operação | Handoff comercial: o vendedor preenche a "ficha de venda" (o que prometeu, preço, contato, particularidades) | Vendedor → GC | Mesmo dia da assinatura | Ficha preenchida; sem ficha, o cliente não entra no quadro | **[Opinião/heurística]**: é o ponto onde mais se perde informação quando quem vende não entrega |
| 1. Onboarding | Criar o grupo de WhatsApp do cliente (dono como admin), pasta no Drive (`CLI-00X`) e projeto no quadro a partir do template | GC | D-1 (até 24h após assinatura) | Grupo, pasta e tarefas-padrão criadas | Checklist do curso GMN: "grupo criado no primeiro dia"; "o grupo é parte da entrega, não um canal de suporte" **[Documentada, fonte interna]**\[5\] |
| 1. Onboarding | Formulário único de briefing + pedido de TODOS os acessos e materiais de uma vez (doc único, não pelo chat) | GC | D-1 | Formulário enviado com prazo de 48h | Checklist do curso: "pedi tudo de uma vez, num doc único, não no corpo da conversa" **[Documentada, fonte interna]**\[5\] |
| 1. Onboarding | Coleta de acessos: GMN (convite como gerente/administrador, nunca senha compartilhada), BM/conta de anúncio, domínio/DNS, WhatsApp Business/número, Instagram | GC cobra; TR, LP e IA validam | Até 48h | Cada acesso testado com uma ação real | Ajuda do Google (Pessoas e acesso), citada no plano de 7 dias **[Guia oficial, via documento interno]**\[4\] |
| 1. Onboarding | **Gatilho do D1:** relógio começa quando o último acesso crítico chega. Avisar no grupo: "Recebemos tudo, hoje é o D1, entrega em [data]" | GC | — | Mensagem registrada no grupo | O plano GMN já define "D1 é o dia em que o cliente dá o acesso" **[Documentada, fonte interna]**\[4\] |
| 1. Onboarding | Kickoff de 30 a 45 min (vídeo ou presencial): metas, públicos, diferenciais, quem aprova, expectativas por escrito | GC + TR | D1 | Ata de 5 linhas no grupo | **[Opinião/heurística]**: prática comum de agências; o curso GMN pede registrar expectativas "por escrito no grupo"\[5\] |
| 1. Onboarding | Marco zero (baseline): print e PDF do GMN, posição no mapa em grade, métricas atuais de anúncios e do site | SEO/GC | D1 | Pasta "relatório 1 – inicial" datada | Plano GMN T2: "corrigir antes de documentar impede provar a melhora" **[Documentada, fonte interna]**\[4\] |
| 2. Produção | Posicionamento digital: pesquisa de 3 a 5 concorrentes → wireframe → copy → front-end/motion → SEO on-page → domínio/deploy → botão WhatsApp | LP + SEO | D1–D5 | Link de homologação funcionando no celular | Processo do doc do Guto **[Documentada, fonte interna]**\[7\] |
| 2. Produção | GMN: entrevista (até D2) → fotos (pedir no D1, receber até D3) → ficha (D3) → OK do cliente (manhã do D4) → preencher e pedir verificação (D4) → posts do mês (até D6) | GC/SEO; operação do painel conforme definirem | D1–D6 | Ficha aprovada por escrito; verificação pedida | Plano de 7 dias GMN, T1–T12 **[Documentada, fonte interna, com base na ajuda do Google]**\[4\] |
| 2. Produção | Tráfego: BM/página → benchmark (Biblioteca de Anúncios) → públicos e orçamento aprovados → criativos (mínimo 3 vídeos, 3 fotos, 3 carrosséis) → bloco único de rastreio (UTMs, GTM, GA4, Pixel, tag Google Ads) → subir campanhas\[2\] | TR (+ LP no rastreio) | D1–D6 | Campanhas no ar, com eventos de conversão disparando e checados | Doc do Guto + decisão de 23/11 **[Documentada, fonte interna]**\[6\]\[7\] |
| 2. Produção | Automação comercial (SDR de IA): infraestrutura VPS → base do cardápio/produtos → fluxo (receptivo, triagem, demonstração, valores, entrega ao humano) → testes com 20 a 30 conversas simuladas → treino | IA + LP (infra) | D1–D10 (15 dias corridos combinados)\[2\] | Bot em produção com regra de transbordo para humano testada | Doc do Guto **[Documentada, fonte interna]**.\[7\] Número de conversas de teste: **[Opinião/heurística]** |
| 3. Aprovação | Rodada 1: apresentação (vídeo Loom de 3 a 5 min + link no grupo, ou reunião de 20 min). Cliente responde em até 48h úteis, com todos os ajustes numa única mensagem | GC | D5 | Lista de ajustes consolidada | **[Opinião/heurística]**: prática de mercado; reduz idas e vindas |
| 3. Aprovação | Rodada 2 (última inclusa): aplicar ajustes; o que passar disso vira escopo novo | LP/TR/SEO | D6 | "Aprovado" por escrito no grupo | **[Opinião/heurística]**: duas rodadas é o padrão mais comum em propostas de agência; não encontrei estudo controlado |
| 4. Entrega (D7) | Publicação + relatório de abertura: marco zero × entregue, status de verificação do GMN, campanhas no ar, próximos 30 dias | GC | D7 | Relatório enviado; cobrança dos 50% restantes (prazo de 7 dias úteis após a entrega)\[3\] | Plano GMN T12 + regra de pagamento de 08/10 **[Documentada, fonte interna]**\[4\] |
| 5. Handoff | Pacote de handoff: documento de acessos (quem é dono de quê; o perfil e a conta de anúncio são do cliente), manual de 1 página do SDR (quando chama humano, horário), glossário de métricas | GC | D7–D8 | Cliente confirma o recebimento | **[Opinião/heurística]** |
| 6. Pós-entrega | Check-in D+7 (verificação do GMN, saída da fase de aprendizado, primeiras conversas do SDR); relatório mensal em dia fixo (o curso sugere dia 6 ou 7, porque o painel do Google fecha o mês com atraso); presença no grupo pelo menos 2 vezes por semana | GC + TR | D+7, D+30, mensal | Relatório mensal; decisão de renovação ou upsell | Checklist do curso GMN **[Documentada, fonte interna]**\[5\] |
| 6. Pós-entrega | Retrospectiva interna de 20 min por cliente: tempo real × estimado, onde travou, o que vira mudança no template | GC + todos | D+8 | Template atualizado (versão v02, v03…) | Retrospectiva do Scrum Guide **[Comprovada/documentada]**\[8\] |

**Definition of Done por produto** **[Comprovada/documentada, conceito]**. O Scrum Guide 2020 trata a Definition of Done como "a formal description of the state of the Increment when it meets the quality measures required" (scrumguides.org).\[8\] Se um item não atende a DoD, ele não pode ser apresentado.\[8\] A lista abaixo é minha adaptação **[Opinião/heurística]**:

- **Landing page:**
  - abre em até 3 s no 4G;
  - passa no teste de dispositivos móveis;
  - botão de WhatsApp com mensagem pré-preenchida e UTM;
  - domínio do cliente com HTTPS;
  - title e meta description com a palavra-chave local;
  - GA4 e Pixel disparando;
  - aprovado por escrito.
- **GMN:**
  - ficha conferida contra os limites do Google;\[4\]
  - OK do cliente guardado;\[4\]
  - verificação pedida com a data registrada;\[4\]
  - fotos enviadas;
  - posts do mês aprovados e, se já verificado, programados.\[4\]
- **Tráfego:**
  - acesso da BM e da conta de anúncio em nome do cliente;
  - orçamento aprovado por escrito;
  - pelo menos 3 variações por formato;
  - eventos de conversão testados (clique no WhatsApp/lead);
  - campanha "ativa" e sem reprovação de anúncio.
- **SDR de IA:**
  - roteiro aprovado;
  - preços vindos da base, não do prompt;
  - transbordo para humano testado;
  - mensagem fora do horário testada;
  - registro das conversas no Chatwoot;
  - 20 a 30 conversas de teste sem erro crítico.

## (b) Rotina diária e semanal por papel

**Capacidade primeiro.** Considerem cerca de 5 a 6 horas de trabalho produtivo por dia por pessoa **[Opinião/heurística]**. O resto vai para comunicação, imprevistos e venda. A coluna "Tempo real (h)" do quadro é o que vai transformar essa heurística em número de vocês:\[1\] depois de 3 ou 4 clientes, somem as horas por pacote e dividam a capacidade semanal por esse valor.

**Lei de Little** **[Comprovada/documentada, teoria de filas; Little, 1961, *Operations Research*]**: tempo médio de entrega = trabalho em andamento ÷ vazão. Na prática:
- com 6 pacotes abertos e capacidade de fechar 2 por semana, o pacote médio leva 3 semanas, mesmo que cada um "caiba" em 7 dias;
- a regra operacional que decorre disso é **não abrir mais D1s por semana do que a média de entregas da semana anterior** **[Opinião/heurística, derivada da lei]**.

**Escalonar os inícios** **[Opinião/heurística]**: no máximo 2 novos D1 por semana enquanto não houver dados. Assim os D4 (aprovações) e os D7 (entregas) não caem todos no mesmo dia.

**Gerald Weinberg** (Quality Software Management, 1992) propôs que cada projeto simultâneo a mais consome cerca de 20% do tempo em troca de contexto: com 2 projetos, cerca de 40% para cada; com 3, cerca de 20% para cada. É **[Opinião/heurística]** de um autor experiente, não dado empírico, mas aponta na mesma direção dos estudos de laboratório sobre custo de troca.

### Rotina diária-padrão (todos)

| Horário | Bloco | Regra |
|---|---|---|
| 08h30–09h00 | Triagem | Ler grupos de clientes e o quadro; mover cartões; nada de execução. **[Opinião/heurística]** |
| 09h00–09h15 | Daily (15 min, em pé ou por vídeo, sempre no mesmo horário) | Cada um diz: o que entregou, o que entrega hoje, o que está travado e por quem. Discussões longas ficam para depois, só com os envolvidos. Scrum Guide: evento de 15 minutos, "at the same time and place every working day" **[Comprovada/documentada]**\[8\] |
| 09h15–12h00 | Bloco de foco 1: **um cliente, um tipo de tarefa** | Notificações desligadas. Gloria Mark (UC Irvine) disse em entrevista que se leva cerca de 23 min para voltar à tarefa após uma interrupção. Esse número vem da entrevista, não de artigo revisado; o artigo CHI 2008 da autora mostra mais velocidade e mais estresse sob interrupção **[acadêmica + entrevista]**. Leroy (2009): o resíduo de atenção piora o desempenho na tarefa seguinte **[Comprovada/documentada]** |
| 12h00–13h00 | Almoço | — |
| 13h00–13h30 | Janela de comunicação com clientes | Responder grupos, cobrar materiais, enviar aprovações. SLA de primeira resposta no grupo: até 4h úteis **[Opinião/heurística]** |
| 13h30–16h30 | Bloco de foco 2 (outro cliente ou rua para vendas) | Dias de rua ficam marcados no calendário e não recebem tarefas G |
| 16h30–17h00 | Atualizar o quadro | Status, "Concluída em" e **tempo real**; registrar travas em "Aguardando: quem"\[1\] |
| 17h00 | Fechamento de caixa (decisão de 23/11)\[6\] | Responsável fixo, 15 min |

### Rotina por papel

| Papel (pessoa hoje) | Diário | Semanal | Métricas do papel (equipe, não ranking) |
|---|---|---|---|
| **Gestor de contas/operações** (Henrique) | Triagem de todos os grupos; cobrar acessos e materiais travados; conduzir aprovações; atualizar "Aguardando" | Segunda: planejamento (puxar do backlog para a semana respeitando a capacidade). Sexta: revisão com cada cliente e retro interna. Envio dos relatórios mensais | % de D1 alcançados em até 48h após a assinatura; dias em "Aguardando cliente"; entregas no D7 |
| **Tráfego** (Igor) | Checagem de 15 min das contas ativas (gasto, reprovações, rastreio); bloco de setup do cliente em D1–D6. Dias de rua sem setup | Otimizações em lote, num dia fixo (não mexer todo dia: edições significativas reiniciam a fase de aprendizado, conforme a documentação da Meta); relatório semanal de uma tela\[8\] | Campanhas no ar até o D7; conversões rastreadas versus cliques no WhatsApp; custo por lead (acompanhar, não usar como meta individual) |
| **Automação/SDR + SEO/copy** (Hugo) | Revisar 10 a 20 conversas reais do SDR do dia anterior e corrigir prompt ou base; bloco de construção do SDR do cliente novo; bloco de copy/SEO | Atualizar a biblioteca de prompts e fluxos reutilizáveis; relatório do SDR (conversas, transbordos, pedidos) | % de conversas com transbordo correto; erros críticos por 100 conversas; reaproveitamento do template (horas por novo SDR caindo) |
| **Landing page/infra** (Bernardo) | Bloco de produção da página do cliente da vez; checagem da VPS/Chatwoot (uptime) | Atualizar o kit de componentes e seções reaproveitáveis (as páginas de demonstração da planilha "Índice de landing pages" viram template); backups\[2\] | Horas por página (deve cair a cada cliente); bugs após o deploy; páginas aprovadas na 1ª rodada |

### Rituais semanais (máximo de 2h somadas, fora a daily)

**[Opinião/heurística, adaptada do Scrum/Kanban]**

- **Segunda, 45 min (planejamento):** revisar a capacidade, decidir quantos D1 abrem na semana e puxar tarefas.
- **Quarta, 15 min (revisão de riscos):** olhar os clientes que estão no D4, porque é ali que o prazo escorrega quando falta aprovação.
- **Sexta, 45 min (revisão e retro):** o que entregou, tempo real × estimado e uma mudança no template.
- **Reuniões estratégicas de 3–4h, como as de 08/10 e 23/11:** viram uma sessão mensal com pauta fechada.\[3\]

## (c) Ficha de tarefa padrão

A planilha atual já tem 15 colunas (A–O).\[1\] Recomendo manter todas e acrescentar 6 campos. Os campos marcados com * são novos.

| Campo | Exemplo | Por quê |
|---|---|---|
| Código | T-231 | Rastreabilidade; nunca reaproveitar (regra já existente)\[1\] |
| Tarefa (verbo + resultado) | "Configurar bloco único de rastreio (GTM, GA4, Pixel, tag Ads)" | Já existe |
| Responsável (um só) | Igor | Um dono por tarefa |
| Revisor* | Bernardo | Quem confere antes de "Feito" (o status "Revisão" já existe; falta o nome) |
| Projeto/cliente | CLI-004 Guto Bebidas | Já existe |
| Produto → serviço* | Gestão de tráfego → Meta Ads | Permite somar horas por produto e precificar |
| Etapa do template + dia-alvo* | TR-06 · D4 | Liga a tarefa ao playbook e ao relógio do D1 |
| Prioridade | Alta (trava cliente ou outras tarefas)\[1\] | Já existe |
| Status | Backlog / A fazer / Fazendo (máx. 3) / Aguardando / Revisão / Feito / Cancelada\[1\] | Já existe; WIP explícito |
| Prazo | 26/11 | Já existe |
| Estimativa | P/M/G | Já existe |
| Semana (sprint) | 2026-S48 | Já existe |
| Depende de | T-228 | Já existe |
| Aguardando quem / desde* | Cliente, desde 24/11 | Mede o tempo travado fora do time |
| Critério de pronto (DoD)* | "Evento de clique no WhatsApp aparece no Gerenciador de Eventos e no GA4" | Evita o "feito" ambíguo |
| Link do entregável / evidência | URL, print | Já existe ("Link ou observação") |
| Criada em / Concluída em | — | Já existe |
| Tempo real (h) | 1,5 | Já existe; é a base de precificação e capacidade\[1\] |
| Rodadas de ajuste* | 1 | Mede o retrabalho de aprovação |

## (d) Ferramentas recomendadas

**Princípio:** a ferramenta certa é a que vocês param de trocar. **[Opinião/heurística]**

| Função | Recomendação agora (até cerca de 10 clientes ativos) | Quando trocar | Etiqueta |
|---|---|---|---|
| Gestão de tarefas | **Google Sheets "Quadro de tarefas ATIVOS" + AppSheet** (decisão de 10/11).\[1\] Mantenham por 90 dias | Acima de 300 tarefas abertas ou necessidade de automações complexas: ClickUp ou Asana (templates de projeto, dependências, controle de tempo nativo). Trello é bom para Kanban simples, mas fraco em relatórios de horas | **[Opinião/heurística]** |
| Templates/SOPs | Google Docs por produto (v01, v02…) + checklists numerados (TR-01…) | — | **[Opinião/heurística]** |
| Comunicação com o cliente | Grupo de WhatsApp por cliente (dono como admin)\[5\] | Se o número de grupos ficar difícil de acompanhar, centralizar no Chatwoot (que vocês já estão implantando) com etiquetas por cliente | Prática do curso GMN **[Documentada, fonte interna]** |
| Comunicação interna | **Google Chat** por setor (avaliado em 23/11), em vez de Slack e Discord ao mesmo tempo\[6\] | — | **[Opinião/heurística]** |
| Aprovações | Vídeo curto (Loom ou gravação de tela) + link de homologação; aprovação "por escrito no grupo" | — | **[Opinião/heurística]** |
| Atendimento/CRM do SDR | Chatwoot (self-hosted, white label) + Evolution API\[3\]\[6\] | Kommo ou RD Station CRM só se o cliente exigir CRM de vendas com funil e não quiser self-hosted | **[Opinião/heurística]** |
| Rastreio | GTM + GA4 + Pixel/CAPI + tag do Google Ads em bloco único (decisão de 23/11)\[2\]\[6\] | — | Documentação da Meta e do Google **[Guia oficial]** |
| GMN | Painel do Perfil da Empresa + GBP Check + mapa em grade (Local Falcon, já usado na prospecção)\[2\]\[4\] | — | **[Documentada, fonte interna]** |
| Relatórios | Looker Studio com modelo único (GA4, Ads, Meta) | — | **[Opinião/heurística]** |

## Produtização: o que os frameworks dizem e como aplicar

- **Productized services (Brian Casel):** transformar um serviço sob medida em oferta com escopo, preço, prazo e processo fixos. É **[Opinião/heurística]**, uma tese de praticante com casos, não pesquisa controlada.
  - Vocês já fizeram a parte da oferta: GMN a R$ 800 de setup + R$ 350/mês; pacotes de R$ 1.500 e R$ 3.000.\[3\]\[6\]
  - Falta o lado da entrega: template de tarefas versionado, DoD por produto e limite de rodadas.
- **Agency Management Institute (Drew McLellan):** defende SOPs, onboarding formal e foco em rentabilidade, com meta de margem na faixa de 20–30% da receita da agência. Não consegui verificar a citação literal; é **[Opinião/heurística]** de consultoria.
- **Utilização de horas:** blogs de ferramentas e a SPI Research citam metas de 70–85% de horas faturáveis em serviços profissionais. Não confirmei a fonte primária. Para sócios que também vendem, usar 60–70% como meta de capacidade é mais realista **[Opinião/heurística]**.
- **Como produtizar na prática** **[Opinião/heurística]**:
  1. Congelar o template do Guto como v01 de cada produto.\[6\]\[7\]
  2. Cada cliente novo usa o template sem alterar.
  3. Mudanças só na retro de sexta, gerando v02.
  4. Depois de 3 clientes, as tarefas com tempo real estável viram candidatas a automação (pesquisa de concorrentes, relatório de palavras-chave, copy-base), que o Igor já está construindo.\[6\]

## Medição e motivação: o que funciona e o que gera efeito colateral

**O que a evidência apoia:**
- **Limitar o WIP e visualizar o fluxo:** o Kanban Guide coloca o controle de WIP como prática central de um sistema puxado **[Comprovada/documentada, guia oficial]**. O limite de 3 itens em "Fazendo" de vocês está correto.\[1\]
- **Medir no nível do time e do fluxo:** lead time do D1 ao D7, % de entregas no prazo, tempo em "Aguardando cliente", rodadas de ajuste. Esses indicadores ajudam a diagnosticar sem incentivar fraude individual. A ligação com a Lei de Little é **[Comprovada/documentada]**; a escolha dos indicadores é **[Opinião/heurística]**.
- **Rituais curtos com horário fixo** (daily de 15 min, retro) **[Comprovada/documentada como prática do Scrum Guide]**.\[8\] A eficácia dependente de contexto é **[Opinião/heurística]**.
- **Proteger blocos de foco:** a pesquisa sobre custo de troca e resíduo de atenção apoia reduzir alternâncias **[Comprovada/documentada, laboratório]**. A transposição para agência é **[Opinião/heurística]**.

**O que gera efeito colateral:**
- **Lei de Campbell (1979):** quanto mais um indicador quantitativo é usado para decisões, mais ele fica sujeito a pressões de corrupção e mais distorce o processo que deveria monitorar **[Comprovada/documentada, texto acadêmico clássico]**.
  - Exemplo na agência: se "tarefas concluídas" der pontos, as tarefas serão fatiadas em pedaços pequenos para pontuar; se "custo por lead" for meta, o tráfego vai comprar leads baratos e ruins.
- **Goals Gone Wild (Ordóñez et al., 2009):** metas específicas e desafiadoras podem estreitar o foco, aumentar o risco e estimular comportamento antiético **[Comprovada/documentada, revisão acadêmica]**.
- **Wells Fargo (CFPB, 2016):** metas agressivas de vendas levaram funcionários a abrir cerca de 1,5 milhão de contas de depósito e cerca de 565 mil pedidos de cartão sem autorização. O banco pagou US$ 185 milhões em multas, dos quais US$ 100 milhões ao CFPB **[Comprovada/documentada, órgão regulador]**.
- **Gamificação:**
  - Hamari et al. (2014) revisaram 24 estudos empíricos. É uma revisão, não uma meta-análise estatística, e conclui que o efeito existe mas depende do contexto e dos usuários.
  - Mollick e Rothbard (2014, Wharton) mostraram que jogos no trabalho melhoraram o afeto positivo só de quem consentia em jogar e pioraram para os demais **[Comprovada/documentada, acadêmica]**.

**Recomendação sobre gamificação** **[Opinião/heurística, apoiada na evidência acima]**:
- Se quiserem algum elemento de jogo, que seja **coletivo e voluntário**. Por exemplo:
  - meta da semana do time ("todos os D7 no prazo"), com uma recompensa compartilhada;
  - quadro visível de "dias sem entrega atrasada";
  - reconhecimento na retro de sexta.
- **Não usar** pontos por tarefa, ranking entre sócios nem bônus individual atrelado a métrica de cliente.
- Metas comerciais (as "5 vendas/semana" discutidas em 08/10) devem ficar separadas das métricas de entrega.\[3\] Assim a pressão de venda não vira pressão para encurtar a definição de pronto.

## Recomendações (em ordem de prioridade)

1. **Esta semana:** decidir por escrito as 4 contradições.
   - Quem opera o GMN.
   - SDR em 15 dias corridos ou 10 dias úteis.
   - Prazos em dias úteis.
   - Regra do D1 = acessos recebidos.

   **[Opinião/heurística]**
2. **Esta semana:** publicar a DoD de cada produto (seção (a)) no topo de cada template e no contrato. O cliente precisa ver que GMN no D7 = "verificação pedida"\[4\] e que tráfego no D7 = "no ar e rastreado". **[Comprovada/documentada, conceito DoD + limites oficiais Google/Meta]**
3. **Próximas 2 semanas:** congelar os templates v01 a partir do Guto, acrescentar os 6 campos novos na planilha e preencher "Tempo real" em 100% das tarefas. **[Opinião/heurística]**
4. **Contínuo:** no máximo 2 novos D1 por semana até haver 4 semanas de dados; depois, abrir D1s conforme a vazão medida (Lei de Little). **[Comprovada/documentada (lei) + heurística (número)]**
5. **Contínuo:** rotina com blocos de foco, daily de 15 min e rituais semanais somando no máximo 2h; reuniões longas viram uma sessão mensal. **[Comprovada/documentada (Scrum Guide, troca de contexto) + heurística (horários)]**
6. **Descartar** a gamificação individual. Se houver, que seja coletiva e voluntária. **[Comprovada/documentada, Campbell, Ordóñez, Mollick & Rothbard]**
7. **Rever em 90 dias:** só então avaliar ClickUp ou Asana, se a planilha não aguentar. **[Opinião/heurística]**

## Caveats

- As fontes externas citadas são referências bibliográficas consolidadas, mas o texto literal não foi conferido ao vivo nesta sessão. Os números da APA (40%), de Gloria Mark (23 min), de Weinberg e das faixas de utilização (70–85%) circulam muito de segunda mão.
  - **APA (40%):** é uma afirmação do resumo da entidade, não um resultado medido.
  - **Gloria Mark (23 min):** vem de entrevista.
  - **Weinberg:** é heurística.
- Não encontrei pesquisa controlada sobre o número ideal de rodadas de aprovação, sobre SLA de resposta em grupos de WhatsApp ou sobre prazos de 7 dias para pacotes de agência. As recomendações nesses pontos são heurísticas de mercado e devem ser ajustadas com os dados de tempo real de vocês.
- A regra de cerca de 50 eventos em 7 dias da Meta pode ter mudado: a API já expõe limites dinâmicos.\[8\] Confiram a Central de Ajuda antes de citar números ao cliente.
- O documento interno do GMN registra divergências entre o Sebrae RN e o Google:
  - categorias adicionais: até 9 no Google contra 3 no Sebrae;\[4\]
  - prazo do cartão-postal: até 14 dias no Google contra 5 a 7 no Sebrae.\[4\]

  Ele também registra que as Perguntas e Respostas do perfil foram encerradas pelo Google em 3/11/2025.\[4\] Em caso de dúvida, sigam a tela do painel.
- Não localizei fontes brasileiras verificadas (Sebrae, RD Station, Operand, mLabs) sobre onboarding de agência. A parte brasileira deste relatório se apoia no material interno e no curso de GMN.

## Fontes

1. [Google Sheets](https://docs.google.com/spreadsheets/d/1g7cFgksYnu7_YpPCewVUtGThya8i46XQOdmxkVNVbl4/edit)
2. Google Drive
3. [Google Drive](https://drive.google.com/open?id=1MmBRlztFkZN37pqhw0c3h4m1CTkUXSXzlOsihAD3Oj4)
4. [Google Drive](https://drive.google.com/open?id=1vwH5YVfleOUBw2nJlnAhX8NZ_lPMv48efjCtsvBW3iw)
5. [Google Drive](https://drive.google.com/open?id=1EwqBJhPhroyHSQ9knRucP0vC9VHjQAa6DaGqhXi7Zfo)
6. [Google Drive](https://drive.google.com/open?id=1GiH5aDcNG4_EaHPE3JhzQJd_J8PjfcEk-OOo3nkzT9w)
7. [Google Drive](https://drive.google.com/open?id=1hh_yUJtKQfaVLVzPpHH9bVd4fpHJAx9kzsXN2WfYWzs)
8. Context7
