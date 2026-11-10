---
fonte: https://help.asana.com/s/article/data-contributions?language=en_US
baixado: 2026-11-10
---

# Data contributions

Customers maintain control over their data contribution preferences; when enabled Asana collects de-identified information regarding platform usage. Known as "Usage Patterns," this data helps us identify common use cases and evaluate our performance so we can build a better product for you. **Admins & Super Admins on our Starter, Advanced, and Enterprise plans can opt out at any time via the Admin Console. **

To clarify our practices: Derived usage patterns are de-identified, and  this data is not used to train or fine-tune AI models. This is designed to analyze high-level usage patterns, providing insights that help us improve your experience using Asana. 

> For our Enterprise customer on negotiated terms, data contribution to derive usage patterns will start at your next renewal after September 16th, 2026. For our Advanced, Personal, or Starter domains, data contributions will start on September 16th, 2026.  A toggle is available in the admin portal to disable Data contributions available in advance so you can update your preferences in advance of the policy applying. 

**To opt out, an Admin or Super Admin should navigate to Admin Console \> Security \> Data Contributions and choose ‘Do not share data’:**

> Data contribution is permanently turned off for Asana Gov and HIPAA customers, and is default disabled for customer with EU Data Residency.

## How this benefits you

Usage patterns help us build the features your team actually needs, faster so you get more value out of Asana sooner.

Today, we rely heavily on direct customer conversations and manual feedback to understand how Asana is used in practice. That's valuable but it only captures a slice of real-world usage. Usage patterns let us see, at scale, which workflows and AI features are working well and where friction still exists so we can fix quality gaps and ship improvements before they become a support ticket for your team.

This also means our roadmap is shaped by how customers like you actually work, not assumptions. High-impact workflows get prioritized. AI features get tuned to reflect the way real teams structure projects, automate work, and search for information. This translates into faster time-to-value and stronger adoption across your organization. Using aggregated usage data to guide product development this way is standard practice across enterprise software, and one we apply with the privacy safeguards described throughout this article.

## What are usage patterns?

Usage patterns are broad category labels that describe the type of action people take in Asana. For example, a request to create a project from a template or summarize project status may be grouped into a general theme. Asana uses these labels to understand which experiences are helpful, where quality gaps exist, and which workflows may need improvement.

To create these labels, an AI or ML model processes the interaction long enough to assign a general theme - Asana employees cannot access the unprocessed data. The usage pattern stored is limited to the labels and, in some cases, a quality score tied to that label.

An end-to-end Example:

+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **What a user enters**                             | **How it’s processed**                             | **What Asana keeps & reports on:**                 |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| A user asks their AI Teammate “Find all tasks      | An LLM  processes the request, and assigns a usage | The labels are stored for reporting:               |
| assigned to me that are overdue in the Q3 Launch   | pattern label (or multiple), and identifying user  |                                                    |
| project.”                                          | and domain details are removed during processing   | -   ‘Project search with assignee and overdue      |
|                                                    |                                                    |     filter’                                        |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+

 

## Data we collect and analyze

When the usage patterns setting is enabled, Asana retains the de-identified labels about the type of work performed, along with high-level account details such as plan tier, approximate domain size, and industry. This data is designed to stay general rather than describe a specific customer’s work.

Usage pattern data is de-identified. Asana does not associate the raw text of prompts or responses to the usage patterns data or to a user name, user ID, domain name, or domain ID.  Asana does not use your data   to train AI models, and third-party model providers are prohibited from training on customer data.

### Examples of data collected

+------------------------------------+------------------------------------------------------------------------+------------------------------------------------+
| **Source**                         | **Input Example**                                                      | **Example label(s)**                           |
|                                    |                                                                        |                                                |
|                                    | *The data we transiently process, then discard*                        | *Never tied to an identifiable domain or user* |
+------------------------------------+------------------------------------------------------------------------+------------------------------------------------+
| Search queries                     | The terms you type when searching for tasks or projects in Asana &     | ‘Keyword search’, ‘task filter’                |
|                                    | applied filters                                                        |                                                |
+------------------------------------+------------------------------------------------------------------------+------------------------------------------------+
| AI Teammate instructions           | “Find all tasks assigned to me that are overdue in the Q3 Launch       | ‘search with assignee & overdue filter’        |
|                                    | project”                                                               |                                                |
+------------------------------------+------------------------------------------------------------------------+------------------------------------------------+
| Rule and automation configurations | The conditions and actions you set up in Asana Rules, like “when a     | ‘mark complete when moved to section’          |
|                                    | task is moved to Done, mark it complete”                               |                                                |
+------------------------------------+------------------------------------------------------------------------+------------------------------------------------+
| Project and section names          | Project named “FY ‘25 Product Roadmap”                                 | ‘development planning’                         |
+------------------------------------+------------------------------------------------------------------------+------------------------------------------------+
| Custom field names and types       | Field named “Budget Status”                                            | ‘status’                                       |
+------------------------------------+------------------------------------------------------------------------+------------------------------------------------+
| AI Chat conversations and prompts  | “Summarize the status of this project for my stakeholders”             | ‘project status summary’                       |
+------------------------------------+------------------------------------------------------------------------+------------------------------------------------+

