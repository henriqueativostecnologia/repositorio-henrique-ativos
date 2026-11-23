---
tipo: cópia de contexto (documento do Igor, texto integral)
original: Drive ATIVOS › 10 Comercial › 11 Prospecção › Extração (especificação e arquitetura)
link: https://docs.google.com/document/d/1kDxAd1v5ACrj1xcAoFYluxJBCu2v93bBTWKEDmrQJjs/edit
copiado: 23/11/2026
regra: usar como contexto; em conflito com decisões mais novas registradas em comercial/, vale a decisão mais nova
---

# Arquitetura da extração de negócios locais (ADR v0)

Nov 17, 2026 · @Ativos Tecnologia

## 1. Decisão

**Status:** proposto · **Decisor:** Igor · **Implementa:** a sessão de infraestrutura que receber este documento.

Construir um **único serviço em Python**, com **Postgres** como fonte da verdade, rodando em um container na **VPS Hostinger via Coolify**. O serviço executa as cinco etapas da especificação (descobrir, diagnosticar, achar o decisor, contatos, priorizar) como **jobs idempotentes controlados por uma tabela de fila no próprio Postgres**, sem Redis, sem Celery e sem n8n no caminho crítico. A saída é um CSV por visão (lista completa, resumo por bairro, rota).

Três decisões que sustentam o resto:

1. **Descobrir barato**: usar a busca de texto do Google Places pedindo só IDs (sem cobrança) e buscar os detalhes depois, apenas dos lugares que passam no filtro de segmento. Isso evita pagar o SKU Enterprise da busca em todo resultado.
2. **Guardar só o que os termos permitem**: o place\_id pode ser guardado; latitude e longitude só por até 30 dias; os demais campos do Google (nota, site, horário, telefone) não têm permissão expressa de cache nos termos. A base guarda o place\_id, o que a Ativos mede por conta própria (resposta do site, PageSpeed, CNPJ) e uma data de validade para o que veio do Google. Ponto a confirmar antes de escalar (seção 7).
3. **Piloto antes de escala**: uma praça, um segmento, cerca de 50 negócios, com teto de gasto no código.

**Fica de fora de propósito** (para não superengenheirar a v0): não há fila externa, painel próprio, scraping de Instagram, envio de mensagens, nem integração com CRM. Cada um entra só se o piloto mostrar necessidade.

## 2. Requisitos e restrições

