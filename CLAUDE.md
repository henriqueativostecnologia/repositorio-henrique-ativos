# CLAUDE.md: regras para todos os chats deste repositório

Este arquivo é lido no início de cada chat. Aqui fica só o essencial; o detalhe fica em outro arquivo (do repositório ou do Google Drive), com uma linha aqui dizendo onde está e quando consultar.

## Quem sou e o que é a ATIVOS

* **Henrique**: contador, pós-graduado em gerenciamento de projetos. Responsável pelo **financeiro** e pelo **gerenciamento de projetos** da ATIVOS.
* **ATIVOS Tecnologia**: empresa em início de operação, com 3 linhas de serviço: **posicionamento digital**, **marketing digital** e **automação comercial**.
* **Projetos**: projetos para clientes (começamos com 2) e projetos internos da própria ATIVOS. Os dois tipos são gerenciados aqui.
* **Esta conta**: conta Claude do e-mail institucional do Henrique na ATIVOS. Cada sócio tem o seu e-mail corporativo, a sua conta Claude Pro e o seu repositório no GitHub.
* **Este repositório**: a parte financeira, organizacional e de gerenciamento de projetos da ATIVOS e dos projetos dela.

## Como trabalhar comigo

* Explique de forma simples e mostre **o porquê** de cada passo.
* **Um passo por vez**: mostre o passo, espere eu executar e só então siga.
* **Um tema por vez** quando houver uma lista de assuntos.
* **Decisões em tabela**, com uma recomendação por item.

## Mudanças no repositório (o "cofre")

* Toda mudança entra por **pull request (PR)**. Nada direto no `main`.
* Só junte o PR ao `main` quando eu escrever **"aprovado"**.
* Cada PR vem **resumido no chat**: um texto curto e uma tabela "o que muda / por quê", para eu aprovar sem abrir o GitHub.

## Dados

* **Nunca** coloque dados reais no repositório: valores, senhas, dados de clientes. O repositório guarda métodos, regras e modelos.
* Documentos e arquivos reais ficam no **Google Drive da ATIVOS** (já conectado).
* Quando eu anexar um arquivo, **pergunte onde guardar**:
  1. no repositório (métodos, regras e modelos, sem dados reais);
  2. no Google Drive da ATIVOS (documentos e arquivos reais);
  3. só usar agora, sem guardar.

## Histórico e pastas

* Em 29/10/2026 o repositório foi zerado de propósito. **Não consulte o histórico do git anterior a essa data**; parta só dos arquivos atuais e do que eu disser.
* `prospeccao/`: programas de busca, com chat próprio. **Não mexa nesta pasta** neste chat.
* `referencias/Checklist - Avaliar skill de fora.md`: usar sempre que for avaliar uma skill ou um plugin de fora do catálogo oficial.

## Plataformas (Notion, Slack e outras)

* **Sempre, sem exceção:** antes de começarmos a usar qualquer plataforma, app ou sistema novo, **solicite ao Henrique a documentação oficial**. Não comece a trabalhar com a plataforma sem pedir. Ele baixa e envia; você guarda em `plataformas/<nome>/` e escreve o `resumo.md`, por PR.
* Antes de trabalhar com uma plataforma, leia o `plataformas/<nome>/resumo.md`. Como funciona: `plataformas/README.md`.

## Skills e plugins

* Procure primeiro no **catálogo oficial**. Se faltar, procure em repositórios do GitHub e passe cada candidata pelo checklist de `referencias/`.
* Apresente as opções em tabela (✅ instalar / ⏸️ adiar / ❌ descartar), um tema por vez.
* **Depois de cada instalação**, explique no chat o que é cada skill, para que serve e quando usar, e registre isso em `referencias/skills-instaladas.md` (por PR).
* Sempre que usar uma skill, diga qual no início da resposta ("Usando: nome-da-skill").
* **Qual skill usar:** consulte `referencias/skills-instaladas.md` (tabela "Qual usar") quando um pedido servir para mais de uma skill.
