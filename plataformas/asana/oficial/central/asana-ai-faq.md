---
fonte: https://help.asana.com/s/article/asana-ai-faq?language=en_US
baixado: 2026-11-10
---

# Asana AI FAQ

In this article, you'll find answers to some of the most frequently asked questions about Asana AI. For a more exhaustive list of questions and answers about Asana AI, please visit the [Asana AI Fact Sheet](https://security.asana.com/?itemUid=c21c12a4-664a-4b9e-ac10-b63bfafb0305&source=documents_card) from the Asana Trust Center.

#### Related articles:

- [Get started with Asana AI](https://help.asana.com/s/article/get-started-with-asana-ai?language=en_US)
- [Smart status](https://help.asana.com/s/article/smart-status)
- [Smart chat](https://help.asana.com/s/article/ai-chat)
- [Smart rule creator](https://help.asana.com/s/article/smart-rules?language=en_US)
- [Smart summaries](https://help.asana.com/s/article/smart-summaries?language=en_US)
- [Smart fields](https://help.asana.com/s/article/smart-fields?language=en_US)
- [Smart editor](https://help.asana.com/s/article/smart-editor?language=en_US)
- [Smart projects](https://help.asana.com/s/article/smart-projects?language=en_US)
- [Smart goals](https://help.asana.com/s/article/smart-goals?language=en_US)
- [Asana AI Studio](https://help.asana.com/s/article/ai-studio)

## What is Asana AI?

Asana AI refers to a suite of artificial intelligence features integrated into the Asana collaborative work management platform and powered by large language models (LLMs). These features are designed to help teams work more efficiently by automating tasks, providing insights, and optimizing workflows.

For a description of individual Asana AI features, see [Asana AI features and admin controls](https://help.asana.com/s/article/asana-ai-features-and-admin-controls?language=en_US).

## Asana's AI partners

### Who are Asana's AI partners?

Asana AI incorporates generative AI capabilities via LLMs from these AI partners:

- [OpenAI](https://openai.com/) (introduced May 2023)
- [Anthropic](https://www.anthropic.com/) (introduced September 2023)
- [AWS Bedrock](https://aws.amazon.com/bedrock/) (introduced April 2025)
- [Google Gemini](https://gemini.google.com/) (introduced July 2026)
- [Fireworks.ai](https://fireworks.ai/) (introduced September 2026)

For further details on these AI partners, see [Asana AI customization.](https://help.asana.com/s/article/Asana-AI-customization)

### What are open-weight models and who develops them?

Open-weight models are AI models whose trained parameters are made publicly available by their developers. Asana uses open-weight models to help balance performance and cost across AI features. These models are developed by third-party companies and served through Fireworks.ai, Asana's inference provider for open-weight models. Asana has no direct commercial relationship with open-weight model developers. The open weight models are hosted and run on Fireworks servers, so customer data is not shared with the open-weight model developers. For more information, see [](https://docs.google.com/document/d/1X6IUZfiw5eUbUN5lyEOgalGSajGRw2INJLldgYvalM4/edit?tab=t.309fc5jcewfl) [Understanding open-weight models in Asana.](https://help.asana.com/s/article/open-weight-models)

### How do I enable or disable Asana AI?

Customers can visit the [Asana AI page](https://help.asana.com/s/article/asana-ai-features-and-admin-controls) of their admin console to enable or disable AI features for their organization at any time. See [Asana AI features and admin controls](https://help.asana.com/s/article/asana-ai-features-and-admin-controls) for details.

## Data, security, and oversight

### What kinds of data does Asana AI use?

Asana AI uses two types of data:

- Usage metadata (e.g. task creation time, viewer count)
- User-generated content (e.g. task titles, descriptions, comments)

### Is customer data used for training?

No. Asana does not use customer data for training and has contractual agreements with its AI partners that prohibit the use of customer data to train or improve their AI models and services.

### How long is customer data retained when used for Asana AI?

To protect our customers, Asana’s AI partners are contractually required to delete customer data upon completion of an individual AI query. Please see the Asana AI Fact Sheet shared above for further details.

### How does Asana develop and validate the safety, robustness, and accuracy of Asana AI?

Asana employs a multi-layered approach to address potential technical, legal, ethical and performance issues in Asana AI. This process begins with a cross-functional team that systematically reviews each proposed AI feature, considering its intended purpose, operational and model details, data usage, and potential quality or accuracy issues.

Asana implements multiple types of testing:

- **Unit Testing**: Individual functions and components are tested to confirm they operate as intended without introducing quality/accuracy issues.
- **Integration Testing**: Different components of the AI are combined and tested to ensure they work together seamlessly without introducing quality/accuracy issues when interacting.
- **End-to-End Testing**: Asana runs real-world scenarios to evaluate the entire system’s performance, focusing on accuracy, fairness, and overall user experience. This helps identify any quality/accuracy issues that might surface in practical use cases.
- **AI Partnering**: Asana collaborates closely with its AI partners, who conduct their own bias testing, red teaming, and other security measures. These partners' safeguards are integrated into Asana’s AI features, helping to ensure that the AI models are fair, reliable, and secure.

For a better feel of Asana's testing playbook, visit our blog (e.g. [Asana's LLM testing playbook: Our analysis of Claude 3.5 Sonnet](https://asana.com/inside-asana/llm-testing-claude-sonnet-analysis)).

### Can users understand the reasoning behind Asana's AI outputs?

To promote transparency, certain Asana AI features link, where relevant, to their work in Asana (e.g. tasks, messages, comments) to cite to specific work and the associated reasoning behind including the AI-driven insights shared with users.

### Where is Asana AI hosted?

Asana features are hosted in Asana's data centers. For more information, see [Subprocessors](https://asana.com/terms/subprocessors) and [Data residency at Asana](https://help.asana.com/s/article/data-residency-for-asana).

Asana AI’s partner-powered features share relevant customer data with those AI partners, whose servers are currently located in the United States or European Union depending on the region an Asana customer has chosen for storing their Asana data using the Data Residency settings above. These AI partners do not train on customer data and delete such data  upon completion of a particular AI query, as further described elsewhere in Asana AI’s documentation.

### What technical and organizational security measures do Asana's AI partners maintain?

As a condition of permitting a [subprocessor](https://asana.com/terms#subprocessors) to process personal data, Asana enters into a written agreement with each subprocessor containing data protection obligations at least as protective as those put into place to protect customer personal data from accidental or unlawful destruction, loss, alteration, or unauthorized disclosure or access.

You can learn more about OpenAI’s technical and organizational security measures at [https://openai.com/security](https://openai.com/security).

You can learn more about Anthropic’s technical and organizational security measures at [https://trust.anthropic.com/](https://trust.anthropic.com/).

You can learn more about Fireworks.ai's technical and organizational security measures at [https://trust.fireworks.ai/](https://trust.fireworks.ai/). 

### How much human oversight is involved in Asana AI?

Asana AI features are natively designed to include human review steps to reflect our stance that humans are ultimately responsible for incorporating decisions, recommendations or insights generated by AI. Furthermore, where customization may be available to users, Asana’s customers can optimize human review steps through their instructions in order to cater to their specialized use case(s).

### Does Asana have ethical principles or guidelines for AI development?

Yes, Asana follows human-centered AI principles, which include commitment to safety, promoting transparency, enhancing human capabilities, and respecting privacy. See the [Asana AI Principles](https://asana.com/pl/ai-principles) for details.

## AI features and settings

### Why can’t I see AI features in my Asana?

Asana AI features are now available for [organizations](https://help.asana.com/s/article/managing-an-organization?language=en_US) and [workspaces](https://help.asana.com/s/article/understanding-workspaces?language=en_US) with a paid subscription. If your organization/workspace has a paid subscription and you don’t have access, please reach out to your designated super admin (for organizations) or the billing owner/creator (for workspaces) to ensure that Asana AI features are enabled in the admin console.

To learn more about the differences between types of Asana instances, visit our [Workspaces and organizations](https://help.asana.com/s/article/workspaces-and-organizations-faq?language=en_US) article.

- For **organizations**, this excludes guest accounts. Guests do not have access to AI features.
- For **workspaces**, this excludes limited access members.

### How do I edit my organization's AI settings?

Customers can visit the [Optimize with artificial intelligence](https://help.asana.com/s/article/asana-ai-features-and-admin-controls?language=en_US) tab of the admin console to enable or disable AI features for their organization at any time. See [Asana AI features and admin controls](https://help.asana.com/s/article/asana-ai-features-and-admin-controls) for details.

### What languages are currently supported by AI?

While Asana's AI capabilities are designed to work in [all supported languages](https://help.asana.com/s/article/navigation-and-display?language=en_US), we have only completed testing for English at this time. We will continue to validate other supported languages as we roll out features to our customers and will share more details soon.

### How do I know if an Asana feature is powered by AI?

Asana is thoughtfully integrating AI capabilities to enhance your productivity. We've developed a consistent design system to help you easily identify these features. In some cases, you'll see a clear label such as “AI” (e.g. “AI Teammates”) or similar wording directly within the feature. In other instances, you'll notice our distinctive starburst icon which indicates that AI is at work to assist you — like the one shown below and similar ones used across Asana.

[](https://forum.asana.com/c/forum-en/tips/6)
