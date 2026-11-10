---
fonte: https://help.asana.com/s/article/ai-studio-models?language=en_US
baixado: 2026-11-10
---

# AI Studio models

AI Studio lets you build smart workflows that run on models from Asana’s AI partners. You choose a model for each workflow so you can match capability to the job and keep costs predictable.

An AI workflow is a rule with an AI step. When you add AI to a rule, the AI step is handled by the model you choose. That model supplies the reasoning and writing for that step. In practice, this means your rule can use the power of systems like ChatGPT or Claude, depending on which partner and model you select. You can change the model at any time as you refine the workflow.

## What is a model?

The word model refers to the term **Large Language Model**, or **LLM** for short. A model is the AI system that generates the response for a workflow step. AI Studio connects to partners (including OpenAI, Anthropic, Google, and open-weight models served through Fireworks.ai) so you can pick the system whose strengths match the job to be done.

Models trade off quality, speed, and credits. Lighter models are fast and efficient for triage, short comments, and small text transforms. Heavier models handle longer context, more reasoning, and higher polish writing, but they use more credits.

The models used in AI Studio come from [our AI partners](https://help.asana.com/s/article/asana-ai-faq#asana39s-ai-partners), who build, own, and operate these systems. AI Studio connects to them so your workflow can use their capabilities inside your rules. Asana does not create or train these models; we integrate them and give you a simple way to choose the one that fits the job.

The models available to you in AI Studio depend on which AI providers your organization's admin has enabled. If a provider has been disabled, models from that provider will not appear in the model selector.

Asana does not use customer data for training and has contractual agreements with its AI partners that prohibit the use of customer data to train or improve their AI models and services.

## Default model

When you create a new workflow, AI Studio starts you with a default model so you can build quickly. Today that default is Claude Sonnet 4.5, chosen for a good balance of quality and credit efficiency. You can change it at any time in the workflow model setting.

Currently, if AI features powered by Anthropic have been disabled by an admin, GPT-5 will become the default model. Open-weight models served through Fireworks.ai are not part of the default model selection and do not join the fallback chain.

A common question is whether the default model is good enough. The answer is usually yes. For high volume steps like classifying tasks, drafting short updates, or extracting a few fields, the default is usually the right place to start. Feel free to keep it unless you see gaps like missed context or writing quality that does not meet your bar.

A quick way to check and decide whether the default model is right for the job is to pick five representative tasks and run your workflow with it. Skim for accuracy, tone, and length. If something feels underpowered, switch the model to a heavier option and rerun the same samples, then compare the outputs and note the credit impact. Choose the option that meets your quality bar at the lowest predictable credit cost.

## Models available in AI Studio

AI Studio offers a range of large language models you can use in your smart workflows. The right model to use depends on the type of work to be done and the potential cost.

**Claude Sonnet 4.5**

Premium model. Great at writing documents and most tasks.

**GPT-5.2**

Premium model. Best for complex tasks and following detailed guidance.

**GPT-5**

Premium model. Best for complex tasks and following detailed guidance.

**GPT-5 mini**

Best for most tasks.

**Claude Opus 4.6**

Elite model. Best at writing documents and following complex guidance.

**Claude Haiku 4.5**

Premium model. Good at summarizing and classifying info.

**Kimi K3**

Premium model. Best for most tasks.

**GLM 5.2**

Premium model. Best for most tasks.

**Deepseek V4 Flash**

Best for simple tasks.

To read the model descriptions from our AI partners in their own words, visit [Anthropic’s models overview](https://docs.claude.com/en/docs/about-claude/models/overview) and [OpenAI’s models page](https://platform.openai.com/docs/models). 

For details on the open weight models in Asana, see [Understanding Open-Weight Models in Asana](https://help.asana.com/s/article/open-weight-models).

## How to choose a model

When building a workflow, you can pick a model inside each rule. Start with the simplest option that gets the job done. Lighter models are fast and credit efficient, which suits triage, short comments, routing, and small text transforms. Heavier models can add value when you need deeper reasoning, long context, or high quality writing. Switch between the available models in the AI Studio settings panel when creating an AI rule.

You can also mix models across one process. Many teams run a lighter model for high volume steps and reserve a heavier model for a final summary or decision point. AI Studio supports this by letting you pick a model per rule.

For example, in a creative requests workflow where the goal is to produce a high-quality draft of a blog post, the workflow will consist of multiple rules. Rules designed to rename tasks or move work between sections will be fine with lower-cost models, but the rules which deal with the drafting of content may benefit from a higher-cost model to achieve the desired output quality.

As mentioned, AI Studio uses credits, and different models consume credits at different rates. All paid plans include AI Studio Basic at no extra cost, which comes with a pre-set credit limit per month so teams can start building immediately. If you need more credits, admins can [purchase AI Studio Plus directly](https://app.asana.com/admin/billing/ai_studio/upgrade?_gl=1*1x067hu*_gcl_au*MTk3MjcxMjI1NC4xNzU0NjUxOTQy*FPAU*MTk3MjcxMjI1NC4xNzU0NjUxOTQy*_ga*MjQxMTM1NDcwLjE2NTE1NjUwMzM.*_ga_J1KDXMCQTH*czE3NjIyNTY2MDYkbzY1NCRnMSR0MTc2MjI1NjY1NCRqMTIkbDAkaDEzMjkzOTU2Ng..*_fplc*RmpUYWJVYkRNckROZFp1Y2xMdzY4cjN4UnZ1NGZ5bmczemRnaUZHTFZoaU5WU3lEZExNcVh1Uk5LblhzZGFGOW5wcU5LdFZYZTUlMkZoalhDNkNWZmxBdnZmeFptdkMlMkZvWXBuZTJmYml4Y25wS0xFTmI5VmhjSkFzY1Fzc3FwUSUzRCUzRA..) in the admin console, and there’s also an [AI Studio Pro](https://asana.com/sales) option available through sales for larger scale operations. For current credit amounts and purchase details, visit our [AI Studio product page](https://asana.com/product/ai/ai-studio) or [AI Studio add-on and pricing](https://help.asana.com/s/article/ai-studio-pricing?language=en_US).
