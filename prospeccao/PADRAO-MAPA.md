---
tipo: procedimento padrão (POP)
dono: Henrique
atualizado: 17/11/2026
revisao: depois das primeiras visitas de cada cidade, ou quando uma regra mudar
modelo: mapa de Nova Iguaçu, Centro (17/11/2026)
---

# Padrão do mapa de prospecção de comércio local

## Objetivo

Qualquer sócio cria o mapa de uma cidade ou bairro novo **idêntico** ao de Nova Iguaçu: mesma busca, mesmas regras, mesma planilha e mesma página. Só muda **onde** (cidade, bairros e ponto de saída).

## Escopo

* Vale para: comércio local, imobiliário, jurídico e automotivo do Posicionamento Digital (`servicos/catalogo.md`).
* Não vale para: e-commerce e agências (Rastreamento de Dados), que não são prospectados na rua.
* Os programas estão em `prospeccao/programas/prospeccao/` (passo a passo técnico no `LEIA-ME.txt` de lá). Este documento é o **padrão**: o que o mapa tem e o que pode ou não mudar.

## O que muda e o que não muda

| Muda por cidade (arquivo `dados/config.json`) | Nunca muda (é o padrão) |
|---|---|
| Cidade e título (`titulo`, `cidade_no_endereco`) | Termos de busca e quantidade de pontos por termo |
| Bairros da área e bairros sem contorno (`bairros_sem_contorno`) | Regras de segmento, grupo, cenário, oferta e planejada/opcional |
| Ponto de saída (`ponto_saida`) | Colunas da planilha e abas |
| Fundo do mapa e seus limites (`fundo_mapa`, `limites_fundo`) | Campos do cartão, filtros, cores e alertas da página |
| Lista de redes da região (`redes`, `fora_do_roteiro`, `conferir_segmento`) | Limites dos **sinais** (nota 4,0, 10 avaliações, PageSpeed 50, ano 2023): **não cortam lojas**, só definem alertas e cenário |
| Fonte e descrição da área (`fonte`, `area_descricao`) | Cases por segmento (`cases`), iguais em todas as cidades |

Qualquer mudança na coluna da direita é decisão do Henrique e entra por PR, valendo para todas as cidades.

## Quem faz o quê (RACI)

| Etapa | Responsável | Aprova | Consultado | Informado |
|---|---|---|---|---|
| Escolher cidade e bairros | Sócio da cidade | Henrique | Igor | Sócios |
| Montar área e mapa da área | Claude do sócio | Sócio da cidade | — | Henrique |
| Estimativa e buscas (SerpApi) | Claude do sócio | Sócio da cidade (antes de cada busca) | Henrique (saldo do mês) | — |
| Teste dos sites (Firecrawl) | Claude do sócio | Sócio da cidade | — | — |
| Gerar planilha e mapa, salvar no Drive | Claude do sócio | Sócio da cidade | — | Henrique |
| Visitas e áudio de feedback | Sócio da cidade | — | — | Henrique e Igor |
| Mudar uma regra do padrão | Henrique | Henrique | Igor | Todos os sócios |

## Fluxo

```
1 Área ──► 2 Pontos e estimativa ──► 3 Buscas ──► 4 Teste dos sites
                (aprovar)                (SerpApi)     (Firecrawl)
                                                            │
8 Visitas ◄── 7 Drive ◄── 6 Planilha e mapa ◄── 5 Classificar e roteiro
(áudio)
```

## Etapas

### 1. Área
* **Como:** lista oficial de bairros da prefeitura; contornos do OpenStreetMap; mapa simples da área (`mapa_area.py`) para aprovar.
* **Atenção:** conferir na lista se algum bairro mudou de cidade (em Nova Iguaçu, Juscelino hoje é de Mesquita). Bairro pequeno sem contorno entra em `bairros_sem_contorno`.
* **Saída:** área aprovada e ponto de saída escolhido (uma avenida principal, sem número).

### 2. Pontos e estimativa
* **Como:** `1_grade.py`. Termos comuns em pontos a cada **2 km** dentro da área (ou até **300 m** da borda); termos raros em **4 pontos** bem distribuídos.
* **Regra:** mostrar a estimativa de buscas e **esperar a aprovação** do sócio antes de buscar.

