---
tipo: cópia de contexto (pesquisa do Igor, texto integral)
original: Drive ATIVOS › 20 Clientes › CLI-004 Guto Bebidas › 03 Entregas › Rankeamento
link: https://docs.google.com/document/d/1Vf-EgX4ahAdmx7dvYu7REJHIsHCCGoM18MR6bE1yh2k/edit
copiado: 24/11/2026
regra: cópia integral; sem contato, CPF, CNPJ, senha nem acesso. Afirmações marcadas "verificar" pelo autor precisam de conferência no texto oficial antes de ir para proposta ou contrato
---

# Posicionamento Digital em 7 dias: workflow validado para landing page + Google Perfil da Empresa + SEO/AEO/GEO (distribuidora de bebidas via WhatsApp)

O seu mapa está certo na sequência criativa, mas faltam as etapas que de fato travam um prazo de 7 dias: o caminho crítico não é o design, e sim **acesso e verificação do Perfil da Empresa no Google (GBP), coleta de materiais do cliente e conformidade (idade 18+ e LGPD)**. Por isso, o briefing e a coleta de acessos precisam acontecer no dia 0, e a trilha de Busca precisa rodar em paralelo com a da landing page, não depois dela. Para AEO/GEO, a posição oficial do Google é que não existe otimização especial além de bom SEO.\[1\] O único método com dado empírico controlado (o paper GEO) mede ganhos de visibilidade com citações, estatísticas e fontes no texto, e não com truques técnicos.

**Nota de método:** nesta sessão não tive ferramenta de busca aberta na web. Confirmei por documentação indexada as fontes oficiais do Google Search Central (IA na Busca, guia de otimização para IA, dados estruturados LocalBusiness, Core Web Vitals) e li os arquivos internos da Ativos no Drive (estimativas P/M/G, checklist de onboarding do curso de GMN, relatório de ranking GBPCheck). Os itens marcados **"(verificar)"** vêm de conhecimento prévio sobre fontes reconhecidas (Whitespark, paper GEO, legislação brasileira, CONAR). Eles estão corretos até onde sei, mas precisam de checagem do texto original antes de entrarem em proposta ou contrato.

**Legenda de evidência:** [OFICIAL] = documentação do Google ou lei · [EMPÍRICO] = estudo com dados · [CONSENSO] = prática de mercado recorrente · [OPINIÃO] = julgamento meu ou de terceiros · [INTERNO] = dado da própria Ativos.

## TL;DR

- **Confirma, com ajustes:** pesquisa de concorrentes → wireframe → front → deploy → CTA → aprovação é a espinha dorsal de mercado. Faltam briefing, coleta de acessos, copy como etapa própria, QA mobile/velocidade, conformidade (aviso 18+, "beba com moderação", LGPD/cookies), rodada de ajuste limitada e handoff com relatório. Motion e pesquisa de 3–5 concorrentes "por seção" são os cortes mais seguros para caber em 7 dias.
- **GBP é o caminho crítico:** o Google ranqueia o local por relevância, distância e proeminência [OFICIAL, verificar]. A categoria principal e as avaliações pesam mais que qualquer ajuste no site, segundo o estudo Whitespark Local Search Ranking Factors (whitespark.ca/local-search-ranking-factors, o mesmo citado no Módulo 06, Aula 07 do curso Escola de SEO) [EMPÍRICO, edição e percentuais a verificar]. Mudanças levam de 1 a 6 dias para aparecer [INTERNO, curso]. A verificação pode estourar o prazo, então peça acesso no D0 e coloque no contrato que o prazo conta a partir do acesso.
- **AEO/GEO:** o Google diz que não há requisito extra para AI Overviews/AI Mode e que pode-se ignorar llms.txt e "chunking" [OFICIAL].\[1\] O paper GEO mostra até ~40% de ganho de visibilidade em respostas generativas com citação de fontes, estatísticas e citações textuais [EMPÍRICO, verificar]. Para negócio local, o que alimenta a IA é o mesmo que alimenta o Maps. O guia de otimização para IA do Google Search Central afirma que "Using products like Merchant Center (such as Merchant Center feeds) and Google Business Profiles can help your products and services to be visible in both AI responses and other Google Search results" [OFICIAL]. Na prática: GBP completo, avaliações, NAP consistente e uma página com fatos claros (bairros atendidos, horário, pedido mínimo, FAQ).

