---
fonte: https://help.asana.com/s/article/data-residency-for-asana?language=en_US
baixado: 2026-11-10
---

# Data Residency for Asana

Data residency for Asana allows global teams to choose the region where certain types of data at rest are stored. Data Residency, coupled with [Asana’s Privacy Commitment](https://asana.com/terms/privacy-commitment) ensures your data is stored and used only in the ways our customers require.

**Who can use this feature?**

Data residency is available to be purchased as an add-on in [Enterprise organizations](https://asana.com/enterprise) and divisions and is included in [Enterprise+](https://asana.com/enterprise) tiers. [Super admins ](https://help.asana.com/s/article/admin-and-super-admin-roles-in-asana?language=en_US)can enable data residency for an organization.

**What you need to know about data residency:**

- Customers must store all Asana data in a single region
- For data residency access, paid plan customers must upgrade to an [Enterprise organization](https://asana.com/enterprise) plan or [Enterprise+](https://asana.com/enterprise).
- Contact our [Sales team](https://asana.com/sales) to set up data residency for your organization.

## Where data residency for Asana is available

Asana partners with Amazon Web Services to deliver in-region storage with high reliability and performance. With access to a regional data center, customers can more easily adhere to both internal data policies as well as evolving government and third-party regulations favoring data residency requirements.

Check out the table below, to see where data residency is available and the corresponding backup regions.

|                                       |                               |
|:-------------------------------------:|:-----------------------------:|
|       **Data residency region**       |    **Data backup region**     |
| Virginia**, **United States (default) | Ohio, United States (default) |
|          Frankfurt, Germany           |        Dublin, Ireland        |
|             Tokyo, Japan              |         Osaka, Japan          |
|           Sydney, Australia           |     Melbourne, Australia      |

## How data residency for Asana works

### Data stored in the data region

The following categories of customer data will be stored at rest in a data center within the customer’s selected region as of the date data residency is enabled:

- Customer data: including teams, projects, tasks, domain & CSV exports, and attachments.
- User-generated content included in a user's first project
- User profile data: user name, profile photo, and locale

### Data stored outside the data region

The following categories of data may be stored outside of the customer’s data region:

- User authentication: e-mail addresses, passwords (guests), one-time keys (e.g. password reset links, signup/invite links), IP addresses, random identifier
- Data used to measure seat count, usage, and revenue

### Data shared with AI Partners for LLM Processing

Asana AI’s partner-powered features share relevant customer data with our AI partners. Our AI partners’ servers are generally located in the United States but customers who have chosen the European Union for their Data Residency settings will have their data processed on servers located in the EU.

**Note**: The data residency feature does not change any aspects of Asana other than the data at rest storage location in Amazon Web Services. Asana will continue to store and process all categories of data in the United States and other international locations in accordance with [Asana's Privacy Statement](https://asana.com/terms/privacy-statement), and where applicable, the Data Processing Addendum entered into with Asana**. **For more information on where information is stored and processed via our subprocessors or Asana affiliates, please see our [Subprocessors and Affiliate page](https://asana.com/terms/subprocessors).

## Regional AI processing availability

Asana AI's regional data processing is currently available only for customers with **Regional Data Residency enabled in the EU**. For these customers:

1.  User-Generated Content processed by AI features remains on servers within the EU region
2.  AI features automatically disable if the underlying Large Language Model (LLM) is not available on EU-based servers

**For customers with Regional Data Residency in other regions** (e.g., Australia, Japan, Middle East):

1.  Customer Data remains stored in your selected regional datacenter
2.  AI feature requests are processed in the US, as regional AI processing endpoints are not yet available in these regions

**EU-Specific Feature Limitations:**

The following Anthropic features are currently unavailable for EU customers with regional AI processing due to AWS Bedrock hosting limitations:

1.  Anthropic web search capabilities
2.  Features that depend on Agent Skills, including AI Teammates Microsoft Office document editing

Customers can contact their account team to discuss options if full AI feature access is required.

## Data migration

By default, data will continue to reside in the United States for new workspaces and existing customer data. Customers must contact our [Sales team](https://asana.com/sales) to opt-in for data residency to migrate their organization to their selected data region.

### How does Asana approach privacy and security?

Asana adheres to global privacy laws and security standards. For more information about Trust at Asana please click [here](https://asana.com/trust). Customer data is [encrypted](https://security.asana.com/?itemUid=ef061e5b-a2f4-469e-92bc-ab973e3d7842&source=search) at rest and in transit, and protected with [cross-regional backups](https://security.asana.com/?itemUid=b05bcec1-da7e-4885-9603-a39fd73a1cdc&source=title).

### Enterprise Key Management

New and existing [Enterprise Key Management (EKM)](https://help.asana.com/s/article/enterprise-key-management-ekm?language=en_US) customers can choose to create and store their encryption keys in a specific data region with data residency.

### Multi Orgs

New and existing customers needing more than one data residency region to support their multi-geo compliance needs can opt-in to [multi-org](https://help.asana.com/s/article/multi-org-deployment?language=en_US) deployment & get multi-geo data residency allowing them to keep their data distinct.

### Network and Data Flow Diagrams

See [Asana’s Trust Center](https://security.asana.com/?itemUid=eecad1f5-1070-455d-b87e-9db1fc732d2b&source=title) for a high-level data flow diagram and detailed network diagram.

### Ready to get started?

Reach out to our [Sales team](https://asana.com/sales) today.

[ ](https://forum.asana.com/c/forum-en/tips/6)
