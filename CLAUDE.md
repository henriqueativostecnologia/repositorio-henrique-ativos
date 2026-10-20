# Prospecção ATIVOS: instruções para o Claude

* Quem: Henrique, da ATIVOS Tecnologia. Contador, aprendendo IA. Explique de forma simples, mostre o porquê de cada passo, sem jargão. Vá um passo por vez: mostre o passo, espere eu executar e só depois siga.
* Objetivo: mapear comércios locais e montar roteiros de visita para vender landing page e posicionamento digital (Google, Instagram, WhatsApp).
* Decisões: em tabela no chat, com recomendação por item.
* SerpApi: chamar pelo servidor MCP `mcp.serpapi.com/mcp`. A chave é colocada pela rede do ambiente; nunca peça a chave no chat. Antes de qualquer busca, mostre a estimativa e espere minha aprovação. Um termo por busca. Use o campo `unclaimed_listing` (ficha sem dono).
* Cada busca começa pelas definições: Etapa 1 (amostra), Etapa 2 (busca completa) e Critérios. Pergunte as três; nada vem pré-definido.
* Dados reais (planilhas e respostas da SerpApi com nomes, telefones e endereços) não entram no repositório: são entregues como arquivo para eu baixar.
* Programas (sem dados) ficam em `programas/` e podem ser melhorados e salvos aqui.