## Key Findings

1. **Capacidade interna x prazo é o risco nº 1 [INTERNO].** Na reunião de 09/11/2026 a equipe estimou 40 h para site e 18 h para ranqueamento por cliente, com dedicação média de 3 h/dia por pessoa a demandas externas.\[2\] São 58 h de trabalho. Com 3 pessoas × 3 h × 5 dias úteis = 45 h, o pacote completo não cabe em 7 dias corridos sem cortar escopo ou usar templates. A boa notícia: as próprias estimativas mostram que, com os templates já prontos (Guto Bebidas, Café 40 etc.), as tarefas viram P/M (pesquisa P, wireframe P, copy M, montagem G, domínio P, revisão P).\[2\]\[3\]
2. **O Google é explícito sobre IA na Busca [OFICIAL, Google Search Central].** "There are no additional requirements to appear in AI Overviews or AI Mode, nor other special optimizations necessary." Também: "You don't need to create new machine readable files, AI text files, or markup to appear in these features. There's also no special schema.org structured data that you need to add."\[1\] O guia de IA manda "Prioritize effective SEO strategies over 'AEO/GEO hacks'" e acompanhar o relatório "Generative AI performance" no Search Console.\[1\]
3. **Dados estruturados: LocalBusiness exige só `name` e `address` [OFICIAL].** Recomendados: `geo` (mínimo 5 casas decimais), `openingHoursSpecification`, `telephone` com código do país, `url`, `priceRange` (menos de 100 caracteres) e o subtipo mais específico possível.\[1\] O Google também lista entre os fundamentos "Making sure your structured data matches the visible text on the page" e "Checking that your Merchant Center and Business Profile information is up-to-date".\[1\]
4. **Core Web Vitals "bom" [OFICIAL, web-vitals/web.dev]:** LCP ≤ 2,5 s, INP ≤ 200 ms, CLS ≤ 0,1.\[1\] Esse deve ser o critério objetivo de "pronto" do QA, não "está rápido".
5. **Ranqueamento local [EMPÍRICO, Whitespark Local Search Ranking Factors, whitespark.ca/local-search-ranking-factors, edição e percentuais a verificar].** Nas edições recentes, os fatores de topo no GBP foram categoria principal, palavra-chave no nome do perfil (que é proibido inserir artificialmente pelas diretrizes do Google), proximidade, endereço na cidade buscada, nota alta e palavras-chave nas avaliações. Para o cliente, isso quer dizer que categoria certa + volume de avaliações rendem mais que o site.
6. **O seu relatório de ranking já mostra onde está o jogo [INTERNO, GBPCheck 19/11/2026].** A Distribuidora de Bebidas Ouro Preto (4,9 ★, 38 avaliações) aparece em 25/25 pontos da grade, com ranking médio de 6,32. A Hudsons Beer (247 avaliações) tem média de 4,56, e a Castelo (229 avaliações), 5,28.\[3\] A diferença é de **proeminência/avaliações**, não de presença. O plano de pós-entrega deve priorizar a placa QR/NFC de avaliação.\[3\]
7. **Bebida alcoólica muda o escopo [OFICIAL/autorregulação, verificar textos].** A ECA art. 243 (redação da Lei 13.106/2015) torna crime vender ou fornecer bebida alcoólica a menor. O Anexo P do CONAR pede advertência ("beba com moderação"/"evite o consumo excessivo de álcool") e filtro de idade em sites. A Lei 9.294/1996 restringe propaganda de bebidas acima de 13 °GL (cerveja costuma ficar fora da lei, mas dentro do CONAR). Na prática, a landing precisa de **portão de idade 18+**, advertência visível e aviso de "venda proibida para menores de 18 anos", e o atendimento no WhatsApp precisa de um passo de confirmação de idade na entrega.
8. **WhatsApp e Meta têm política própria para álcool [CONSENSO, verificar].** A política de comércio do WhatsApp Business restringe a venda de álcool por catálogo/transação, e os anúncios da Meta exigem segmentação 18+ e conformidade local. Prefira o botão "Pedir pelo WhatsApp" com mensagem pré-preenchida em vez de depender do catálogo nativo.

## Details

### Tabela 1 — Serviço 1: Landing page (D0 a D7)

