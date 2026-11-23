---
tipo: receita de serviço
servico: Landing page (Posicionamento Digital)
versao: v0 de 23/11/2026 (base: CLI-004 Guto Bebidas)
prazo: 7 dias (D1 a D7)
dono: Bernardo
---

# Receita · Landing page

Decisões de 23/11/2026: a **pesquisa de mercado e o wireframe são do Hugo**, com a automação que o Igor está criando; a **copy é do Hugo**; o resto é do Bernardo. O SEO da página (arquitetura, título, descrição, dados estruturados, SEO/AEO/GEO) é do **Henrique**, porque é o mesmo estudo do Google Meu Negócio.

## Tarefas

| ID | Tarefa | Responsável | Dia | Depende de | Pronto quando |
|---|---|---|---|---|---|
| LP-01 | Pesquisa de mercado: 3 a 5 concorrentes, abrir as seções de cada página, achar a seção campeã (copy e design). Sem referência boa no segmento, buscar em outros | Hugo (automação do Igor) | D1 a D2 | — | Quadro de referências por seção |
| LP-02 | Wireframe: esqueleto da página a partir da pesquisa | Hugo (automação do Igor) | D2 | LP-01 | Wireframe aprovado pelo Bernardo |
| LP-03 | Arquitetura de posicionamento: seções e termos que a página precisa ter para o Google e para as buscas de IA | Henrique | D2 | público e palavras-chave (receita do Google Meu Negócio) | Lista de seções e termos entregue ao Hugo |
| LP-04 | Copy da página (modelando a referência campeã), com os termos do LP-03 | Hugo | D2 a D3 | LP-02, LP-03 | Copy revisada |
| LP-05 | Artes e front-end | Bernardo | D3 a D4 | LP-04, fotos e logo (IN-08) | Página em ambiente de teste |
| LP-06 | Motion: efeitos visuais (ferramentas de motion e Higgsfield) só onde dão sofisticação | Bernardo | D5 | LP-05 | Efeitos aplicados sem pesar a página |
| LP-07 | SEO na página: título, descrição, cabeçalhos, texto alternativo das imagens, dados estruturados de negócio local (nome, endereço, telefone e horário iguais aos do Google) | Henrique define, Bernardo aplica | D5 | LP-03, LP-05 | Conferido no teste de resultados aprimorados do Google |
| LP-08 | Política de privacidade e aviso de cookies (LGPD) | Bernardo | D5 | LP-05 | Página publicada e linkada no rodapé |
| LP-09 | Domínio e deploy: o cliente já tem domínio ou site? Apontar a URL, hospedar, publicar, certificado de segurança (HTTPS) | Bernardo | D5 a D6 | domínio (IN-08) | Site no domínio do cliente, com cadeado |
| LP-10 | Botão: destino (WhatsApp ou cardápio digital), mensagem pronta e UTM | Bernardo | D6 | LP-09, número do SDR (automação) | Botão testado no celular |
| LP-11 | Teste no celular: abre bem, velocidade (PageSpeed no celular 50 ou mais, meta 70), sem erro | Bernardo | D6 | LP-09 | Print do PageSpeed na pasta Site |
| LP-12 | Instalar o rastreio do site (GTM, Analytics, pixel, tag do Google) | Bernardo instala, Igor confere | D6 | bloco de rastreio (receita de tráfego, RA-02) | Igor confirmou os eventos |
| LP-13 | Cadastrar o site no Google Search Console e enviar o sitemap | Henrique | D6 | LP-09 | Propriedade verificada, sitemap enviado |
| LP-14 | Revisão interna e aprovação do cliente | Henrique (FI-01), Bernardo apresenta (FI-02) | D7 | LP-06 a LP-13 | Aceite por escrito (FI-03) |
| LP-15 | Uma rodada de ajustes pedidos pelo cliente | Bernardo | até D7+2 | LP-14 | Ajustes publicados |

## Checklist da entrega (usado no FI-01)

* Abre bem no celular e no computador; HTTPS ativo; PageSpeed no celular 50 ou mais. (Abaixo de 50, o próprio mapa de prospecção da ATIVOS classificaria o site como "com falha", Cenário B.)
* Nome, endereço, telefone e horário iguais aos do perfil no Google.
* Botão leva ao destino certo, com UTM.
* Política de privacidade no rodapé.
* Rastreio conferido pelo Igor; site no Search Console.

## Fontes

* Documentação do CLI-004 Guto Bebidas: `servicos/referencias/cli-004-guto-documentacao-servicos-v0.md`.
* Google: [dados estruturados de negócio local](https://developers.google.com/search/docs/appearance/structured-data/local-business) e [Search Console](https://support.google.com/webmasters/answer/9128668).
