---
tipo: cópia de contexto (documento do Igor, texto integral)
original: Drive ATIVOS › 10 Comercial › 11 Prospecção › Extração (especificação e arquitetura)
link: https://docs.google.com/document/d/1tmHxkKivR1YYOMjeA-9gh4t_BB-oFa-BG5hNxYQUdaI/edit
copiado: 23/11/2026
regra: usar como contexto; em conflito com decisões mais novas registradas em comercial/, vale a decisão mais nova
---

# Extração e qualificação de negócios locais – especificação v0

Nov 16, 2026 · @Ativos Tecnologia

## 1. Objetivo e escopo

Este documento diz ao chat de extração o que levantar no Google e como classificar cada comércio local, para gerar uma lista priorizada por rota de visita presencial. É um documento novo, separado do Playbook Jurídico; a lógica de levantamento foi adaptada dele (Etapa 1: descobrir, diagnosticar, achar o decisor, contatos, priorizar).

- **Quem usa a lista**: um representante comercial em Belo Horizonte (BH e Contagem) e outro em Nova Iguaçu (RJ). Quantas visitas por dia cada um faz ainda não está definido.
- **Abre-carteira (confirmado)**: Posicionamento Digital. Otimizar o Google Meu Negócio e entregar um site otimizado para SEO, GEO e AEO, para o comércio local acompanhar a evolução da tecnologia. Quem já tem site ou perfil: otimizar. Quem não tem: criar do zero, com base no mapeamento das landing pages que a Ativos já tem como cases.
- **Entrega esperada**: uma lista de comércios por segmento e bairro, cada um com diagnóstico (tem site? Google Meu Negócio fraco? já anuncia?), contato do decisor quando houver, nota de prioridade e rota (seções 3 a 6).
- **Fora deste chat**: textos de abordagem, objeções e estratégia por segmento (vêm depois, em outro momento) e a escolha dos bairros por onde a rota começa (o Igor define depois da primeira extração).

## 2. Segmentos e termos de busca no Maps

Ordem de prioridade: Alimentação primeiro (6 cases nas 2 praças), depois Automotivo; Serviços técnicos e Tatuagem e beleza entram como complemento. Praças com cases: Belo Horizonte e Contagem (MG) e Nova Iguaçu (RJ). Em cada visita o representante leva o case do mesmo subsegmento, então a extração deve etiquetar o subsegmento de cada comércio.

| Prioridade | Segmento | Cases (landing pages) | Observação |
| --- | --- | --- | --- |
| 1 | Alimentação | Café 40 (Nova Iguaçu): cafeteria, coworking, eventos. Tourão (BH): self-service, churrasco, marmita. Gennaro (Savassi, BH): italiano com toque mineiro. Nashy Sushi (BH e Contagem): japonês, rodízio. Seu Vidal (Nova Iguaçu): smash burger. Guto Bebidas (BH): adega e delivery | Prioridade |
| 2 | Automotivo | Quality (Nova Iguaçu): detalhamento, vitrificação, busca e entrega. MK Garagem (Concórdia, BH): lavagem detalhada, polimento | 2 cases |
| 3 | Serviços técnicos | Quadrimax (BH e região): ar-condicionado, instalação, manutenção, higienização. Manutenção e venda de iPhone: sem case ainda | Complemento |
| 4 | Tatuagem e beleza | Quintão Ink (Toronto): serve de portfólio, não de "atendemos aqui" | Complemento |

### Termos de busca e segmentos ligados