| Etapa | Tarefa | Subtarefas | Entrada necessária | Entregável | Papel responsável | Tempo estimado | Ferramentas | Depende de | Critério de "pronto" |
|---|---|---|---|---|---|---|---|---|---|
| 0. Kickoff | Briefing + handoff comercial→operação | Formulário único; objetivo (pedidos no WhatsApp); oferta (gelo, combos, entrega, pedido mínimo, raio); público; tom; restrições | Contrato assinado; ficha comercial | Doc de briefing aprovado | Gestor de projeto / comercial | 1–2 h (P) | Formulário Notion/Google Forms; grupo WhatsApp | — | Cliente respondeu 100% dos campos obrigatórios e aprovou por escrito |
| 0. Kickoff | Coleta de acessos e materiais | Domínio/Registro.br, número de WhatsApp oficial, logo, fotos reais, cardápio/lista de preços, CNPJ, endereço, horários, links (iFood/Instagram) | Briefing | Pasta do cliente com checklist preenchido | Gestor / operação | 1 h + espera do cliente | Drive, checklist de onboarding | Briefing | Todos os itens recebidos ou com substituto definido (ex.: foto de banco de imagens) |
| 1. Pesquisa | Benchmark enxuto | 2–3 concorrentes locais (do relatório GBPCheck) + 1 referência nacional; anotar promessa, prova, CTA e oferta | Lista de concorrentes do Maps | 1 página de insights (não por seção) | Estrategista/copy | 2 h (P) | GBPCheck, Google Maps, swipe file | Briefing | 3–5 insights acionáveis viraram decisões de copy/layout |
| 1. Pesquisa | Palavras/perguntas que entram na página | Receber do Serviço 2 a lista de termos + perguntas para o FAQ | Relatório de palavras-chave (Serviço 2) | Lista de H1/H2/FAQ | Copy + SEO | 30 min | Planilha | Etapa 2 do Serviço 2 | Termo principal e cidade/bairro definidos para H1 e title |
| 2. Estrutura | Wireframe a partir de template | Hero (promessa + CTA), produtos/combos, como pedir (3 passos), área de entrega, prova social (avaliações Google), FAQ, rodapé com NAP e avisos legais | Insights + briefing | Wireframe de baixa fidelidade | Designer/UX | 2 h (P) | Figma ou template Next.js | Benchmark | Um único objetivo de conversão; CTA visível no topo do mobile |
| 3. Copy | Texto da página | Headline, subtítulos, CTAs, FAQ factual (horário, pedido mínimo, bairros, formas de pagamento, entrega gelada), microcopy do botão | Wireframe, termos, dados do cliente | Copy em doc | Copywriter | 3–4 h (M) | Doc + IA com revisão humana | Wireframe; palavras-chave | Copy revisada, com fatos verificados pelo cliente e advertências legais incluídas |
| 4. Design + front | Artes e montagem | Design system (cores, fonte), fotos tratadas, montagem responsiva, schema LocalBusiness/LiquorStore, meta title/description, OG image | Copy aprovada; fotos | Página em ambiente de teste (URL Vercel) | Designer + dev | 6–8 h (G) | Figma, Next.js, Vercel | Copy | Página navegável em staging, sem lorem ipsum |
| 5. Integrações | CTA e rastreamento | Link wa.me com mensagem pré-preenchida (UTM no texto), botão flutuante, clique-para-ligar, link do cardápio, GA4/GTM com evento de clique | Número oficial do WhatsApp | CTA funcionando + eventos | Dev / dados | 1–2 h (P) | GTM, GA4, wa.me | Montagem | Clique gera evento no GA4 e abre conversa com texto correto |
| 6. Conformidade | Bebida alcoólica + LGPD | Portão de idade 18+; "venda proibida para menores de 18"; "beba com moderação"; política de privacidade; banner de cookies só se houver cookies não essenciais (analytics/pixel) | Dados do controlador (CNPJ, e-mail) | Página de privacidade + banner + age gate | Dev + responsável jurídico/compliance | 1–2 h (P) | CMP leve ou banner próprio | Montagem | Nenhum script de marketing carrega antes do consentimento; avisos visíveis |
| 7. QA | Testes mobile, velocidade e links | Teste em 2 Android + 1 iPhone; PageSpeed; links; NAP igual ao GBP; validação de dados estruturados | Staging | Checklist de QA | Dev (revisor diferente de quem montou) | 1–2 h (P) | PageSpeed Insights, Rich Results Test | Integrações + conformidade | LCP ≤ 2,5 s, INP ≤ 200 ms, CLS ≤ 0,1 no mobile; zero link quebrado |
| 8. Aprovação | Revisão do cliente | Enviar link + vídeo curto (Loom) explicando; 1 rodada consolidada de ajustes | Staging aprovado no QA | Lista única de ajustes | Gestor | 30 min + espera | WhatsApp, Loom | QA | Cliente enviou feedback em um único pacote dentro do prazo combinado (24 h) |
| 9. Ajustes | Rodada de correção | Aplicar ajustes; nova checagem rápida | Lista de ajustes | Versão final | Dev/designer | 1–3 h | — | Aprovação | Aprovação escrita ("pode publicar") |
| 10. Publicação | Domínio e deploy | Apontar DNS; HTTPS; redirecionar www; Search Console + sitemap; pedir indexação | Acesso ao domínio | Site no ar no domínio final | Dev | 1 h (P) + propagação | Registro.br, Vercel, Search Console | Aprovação final | URL final carrega com HTTPS e propriedade verificada no Search Console |
| 11. Handoff | Entrega de acessos e relatório | Transferir/compartilhar acessos; doc "como pedir alteração"; relatório D0 (prints, PageSpeed, eventos) | Tudo acima | Relatório de entrega + termo de aceite | Gestor | 1 h (P) | Doc/PDF | Publicação | Cliente assinou o aceite; acessos documentados no cofre de senhas |

