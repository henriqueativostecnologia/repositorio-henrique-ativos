---
tipo: cópia de contexto (de-para do Igor, texto integral)
original: Drive ATIVOS › 40 Processos › 42 Fluxos dos serviços
link: https://docs.google.com/document/d/1Z1aWWhbZAxbfCAMEP-wPKge3cFtMi6K_FJ1klyP_nAs/edit
copiado: 24/11/2026
situacao: documento com o status das decisões (todas 'Aberto' em 24/11; reexportar depois da reunião)
regra: cópia integral; sem contato, CPF, CNPJ, senha nem acesso. Consolida as 4 pesquisas e vira a versão 2 das receitas de servicos/ depois da reunião. Canal do WhatsApp: ver servicos/automacao-comercial/referencias/whatsapp-regras-oficiais-e-casos-2026-11-24.md (decisão da fase 1 do Igor)
---

# Ativos · De-para e operação padrão de 7 dias

Nov 24, 2026 · @Ativos Tecnologia

## Resumo e convenções

Seu mapa acerta a ordem dos seis serviços. A pesquisa muda o que vem antes e depois de cada etapa, não a sequência criativa. Quatro mudanças valem para todos os produtos:

1. **O relógio começa no acesso, não na assinatura.** D0 é o onboarding (briefing, acessos e materiais). D1 é o primeiro dia útil depois que o último acesso crítico chega. Os dias do relógio são úteis, de segunda a sexta (ponto em aberto 1).
2. **Entram as etapas que travam o prazo:** coleta e teste de acessos, verificações do Google e da Meta, aprovação com regra (um pacote só, resposta em 24 h úteis) e QA antes de publicar.
3. **Bebida alcoólica muda o setup desde o D1:** 18+ na landing, nos anúncios e no WhatsApp, advertência do CONAR nas peças e LGPD no site e no atendimento.
4. **O canal do WhatsApp decide dois produtos.** A política do WhatsApp, atualizada em 23/09/2026 e lida hoje, proíbe mensagens sobre álcool no app WhatsApp Business e proíbe catálogo e carrinho para álcool. No Brasil, a mensagem sobre álcool só é permitida pela Plataforma (API), seguindo a lei local e só para maiores de 18. Sem a API também não existe o `ctwa_clid`, então não há rastreio do anúncio até a venda. Recomendação: número de vendas na Cloud API e atendimento humano pelo Chatwoot (ponto em aberto 2).

**O que conta como pronto em cada produto**

| Produto | Pronto no | Definição de pronto |
| --- | --- | --- |
| Landing page | D7 | No ar no domínio do cliente, com 18+ e LGPD, botão medido, LCP ≤ 2,5 s no celular e aprovação por escrito |
| Perfil da Empresa no Google | D7 | Perfil preenchido, verificação pedida (ou perfil já verificado), sistema de avaliações entregue e 2 posts aprovados |
| Tráfego (Meta e Google) | D7 | Campanhas publicadas ou em revisão, rastreio aprovado no QA, otimização para conversas; o aprendizado leva de 2 a 4 semanas |
| SDR de IA | D10 | Piloto controlado no ar com humano de plantão, preço vindo só do banco e idade verificada; vira produção depois de 48 h sem incidente crítico |

O pacote completo soma cerca de 144 h por cliente. Com a dedicação medida em 09/11 (3 h por dia por pessoa), ele não cabe no relógio; nos dias de pico é preciso perto de 5 h (seção Capacidade).

**Códigos de fonte usados nas tabelas**