| Segmento | Buscar no Maps | Ligados (ampliar depois) |
| --- | --- | --- |
| Alimentação | cafeteria, padaria artesanal, confeitaria, restaurante self service, marmitaria, churrascaria, pizzaria, restaurante italiano, restaurante japonês, temakeria, hamburgueria, açaí, pastelaria, adega, distribuidora de bebidas, açougue | – |
| Automotivo | estética automotiva, detalhamento automotivo, lava jato, polimento, vitrificação, higienização automotiva, martelinho de ouro, insulfilm, envelopamento, PPF | funilaria, auto center, troca de óleo, som automotivo, estética de motos |
| Serviços técnicos (climatização) | ar condicionado, instalação de ar condicionado, climatização, refrigeração | assistência técnica, eletricista, energia solar, dedetização, desentupidora, serralheria, vidraçaria |
| Serviços técnicos (iPhone) | assistência técnica iPhone, conserto de iPhone, troca de tela iPhone, troca de bateria iPhone, loja de iPhone, iPhone seminovo | – |
| Tatuagem e beleza | estúdio de tatuagem, tatuador, piercing | barbearia, sobrancelha, lash designer, micropigmentação, nail designer |

A página land-posicionamento-ativos é a oferta da Ativos (Google e Maps, anúncios, WhatsApp com IA e CRM), não um case.

## 3. Pipeline de extração

Cinco passos, na ordem. Faça primeiro um piloto pequeno (uma praça, um segmento, poucos bairros) para validar custo de API e qualidade dos dados antes de escalar.

| Passo | O que acontece | Fonte / API | Campos que saem |
| --- | --- | --- | --- |
| 1. Descobrir | Para cada praça (BH, Contagem, Nova Iguaçu) e cada termo de busca do segmento (seção 2), buscar em grade por bairro. Guardar o place\_id para não duplicar e poder reexecutar | Google Places API (busca por texto e detalhes do lugar) | place\_id, nome, endereço, bairro, coordenadas, telefone, website, nota, nº de avaliações, horário, status de funcionamento, tipo, segmento e subsegmento |
| 2. Diagnosticar | Classificar site, Google Meu Negócio e Instagram pelos critérios da seção 4 | Requisição HTTP própria ao site + PageSpeed Insights API (gratuita, com chave); Places API; extração atual do Instagram do Igor | status do site e motivos, nota de velocidade, posição no GMN, atividade do Instagram, se anuncia |
| 3. Achar o decisor | Identificar dono ou gerente. Cruzar a página "sobre" do site, bio e link do Instagram do negócio e o quadro societário do CNPJ | Dados do próprio site e Instagram; BrasilAPI ou dados abertos da Receita (CNPJ, quadro societário, porte) | nome do decisor, perfil no Instagram, CNPJ, grau de confiança (alto, médio, baixo) |
| 4. Contatos | Separar celular de fixo no telefone do Google; achar link wa.me ou e-mail no site e no rodapé; validar o e-mail antes de qualquer disparo | Dados do site e do Google + verificador de e-mail (a escolher) | WhatsApp, e-mail validado, telefone, canal preferido |
| 5. Priorizar | Calcular a nota de prioridade e agrupar por bairro (seção 5) | Planilha ou banco | lista ordenada por praça, bairro e prioridade |

Observação para o passo 3: em comércio local o decisor costuma ser o dono ou um gerente, não um sócio de escritório. Nem sempre haverá nome público; nesse caso, registrar "decisor não identificado" e deixar o representante descobrir na visita.

## 4. Critérios de qualificação

Os limites abaixo são um padrão sugerido para o Igor aprovar ou ajustar (hipótese). O chat deve parametrizá-los para mudar sem refazer a extração. Registre sempre o motivo de cada classificação.

| Critério | Como detectar | Classificação |
| --- | --- | --- |
| Sem site próprio | Campo website vazio no Google, ou apontando só para Instagram, Facebook, Linktree, wa.me ou agregador de delivery (iFood, Rappi etc.) | sem site |
| Site com problema | Sinais, cada um registrado: não abre (erro HTTP ou timeout); sem HTTPS; sem meta viewport (não adaptado ao celular); nota de desempenho no celular abaixo de 50 no PageSpeed; ano no rodapé de 3 anos ou mais atrás; sem dados estruturados schema.org do tipo local; sem WhatsApp ou telefone clicável | defasado se houver sinal fatal (não abre, sem HTTPS ou sem celular) ou 2 sinais ou mais; senão, ok |
| Google Meu Negócio fraco | Nota abaixo de 4,3, ou menos de 30 avaliações, ou sem horário, sem website ou poucas fotos. Rodar a busca local "termo + bairro" e registrar a posição do comércio e a diferença de avaliações para o 1º do mapa | fraco se algum desses; mal ranqueado se estiver fora dos 3 primeiros da busca local |
| Instagram parado | Perfil encontrado pelo link do site ou do Google; data do último post, frequência, seguidores, link na bio | sem perfil, parado (último post há mais de 60 dias) ou ativo |
| Já anuncia | Consulta do nome do negócio na Biblioteca de Anúncios da Meta (hoje manual) | anuncia, não anuncia, não verificado |

