#!/usr/bin/env bash
# Lembrete automático (UserPromptSubmit): a cada mensagem do Henrique, mostra ao Claude
# a regra de skills e a tabela "Qual usar" de referencias/skills-instaladas.md.
dir="${CLAUDE_PROJECT_DIR:-$(pwd)}"
arq="$dir/referencias/skills-instaladas.md"
echo "LEMBRETE (regra do CLAUDE.md): antes de responder, confira a tabela abaixo. Se alguma skill servir para este pedido, USE (chame a skill). Comece a resposta com \"Usando: nome-da-skill\" ou \"Sem skill: motivo\"."
if [ -f "$arq" ]; then
  sed -n '/^## Qual usar/,/^## /p' "$arq" | sed '$!b;/^## /d'
fi

# Coordenação entre os chats (gestao/coordenacao-chats.md): mostra os avisos "novo" do Mural,
# lidos do main no GitHub (assim os dois chats veem o mesmo mural, mesmo com branches diferentes).
timeout 4 git -C "$dir" fetch -q origin main 2>/dev/null
mural=$(git -C "$dir" show origin/main:gestao/coordenacao-chats.md 2>/dev/null || cat "$dir/gestao/coordenacao-chats.md" 2>/dev/null)
novos=$(printf '%s\n' "$mural" | grep -E '\| *novo *\|$')
if [ -n "$novos" ]; then
  echo ""
  echo "MURAL DOS CHATS (gestao/coordenacao-chats.md, versão do main): avisos ainda não aplicados. Veja os que são \"Para\" este chat e aplique; ao aplicar, marque como aplicado (data) no mesmo PR."
  echo "| Data | De | Para | Aviso | Onde | Situação |"
  printf '%s\n' "$novos"
fi
