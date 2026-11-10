#!/usr/bin/env bash
# Lembrete automático (UserPromptSubmit): a cada mensagem do Henrique, mostra ao Claude
# a regra de skills e a tabela "Qual usar" de referencias/skills-instaladas.md.
dir="${CLAUDE_PROJECT_DIR:-$(pwd)}"
arq="$dir/referencias/skills-instaladas.md"
echo "LEMBRETE (regra do CLAUDE.md): antes de responder, confira a tabela abaixo. Se alguma skill servir para este pedido, USE (chame a skill). Comece a resposta com \"Usando: nome-da-skill\" ou \"Sem skill: motivo\"."
if [ -f "$arq" ]; then
  sed -n '/^## Qual usar/,/^## /p' "$arq" | sed '$!b;/^## /d'
fi