## Manage the setting in the admin console

Admins can manage this setting from the admin console.

1.  Click **Admin console**.
2.  Select **Security**
3.  Scroll down to **Compliance**
4.  Click **Data contributions**
5.  In **Share Usage Patterns**, choose whether to share product usage patterns with Asana, then save your changes

Only organization admins and super admins can access this setting. Only Super Admins can opt-in, both Admins & Super Admins can opt-out. Other members and guests cannot change it.

> The steps above apply to organization admins only. To opt out of data contributions for a division, your admin should contact Asana Support.

## Data contributions setting based on your plan

For Starter and Advanced, sharing usage patterns is on by default, and admins can turn it off. For Enterprise and Enterprise+, the default depends on region. Domains in the EU start with the setting off and can turn it on, while domains outside the EU start with the setting on and can turn it off.

Some plans show the setting in a fixed state. Asana Personal keeps the setting on and does not allow changes. Customers with HIPAA or Asana Gov cannot share usage patterns data through this setting; they are permanently disabled

Starting September 1st, existing customers will see the option to configure their usage patterns data contribution setting in advance of their next renewal. This allows Admins to choose their preferred setting before any data contribution occurs. 

## Frequently asked questions

**General**

- Can I opt out of my data being collected?
  - If you are in Starter or above, you may configure your settings and opt out at any time via the Admin Console by a Super Admin. Following our announcement, you can opt out before your plan renews to ensure your settings will be honored prior to our Data Contributions usage coming into effect.
- Is this data being used to fine-tune a provider model?
  - No. Please see Asana’s [Privacy Statement](https://asana.com/terms/privacy-statement) for more information on how your data is being used.
- What will Asana be able to see about my data when looking at usage patterns?
  - Asana will only be able to see de-identified labels logged separately and independently of any of the Customer Data it was derived from.
  - No connection between the logged labels and Customer Data or user/domain data persists. Asana has a policy to not make any attempt to re-identify the label back to a specific user or domain. 
- What are some examples of how data will be labelled?
  - If a project was called ‘2026 Fall Digital campaign’, we might label it ‘Marketing campaign.’ 
  - If a user asks Dash to ‘Run competitive research between my company and a competitor’, we might label it ‘Competitive Research.’
  - Asana maintains sufficient de-identification standards to ensure labels will not be traced back to any specific Customer Data. Domain and user IDs are removed during processing and re. 
- Who at Asana will be able to see this data?
  - Asana follows internal production access control and access is restricted to authorized Asana personnel who are required to access this data to perform functions as part of the delivery of services. Access is granted based on the principle of least privilege and commensurate with job function.

**Third Parties & Model Providers**

- Is my data sent outside Asana's infrastructure for this analysis? Is the model provider a subprocessor, and is it on your published subprocessor list?
  - Yes, they are sent via API to a third party model provider. Our current model providers are listed as subprocessors on our Subprocessors page at [https://asana.com/terms/subprocessors](https://asana.com/terms/subprocessors). Asana (and its affiliates as applicable) have entered into written agreements with such model providers to ensure there are data protection obligations at least as protective as the technical and organizational measures Asana has put into place to protect customer personal data from accidental or unlawful destruction, loss, alteration, or unauthorized disclosure or access. 
- Does the model provider retain, log, or train on the data we send them?
  - No. Asana has contractual agreements with our model partners that prohibit the use of customer data to train or improve their AI models and services. Visit the trust center for more information: [https://trustcenter.asana.com/](https://trustcenter.asana.com/)

**Opt-Out Settings & Details**

- When is the opt out enforced technically — is data excluded before processing, or filtered after collection?
  - Data is excluded before processing. We do not process data from domains that are opted-out via the Admin Console.
- If we opt-out, will previously collected data be deleted?
  - Previously collected data is not deleted. Because the data is deidentified, Asana is unable to trace or know which logs came from a specific domain. 
- Opt-out is applied domain-wide — can we exclude specific projects, teams, or sensitive workspaces while participating elsewhere?
  - No, this is not currently possible. 
- Can I opt out of data contributions for a division?
  - Opting out of data contributions for a division is not available as a self-serve option. To opt out, your admin should contact Asana Support. Asana will process the request on your behalf.

**Re-identification**

- You retain some information about plan tier, approximate domain size, and industry vertical. For a large or unusual customer, couldn't those attributes plus a distinctive label re-identify us? 
  - The logs we retain are in no way associated with the underlying Customer Data. Asana will have additional measures in place to minimize the ability to re-identify based on distinctive labeling.
- What prevents a rare, org-specific request (e.g., a project named after an unreleased product) from becoming a label that leaks intent?
  - Our teams generally try to create labels that are broad and descriptive in an effort to mitigate the possibility of significant inference of intent or very detailed descriptions of the underlying Customer Data.
