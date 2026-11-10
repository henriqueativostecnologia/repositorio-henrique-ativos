---
fonte: https://help.asana.com/s/article/fedramp-compliance?language=en_US
baixado: 2026-11-10
---

# FedRAMP Compliance

## What is FedRAMP?

The Federal Risk and Authorization Management Program (FedRAMP) is a U.S. government-wide program that provides a standardized approach to security assessment, authorization, and continuous monitoring for cloud products and services.

The core goals of FedRAMP are to:

- Standardize security requirements for cloud services across federal agencies
- Reduce duplication of security assessments and authorizations
- Ensure consistent application of NIST standards across cloud products
- Improve security posture of government-used cloud services through continuous monitoring

## Asana Gov shared responsibility model 

Asana Gov operates under a shared responsibility model driven by FedRAMP Moderate. This means some security and compliance controls are managed by Asana, some by the customer, and some are shared between Asana and the customer.

For a comprehensive list of FedRAMP Moderate Controls, visit [fedramp.gov](http://fedramp.gov/). The content on this page is a modified version of the Asana Gov FedRAMP Customer Responsibilities Matrix (CRM). Federal agencies can request a copy of Asana Gov’s SSP and other relevant security documentation, including Asana Gov’s detailed CRM, via the [FedRAMP Marketplace](https://marketplace.fedramp.gov/products). For non-agency Asana Gov customers to request access to the CRM, contact [](https://gcs.atlassian-us-gov-mod.net/servicedesk/customer/user/login?destination=portals) Asana support.

Each table outlines relevant FedRAMP control families and notes where Asana may share responsibility with our customers. For controls with customer responsibility, you will find details and links to documentation. Content in this table may be modified to reflect the latest updates with applicable controls.

 

+------------------------------------------------------------------------------------------------------------------------+-------------------------------------+
| **Access Control (AC) Control Family**                                                                                 | Relevant NIST 800-53 Controls       |
+------------------------------------------------------------------------------------------------------------------------+-------------------------------------+
| **Asana Responsibility:**                                                                                              | AC-05, AC-06, AC-08                 |
|                                                                                                                        |                                     |
| We provide platform controls via admin console, SAML single-sign on integration, and audit logs to our customers.      |                                     |
|                                                                                                                        |                                     |
| Provides system use notification                                                                                       |                                     |
+------------------------------------------------------------------------------------------------------------------------+-------------------------------------+
| **Customer Responsibility**:                                                                                           |                                     |
|                                                                                                                        |                                     |
| Manage access permissions for users, 3P providers, and partners in the following ways:                                 |                                     |
|                                                                                                                        |                                     |
| -   Manage access via customer-defined groups with specific permissions                                                |                                     |
| -   Give users access permissions based on valid authorizations and intended usage.                                    |                                     |
| -   Using our audit log API set up necessary measures to be notified when account changes take place                   |                                     |
| -   Modify, disable, and remove accounts based on terminated and transferred users.                                    |                                     |
| -   Conduct annual reviews of user accounts.                                                                           |                                     |
| -   Establish processes for reissuing credentials.                                                                     |                                     |
+------------------------------------------------------------------------------------------------------------------------+-------------------------------------+
| Manage individual user accounts in the following ways:                                                                 |                                     |
|                                                                                                                        |                                     |
| -   Grant user accounts permission based on their roles.                                                               |                                     |
| -   Configure your identity provider to Asana Gov                                                                      |                                     |
| -   Monitor new, reactivated, disabled, and removed user accounts.                                                     |                                     |
| -   Monitor account usage and establish processes for reporting incidents.                                             |                                     |
| -   Disable user accounts of individuals posing significant risks within one hour.                                     |                                     |
|                                                                                                                        |                                     |
| Admins have specific privileges that are restricted to admins. Super admins have specific privileges that are          |                                     |
| restricted to super admins. Customers are responsible for determining who these are.                                   |                                     |
+------------------------------------------------------------------------------------------------------------------------+-------------------------------------+
| **Customer Responsibility:**                                                                                           |                                     |
|                                                                                                                        |                                     |
| -   All integrations and Personal Access Tokens (PATs) are disabled by default. Customers are responsible for          |                                     |
|     reviewing and adjusting these settings to meet their needs.                                                        |                                     |
| -   Customers are solely responsible for reviewing the security of any third party integrations on their own           |                                     |
| -   Asana Intelligence and Machine Learning features will be disabled & it up to super admins to enable these features |                                     |
|     for their domain                                                                                                   |                                     |
| -   We have a default timeout set for FedRAMP domains (8 hours)                                                        |                                     |
| -   Private by default - All projects, portfolios, teams, and goals                                                    |                                     |
+------------------------------------------------------------------------------------------------------------------------+-------------------------------------+

+------------------------------------------------------------------------------------------------------------------------+-------------------------------------+
| **Audit & Accountability (AU) Control Family**                                                                         | Relevant NIST 800-53 Controls       |
+------------------------------------------------------------------------------------------------------------------------+-------------------------------------+
| **Asana Responsibility:**                                                                                              | **AU-02, AU-03, AU-04, AU-07,       |
|                                                                                                                        | AU-09, AU-11**                      |
| We provide audit logs with apps and administration activities. Refer to Asanas [Audit Log API                          |                                     |
| documentation ](https://developers.asana.com/reference/audit-log-api)                                                  |                                     |
+------------------------------------------------------------------------------------------------------------------------+-------------------------------------+
| **Customer Responsibility:**                                                                                           |                                     |
|                                                                                                                        |                                     |
| Customers are responsible for monitoring their organization’s data deletions, data access, data changes, permission    |                                     |
| changes, and admin activities.                                                                                         |                                     |
+------------------------------------------------------------------------------------------------------------------------+-------------------------------------+

 

+-----------------------------------------------------------------------------------------------------------------------+-------------------------------------+
| **Identification & Authentication (IA) Control Family**                                                               | Relevant NIST 800-53 Controls       |
+-----------------------------------------------------------------------------------------------------------------------+-------------------------------------+
| **Asana Responsibility:**                                                                                             | IA-08, IA-08(01) , IA-11, IA-05(01) |
|                                                                                                                       |                                     |
| We provide SAML single sign-on configuration.                                                                         |                                     |
+-----------------------------------------------------------------------------------------------------------------------+-------------------------------------+
| **Customer Responsibility: **                                                                                         |                                     |
|                                                                                                                       |                                     |
| Customers are responsible to integrate with their identity provider & enable respective functions                     |                                     |
+-----------------------------------------------------------------------------------------------------------------------+-------------------------------------+
| **Password policy in Asana gov complies with NIST 800-63b :**                                                         |                                     |
|                                                                                                                       |                                     |
| -   Verify that users don’t use commonly used, expected, or compromised passwords.                                    |                                     |
| -   Store only encrypted authenticators in your identity provider.                                                    |                                     |
| -   Require a user with a recovered account to create a new password.                                                 |                                     |
| -   Allow users to select long passwords and passphrases with spaces and special characters.                          |                                     |
+-----------------------------------------------------------------------------------------------------------------------+-------------------------------------+
| Customers are responsible for configuring their identity provider to re-authenticate users in accordance with their   |                                     |
| own requirements.                                                                                                     |                                     |
+-----------------------------------------------------------------------------------------------------------------------+-------------------------------------+
| Guest users in Asana gov domain:                                                                                      |                                     |
|                                                                                                                       |                                     |
| -   Guest users will be required to login using magic links                                                           |                                     |
|     -   Guest-only users will be required to log in using magic link, links expire in 15 minutes and are single-use   |                                     |
|         only on Asana Gov. Reach out to customer support to change the expiry duration.                               |                                     |
|     -   **Guest invites** control will be set to **Admins only** by default in Asana Gov.                             |                                     |
| -   2FA will be required for all domain members and guests by default.                                                |                                     |
+-----------------------------------------------------------------------------------------------------------------------+-------------------------------------+
| **Refer to our documentation for more information:**                                                                  |                                     |
|                                                                                                                       |                                     |
| -   Configure SAML single sign-on (reach out to customer support)                                                     |                                     |
| -   [Understand user                                                                                                  |                                     |
|     provisioning](https://help.asana.com/s/article/provisioning-and-deprovisioning-users-with-scim?language=en_US)    |                                     |
| -   [Understand Asana Password                                                                                        |                                     |
|     Policy](https://h                                                                                                 |                                     |
| elp.asana.com/s/article/managing-password-settings-in-the-admin-console?language=en_US#h_01HEJ6HNW2RXSV4ENZNK83NDNS)  |                                     |
+-----------------------------------------------------------------------------------------------------------------------+-------------------------------------+

Federal agencies can request a copy of Asana Gov’s SSP and other relevant security documentation via the [FedRAMP Marketplace](https://marketplace.fedramp.gov/products).  For non-agency Asana Gov customers to request access to the CRM, contact [](https://gcs.atlassian-us-gov-mod.net/servicedesk/customer/user/login?destination=portals) Asana support.

## Additional resources

- [Asana Trust Center](https://security.asana.com/)
- [FedRAMP Marketplace Listing](https://marketplace.fedramp.gov/products/FR2527132001)
- 🌐 [Asana Gov Marketing Page](http://asana.com/product/asana-gov) 
- 💬 [Contact Sales](http://asana.com/product/asana-gov#form)
