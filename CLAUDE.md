# Repositório do Henrique (ATIVOS Tecnologia): instruções para o Claude

## Quem e para quê
* Quem: Henrique, da ATIVOS Tecnologia. Contador, com pós em gerenciamento de projetos, aprendendo IA. Explique de forma simples, mostre o porquê de cada passo, sem jargão.
* Papel do Henrique: financeiro e gestão de projetos da ATIVOS (dos clientes e internos). Landing pages são de outro colaborador.
* Este repositório: financeiro, organização e gestão de projetos da ATIVOS e dos seus clientes. A ficha da empresa (sócios, serviços, clientes, ferramentas) está em `empresa/ficha-da-empresa.md`.

## Como trabalhar comigo
* Um passo por vez: mostre o passo, espere eu executar e só depois siga.
* Decisões: em tabela no chat, com recomendação por item.
* Toda mudança no repositório vai por pull request. Só junte ao `main` quando eu disser "aprovado".
* Antes de mexer em qualquer coisa, atualize o branch a partir do `main`.

## Dados
* Dados reais de clientes (propostas, valores, contatos) ficam no Google Drive da ATIVOS, nunca no GitHub.
* Dados reais da prospecção (planilhas e respostas da SerpApi com nomes, telefones e endereços) também não entram no repositório: são entregues como arquivo para eu baixar.
* Programas (sem dados) ficam em `programas/` e podem ser melhorados e salvos aqui.

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
* A prospecção tem um chat próprio ("Prospecção de comércios locais"). Na reorganização, os programas mudam de pasta, mas o conteúdo deles não é alterado.
* SerpApi: chamar pelo servidor MCP `mcp.serpapi.com/mcp`. A chave é colocada pela rede do ambiente; nunca peça a chave no chat. Antes de qualquer busca, mostre a estimativa e espere minha aprovação. Um termo por busca. Use o campo `unclaimed_listing` (ficha sem dono).
* Cada busca começa pelas definições: Etapa 1 (amostra), Etapa 2 (busca completa) e Critérios. Pergunte as três; nada vem pré-definido.
