---
fonte: https://support.google.com/appsheet/answer/13390789?hl=en
baixado: 2026-11-10
---

# Predefined policy templates

You can create policies to control the behavior of almost every aspect of the creation, management, and distribution of AppSheet apps.

When defining an app policy, you have two options: 

1.  Use a predefined policy template. See [Add a predefined policy](https://support.google.com/appsheet/answer/11948767#add-predefined-policy).
2.  Write your own custom policy from scratch. See [Add a custom policy](https://support.google.com/appsheet/answer/11948767#add-custom-policy).

Using a predefined template can help you to get a configured policy running quickly. You can also use a template as a starting point for writing your own customized version of a policy.

To write your own, more complex policies, you may want to create your own custom policy from scratch.

## App policy templates

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Template name**                                                             | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Acceptable image resolution                                                   | Requires that images captured in apps meet a minimum specified resolution.    |
|                                                                               | See also [Control image                                                       |
|                                                                               | size](https://support.google.com/appsheet/answer/10106529#control-image-).    |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Apps must have documentation                                                  | Requires that apps include documentation before they can be deployed.         |
|                                                                               | See [App                                                                      |
|                                                                               | documentati                                                                   |
|                                                                               | on](https://support.google.com/appsheet/answer/10106613#app-documentation) on |
|                                                                               | the About page.                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Disable AppSheet databases                                                    | Prevents use of AppSheet databases, as follows:                               |
|                                                                               |                                                                               |
|                                                                               | -   App creators are restricted from including AppSheet database tables in    |
|                                                                               |     their apps                                                                |
|                                                                               | -   End users are restricted from using apps that are built with AppSheet     |
|                                                                               |     databases                                                                 |
|                                                                               |                                                                               |
|                                                                               | See [Disable AppSheet                                                         |
|                                                                               | databases](https://support.google.com/appsheet/answer/12629371).              |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Disable Chat apps                                                             | Prevents app creators from enabling their AppSheet apps to run as Chat        |
|                                                                               | apps. See [Prevent app creators from enabling Chat apps with                  |
|                                                                               | AppS                                                                          |
|                                                                               | heet](https://support.google.com/appsheet/answer/13198694#prevent-chat-apps). |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Disable external integration through app API                                  | Prevents app creators from setting up API-based integration with external     |
|                                                                               | cloud services that send data to an app.                                      |
|                                                                               |                                                                               |
|                                                                               | Enabling this policy disables use of the AppSheet API. See [Prevent app       |
|                                                                               | creators from enabling the                                                    |
|                                                                               | AP                                                                            |
|                                                                               | I](https://support.google.com/appsheet/answer/10105769#prevent-enabling-api). |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Disable Gemini in AppSheet Solutions                                          | Prevent app creators from using AI in automations. See [Control which app     |
|                                                                               | creators can use AI in                                                        |
|                                                                               | automations](https://support.google.com/appsheet/answer/16052764).            |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Disable Google Forms Event                                                    | Prevents app creators from [building an automation using Google               |
|                                                                               | Forms.](https://support.google.com/appsheet/answer/14634161)                  |
|                                                                               |                                                                               |
|                                                                               | See [Prevent app creators from using Google                                   |
|                                                                               | Forms](https://support.google.com/appsheet/answer/14836137).                  |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Disable Google Forms Table                                                    | Prevents app creators from [creating an app using Google                      |
|                                                                               | Forms](https://support.google.com/appsheet/answer/14824665) or adding a table |
|                                                                               | using a form from Google Forms.                                               |
|                                                                               |                                                                               |
|                                                                               | See [Prevent app creators from using Google                                   |
|                                                                               | Forms](https://support.google.com/appsheet/answer/14836137).                  |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Disallow webhook                                                              | Prevents app creators from using                                              |
|                                                                               | [webhooks](https://support.google.com/appsheet/answer/11511009) in their      |
|                                                                               | apps. See [Prevent app creators from using                                    |
|                                                                               | webhooks]                                                                     |
|                                                                               | (https://support.google.com/appsheet/answer/13573588#prevent-using-webhooks). |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Enable offline use                                                            | Requires that apps are configured to run offline by turning on **The app can  |
|                                                                               | start when offline** when configuring settings for offline use. See [Enable   |
|                                                                               | app to start when                                                             |
|                                                                               | offl                                                                          |
|                                                                               | ine](https://support.google.com/appsheet/answer/10108551#start-when-offline). |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Enforce FedRAMP compliance                                                    | Requires that all apps only use FedRAMP-compliant services and features.      |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Must sync-on-start                                                            | Requires that apps refresh their data each time they start. See [Sync on      |
|                                                                               | start](https://support.google.com/appsheet/answer/10107724#sync-on-start).    |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Only users from specific domain                                               | Only allows users from specific domains to access apps.                       |
|                                                                               |                                                                               |
|                                                                               | **Note**: When configuring this policy template, you’ll need to replace       |
|                                                                               | `ourdomain.com` and `subdomain.ourdomain.com` with the specific domains to    |
|                                                                               | allow.                                                                        |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Prevent row delete                                                            | Prevents apps from deleting rows of data in their connected data sources by   |
|                                                                               | ensuring the Deletes option is always unchecked in table settings. See        |
|                                                                               | [*Control add, update, and delete                                             |
|                                                                               | operations*](https://support.google.com/appsheet/answer/10106345).            |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Require direct sharing                                                        | Requires that access is only granted to users explicitly shared to an app in  |
|                                                                               | the [*sharing                                                                 |
|                                                                               | dialog*](ht                                                                   |
|                                                                               | tps://support.google.com/appsheet/answer/10104983#share-restricted-audience). |
|                                                                               | Only [*individual                                                             |
|                                                                               | users*                                                                        |
|                                                                               | ](https://support.google.com/appsheet/answer/10104983#share-individual-users) |
|                                                                               | users added directly to an app can access it, ensuring that sign-in is        |
|                                                                               | required and all access is explicitly managed through the sharing dialog.     |
|                                                                               | Restricts app access as follows:                                              |
|                                                                               |                                                                               |
|                                                                               | -   [Require user                                                             |
|                                                                               |     sign-in](https://support.google.com/appsheet/answer/10104975)             |
|                                                                               | -   Prevent all signed-in users from accessing the app (disable [Allow all    |
|                                                                               |     signed-in                                                                 |
|                                                                               |                                                                               |
|                                                                               |  users](https://support.google.com/appsheet/answer/10104983#share-signed-in)) |
|                                                                               | -   Disable [Require domain                                                   |
|                                                                               |     authentication](https                                                     |
|                                                                               | ://support.google.com/appsheet/answer/10104381#require-domain-authentication) |
|                                                                               |                                                                               |
|                                                                               | **Note**: To restrict sharing of apps with external users, use the Restrict   |
|                                                                               | external app sharing policy described below.                                  |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Require sign-in                                                               | Restricts public access to apps by [*requiring users to sign                  |
|                                                                               | in*](https://support.google.com/appsheet/answer/10104975) (authenticate) to   |
|                                                                               | access an app.                                                                |
|                                                                               |                                                                               |
|                                                                               | **Note**: To restrict the authentication provider used during sign-in, use    |
|                                                                               | the Restrict authentication provider policy.                                  |
|                                                                               |                                                                               |
|                                                                               | The Require sign-in policy applies to the app itself and doesn't necessarily  |
|                                                                               | restrict automation events that are triggered by changes made to external     |
|                                                                               | sources (e.g., automations triggered by submissions to a Google Form by       |
|                                                                               | external users).                                                              |
|                                                                               |                                                                               |
|                                                                               | App creators can configure their apps in ways that prevent AppSheet from      |
|                                                                               | identifying who is triggering the automation event. It is always the app      |
|                                                                               | creator's responsibility to ensure that external sources comply with their    |
|                                                                               | organizational rules and policies as well as AppSheet terms of service.       |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Restrict app sharing                                                          | Restricts app sharing as follows:                                             |
|                                                                               |                                                                               |
|                                                                               | -   Prevents the sharing of apps with an entire domain using the Share dialog |
|                                                                               | -   Limits the number of users that the app can be shared with using the      |
|                                                                               |     Share dialog (defaults to 5, but can be customized)                       |
|                                                                               |                                                                               |
|                                                                               | See also: [Share: The                                                         |
|                                                                               | Essentials](https://support.google.com/appsheet/answer/10104983)              |
|                                                                               |                                                                               |
|                                                                               | **Note**: To restrict sharing of apps with external users, use the Restrict   |
|                                                                               | external app sharing policy described below.                                  |
|                                                                               |                                                                               |
|                                                                               | The Restrict app sharing policy applies to the app itself and doesn't         |
|                                                                               | necessarily restrict automation events that are triggered by changes made to  |
|                                                                               | external sources (e.g., automations triggered by submissions to a Google Form |
|                                                                               | by external users).                                                           |
|                                                                               |                                                                               |
|                                                                               | App creators can configure their apps in ways that prevent AppSheet from      |
|                                                                               | identifying who is triggering the automation event. It is always the app      |
|                                                                               | creator's responsibility to ensure that external sources comply with their    |
|                                                                               | organizational rules and policies as well as AppSheet terms of service.       |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Restrict authentication provider                                              | Restricts user sign-in to one authentication provider. Google is the default. |
|                                                                               |                                                                               |
|                                                                               | To specify the authentication provider, use one of the following strings:     |
|                                                                               |                                                                               |
|                                                                               | -   `apple`                                                                   |
|                                                                               | -   `box`                                                                     |
|                                                                               | -   `dropbox`                                                                 |
|                                                                               | -   `google`                                                                  |
|                                                                               | -   `microsoft`                                                               |
|                                                                               | -   `salesforce`                                                              |
|                                                                               | -   `smartsheet`                                                              |
|                                                                               |                                                                               |
|                                                                               | **Note**:  To fully restrict access by users outside of the owner's domain,   |
|                                                                               | use this policy in conjunction with the Require sign-in policy.               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Restrict Automation email attachments                                         | Prevents app creators from [adding an attachment to                           |
|                                                                               | ema                                                                           |
|                                                                               | ils](https://support.google.com/appsheet/answer/11447614#attachment-settings) |
|                                                                               | that are sent from automations. See [Prevent app creators from adding email   |
|                                                                               | attachments in                                                                |
|                                                                               | automations](ht                                                               |
|                                                                               | tps://support.google.com/appsheet/answer/11447614#prevent-email-attachments). |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Restrict data sources                                                         | Restricts app access to specific [data                                        |
|                                                                               | sources](https://support.google.com/appsheet/answer/10106309) by data source  |
|                                                                               | name.                                                                         |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Restrict external app sharing                                                 | Restricts app sharing to only emails or domains internal to the domain        |
|                                                                               | belonging to the app owner's organization. For an [AppSheet                   |
|                                                                               | organization](https://support.google.com/appsheet/answer/13691133), this      |
|                                                                               | includes all secondary domains managed by the parent Google Workspace         |
|                                                                               | account, if applicable.                                                       |
|                                                                               |                                                                               |
|                                                                               | **Note**:  To fully restrict access by users outside of the owner's domain,   |
|                                                                               | use this policy in conjunction with Restrict authentication provider          |
|                                                                               | (described previously).                                                       |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Restrict external data sources and auth domains                               | Prevents app creators from using external data sources and authentication     |
|                                                                               | domains in an app.                                                            |
|                                                                               |                                                                               |
|                                                                               | **For Workspace users**: Only Workspace authentication and data sources are   |
|                                                                               | allowed.                                                                      |
|                                                                               |                                                                               |
|                                                                               | **For non-Workspace users**: The app editors are only allowed to attach the   |
|                                                                               | data sources to an app or integrate with the auth domains with the apps that  |
|                                                                               | are the same as the app owner's email domain.                                 |
|                                                                               |                                                                               |
|                                                                               | See also:                                                                     |
|                                                                               |                                                                               |
|                                                                               | -   [Prevent app creators from using external data                            |
|                                                                               |     sources](https://support.google.com/appsheet/answer/13579362)             |
|                                                                               | -   [Prevent app creators from using external authentication                  |
|                                                                               |     domai                                                                     |
|                                                                               | ns](https://support.google.com/appsheet/answer/10105757#prevent-auth-domains) |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Restrict external database sharing                                            | Restricts AppSheet database sharing to only emails or domains internal to the |
|                                                                               | domain belonging to the app owner's organization. For an [AppSheet            |
|                                                                               | organization](https://support.google.com/appsheet/answer/13691133), this      |
|                                                                               | includes all secondary domains managed by the parent Google Workspace         |
|                                                                               | account, if applicable.                                                       |
|                                                                               |                                                                               |
|                                                                               | See also [Restrict external database                                          |
|                                                                               | sharing](ht                                                                   |
|                                                                               | tps://support.google.com/appsheet/answer/12637319#restrict-external-sharing). |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Restrict providers attachable to apps                                         | Restricts app access to specific [data source                                 |
|                                                                               | types](https://support.google.com/appsheet/answer/10106309).                  |
|                                                                               |                                                                               |
|                                                                               | To specify data source types, use one or more of the following strings:       |
|                                                                               |                                                                               |
|                                                                               | -   `airtable`                                                                |
|                                                                               | -   `apigee_api`                                                              |
|                                                                               | -   `apple`                                                                   |
|                                                                               | -   `aws_cognito_domain`                                                      |
|                                                                               | -   big_query                                                                 |
|                                                                               | -   `box`                                                                     |
|                                                                               | -   `data_studio` ([Looker                                                    |
|                                                                               |     Studio](https://cloud.google.com/looker/docs/studio/))                    |
|                                                                               | -   `database` (all cloud and on-premises databases)                          |
|                                                                               | -   `dropbox`                                                                 |
|                                                                               | -   `dynamodb`                                                                |
|                                                                               | -   `google`                                                                  |
|                                                                               | -   `google_calendar`                                                         |
|                                                                               | -   `google_tables` (see also [Disable AppSheet                               |
|                                                                               |     databases](https://support.google.com/appsheet/answer/12629371))          |
|                                                                               | -   `integration_connector`                                                   |
|                                                                               | -   `mariadb`                                                                 |
|                                                                               | -   `microsoft`                                                               |
|                                                                               | -   `mysql`                                                                   |
|                                                                               | -   `odata`                                                                   |
|                                                                               | -   `okta_domain`                                                             |
|                                                                               | -   `openid_connect`                                                          |
|                                                                               | -   `oracle`                                                                  |
|                                                                               | -   `postgres`                                                                |
|                                                                               | -   `redshift`                                                                |
|                                                                               | -   `salesforce`                                                              |
|                                                                               | -   `sqlserver`                                                               |
|                                                                               | -   sketch (to [create an view apps using                                     |
|                                                                               |     Spec](https://support.google.com/appsheet/answer/12007354))               |
|                                                                               | -   `smartsheet`                                                              |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Restrict Webhook URLs                                                         | Restricts app creators to use only a specific set of webhook URLs             |
|                                                                               | wh                                                                            |
|                                                                               | en [calling webhooks](https://support.google.com/appsheet/answer/11511244) in |
|                                                                               | their automations. See [Restrict webhook                                      |
|                                                                               | URLs                                                                          |
|                                                                               | ](https://support.google.com/appsheet/answer/13573588#restrict-webhook-urls). |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Restrict use of external apps                                                 | Blocks users from accessing apps created externally to your organization.     |
|                                                                               |                                                                               |
|                                                                               | **For Workspace users with an AppSheet organization**: Your "organization" is |
|                                                                               | defined as all verified [domains](https://support.google.com/a/answer/177483) |
|                                                                               | associated with your Workspace account. If an app is created in the same      |
|                                                                               | Workspace organization or verified domain, it is considered to be internal    |
|                                                                               | and will not be blocked.                                                      |
|                                                                               |                                                                               |
|                                                                               | **For non-Workspace users or Workspace customers without an AppSheet          |
|                                                                               | organization**: If an app is created in the app owner's email domain, it is   |
|                                                                               | considered to be internal and will not be blocked.                            |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Restrict who can deploy apps                                                  | Restricts app deployment to specific app creators.                            |
|                                                                               |                                                                               |
|                                                                               | **Note**: You will need to specify the IDs of the app creators that are       |
|                                                                               | allowed to deploy apps by editing the `LIST(11111, 11122)` function in the    |
|                                                                               | policy condition expression. To determine the ID of an app creator, go to     |
|                                                                               | your [team members page](https://support.google.com/appsheet/answer/11938918) |
|                                                                               | and view the ID adjacent to the email address for each app creator on your    |
|                                                                               | team.                                                                         |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Run as app creator                                                            | Ensures all apps run using the app creator’s identity to access connected     |
|                                                                               | data sources by ensuring that the access mode is set to "as app creator". See |
|                                                                               | [Access mode: as app creator or app                                           |
|                                                                               | user](https://support.google.com/appsheet/answer/10105756?).                  |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
