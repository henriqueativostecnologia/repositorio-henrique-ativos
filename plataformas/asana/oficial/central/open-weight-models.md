---
fonte: https://help.asana.com/s/article/open-weight-models?language=en_US
baixado: 2026-11-10
---

# Understanding Open-Weight Models in Asana

Asana uses open-weight models to give customers greater flexibility and optimized performance across AI-powered workflows. Fireworks.ai serves as Asana's inference provider for these models.

## What are Open-Weight Models?

Open-weight models are AI models where the neural network's trained parameters, or "weights," are made publicly accessible by the developers. Unlike closed models, this transparency allows companies to customize and host models more efficiently while maintaining greater control over the infrastructure and output quality.

## Benefits of Open-Weight Models

The integration of open-weight models allows Asana to strike an optimal balance between cost, quality, and performance for AI products. By routing some traffic to these models, we can deliver faster results and maintain high-quality outputs while managing operational costs effectively.

## Open-Weight Model Developers

Open-weight models are developed by companies for general personal and commercial use, free of charge, as long as certain licensing terms are followed. Asana has no direct commercial relationship with these companies, and customer data is not transmitted to open weight model developers.

[Fireworks.ai](http://fireworks.ai) is our chosen inference provider for open-weight models, and we may introduce other open-weight model families on AWS Bedrock in the future. All our inference provider infrastructure meets Asana’s strict security, privacy, and compliance requirements.

Here is a list of open-weight model developers Asana utilizes in its product:

| **Model developers** | **Date introduced** | **Region Support** | **Inference Provider(s)** |
|----------------------|---------------------|--------------------|---------------------------|
| Kimi                 | September 16, 2026  | US                 | Fireworks.ai              |
| z.ai                 | September 16, 2026  | US                 | Fireworks.ai              |
| Deepseek             | September 16, 2026  | US                 | Fireworks.ai              |

## Data Privacy and Model Training

Asana maintains a strict policy regarding the use of customer data for model training. We do not train any models, including open-weight models, on customer data in any form without prior consent. This ensures that your organization's data remains private and is used solely to power the AI features within your own workspace.

## Admin Controls and Availability

We believe in providing admins with granular control over their organization's AI experience.

### Default Settings

- **New and existing free, Starter, Advanced, Enterprise, and Enterprise+ Domains (excluding Enterprise+ domains with the EU-Data Residency Add-on)**: These models will be **on-by-default** to provide immediate access to enhanced performance.

### Exclusions and Restrictions

- **Customers who have disabled one or more providers:** For customers who have made it clear they have provider-specific preferences by disabling one or more LLM providers in their admin console, we will set new LLM providers (including Fireworks) to **off-by-default**. 
- **AsanaGov**: Due to strict compliance and regulatory requirements (such as prohibitions on specific types of use), Fireworks.ai and open-weight models are **excluded** from AsanaGov/FedRAMP domains.
- **Enterprise+ customers with the EU-Data Residency Add-on:** Fireworks is not available for domains with the EU-Data Residency Add-on enabled. The Fireworks provider toggle will appear as unavailable in the admin console for these domains.
- **AWS Marketplace customers**: Customers that purchase Asana via the AWS Bedrock have all their AI traffic routed through Asana’s AWS Bedrock instance.

## How to Manage AI Providers

Admins can manage these settings directly within the admin console.

1.  Click your profile picture in Asana and navigate to the admin console.
2.  Click **Settings.**
3.  Scroll down to **Domain settings** and click **Asana AI.**
4.  Click **Providers and APIs** under **Advanced.**
5.  Enable or disable specific providers by clicking the relevant check boxes.
6.  Click **Save changes.**

** **
