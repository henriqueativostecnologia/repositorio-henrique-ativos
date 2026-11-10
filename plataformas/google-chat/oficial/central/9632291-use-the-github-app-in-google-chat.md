---
fonte: https://support.google.com/chat/answer/9632291?hl=en
baixado: 2026-11-10
---

# Use the GitHub app in Google Chat

This article has different instructions for each platform/version: Computer, Android phone & tablet, iPhone & iPad. All versions are copied below.

## Version: Computer

Use the GitHub app in Chat to get notifications about GitHub events, such as issues, pull requests, and comments.

### Before you begin

To use the GitHub app for Chat:

- You need permission to install apps from your Google Workspace administrator.
- Add the app to Chat. [Learn how to find apps and add them to Chat](https://support.google.com/chat/answer/7655820).
- You need a GitHub account.
- You need to install the [Google Chat app for your GitHub repository](https://github.com/apps/google-chat-app).

##### Understand GitHub app & OAuth app authentication mechanisms

This outlines the distinct characteristics and operational models of GitHub apps and OAuth apps, which serve as primary mechanisms for third-party services to integrate with and access GitHub resources. A comprehensive understanding of these differences is critical to maintain an optimal security posture within an organization.

#### 1. Comparative analysis: Key distinctions

The fundamental differences between the 2 models reside in the identity used for access (the *Principal*) and the mechanism that governs resource authorization.

|                              |                                                                                                                                                                                                                    |                                                                                                                               |
|------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| **Attribute**                | **GitHub app (Recommended sign in)**                                                                                                                                                                               | **OAuth app (Legacy sign in)**                                                                                                |
| **Principal identity**       | Acts as an independent **Application Identity**, separate from any user, or on behalf of the authorizing user, depending on the use case.                                                                          | Acts **on behalf of the authorizing user**, inheriting their privileges.                                                      |
| **Authorization model**      | **Fine-grained permissions (Recommended):** Utilizes the **Principle of Least Privilege**, allowing access to specific repositories and resource types. For example: Read access for metadata only.                | **Broad scopes:** Access is defined by wide scopes like granting access to **all resources** visible to the authorizing user. |
| **Credential longevity**     | **Short-lived tokens:** Access tokens possess a limited lifespan (typically 1 hour) and require frequent renewal, significantly mitigating risk in the event of compromise.                                        | **Long-lived tokens:** Access tokens persist until manually revoked by the user, representing a prolonged exposure risk.      |
| **Installation requirement** | Must be **installed** by an Administrator or Organization owner, establishing a formal link to the account or organization and authorized by the user for use cases where the app is acting on behalf of the user. | Must be **authorized** by an individual user, linking access directly to that user's identity.                                |

For more comprehensive documentation, refer to [Differences between GitHub Apps and OAuth apps](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/differences-between-github-apps-and-oauth-apps).

#### 2. Recommendation

Based on security best practices, the **GitHub App authentication mechanism is recommended** for all third-party and organizational integrations. This model enforces the **Principle of Least Privilege** and employs robust, time-limited credentials, thereby maintaining a higher standard of security and operational stability compared to the delegated authority model of OAuth Apps.

[Install the Google Chat App for GitHub repositories](https://github.com/apps/google-chat-app).

### Set up the GitHub app in Chat

1.  Open [Chat](https://chat.google.com).
2.  Open a direct message with the app or go to a space with the app.
3.  To open the configuration window, click **Sign in**.
4.  Click **Configure Access** and then **Sign in to GitHub**.
5.  Complete the sign-in process then close the popup.
6.  To update the Chat dialog, click **Refresh**.
7.  Under **Add Repositories**, type the GitHub repository you want notifications for.
8.  Check the boxes for the events you want notifications for.
9.  Click **Save**.

**Tip:** You need to set up notifications in each space where you add the app. The app sends notifications to all spaces where it's a member.

### Migrate from OAuth app (Legacy) to GitHub app (Recommended)

To migrate your current connection from the older OAuth app authentication method to the recommended GitHub app method:

1.  Open [Chat](https://chat.google.com/).
2.  Open a direct message or space with the GitHub app.
3.  In the message field, click Google Workspace tools .
4.  In the command list, select **GitHub Reauthorize**.
5.  To complete the migration and reauthorization process, follow the on-screen instructions in the Chat dialogue.

### Use the GitHub app in spaces

To use the app in spaces, you need to **@mention** or **/mention** the app in each message and in replies to the messages from the app.

The **@mention** or **/mention** confirms you've sent the message to the app and not to others in the space.

1.  Open the Chat app .
2.  In a space, enter **@github** or **/github** followed by the command.
    - When you mention **@github** or **/github**, the message is sent to the app and not to others in the space.

### Change app settings

In spaces, only the person who added the app can change the settings.

1.  Open [Chat](https://chat.google.com).
2.  Open a direct message with the app or go to a space with the app.
3.  To open the current settings for the app, enter: `/github_settings`.
4.  Change the settings as needed.
5.  Click **Save**.

Removing the app from a space deletes the app settings.

### Learn about commands for the GitHub app in Chat

In the message field of a direct message or space with the GitHub app in Chat, you can use:

- **Slash commands:**
  - `/github_settings`: Opens the settings dialogue.
  - `/github_reminders`: For personal or team open pull requests, set up and edit scheduled reminders.
  - `/github_subscribe`: Subscribes to a GitHub \<repoURL\> or \<owner/repo\>.
  - `/github_openIssue`: Opens a new GitHub issue.
  - `/github_logout`: Logs out of your GitHub account.
  - `/github_help`: Displays the help message.
  - `/github_feedback`: Send feedback about the GitHub app.
- **Quick commands:** To access the quick commands, click Google Workspace tools .
  - **GitHub Connect:** Displays a message with a “Sign in” and “Legacy Sign in” option.
  - **GitHub Reauthorize:** Allows you to migrate to a new connection method.

To get a full list of supported commands:

1.  On your computer, open [Chat](https://chat.google.com/).
2.  Open a direct message or go to a space where the GitHub app is installed.
3.  Enter: `/github_help`.

### Troubleshoot issues with GitHub app in Chat

##### If you get an error when you subscribe to real-time notifications

##### GitHub app

To set up real-time notifications in spaces:

1.  In your browser, go to [GitHub profile settings](https://github.com/settings/profile).
2.  Under “Integrations,” click **Applications** and then **Authorized GitHub apps**.
    - After you connect the GitHub app in Google Chat, your list of authorized apps shows “Google Chat.”
3.  [Install the Google Chat App for GitHub repository](https://github.com/apps/google-chat-app).
    - Or, you can request installation from the organization/repository owner.
4.  Wait until installation is complete.
5.  In Google Chat, open a direct message or space with the GitHub app.
6.  In the message field, to create a subscription, enter: `/github_subscribe [organisation/repo]` or `/github_settings`.

##### OAuth app

To set up real-time notifications in spaces, you must:

- Be an organization owner of the proposed repository.
- Authorize the app on the GitHub organization.
  1.  In your browser, go to [GitHub profile settings](https://github.com/settings/profile).
  2.  Under “Integrations,” click **Applications** and then **Authorized OAuth apps**.
      - After you connect the GitHub app in Google Chat, your list of authorized apps shows "Google Chat."
  3.  [Grant the app access to the organization you want to access](https://docs.github.com/articles/restricting-access-to-your-organization-s-data/).

##### If you receive too many notifications from the GitHub app

1.  In the message field, enter: `/github_settings`.
2.  To edit your repository notifications settings, click **Notification settings**.
3.  To filter the notifications, next to each notification type, click the down arrow .
    - It displays additional options to filter notifications.
4.  Check the boxes for the notifications you want.
5.  Click **Save**.

##### If you don’t get @mentioned in scheduled reminders

To get mentioned in scheduled reminders, you must’ve connected your Google Chat account to the GitHub account.

1.  In the message field, enter: `/github_settings`.
2.  To connect your account:
    1.  In the pop-up, click **Configure access** and then **Sign in to GitHub**.
    2.  Sign in to your GitHub account.
    3.  Authorize the app.
3.  In the message you receive from the GitHub app, select **Schedule reminders for your team**.
4.  In the pop-up:
    1.  Click **Create new reminder.**
    2.  Configure the reminder settings.
    3.  Click **Save**.

##### If you don't get reminders with GitHub app

On the repository from where you want to receive reminders, [verify the installation of the Google Chat App for GitHub](https://github.com/apps/google-chat-app/installations/select_target).

*Google, Google Workspace, and related marks and logos are trademarks of Google LLC. All other company and product names are trademarks of the companies with which they are associated.*

## Version: Android phone & tablet

Use the GitHub app in Chat to get notifications about GitHub events, such as issues, pull requests, and comments.

### Before you begin

To use the GitHub app for Chat:

- You need permission to install apps from your Google Workspace administrator.
- Add the app to Chat. [Learn how to find apps and add them to Chat](https://support.google.com/chat/answer/7655820).
- You need a GitHub account.
- You need to install the [Google Chat app for your GitHub repository](https://github.com/apps/google-chat-app).

##### Understand GitHub app & OAuth app authentication mechanisms

This outlines the distinct characteristics and operational models of GitHub apps and OAuth apps, which serve as primary mechanisms for third-party services to integrate with and access GitHub resources. A comprehensive understanding of these differences is critical to maintain an optimal security posture within an organization.

#### 1. Comparative analysis: Key distinctions

The fundamental differences between the 2 models reside in the identity used for access (the *Principal*) and the mechanism that governs resource authorization.

|                              |                                                                                                                                                                                                                    |                                                                                                                               |
|------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| **Attribute**                | **GitHub app (Recommended sign in)**                                                                                                                                                                               | **OAuth app (Legacy sign in)**                                                                                                |
| **Principal identity**       | Acts as an independent **Application Identity**, separate from any user, or on behalf of the authorizing user, depending on the use case.                                                                          | Acts **on behalf of the authorizing user**, inheriting their privileges.                                                      |
| **Authorization model**      | **Fine-grained permissions (Recommended):** Utilizes the **Principle of Least Privilege**, allowing access to specific repositories and resource types. For example: Read access for metadata only.                | **Broad scopes:** Access is defined by wide scopes like granting access to **all resources** visible to the authorizing user. |
| **Credential longevity**     | **Short-lived tokens:** Access tokens possess a limited lifespan (typically 1 hour) and require frequent renewal, significantly mitigating risk in the event of compromise.                                        | **Long-lived tokens:** Access tokens persist until manually revoked by the user, representing a prolonged exposure risk.      |
| **Installation requirement** | Must be **installed** by an Administrator or Organization owner, establishing a formal link to the account or organization and authorized by the user for use cases where the app is acting on behalf of the user. | Must be **authorized** by an individual user, linking access directly to that user's identity.                                |

For more comprehensive documentation, refer to [Differences between GitHub Apps and OAuth apps](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/differences-between-github-apps-and-oauth-apps).

#### 2. Recommendation

Based on security best practices, the **GitHub App authentication mechanism is recommended** for all third-party and organizational integrations. This model enforces the **Principle of Least Privilege** and employs robust, time-limited credentials, thereby maintaining a higher standard of security and operational stability compared to the delegated authority model of OAuth Apps.

[Install the Google Chat App for GitHub repositories](https://github.com/apps/google-chat-app).

### Set up the GitHub app in Chat

1.  Open the Chat app .
2.  Open a direct message with the app or go to a space with the app.
3.  To open the configuration window, tap **Sign in**.
4.  Tap **Configure Access** and then **Sign in to GitHub**.
5.  Complete the sign-in process then close the popup.
6.  To update the Chat dialog, tap **Refresh**.
7.  Under **Add Repositories**, type the GitHub repository you want notifications for.
8.  Check the boxes for the events you want notifications for.
9.  Tap **Save**.

**Tip:** You need to set up notifications in each space where you add the app. The app sends notifications to all spaces where it's a member.

### Migrate from OAuth app (Legacy) to GitHub app (Recommended)

To migrate your current connection from the older OAuth app authentication method to the recommended GitHub app method:

1.  Open the Chat app .
2.  Open a direct message or space with the GitHub app.
3.  In the message field, tap Google Workspace tools .
4.  In the command list, select **GitHub Reauthorize**.
5.  To complete the migration and reauthorization process, follow the on-screen instructions in the Chat dialogue.

### Use the GitHub app in spaces

To use the app in spaces, you need to **@mention** or **/mention** the app in each message and in replies to the messages from the app.

The **@mention** or **/mention** confirms you've sent the message to the app and not to others in the space.

1.  Open the Chat app .
2.  In a space, enter **@github** or **/github** followed by the command.
    - When you mention **@github** or **/github**, the message is sent to the app and not to others in the space.

### Change app settings

In spaces, only the person who added the app can change the settings.

1.  Open the Chat app .
2.  Open a direct message with the app or go to a space with the app.
3.  To open current settings for the app, enter: `/github_settings`.
4.  Change the settings as needed.
5.  Tap **Save**.

Removing the app from a space deletes the app settings.

### Learn about commands for the GitHub app in Chat

In the message field of a direct message or space with the GitHub app in Chat, you can use:

- **Slash commands:**
  - `/github_settings`: Opens the settings dialogue.
  - `/github_reminders`: For personal or team open pull requests, set up and edit scheduled reminders.
  - `/github_subscribe`: Subscribes to a GitHub \<repoURL\> or \<owner/repo\>.
  - `/github_openIssue`: Opens a new GitHub issue.
  - `/github_logout`: Logs out of your GitHub account.
  - `/github_help`: Displays the help message.
  - `/github_feedback`: Send feedback about the GitHub app.
- **Quick commands:** To access the quick commands, tap Google Workspace tools .
  - **GitHub Connect:** Displays a message with a “Sign in” and “Legacy Sign in” option.
  - **GitHub Reauthorize:** Allows you to migrate to a new connection method.

To get a full list of supported commands:

1.  On your Android phone or tablet, open the Chat app .
2.  Open a direct message or go to a space where the GitHub app is installed.
3.  Enter: `/github_help`.

### Troubleshoot issues with GitHub app in Chat

##### If you get an error when you subscribe to real-time notifications

##### GitHub app

To set up real-time notifications in spaces:

1.  In your browser, go to [GitHub profile settings](https://github.com/settings/profile).
2.  Under “Integrations,” tap **Applications** and then **Authorized GitHub apps**.
    - After you connect the GitHub app in Google Chat, your list of authorized apps shows “Google Chat.”
3.  [Install the Google Chat App for GitHub repository](https://github.com/apps/google-chat-app).
    - Or, you can request installation from the organization/repository owner.
4.  Wait until installation is complete.
5.  In Google Chat, open a direct message or space with the GitHub app.
6.  In the message field, to create a subscription, enter: `/github_subscribe [organisation/repo]` or `/github_settings`.

##### OAuth app

To set up real-time notifications in spaces, you must:

- Be an organization owner of the proposed repository.
- Authorize the app on the GitHub organization.
  1.  In your browser, go to [GitHub profile settings](https://github.com/settings/profile).
  2.  Under “Integrations,” tap **Applications** and then **Authorized OAuth apps**.
      - After you connect the GitHub app in Google Chat, your list of authorized apps shows “Google Chat.”
  3.  [Grant the app access to the organization you want to access](https://docs.github.com/articles/restricting-access-to-your-organization-s-data/).

##### If you receive too many notifications from the GitHub app

1.  In the message field, enter: `/github_settings`.
2.  To edit your repository notifications settings, tap **Notification settings**.
3.  To filter the notifications, next to each notification type, tap the down arrow .
    - It displays additional options to filter notifications.
4.  Check the boxes for the notifications you want.
5.  Tap **Save**.

##### If you don’t get @mentioned in scheduled reminders

To get mentioned in scheduled reminders, you must’ve connected your Google Chat account to the GitHub account.

1.  In the message field, enter: `/github_settings`.
2.  To connect your account:
    1.  In the pop-up, tap **Configure access** and then **Sign in to GitHub**.
    2.  Sign in to your GitHub account.
    3.  Authorize the app.
3.  In the message you receive from the GitHub app, select **Schedule reminders for your team**.
4.  In the pop-up:
    1.  Tap **Create new reminder.**
    2.  Configure the reminder settings.
    3.  Tap **Save**.

##### If you don't get reminders with GitHub App

On the repository from where you want to receive reminders, [verify the installation of the Google Chat App for GitHub](https://github.com/apps/google-chat-app/installations/select_target).

*Google, Google Workspace, and related marks and logos are trademarks of Google LLC. All other company and product names are trademarks of the companies with which they are associated.*

## Version: iPhone & iPad

Use the GitHub app in Chat to get notifications about GitHub events, such as issues, pull requests, and comments.

### Before you begin

To use the GitHub app for Chat:

- You need permission to install apps from your Google Workspace administrator.
- Add the app to Chat. [Learn how to find apps and add them to Chat](https://support.google.com/chat/answer/7655820).
- You need a GitHub account.
- You need to install the [Google Chat app for your GitHub repository](https://github.com/apps/google-chat-app).

##### Understand GitHub app & OAuth app authentication mechanisms

This outlines the distinct characteristics and operational models of GitHub apps and OAuth apps, which serve as primary mechanisms for third-party services to integrate with and access GitHub resources. A comprehensive understanding of these differences is critical to maintain an optimal security posture within an organization.

#### 1. Comparative analysis: Key distinctions

The fundamental differences between the 2 models reside in the identity used for access (the *Principal*) and the mechanism that governs resource authorization.

|                              |                                                                                                                                                                                                                    |                                                                                                                               |
|------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| **Attribute**                | **GitHub app (Recommended sign in)**                                                                                                                                                                               | **OAuth app (Legacy sign in)**                                                                                                |
| **Principal identity**       | Acts as an independent **Application Identity**, separate from any user, or on behalf of the authorizing user, depending on the use case.                                                                          | Acts **on behalf of the authorizing user**, inheriting their privileges.                                                      |
| **Authorization model**      | **Fine-grained permissions (Recommended):** Utilizes the **Principle of Least Privilege**, allowing access to specific repositories and resource types. For example: Read access for metadata only.                | **Broad scopes:** Access is defined by wide scopes like granting access to **all resources** visible to the authorizing user. |
| **Credential longevity**     | **Short-lived tokens:** Access tokens possess a limited lifespan (typically 1 hour) and require frequent renewal, significantly mitigating risk in the event of compromise.                                        | **Long-lived tokens:** Access tokens persist until manually revoked by the user, representing a prolonged exposure risk.      |
| **Installation requirement** | Must be **installed** by an Administrator or Organization owner, establishing a formal link to the account or organization and authorized by the user for use cases where the app is acting on behalf of the user. | Must be **authorized** by an individual user, linking access directly to that user's identity.                                |

For more comprehensive documentation, refer to [Differences between GitHub Apps and OAuth apps](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/differences-between-github-apps-and-oauth-apps).

#### 2. Recommendation

Based on security best practices, the **GitHub App authentication mechanism is recommended** for all third-party and organizational integrations. This model enforces the **Principle of Least Privilege** and employs robust, time-limited credentials, thereby maintaining a higher standard of security and operational stability compared to the delegated authority model of OAuth Apps.

[Install the Google Chat App for GitHub repositories](https://github.com/apps/google-chat-app).

### Set up the GitHub app in Chat

1.  Open the Chat app .
2.  Open a direct message with the app or go to a space with the app.
3.  To open the configuration window, tap **Sign in**.
4.  Tap **Configure Access** and then **Sign in to GitHub**.
5.  Complete the sign-in process then close the popup.
6.  To update the Chat dialog, tap **Refresh**.
7.  Under **Add Repositories**, type the GitHub repository you want notifications for.
8.  Check the boxes for the events you want notifications for.
9.  Tap **Save**.

**Tip:** You need to set up notifications in each space where you add the app. The app sends notifications to all spaces where it's a member.

### Migrate from OAuth app (Legacy) to GitHub app (Recommended)

To migrate your current connection from the older OAuth app authentication method to the recommended GitHub app method:

1.  Open the Chat app .
2.  Open a direct message or space with the GitHub app.
3.  In the message field, tap Google Workspace tools .
4.  In the command list, select **GitHub Reauthorize**.
5.  To complete the migration and reauthorization process, follow the on-screen instructions in the Chat dialogue.

### Use the GitHub app in spaces

To use the app in spaces, you need to **@mention** or **/mention** the app in each message and in replies to the messages from the app.

The **@mention** or **/mention** confirms you've sent the message to the app and not to others in the space.

1.  Open the Chat app .
2.  In a space, enter **@github** or **/github** followed by the command.
    - When you mention **@github** or **/github**, the message is sent to the app and not to others in the space.

### Change app settings

In spaces, only the person who added the app can change the settings.

1.  Open the Chat app .
2.  Open a direct message with the app or go to a space with the app.
3.  To open the current settings for the app, enter: `/github_settings`.
4.  Change the settings as needed.
5.  Tap **Save**.

Removing the app from a space deletes the app settings.

### Learn about commands for the GitHub app in Chat

In the message field of a direct message or space with the GitHub app in Chat, you can use:

- **Slash commands:**
  - `/github_settings`: Opens the settings dialogue.
  - `/github_reminders`: For personal or team open pull requests, set up and edit scheduled reminders.
  - `/github_subscribe`: Subscribes to a GitHub \<repoURL\> or \<owner/repo\>.
  - `/github_openIssue`: Opens a new GitHub issue.
  - `/github_logout`: Logs out of your GitHub account.
  - `/github_help`: Displays the help message.
  - `/github_feedback`: Send feedback about the GitHub app.
- **Quick commands:** To access the quick commands, tap Google Workspace tools .
  - **GitHub Connect:** Displays a message with a “Sign in” and “Legacy Sign in” option.
  - **GitHub Reauthorize:** Allows you to migrate to a new connection method.

To get a full list of supported commands:

1.  On your iPhone or iPad, open the Chat app .
2.  Open a direct message or go to a space where the GitHub app is installed.
3.  Enter: `/github_help`.

### Troubleshoot issues with GitHub app in Chat

##### If you get an error when you subscribe to real-time notifications

##### GitHub app

To set up real-time notifications in spaces:

1.  In your browser, go to [GitHub profile settings](https://github.com/settings/profile).
2.  Under “Integrations,” tap **Applications** and then **Authorized GitHub apps**.
    - After you connect the GitHub app in Google Chat, your list of authorized apps shows “Google Chat.”
3.  [Install the Google Chat App for GitHub repository](https://github.com/apps/google-chat-app).
    - Or, you can request installation from the organization/repository owner.
4.  Wait until installation is complete.
5.  In Google Chat, open a direct message or space with the GitHub app.
6.  In the message field, to create a subscription, enter: `/github_subscribe [organisation/repo]` or `/github_settings`.

##### OAuth app

To set up real-time notifications in spaces, you must:

- Be an organization owner of the proposed repository.
- Authorize the app on the GitHub organization.
  1.  In your browser, go to [GitHub profile settings](https://github.com/settings/profile).
  2.  Under “Integrations,” tap **Applications** and then **Authorized OAuth apps**.
      - After you connect the GitHub app in Google Chat, your list of authorized apps shows “Google Chat.”
  3.  [Grant the app access to the organization you want to access](https://docs.github.com/articles/restricting-access-to-your-organization-s-data/).

##### If you receive too many notifications from the GitHub app

1.  In the message field, enter: `/github_settings`.
2.  To edit your repository notifications settings, tap **Notification settings**.
3.  To filter the notifications, next to each notification type, tap the down arrow .
    - It displays additional options to filter notifications.
4.  Check the boxes for the notifications you want.
5.  Tap **Save**.

##### If you don’t get @mentioned in scheduled reminders

To get mentioned in scheduled reminders, you must’ve connected your Google Chat account to the GitHub account.

1.  In the message field, enter: `/github_settings`.
2.  To connect your account:
    1.  In the pop-up, tap **Configure access** and then **Sign in to GitHub**.
    2.  Sign in to your GitHub account.
    3.  Authorize the app.
3.  In the message you receive from the GitHub app, select **Schedule reminders for your team**.
4.  In the pop-up:
    1.  Tap **Create new reminder.**
    2.  Configure the reminder settings.
    3.  Tap **Save**.

##### If you don't get reminders with GitHub App

On the repository from where you want to receive reminders, [verify the installation of the Google Chat App for GitHub](https://github.com/apps/google-chat-app/installations/select_target).

*Google, Google Workspace, and related marks and logos are trademarks of Google LLC. All other company and product names are trademarks of the companies with which they are associated.*
