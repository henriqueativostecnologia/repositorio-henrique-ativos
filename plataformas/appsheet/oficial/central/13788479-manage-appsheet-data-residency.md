---
fonte: https://support.google.com/appsheet/answer/13788479?hl=en
baixado: 2026-11-10
---

# Manage AppSheet data residency

This feature is available to Google Workspace organizations that have AppSheet Enterprise Plus accounts only.

Learn how to manage data residency for your AppSheet apps.

- [What is AppSheet data residency?](#what-is-data-residency)
- [What data is stored in a specific region?](#data)
- [What are the limitations when using a specific region?](#limitations)
- [Before you begin: Consider tradeoffs](#tradeoffs)
- [Enable regions on your Enterprise Plus account](#enable-eu-region)
- [Select the region to use for your apps](#select-region)
- [Copy an app between regions](#copy-apps-region)
- [Manage IP addresses and firewall information for a specific region](#manage-ip)

## What is AppSheet data residency?

Your AppSheet app data is subject to the laws of the country in which it is stored and data privacy and security protections can vary by region. To help you meet data residency requirements, AppSheet gives you the ability to control the geographical area, or "region", in which your data is stored and processed. 

Today, you can choose to store your AppSheet app data in the following regions:

+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **Region**                                         | **Description**                                    | **AppSheet URL**                                   |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **Asia Pacific**                                   | Data is stored and processed in Asia Pacific       | `asia-southeast.appsheet.com`                      |
|                                                    | region only.                                       |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **European Union (EU)**                            | Data is stored and processed in EU region          | `eu.appsheet.com`                                  |
|                                                    | only. This helps customers by supporting           |                                                    |
|                                                    | compliance with the [General Data Protection       |                                                    |
|                                                    | Regulation (GDPR)](https://gdpr-info.eu/) data     |                                                    |
|                                                    | protection requirements.                           |                                                    |
|                                                    |                                                    |                                                    |
|                                                    | See also:                                          |                                                    |
|                                                    |                                                    |                                                    |
|                                                    | -   [What data is stored in a specific             |                                                    |
|                                                    |     region?](#data)                                |                                                    |
|                                                    | -   [Which data sources are supported in a         |                                                    |
|                                                    |     specific region?](#data-sources)               |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **Global (All regions)**                           | Data storage is not restricted. This is the        | `appsheet.com`                                     |
|                                                    | default.                                           |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+

## What data is stored in a specific region?

The data that is stored in the Asia Pacific or EU region includes (but is not limited to):

- App definitions
- Data source configurations and access tokens
- Customer data in AppSheet databases
- Audit logs
- Backups (described below)

### Backups

AppSheet maintains backups of primary data for disaster recovery and business continuity. In rare cases, AppSheet uses backups to restore data and maintain high [reliability](https://support.google.com/googlecloud/answer/6056635).

These backups aren’t available to restore data upon customer request. Backups expire (are overwritten) on defined timelines.

## What are the limitations when using a specific region?

The following lists the limitations when using a specific region:

- Gemini for App Creation is supported in the Global region only; it is not supported in the Asia Pacific or EU region. Gemini for AppSheet Solutions is supported in the Global and EU regions; it is not supported in the Asia Pacific region at this time.
- The following [*data sources*](https://support.google.com/appsheet/answer/10106309) are not supported in the Asia Pacific or EU region:
  - Box
  - Dropbox
  - Microsoft Excel
  - Salesforce
- Only Google providers are supported to authenticate AppSheet sign-ins in the Asia Pacific (Preview) or EU region. See [Require sign-in: The Essentials](https://support.google.com/appsheet/answer/10104975). 

## Before you begin: Consider tradeoffs

Selecting a specific region doesn't provide performance improvements or fine-tuning for your network or data access. Take the following factors into consideration before selecting your region:

- Users outside of the region where their data is located might experience higher latency in some cases. Latency could happen while:

  - Editing shared objects in real time across regions
  - Sharing files, such as documents, with someone outside the user's region
  - Traveling internationally

- In rare cases, when a data region has been selected users outside that region might lose access to the data due to events beyond Google’s control (for example, natural disasters).

- If there are apps in multiple regions that share the same data source, your users may be more likely to run into concurrency issues, as described in [Concurrent usage with multiple users](https://support.google.com/appsheet/answer/10104702?). AppSheet currently recommends that you avoid sharing data sources across regions if possible. 

## Enable a specific region on your Enterprise Plus account

To enable a specific region, such as EU, for data residency on your Enterprise Plus account, complete the [AppSheet region request form](https://goo.gle/4i3bVIw).

If required by your organization, you can support multiple regions for the same Enterprise Plus account. Then, you can optionally allow app creators to [*select the region for their apps*](#choose-region) or enforce the use of one region. 

## Select the region to use for your apps

If multiple regions are supported for your Enterprise plus account and your company doesn't enforce the use of one region, you can select the region based on the URL you use to access AppSheet:

- `asia-southeast.appsheet.com`: View and create apps in the Asia Pacific region. 
- `eu.appsheet.com`: View and create apps in the EU region. 
- `appsheet.com`: View and create apps in the Global region. 

Only apps created in the selected region are displayed and accessible from the My Apps page.

If you are using OpenID Connect, you need to update the callback URL to use the Asia Pacific or EU region. See [Control user access using OpenID Connect](https://support.google.com/appsheet/answer/10105083).

## Copy an app between regions

When copying an app between regions, only the app definition is copied, not its data source or file data. As a result, you might need to configure the same data source in the target region; this only needs to be done once per data source, not once per app. If you need to copy an AppSheet database to a new region, contact [AppSheet Support](https://www.appsheet.com/support) for assistance.

To copy an app between regions, perform the following steps:

1.   Sign in to [AppSheet](https://www.appsheet.com).
2.  Open the app in the editor and select **Manage \> Collaborate & Publish \> Copy App**.
    We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
    You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

    ## If you are using the legacy editor

    Open the app in the editor, select **Manage \> Author**, and click **Copy App**. 
3.  In the Copy your app dialog, click **Copy to region**.
4.  In the **App name** field, edit the name of the app, if desired.
5.  In the **Region** list, select the region to copy the app to (such as `https://eu.appsheet.com`).
6.  Click **Copy**.

## Manage IP addresses and firewall information for a specific region

If you are managing network traffic within your organization, or if you need to request AppSheet traffic be added to your allow list, use the AppSheet IP addresses for the specific data residency region, as described in [*Manage IP addresses and firewall information*](https://support.google.com/appsheet/answer/10104492).
