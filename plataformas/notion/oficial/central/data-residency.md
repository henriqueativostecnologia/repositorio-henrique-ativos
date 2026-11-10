---
fonte: https://www.notion.com/help/data-residency
baixado: 2026-11-10
---

# Data residency for Notion

In this help doc

## Learn about Notion’s data residency offering.

[Jump to FAQs](https://www.notion.com/help/data-residency#faq)

------------------------------------------------------------------------

Data residency, along with [Notion's security practices](https://www.notion.so/security), ensures that your data is stored and used only in the ways you require. With this update, eligible workspace owners will be able to choose whether to store their data at rest in their specified data region.

## [Who can use this feature?](https://www.notion.com/help/data-residency#who-can-use-this-feature)

If you’re on an Enterprise Plan, you can request to move existing workspace data to your selected data region. If you work with a Notion account team, contact them to set up data residency migration for an existing workspace.

If you don’t work with an account team, contact Notion support ([\[email protected\]](/cdn-cgi/l/email-protection#621607030f220f0309070c0d160b0d0c4c010d0f)) to check whether your workspace is eligible for migration. Until you contact Notion and receive confirmation that migration is complete, your workspace data will remain hosted in the United States.

## [How does data residency work?](https://www.notion.com/help/data-residency#how-does-data-residency-work)

Notion partners with Amazon Web Services to deliver reliable, high-performance data storage through regional data centers.

[TABLE]

*\* Please contact your account team for more information about Notion’s hosting in Japan and Korea.*

## [Data stored in the data region](https://www.notion.com/help/data-residency#data-stored-in-the-data-region)

The following categories of Customer Data (as defined in Notion's [Master Subscription Agreement](https://www.notion.so/Master-Subscription-Agreement-4e1c5dd3e3de45dfa4a8ed60f1a43da0)) will be stored at rest in a data center within the customer’s selected region as of the date that data residency is enabled:

- Page content

- Files (such as images and documents) uploaded to Notion

- Search index of Customer Data

- Third-party or bot-generated messages and files that are stored in Notion

## [Data stored outside the data region](https://www.notion.com/help/data-residency#data-stored-outside-the-data-region)

Unless listed above as [data stored in the data region](https://www.notion.com/help/data-residency?_ck=bb12d75484663688acf8eaa43caa0f1ee40c3dfc789d795e8f79c7e9ef8fcfc6#data-stored-in-the-data-region), data may be stored in regions outside of the customer’s data region. Examples:

- Account Information (as defined in Notion's [Master Subscription Agreement](https://www.notion.so/Master-Subscription-Agreement-4e1c5dd3e3de45dfa4a8ed60f1a43da0)).

- Usage Data (as defined in Notion's [Master Subscription Agreement](https://www.notion.so/Master-Subscription-Agreement-4e1c5dd3e3de45dfa4a8ed60f1a43da0)).

- Data processed by [Notion’s subprocessors](https://www.notion.so/notion/Notion-s-List-of-Subprocessors-268fa5bcfa0f46b6bc29436b21676734).

Notion Calendar and Notion Mail, any Notion Calendar and Notion Mail features, and any Beta Services are not covered by data residency.

**Note**: The data residency feature only changes the data at rest storage location for the categories of Customer Data described above stored by Notion in Amazon Web Services — no other aspects of Notion are affected. This commitment does not extend to any non-Notion Services. Notion will continue to store and process all categories of data in the United States and other international locations in accordance with Notion's Privacy Policy and, where applicable, the Data Processing Addendum. For more information on where information is stored and processed via our subprocessors or Notion affiliates, please see our [Subprocessors page](https://www.notion.so/notion/Notion-s-List-of-Subprocessors-268fa5bcfa0f46b6bc29436b21676734).

## [Data migration](https://www.notion.com/help/data-residency#data-migration)

To migrate an existing workspace, contact your Notion account team or Notion support ([\[email protected\]](/cdn-cgi/l/email-protection)). Notion will confirm whether your workspace is eligible and help you understand the next steps.

By default, your data will continue to reside in the United States. To migrate your organization's data to a data region, please contact your account team. Once the workspace is migrated, the categories of Customer Data described above will be deleted in the US after 30 days.

Enterprise organizations can specify a default region for newly created workspaces by going to your organization settings → `Data & Compliance` → `Data Residency`. Setting the region to Europe will prevent needing to migrate net new workspaces.

------------------------------------------------------------------------

## FAQs

What is the cost of enabling data residency?

Data residency is available free of charge to customers on the Enterprise Plan.

What products are not covered by data residency?

Notion Calendar and Notion Mail, any Notion Calendar and Notion Mail features, and any Beta Services are not covered by data residency.

Is Customer Data stored in the data region when using Notion AI?

The categories of Customer Data described above are stored in the data region with the data residency feature. The large language model (LLM) providers we use to provide Notion AI utilize zero data retention for Enterprise Plan workspaces, so no data is stored with LLM providers. See [here](https://www.notion.com/help/notion-ai-security-practices) for more information on Notion AI security and privacy practices.

How does Notion handle backups?

Notion’s backups are stored within the same region as production in the data region. Notion is hosted by AWS and stores Customer Data using a combination of databases. By default, AWS provides durable infrastructure to store important data and is designed for durability of 99.9% of objects. Automated backups of all customer and system data is enabled, and data is backed up daily at minimum. The backups are encrypted in the same way as live production data, and are monitored and alerted.

Will integrations still be available?

Yes, previously enabled apps will remain enabled. Admins can choose to disable the addition of new integrations that are not allowlisted. Data that is hosted or processed by integrations and non-Notion Services are outside the scope of Notion’s data residency offering.

My company isn’t based in the data region. Can I still have my data hosted there?

Yes, customers on our Enterprise Plan can contact their account team to migrate an existing workspace to the data region and have their data hosted there.

When is Customer Data processed outside the data region?

The data residency feature only changes the data at rest storage location for the categories of Customer Data described above that are stored by Notion in Amazon Web Services.

Processing of Customer Data outside the data region can include:

- Customer Data processed by Notion [subprocessors](https://notion.notion.site/Notion-s-List-of-Subprocessors-268fa5bcfa0f46b6bc29436b21676734), including LLM providers

- [Duplicating content](https://www.notion.com/help/transfer-content-to-another-account) from other workspaces such as downloading templates and moving content from a US workspace to a data region workspace

- If a [synced block’s](https://www.notion.com/help/synced-blocks) source is a different data region hosted workspace

## Contents

- [Who can use this feature?](#who-can-use-this-feature)
- [How does data residency work?](#how-does-data-residency-work)
- [Data stored in the data region](#data-stored-in-the-data-region)
- [Data stored outside the data region](#data-stored-outside-the-data-region)
- [Data migration](#data-migration)
