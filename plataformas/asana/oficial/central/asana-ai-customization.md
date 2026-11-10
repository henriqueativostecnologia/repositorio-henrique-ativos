---
fonte: https://help.asana.com/s/article/Asana-AI-customization?language=en_US
baixado: 2026-11-10
---

# Asana AI customization

This Help Center article supplements [Asana AI features and admin controls](https://help.asana.com/s/article/asana-ai-features-and-admin-controls?language=en_US) and provides further detail regarding certain **advanced settings and customizations** available in the admin console.

Settings discussed in this article are managed through the **Advanced settings** subsection of the Asana AI section of the admin console.

#### Related articles:

- [Asana AI features and admin controls](https://help.asana.com/s/article/asana-ai-features-and-admin-controls)
- [Asana AI FAQ](https://help.asana.com/s/article/asana-ai-faq)

## Asana AI providers and feature breakdown

Asana AI allows customers to separately enable or disable models that are provided by Asana’s AI partners using third-party servers. This selection is managed through the **Advanced settings** section of the admin console.

## Provider selection

In the admin console's **Advanced settings** section, admins can:

- Enable or disable certain third-party AI providers
- View which AI providers are currently enabled for Asana AI

For some organizations, provider toggles may be locked. Organizations with Asana Data Residency and those purchasing Asana through AWS Marketplace have all AI traffic routed through AWS Bedrock. As a result, providers like [Fireworks.ai](http://fireworks.ai) and Google cannot be enabled for these domains.

## Important considerations

### AI provider requirements

It's important to note that Asana AI features require at least one AI provider toggle (e.g., OpenAI, Anthropic, Google, or Fireworks.ai) to be enabled. AI features will be unavailable to your organization if you do not enable at least one AI partner. In most cases, if a specific provider is disabled, eligible requests will be routed to another enabled provider rather than the feature being turned off entirely, but some features require certain providers to be enabled to function. See below for more detail.

### Provider hosting limitations

Models provided by AWS Bedrock are hosted on the same Amazon Web Services (AWS) infrastructure where Asana's core platform has always been hosted. Since AWS is Asana's existing cloud service provider, using AWS Bedrock keeps AI data processing within the AWS network, enhancing security and privacy. As AWS Bedrock is a core component of Asana AI, it cannot be separately disabled. Customers who do not want to use AWS Bedrock can disable Asana AI entirely in the Admin Console. Unlike AWS Bedrock, models provided by OpenAI, Anthropic, Google, and Fireworks.ai are hosted on third-party servers outside our AWS network.

### Feature break-down by third-party AI partner

|                                                           |                                                             |
|-----------------------------------------------------------|-------------------------------------------------------------|
| **Feature**                                               | **Provider**                                                |
| Smart chat                                                | Anthropic                                                   |
| Smart rule creator                                        | OpenAI and Anthropic                                        |
| Smart fields                                              | OpenAI, Anthropic, or Google\*                              |
| Smart editor                                              | OpenAI, Anthropic, or Google\*                              |
| Smart status                                              | Anthropic                                                   |
| Smart projects                                            | OpenAI                                                      |
| Smart summaries on projects, tasks, portfolios, and inbox | OpenAI, Anthropic, or Google\*                              |
| Smart import for tasks                                    | Anthropic                                                   |
| Smart import for projects                                 | Anthropic                                                   |
| Smart goals                                               | Anthropic                                                   |
| AI Studio                                                 | OpenAI or Anthropic - as available and as selected by users |

\*[Google Gemini](https://gemini.google.com/) and Fireworks.ai support is currently available for a limited set of features and is being expanded over time.

## Proactive AI

### What is proactive AI?

Proactive AI is a capability that will surface AI-generated content to users at the optimal time, without them needing to manually request it. An example of proactive AI is sending a project smart summary insight to project members when certain types of relevant activity have occurred, without them having to explicitly ask for it.

Proactive AI will use data from your organization - including metadata and user generated content - to identify the right moment to surface AI features and insights, and the right users to surface them to.

### How does proactive AI work?

There are a variety of Asana AI features that operate proactively, but the general flow is:

- Users create and edit work content (such as tasks or projects) throughout their regular use of Asana. These activities are aggregated and analyzed to identify high-level patterns about how work is progressing.
- When certain patterns are recognized or conditions are met, Asana AI will determine an optimal time to trigger a proactive AI feature and identify the most relevant users to surface the feature to.
- Users are made aware of the proactive AI feature through a notification or UI element.
- They can choose to take a recommended follow up action, sign up for similar recurring outputs on an ongoing basis, and/or dismiss the proactive AI.

For example, a user may receive a proactive project smart summary insight inside Asana because the project meets certain conditions like reaching a certain amount of recent activities. The user(s) who receive the proactive insight are selected based on a variety of relevancy factors, such as users recently added to the project or project admins, to ensure that proactive features are relevant to the right people at the right time.

After experiencing the proactive AI feature, the user can optionally choose to take a follow up action, such as opting into this insight on a regular recurring basis or copying the insight to share it with others.

### How is my data protected with proactive AI?

Proactive AI leverages the same security and privacy practices as the rest of Asana’s AI features. There are no changes to the [Asana AI safeguards](https://help.asana.com/s/article/asana-ai-features-and-admin-controls?language=en_US).

You can learn more about Asana’s security and privacy practices at our [Trust Center](http://security.asana.com/).

## Web access

Web access is a capability that allows Asana AI to access information from the web to provide more accurate and up-to-date responses. This capability is currently limited to Asana AI Studio, where users can configure their smart workflows to conduct web searches and read web links available on the public internet. When enabled, this capability helps Asana AI deliver more comprehensive answers by incorporating real-time information from online sources.

### How it works

Web access has two components:

1.  Web search
2.  Web links

To use web access capabilities, customer admins must enable the functionality in the Asana AI section of the admin console.

### Web search

**Web search** conducts a web search and retrieves results based on key words determined by Asana AI.

- **Configuration**: If enabled in the admin console, rule creators must explicitly enable web access when building an AI Studio rule.
- **Intelligent searching**: When a smart workflow runs, Asana AI will automatically determine whether a web search would improve its response quality. Searches won't occur with every interaction.
- **Source citations**: When Asana AI uses information from the web, it will include citations to reference the original sources.

### Web links

**Web links** visits and retrieves results only from a user-provided URL

- **On by default**: If enabled in the admin console, Asana AI will default to reading content from specific web links users provide when creating or running a smart workflow via AI Studio. Users can turn this off in the settings of their particular AI Studio rule.
- **Which links are read**: AI will read any links contained in the guidance of the rule, as well as any links in the task which triggers the smart workflow. It will not read links in @mentioned tasks or projects.

### Important considerations

Web access is not available for HIPAA-compliant workspaces due to limitations set by Asana's AI partners. Web search functionality is currently only available using OpenAI models.

## Third-party data

### What is third-party data?

Access to third-party data allows users to run searches, retrieve information and share content with connected applications like Google Drive, Slack, Salesforce, and Microsoft 356. These data connectors can be enabled and managed by connecting your [Amazon Q Business](https://aws.amazon.com/q/?trk=c570e8a2-ec3c-4968-baa4-f8537e37dd1d&sc_channel=ps&ef_id=Cj0KCQjwgIXCBhDBARIsAELC9Zg3M9G4mxAloVhTYkKCNARFafy2yRzn7zguVX-yeCjoXHWk_vMk7rIaAjeoEALw_wcB:G:s&s_kwcid=AL!4422!3!692006004634!p!!g!!amazon%20q!21048268530!159639951495&gad_campaignid=21048268530&gbraid=0AAAAADjHtp-aL9hz4r-GXqQTZJQ8_Q_PR&gclid=Cj0KCQjwgIXCBhDBARIsAELC9Zg3M9G4mxAloVhTYkKCNARFafy2yRzn7zguVX-yeCjoXHWk_vMk7rIaAjeoEALw_wcB) index to Asana. Amazon Q Business is an independent product, purchased through Amazon Web Services. 

### How is third-party data used?

Only data from explicitly connected data sources will be used within Asana features:

- Asana  Smart chat will automatically search for relevant information across Asana and any connected data sources in order to answer user questions.
- AI Studio allows users to connect third-party data sources in the rule configuration settings. One connected, this data source will be used when running the user-defined set of instructions. 

### How is my data protected with proactive AI?

Neither Asana nor our AI partners use your data for training AI models. In addition, Asana’s AI partners are contractually required to delete customer data upon completion of the relevant AI query. 

To learn more about how AWS manages data, visit [Amazon Q index Security and Data Protection.](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/security.html)

## AI for Asana Gov customers

Asana Gov customers are defaulted to have all AI features disabled, but these features can be enabled while continuing to meet FedRAMP requirements. Super admin permission is required to enable Asana AI features. 

For Asana Gov customers, all enabled AI features are powered by AWS Bedrock which maintains a [FedRAMP Authorization](https://aws.amazon.com/about-aws/whats-new/2024/08/amazon-bedrock-achieves-fedramp-high-authorization/). Models provided by AWS Bedrock are hosted on the same Amazon Web Services (AWS) infrastructure as Asana Gov. Since AWS is Asana's existing cloud service provider, using AWS Bedrock keeps AI data processing within the AWS infrastructure. Fireworks.ai is excluded from Asana Gov domains due to FedRAMP compliance requirements.

Not all AI features are available to Asana Gov users as some features require data outside of Asana Gov’s infrastructure. The following features are disabled and can not be enabled for Asana Gov domains: 

- Access web content 
- 3rd party data connectors

[](https://forum.asana.com/c/forum-en/tips/6)