- **DOC**: sua documentação CLI-004 (23/11)
- **PGMN**: Plano de 7 dias do perfil, do setor de SEO (23/11)
- **PPOS**: pesquisa Posicionamento Digital em 7 dias
- **PSDR**: pesquisa SDR de IA no WhatsApp
- **PTRA**: pesquisa Meta Ads e Google Ads com rastreio via WhatsApp
- **POPE**: pesquisa Operação padrão da agência
- **WA-POL**: [WhatsApp Business Messaging Policy](https://whatsappbusiness.com/policy/), lida em 24/11/2026

Nível da evidência, entre colchetes: **oficial** (documentação da plataforma ou lei), **empírico** (estudo), **mercado** (prática de agência), **interno** (dado da Ativos), **opinião** (julgamento). "Verificar" marca o que a pesquisa citou sem abrir o texto original.

## Conflitos de responsável e de regra

Os cinco pontos que você anotou estão resolvidos abaixo com uma proposta; confirme os marcados com "confirmar". As pesquisas trouxeram mais cinco conflitos, listados depois da linha 5. O critério de desempate foi a carga em horas de cada pessoa no pacote (seção Capacidade): Henrique 24 h, Igor 29 h, Hugo 38,5 h e Bernardo 40,5 h.

| # | Ponto | O que cada fonte diz | Resolução proposta | Situação |
| --- | --- | --- | --- | --- |
| 1 | Responsáveis na landing page | DOC: só domínio e deploy têm dono (Bernardo). Painel lateral: Igor na pesquisa e no wireframe, Hugo na copy | Bernardo é o dono e faz wireframe, design, front, integrações, conformidade e deploy. Hugo faz o benchmark de sites e Maps e toda a copy (landing, descrição do perfil, posts, bio). Igor entra só com as tags. O QA fica com o Henrique, com checklist | Resolvido, confirmar. Igor tem a maior carga fora do SDR e ainda vende na rua; quem escreve a copy já modela a partir da referência (DOC) |
| 2 | Perfil da Empresa e busca | DOC: serviço com o Henrique. Painel lateral: Hugo em público e palavras-chave. PGMN: Igor opera o painel e é o único no GBP Check | Henrique é dono e executor: acesso, entrevista, palavras-chave, arquitetura, ficha, painel, verificação, avaliações, citações e baseline em IA. Hugo escreve a descrição e os posts. Igor roda só o GBP Check | Resolvido, confirmar. Henrique tem a menor carga; Hugo já leva SDR e copy. Falta o ponto em aberto 9 (acesso do Henrique ao GBP Check) |
| 3 | Prazos | DOC: Gantt só com 3 entregas; automação e perfil sem prazo; posicionamento fora do Kanban. Ata de 23/11 (citada em POPE e PTRA): 7 dias para tráfego, perfil e landing; 15 para o SDR | Todos os serviços entram no relógio: landing, perfil e tráfego de D1 a D7; SDR de D1 a D10 úteis, dentro dos 15 corridos. Posicionamento digital deixa de ser entrega à parte: é o produto que junta landing e perfil. No Kanban, 1 cartão por serviço | Resolvido; falta úteis ou corridos (ponto 1) |
| 4 | Cardápio | DOC: Hugo monta o cardápio no WhatsApp Business; Bernardo, o banco do cardápio | O catálogo nativo sai, porque WA-POL proíbe catálogo e carrinho para álcool \[oficial\]. O cardápio do SDR é o banco: Bernardo faz a estrutura e a sincronização; Hugo e o cliente carregam produtos, preços e fotos; o SDR manda foto por SKU e o link do cardápio digital | Resolvido |
| 5 | Tags no Google Ads | DOC: GTM, Analytics, pixel e tag do Google Ads descritos só no Meta | Bloco único de rastreio para os dois canais, decidido na reunião de 23/11 (PTRA). Dono: Igor. Bernardo instala o contêiner na landing e cuida do webhook e do n8n | Resolvido |
| 6 | Dono da conta de anúncios | DOC: vincular a conta do cliente à nossa BM. PTRA: conta e portfólio são do cliente, com a Ativos como parceira | A Ativos entra como parceira no portfólio do cliente, com pagamento no nome dele \[mercado\] | Resolvido |
| 7 | Canal do WhatsApp | PSDR: piloto aceitável na conexão não oficial, com número dedicado. PTRA: o número que recebe anúncio precisa da API oficial. WA-POL: mensagem sobre álcool proibida no app | Cloud API no número de vendas; conexão não oficial só para testes internos | Aberto (ponto 2) |
| 8 | Contagem do dia | PPOS: D0 = briefing e acesso. PGMN: D1 = dia do acesso. POPE: D1 = último acesso crítico, dias úteis. PTRA: dias corridos | D0 = onboarding; D1 = primeiro dia útil depois do último acesso crítico | Resolvido; úteis ou corridos no ponto 1 |
| 9 | Rodadas de aprovação | PPOS e PTRA: 1 rodada, resposta em 24 h. POPE: 2 rodadas e 48 h úteis, mas ela mesma avisa que não cabe no D6 | 1 pacote de aprovação no D5, resposta até 12h do D6 e ajustes no D6. Atraso do cliente pausa o relógio | Aberto (ponto 4) |
| 10 | Posts do perfil | PGMN: posts do mês 1 inteiro no setup. PPOS: 1 ou 2 no setup, o resto na recorrência | 2 posts e o calendário do mês no setup; o resto entra na mensalidade | Aberto (ponto 5) |

## De-para · Posicionamento Digital · Landing page

Das 7 etapas do seu mapa, 1 fica como está, 6 mudam e 7 entram; nenhuma sai. A maior mudança: a publicação vai para depois da aprovação, e entram copy, conformidade 18+ e QA com critério numérico.

| Etapa do meu mapa | Equivalente no mercado | Decisão | Justificativa com fonte |
| --- | --- | --- | --- |
| — | Briefing único e coleta de acessos e materiais no D0 | Adicionar (vai para o onboarding) | PPOS e POPE: briefing e acesso destravam o D1 \[mercado\]. O checklist do curso de GMN pede tudo num documento só, não pelo chat \[interno\] |
| 1. Pesquisa de mercado (3 a 5 concorrentes, seção por seção) | Benchmark enxuto: 2 a 3 concorrentes do topo do Maps e 1 referência nacional, em 1 página de insights | Ajustar | PPOS: os concorrentes saem da grade do GBP Check (Hudsons Beer, Castelo), em 2 h; análise por seção é o corte mais seguro para caber em 7 dias \[mercado, opinião\]. DOC: a copy sai da referência, então o benchmark continua |
| — | Palavras e perguntas da trilha de busca entram na página | Adicionar | PPOS: o relatório de termos define H1, title e FAQ \[mercado\]. Evita fazer a pesquisa de palavras duas vezes |
| 2. Wireframe | Wireframe a partir do template do segmento | Manter | PPOS: hero com CTA, combos, como pedir em 3 passos, área de entrega, avaliações, FAQ e rodapé com endereço e avisos \[mercado\]. Estimativa interna: P \[interno\] |
| — | Copy como etapa própria, com FAQ factual e bloco de fatos | Adicionar | PPOS: copy M (3 a 4 h) na estimativa da reunião de 09/11 \[interno\]. O FAQ factual é o que alimenta busca e IA \[oficial: Google Search Central\] |
| 3. Artes e front-end | Design e montagem numa URL de teste, com meta tags e schema | Ajustar | PPOS: a página vai ao cliente num endereço de teste, não no domínio final \[mercado\]. No Guto a página já subiu antes da aprovação (DOC) |
| 4. Motion | Opcional: só microanimações em CSS | Ajustar (opcional) | PPOS: motion não muda a conversão de quem vende pelo WhatsApp e pesa no carregamento \[opinião\]; limites do Core Web Vitals \[oficial\]. No Guto já está feito: fica se passar no QA |
| — | Conformidade de bebida alcoólica e LGPD | Adicionar | PPOS: portão 18+, "venda proibida para menores de 18 anos", "beba com moderação" (ECA art. 243 e CONAR Anexo P) \[oficial, verificar o texto\]. LGPD: política de privacidade e consentimento antes de pixel e analytics \[oficial\] |
| 6. Ajuste do botão | Integração e medição: wa.me com mensagem pronta e código curto, botão flutuante, evento no GA4, teste em celular real | Ajustar | PPOS \[mercado\]. PTRA: o código curto na mensagem liga o clique do Google (GCLID) à venda no CRM \[mercado\] |
| — | QA no celular e de velocidade, feito por quem não montou | Adicionar | PPOS: LCP ≤ 2,5 s, INP ≤ 200 ms, CLS ≤ 0,1 no celular \[oficial\]; revisor diferente do montador \[mercado\] |
| 7. Aprovação | 1 pacote de aprovação, resposta em 24 h úteis, relógio pausado sem resposta | Ajustar | PPOS e PTRA: 1 rodada e 24 h \[mercado\]. POPE propõe 2 rodadas, mas admite que não cabem no D6 \[opinião\] |
| — | Rodada de ajustes | Adicionar | PPOS: 1 a 3 h, com "pode publicar" por escrito \[mercado\] |
| 5. Domínio e deploy | Publicação no fim: DNS, HTTPS, www, Search Console e sitemap | Ajustar (muda de lugar) | PPOS: publicar só depois do "pode publicar" e já com Search Console \[mercado\]. O acesso ao domínio é pedido no D0, para o DNS não travar |
| — | Entrega de acessos, termo de aceite e relatório | Adicionar (vai para a entrega) | PPOS e POPE \[mercado\]; o aceite libera a cobrança dos 50% restantes (reunião de 08/10) \[interno\] |

## De-para · Posicionamento Digital · Perfil da Empresa, SEO, AEO e GEO

Seu mapa tem 4 etapas de estratégia e nenhuma de execução no painel. Das 4, 1 fica, 3 mudam e entram 10, quase todas do seu próprio Plano de 7 dias do perfil (PGMN). Saem 2 táticas que o Google descarta. O caminho crítico é o acesso no D0 e a verificação pedida no D4.

| Etapa do meu mapa | Equivalente no mercado | Decisão | Justificativa com fonte |
| --- | --- | --- | --- |
| — | Acesso e propriedade do perfil no D0, por convite, nunca com senha | Adicionar | PGMN T1 \[oficial: [Ajuda do Google](https://support.google.com/business/answer/3403100)\]. PPOS: o perfil depende só do acesso e é o que mais move o ranking local \[opinião\] |
| — | Marco zero antes de mexer: prints, grade do GBP Check, desempenho | Adicionar | PGMN T2: corrigir antes de documentar impede provar a melhora \[interno\] |
| — | Entrevista de 15 perguntas e documentos (fachada com nome, comprovante) | Adicionar | PGMN T3: fachada sem nome e falta de comprovante reprovam o vídeo de verificação \[oficial: [Ajuda do Google](https://support.google.com/business/answer/14271705)\] |
| 1. Pesquisa do público-alvo | Público e termos numa tarefa só | Ajustar (fundir com a 2) | PPOS: "público e palavras-chave" em 2 h \[mercado\]. PGMN T5: volume medido na cidade, não no país \[curso, interno\] |
| 2. Relatório de palavras-chave | Relatório único: 1 termo principal, 5 a 10 secundários e 8 a 12 perguntas, que alimenta landing, perfil e Google Ads | Ajustar | PPOS \[mercado\]. PTRA usa os mesmos grupos no Google Ads \[mercado\]. Uma pesquisa só para três serviços |
| 3. Arquitetura de posicionamento | Categoria principal e adicionais, descrição, serviços, atributos, bairros e o espelho entre página e perfil | Manter (com mais escopo) | PPOS: categoria escolhida pelo que os 3 primeiros da grade usam. Whitespark: categoria principal é o fator individual mais forte \[empírico, verificar a edição\] |
| — | Ficha do perfil e conferência contra os limites do Google | Adicionar | PGMN T6 e T7 \[oficial: [Diretrizes do Google](https://support.google.com/business/answer/3038177)\]. Nome real, sem palavra-chave, para evitar suspensão. Categorias adicionais: o Google diz até 9 e o Sebrae, 3; vale o que o painel mostrar |
| — | OK do cliente na ficha antes de preencher | Adicionar | PGMN T8: sem o OK até o meio do D4, a verificação começa tarde e a entrega escorrega \[opinião\] |
| 4. Otimização SEO, AEO e GEO | Três tarefas concretas: preencher o perfil; SEO da página (schema e endereço igual ao perfil); bloco de fatos citáveis e baseline de testes em IA | Ajustar (reescrever) | Google: não há otimização especial para AI Overviews e AI Mode além de bom SEO \[oficial, confirmado na PPOS\]. Paper GEO: citações, números e fontes elevam a visibilidade \[empírico, verificar\]. Não prometer aparição em IA \[opinião\] |
| — | Verificação pedida no mesmo dia do preenchimento (D4) | Adicionar | PGMN T10: a análise do vídeo leva até 5 dias úteis; o cartão-postal, até 14 \[oficial\]. Por isso o D7 é "perfil preenchido e verificação pedida" |
| — | Sistema de avaliações: link curto, placa QR ou NFC, script pós-entrega | Adicionar | PPOS: no GBP Check de 19/11, o perfil do cliente tem 38 avaliações contra 247 do líder \[interno\]; avaliações estão entre os fatores mais pesados \[empírico\] |
| — | Citações locais: mesmo nome, endereço e telefone em Bing, Apple e redes | Adicionar | PPOS \[mercado\]. Pode ir para a mensalidade se faltar hora |
| — | Posts de abertura | Adicionar (reduzido) | PGMN T11 pede o mês inteiro; PPOS manda 1 ou 2 no setup e o resto na recorrência \[interno, curso\]. Proposta: 2 posts e o calendário |
| — | Search Console, sitemap e relatório com baseline | Adicionar | PPOS: acompanhar o relatório de IA generativa no Search Console \[oficial\] |
| (Sebrae) Responder as "Perguntas esperadas" | — | Remover | PGMN: o Google encerrou as Perguntas e Respostas do perfil em 3/11/2025 |
| (mercado) llms.txt e markup "para IA" | — | Remover | PPOS: o Google diz que não usa llms.txt e que não há schema especial para IA \[oficial\] |

## De-para · Automação Comercial · SDR de IA e infraestrutura

O fluxo de 5 passos do seu mapa é o padrão de mercado e fica. O que muda vem antes dele: a decisão de canal, o discovery e as regras do negócio. O cardápio no WhatsApp Business sai do piloto. A política do WhatsApp lida hoje vai além das pesquisas: ela proíbe mensagem sobre álcool no app e exige filtro de idade e caminho para humano.

| Etapa do meu mapa | Equivalente no mercado | Decisão | Justificativa com fonte |
| --- | --- | --- | --- |
| — | Decisão de canal antes da infraestrutura: Cloud API ou conexão não oficial; número atual ou dedicado | Adicionar | WA-POL: "prohibited from messaging about any Regulated Verticals" no app; álcool é vertical regulada e, no Brasil, só vale pela Plataforma \[oficial, lido em 24/11\]. PSDR: o README da Baileys desencoraja uso automatizado e lista o erro 463, conta restrita \[documentado\]. PTRA: sem API oficial não há `ctwa_clid` \[oficial, via doc interna GM-03.1\] |
| Prazo: "sem prazo definido" (DOC) | 15 dias corridos combinados em 23/11 = D1 a D10 úteis; a entrega é um piloto controlado | Ajustar | POPE e PTRA citam a ata de 23/11 \[interno\]. PSDR: em 7 dias cabe um piloto, não o produto completo \[heurística\] |
| — | Discovery: 50 a 100 conversas reais, FAQ, objeções, regras do negócio, tom de voz e linha de base | Adicionar | PSDR: é a etapa que mais falta e a que mais decide a qualidade \[heurística\]. Toda regra com número ou lista fechada, sem "depende" |
| Servidor (VPS) (Bernardo) | Infra com HTTPS, firewall, usuário sem root, SSH por chave, cofre de senhas e homologação | Ajustar | PSDR. Reunião de 01/10: senha root compartilhada em grupo e chave vazada na VPS antiga \[interno\] |
| Cardápio no WhatsApp Business (Hugo) | Cardápio no banco próprio, foto por SKU e link do cardápio digital; catálogo nativo fora | Remover do piloto | WA-POL: proibido oferecer experiência de comércio (catálogo, carrinho) para vertical regulada \[oficial, lido em 24/11\]. CDC art. 30: a oferta precisa obriga o fornecedor \[oficial\] |
| Banco de dados do cardápio (Bernardo) | Banco com SKU, preço, foto e frete por bairro, atualizado pelo cliente por planilha | Manter (com mais escopo) | PSDR: preço consultado por ferramenta, nunca "lembrado" pela IA \[heurística\]. Pronto quando o cliente muda um preço e o bot responde o novo valor em até 5 min |
| — | Prompt em estados, ferramentas (function calling) e base de conhecimento | Adicionar | PSDR: `consultar_preco`, `calcular_frete`, `enviar_foto`, `montar_resumo`, `transferir_humano` \[heurística\] |
| 1. Receptivo | Receptivo com aviso de privacidade na 1ª mensagem | Ajustar | WA-POL e LGPD: política de privacidade publicada e avisos necessários \[oficial\]. Dizer que é IA é boa prática \[heurística\] |
| 2. Triagem | Triagem com confirmação de maioridade antes de ofertar | Ajustar | WA-POL: mensagens "gated per legal age" e nenhuma para menores de 18 \[oficial\]. ECA art. 243 \[oficial\]. O entregador confere documento |
| 3. Demonstração | Foto e arte vindas do banco (`enviar_foto(sku)`) | Ajustar | PSDR; WA-POL (sem catálogo). Imagens JPEG ou PNG de até 5 MB \[documentado, verificar\] |
| 4. Valores e fechamento | Preço e frete por ferramenta; área, pagamento e troco; resumo confirmado pelo cliente | Ajustar | PSDR: sem resumo, o humano refaz a triagem \[heurística\]. CDC art. 30 \[oficial\]. Se coordenar pedido conta como "experiência de comércio", WA-POL não diz (ponto em aberto 3) |
| 5. Entrega ao humano | Transbordo: o bot para, etiqueta `pedido_pronto` e resumo ao atendente em menos de 1 min | Manter (com critério) | WA-POL: automação exige caminho claro para humano \[oficial\]. Chatwoot: estados open e pending \[documentado\] |
| Regra: follow-up | 1 tentativa dentro da janela de 24 h; depois, só template aprovado e com opt-in | Ajustar | WA-POL: fora da janela de 24 h, só template aprovado \[oficial\] |
| Regra: fora do horário | Mantém; o cliente decide se aceita pedido agendado | Manter | PSDR \[heurística\] |
| — | Marcação da venda no Chatwoot, com valor e origem | Adicionar | PTRA: sem isso "rastrear até a compra" não existe \[opinião\] |
| Testes e treino (Hugo) | 40 a 60 casos, red team e teste do cliente (UAT), com critério de pronto | Ajustar | PSDR: 90% de acerto e 100% nos casos críticos (preço, idade, transbordo) \[heurística\]. POPE fala em 20 a 30 conversas; ficou o roteiro maior por ser bebida alcoólica |
| — | Monitoramento, logs e backup fora da VPS | Adicionar | PSDR \[heurística\]. Resolução ANPD 15/2024: incidente relevante comunicado em 3 dias úteis \[oficial, verificar\] |
| — | LGPD do atendimento: base legal, retenção, contrato de operador | Adicionar | PSDR: o cliente é o controlador e a Ativos, a operadora \[oficial: LGPD\] |
| Subida na VPS (Bernardo) | Go-live controlado: horário ou volume limitado, humano de plantão, desligar com 1 clique | Ajustar | PSDR: 48 h sem incidente crítico antes de virar produção \[heurística\] |
| — | Revisão diária de conversas e regressão a cada mudança de prompt | Adicionar | PSDR \[heurística\] |

## De-para · Gestão de Tráfego · Meta Ads

As 8 etapas do seu mapa estão na ordem certa; 4 ficam e 4 mudam. As duas correções de peso: o rastreio roda em paralelo aos criativos, não depois, e o remarketing sai do D7. Entram aprovação, QA e o funil de venda no CRM.

| Etapa do meu mapa | Equivalente no mercado | Decisão | Justificativa com fonte |
| --- | --- | --- | --- |
| 1. Página do Facebook | Página e Instagram com restrição de idade 18+ | Manter (com 18+) | [Política de anúncios de álcool da Meta](https://transparency.meta.com/pt-br/policies/ad-standards/restricted-goods-services/alcohol/): não direcionar a menores de 18 e seguir a lei local \[oficial, lido em 24/11\] |
| 2. Business Manager | Conta de anúncios no portfólio do cliente, com a Ativos como parceira; pagamento do cliente; 2FA; verificação da empresa e do domínio | Ajustar | PTRA: a conta pertence ao cliente \[mercado\]. A verificação pode levar dias, por isso é disparada no D1 \[oficial\] |
| 2b. "Integrar também o WhatsApp" | WhatsApp na Plataforma (Cloud API), com webhook que grava o `ctwa_clid` | Ajustar (vira etapa própria, ligada à decisão de canal) | PTRA: o `ctwa_clid` chega no objeto `referral` da 1ª mensagem, só na API oficial \[oficial, via GM-03.1\]. WA-POL: álcool só na Plataforma \[oficial\] |
| 3. Benchmark de concorrência | Biblioteca de Anúncios e perfis do Maps; swipe file de 10 a 20 anúncios e 3 ângulos | Manter | PTRA \[mercado\]. Fica no mesmo documento do benchmark da landing, para não pesquisar duas vezes |
| 4. Estratégia e públicos | 1 campanha e 1 conjunto (raio + 18+ + público amplo); o 2º só com cerca de 50 conversas por semana em cada; orçamento aprovado por escrito | Ajustar | PTRA: o conjunto sai do aprendizado com cerca de 50 eventos em 7 dias \[oficial, número aproximado\]; muitos públicos pulverizam o aprendizado \[mercado\] |
| 5. Produção de criativos (3 vídeos, 3 fotos, 3 carrosséis) | Lote 1 de 9 peças com advertência do CONAR e modelos adultos; depois 2 a 4 a cada 2 semanas | Manter (com compliance) | PTRA: 9 peças bastam para 1 ou 2 conjuntos \[mercado\]. CONAR Anexo P exige advertência em toda peça \[oficial, verificar o texto\] |
| 6. Rastreio e dados | Bloco único de rastreio do D3 ao D5, com a API de Conversões para mensagens (`LeadSubmitted` e `Purchase`) | Ajustar (antes dos criativos ficarem prontos) | PTRA: depende de WABA, webhook e CRM, que demoram mais que os criativos \[mercado\]. Bloco único decidido em 23/11 \[interno\] |
| — | Funil de venda no Chatwoot: conversa, qualificado, pedido, pago, com valor | Adicionar | PTRA: sem o valor da venda não há o que devolver à Meta \[opinião\] |
| — | Aprovação de criativos e textos pelo cliente | Adicionar | PTRA \[mercado\]. Entra no pacote único de aprovação do D5 |
| — | QA de rastreio e anúncio, com checklist assinado | Adicionar | PTRA: evento de teste no Events Manager, mensagem pronta e código no CRM \[mercado\] |
| 7. Subir campanhas | Publicar no D6, otimizando para conversas | Manter | PTRA: revisão da Meta em até 24 h \[oficial\]; só otimizar para compra com dezenas de vendas por semana \[opinião\] |
| 8. Remarketing | Planejar os públicos no D6 e ativar quando houver tamanho, de 2 a 4 semanas depois | Ajustar (sai do D7) | PTRA \[mercado\] |
| — | Relatório de setup com a expectativa de aprendizado | Adicionar | PTRA \[mercado\]. Corrige a premissa de "aquecimento de conta" da reunião: o aprendizado só começa quando o conjunto entrega \[oficial\] |

## De-para · Gestão de Tráfego · Google Ads e bloco único de rastreio

As 7 etapas do seu mapa batem com o fluxo de mercado para negócio local; 4 ficam e 3 mudam. Falta o que faz o Google aprender: conversão configurada e o GCLID levado até a venda.

| Etapa do meu mapa | Equivalente no mercado | Decisão | Justificativa com fonte |
| --- | --- | --- | --- |
| — | Conta do cliente ligada à MCC, pagamento do cliente, verificação do anunciante e checagem da política de álcool | Adicionar | PTRA: a verificação pode levar dias; álcool é conteúdo restrito, sem menores e sem consumo excessivo \[oficial, verificar o texto\] |
| 1. Análise de concorrentes | Centro de Transparência de Anúncios e busca anônima; entra no benchmark único | Manter | PTRA \[mercado\] |
| 2. Pesquisa de palavras-chave | Parte do relatório único de termos do perfil, agrupado em 2 ou 3 grupos e com negativas | Ajustar | PTRA: grupos de intenção única; negativas como emprego, atacado de outra cidade, grátis \[mercado\] |
| 3. Termos e correspondência | Frase e exata no começo; ampla só com lance inteligente e dados de conversão | Manter (com regra) | PTRA \[mercado\] |
| 4. Configuração da campanha | Só Rede de Pesquisa, local por presença, raio de entrega, horário do atendimento, orçamento diário; Maximizar cliques com teto ou Maximizar conversões; sem Performance Max | Manter (com regras) | PTRA \[oficial, mercado\]: sem histórico, o Performance Max gasta em inventário de baixa intenção |
| 5. Ativos da campanha | 2 anúncios responsivos por grupo (15 títulos, 4 descrições), sitelinks, frases de destaque, local (perfil vinculado), chamada, imagens e logo | Ajustar | PTRA: força do anúncio "Boa" ou melhor \[oficial\]. O ativo de local depende do perfil do Henrique |
| 6. Site e UTMs | URL final, sufixo com UTMs, conversão principal "clique no WhatsApp" e GCLID guardado e levado ao CRM pelo código curto | Ajustar | PTRA: sem conversão e sem GCLID não há lance inteligente nem atribuição de venda \[oficial\]. Resolve o ponto "tags no Google Ads" da sua documentação |
| — | Aprovação do cliente e QA de clique real | Adicionar | PTRA \[mercado\] |
| 7. Campanha no ar | Publicar no D6 e acompanhar o status "Qualificado (limitado)" | Manter | PTRA: revisão em cerca de 1 dia útil \[oficial\] |
| — | Conversões offline: GCLID, data e valor da venda | Adicionar | [Ajuda do Google Ads](https://support.google.com/google-ads/answer/16884284): desde 15/06/2026 a importação offline migrou para a Data Manager API e está bloqueada na Google Ads API para quem não usava \[oficial, lido em 24/11\]. Para um cliente pequeno, planilha pela interface; conferir o caminho na tela |

**Bloco único de rastreio (Meta e Google).** Configurado uma vez pelo Igor e usado pelos dois canais: GTM, GA4, pixel e dataset, tag do Google Ads, Consent Mode, UTMs padrão, GCLID guardado na landing e código curto na mensagem do WhatsApp. Do lado do WhatsApp, o webhook da Cloud API grava o `ctwa_clid` no Chatwoot. Quando o atendente marca "pago" com valor, o n8n devolve `Purchase` à Meta e a venda entra na planilha offline do Google (PTRA). O número de decisão é a venda no CRM, não o relatório das plataformas.

## Versão final · Onboarding e gestão de conta (todos os produtos)

A versão padronizada tem 70 tarefas em 7 blocos, cada uma com código (ON, LP, GM, RT, MA, GA, SD). Os códigos viram a coluna "Etapa do template" do quadro de tarefas. Tempos são horas de trabalho com o template v01 pronto, estimadas a partir das pesquisas e das estimativas P/M/G de 09/11; o primeiro cliente de um segmento novo demora mais.

**O que dispara o D1:** briefing respondido, acesso ao perfil, portfólio da Meta com a conta de anúncios, conta do Google Ads, domínio e DNS, número de WhatsApp com o canal decidido. Fotos e entrevista do perfil podem chegar até o D2.

| Código | Etapa | Tarefa | Subtarefas | Responsável | Tempo | Dia | Depende de | Pronto quando |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ON-01 | Venda para operação | Ficha de venda | O que foi prometido, preço, escopo por produto, decisor, orçamento de mídia previsto, particularidades | Quem vendeu, para o Henrique | 0,5 h | D0 | Contrato assinado e 50% pagos | Ficha preenchida; sem ficha, o cliente não entra no quadro |
| ON-02 | Abertura | Abrir o cliente | Grupo de WhatsApp com o dono como admin, pasta CLI-00X, projeto no quadro a partir do template v01 | Henrique | 0,5 h | D0 | ON-01 | Grupo, pasta e cartões criados |
| ON-03 | Abertura | Briefing e pedido único de acessos e materiais | Briefing: oferta, combos, pedido mínimo, raio e bairros, pagamento, horário e feriados, público, tom, orçamento de mídia, quem atende. Materiais: logo, 12 ou mais fotos (fachada com nome, interior, produto, equipe), cardápio com preços, CNPJ, comprovante. Acessos: perfil, Meta, Google Ads, domínio, número | Henrique | 1 h | D0 | ON-02 | Documento único enviado, com prazo de 48 h |
| ON-04 | Abertura | Coletar e testar acessos | Tudo por convite, nunca senha. Cada acesso testado com uma ação real: Henrique no perfil, Igor na Meta e no Google, Bernardo no domínio | Henrique (cobra) | 1 h | D0 | ON-03 | Checklist de acessos todo verde |
| ON-05 | Relógio | Disparar o D1 | Mensagem no grupo: "recebemos tudo, hoje é o D1, entrega em \[data\]", com a data do pacote de aprovação e da resposta | Henrique | 5 min | D1 | ON-04 | Mensagem registrada no grupo |
| ON-06 | Relógio | Kickoff de 30 a 45 min | Metas, diferenciais, quem aprova, orçamento de mídia, regra do pacote único de aprovação; ata de 5 linhas no grupo | Henrique e Igor | 0,75 h cada | D1 | ON-05 | Ata no grupo; orçamento aprovado por escrito |
| ON-07 | Relógio | Marco zero | Prints do perfil, grade do GBP Check (mesmo raio todo mês), métricas atuais de site e anúncios, num PDF datado | Henrique e Igor (GBP Check) | 0,5 h cada | D0 e D1 | ON-04 | Pasta "relatório 1, inicial" com data |
| ON-08 | Aprovação | Pacote único de aprovação | Link de teste da landing, grade dos 9 criativos, textos dos anúncios e resumo da ficha já aprovada; vídeo de 3 a 5 min; lista do que aprovar | Henrique | 1 h | D5, até 12h | LP-09, MA-05, GA-04 | Pacote enviado; resposta pedida em mensagem única até 12h do D6 |
| ON-09 | Entrega | Relatório de abertura e entrega de acessos | Marco zero contra o entregue, status da verificação, campanhas, SDR em piloto, documento de acessos (o que é do cliente), próximos 30 dias, termo de aceite | Henrique, com uma seção de cada um | 2 h | D7 | Todas | Aceite assinado; cobrança dos 50% restantes |
| ON-10 | Pós-entrega | Check-in e retro | Check-in com o cliente; retro interna de 20 min: tempo real contra estimado, onde travou, mudança no template (v02) | Henrique e todos | 1 h | D+7 | ON-09 | Template versionado |

## Versão final · Landing page (D1 a D7)

Dono do serviço: Bernardo. São 11 tarefas e 24,5 h (Bernardo 16,5 h, Hugo 7 h, Henrique 1 h). A página vai ao cliente numa URL de teste no D5 e só ganha o domínio no D6, depois do "pode publicar".

| Código | Etapa | Tarefa | Subtarefas | Responsável | Tempo | Dia | Depende de | Pronto quando |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LP-01 | Pesquisa | Benchmark do cliente, parte de sites e Maps | 2 a 3 concorrentes do topo da grade do GBP Check e 1 referência nacional; promessa, prova, oferta, CTA e seções; 1 página de insights no mesmo documento da parte de anúncios (MA-02) | Hugo | 2 h | D1 | ON-07 | 3 a 5 insights viraram decisões de copy e layout |
| LP-02 | Estrutura | Wireframe a partir do template do segmento | Hero com promessa e CTA, combos, como pedir em 3 passos, área de entrega, avaliações do Google, FAQ, rodapé com endereço e avisos legais | Bernardo | 2 h | D1 | LP-01 | 1 objetivo de conversão; CTA visível no topo do celular |
| LP-03 | Copy | Texto, FAQ e bloco de fatos | Headline, subtítulos e CTAs; FAQ factual (horário, pedido mínimo, bairros, pagamento); bloco de fatos citáveis; microcopy do botão; advertências legais | Hugo | 4 h | D2 | LP-02, GM-03 | Copy revisada; fatos conferidos com o cliente |
| LP-04 | Design e front | Design e montagem na URL de teste | Paleta e fonte do template do segmento, fotos tratadas, montagem responsiva, meta title e description, imagem de compartilhamento | Bernardo | 7 h | D2 e D3 | LP-03, fotos do ON-03 | Página navegável na URL de teste, sem texto provisório |
| LP-05 | Design e front | Motion (opcional) | Só microanimações em CSS em 1 ou 2 seções | Bernardo | 0,5 h | D3 | LP-04 | LCP e INP continuam dentro do limite |
| LP-06 | Integrações | CTA e instalação do rastreio | Link wa.me com mensagem pronta e código curto, botão flutuante, clique para ligar, link do cardápio digital; snippet do contêiner GTM (as tags são do RT-02) | Bernardo | 1,5 h | D4 | LP-04, RT-01 | Clique abre a conversa com o texto certo |
| LP-07 | Conformidade | 18+ e LGPD | Portão de idade; "venda proibida para menores de 18 anos"; "beba com moderação"; política de privacidade; banner de consentimento | Bernardo | 1,5 h | D4 | LP-04 | Nenhum script de marketing antes do consentimento; avisos visíveis |
| LP-08 | SEO da página | Termos, schema e endereço | Title e description com termo e cidade, H1, endereço igual ao do perfil, mapa, schema LocalBusiness ou LiquorStore com horário e geo, FAQ visível | Hugo (0,5 h) e Bernardo (1 h) | 1,5 h | D4 | LP-04, GM-04 | Rich Results Test sem erro; schema igual ao texto visível |
| LP-09 | QA | Teste no celular e de velocidade | 2 Android e 1 iPhone, PageSpeed, links, endereço igual ao perfil, checklist; quem testa não é quem montou | Henrique | 1 h | D5, manhã | LP-06 a LP-08, RT-02 | LCP ≤ 2,5 s, INP ≤ 200 ms, CLS ≤ 0,1 no celular; zero link quebrado |
| LP-10 | Ajustes | Rodada única de ajustes | Aplicar a lista do cliente | Bernardo (2 h) e Hugo (0,5 h) | 2,5 h | D6 | Resposta ao ON-08 | "Pode publicar" por escrito |
| LP-11 | Publicação | Domínio e Search Console | Apontar o DNS (acesso pego no D0), HTTPS, redirecionar www, Search Console, sitemap, pedir indexação | Bernardo | 1 h | D6 | LP-10 | URL final com HTTPS e propriedade verificada |

## Versão final · Perfil da Empresa, SEO, AEO e GEO (D1 a D7)

Dono do serviço: Henrique. São 11 tarefas e 15 h (Henrique 13,5 h, Hugo 1,5 h). O relatório de palavras-chave sai no D1 porque alimenta a copy da landing (D2) e o Google Ads (D3). A verificação é pedida no D4; se o Google levar o prazo máximo, o perfil fica no ar depois do D7.

| Código | Etapa | Tarefa | Subtarefas | Responsável | Tempo | Dia | Depende de | Pronto quando |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| GM-01 | Acesso | Acesso e propriedade do perfil | Perguntar se existe perfil e quem criou; convite em Pessoas e acesso como administrador; nunca senha; conferir edição e endereço | Henrique | 0,5 h | D0 | ON-03 | Convite aceito e edição conferida, ou "não existe perfil" registrado |
| GM-02 | Dados do negócio | Entrevista e documentos | 15 perguntas em 3 blocos; foto da fachada com o nome; comprovante; telefone com DDD, horário e feriados, serviços, diferenciais | Henrique (o cliente responde até o fim do D2) | 1 h | D1 e D2 | GM-01 | Respostas e documentos recebidos |
| GM-03 | Público e termos | Relatório único de palavras-chave | 3 a 5 termos do segmento; volume na cidade; teste do bloco local do mapa; 1 termo principal, 5 a 10 secundários e 8 a 12 perguntas reais; OK de gasto da ferramenta com o Igor | Henrique | 2,5 h | D1 | ON-04 | Tabela datada com a fonte, enviada para LP-03, GM-04 e GA-02 |
| GM-04 | Arquitetura | Posicionamento e categorias | Categoria principal testada contra os 3 primeiros da grade e adicionais; descrição; serviços e produtos; atributos; bairros; espelho entre página e perfil | Henrique | 1 h | D2 | GM-02, GM-03 | Categoria escolhida com base em quem ranqueia |
| GM-05 | Ficha | Ficha do perfil e conferência | 8 seções; nome real, sem palavra-chave; descrição até 750 caracteres (o essencial nos 250 primeiros); serviços até 250; área de cobertura; conferência dos limites | Henrique (descrição e serviços escritos pelo Hugo, 0,5 h) | 2,5 h | D3 | GM-04 | Ficha sem item reprovado |
| GM-06 | Avaliações | Sistema de avaliações | Link curto; placa QR ou NFC no balcão e com o entregador; script pós-entrega no WhatsApp; responder as avaliações existentes | Henrique e cliente | 1 h | D3 | GM-01 | Cliente já pediu avaliação às primeiras 10 pessoas |
| GM-07 | Aprovação | OK do cliente na ficha | Ficha em linguagem simples; OK por escrito no WhatsApp | Henrique | 0,25 h | D4, manhã | GM-05 | OK guardado até 12h do D4 |
| GM-08 | Painel | Preencher o perfil e pedir a verificação | Procurar duplicado; mudar nome, endereço e categoria antes de verificar; subir logo e fotos; cadastrar serviços; pedir a verificação no mesmo dia (vídeo contínuo de 30 s ou mais, gravado pelo cliente com roteiro); registrar a data | Henrique | 2,5 h | D4 | GM-07, fotos do ON-03 | Perfil preenchido e verificação pedida com data, ou perfil já verificado |
| GM-09 | Citações | Mesmo nome, endereço e telefone fora do Google | Bing Places, Apple Business Connect, Facebook, Instagram e apps de delivery que o cliente usa | Henrique | 1,5 h | D5 | GM-08 | Dados idênticos em todas as plataformas da lista |
| GM-10 | Conteúdo | Posts de abertura | 2 posts de 1.000 a 1.500 caracteres, sem telefone, e-mail ou link externo, com imagem real; calendário dos posts do mês 1 | Hugo escreve (1 h), cliente aprova, Henrique programa (0,25 h) | 1,25 h | D5 e D6 | GM-04 | 2 posts aprovados; programados se o perfil já estiver verificado |
| GM-11 | Medição | Baseline em IA e Search Console | 5 perguntas no ChatGPT, Gemini, Perplexity e Google AI Mode, com prints; conferir a propriedade do Search Console criada no LP-11 | Henrique | 1 h | D6 e D7 | LP-11 | Baseline com prints e data na pasta do cliente |

## Versão final · Meta Ads, Google Ads e bloco de rastreio (D1 a D7)

Dono do serviço: Igor. São 20 tarefas e cerca de 45 h: Igor 27,5 h, design e videomaker 12 h, Bernardo 4 h, Hugo 1 h e Henrique 0,25 h. As verificações saem no D1 porque são os únicos passos fora do nosso controle. A publicação é no D6, e o D7 entrega "campanhas no ar ou em revisão, com rastreio validado".

| Código | Etapa | Tarefa | Subtarefas | Responsável | Tempo | Dia | Depende de | Pronto quando |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MA-01 | Meta · acessos | Portfólio, página e verificações | Página com endereço e descrição, ligada ao Instagram; conta de anúncios no portfólio do cliente com a Ativos como parceira; pagamento do cliente; 2FA; verificação da empresa e do domínio disparadas; 18+ na página e no Instagram | Igor | 2 h | D0 e D1 | ON-04 | Acesso de parceiro completo; verificações enviadas; 18+ configurado |
| GA-01 | Google · acessos | Conta, MCC e compliance | Conta do cliente ligada à MCC; pagamento do cliente; verificação do anunciante enviada; textos e landing checados contra a política de álcool | Igor | 1 h | D0 e D1 | ON-04 | Conta ativa; verificação enviada |
| MA-02 | Meta · benchmark | Benchmark do cliente, parte de anúncios | Biblioteca de Anúncios (cidade, "distribuidora", "delivery de bebidas") e Centro de Transparência do Google; 10 a 20 anúncios; ganchos, ofertas, formatos, CTA | Igor | 2 h | D1 | ON-06 | Swipe file e 3 ângulos priorizados, no mesmo documento do LP-01 |
| MA-03 | Meta · estratégia | Estrutura, público e orçamento | Objetivo com destino WhatsApp; 1 campanha; 1 conjunto (raio de entrega, 18+, público amplo); 2º conjunto só se o orçamento render cerca de 50 conversas por semana em cada; mensagem pronta; nomenclatura | Igor | 1,5 h | D2 | MA-02, orçamento do ON-06 | Estrutura cabe no orçamento aprovado |
| MA-04 | Meta · criativos | Briefing criativo | Roteiros de 3 vídeos (gancho em 3 s, oferta, CTA), 3 estáticos e 3 carrosséis; advertência do CONAR em todas; modelos que aparentem 25 anos ou mais; nada de consumo excessivo, direção ou menores | Igor | 2 h | D2 | MA-02, MA-03 | Cada peça com gancho, oferta, CTA e advertência |
| RT-01 | Rastreio | Mapa de eventos e contêiner | GTM, GA4, pixel e dataset, tag do Google Ads, Consent Mode, auto-tagging; nomes de evento e UTMs padrão | Igor | 1,5 h | D3 | ON-04 | Mapa de eventos aprovado; contêiner criado |
| GA-02 | Google · palavras | Grupos, correspondência e negativas | Base no relatório GM-03 e no Planejador; 2 ou 3 grupos de intenção única; 30 a 60 termos; frase e exata; negativas | Igor | 1,5 h | D3 | GM-03 | Grupos sem sobreposição relevante |
| GA-03 | Google · campanha | Configuração em rascunho | Só Rede de Pesquisa; local por presença; raio; horário do atendimento; orçamento diário; Maximizar cliques com teto ou Maximizar conversões; sem Performance Max | Igor (revisão cruzada do Henrique, 0,25 h) | 1,25 h | D3 | GA-02 | Rascunho revisado por outra pessoa |
| MA-05 | Meta · criativos | Produção do lote 1 | 9 peças em 9:16, 4:5 e 1:1; captação na loja; legendas; variações de texto | Design e videomaker (12 h), revisão do Igor (0,5 h) | 12,5 h | D3 e D4 | MA-04 | 9 peças revisadas contra a política de álcool e o CONAR |
| RT-02 | Rastreio | Tags na landing | Tags e gatilhos; GCLID e UTMs guardados; código curto na mensagem do wa.me; conversão principal "clique no WhatsApp" no Google Ads; Enhanced Conversions | Igor | 3 h | D4 | LP-06, RT-01 | Tag Assistant e Test Events sem erro e sem duplicidade |
| GA-04 | Google · anúncios | Anúncios e ativos | 2 anúncios responsivos por grupo; sitelinks, frases de destaque, local, chamada, imagens, logo | Igor | 2 h | D4 | GA-03, fotos do ON-03 | Força do anúncio "Boa" ou melhor |
| RT-03 | Rastreio | WhatsApp até a venda | D5: webhook da Cloud API grava `referral` e `ctwa_clid` no Chatwoot; funil conversa, qualificado, pedido, pago, com campo de valor. D7: n8n envia `LeadSubmitted` e `Purchase` à API de Conversões para mensagens; planilha offline do Google | Bernardo (4 h), Igor (1,5 h), Hugo (1 h, marcação pelo SDR) | 6,5 h | D5 e D7 | SD-05 | Evento de teste com `ctwa_clid` e valor no Events Manager |
| RT-04 | QA | QA de rastreio e anúncio | Clique em pré-visualização; WhatsApp abre com o texto; `ctwa_clid` ou código no Chatwoot; evento de teste; UTMs no DebugView do GA4 | Igor | 2 h | D5 | RT-02, RT-03 (parte do D5) | Checklist 100% OK e assinado |
| GA-05 | Google · URL | URL final e UTMs | URL final da landing, sufixo com UTMs, teste do wa.me com código | Igor | 0,5 h | D5 | RT-02 | Sessões google / cpc no GA4 de teste |
| MA-06 | Meta · campanha | Montar em rascunho | Campanha, conjunto, 6 a 9 anúncios, textos com advertência | Igor | 1,5 h | D6, manhã | MA-05, RT-02 | Rascunho completo, pronto para publicar |
| MA-07 | Meta · publicação | Publicar | Depois da resposta ao ON-08 e do RT-04; acompanhar a revisão (até 24 h) | Igor | 0,5 h | D6 | ON-08, RT-04 | Anúncios ativos, sem reprovação |
| GA-06 | Google · publicação | Publicar | Ativar; acompanhar "Qualificado (limitado)" | Igor | 0,5 h | D6 | ON-08, RT-04, LP-11 | Status "Qualificado" com impressões |
| MA-08 | Meta · remarketing | Planejar públicos | Engajou no Instagram ou Facebook em 30 a 90 dias, visitou a landing, conversou no WhatsApp; excluir compradores recentes | Igor | 0,5 h | D6 | MA-07 | Públicos criados e conjunto pausado até ter tamanho |
| MA-09 | Entrega | Seção de tráfego do relatório | Prints das estruturas, mapa de eventos, expectativa de 2 a 4 semanas de aprendizado | Igor | 1 h | D7 | MA-07, GA-06 | Seção entregue ao Henrique para o ON-09 |
| GA-07 | Google · offline | Conversões offline | Planilha com GCLID ou código, data e valor; ação "Venda WhatsApp (offline)"; importação semanal | Igor | 1,5 h | D7 | RT-03 | 1ª importação aceita, ou planilha pronta se ainda não houve venda |

Se o canal oficial do WhatsApp não estiver aprovado até o D5, as campanhas sobem otimizando para conversas, e o RT-03 entra assim que a Meta aprovar. O cliente precisa saber que, até lá, não há venda atribuída ao anúncio.

## Versão final · SDR de IA e infraestrutura (D1 a D10)

Dono do serviço: Hugo; infraestrutura com o Bernardo. São 18 tarefas e 50,5 h (Hugo 29 h, Bernardo 20 h, Henrique 1 h, Igor 0,5 h). O relógio é de 10 dias úteis, dentro dos 15 corridos combinados em 23/11, e a entrega do D10 é um piloto controlado. O passo fora do nosso controle é a aprovação da Meta para o número na Cloud API, por isso a decisão de canal vem no D0.

| Código | Etapa | Tarefa | Subtarefas | Responsável | Tempo | Dia | Depende de | Pronto quando |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SD-00 | Canal | Decisão de canal | Cloud API ou conexão não oficial; número atual ou dedicado; verificação da empresa na Meta; termo de ciência se não for oficial | Bernardo (1 h) e Igor (0,5 h); o cliente assina | 1,5 h | D0 | ON-04 | Decisão registrada e assinada pelo cliente |
| SD-01 | Discovery | Atendimento atual | 50 a 100 conversas reais, com autorização; entrevista de 1 h com o dono e o atendente; tempo de resposta atual; quem passa o pedido para a entrega | Hugo | 4 h | D1 e D3 | ON-04 | 50 conversas lidas e 5 jornadas típicas descritas |
| SD-02 | Discovery | Documento de regras e FAQ | Área por bairro ou CEP, frete por faixa, pedido mínimo, pagamento, troco, casco, horário, estoque, idade mínima; 30 perguntas e objeções mais comuns | Hugo, com o cliente | 3 h | D3 e D4 | SD-01 | Toda regra com número ou lista fechada; FAQ aprovada pelo dono |
| SD-03 | Discovery | Tom de voz e linha de base | Nome do atendente virtual, informalidade, emojis, palavras proibidas, aviso de que é IA; 10 diálogos ideais; tempo da 1ª resposta, conversão e transbordo de hoje | Hugo | 2 h | D4 | SD-02 | Dono aprova os 10 exemplos; linha de base medida |
| SD-04 | Infraestrutura | VPS e serviços | Coolify, Chatwoot, n8n e Postgres a partir do template; HTTPS; firewall; usuário sem root; SSH por chave; senhas no cofre; ambiente de homologação | Bernardo | 3 h | D1 e D2 | SD-00 | Serviços com HTTPS; nenhuma senha em grupo de chat |
| SD-05 | Infraestrutura | Conectar o WhatsApp | Cloud API: WABA, nome de exibição, webhook, token permanente; ou pareamento por QR em número dedicado, só para teste | Bernardo | 2 h e a espera da Meta | D2 a D4 | SD-00, SD-04 | Mensagem de teste ida e volta, com mídia |
| SD-06 | Dados | Banco do cardápio | SKU, nome, categoria, volume, preço, promoção, ativo, foto, teor; frete por bairro; horário; planilha do cliente sincronizada | Bernardo (3 h) e Hugo com o cliente na carga (1 h) | 4 h | D5 | SD-02 | Todos os SKUs ativos com preço e foto; o cliente muda um preço e o bot responde o novo valor em até 5 min |
| SD-07 | Dados | Fotos dos produtos | JPEG ou PNG de até 5 MB, nome pelo SKU, URL estável | Bernardo | 1,5 h | D6 | SD-06 | Todas carregando no WhatsApp |
| SD-08 | Agente | Prompt v1 em estados | Saudação, triagem, idade, oferta, carrinho, endereço e frete, pagamento, resumo, humano; regras "nunca": inventar preço, prometer prazo fora da regra, vender a menor, sair do assunto | Hugo | 4 h | D5 e D6 | SD-02, SD-03 | Revisado por outra pessoa; passa no teste rápido |
| SD-09 | Agente | Ferramentas | `buscar_produto`, `consultar_preco`, `calcular_frete`, `enviar_foto`, `montar_resumo`, `transferir_humano` | Bernardo (4 h) e Hugo (2 h) | 6 h | D6 a D8 | SD-06, SD-08 | Nenhum preço "de memória" nos testes |
| SD-10 | Agente | Verificação de idade | Pergunta de maioridade antes de ofertar; recusa padrão; registro do aceite; checklist do entregador para conferir documento | Hugo, com o cliente | 1 h | D6 | SD-08 | Todos os casos "sou menor" recusados |
| SD-11 | Integração | Transbordo, horário e follow-up | O bot para ao transferir; etiqueta `pedido_pronto`; resumo ao atendente; mensagem fora do horário; 1 follow-up dentro de 24 h | Bernardo (2 h) e Hugo (1 h) | 3 h | D7 a D9 | SD-05, SD-09 | Humano recebe o resumo em menos de 1 min; nada enviado fora da janela de 24 h |
| SD-12 | Testes | Roteiro funcional | 40 a 60 casos: pedido simples e combinado, produto inexistente, sem estoque, fora da área, troco, mudança no meio, áudio, foto, mensagens picadas | Hugo | 5 h | D7 e D8 | SD-09 a SD-11 | 90% de acerto e 100% nos casos de preço, idade e transbordo |
| SD-13 | Testes | Red team | Desconto falso, "ignore as instruções", menor de idade, ofensa, assunto fora do escopo, dados de outro cliente | Hugo | 3 h | D9 | SD-12 | Nenhuma falha crítica aberta |
| SD-14 | LGPD | Base legal e avisos | Aviso na 1ª mensagem; base legal para pedido e para promoção; retenção das conversas; cláusula de operador no contrato | Henrique, com o modelo jurídico | 1 h | D7 | SD-02 | Aviso ativo; cláusula no contrato |
| SD-15 | Operação | Monitoramento e backup | Uptime Kuma; alerta de queda; logs das ferramentas; custo de tokens; cópia diária do banco fora da VPS | Bernardo | 2,5 h | D9 | SD-04 | Alerta chega em menos de 5 min; restauração testada 1 vez |
| SD-16 | Aceite | Teste do cliente (UAT) | Dono e atendente conversam com o bot como clientes por 1 a 2 dias | Hugo acompanha; o cliente testa | 2 h | D9 e D10 | SD-13 | Aceite por escrito |
| SD-17 | Go-live | Piloto controlado | Horário ou volume limitado; humano de plantão; desligar com 1 clique | Bernardo (1 h) e Hugo (1 h) | 2 h | D10 | SD-15, SD-16 | 48 h sem incidente crítico para virar produção |

A partir do D10, a revisão diária de conversas e a regressão do prompt entram na rotina do Hugo. **Fica para a fase 2 (semanas 3 a 6):** templates aprovados para status do pedido e reengajamento com opt-in, painel de preços para o cliente, painel de métricas, transcrição de áudio e integração com o PDV. O catálogo nativo não entra nem na fase 2, porque a política proíbe para álcool.

## Quadro dia a dia de um cliente com o pacote completo

O quadro abaixo junta as cinco tabelas por dia e por pessoa, com as horas daquele dia entre parênteses. É o que cada um puxa para o "Fazendo" quando o cliente está naquele D. Landing, perfil e tráfego terminam no D7; o SDR segue até o D10.

| Dia | Henrique | Hugo | Bernardo | Igor | Design e videomaker | Cliente |
| --- | --- | --- | --- | --- | --- | --- |
| D0 (antes do relógio) | ON-01 a ON-04, GM-01 (3,5 h) | — | SD-00 (1 h) | ON-07, MA-01, GA-01, SD-00 (2,5 h) | — | Responde o briefing, dá os acessos, assina a decisão de canal |
| D1 | ON-05, ON-06, ON-07, GM-02, GM-03 (4,1 h) | LP-01, SD-01 (4 h) | LP-02, SD-04 (3,5 h) | ON-06, MA-01, MA-02, GA-01 (4,25 h) | — | Kickoff; entrevista do SDR; recebe as 15 perguntas do perfil |
| D2 | GM-02, GM-04 (1,75 h) | LP-03 (4 h) | LP-04, SD-04, SD-05 (4,25 h) | MA-03, MA-04 (3,5 h) | — | Devolve entrevista e documentos; confirma os fatos da copy |
| D3 | GM-05, GM-06, GA-03 (3,25 h) | GM-05, SD-01, SD-02 (4 h) | LP-04, LP-05 (5,75 h) | RT-01, GA-02, GA-03, MA-05 (4,25 h) | MA-05 (6 h) | Recebe a captação na loja; fotos até hoje; começa a pedir avaliações; regras do SDR |
| D4 | GM-07, GM-08 (2,75 h) | LP-08, SD-02, SD-03 (4 h) | LP-06, LP-07, LP-08, SD-05 (5 h) | RT-02, GA-04, MA-05 (5,25 h) | MA-05 (6 h) | OK na ficha até 12h; grava o vídeo de verificação; aprova os diálogos do SDR |
| D5 | LP-09, ON-08, GM-09 (3,5 h) | GM-10, SD-06, SD-08 (4 h) | RT-03, SD-06 (5 h) | RT-03, RT-04, GA-05 (4 h) | — | Recebe o pacote único de aprovação até 12h; carrega preços na planilha |
| D6 | GM-10, GM-11 (0,75 h) | LP-10, SD-08, SD-09, SD-10 (4,5 h) | LP-10, LP-11, SD-07 (4,5 h) | MA-06, MA-07, MA-08, GA-06 (3 h) | — | Responde o pacote até 12h; aprova os 2 posts |
| D7 | ON-09, GM-11, SD-14 (3,5 h) | RT-03, SD-09, SD-11, SD-12 (4 h) | RT-03, SD-09 (4 h) | MA-09, GA-07 (2,5 h) | — | Recebe o relatório e assina o aceite |
| D8 | — | SD-12 (4 h) | SD-09, SD-11 (3 h) | — | — | — |
| D9 | — | SD-13, SD-16 (4 h) | SD-11, SD-15 (3,5 h) | — | — | Testa o SDR como cliente |
| D10 | — | SD-16, SD-17 (2 h) | SD-17 (1 h) | — | — | Aceite do piloto; atendente de plantão |

Os dias de folga do Henrique (D2 e D6) são onde entram a gestão dos outros clientes e as entregas da semana. Os picos de Bernardo (D3) e Igor (D4) passam de 5 h e não aceitam um segundo cliente no mesmo D.

## Capacidade e vários clientes ao mesmo tempo

Com o pacote completo, a equipe consegue abrir 1 cliente a cada 2 semanas, e só se cada pessoa der cerca de 5 h por dia às entregas. Com as 3 h por dia medidas em 09/11, o pacote não cabe no relógio: Bernardo precisaria de 13,5 dias úteis e Hugo, de 12,8.

&#91;embedded content: Horas por pessoa e por dia de um pacote completo · estimativas deste plano (soma das tabelas acima)\]

| Pessoa | Pacote completo | Sem o SDR | Dias úteis de trabalho a 3 h/dia | A 5 h/dia | Recorrente por cliente já entregue |
| --- | --- | --- | --- | --- | --- |
| Bernardo | 40,5 h | 20,5 h | 13,5 | 8,1 | Cerca de 0,5 h por semana (VPS, alertas, backup) |
| Hugo | 38,5 h | 9,5 h | 12,8 | 7,7 | SDR: 9,5 h na 1ª semana do piloto, 6,5 h nas semanas 2 a 4 e cerca de 3 h depois (PSDR) |
| Igor | 29,25 h | 28,75 h | 9,8 | 5,9 | Cerca de 5 h por semana com Meta e Google (rotina da PTRA) |
| Henrique | 24,1 h | 23,1 h | 8,0 | 4,8 | Cerca de 1,5 h por semana (perfil e grupo do cliente) |
| Design e videomaker | 12 h | 12 h | 4,0 | 2,4 | Cerca de 1 h por semana (2 a 4 peças a cada 2 semanas) |

**Regras para atender vários clientes**

1. **Até ter 4 semanas de tempo real no quadro, abra no máximo 1 pacote completo a cada 2 semanas, com D1 na segunda-feira.** O pacote de aprovação cai na sexta, a resposta na segunda até 12h e o piloto do SDR na sexta da semana 2. A POPE sugeria até 2 D1 por semana, mas com SDR e tráfego no pacote as horas não sustentam isso.
2. **Abra pela soma de horas por pessoa, não pelo número de clientes.** Um pacote só de landing e perfil pesa em Henrique (23 h) e Bernardo (16,5 h); ele só entra numa semana em que a soma dos dois caiba em 25 h.
3. **O tráfego recorrente é o primeiro limite.** Cada cliente entregue toma cerca de 5 h por semana do Igor. A primeira semana de um setup novo toma 21,25 h do Igor e a segunda, 5,5 h. A 25 h por semana, com 2 clientes recorrentes sobram 15 h, menos do que o setup pede. A primeira contratação ou terceirização deve ser um operador para a rotina de tráfego.
4. **Nunca dois pilotos de SDR na mesma semana:** a 1ª semana de cada piloto toma 9,5 h do Hugo.
5. **O prazo médio depende da fila (Lei de Little, citada na POPE).** Se a equipe entrega 1 pacote completo a cada 2 semanas e houver 3 em andamento, cada um leva em média 6 semanas. O relógio de 7 dias só vale se a entrada respeitar a vazão.
6. **Troque estas estimativas pelo tempo real** da planilha depois de 3 ou 4 clientes; elas vêm das pesquisas e do template, não de medição.

## Rotina diária e semanal de cada profissional

Todos seguem o mesmo esqueleto de dia e de semana; o que muda é o conteúdo de cada bloco. Com vários clientes, a regra é um cliente por bloco de foco e as tarefas recorrentes em lote, porque o maior custo da equipe é a troca de contexto (POPE: Leroy, 2009 \[empírico\]).

**Esqueleto do dia (todos, de segunda a sexta)**

| Horário | Bloco | Regra |
| --- | --- | --- |
| 08h30 a 09h00 | Triagem | Ler os grupos e o quadro, mover cartões; nada de execução |
| 09h00 a 09h15 | Daily | O que entregou, o que entrega hoje, o que trava e quem trava; discussão longa fica para depois (Scrum Guide, via POPE) |
| 09h15 a 12h00 | Foco 1 | Um cliente, um tipo de tarefa, notificações desligadas. Vai para o cliente cujo D trava outra pessoa ou a entrega (D4 a D6 antes de D1 a D3) |
| 13h00 a 13h30 | Janela de clientes | Responder grupos, cobrar materiais, enviar aprovações. Primeira resposta em até 4 h úteis \[heurística\] |
| 13h30 a 16h30 | Foco 2 | Segundo cliente em setup, ou as recorrentes de todos em lote, ou rua (dias de rua marcados no calendário, sem tarefa G) |
| 16h30 a 17h00 | Quadro | Status, "Concluída em", tempo real e "Aguardando quem, desde" |
| 17h00 | Fechamento de caixa | Responsável fixo, 15 min (decisão de 23/11) |

**Regras com vários clientes**

- No máximo 3 cartões em "Fazendo" por pessoa (regra já existente no quadro).
- Dois clientes em setup ao mesmo tempo ganham um bloco inteiro cada (foco 1 e foco 2), nunca meia hora de cada.
- Tarefa recorrente se faz para todos os clientes de uma vez: as checagens de contas, a revisão de conversas e os alertas das VPS têm horário fixo.
- As métricas de cada papel são da equipe e servem para diagnosticar, não para ranking entre sócios (POPE: Lei de Campbell).

**Semana-padrão**

| Dia | Todos | Henrique | Hugo | Bernardo | Igor |
| --- | --- | --- | --- | --- | --- |
| Segunda | Planejamento, 45 min: capacidade em horas e quantos D1 abrem | Conduz o planejamento; dispara o D1 dos pacotes novos | Relatório semanal do SDR dos pilotos no mês 1 | Confere os backups do fim de semana | Sobe as conversões offline da semana anterior |
| Terça | — | Programa 1 post por perfil recorrente | Bloco de SDR | Bloco de landing | Otimização em lote de Meta e Google e report de 1 tela por cliente |
| Quarta | Revisão de riscos, 15 min: clientes no D4 | Cobra os OKs de ficha que vencem no D4 | Regressão dos casos críticos se o prompt mudou | Janela de atualizações de segurança das VPS | Briefing de criativos novos (semanas pares) |
| Quinta | — | Presença no grupo de cada cliente (2ª vez na semana) | Bloco de SDR | Bloco de landing | Dia de rua (sugestão; ponto em aberto 10) |
| Sexta | Revisão e retro, 45 min: entregue, tempo real contra estimado, 1 mudança no template | Envia o pacote de aprovação dos clientes em D5 | Atualiza a biblioteca de prompts | Atualiza o kit de seções da landing | Confere se as vendas da semana têm valor e origem no Chatwoot |

Reuniões de 3 a 4 h, como as de 08/10 e 23/11, viram uma sessão mensal com pauta fechada. Os rituais semanais somam 1 h 45 min.

**Rotina por pessoa**

| Pessoa e papel | Todo dia | Toda semana | Todo mês | Medida do papel |
| --- | --- | --- | --- | --- |
| Henrique, gestão de contas e Perfil da Empresa | Triagem de todos os grupos; cobrança de acessos e respostas na janela das 13h; foco no perfil do cliente em D1 a D5; responder avaliações novas dos perfis recorrentes | Conduz planejamento, riscos e retro; 1 post por perfil; presença em cada grupo 2 vezes (curso de GMN) | Relatório mensal no dia 6 ou 7, porque o painel do Google fecha o mês com atraso (curso de GMN); grade do GBP Check no mesmo raio; check-in D+7 e retro de cada cliente entregue | % de D1 em até 48 h da assinatura; dias em "Aguardando cliente"; entregas no D7 |
| Igor, tráfego e vendas | Checagem de 10 a 15 min por conta ativa, em lote (gasto, reprovação, pagamento, dataset); foco 1 no setup do cliente em D1 a D6; a cada 2 dias, vendas com valor e origem | Otimização em lote num dia fixo, sem edição grande durante o aprendizado; conversões offline; report curto; dias de rua fixos | Relatório e reunião por cliente; auditoria de rastreio; estratégia de lance do Google; briefing de criativos a cada 2 semanas | Campanhas no ar até o D7; vendas rastreadas contra cliques no WhatsApp; custo por conversa, acompanhado e não como meta |
| Hugo, SDR de IA e copy | Revisar conversas reais de cada SDR: 20 a 30 por dia na 1ª semana do piloto, 10 a 20 depois; falha crítica corrigida em até 24 h; foco no SDR em implantação e na copy do cliente em D1 e D2 | Regressão dos casos críticos a cada mudança de prompt; relatório semanal no mês 1; biblioteca de prompts | Relatório do SDR: conversas, transbordos, conversão, 1ª resposta, fora do horário, recusas por idade, erros de preço (meta: zero) | % de transbordo certo; erros críticos por 100 conversas; horas por SDR novo caindo |
| Bernardo, landing e infraestrutura | 10 min nos alertas de todas as VPS e do Chatwoot; foco na landing do cliente em D1 a D6; bloco de infra do SDR | Atualizações de segurança em janela fixa; backups conferidos; credenciais novas no cofre; kit de seções da landing | Teste de restauração de um cliente por vez; custo de VPS e de tokens por cliente | Horas por landing caindo; erros depois do deploy; landings aprovadas na 1ª rodada |

A rotina por pessoa vem da POPE, da PTRA (tráfego) e da PSDR (SDR). Os horários e a distribuição pelos dias da semana são proposta minha \[opinião\].

## Pontos em aberto para você decidir

São 18 decisões, cada uma com a minha recomendação. As três primeiras a fechar são a 2 (canal), a 3 (pedido pelo WhatsApp) e a 8 (perfil da Guto), porque travam o Guto nesta semana. Mude o status na última coluna conforme decidir.

| # | Decisão | Opções | Recomendação | Quem decide | Status |
| --- | --- | --- | --- | --- | --- |
| 1 | Dias do relógio | Úteis (seg a sex) ou corridos | Úteis, contados do D1. Em 5 dias úteis o pacote não cabe (seção Capacidade). O Guto mantém o prazo já combinado | Igor e Henrique | Aberto |
| 2 | Canal do WhatsApp | Cloud API no número de vendas; coexistência com o app; conexão não oficial com número dedicado | Cloud API no número de vendas, com os humanos atendendo pelo Chatwoot; conexão não oficial só para teste interno. WA-POL proíbe mensagem sobre álcool no app, então o cliente que hoje vende pelo app está exposto; avisar | Igor, Bernardo e cliente | Aberto |
| 3 | Pedido pelo WhatsApp conta como "experiência de comércio"? | Seguir com o SDR fechando pedido; limitar o SDR a tirar dúvidas e passar ao humano | WA-POL não responde. Pedir parecer jurídico e perguntar ao suporte da Meta ou ao BSP antes do go-live. Até lá: nada de catálogo, carrinho ou pagamento dentro do WhatsApp | Igor, com jurídico | Aberto |
| 4 | Rodadas de aprovação | 1 rodada em 24 h; 2 rodadas em 48 h | 1 pacote único no D5, resposta até 12h do D6; atraso pausa o relógio; ajuste extra vira escopo novo ou mensalidade | Henrique | Aberto |
| 5 | Posts do perfil no setup | Mês 1 inteiro; 2 posts e calendário | 2 posts e o calendário; o resto na mensalidade | Henrique | Aberto |
| 6 | Motion no padrão da landing | Manter; cortar; só CSS | Só microanimações em CSS, e só se passar no QA de velocidade | Bernardo | Aberto |
| 7 | Avaliações e citações: setup ou mensalidade | Tudo no setup; tudo na mensalidade | Link, placa e script de avaliação no setup (maior alavanca); citações no setup só se couber nas horas | Henrique | Aberto |
| 8 | Perfil da Guto | Confirmar se "Distribuidora de Bebidas Ouro Preto" (38 avaliações no GBP Check de 19/11) é o perfil da Guto | Confirmar hoje: se o perfil já existe e está verificado, não há verificação e o perfil sai do caminho crítico | Henrique | Aberto |
| 9 | Acesso ao GBP Check | Só o Igor; Henrique também | Dar acesso ao Henrique, dono do serviço, para tirar o Igor do perfil | Igor | Aberto |
| 10 | Dias de rua e fechamento de caixa | Definir dias fixos e responsável | Igor na rua em dias fixos (sugestão: quinta), sem tarefa G; o fechamento de caixa com um responsável fixo, como decidido em 23/11 | Todos | Aberto |
| 11 | Ritmo de entrada | Até 2 D1 por semana (POPE); 1 pacote completo a cada 2 semanas | 1 pacote completo a cada 2 semanas, D1 na segunda, até ter 4 semanas de tempo real | Igor e Henrique | Aberto |
| 12 | Primeira contratação | Operador de tráfego; dev; SDR | Operador para a rotina de tráfego: com 2 clientes recorrentes o Igor já não abre setup novo | Sócios | Aberto |
| 13 | Design e videomaker | Quem são, como contratam, disponibilidade | Garantir 12 h no D3 e no D4 de cada cliente, com captação na loja agendada no kickoff | Igor | Aberto |
| 14 | Orçamentos | Mídia mínima a propor; gasto da ferramenta de palavras | Mídia: o piso que gere volume de conversas (PTRA cita R$ 30 a 50 por dia por conjunto, se a conversa custar R$ 5 a 15). Ferramenta: escolher entre DataForSEO e SE Ranking (PGMN) | Igor | Aberto |
| 15 | Revisão jurídica | Advogado agora; depois do primeiro cliente | Agora: avisos 18+ e CONAR, política de privacidade, cláusula de operador, termo de ciência e as licenças que WA-POL exige do cliente | Sócios | Aberto |
| 16 | Segurança | Cofre de senhas agora ou depois | Agora: credenciais root fora dos grupos e chave vazada trocada antes do próximo cliente (reunião de 01/10) | Bernardo | Aberto |
| 17 | Uma VPS por cliente | Manter; servidor compartilhado com isolamento | Manter no início, mas medir a manutenção: o custo cresce com cada cliente | Bernardo | Aberto |
| 18 | Ferramenta de tarefas | Trocar de novo; manter Sheets e AppSheet | Manter por 90 dias e acrescentar os 6 campos da POPE (revisor, produto e serviço, código do template e dia, aguardando quem e desde, critério de pronto, rodadas) | Henrique | Aberto |

**Quatro decisões novas, da revisão para a reunião** (a [página visual do de-para](https://claude.ai/artifact/GgVEKTEdMZnQCbPTTvnjAF) traz as 22 na ordem da pauta):

- **19. Preço contra horas do pacote.** A 144 h, um pacote de R$ 3.000 dá cerca de R$ 21 por hora, antes de VPS, ferramentas e criativos. Conferir o que cada pacote inclui e refazer a conta com o tempo real do Guto. Decidem os sócios.
- **20. Treino do atendente no Chatwoot.** Migrar o número para a Cloud API tira o número do aplicativo, e o padrão não tinha essa tarefa. Proposta: Hugo treina no D5, dentro do RT-03, antes da migração.
- **21. O que conta como entrega para cobrar os 50% restantes.** Proposta: o aceite do D7 cobra landing, perfil e tráfego; o SDR é cobrado no aceite do piloto, no D10.
- **22. Advertências do CONAR por tipo de bebida.** As pesquisas citam anexos diferentes. O Código tem três: A (destilados), P (cervejas e vinhos) e T (ices). Proposta: uma lista única, revisada pelo jurídico.

## O que isso muda no Guto até 29/11

O Guto está no 2º dia de um prazo corrido que termina no domingo, 29/11. Até lá cabem a landing publicada e o perfil preenchido com verificação pedida. O tráfego só sai "publicado ou em revisão" se acessos e canal forem resolvidos hoje. O SDR tem até 07/12, que são os 15 dias corridos contados de 23/11.

- [ ] Hoje: confirmar se a "Distribuidora de Bebidas Ouro Preto" do GBP Check é o perfil da Guto e pegar o convite de administrador (GM-01, ponto 8).
- [ ] Hoje: decidir o canal (ponto 2) e avisar o cliente de que a política do WhatsApp proíbe mensagem sobre álcool no app WhatsApp Business.
- [ ] Hoje: disparar a verificação da empresa e do domínio na Meta e a do anunciante no Google (MA-01, GA-01); pedir o orçamento de mídia por escrito.
- [ ] Landing, antes de apresentar: portão 18+, avisos, política de privacidade e banner (LP-07); botão com wa.me, mensagem pronta e código (LP-06); QA de velocidade com o motion que já está no ar (LP-09).
- [ ] Copy: conferir com o cliente os fatos do FAQ (horário, pedido mínimo, bairros, pagamento).
- [ ] Perfil: entrevista e fotos até quarta, 25/11; ficha e OK do cliente até sexta de manhã; preencher e pedir a verificação no mesmo dia.
- [ ] Pacote único de aprovação na sexta, 27/11 (landing, criativos, textos, ficha). Combinar agora se o cliente responde no sábado; se não, o tráfego publica na segunda, 30/11, e isso precisa ser dito hoje.
- [ ] SDR: formalizar com o cliente o piloto controlado até 07/12 e começar o discovery (SD-01).
- [ ] Quadro: abrir os 6 cartões de serviço do Guto com os códigos deste documento e o tempo real em cada tarefa, para que ele vire a base da v02 do template.

## Fontes e ressalvas

Três pontos de plataforma foram conferidos hoje na fonte oficial; o resto vem dos documentos anexados, com o nível de evidência marcado em cada linha.

**Lidas em 24/11/2026**

- [WhatsApp Business Messaging Policy](https://whatsappbusiness.com/policy/), atualizada em 23/09/2026: álcool é vertical regulada; o Brasil está na lista de países permitidos só pela Plataforma; mensagem sobre vertical regulada é proibida no app; experiência de comércio é proibida; mensagens com filtro de idade; caminho para humano; janela de 24 h.
- [Violações de política da WhatsApp Business Platform](https://developers.facebook.com/documentation/business-messaging/whatsapp/policy-enforcement-violations): a violação ALCOHOL cobre a venda de bebidas alcoólicas.
- [Política de anúncios de bebidas alcoólicas da Meta](https://transparency.meta.com/pt-br/policies/ad-standards/restricted-goods-services/alcohol/): sem direcionamento a menores de 18 e com a lei local.
- [Ajuda do Google Ads sobre a Data Manager API](https://support.google.com/google-ads/answer/16884284) e o [aviso aos desenvolvedores de 15/05/2026](https://developers.google.com/ads/blog/posts/2026/05/changes-to-offline-click-conversion): importação offline migrou para a Data Manager API.

**Documentos anexados:** DOC, PGMN, PPOS (relatório e página), PSDR (relatório e página), PTRA (relatório e página) e POPE (relatório, página e PDF). Três arquivos do SDR e dois do Posicionamento eram cópias idênticas. O handoff de 23/11 trata de outro cliente e de GA4, então não entrou aqui.

**Ressalvas**

- Seguem sem conferência no texto original, como as pesquisas marcaram: CONAR Anexo P, Lei 9.294/1996, ECA art. 243, política de álcool do Google Ads, Resolução ANPD 15/2024, percentuais do Whitespark, números do paper GEO, lista de eventos da API de Conversões para mensagens, regra de cerca de 50 eventos da Meta e disponibilidade da coexistência.
- A política do WhatsApp não diz se fechar pedido pela conversa conta como experiência de comércio (ponto 3). Este documento não é parecer jurídico.
- As horas são estimativas tiradas das pesquisas e do template v01, não medição. A distribuição por dia, a divisão de responsáveis e os horários da rotina são proposta minha.
