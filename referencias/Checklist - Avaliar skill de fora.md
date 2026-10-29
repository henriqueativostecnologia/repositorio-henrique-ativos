---
tipo: referência
origem: cofre pessoal do Henrique (29/10/2026), adaptado para a ATIVOS
---

# Checklist: avaliar uma skill ou um plugin de fora do catálogo

Usado sempre que alguém da ATIVOS pedir "procura uma skill (ou um plugin) de X". O Claude busca na web (Diretório do Claude, skills.sh, GitHub) e passa **cada candidata** por esta lista antes de recomendar. O resultado vai para o chat como tabela de decisão (✅ instalar / ⏸️ adiar / ❌ descartar).

| # | Pergunta | Sinal bom | Sinal de alerta |
|---|---|---|---|
| 1 | **Quem fez?** | Fonte oficial (Anthropic, Vercel, Microsoft) ou autor conhecido | Autor desconhecido, sem outros projetos |
| 2 | **Quantos usam?** | 1.000+ instalações no skills.sh ou 100+ estrelas no GitHub | Menos de 100 instalações ou estrelas: tratar como "pouco testada" |
| 3 | **Está viva?** | Atualizada nos últimos meses, mais de uma versão | Uma versão só, ou parada há mais de um ano |
| 4 | **Licença** | Livre (MIT, Apache) | Restrita ou ausente |
| 5 | **Custo** | Grátis, ou custo conhecido e aprovado pela ATIVOS | Exige serviço ou conector pago que ninguém aprovou |
| 6 | **O que faz por dentro** | O Claude leu o SKILL.md e os arquivos de apoio | Scripts que o Claude não leu, ou que baixam coisas da internet |
| 7 | **Age sozinha?** | Só prepara; você aprova | Envia e-mail, publica, paga ou altera dados sem perguntar |
| 8 | **Dados** | Trabalha com o que você envia | Pede senha, ou manda dados para serviço de terceiros |
| 9 | **Sobreposição** | Faz algo que nenhuma skill instalada faz | Repete uma instalada (disputa o mesmo pedido) |
| 10 | **Funciona no app?** | Instalável como .zip, sem depender de terminal | Depende de terminal, Node.js ou programa local |
| 11 | **Padrão brasileiro** | Neutra ou adaptável | Regras só dos EUA (impostos, folha, leis) |

**Só para plugins** (um plugin é um pacote: pode trazer skills, conectores, comandos e automações, por isso tem mais poder do que uma skill):
| # | Pergunta | Sinal bom | Sinal de alerta |
|---|---|---|---|
| 12 | **Quantas skills traz?** | Poucas, todas úteis | Muitas repetindo as instaladas: instalar só as úteis, como .zip |
| 13 | **Liga conectores?** (arquivo `.mcp.json`) | Nenhum, ou só os que você já usa | Conectores para serviços pagos ou que você não usa |
| 14 | **Tem automações?** (hooks, tarefas agendadas) | Nenhuma, ou só com aprovação | Roda sozinho em horários ou a cada ação, sem perguntar |
| 15 | **Muda sozinho?** | Versão fixa | Atualiza automaticamente pela loja (preferir .zip avulso para controlar) |

**Como decidir:** alerta nos itens 6, 7, 8 ou 14 → não instalar sem o responsável ver o motivo. Alerta só nos itens 2 e 3 → pode instalar para teste, avisando que é pouco testada.