### Tabela 2 — Serviço 2: Google Perfil da Empresa + SEO/AEO/GEO (D0 a D7, em paralelo)

| Etapa | Tarefa | Subtarefas | Entrada necessária | Entregável | Papel responsável | Tempo estimado | Ferramentas | Depende de | Critério de "pronto" |
|---|---|---|---|---|---|---|---|---|---|
| 0. Acesso | Acesso/propriedade do GBP | Descobrir o e-mail proprietário; entrar como **gerente** (o perfil é do cliente); se o perfil for novo, criar e transferir a propriedade; iniciar verificação\[4\] | E-mail do cliente; endereço; telefone | Acesso de gerente ativo | Especialista GBP | 30 min + espera | business.google.com | Contrato | Acesso aceito **ou** verificação iniciada no D0 |
| 1. Marco zero | Diagnóstico inicial | Análise de saúde do perfil; grade de ranking (mesmo raio e grade todo mês); contagem de avaliações x top 3; NAP em diretórios | Acesso | Relatório "inicial" com nota e mapa | Especialista SEO local | 1–2 h (P) | GBPCheck, Maps | Acesso | PDF salvo na pasta do cliente com data\[4\] |
| 2. Público e termos | Pesquisa de público + palavras-chave | Como o cliente busca (ex.: "distribuidora de bebidas perto de mim", "disk cerveja [bairro]", "gelo delivery", "adega 24h"); perguntas reais (horário, entrega, pedido mínimo) | Briefing; marco zero | Relatório de termos com 1 principal + 5–10 secundários + 8–12 perguntas | Especialista SEO | 2 h (P) | SE Ranking/DataForSEO, Google Autocomplete, "As pessoas também perguntam" | Briefing | Termos priorizados e enviados à copy da landing (Serviço 1) |
| 3. Arquitetura | Posicionamento e mapa de entidades | Definir categoria principal + secundárias; descrição; serviços/produtos; atributos; bairros atendidos; como a página e o GBP se espelham | Termos | Doc de arquitetura (1 página) | Especialista SEO | 1 h (P) | Doc | Termos | Categoria principal escolhida com base nos concorrentes que ranqueiam |
| 4. Otimização GBP | Preenchimento completo | Nome **real** (sem palavra-chave inserida); categoria; horário + feriados; telefone/WhatsApp; site (UTM); área de atendimento; descrição; produtos (sem preço de álcool se houver restrição); fotos reais (fachada, interior, produtos, equipe); logo e capa; atributos; primeiras postagens | Materiais do cliente; arquitetura | Perfil 100% preenchido | Especialista GBP | 2–3 h (M) | GBP, Canva/IA para formatar fotos | Acesso + arquitetura | Todas as seções preenchidas; nada viola as diretrizes |
| 5. Avaliações | Sistema de avaliações | Link curto de avaliação; placa QR/NFC no balcão e no entregador; script de pedido no WhatsApp pós-entrega; responder as avaliações existentes | Acesso | Link + placa + script | Especialista GBP + cliente | 1 h (P) | GBPCheck (cards de avaliação), placa NFC | Acesso | Cliente sabe pedir e já pediu às primeiras 10 pessoas |
| 6. On-page | SEO da landing | Title/description com termo + cidade; H1; NAP idêntico ao GBP; mapa incorporado; schema LocalBusiness/LiquorStore com horário e geo; FAQ visível | Arquitetura; staging | Página otimizada | SEO + dev | 1–2 h (P) | Rich Results Test | Serviço 1, etapa 4 | Dados estruturados válidos e iguais ao texto visível |
| 7. AEO/GEO | Conteúdo citável | Bloco de fatos claros (quem, onde, raio de entrega, horário, pedido mínimo, pagamento); FAQ com respostas diretas; prova (nº de avaliações, anos de operação); consistência em Instagram, iFood e diretórios | Arquitetura | Seção "fatos" + checklist de consistência | SEO / copy | 1–2 h (P) | ChatGPT, Gemini, Perplexity, Google AI Mode (para testar) | On-page | Teste de 5 perguntas nos 4 assistentes registrado como marco zero (com prints) |
| 8. Citações locais | NAP consistente | Bing Places, Apple Business Connect, Instagram, Facebook, iFood/Zé (se usar), listas locais | NAP final | Planilha de citações | Assistente SEO | 1–2 h (P) | Bing Places, Apple Business Connect | GBP otimizado | NAP idêntico em todas as plataformas listadas |
| 9. Indexação | Search Console | Verificar propriedade; enviar sitemap; inspeção de URL; ativar acompanhamento do relatório de IA generativa quando disponível | Deploy | Propriedade ativa | SEO | 30 min (P) | Search Console | Publicação | URL inspecionada sem erro |
| 10. Relatório | Entrega + baseline | Antes/depois do GBP; ranking D0; prints dos testes em IA; próximos 30 dias (postagens, avaliações) | Tudo | Relatório de entrega | Especialista SEO | 1 h (P) | GBPCheck, Doc/PDF | Todas | Cliente recebeu e entendeu que o Google leva de 1 a 6 dias para mostrar mudanças e que não há garantia de posição\[4\] |