A API do Google não informa se o perfil foi reivindicado pelo dono; não classifique isso, só o que os campos mostram.

### Cenário do comércio e ação do abre-carteira

Cada comércio recebe um cenário, na ordem abaixo (o primeiro que se aplica). O abre-carteira é sempre o Posicionamento Digital; muda o que se faz nele.

| Cenário | Regra | Ação no Posicionamento Digital |
| --- | --- | --- |
| A. Sem site | sem site próprio | Criar site do zero, otimizado para SEO, GEO e AEO, e otimizar o Google Meu Negócio |
| B. Site defasado | site com problema = defasado | Otimizar e modernizar o site (SEO, GEO, AEO) e o Google Meu Negócio |
| C. Site ok, GMN fraco | site ok e GMN fraco ou mal ranqueado | Otimizar o Google Meu Negócio e ajustar o site |
| D. Site ok, GMN ok | nenhum dos anteriores | Baixa prioridade para o abre-carteira; olhar Instagram e anúncios como segundo gancho |

## 5. Nota de prioridade e rota

A ordem herdada do Jurídico: sem site ou site defasado pesa mais, depois Google Meu Negócio fraco, depois já anuncia. Pesos e faixas são hipótese para o Igor ajustar.

| Sinal | Pontos |
| --- | --- |
| Sem site próprio | +5 |
| Site defasado | +4 |
| Google Meu Negócio fraco | +2 |
| Mal ranqueado na busca local | +1 |
| Instagram parado ou sem perfil | +1 |
| Já anuncia (indica verba de marketing) | +1 |
| Decisor identificado, confiança alta ou média | +1 |
| WhatsApp ou celular disponível | +1 |

Faixas: alta com 6 pontos ou mais, média de 3 a 5, baixa abaixo de 3. Excluir da lista: negócio fechado definitivamente, duplicado por place\_id e endereço que não recebe visita.

**Rota**: agrupar por praça, bairro e subsegmento, e ordenar por prioridade dentro do bairro, para o representante render várias visitas na mesma rota com o case do mesmo subsegmento. Os bairros por onde a rota começa não são escolhidos pelo chat: entregue ao Igor o resumo por praça, bairro e segmento (quantos negócios de prioridade alta, média e baixa) e ele decide.

## 6. Saída esperada

Três visões sobre a mesma base, em CSV ou planilha (onde a lista fica guardada em definitivo ainda não foi decidido, então o formato deve ser portável para planilha, banco ou CRM):

1. **Lista completa**: um registro por comércio, com os campos abaixo.
2. **Resumo para escolher bairros**: praça × bairro × segmento, com a contagem de negócios por prioridade e por cenário.
3. **Rota**: lista de um bairro, ordenada por prioridade, pronta para o representante.

| Grupo | Campos |
| --- | --- |
| Identificação | place\_id, nome, endereço, bairro, cidade, coordenadas, telefone, website, nota, nº de avaliações, horário, status |
| Segmento | segmento, subsegmento, termo de busca que o encontrou, case a levar |
| Site | tem site próprio (sim, não), status (sem site, defasado, ok), sinais detectados, nota de velocidade no celular |
| Google Meu Negócio | fraco (sim, não) e motivos, posição na busca local, diferença de avaliações para o 1º |
| Instagram | perfil, seguidores, data do último post, situação (sem perfil, parado, ativo) |
| Anúncios | anuncia (sim, não, não verificado) |
| Decisor | nome, perfil no Instagram, CNPJ, grau de confiança |
| Contato | WhatsApp, e-mail validado, telefone (celular ou fixo), canal preferido |
| Qualificação | cenário (A a D), pontos, faixa de prioridade, ação no Posicionamento Digital |
| Controle | data da extração, fonte de cada campo, erros |

