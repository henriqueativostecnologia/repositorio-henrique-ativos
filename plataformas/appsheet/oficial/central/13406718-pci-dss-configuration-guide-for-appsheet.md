---
fonte: https://support.google.com/appsheet/answer/13406718?hl=en
baixado: 2026-11-10
---

# PCI DSS configuration guide for AppSheet

For a customer to be compliant on AppSheet with the **Payment Card Industry Data Security Standard (PCI DSS)**, there are some actions and processes the customer owns under the "Shared Responsibility Model." The following items should be reviewed by customers who are required to be PCI DSS compliant. These items are self-service within AppSheet and need to be addressed for the customer organization (org) to be PCI DSS compliant. The overarching concept is "Google secures the platform, the customer secures their data."

## Customer responsibility

The following table lists the requirements for which the customer has responsibility in order to be PCI DSS compliant. For more information about the requirements, see [PCI DSS Quick Reference Guide](https://www.pcisecuritystandards.org/document_library/#results).

For all other PCI DSS requirements not listed in this table, AppSheet and its production environment comply with the standard.

|                                                                                       |                                                      |
|---------------------------------------------------------------------------------------|------------------------------------------------------|
| **PCI DSS requirement**                                                               | **Section**                                          |
| Requirement 3: Protect stored cardholder data                                         | [Data masking](#data-masking)                        |
| Requirement 3: Protect stored cardholder data                                         | [Data storage](#data-storage)                        |
| Requirement 4: Encrypt transmission of cardholder data across open, public networks   | [Data encryption](#data-encryption)                  |
| Requirement 7: Restrict access to cardholder data by business need to know            | [Use/Authorization](#use-authorizations)s            |
| Requirement 8: Assign a unique ID to each person with computer access                 | [Complex password requirements or OAuth](#password)  |
| Requirement 10: Track and monitor all access to network resources and cardholder data | [Audit trail](#audit-trail)                          |

## Data masking

AppSheet offers the ability to mark certain data in a customer's data store as sensitive, which obscures it in the audit logs. Masking sensitive data is part of [*PCI DSS Requirement 3 - Protect stored cardholder data*](https://www.pcisecuritystandards.org/document_library/#results). Any data subject to PCI DSS processed with an AppSheet app must be marked as sensitive by the customer, as described in [Sensitive Personally Identifiable Information (PII) data policy](https://support.google.com/appsheet/answer/10104377).

## Data storage

AppSheet does not permanently store customer data, instead it is stored in the data source configured and controlled by the customer. Customers should make sure that any data sources used by AppSheet are PCI DSS compliant per [*PCI DSS Requirement 3 - Protect stored cardholder data*](https://www.pcisecuritystandards.org/document_library/#results).

## Data encryption

AppSheet applications can only be accessed over HTTPs which ensures that traffic between the end user and AppSheet is encrypted. Customers are responsible for ensuring that any data sources are configured to use encryption. See [*Using data from MySQL*](https://support.google.com/appsheet/answer/10106676) for details.

## Use/Authorizations

User and policy management is a customer responsibility. Team Root and Admin accounts can create and manage team policies that define access rights for their accounts and applications. Details are provided in [Define governance policies](https://support.google.com/appsheet/answer/11948767).

## Complex password requirements or OAuth

Users authenticate to AppSheet apps using OAuth via an identity provider. Customers should make sure that their identity provider is PCI DSS compliant, and that the AppSheet application is restricted to only allow access to signed-in users, as described in [*Require sign-in: The Essentials*](https://support.google.com/appsheet/answer/10104975). ([*PCI DSS Requirement 8: Assign a unique ID to each person with computer access*](https://www.pcisecuritystandards.org/document_library/#results)}

## Audit trail

Customers have the ability to review the audit trail of all administrative activities performed within the customer's org, including the use of Trace. Detailed instructions are provided in [Monitor app activity using Audit History](https://support.google.com/appsheet/answer/10104794). ([*PCI DSS Requirement 10: Track and monitor all access to network resources and cardholder data*](https://www.pcisecuritystandards.org/document_library/#results))