### 3. Buscas (SerpApi pelo MCP)
* **Como:** `2_buscar.py`, sempre `--simular` antes. **Um termo por busca**, página 1; página 2 só se o sócio decidir.
* **Padrão de cada busca:** Google Maps, idioma pt-BR, zoom 15 (comuns) ou 14 (raros), até 20 lojas por busca.
* **Trava:** para quando faltarem 10 buscas para o limite do mês (250 no plano grátis).

**Termos de busca do padrão**

| Tipo | Termos (8 pontos cada se comum, 4 se raro) |
|---|---|
| Comuns | advocacia previdenciária, advocacia trabalhista, estética automotiva, lava-rápido, imobiliária, cafeteria, bar, restaurante, hamburgueria, restaurante japonês, barbearia, salão de beleza, assistência técnica de celular |
| Raros | detalhamento automotivo, compra e venda de veículos, construtora, empório, restaurante italiano, distribuidora de bebidas, adega, ar condicionado, estúdio de tatuagem, clínica de estética, loja de celular |
| Fora por enquanto | clínica (só mapear, ainda não abordar) |

### 4. Teste dos sites (Firecrawl)
* **Como:** abrir cada site próprio e registrar: **HTTPS**, **adapta ao celular**, **fora do ar** (domínio inexistente, erro 404/5xx). Certificado inválido conta como "sem HTTPS". Bloqueio de robô fica "sem conclusão".
* **Ainda fora:** PageSpeed (precisa de chave do Google) e ano do rodapé (só sinal de apoio).
* **Custo:** cerca de 1 crédito do Firecrawl por site.

### 5. Classificar e montar o roteiro
* **Como:** `3_classificar.py` e `4_roteiro.py`. Regras na seção "Regras do padrão".
* **Roteiro:** blocos de até **10 planejadas**, do mais perto para o mais longe do ponto de saída; opcionais presas à planejada mais próxima (12a, 12b).

### 6. Planilha e mapa
* **Como:** `5_planilha.py` e `6_pagina.py` (Leaflet embutido e fundo do mapa embutido: funciona sem internet). Fundo do mapa: passo "Gerar o fundo do mapa" do `LEIA-ME.txt`.
* **Se já houver visitas:** baixar a planilha do Drive e passar no passo 4, para **não perder** Resultado, Data da visita, Falou com quem, Objeção e Próximo passo.

### 7. Drive
* **Onde:** `10 Comercial › 11 Prospecção`. Planilha como **Google Sheets** ("Roteiro <Cidade> <Área> - visitas") e mapa como `Roteiro_<Cidade>_<Area>_<AAAA-MM-DD>.html`.
* **Só a versão mais nova fica na pasta** (decisão de 17/11/2026). Ao gerar de novo: a **planilha** é atualizada no mesmo arquivo do Google Sheets (o link não muda e o que já foi preenchido nas colunas de visita é mantido); o **mapa** novo entra e o anterior vai para a lixeira do Drive. Guardar uma versão específica só quando o sócio pedir.
* **Nunca** no GitHub: planilhas, respostas das buscas, testes dos sites e a configuração com nomes de redes.

### 8. Visitas
1. No mapa (na porta): escolher o **Resultado da visita** no cartão. A loja fica roxa com ✓.
2. No chat do Claude (indo para a próxima): **áudio** respondendo à checklist de feedback (pauta de 16/11, seção 3), dizendo também o resultado. O Claude registra na planilha.

## Regras do padrão

**Grupo:** "com site" = site próprio. "Sem site" = sem site, ou "site" que é só Instagram, Facebook, WhatsApp, iFood, Linktree, página de links, cardápio online, página de agendamento, página de plataforma, anúncio em portal, perfil no Jusbrasil, site grátis do Google ou link encurtado.

**Segmentos (22):** Advocacia previdenciária · Advocacia trabalhista · Advocacia (trabalhista e previdenciária) · Imobiliária · Construtora · Compra e venda de veículos · Estética / detalhamento · Lava-jato · Cafeteria · Empório · Bar · Hamburgueria · Restaurante japonês · Restaurante italiano / pizzaria · Restaurante self-service / marmita · Restaurante (outros) · Distribuidora de bebidas / adega · Barbearia · Beleza · Celular (manutenção e venda) · Climatização · Tatuagem. Clínica fica em aba própria ("só mapear").

**Cenário (nesta ordem):**

