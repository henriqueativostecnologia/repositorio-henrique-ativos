---
tipo: referência
criado: 04/11/2026
---

# Plataformas usadas pela ATIVOS

Uma pasta por plataforma (Notion, Slack, Chatwoot etc.), com a documentação oficial e um resumo do que importa para a ATIVOS.

## Como funciona

1. Antes de começarmos a usar uma plataforma nova, o Claude pede ao Henrique a **documentação oficial**.
2. O Henrique baixa a documentação no site oficial e envia no chat.
3. O Claude guarda o material na pasta da plataforma e escreve o `resumo.md`, por PR.
4. Os chats futuros leem o `resumo.md` antes de trabalhar com a plataforma. A documentação original só é consultada quando o resumo não basta.

## Estrutura de cada pasta

```
plataformas/
  notion/
    resumo.md     ← o que é, o que a ATIVOS usa, recursos úteis, limites, ideias
    oficial/      ← documentação oficial como veio (PDF, Markdown ou texto)
```

## Modelo do resumo.md

* **O que é** e para que a ATIVOS usa
* **Onde é acessada** (app, site, conector do Claude, skill)
* **Recursos úteis para a ATIVOS**, inclusive os que ainda não usamos
* **Limites e cuidados** (plano, custos, permissões)
* **Ideias de uso**
* **Fonte**: link da documentação oficial e data do download

## Regras

* Nada de senhas, chaves de acesso ou dados de clientes nesta pasta.
* Documentação muito grande: guardar só as partes que usamos, e anotar no resumo o link do restante.

## Plataformas registradas

| Plataforma | Pasta | Situação |
|---|---|---|
| Notion | — | Aguardando documentação |
| Slack | — | Aguardando documentação |
