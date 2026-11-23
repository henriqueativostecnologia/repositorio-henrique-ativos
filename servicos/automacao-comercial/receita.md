---
tipo: receita de serviço
servico: Automação comercial (SDR de IA no WhatsApp e infraestrutura)
versao: v0 de 23/11/2026 (base: CLI-004 Guto Bebidas)
prazo: 15 dias (D1 a D15)
dono: Hugo (SDR); Bernardo (infraestrutura)
---

# Receita · Automação comercial

O SDR de IA atende no receptivo do WhatsApp como recepcionista e balconista: recebe, faz a triagem, mostra o cardápio, passa valores, leva ao fechamento e entrega ao humano. Decisão de 23/11/2026: **cardápio no WhatsApp com o Hugo; banco de dados do cardápio com o Bernardo**.

Por que há tarefas da Meta aqui: pela [política do WhatsApp Business](https://whatsappbusiness.com/policy/), uma mensagem que a empresa inicia fora da janela de 24 horas precisa de **modelo de mensagem aprovado**, e o cliente final precisa ter dado **permissão (opt-in)** ([guia da Meta](https://developers.facebook.com/documentation/business-messaging/whatsapp/getting-opt-in)). O follow-up do SDR depende disso.

## Tarefas

| ID | Tarefa | Responsável | Dia | Depende de | Pronto quando |
|---|---|---|---|---|---|
| AU-01 | Definir o número do SDR (novo ou migrar o atual; número usado no app comum precisa ser migrado) | Hugo, com o cliente | D1 | IN-06 | Número definido |
| AU-02 | Conta na plataforma do WhatsApp Business: verificação do negócio na Meta e nome de exibição aprovado | Bernardo | D1 a D5 (a Meta controla) | AU-01, documentos (IN-08) | Negócio verificado e nome aprovado |
| AU-03 | Servidor (VPS) do projeto | Bernardo | D2 a D3 | — | Servidor no ar |
| AU-04 | Roteiro do atendimento: receptivo, triagem, demonstração, valores e fechamento, entrega ao humano; tom de voz; regra fora do horário | Hugo | D2 a D4 | IN-06 | Roteiro aprovado pelo cliente |
| AU-05 | Banco de dados do cardápio (produtos, preços, fotos) | Bernardo | D3 a D5 | cardápio (IN-08) | Banco consultável pelo SDR |
| AU-06 | Cardápio no WhatsApp Business (catálogo) | Hugo | D3 a D5 | cardápio (IN-08) | Catálogo publicado |
| AU-07 | Prompt e base de conhecimento: perguntas frequentes, área e taxa de entrega, formas de pagamento, horário | Hugo | D4 a D7 | AU-04 | Base escrita |
| AU-08 | Regra de passagem para humano: quem recebe, em qual canal, em quanto tempo responde | Hugo, com o cliente | D5 | AU-04 | Regra combinada por escrito |
| AU-09 | Modelos de mensagem para o follow-up e para fora da janela de 24 horas; enviar para aprovação | Hugo | D6 a D8 (a Meta aprova) | AU-02 | Modelos aprovados |
| AU-10 | Permissão (opt-in): como e onde o cliente final aceita receber mensagens | Hugo | D6 | AU-04 | Texto de opt-in no fluxo |
| AU-11 | CRM de atendimento (Chatwoot): caixa de entrada, usuários do cliente, etiquetas (lead, passou para humano, comprou) | Bernardo | D6 a D8 | AU-03 | Cliente acessa e vê as conversas |
| AU-12 | Deploy do SDR no servidor | Bernardo | D8 a D9 | AU-03, AU-05, AU-07, AU-11 | SDR respondendo no número de teste |
| AU-13 | Testes internos: pedido completo, cliente que some (follow-up), fora do horário, produto inexistente, preço, passagem para humano | Hugo | D9 a D11 | AU-12 | Roteiro de testes sem falha |
| AU-14 | Rastreio do WhatsApp: origem do lead (anúncio) e marcação de compra | Bernardo, com o Igor (RA-06) | D10 a D12 | AU-11 | Lead de teste com origem e compra |
| AU-15 | Teste com o cliente e ajustes | Hugo | D12 a D13 | AU-13 | Cliente aprovou por escrito |
| AU-16 | Ligar no número real e acompanhar de perto por 48 horas | Hugo | D14 a D15 | AU-15, AU-02 | 48 horas sem falha grave |
| AU-17 | Treinar a equipe do cliente: atender quem o SDR passou, marcar a compra no CRM | Hugo | D15 | AU-16 | Treino feito (FI-04) |

## Fontes

* Documentação do CLI-004 Guto Bebidas: `servicos/referencias/cli-004-guto-documentacao-servicos-v0.md`.
* WhatsApp: [política comercial](https://whatsappbusiness.com/policy/) e [opt-in](https://developers.facebook.com/documentation/business-messaging/whatsapp/getting-opt-in).