| Cenário | Regra | Oferta indicada |
|---|---|---|
| A | Sem site próprio | Google Meu Negócio + site novo |
| B | Site próprio com falha: sem HTTPS, não se adapta ao celular, fora do ar (ou PageSpeed abaixo de 50, quando houver) | Google Meu Negócio + reforma do site |
| C | Site ok e Google fraco: **Força no Google** fraca ou média, nota abaixo de 4,0, menos de 10 avaliações, ficha sem dono ou sem horário | Google Meu Negócio (+ ajuste leve no site) |
| D | Site ok e Google ok | Baixa prioridade (outro serviço ou diagnóstico de cortesia) |
| B ou C / B ou D | Site ainda sem teste | Definir depois do teste |

**Nenhuma loja é cortada por nota ou por avaliações** (decisão de 17/11/2026, que também tirou o antigo corte do lava-jato). Nota baixa e poucas avaliações são oportunidade: a loja entra planejada, com o alerta correspondente.

**Força no Google (0 a 100):** nota superficial da ficha, com os critérios do GBP Check (`plataformas/gbp-check/`), a partir dos dados da busca. Proposta inicial de 17/11/2026, a ajustar depois do curso de SEO; pesos na configuração (`forca_google`).

| Item | Pontos |
|---|---|
| Ficha verificada (tem dono) | 20 |
| Avaliações na média do segmento na área ou acima (metade da média: 10) | 20 |
| Nota 4,5+ (4,0 a 4,4: 10) | 15 |
| Posição na busca: top 3 (4ª a 10ª: 12; 11ª a 20ª: 6) | 20 |
| Mais de uma categoria | 10 |
| Horário, telefone e site na ficha | 5 cada |

Faixas: **Fraco** abaixo de 40 · **Médio** 40 a 69 · **Forte** 70+. Fraco e Médio contam como "Google fraco" no cenário. Não mede fotos, postagens e respostas às avaliações: para os leads quentes, rodar a Pré Análise do GBP Check.

**Planejada / opcional:** planejada = cenários A, B e C (e "B ou C"/"B ou D" até o teste). **Opcional = só o Cenário D.** Poucas avaliações continua planejada. A regra "segmento sem case fica opcional" existe no programa (`aguardando_case`), mas hoje está vazia.

**Case a levar (por segmento):** o nome e o link de cada case vêm do **Índice de landing pages de demonstração** (Drive, `10 Comercial › 14`) e ficam na configuração da cidade (`cases`), fora do repositório.

| Situação | Segmentos |
|---|---|
| Case próprio | Cafeteria e empório (mesmo case) · hamburgueria · self-service/marmita · italiano · japonês · distribuidora/adega · estética e lava-jato (mesmo case) · climatização · tatuagem |
| Case emprestado (o de alimentação mais parecido) | Bar · Restaurante (outros) |
| Sem case próprio (landing em produção) | Barbearia · Celular · Beleza |
| Sem case, playbook próprio | Advocacia (vai usar a página do CLI-001 Dr. Felipe quando publicada) · Imobiliária · Construtora · Compra e venda de veículos |

**Alertas (por extenso no cartão):** Ficha sem dono: mostrar no celular · Poucas avaliações: confirme que está aberta · Nota baixa: conversa sobre reputação · Rede: perguntar quem decide o marketing · Conferir se é do segmento · Conferir se é a mesma loja da parada X · Sem case ainda: visitar só quando o case estiver pronto.

## Informações por comércio

**Planilha, aba "Lojas" (35 colunas, nesta ordem):** Parada · Bloco · Tipo de parada · Grupo: com site / sem site · Segmento · Nome · Bairro · Endereço · Telefone · Alertas · Nota · Avaliações · Ficha sem dono · Situação do site · Site atual · Rede/franquia · Gourmet (só informação) · Melhor posição (só informação) · Faixa de nota · Faixa de avaliações · Km desde a parada anterior · Tipo no Google · Achada pelos termos · Link do Maps · Força no Google (0-100) · Google (faixa) · Cenário · Sinais encontrados · Oferta indicada · Case a levar · **Resultado** (lista: Não falei com quem decide, Sem interesse, Talvez, Interessado, Fechou) · Data da visita · Falou com quem · Objeção · Próximo passo.

**Outras abas:** Rotas no Maps (link de cada bloco) · Resumo do teste (% de "Interessado + Fechou" por total, grupo, segmento, ficha sem dono, faixa de nota, faixa de avaliações, tipo de parada e cenário) · Só mapear (não abordar) · Como ler.

