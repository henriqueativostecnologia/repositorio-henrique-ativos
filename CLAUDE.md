# CLAUDE.md: regras para todos os chats deste repositório

Este arquivo é lido no início de cada chat. Aqui fica só o essencial; o detalhe fica em outro arquivo (do repositório ou do Google Drive), com uma linha aqui dizendo onde está e quando consultar.

## Quem sou e o que é a ATIVOS

* **Henrique**: contador, pós-graduado em gerenciamento de projetos. Responsável pelo **financeiro** e pelo **gerenciamento de projetos** da ATIVOS.
* **Sócios**: Henrique e Igor no **comercial** (vendem todas as linhas), no **financeiro interno** e na **gestão de tarefas**; Hugo e Bernardo no **operacional** (sites, criativos para anúncios, automações, rastreamento, dashboards); Igor é o fundador e arquiteto de dados, e atua no operacional quando o projeto pede. Detalhe em `organizacao/estrutura.md`.
* **ATIVOS Tecnologia**: empresa em estruturação, com 4 serviços avulsos (**Posicionamento Digital**, **Assessoria de Marketing / tráfego pago**, **Automação Comercial**, **Rastreamento de Dados**) e 1 **pacote** (Posicionamento + Assessoria + Automação). Público, escopo e responsáveis em `servicos/catalogo.md`; consulte antes de propostas e projetos.
* **Projetos**: projetos para clientes (3 primeiros: `clientes/indice.md`) e projetos internos da ATIVOS. Os dois tipos são gerenciados aqui.
* **Ferramentas**: Notion (tarefas e projetos), Slack (conversas), Google Drive (arquivos). Sempre que outra ferramenta for melhor para algo, recomende.
* **Conectores Google ativos** (desde 05/11/2026): Drive, Docs e Sheets. Você pode ler e editar direto a planilha de tarefas e os Google Docs do Drive ATIVOS, seguindo a skill google-workspace.
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

* **Nunca** coloque dados reais no repositório: valores, senhas, acessos, contratos e dados de contato ou documentos (CPF, CNPJ) de clientes. O repositório guarda métodos, regras e modelos.
* **Clientes no repositório:** só **código e nome curto**, ex.: `CLI-001 Dr. Felipe (advocacia)`. O resto fica no Drive.
* **Sempre cite o cliente com código e nome** (ex.: "CLI-002 Lucas Melo"), nunca só o número, no chat, na planilha e nos documentos. Projetos de cliente: `CLI-001-PAC Dr. Felipe`.
* Documentos e arquivos reais ficam no **Drive compartilhado "ATIVOS"** (já conectado; pasta raiz: `0AE6MYs89GYdWUk9PVA`, https://drive.google.com/drive/folders/0AE6MYs89GYdWUk9PVA). Onde salvar cada coisa, numeração das pastas e nomes de arquivo: `organizacao/manual-drive.md`. Consulte antes de criar ou salvar algo no Drive.
* Quando eu anexar um arquivo, **pergunte onde guardar**:
  1. no repositório (métodos, regras e modelos, sem dados reais);
  2. no Google Drive da ATIVOS (documentos e arquivos reais);
  3. só usar agora, sem guardar.

## Histórico e pastas

* Em 29/10/2026 o repositório foi zerado de propósito. **Não consulte o histórico do git anterior a essa data**; parta só dos arquivos atuais e do que eu disser.
* `prospeccao/`: programas de busca, com chat próprio. **Não mexa nesta pasta** neste chat.
* `servicos/`: modelos de cada serviço (fases, portões, prazos, responsáveis). Consulte ao planejar ou acompanhar um projeto de cliente. Hoje: `pacote/eap-padrao.md` (EAP e tempos padrão por tarefa, v1 de 09/11) e `infraestrutura-de-dados/fluxo-de-implantacao.md` (rascunho).
* **Tarefas:** a lista oficial é a planilha **Quadro de tarefas ATIVOS** no Drive (`00 Geral › 03 Gestão de tarefas`, id `1g7cFgksYnu7_YpPCewVUtGThya8i46XQOdmxkVNVbl4`), até a migração para o Notion. Consulte no início de cada tema. Modelo de projetos e de tarefas: `gestao/modelo-de-projetos.md`. Regras para qualquer Claude cadastrar ou atualizar tarefas na planilha: `gestao/instrucoes-claude-tarefas.md` (siga sempre). O `gestao/tarefas.md` está aposentado.
* `referencias/Checklist - Avaliar skill de fora.md`: usar sempre que for avaliar uma skill ou um plugin de fora do catálogo oficial.

## Modelo de execução de cada demanda

* Antes de executarmos uma demanda nova, criamos juntos o modelo de execução (POP, checklists, modelos, tarefas padrão), **compilando 3 fontes**: o que a ATIVOS já sabe e decidiu, os cursos e treinamentos que o Henrique enviar e a documentação oficial da plataforma. Cursos comprados ficam só no Drive; no repositório, apenas o que produzirmos a partir deles.

## Plataformas (Notion, Slack e outras)

* **Sempre, sem exceção:** antes de começarmos a usar **aqui** qualquer plataforma, app ou sistema novo (gestão, organização, financeiro, comunicação), garanta a **documentação oficial completa**. Ferramentas só do operacional (GTM, GA4, BigQuery, Chatwoot etc.) ficam fora: o Henrique não opera essas demandas.
* **Documentação pública:** você mesmo busca no site oficial e guarda **completa** em `plataformas/<nome>/oficial/`, com um **índice** (título, link e data de cada artigo), por PR. **Nunca resumo.** Se o site estiver bloqueado na rede do ambiente, peça ao Henrique para liberar o domínio. **Documentação com login ou material pago:** peça ao Henrique para enviar.
* Antes de trabalhar com uma plataforma, **busque dentro** de `plataformas/<nome>/oficial/` (índice no `README.md` da pasta) o trecho necessário. Como funciona: `plataformas/README.md`. Notion: documentação completa baixada em 10/11/2026.

## Skills e plugins

* Procure primeiro no **catálogo oficial**. Se faltar, procure em repositórios do GitHub e passe cada candidata pelo checklist de `referencias/`.
* Apresente as opções em tabela (✅ instalar / ⏸️ adiar / ❌ descartar), um tema por vez.
* **Depois de cada instalação**, explique no chat o que é cada skill, para que serve e quando usar, e registre isso em `referencias/skills-instaladas.md` (por PR).
* **Antes de cada solicitação do Henrique e de cada entrega**, confira na tabela "Qual usar" (`referencias/skills-instaladas.md`) se alguma skill serve. Se servir, **use**: o Henrique quer aproveitar o máximo delas. Se nenhuma servir, não force.
* Toda resposta começa com **"Usando: nome-da-skill"** ou **"Sem skill: motivo"**, para o Henrique ver nos dois casos.
* **Qual skill usar:** consulte `referencias/skills-instaladas.md` (tabela "Qual usar") quando um pedido servir para mais de uma skill.