## 7. Cuidados

- **Termos e custo do Google**: confirmar nos termos atuais da Google Maps Platform o que pode ser guardado além do place\_id e por quanto tempo. Pedir só os campos necessários, definir orçamento e alerta de gasto antes de rodar em escala, e estimar o custo do piloto antes.
- **Instagram**: a API oficial não lista seguidores nem posts de outras contas fora do Business Discovery (só contas profissionais). Raspagem viola os termos da Meta e pode bloquear a conta: usar só para prioridade alta, em volume baixo e com conta separada. Preferir dados públicos já linkados no site ou no Google.
- **LGPD**: o dono pode ser pessoa física. Coletar só o necessário para a visita, sem dado sensível, registrar a fonte e manter forma de excluir quem pedir. Orientação geral, não parecer jurídico.
- **Dados mudam**: nota, posição no mapa e status de funcionamento mudam. Registrar a data da extração e reconferir o diagnóstico pouco antes da visita, antes de citar qualquer número ao comerciante.
- **Esta extração não envia mensagens**: só levanta e classifica. Qualquer disparo de WhatsApp ou e-mail fica fora deste escopo.

## 8. Em aberto

| Item | Situação |
| --- | --- |
| Bairros por onde a rota começa | O Igor define depois da raspagem, olhando o resumo por praça, bairro e segmento. O chat de extração não escolhe. |
| Quem visita | Um representante em Belo Horizonte (cobre Contagem) e um em Nova Iguaçu. |
| Visitas por dia | Ainda não definido. Por isso a rota sai ordenada por prioridade, sem corte por dia. |
| Limiares do critério (nota, avaliações, velocidade, idade do site, posts) | Hipótese deste documento. O Igor aprova ou ajusta depois de ver o piloto. |
| Pesos da nota de prioridade | Hipótese. Ajustar com o resultado das primeiras visitas. |
| Onde a lista fica guardada | Não decidido (planilha, banco ou CRM). Entregar em formato portável. |
| Abordagem, objeções e estratégia por segmento | Fora deste documento: está sendo montada à parte, a partir do cliente no centro. |

## 9. Instruções para o chat de extração

Você vai executar a extração e a qualificação descritas acima. Siga esta ordem:

1. **Piloto primeiro**: uma praça, um segmento, cerca de 50 negócios. Estime o custo das chamadas antes de rodar e mostre ao Igor a lista, os campos preenchidos, os erros e o custo real.
2. **Só depois do aval**, rodar os demais segmentos e praças (Belo Horizonte e Contagem, Nova Iguaçu), na prioridade da seção 2.
3. **Não escolha bairros nem monte rota final.** Entregue a visão de resumo (seção 6, item 2) e espere o Igor decidir.
4. **Marque a origem e a confiança de cada campo.** Quando não conseguir confirmar algo (decisor, site oficial, status de funcionamento), deixe vazio ou marque "não verificado". Nunca preencha por suposição.
5. **Aplique os critérios da seção 4 como estão**, com os limiares da hipótese, e registre quais sinais dispararam em cada negócio para o Igor poder ajustar depois.
6. **Respeite a seção 7**: termos do Google, limites do Instagram, LGPD, e nenhum envio de mensagem.
7. **Se algo travar** (cota, chave, campo indisponível), diga o que tentou e proponha o caminho mais barato para destravar, em vez de parar.

**Entregáveis**: lista completa, resumo para escolher bairros, relatório do piloto (cobertura de cada campo, erros, custo) e a lista de decisões que dependem do Igor.
