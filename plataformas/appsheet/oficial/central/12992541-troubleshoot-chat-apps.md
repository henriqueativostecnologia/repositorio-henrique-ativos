---
fonte: https://support.google.com/appsheet/answer/12992541?hl=en
baixado: 2026-11-10
---

# Troubleshoot Chat apps

The following sections provide tips for troubleshooting issues when configuring your Chat app. The most common challenge in Chat app creation is managing access permissions. See also [Troubleshoot Chat messages](https://support.google.com/appsheet/answer/13265243).

------------------------------------------------------------------------

[Expand all](#expand)** ** \|** **[Collapse all](https://support.google.com/appsheet/answer/12992541)

#### Why can't I access Chat apps in my AppSheet editor?

You must be a **Google Workspace user** to create Chat apps with AppSheet. See [Add AppSheet to Google Workspace](https://support.google.com/a/answer/10447197). Be sure to sign in to AppSheet using your Google Workspace account.

If you aren't a Google Workspace user or aren't signed in with your Google Workspace account, you won't see the Chat apps icon  in the navigation bar.

Navigation bar with Chat app icon crossed out

#### Why do I get a permissions error when accessing the Google Cloud project?

When you access the Google Cloud project in the Console, make sure you are signed in using your AppSheet account. If you are an admin and are unable to access the Google Cloud project associated with a Chat app, you may need to grant your account access. See [Manage access to projects, folders, and organizations](https://cloud.google.com/iam/docs/granting-changing-revoking-access). 

If you selected **Automatic configuration** to [create and connect a Google Cloud project to your app](#connect-project), it can take up to **7 minutes** before you can [enable the Google Chat API](https://support.google.com/appsheet/answer/12849362#enable-chat-api). If you see one or both of the following error message, wait a few minutes and then refresh the page:

`You do not have permissions to view this page.`

`You do not have permission to update the configuration.`

#### I deployed my app and enabled it in the Chat Setup section of AppSheet. Why isn’t my Chat app appearing in Google Chat?

Importantly, “deployed” is not the same as “published”. To get your AppSheet app into Chat and running as a *Chat app*, it must be “published” and shared with users. See [Test and share Chat apps](https://support.google.com/appsheet/answer/12857667). 

#### Why can't I enable a Chat app in the Chat Setup section of AppSheet?

You must be an app creator in order to [enable a Chat app](https://support.google.com/appsheet/answer/12849362#enable-chat-apps) in the Chat Setup section of AppSheet. 

#### I created my Chat app. Why don't I see it in my domain-internal marketplace?

This is likely due to the fact that your Workspace team uses a Workspace Marketplace allowlist. Contact your Workspace admin and follow your team's process to approve access. Only the original app creator will see it listed; co-creators will also be subject to allowlist settings.

#### Why can't users find or install my Chat app, even after I've shared it with them in AppSheet?

This is likely due to the fact that your Workspace team uses a Workspace Marketplace allowlist. Contact your Workspace admin and follow your team's process to approve access to the user accounts.

#### Google Cloud project already in use by another Chat app

You can configure **one** Chat app per Google Cloud project. If a Google Cloud project is already in use by another app, the following error message is displayed:

`This project is already linked to another app. Please use a different GCP project.`

To resolve this issue, you can:

1.  [Create and connect another Google Cloud project](https://support.google.com/appsheet/answer/12849362#enable-chat=apps).
2.  Disconnect the other app from the Google Cloud project by clearing the [**Google Project** **Number** field](https://support.google.com/appsheet/answer/12849362#project-number-field). 

#### Why do only some AppSheet views work on Chat?

Some AppSheet views cannot be rendered using the existing Google Chat framework capabilities. We will continue to add support for more AppSheet views and settings as capabilities are added to the Google Chat framework. See [Summary of features supported for Chat apps with AppSheet](https://support.google.com/appsheet/answer/12917178).

#### How do I resolve the error "Cloud Resource Manager project creation is disabled"?

If you selected [automatic configuration](https://support.google.com/appsheet/answer/12849362#automatic-configuration) and your organization is blocking the use of the Google Cloud Platform by a domain policy, then you will receive the following error: 

`Cloud Resource Manager project creation is disabled`. 

To resolve this issue, request that your organization administrator grant access to Google Cloud services. See [Turn Google Cloud on or off for users](https://support.google.com/a/answer/9197205).

#### How do I resolve the error "Your domain doesn't have access to create Chat apps"?

If you selected [automatic configuration](https://support.google.com/appsheet/answer/12849362#automatic-configuration) and your organization is blocking the use of the Google Cloud Platform by a domain policy, then you will receive the following error: 

`Your domain doesn't have access to create Chat apps`. 

To resolve this issue:

- Request that your organization administrator allowlist the following (see [Restricting identities by domain](https://cloud.google.com/resource-manager/docs/organization-policy/restricting-domains)):

  - Google service account that acts as the owner of the automatic project: `appsheet-workspace-server@system.gserviceaccount.com`

  - Lower-permission service account ending in either `@appsheet-prod-service-accounts.iam.gserviceaccount.com` (non-EU region) or  `@appsheet-prod-eu-saccts.iam.gserviceaccount.com` (EU region)

  See also [Control API access with domain-wide delegation](https://support.google.com/a/answer/162106).  

- Create a Chat app using [manual configuration](https://support.google.com/appsheet/answer/12849362#manual-configuration). 

#### How do I resolve the error "Request failed (Code: 2) - Google Cloud project does not match"

When using [manual configuration](https://support.google.com/appsheet/answer/12849362#manual-configuration), if the **Google Project Number** field [configured for your app](https://support.google.com/appsheet/answer/12849362#enable-chat-apps), does not match the Google Cloud project number associated with the [configured Google Chat API](https://support.google.com/appsheet/answer/12849362#configure-chat-api). In this scenario, the following error message is displayed:

`Request failed (Code: 2). The GCP project linked to your app does not match the GCP project of this chat app`

Update the value in the **Google Project Number** field to use the correct project number.