### Cronograma de 7 dias (o que roda em paralelo)

| Dia | Trilha Landing | Trilha Busca | Cliente |
|---|---|---|---|
| D0 | Briefing + coleta de materiais | Acesso de gerente no GBP / iniciar verificação | Responde ao briefing, envia fotos e acessos |
| D1 | Benchmark enxuto + wireframe | Marco zero + palavras-chave | — |
| D2 | Copy | Arquitetura + início da otimização do GBP | Valida fatos (horário, raio, pedido mínimo) |
| D3 | Design + montagem | GBP completo + sistema de avaliações | Começa a pedir avaliações |
| D4 | Integrações (WhatsApp, GA4) + conformidade | On-page + schema + bloco AEO/GEO | — |
| D5 | QA → envio para aprovação | Citações locais (Bing/Apple/redes) | Feedback consolidado em até 24 h |
| D6 | Ajustes + deploy + Search Console | Indexação + testes em IA (baseline) | Aprovação final |
| D7 | Handoff | Relatório de entrega | Assina o aceite |

O caminho crítico é briefing → copy → montagem → aprovação → deploy. O GBP depende apenas do acesso e pode concluir até o D4 se a verificação não travar [OPINIÃO baseada no fluxo acima].

### Checklist de GBP para negócio local (com nível de evidência)

