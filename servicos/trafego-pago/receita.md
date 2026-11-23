---
tipo: receita de serviço
servico: Tráfego pago, setup (Meta Ads e Google Ads, com o bloco de rastreio)
versao: v0 de 23/11/2026 (base: CLI-004 Guto Bebidas)
prazo: 7 dias (D1 a D7)
dono: Igor
---

# Receita · Tráfego pago (setup)

Decisão de 23/11/2026: **um bloco de rastreio só**, feito uma vez e usado pelo Meta e pelo Google. O objetivo mais comum em negócio local é atrair interessados no WhatsApp.

Divergência registrada: o `catalogo.md` (04/11) põe o Hugo nos anúncios; a venda do CLI-004 Guto Bebidas pôs o **Igor**. Esta receita segue a venda.

## Meta Ads

| ID | Tarefa | Responsável | Dia | Depende de | Pronto quando |
|---|---|---|---|---|---|
| MT-01 | Página do Facebook: criar ou ajustar (endereço, descrição, básico) e vincular ao Instagram | Igor | D1 | acessos (IN-08) | Página ligada ao Instagram |
| MT-02 | Business Manager: conta de anúncio do cliente ligada à nossa BM, Facebook, Instagram e WhatsApp integrados | Igor | D1 a D2 | MT-01 | Acessos conferidos |
| MT-03 | Forma de pagamento da conta de anúncio (o cliente cadastra) | Cliente (Igor cobra) | D2 | MT-02 | Pagamento ativo |
| MT-04 | Verificar o domínio do site na BM | Igor | D6 | LP-09 | Domínio verificado |
| MT-05 | Benchmark: Biblioteca de Anúncios, Google, sites bem posicionados e perfis no Google dos concorrentes (títulos, textos, vídeo, foto, carrossel, estrutura do site) | Igor | D1 a D2 | — | Quadro de referências |
| MT-06 | Estratégia e públicos: público, localização, orçamento aprovado pelo cliente, públicos criados | Igor | D2 a D3 | MT-05, orçamento (IN-08) | Estratégia escrita e aprovada |
| MT-07 | Briefing dos criativos a partir do benchmark | Igor | D3 | MT-06 | Briefing entregue |
| MT-08 | Produzir criativos: pelo menos 3 vídeos, 3 fotos e 3 carrosséis (não precisa de todos de uma vez) | Design e videomaker (gestão do Igor) | D3 a D5 | MT-07, fotos (IN-08) | Criativos na pasta Tráfego |
| MT-09 | Aprovação dos criativos pelo cliente | Igor | D6 | MT-08 | Aprovação por escrito |
| MT-10 | Subir as campanhas (objetivo: mensagens ou leads) | Igor | D7 | MT-09, RA-03 | Campanhas no ar |
| MT-11 | Remarketing: quem engajou no Instagram e quem visitou o site (liga quando houver público suficiente) | Igor | D7 | MT-10 | Públicos criados |

## Google Ads

| ID | Tarefa | Responsável | Dia | Depende de | Pronto quando |
|---|---|---|---|---|---|
| GA-01 | Análise de concorrentes: títulos e descrições usados | Igor | D1 a D2 | — | Quadro de referências |
| GA-02 | Pesquisa de palavras-chave: volume, abrangência, variações; cauda longa ou só fundo de funil | Igor (usa o estudo de palavras do Henrique) | D2 | GA-01 | Lista com volume |
| GA-03 | Termos e correspondência (ampla, de frase, exata) e lista de **palavras negativas** | Igor | D3 | GA-02 | Grupos de anúncio montados |
| GA-04 | Faturamento da conta (o cliente cadastra) | Cliente (Igor cobra) | D2 | acessos (IN-08) | Pagamento ativo |
| GA-05 | Configurar a campanha: só rede de pesquisa, local e raio, horário de funcionamento, orçamento diário | Igor | D4 | GA-03 | Campanha em rascunho |
| GA-06 | Anúncios: 2 a 3 anúncios responsivos por grupo | Igor (copy com apoio do Hugo) | D4 | GA-05 | Anúncios com qualidade "boa" ou melhor |
| GA-07 | Recursos: sitelinks, frases de destaque, ligação, mensagem/WhatsApp, logo, imagens, local (vincular o perfil do Google, quando verificado) | Igor | D5 | GA-05, fotos (IN-08) | Recursos aprovados |
| GA-08 | Publicar a campanha | Igor | D7 | GA-06, GA-07, RA-04 | Campanha no ar |

## Bloco de rastreio (usado pelo Meta e pelo Google)

| ID | Tarefa | Responsável | Dia | Depende de | Pronto quando |
|---|---|---|---|---|---|
| RA-01 | Plano de medição: o que conta como conversão (clique no WhatsApp, formulário, ligação, compra) | Igor | D2 | IN-06 | Lista de conversões escrita |
| RA-02 | GTM e Google Analytics no site | Igor define, Bernardo instala | D6 | LP-09, RA-01 | Eventos aparecem no Analytics |
| RA-03 | Pixel da Meta **com a API de Conversões** | Igor | D6 | RA-02, MT-04 | Eventos no Gerenciador de Eventos |
| RA-04 | Tag e conversões do Google Ads | Igor | D6 | RA-02 | Conversões com status "ativo" |
| RA-05 | Padrão de UTMs em todos os links (anúncios, botão, perfil do Google) | Igor | D6 | RA-01 | Planilha de UTMs |
| RA-06 | Rastreio do WhatsApp: de qual anúncio veio cada lead e qual comprou | Igor, com a Automação (AU-14) | junto com a Automação (até D15) | AU-11 | Lead de teste marcado com origem e compra |
| RA-07 | Teste de ponta a ponta: lead de teste aparece em cada ferramenta | Igor | D7 | RA-02 a RA-05 | Print de cada ferramenta na pasta Dados |

## Fontes

* Documentação do CLI-004 Guto Bebidas: `servicos/referencias/cli-004-guto-documentacao-servicos-v0.md`.
* Meta: [API de Conversões junto com o pixel](https://www.facebook.com/business/help/952192354843755).
* Google Ads: [boas práticas de campanha de pesquisa](https://support.google.com/google-ads/answer/7507883).
