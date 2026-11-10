---
tipo: referência
criado: 04/11/2026
atualizado: 10/11/2026
---

# Plataformas usadas pela ATIVOS

Uma pasta por plataforma (Notion, Slack etc.), com a **documentação oficial completa**. Sem resumo: a fonte é sempre o texto oficial.

## Como funciona

1. Antes de começarmos a usar uma plataforma nova, o Claude garante a documentação oficial completa.
2. **Documentação pública:** o próprio Claude baixa do site oficial, artigo por artigo, e converte em texto. Se o site estiver bloqueado na rede do ambiente, o Henrique libera o domínio (menu do ambiente › Editar › Acesso à rede).
3. **Documentação com login ou material pago:** o Henrique envia.
4. O Claude guarda tudo em `plataformas/<nome>/oficial/`, com um `README.md` de índice (título, link e data de cada artigo), por PR.
5. Nos chats seguintes, o Claude **busca dentro** dos arquivos o trecho necessário; não lê tudo a cada vez.

## Estrutura de cada pasta

```
plataformas/
  notion/
    oficial/
      README.md   ← índice: título, link de origem e data de cada artigo
      central/    ← artigos da Central de Ajuda (um arquivo por artigo)
      guias/      ← guias oficiais
```

## Regras

* Nada de senhas, chaves de acesso ou dados de clientes nesta pasta.
* Cada arquivo traz no topo o link de origem e a data do download.
* Para atualizar, o Claude baixa de novo e substitui (o histórico fica no git).

## Plataformas registradas

| Plataforma | Pasta | Situação |
|---|---|---|
| Notion | `notion/oficial/` | ✅ Completa: 279 artigos da Central de Ajuda + 204 guias (10/11/2026) |
| AppSheet | `appsheet/oficial/` | ✅ Completa: 659 artigos (10/11/2026) |
| Google Chat | `google-chat/oficial/` | ✅ Completa: 119 artigos (10/11/2026) |
| Google Sheets | `google-sheets/oficial/` | ✅ Completa: 599 artigos, incluindo a lista de funções (10/11/2026) |
| Google Docs | `google-docs/oficial/` | ✅ Completa: 126 artigos (10/11/2026) |
| Google Drive | `google-drive/oficial/` | ✅ Completa: 124 artigos (10/11/2026) |
| Google Agenda | `google-agenda/oficial/` | ✅ Completa: 112 artigos (10/11/2026) |
| Google Sites | `google-sites/oficial/` | ✅ Completa: 23 artigos (10/11/2026) |
| Asana | `asana/oficial/` | ✅ Completa: 546 artigos da Central de Ajuda (10/11/2026) |
| Slack | — | Opção futura (decisão de 10/11/2026: conversas no Google Chat) |