- **Relevância, distância e proeminência** são a base do ranqueamento local [OFICIAL, Ajuda do Perfil da Empresa "Dicas para melhorar sua classificação local", verificar texto]. Distância não se otimiza. Relevância vem de categoria, descrição e serviços; proeminência vem de avaliações, links e menções.
- **Nome real, sem palavras-chave extras**: as diretrizes oficiais do Google ("Diretrizes para representar sua empresa no Google", support.google.com/business/answer/3038177, as mesmas referenciadas nos Módulos 03 e 08 do curso) proíbem "Distribuidora X – Cerveja Gelada Delivery BH" se esse não for o nome real [OFICIAL, texto a verificar]. Isso gera suspensão. Mesmo que o Whitespark mostre que palavra-chave no nome ajuda, é violação.
- **Categoria principal** é o fator individual mais forte no Whitespark [EMPÍRICO, verificar]. Teste "Distribuidora de bebidas" contra "Loja de bebidas alcoólicas" com base no que os 3 primeiros da grade usam.
- **Avaliações**: volume, recência, nota e resposta do proprietário [EMPÍRICO/CONSENSO]. No caso do cliente, a diferença para o líder é de 38 contra 247 avaliações [INTERNO].\[3\]
- **Fotos reais e postagens** recorrentes, seguindo a "Política de fotos e vídeos do Perfil da Empresa e política de conteúdo das postagens" do Google (support.google.com/business/answer/7213077, citada no Módulo 04, Aula 04 do curso) [OFICIAL]; mudanças aparecem em 1 a 6 dias [INTERNO, curso; CONSENSO].
- **Horários especiais** (feriados, jogos, Réveillon), que são críticos para distribuidora.
- **Verificação**: pode ser por vídeo, telefone/SMS, e-mail ou cartão postal, conforme o Google decidir [OFICIAL, verificar]. Nunca prometa prazo antes de ver o método oferecido.

### AEO/GEO: o que é consenso, especulação e dado

| Afirmação | Nível | Observação |
|---|---|---|
| Não há requisito técnico extra para AI Overviews/AI Mode; vale o SEO normal | OFICIAL (Google, confirmado)\[1\] | A página precisa estar indexada e elegível a snippet\[1\] |
| llms.txt não é usado pela Busca do Google; "chunking" é desnecessário | OFICIAL (Google, confirmado) | Esclarecimento de 15/06/2026: não ajuda nem atrapalha o ranking; pode ser mantido para outros serviços\[1\] |
| Dados estruturados devem bater com o texto visível; GBP atualizado é fundamento\[1\] | OFICIAL (Google, confirmado) | Use schema por higiene, não como "atalho para IA" |
| Adicionar citações de fontes, estatísticas e citações textuais aumenta a visibilidade em respostas generativas (até ~40%); keyword stuffing não funciona | EMPÍRICO (Aggarwal et al., "GEO: Generative Engine Optimization", arXiv 2311.09735, KDD 2024; verificar números) | Experimento em ambiente controlado com benchmark próprio, não em local search brasileiro. Generalize com cautela |
| Menções da marca na web correlacionam com aparecer em respostas de IA | EMPÍRICO correlacional (estudos de ferramentas de SEO, ex.: Ahrefs; verificar) | Correlação, não causa. Para negócio local, as "menções" são avaliações, imprensa local e listas de bairro |
| ChatGPT/Perplexity/Gemini puxam dados de negócios locais de mapas, avaliações e diretórios | CONSENSO/ESPECULAÇÃO | Faz sentido (o Gemini usa o ecossistema Google; outros usam buscadores e parceiros), mas as fontes mudam com frequência. Teste e registre, não prometa |
| "Otimização para IA" garante citação | OPINIÃO de mercado (falsa como promessa) | Não ponha no contrato. Prometa entregáveis (GBP completo, página com fatos, baseline de testes), não posição |

## Recommendations

**(a) O que confirma o seu mapa**
- A sequência pesquisa → wireframe → front → deploy → CTA → aprovação é o fluxo padrão de agência [CONSENSO]. Suas estimativas internas (pesquisa P, wireframe P, domínio P, revisão P) estão coerentes com isso [INTERNO].\[2\]
- Pesquisa de público → palavras-chave → arquitetura → otimização é a ordem correta para SEO local [CONSENSO]. O relatório de palavras-chave deve alimentar a copy da landing, o que seu mapa já sugere.
- Tratar SEO, AEO e GEO como uma frente única é exatamente o que o Google recomenda [OFICIAL].\[1\]

