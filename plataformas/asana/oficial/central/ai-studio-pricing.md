---
fonte: https://help.asana.com/s/article/ai-studio-pricing?language=en_US
baixado: 2026-11-10
---

# AI Studio add-on and pricing

**AI Studio is available for [Starter](https://asana.com/plan/starter), [Advanced,](https://asana.com/plan/advanced) [Enterprise](https://asana.com/enterprise), and [Enterprise+](https://asana.com/enterprise) customers.**

## AI Studio pricing options

AI Studio is available three ways; free access on the AI Studio **Basic** tier, and paid access via AI Studio **Plus** or AI Studio **Pro**.

> If you purchased AI Studio before September 16, 2026, some features and credit structures differ. Please refer to the section below titled ‘If you purchased AI Studio before September 16, 2026’.

**AI Studio Basic**: Included access to AI Studio to explore how AI can help take on routine, manual work (includes rate limits). AI Studio Basic is included in all paid domains using Asana AI.

**AI Studio Plus**: Paid access to AI Studio to level up productivity for individuals and small teams (available on monthly & annual plans).

**AI Studio Pro**: Paid access to AI Studio to scale complex workflows and business operations with advanced billing controls (available on an annual plan).

#### Related articles

- [Introduction to Asana AI Studio](https://help.asana.com/s/article/ai-studio)
- [Create smart workflows with AI Studio](https://help.asana.com/s/article/ai-studio-smart-workflows)
- [Writing instructions in AI Studio](https://help.asana.com/s/article/writing-ai-studio-instructions)
- [AI Studio FAQ](https://help.asana.com/s/article/ai-studio-faq)
- [Asana AI FAQ](https://help.asana.com/s/article/asana-ai-faq)

## AI Studio Basic

AI Studio Basic is part of the core Asana experience, allowing all members of your domain to build smart workflows.

Monthly rate limits for AI Studio Basic are based on your billing account’s tier:

- Starter: 50,000 AI Studio Basic credits per billing account per month.
- Advanced: 75,000 AI Studio Basic credits per billing account per month.
- Enterprise: 200,000 AI Studio Basic credits per billing account per month.
- Enterprise+: 200,000 AI Studio Basic credits per billing account per month.

## AI Studio Plus

Customers can purchase an annual AI Studio Plus subscription, which includes 100,000 credits that reset each month. Should additional credits be required, they may be purchased in increments of 100,000 (for example, 100,000, 200,000, 300,000 and so forth). Alternatively, customers may purchase 1.2 million credits for the year. These credits are valid for the entire annual term and do not reset monthly.

Customers can purchase AI Studio Plus directly in-product. See our [dedicated article on AI Studio Plus](https://help.asana.com/s/article/ai-studio-plus) for detailed information on how to purchase and manage an AI Studio Plus subscription.

## AI Studio Pro

Customers can purchase an annual AI Studio Pro package, which includes 20 million credits valid for the entire annual term. 

Customers who purchase AI Studio Pro can use the builder list to control which members can consume any credits, Basic or Pro. Credits are not split into separate pools.

For further information, please contact your account representative. Learn how to enable AI Studio [here](https://help.asana.com/s/article/ai-studio#How_to_enable_AI_Studio).

## AI Studio credits

### What is a credit? 

Credits are used to power Asana's AI Studio platform. Credits are calculated based on volume of data processed through the large language model selected in the workflow. The credits needed for a query are variable and depend both on the amount of data that is input and output, as well as which large language model (LLM) a query uses. See [Credit consumption](https://help.asana.com/s/article/ai-studio-pricing#Usage_based_pricing) below for more detail and examples.

## Credit consumption

The credits needed for any workflow to run are variable and depend on four factors. Three of these factors are a product of how the workflow’s AI-powered rules are built: the **model selected**, the **volume of input data**, and the **volume of output data**. The final factor which influences credit consumption is the **frequency of execution** of a rule. Workflows which use [web access](https://help.asana.com/s/article/ai-studio-faq#ai-studio-and-web-access) consume additional credits, detailed below.

### Model selection

AI Studio offers access to a choice of models from our AI partners. Because models vary in capability, they also vary in credit consumption. For simple categorization or summarizing workflows, consider using low or medium cost models such as GPT-4o mini, or Claude 3.5 Haiku, respectively. For workflows that require more reasoning, problem solving, handling many files or large attachments, consider using a higher cost model such as GPT-4o or Claude 3.5 Sonnet. AI Studio creators are encouraged to use the most suitable model for their workflow, in order to balance cost and performance. The AI Studio FAQ contains descriptions of the available models, but experimenting with different models will help you find the right balance.

### Volume of input data

The volume of input data has an influence on the credit consumption of a rule. Input data refers to the data included in the task which triggers the rule (task description, comments, attachments, etc.) and the data included in the AI-powered rule’s guidance (the prompt which gives the AI instructions, attachments added to the guidance). For example, if a 20-page document is attached to the rule’s guidance, it will consume more credits each time it runs when compared to a 1-page document.

### Volume of output data

The volume of output data also influences how many credits are consumed. Output data refers to the actions performed by the rule when it runs, including actions like changes made to tasks, or texts that are produced. For example, a rule action which generates a 5-page brief and translates it into multiple languages will consume more credits than an action which simply assigns a task and changes a custom field value.

### Frequency of execution

The number of times a rule runs influences the number of credits consumed. A rule that runs 15 times per week consumes more credits than a similar rule which runs three times per week.

### How web access affects credit consumption

Web access allows Asana AI to gather real-time information from public websites. This includes both conducting web searches (**web search)** and reading content from specific user-provided links (**web links)**.

Executing a web search within a rule, or using web links to access a URL — contained in the rule guidance, or the description of the task that triggers the rule — consumes additional credits per execution, on top of the standard input/output credit consumption.

## Credit limits

### What is a credit limit?

AI Studio Plus and AI Studio Pro customers purchase a set number of credits to power smart workflows with AI Studio. When included credits run out, rules will stop running unless on demand purchasing has been enabled in the admin console. Customers who want their workflows to keep running beyond their included credits should enable on demand purchasing. On demand usage is billed monthly in arrears based on actual consumption from the prior month.

### How will I know that my domain has reached a credit limit?

Admins will receive an email warning and in-product banner when the account has reached 80% of their credit limit threshold and another email when they reach 100% of their credit limit.

### What should I do if I hit a credit limit?

Admins can view credit usage in the Billing tab of the admin console. Customers can purchase additional credits on demand directly in the admin console. On demand usage is billed monthly in arrears based on actual consumption from the prior month.

## Model pricing

As workflows are executed, credits are consumed based on two factors:

**Content size**: This is determined by the total amount of input and output content used by the underlying LLM during the workflow execution. To compute this, we take the total number of tokens from the underlying model selected, divide by 100, and round up to the nearest integer. This represents the base cost.

**Model multiplier**: The content size is multiplied by a factor that varies based on the specific LLM model used. More advanced models like Sonnet, which have higher quality and require more computing resources, have a correspondingly higher multiplier.

The total number of credits consumed by a workflow is calculated by multiplying the **content size** by the **model multiplier**. The model multipliers are:

+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| #### Model                                         | #### Input multiplier                              | #### Output multiplier                             |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **Claude Opus 4.6**                                | 8                                                  | 40                                                 |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **Claude Sonnet 4\***                              | 5                                                  | 25                                                 |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **Claude Sonnet 4.5**                              | 5                                                  | 25                                                 |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **GPT-5**                                          | 2.5                                                | 20                                                 |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **GPT-5.2**                                        | 3.5                                                | 35                                                 |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **GPT-5 mini**                                     | 0.5                                                | 5                                                  |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **Claude 4.5 Haiku**                               | 3                                                  | 15                                                 |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+

## View and export AI Studio usage data in the admin console

Admins and billing owners can view AI Studio usage data via the admin console. The usage tab shows useful data on how AI Studio is being used in your organization or division, whether you're using AI Studio Basic, Plus, or Pro.

To access AI Studio usage data:

1.  Click your profile picture and select **Admin console** from the menu
2.  Choose the **Billing** tab from the left menu
3.  Next, click **AI Studio**
4.  Select the **Usage** tab

The following usage information is displayed:

- AI Studio rule - the rule or workflow name
- Member - the builder associated with the rule
- Number of times run - how many times the rule executed
- Last rule run - when the rule last executed
- Model - the LLM used by the rule or workflow
- Credits used - total credits consumed by the rule

The usage data updates every few hours. You can toggle between the **Smart workflow builders** and **Smart workflow** tabs to view usage per person or per workflow.

### Export AI Studio usage data via CSV

Admins, super admins, and billing owners can export a CSV of AI Studio usage data by clicking the Export CSV button in the top-right corner of the usage tab. The CSV export capability is available for AI Studio Basic, Plus, and Pro. Data included is backfilled to January 8th 2025.

The following information is included in the CSV:

- RuleID
- Rule name
- Rule owner email address
- Run date/time
- Model name
- Credits used
- Credit source (basic or paid)
- Project name

Please note the CSV is delivered via email.

## Managing the AI Studio Pro builder list

If you are using AI Studio Pro, admins can manage credit access through the builder list. The builder list controls which members can consume any credits. Credits are not divided into separate Pro and Basic pools. All credits come from a single pool. When a member is added to the builder list, all workflow automations they own will draw from this shared pool. Automations do not need to be rebuilt.

There are three ways that admins can grant access to Pro credits:

### Via the AI Studio card in the admin console

1.  In the admin console, click **Billing** on the left navigation bar.
2.  Click the **AI Studio** card.
3.  Ensure you are viewing the **Access** tab.
4.  Click **Add members** to grant access to Pro credits by adding people to the builder list.
5.  Click **Remove** beside any name in the builder list to revoke access to Pro credits.

### Via the Add-ons column in the Members table

1.  In the admin console, click the **Members** tab.
2.  Find the **Add-ons** column in the table. See image below.
3.  Click the **Add-ons** dropdown next to the user you wish to grant access to.
4.  Select **AI Studio Pro** to add them to the Pro builder list.

### Bulk assign via CSV import

1.  Export a CSV of the member via the **CSV export** on the **Members** tab.
2.  Add the term **AI Studio Pro** in the Add-ons column next to anyone you wish to grant access to. Note that the term **AI Studio Pro** is case sensitive. See image below.
3.  Import the CSV via the **CSV import** button in the top-right of the **Members** tab.

## If you purchased AI Studio before September 16, 2026

If you are unsure whether this applies to your account, check with your billing owner.

**Credits included with AI Studio Pro**

AI Studio Pro packages purchased before September 16, 2026 include 5 million credits that reset quarterly.

**How the builder list works**

The builder list controls which members can consume Pro credits. Members added to the list gain access to Pro credits, while those not on the list continue using AI Studio Basic credits from a separate pool. When a member is added to the builder list, all workflow automations they own will pull from Pro credits. Automations do not need to be rebuilt.

**What happens when credits run out**

When all credits have been used, rules using AI Studio will no longer run. Rule builders will receive an email notification letting them know their rule cannot run. On demand purchasing is not available for subscriptions purchased before September 16, 2026.

**Purchasing additional credits**

To purchase additional credits, contact your account representative.
