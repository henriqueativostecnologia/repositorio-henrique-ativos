# Repositório do Henrique (ATIVOS Tecnologia): instruções para o Claude

## Quem e para quê
* Quem: Henrique, da ATIVOS Tecnologia. Contador, com pós em gerenciamento de projetos, aprendendo IA. Explique de forma simples, mostre o porquê de cada passo, sem jargão.
* Papel do Henrique: financeiro e gestão de projetos da ATIVOS (dos clientes e internos). Landing pages são de outro colaborador.
* Este repositório: financeiro, organização e gestão de projetos da ATIVOS e dos seus clientes.

## Pastas
* `empresa/`: ficha da empresa (sócios, serviços, clientes, ferramentas).
* `gestao-de-projetos/`: a sistemática de gestão de projetos (base da skill pmo-ativos) e, depois, os modelos.
* `financeiro/`: métodos e modelos do financeiro, sem valores reais.
* `prospeccao/`: programas de busca e de roteiro de visitas. Rodar de dentro de `prospeccao/`, com `dados/` ao lado.
* `referencias/`: checklist para avaliar skills de fora, lista de skills a instalar e registro dos plugins instalados.

## Como trabalhar comigo
* Um passo por vez: mostre o passo, espere eu executar e só depois siga.
* Decisões: em tabela no chat, com recomendação por item.
* Toda mudança no repositório vai por pull request. Só junte ao `main` quando eu disser "aprovado".
* Antes de mexer em qualquer coisa, atualize o branch a partir do `main`.

## Dados
* Dados reais de clientes (propostas, valores, contatos) ficam no Google Drive da ATIVOS, nunca no GitHub.
* Dados reais da prospecção (planilhas e respostas da SerpApi com nomes, telefones e endereços) também não entram no repositório: são entregues como arquivo para eu baixar.
* Programas (sem dados) ficam em `prospeccao/programas/` e podem ser melhorados e salvos aqui.

## Skills e plugins
* Em finanças e gestão de projetos, chame as skills de método pelo nome (por exemplo `financial-statements`, `variance-analysis`, `status-report`, `change-request`). Usar só as skills de formato (planilha, documento) dá uma análise rasa.
* Quando houver necessidade, podemos usar skills e plugins de fora, inclusive de repositórios de terceiros no GitHub. Proponha só quando um oficial não resolver bem.
* Plugin novo ou skill de fora: avaliar antes com `referencias/Checklist - Avaliar skill de fora.md` e, depois de instalar, registrar em `referencias/plugins-instalados.md`.

## Foco atual
* Gestão de projetos primeiro: criar as pastas da ATIVOS no Google Drive e iniciar a sistemática organizacional (como organizar projetos, tarefas internas e externas e documentos). O financeiro também é urgente e vem logo depois.

## Ordem de trabalho
1. Ficha da empresa + este `CLAUDE.md`.
2. Estrutura do repositório: pastas para financeiro, gestão de projetos, prospecção e referências.
3. Organização do Google Drive (pastas de clientes e projetos), do zero.
4. Notion (plano e tabelas, conforme a sistemática) e Slack (canais por cliente).
5. Skill pmo-ativos v1, abrindo os projetos do Dr. Felipe e do Lucas.
6. Financeiro da ATIVOS, com o método que o Henrique vai trazer da conta pessoal.

## Prospecção
* Situação: ainda não foi feita. Existem buscas e roteiros de visita prontos (BH e Nova Iguaçu); nenhuma visita aconteceu.
* Objetivo: mapear comércios locais e montar roteiros de visita para vender os serviços da ATIVOS (Google, Instagram, WhatsApp).
* A prospecção tem um chat próprio ("Prospecção de comércios locais"). Os programas estão em `prospeccao/programas/` (movidos em 29/10/2026 sem alteração no conteúdo).
* SerpApi: chamar pelo servidor MCP `mcp.serpapi.com/mcp`. A chave é colocada pela rede do ambiente; nunca peça a chave no chat. Antes de qualquer busca, mostre a estimativa e espere minha aprovação. Um termo por busca. Use o campo `unclaimed_listing` (ficha sem dono).
* Cada busca começa pelas definições: Etapa 1 (amostra), Etapa 2 (busca completa) e Critérios. Pergunte as três; nada vem pré-definido.
