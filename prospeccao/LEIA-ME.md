# Prospecção

Programas de busca de comércios locais (SerpApi) e de roteiro de visitas. Situação: a prospecção ainda não foi feita. Existem buscas e roteiros prontos (BH e Nova Iguaçu); nenhuma visita aconteceu.

- `programas/prospeccao/`: versão atual (do mapa da área ao roteiro de visitas). Leia o `LEIA-ME.txt` de lá.
- `programas/busca/` e `programas/roteiro/`: versões antigas, como referência da prospecção de BH.

**Onde rodar:** de dentro desta pasta (`prospeccao/`), com a pasta `dados/` ao lado de `programas/`. Assim os comandos do `LEIA-ME.txt` funcionam como estão escritos (por exemplo, `python3 programas/prospeccao/1_grade.py dados/config.json ...`). A pasta `dados/` nunca entra no repositório (o `.gitignore` bloqueia).

Os programas foram movidos para cá em 29/10/2026 sem nenhuma alteração.

## Regras da prospecção (copiadas do CLAUDE.md em 29/10/2026)

* Situação: ainda não foi feita. Existem buscas e roteiros de visita prontos (BH e Nova Iguaçu); nenhuma visita aconteceu.
* Objetivo: mapear comércios locais e montar roteiros de visita para vender os serviços da ATIVOS (Google, Instagram, WhatsApp).
* A prospecção tem um chat próprio ("Prospecção de comércios locais"). Os programas estão em `prospeccao/programas/` (movidos em 29/10/2026 sem alteração no conteúdo).
* SerpApi: chamar pelo servidor MCP `mcp.serpapi.com/mcp`. A chave é colocada pela rede do ambiente; nunca peça a chave no chat. Antes de qualquer busca, mostre a estimativa e espere minha aprovação. Um termo por busca. Use o campo `unclaimed_listing` (ficha sem dono).
* Cada busca começa pelas definições: Etapa 1 (amostra), Etapa 2 (busca completa) e Critérios. Pergunte as três; nada vem pré-definido.

Também do CLAUDE.md (seção Dados), por serem da prospecção:
* Dados reais da prospecção (planilhas e respostas da SerpApi com nomes, telefones e endereços) também não entram no repositório: são entregues como arquivo para eu baixar.
* Programas (sem dados) ficam em `prospeccao/programas/` e podem ser melhorados e salvos aqui.
