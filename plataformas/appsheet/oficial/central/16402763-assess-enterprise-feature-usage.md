---
fonte: https://support.google.com/appsheet/answer/16402763?hl=en
baixado: 2026-11-10
---

# Assess enterprise feature usage

As a team admin, you can generate a report of apps that use enterprise features by using a custom policy. Configure the policy by setting the component and condition, as described in the following sections. The policy preview will display a list of apps that are compliant and non-compliant. Apps that are non-compliant will include those that are using enterprise features. You can download a CSV file that lists the apps and app owners that are using the enterprise features. See [Review policy compliance](https://support.google.com/appsheet/answer/11948767#policy-compliance).

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Check for enterprise feature usage**\                                       | **Export the list of apps and app owners**\                                   |
| \                                                                             | \                                                                             |
| Custom policy for enterprise feature usage                                    | Enterprise feature usage report                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

It is not necessary or recommended to save the policy until you intend to block the non-compliant apps. Once saved, you might change the severity of the policy to “Warning” to notify app creators that they are using enterprise features. 

**The ONLY factor that determines the license required by an app user is the app owner’s license. This procedure is only relevant to determine if downgrading an app owner from Enterprise Plus to Core will result in an app error.**

The following lists the **verifiable enterprise features**, described in the following sections:

1.  [Cloud data sources](#cloud-data-source)
2.  [Authentication domains](#authentication-domains)
3.  [Cloud object stores](#cloud-object-stores)
4.  [Team-shared apps](#team-shared-apps)
5.  [Data source partitioning](#data-source-partioning)
6.  [Stable version/app versioning](#stable-version-app-versioning)
7.  [AppSheet API](#appsheet-api)
8.  [AI tasks](#ai-tasks)
9.  [OCR and predictive models](#ocr-predictive-models)

**Note**: Governance features like policies and team settings, while not included in the list above, are only available to users with an enterprise license.

## Cloud data sources

This feature allows app creators to access enterprise data sources (such as, SQLServer, BigQuery, and so on). See [Manage data sources](https://support.google.com/appsheet/answer/10106309).

To check for usage of this feature, configure the custom policy as follows:

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Component**                                                                 | **Condition**                                                                 |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Tables                                                                        | `AND(NOT(IN([ProviderName], LIST(`\                                           |
|                                                                               | `"big_query",`\                                                               |
|                                                                               | `"database",`\                                                                |
|                                                                               | `"data_studio",`\                                                             |
|                                                                               | `"salesforce",`\                                                              |
|                                                                               | `"sqlserver",`\                                                               |
|                                                                               | `"mysql",`\                                                                   |
|                                                                               | `"postgres",`\                                                                |
|                                                                               | `"redshift",`\                                                                |
|                                                                               | `"mariadb",`\                                                                 |
|                                                                               | `"odata",`\                                                                   |
|                                                                               | `"oracle",`\                                                                  |
|                                                                               | `"apigee_api",`\                                                              |
|                                                                               | `"dynamo_db",`\                                                               |
|                                                                               | `"aws_cognito_domain",`\                                                      |
|                                                                               | `"okta_domain",`\                                                             |
|                                                                               | `"openid_connect",`\                                                          |
|                                                                               | `"integration_connector"`\                                                    |
|                                                                               | `))),`\                                                                       |
|                                                                               | `NOT(STARTSWITH([ProviderName], "integration_connector")))`                   |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

## Authentication domains

This feature allows app creators to limit sharing of their apps to groups of users (such as, Google Groups, Microsoft Groups, and so on). See [Domain integration: The Essentials](https://support.google.com/appsheet/answer/10105757).

To check for usage of this feature, configure the custom policy as follows:

|               |                               |
|---------------|-------------------------------|
| **Component** | **Condition**                 |
| Security      | `[DomainAuthRequired] = "No"` |

## Cloud object stores

This feature allows app creators to specify a cloud container store for image and file capture. By default, images and files captured by the app are stored in the cloud file system associated with the app owner's account. The creator can explicitly add an object store and use that instead. See [Understand cloud object stores](https://support.google.com/appsheet/answer/10106769).

To check for usage of this feature, configure the custom policy as follows:

|               |                                   |
|---------------|-----------------------------------|
| **Component** | **Condition**                     |
| `Tables`      | `[CloudObjectStore] = "_Default"` |

 

## Team-shared apps

This feature allows app creators to define their app as a sample app that other members of their team can copy and build upon. See [Share resources with your team](https://support.google.com/appsheet/answer/10104795).

To check for usage of this feature, configure the custom policy as follows:

|               |                         |
|---------------|-------------------------|
| **Component** | **Condition**           |
| `AppSettings` | `[IsTeamPublic] = "No"` |

 

## Data source partitioning

This feature allows app creators to partition (or divide) the rows of the table into many table sources to make their apps more scalable. See [Scale using data partitions](https://support.google.com/appsheet/answer/10105383).

To check for usage of this feature, configure the custom policy as follows:

|               |                                 |
|---------------|---------------------------------|
| **Component** | **Condition**                   |
| `Tables`      | `[EnablePartitioning] = "No"`   |

## Stable version/app versioning

This feature allows app creators to set a specific stable version of their app for active users while they develop newer versions. See [Maintain a stable version of the app](https://support.google.com/appsheet/answer/10104791).

To check for usage of this feature, configure the custom policy as follows:

|               |                              |
|---------------|------------------------------|
| **Component** | **Condition**                |
| `AppSettings` | `LEN([StableVersion]) = 0`   |

## AppSheet API

This feature allows app creators to allow cloud-based services (such as, Looker Studio and Zapier) to communicate with their app. See [Enable the API for cloud-based service communication](https://support.google.com/appsheet/answer/10105769).

The AppSheet API can only be detected using the pre-built policy "Disable external integration through app API".  See [Prevent app creators from enabling the API](https://support.google.com/appsheet/answer/10105769#prevent-enabling-api).

## AI tasks

This feature allows app creators to use AI in automations to extract information from an image, PDF document, or text; and categorize information. See [Overview of AI in automations](https://support.google.com/appsheet/answer/16045284).

AI tasks can only be detected using the pre-built policy “Disable Gemini in AppSheet Solutions (AI Tasks)". See [Control which app creators can use AI in automations](https://support.google.com/appsheet/answer/16052764).

## Optical Character Recognition (OCR) and predictive models

This feature allows creators to leverage OCR to access the text or writing that appears in an image. Predictive models can also be used to perform a statistical analysis of app data in order to make predictions about future data. See [Optical Character Recognition (OCR)](https://support.google.com/appsheet/answer/10104799).

To check for usage of this feature, configure the custom policy as follows:

|                    |                                                                     |
|--------------------|---------------------------------------------------------------------|
| **Component**      | **Condition**                                                       |
| `BehaviorSettings` | `AND(COUNT([AppPredictiveModels]) = 0, COUNT([AppOcrModels]) = 0)`  |
