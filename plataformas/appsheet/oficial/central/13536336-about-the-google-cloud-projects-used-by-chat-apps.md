---
fonte: https://support.google.com/appsheet/answer/13536336?hl=en
baixado: 2026-11-10
---

# About the Google Cloud projects used by Chat apps

You must be a **Google Workspace user** to create Chat apps with AppSheet. See [Add AppSheet to Google Workspace](https://support.google.com/a/answer/10447197).

Every AppSheet app that is used to build a [*Chat app*](https://developers.google.com/chat/how-tos/apps-develop) requires a [*Google Cloud project*](https://cloud.google.com/resource-manager/docs/creating-managing-projects) to function. Your Cloud project can be automatically or manually configured. With automatic configuration, the Cloud project is created as you step through the wizard on the Chat Setup tab in the app editor.

Automatic configuration is recommended for ease-of-use with setup. Manual configuration is available if your organization restricts certain Google Cloud functionality.

See also: [Choose the configuration mode](https://support.google.com/appsheet/answer/12849362#configuration-mode)

You can configure **one** Chat app per Google Cloud project.

 

Once an app is successfully linked to a Cloud project, if you want to **change the configuration mode** do one of the following:

- Delete the Cloud project created in this step, [copy the app](https://support.google.com/appsheet/answer/12491039), and start over
- Contact [AppSheet Support](https://www.appsheet.com/Support/Contact) for assistance

## Automatic projects

If you use [automatic configuration](https://support.google.com/appsheet/answer/12849362#automatic-configuration) to configure your Chat app, a Cloud project ("automatic project") is created automatically for you in your organization. Note the following about automatic projects:

- You never need to view or manage this automatic project. AppSheet handles the necessary interactions with Google Cloud. For example, if you change a slash command name, it is automatically synchronized with the project.
- Only organization admins have access to the project in the Google Cloud console.
- If your organization has policy restrictions on Google Cloud (for example, prohibiting an out-of-organization service account), you may need to use [manual configuration](https://support.google.com/appsheet/answer/12849362#manual-configuration) instead.

By default, Cloud projects have an Identity and Access Management (IAM) policy with two entries: 

1.  Google service account that acts as the owner of the automatic project: `appsheet-workspace-server@system.gserviceaccount.com`
2.  Lower-permission service account ending in either `@appsheet-prod-service-accounts` or  `@appsheet-prod-eu-saccts.iam.gserviceaccount.com`

### View or update automatic projects

Unless you are an admin, you can’t directly locate, view, or edit automatic projects in the Cloud console. If you're an admin, you can access the projects under the following folder: `Organization root > system-gsuite > appsheet`

Project IDs will be prefixed by `app-`. 

### Delete automatic projects

If you're an admin, you can delete automatic projects as you would standard Cloud projects. See [Shutting down (deleting) projects](https://cloud.google.com/resource-manager/docs/creating-managing-projects#shutting_down_projects).

If you're not an admin, you can't delete automatic projects directly. However, AppSheet deletes automatic projects in the following scenarios:

- If you delete the app configured with an automatic project, AppSheet deletes the project attached to the script along with any settings or information it contains.
- If the automatic project is unused for at least 180 days, your project may be deleted.

Deleting an automatic project deletes all Chat app-related configuration.

## Manual project

If you use [manual configuration](https://support.google.com/appsheet/answer/12849362#manual-configuration) to configure your Chat app, the Cloud project ("manual project") is linked and supports all of the same behaviors described in [*Creating or maintaining a Cloud Project*](https://cloud.google.com/resource-manager/docs/creating-managing-projects). In this case, each time the app configuration is changed, the user must manually sync their settings in the Cloud Console project.