**(b) O que corrige**
- **A Busca não vem depois da landing; roda em paralelo desde o D0.** O GBP depende só do acesso e é o que mais move o ranking local.
- **A pesquisa de concorrentes deve sair do Maps, não do "feeling".** Use os 3 primeiros da grade GBPCheck (Hudsons Beer, Castelo) e não 3–5 sites com análise por seção.\[3\]
- **"Ajuste do botão" vira uma etapa de integração e mensuração**: link wa.me com texto pré-preenchido, evento no GA4 e teste em celular real.
- **"Aprovação do cliente" precisa de regra**: 1 rodada consolidada, prazo de resposta de 24 h e cláusula de que o prazo de 7 dias pausa enquanto o cliente não responde ou não dá acesso.
- **"Otimização AEO/GEO" deve ser reescrita como "conteúdo factual citável + consistência de dados + baseline de testes em IA"**, sem promessa de aparecer.

**(c) O que falta**
1. Briefing formal e handoff comercial→operação (a própria equipe decidiu que a coleta de acessos é a primeira tarefa da operação) [INTERNO].\[2\]
2. Coleta de acessos/materiais em lista única (domínio, WhatsApp oficial, fotos, horários, e-mail proprietário do GBP).
3. Copy como etapa própria (estimada em M internamente).\[2\]
4. Conformidade para bebida alcoólica: portão 18+, advertência e aviso de venda proibida a menores; confirmação de idade no fluxo do WhatsApp e na entrega.
5. LGPD: política de privacidade, base legal do contato via WhatsApp e consentimento antes de pixel/analytics não essenciais [OFICIAL, LGPD + guia de cookies da ANPD, verificar].
6. QA com critério numérico (Core Web Vitals) e teste em aparelho real.\[1\]
7. Schema LocalBusiness e NAP idêntico entre site, GBP e redes.\[1\]
8. Sistema de avaliações (placa QR/NFC + script), que é a maior alavanca do caso.\[3\]
9. Search Console + sitemap + baseline de testes em IA.
10. Handoff: entrega de acessos, termo de aceite e relatório D0 com próximos 30 dias, que é a ponte para a mensalidade.

**(d) O que poderia cortar (ou mover para a mensalidade)**
- **Motion**: não muda a conversão de um negócio que vende por WhatsApp e ameaça LCP/INP. Corte, ou use só microanimações em CSS [OPINIÃO informada pelos limiares de Core Web Vitals].
- **Pesquisa de 3–5 concorrentes "por seção"**: reduza para 1 página de insights em 2 h.
- **Design system completo por cliente**: use a paleta e a fonte do template do segmento (Guto Bebidas já existe) [INTERNO].\[3\]
- **llms.txt e "markup para IA"**: o Google diz que é desnecessário para a Busca [OFICIAL].\[1\] Não gaste horas nisso.
- **Postagens no GBP, citações extras e relatórios mensais**: entregue 1–2 postagens no setup e mova o restante para a recorrência, como o próprio curso recomenda [INTERNO].\[3\]

## Caveats

- **Fontes não abertas nesta sessão:** os percentuais do Whitespark, os números exatos do paper GEO, o texto da Ajuda do GBP, a Lei 9.294/1996, a ECA art. 243, o Anexo P do CONAR, o guia de cookies da ANPD e as políticas de álcool do WhatsApp e da Meta estão marcados "(verificar)". Confirme no original antes de citar em proposta ou contrato. As afirmações do Google Search Central sobre IA, LocalBusiness e Core Web Vitals foram confirmadas.
- **Não consegui levantar SOPs públicos específicos** (Unbounce, HubSpot, RD Station, Rock Content, templates de ClickUp/Notion) nesta sessão. O fluxo da Tabela 1 reflete prática de mercado recorrente [CONSENSO] e as estimativas da própria Ativos [INTERNO], não um playbook citável de terceiros.
- **Tempos são para 1 cliente com template pronto.** No primeiro cliente de um segmento novo, a própria equipe notou que tudo demora mais.\[2\]
- **Este relatório não é parecer jurídico.** Para bebida alcoólica e LGPD, valide os avisos e a política de privacidade com um advogado antes de escalar o produto.

## Fontes

1. Context7
2. [Google Drive](https://drive.google.com/open?id=1gDLDEKKBsR54iitH4ZBKpDPpQ0aO_KgO0GTZMvR9Daw)
3. Google Drive
4. [Google Drive](https://drive.google.com/open?id=1EwqBJhPhroyHSQ9knRucP0vC9VHjQAa6DaGqhXi7Zfo)