**Cartão da página (celular):** número da parada (cor: azul com site, verde sem site, cinza opcional, roxo visitada; contorno laranja = sem dono) · nome · segmento, bairro, nota e avaliações · com site / sem site (e o que é a página) · telefone · Cenário + oferta · sinais · case a levar · alertas · botões **Mostrar case**, **Ver no Maps**, **Site/Página**, **Ligar**, **No mapa** · lista **Resultado da visita** (marca sozinha) e **Desfazer**.

## Página do mapa

* **Barra fixa:** Com/sem site · Bloco (lembrado no aparelho) · Filtros · "Mostrando X lojas · Y de Z planejadas visitadas".
* **Botão Guia (cabeçalho):** cenários e ofertas, força no Google, cores, alertas, rota e o que fazer depois da visita.
* **Painel Filtros:** Só ficha sem dono · Mostrar opcionais · Esconder visitadas · Copiar visitas · Força no Google (Fraco/Médio/Forte) · Segmentos (vários) · Bairros (vários).
* **Mapa:** fundo embutido (OpenStreetMap), linha tracejada da rota, ponto "Saída", zoom de 13 a 16.
* **Por bloco:** nome dos bairros, planejadas, opcionais, km em linha reta e botão "Abrir rota do bloco no Maps".

## Exceções

| Situação | O que fazer |
|---|---|
| Bairro da lista oficial que hoje é de outra cidade | Tirar da área e registrar o motivo |
| Loja de fora da área que apareceu na busca | Fica fora, salvo endereço na cidade e até 300 m da borda (marcada "(borda)") |
| Mesma marca em duas fichas | A de melhor nota fica normal; a outra recebe "Conferir se é a mesma loja" |
| Rede nacional (ex.: locadora de seminovos) | `fora_do_roteiro` |
| Site que bloqueia robô | Fica sem teste, planejada |
| Saldo da SerpApi acabando | A trava para sozinha; esperar a renovação do mês |

## Métricas

| Métrica | Meta inicial | Como medir |
|---|---|---|
| Buscas por loja na área | Até ~0,5 | Buscas usadas ÷ lojas na planilha |
| Planejadas visitadas | Todas as do bloco do dia | Contador da página / coluna Resultado |
| % Interessado + Fechou | A definir depois das primeiras visitas | Aba "Resumo do teste" |

## Decisões (o que mudou e quando)

Registro para este chat e o outro chat do Claude acompanharem as mudanças um do outro: nenhum deles vê a conversa do outro, só o repositório e o Drive.

**Fonte oficial das regras comerciais** (cenários, Força no Google, regra do case, oferta, cadência, ficha padrão): a pasta `comercial/` (`comercial/posicionamento-digital-base.md` e `comercial/segmentos/comercio-local.md`). Antes de mudar uma regra do mapa: `git pull` e ler esses arquivos. Se o mapa mudar uma regra de lá, avisar o Henrique para atualizar `comercial/` por PR. Enquanto `comercio-local.md` não tiver a regra, vale a desta página.

| Data | Decisão |
|---|---|
| 22/10/2026 | Área de Nova Iguaçu: 16 bairros da URG Centro (sem Juscelino, hoje de Mesquita; com Diana). Pontos a cada 2 km; termos raros em 4 pontos |
| 16/11/2026 | Segmentos novos (hamburgueria, japonês, italiano, distribuidora/adega, barbearia, climatização, celular, tatuagem, beleza); restaurante separado por tipo; clínicas só mapear |
| 16/11/2026 | Cenários A-D, oferta indicada e case a levar; só o Cenário D é opcional |
| 17/11/2026 | Barbearia, celular e beleza entram no roteiro como os demais (landing pages em produção) |
| 17/11/2026 | Nenhuma loja é cortada por nota ou avaliações (fim do corte do lava-jato) |
| 17/11/2026 | Depois da visita: Resultado no mapa + áudio com a checklist no chat do Claude |
| 17/11/2026 | Drive: só a versão mais nova do mapa e da planilha, sem cópias |
| 17/11/2026 | Força no Google (0 a 100); Fraco e Médio contam como Google fraco no cenário |
| 18/11/2026 | Regras comerciais fechadas passam a ter a pasta `comercial/` como fonte oficial (regra de sincronia entre chats) |

## Documentos relacionados

* `prospeccao/programas/prospeccao/LEIA-ME.txt` (passo a passo técnico) e `config_exemplo.json`.
* `comercial/posicionamento-digital-base.md` e `comercial/segmentos/`.
* Drive: pauta de alinhamento de 16/11 (checklist de feedback) e Índice de landing pages de demonstração.
