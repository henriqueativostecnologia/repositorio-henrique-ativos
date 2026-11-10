---
fonte: https://support.google.com/appsheet/answer/15965965?hl=en
baixado: 2026-11-10
---

# About the Google Cloud service accounts and projects used by AppSheet

AppSheet can connect with other Google products to enable certain features, like Chat apps and data integrations.  This is done through Google Cloud service accounts and projects, some of which are owned and managed by AppSheet and others that are owned and managed by  your organization. Regardless of who owns the service accounts, your Google Cloud admins have complete control over access to your Google Cloud projects through Identity and Access Management (IAM) and the Google Cloud console.

Learn more about the Google Cloud service accounts and projects used by AppSheet:

- [AppSheet-owned service accounts and projects](#appsheet-owned)
- [Google Cloud service accounts and projects owned by your organization](#organization-owned)
- [AppSheet access to Google Cloud projects](#appsheet-access)
- [Manage permissions to AppSheet-owned service accounts](#manage-permissions-appsheet-owned)
- [Manage automatic projects](#manage-automatic-projects)
- [Features that use Google Cloud service accounts and projects](#features-use-service-accounts-projects)

The following illustration shows the Google Cloud service accounts and projects used by AppSheet, described in the following sections.

Service accounts and projects used by AppSheet

## AppSheet-owned service accounts and projects

The AppSheet-owned service accounts and projects are created inside an AppSheet-owned Google Cloud project. No human manages these service accounts and only AppSheet can view, create, use, and delete the service account.

## Google Cloud service accounts and projects owned by your organization

**Service accounts** owned and managed by your organization are inside your own Google Cloud projects and are managed by your Google Cloud admin. As an AppSheet admin, you can’t directly locate, view, or edit these service accounts unless you are also a Google Cloud admin or have been given appropriate permissions in Google Cloud by your Cloud admin.

**Google Cloud projects** owned by your organization also cannot be located, viewed, or edited unless you are a Google Cloud admin or have been granted the appropriate permissions.

### Automatic projects

For some features to work, AppSheet may create Google Cloud projects on behalf of your organization that are still owned and managed by your Google Cloud admin.  

You never need to view or manage automatic projects. AppSheet handles the necessary interactions with Google Cloud. For example, if you change a slash command name in a Chat app, it is automatically synchronized with the project.

Only Google Cloud admins have access to the project in the Google Cloud console.

If your organization has policy restrictions on Google Cloud (for example, prohibiting an out-of-organization service account), you may need to use manual configuration instead.

To learn more, go to [Manage automatic projects](#manage-automatic-projects).

## AppSheet access to your Google Cloud projects

For some AppSheet features to work, AppSheet needs access to the services in your Google Cloud projects.  In these cases, your Google Cloud admin may need to grant permissions to the AppSheet-owned service accounts. Even though the accounts are owned by AppSheet, your Cloud admin can revoke permissions at any time.

To grant permissions, your Google Cloud admin will use the Google Cloud console to update IAM permissions to grant the AppSheet service account certain roles. Cloud admins can stop allowing AppSheet access to these projects and roles at any time.

To learn more, go to [Manage permissions to AppSheet-owned service accounts](#manage-permissions-appsheet-owned).

## Manage permissions to AppSheet-owned service accounts

Only your Google Cloud admin can assign permissions to AppSheet-owned Service accounts. Your Google Cloud admin will use Google Cloud Identity and Access Management (IAM) in the Google Cloud console. In some cases, AppSheet will auto-assign itself permissions to automatic projects it created but your Google Cloud admin can still manage those permissions, like revoking privileges.

The specific service accounts, roles, and principals used will depend on the AppSheet features being configured but the steps for granting and revoking permissions are the same as  assigning roles to principals in IAM.

To learn more about granting and revoking permissions, see:

- [Grant an IAM role](https://cloud.google.com/iam/docs/grant-role-console#grant_an_iam_role)
- [Revoke IAM roles](https://cloud.google.com/iam/docs/grant-role-console#revoke-roles)

## Manage automatic projects

Manage automatic projects as described in the following sections:

- [View or update automatic projects](#view-update-automatic-projects)
- [Delete automatic projects](#delete-automatic-projects)

### View or update automatic projects

Unless you are a Google Cloud admin, you can’t directly locate, view, or edit automatic projects in the Cloud console. Cloud admins can access the projects under the following folder: **Organization root \> system-gsuite \> appsheet**

Project IDs will be prefixed by `app-`. 

### Delete automatic projects

Google Cloud admins can delete automatic projects as with any standard Cloud projects. See [Shutting down (deleting) projects](https://cloud.google.com/resource-manager/docs/creating-managing-projects#shutting_down_projects).

If you're not a Cloud admin, you can't delete automatic projects directly. However, AppSheet deletes automatic projects in some cases, as noted in [Features that use Google Cloud service accounts and projects](#features-use-service-accounts-projects).

## Features that use Google Cloud service accounts and projects

The following table summarizes the AppSheet features that use Google Cloud service accounts and projects.

The types and names of service accounts, roles, automatic projects, and additional actions used are specific to each AppSheet feature. Review the configuration for each feature.  

+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **Feature**                                        | **Usage**                                          | **More information**                               |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Chat apps                                          | -   AppSheet-owned service accounts                | [Configure Chat apps with                          |
|                                                    | -   Automatic projects (AppSheet creates and       | AppSheet](ht                                       |
|                                                    |     deletes)                                       | tps://support.google.com/appsheet/answer/12849362) |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Integration Connectors (preview)                   | AppSheet-owned service accounts                    | [Set up Integration Connectors with                |
|                                                    |                                                    | AppSheet](ht                                       |
|                                                    |                                                    | tps://support.google.com/appsheet/answer/16178778) |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Export team audit logs to Google BigQuery          | AppSheet-owned service accounts                    | [Export team audit logs to                         |
|                                                    |                                                    | BigQuery](ht                                       |
|                                                    |                                                    | tps://support.google.com/appsheet/answer/12469223) |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