Fonte: [Extração e qualificação de negócios locais (v0)](https://claude.ai/artifact/KGNVC69kFHe25UJqCMyMuy). Este documento não repete os critérios de qualificação; ele diz com quais peças eles rodam.

| Requisito | Detalhe | Consequência na arquitetura |
| --- | --- | --- |
| Cobertura | Belo Horizonte, Contagem e Nova Iguaçu; 4 segmentos, cerca de 40 termos de busca | Busca em grade por bairro e termo; place\_id como chave para não duplicar |
| Volume | Não estimado ainda; o piloto mede | Teto de gasto e cota por execução no código desde o dia 1 |
| Diagnóstico | Site (abre, HTTPS, celular, velocidade, ano), Google, Instagram, anúncios | Cada sinal é uma coluna com origem e data; limiares em configuração, não no código |
| Reprocessar | O Igor ajusta limiares depois do piloto | Guardar os sinais brutos, calcular cenário e nota em uma etapa separada e barata |
| Saída | Lista completa, resumo por praça, bairro e segmento, e rota | Três consultas SQL exportadas em CSV |
| Onde guardar a lista | Ainda não decidido (planilha, banco ou CRM) | Banco próprio mais exportação portável; CRM fica para depois |
| Quem opera | O Igor, sem time de engenharia dedicado | Poucas peças, um repositório, logs legíveis |
| Ambiente | VPS Hostinger com Coolify; teste na VPS, não em Docker local no notebook | Deploy por Coolify, variáveis em segredo, sem dependência do notebook |
| Stack que o Igor já domina | Python, Postgres, Docker Compose, n8n | Python e Postgres como núcleo; n8n apenas se ele quiser agendar e notificar |

## 3. Visão geral

&#91;embedded content: fluxo da extração · 6 etapas, 1 banco\]

As seis etapas rodam em ordem dentro do mesmo serviço. Cada uma lê e grava no Postgres, e só a etapa 5 (qualificar) não chama nenhuma API, por isso pode ser refeita de graça quando o Igor ajustar os limiares.

## 4. Ferramentas e APIs

Preços e franquias do Google conferidos na [tabela oficial](https://developers.google.com/maps/billing-and-pricing/pricing) e nos [campos por SKU](https://developers.google.com/maps/documentation/places/web-service/data-fields) em 17/11/2026; confirme de novo antes de rodar, porque mudam.

| Peça | Para que serve | Custo e limite | Piloto |
| --- | --- | --- | --- |
| Places API (New): Text Search, só IDs | Descobrir lugares por termo e bairro, retornando place\_id | Sem cobrança por requisição (SKU Essentials IDs Only, franquia ilimitada) | Sim |
| Places API (New): Place Details com field mask | Pegar website, nota, avaliações, horário, telefone, status | Campos de website, nota, avaliações, horário e telefone ficam no SKU Enterprise: US$ 20 por mil, 1.000 grátis por mês; businessStatus fica em Pro: US$ 17 por mil, 5.000 grátis | Sim |
| Places API (New): Text Search com esses campos | Alternativa de uma chamada só | Enterprise: US$ 35 por mil, 1.000 grátis. Mais caro que IDs mais Details | Não |
| PageSpeed Insights API v5 | Nota de desempenho no celular, cadeado e viewport | Gratuita com chave; cota informada por terceiros de 25.000 por dia por projeto (confirmar no console) | Sim |
| Cliente HTTP do próprio serviço (httpx) | Abre o site: status, redirecionamento, HTTPS, meta viewport, ano do rodapé, schema.org, link de WhatsApp | Sem custo; respeitar robots e limite de taxa | Sim |
| BrasilAPI (CNPJ) | Razão social, porte e quadro societário para achar o decisor | Gratuita, sem garantia de disponibilidade; tratar como melhor esforço com repetição | Sim, só para prioridade alta |
| Postgres na VPS (Coolify) | Fonte da verdade, fila de jobs, log de custo | Custo da VPS que já existe | Sim |
| Biblioteca de Anúncios da Meta | Saber se o negócio anuncia | Hoje manual; o projeto Ad Library Extractor do Igor pode ser reaproveitado | Não |
| Instagram | Perfil e último post | API oficial não serve para contas de terceiros que não são profissionais; raspagem viola os termos da Meta | Não |
| Verificador de e-mail | Validar e-mail antes de qualquer disparo | A escolher; não há envio nesta fase | Não |
| n8n | Agendar e avisar o fim do job | Opcional; o Igor já usa | Opcional |

Cotas e termos da BrasilAPI não foram confirmados (a documentação não carregou na consulta): a sessão de infraestrutura deve ler [brasilapi.com.br](https://brasilapi.com.br) e medir o limite no piloto.

## 5. Modelo de dados

Postgres, um schema `extracao`. Regra central: **cada dado que veio de fora carrega origem, data da coleta e, quando o Google exige, data de expiração**; a nota e o cenário são calculados a partir dos sinais guardados, nunca gravados à mão.

| Tabela | Chave | Conteúdo |
| --- | --- | --- |
| `lugares` | place\_id | segmento, subsegmento, termo que encontrou, praça, bairro, cidade, estado do pipeline por etapa, descartado (sim, não) e motivo |
| `dados_google` | place\_id + coletado\_em | Campos vindos do Google (nome, endereço, nota, avaliações, site, horário, telefone, status, lat/lng) com `expira_em`; latitude e longitude expiram em até 30 dias e uma rotina apaga ou renova |
| `checagem_site` | place\_id + coletado\_em | URL final, status HTTP, HTTPS, meta viewport, ano no rodapé, schema.org local, WhatsApp ou telefone clicável, nota PageSpeed no celular, erros |
| `checagem_busca_local` | place\_id + coletado\_em | Termo e bairro pesquisados, posição do lugar, diferença de avaliações para o 1º |
| `decisor` | place\_id | Nome, CNPJ, porte, quadro societário resumido, perfil no Instagram, confiança (alta, média, baixa) e origem |
| `contatos` | place\_id | WhatsApp, e-mail, telefone (celular ou fixo), canal preferido, e-mail validado (sim, não, não verificado) |
| `qualificacao` | place\_id + versao\_config | Cenário A a D, pontos, faixa de prioridade, ação no Posicionamento Digital, sinais que dispararam |
| `config_criterios` | versao | Limiares e pesos (nota mínima, avaliações mínimas, velocidade, idade do rodapé, dias do post) para ajustar sem mexer no código |
| `fila_jobs` | id | etapa, place\_id, estado (pendente, rodando, ok, erro), tentativas, próxima tentativa, erro |
| `uso_api` | id | chamada, SKU, quantidade, custo estimado, data; alimenta o teto de gasto |

**Visões de saída** (consultas SQL exportadas em CSV): lista completa, resumo por praça, bairro e segmento (contagem por faixa e por cenário) e rota de um bairro ordenada por prioridade.

**Idempotência**: toda etapa pode rodar de novo para o mesmo place\_id sem duplicar nem estragar o que já existe; a chave de cada registro de checagem é place\_id mais coletado\_em, e a qualificação referencia a versão da configuração usada, o que permite recalcular tudo depois que o Igor mudar um limiar.

## 6. Execução

Um programa com subcomandos (um por etapa) e um modo que processa a fila. Rodado por tarefa agendada do Coolify ou manualmente por comando. Sem servidor de longa duração na v0.

1. **`descobrir`**: para cada praça, bairro e termo, chama a busca de texto só com IDs, grava os place\_id novos em `lugares` e enfileira a coleta de detalhes. Filtra por segmento antes de pagar os detalhes.
2. **`detalhes`**: Place Details com a lista mínima de campos, grava em `dados_google` com `expira_em`.
3. **`diagnosticar`**: abre o site (httpx), chama o PageSpeed e roda a busca local para a posição. Cada checagem é um job independente com repetição.
4. **`decisor` e `contatos`**: só para prioridade alta ou média, para não gastar chamada à toa.
5. **`qualificar`**: lê os sinais e a `config_criterios` e escreve `qualificacao`. Não chama API nenhuma e pode rodar quantas vezes o Igor quiser.
6. **`exportar`**: gera os três CSVs.

**Controles obrigatórios (dia 1):**

- **Teto de gasto** por execução e por dia, lido de `uso_api`; ao atingir, o job para e registra. Alerta de orçamento também no Google Cloud.
- **Limite de taxa** e repetição com espera crescente em cada API; falha de uma etapa não derruba as outras.
- **Fila no Postgres** com bloqueio de linha (`FOR UPDATE SKIP LOCKED`), tentativas máximas e estado por lugar; reiniciar o serviço retoma de onde parou.
- **Registro por execução**: quantos lugares por etapa, quantos erros, custo estimado e real.

**Ordem do piloto**: uma praça, um segmento (Alimentação), cerca de 50 negócios. Antes de rodar, o programa imprime a estimativa de custo e pede confirmação. Depois, o relatório do piloto traz cobertura de cada campo, erros e custo real, e o Igor decide se escala.

## 7. Segurança, termos e LGPD

- **Chaves**: a chave do Google Cloud fica em segredo do Coolify, restrita às APIs usadas (Places e PageSpeed) e ao IP da VPS. Nunca em repositório nem em log.
- **Termos do Google Maps Platform**: pelos [termos específicos](https://cloud.google.com/maps-platform/terms/maps-service-terms), o place\_id pode ser guardado; latitude e longitude podem ficar em cache por até 30 dias corridos e depois devem ser apagadas; para os outros campos (nome, nota, site, horário, telefone) a seção da Places API não traz permissão expressa de cache. As proibições gerais sobre pré-busca e base de dados estão nos termos gerais, que não foram lidos aqui. **A base desta arquitetura já nasce com `expira_em` e uma rotina de limpeza; antes de escalar, o Igor (com apoio jurídico, isto não é parecer) confirma se guardar sinais derivados, como "Google fraco", e os dados de contato está dentro do permitido.** Se não estiver, o plano B é guardar só place\_id e consultar o Google de novo no dia da rota.
- **Instagram**: fora da v0. A API oficial não lista contas de terceiros que não sejam profissionais e a raspagem viola os termos da Meta.
- **LGPD**: o dono pode ser pessoa física. Guardar só o necessário para a visita, registrar a fonte, permitir exclusão por place\_id e não guardar dado sensível.
- **Sem envio de mensagem**: este serviço só lê e classifica.
- **Acesso ao banco**: só o serviço e o Igor; backup diário da VPS e exclusão de dados vencidos.

## 8. Opções consideradas

| Decisão | Escolha | Alternativa | Por que a escolha |
| --- | --- | --- | --- |
| Onde fica a lógica | Código Python em um serviço | Fluxos no n8n | Regras de nota, repetição, teto de gasto e idempotência ficam testáveis e versionadas em código; n8n fica difícil de depurar com milhares de itens. n8n pode só agendar e avisar |
| Banco | Postgres na VPS | Supabase | Menos peças e sem custo extra. Supabase vale se o Igor quiser painel e acesso por outras ferramentas; é Postgres por baixo, então a migração é simples |
| Fila | Tabela no Postgres com SKIP LOCKED | Redis com Celery ou RQ | O volume da v0 não justifica outra peça para operar |
| Descobrir lugares | API oficial do Google Places | Apify (raspagem de Maps) ou provedores de dados | API oficial é mais estável e clara nos termos; raspagem terceirizada pode ser mais barata em volume mas muda sem aviso e tem risco de termos. Reavaliar se o custo do piloto assustar |
| Diagnóstico de site | httpx mais PageSpeed API | Navegador automatizado (Playwright) em todo site | O PageSpeed já renderiza e mede; navegador próprio só entra se faltar algum sinal |
| Interface | CSVs e consultas SQL | Painel web | O Igor precisa da lista, não de um painel; painel entra depois se o uso pedir |
| Ambiente | Deploy na VPS por Coolify | Docker local no notebook | Preferência do Igor: testar na VPS |

## 9. Plano de implementação

Para a sessão que monta a infraestrutura. Cada fase termina com um critério que dá para verificar.

| Fase | O que entregar | Critério de aceite |
| --- | --- | --- |
| 0. Pré-requisitos | Projeto no Google Cloud com faturamento, chave restrita, alerta de orçamento; repositório; Postgres no Coolify | Chamada de teste da API responde; alerta de gasto configurado; banco acessível só pelo serviço |
| 1. Esqueleto | Schema, fila, `uso_api` com teto, configuração de critérios, deploy no Coolify | Rodar um job vazio na VPS e ver o registro no banco; teto interrompe o job |
| 2. Descobrir e detalhes | Busca por IDs, detalhes com lista mínima de campos, `expira_em` e limpeza | 50 lugares de um segmento gravados sem duplicata; custo estimado igual ao real em até uma margem definida |
| 3. Diagnosticar | Checagem de site, PageSpeed, busca local | Cobertura de cada campo medida; erros registrados; reexecução não duplica |
| 4. Qualificar e exportar | Cenário, nota, três CSVs | Igor abre os CSVs e reconhece o cenário de 10 negócios que ele conhece; mudar um limiar e recalcular sem chamar API |
| 5. Decisor e contatos | CNPJ e contatos para prioridade alta | Taxa de decisor identificado e de WhatsApp medida no piloto |
| 6. Relatório do piloto | Cobertura, erros, custo real | Igor decide: escalar, ajustar critérios ou trocar de fonte |
| 7. Escala (só após o aval) | Demais praças e segmentos | Custo dentro do teto aprovado |

Os critérios de qualificação, a nota e as saídas estão na [especificação de extração](https://claude.ai/artifact/KGNVC69kFHe25UJqCMyMuy) e não devem ser reescritos no código sem ela.

## 10. Em aberto

| Item | Quem decide | Impacto |
| --- | --- | --- |
| Os termos gerais do Google permitem guardar sinais derivados e contatos extraídos do Maps? Se não, ficar só com place\_id | Igor, com apoio jurídico | Define o modelo de dados definitivo (seção 7) |
| Teto de gasto do piloto e da escala, em reais | Igor | Entra como configuração do teto na fase 1 |
| Quantos negócios por bairro e quantos bairros na grade | Igor, depois do piloto | Define o custo da escala |
| Cota e termos da BrasilAPI | Sessão de infraestrutura, no piloto | Pode exigir fonte alternativa de CNPJ |
| Verificador de e-mail | Igor | Só se houver envio no futuro |
| Instagram e Biblioteca de Anúncios entram na v1? | Igor, depois do piloto | Hoje ficam manuais |
| Banco definitivo da lista (Postgres próprio, Supabase, CRM) | Igor | Afeta exportação e integração |
| Quem opera no dia a dia (Igor, sessão de código ou time) | Igor | Define o nível de documentação e o alerta |
