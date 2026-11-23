---
tipo: receita de serviço
servico: Início e fim (vale para todo cliente, qualquer serviço)
versao: v0 de 23/11/2026 (base: CLI-004 Guto Bebidas)
dono: Henrique
---

# Receita · Início e fim

Por que existe: sem os acessos e os materiais do cliente, quase todas as outras receitas travam no D1. E sem aceite por escrito, a entrega não tem fim.

## Início

| ID | Tarefa | Responsável | Dia | Depende de | Pronto quando |
|---|---|---|---|---|---|
| IN-01 | Contrato assinado e cobrança do setup emitida | Henrique | D0 | — | Contrato em 01 Contrato e cadastro; cobrança enviada |
| IN-02 | Abrir o cliente: próximo código livre, pasta no Drive (estrutura do CLI-000 Modelo), linha em `clientes/indice.md`, projeto na central | Henrique | D0 | IN-01 | Código, pasta e projeto criados |
| IN-03 | Criar as tarefas das receitas compradas na central, com as datas reais | Henrique | D0 | IN-02 | Todas as tarefas na central, com dono e prazo |
| IN-04 | Criar o grupo de WhatsApp com o cliente e os sócios do projeto | Henrique | D0 | — | Grupo criado e mensagem de boas-vindas enviada |
| IN-05 | Enviar a lista de acessos e materiais (abaixo) | Henrique | D0 | IN-04 | Lista enviada no grupo |
| IN-06 | Reunião de início com o cliente (ver pauta abaixo) | Henrique (conduz) e Igor | D1 | IN-04 | Ata em 05 Reuniões e atas |
| IN-07 | Kickoff interno: cada dono confere as próprias tarefas e dependências | Henrique | D1 | IN-03 | Cada dono confirmou as tarefas |
| IN-08 | Receber e conferir acessos e materiais; cobrar o que faltar | Henrique (cliente envia) | D1 a D3 | IN-05 | Lista completa; acessos no gerenciador de senhas, nunca no Drive |

### Lista de acessos e materiais (IN-05)

| Item | Para qual serviço | Até |
|---|---|---|
| Logo e pelo menos 12 fotos reais (fachada com nome visível, interior, produtos, equipe) | Landing, Google, Tráfego | D3 (pedir no D0) |
| Cardápio ou lista de produtos com preços e fotos | Landing, Automação | D3 |
| Domínio e site atual (se houver), com quem está o registro | Landing | D2 |
| Perfil no Google: existe? quem é o dono? (convite para o Henrique como administrador) | Google | D1 |
| Comprovante de que o cliente administra a empresa (para a verificação do Google) | Google | D2 |
| Facebook e Instagram: convite de acesso; conta de anúncios; forma de pagamento cadastrada pelo cliente | Tráfego | D2 |
| Orçamento de mídia mensal aprovado por escrito | Tráfego | D1 |
| Número de WhatsApp que o SDR vai usar e documentos para a verificação do negócio na Meta | Automação | D2 |
| Horário de funcionamento (com feriados), área de entrega, formas de pagamento, diferenciais | Todos | D1 |

### Pauta da reunião de início (IN-06)

1. Objetivo do cliente e como ele mede sucesso (pedidos, mensagens, ligações).
2. Público, região e horário de atendimento.
3. Diferenciais e concorrentes que ele conhece.
4. Quem aprova cada entrega do lado do cliente, e por qual canal.
5. Prazos combinados, com os avisos: a verificação do Google e a aprovação de mensagens da Meta **não dependem de nós** e podem passar do prazo.
6. Orçamento de mídia e forma de pagamento das contas de anúncio.
7. O que acontece depois das entregas (recorrência mensal).

## Fim (repete para cada entrega)

| ID | Tarefa | Responsável | Dia | Depende de | Pronto quando |
|---|---|---|---|---|---|
| FI-01 | Revisão interna da entrega (checklist da receita) | Henrique | último dia − 1 | entrega pronta | Checklist sem pendência |
| FI-02 | Apresentar ao cliente: reunião ou vídeo explicativo com o link no grupo | Dono do serviço | último dia | FI-01 | Apresentado |
| FI-03 | Aceite por escrito (WhatsApp vale), guardado em 05 Reuniões e atas | Henrique | último dia | FI-02 | Aceite guardado |
| FI-04 | Treinar o cliente: como receber os leads, como pedir avaliação (placa NFC), o que vem no mês | Henrique e dono do serviço | último dia | FI-03 | Treino feito |
| FI-05 | Iniciar a cobrança mensal e criar as tarefas da recorrência na central | Henrique | depois da última entrega | FI-03 | Cobrança agendada; tarefas mensais criadas |
| FI-06 | Pedir depoimento (texto ou vídeo) e avaliação da ATIVOS no Google | Henrique | D30 (com os primeiros resultados) | FI-05 | Depoimento recebido |
| FI-07 | Lições aprendidas: o que mudar na receita | Henrique (todos opinam) | depois da última entrega | FI-03 | PR com a receita atualizada, ou "sem mudança" registrado |
