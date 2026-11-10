---
fonte: https://support.google.com/chat/answer/9632289?hl=en
baixado: 2026-11-10
---

# Use the Salesforce app in Google Chat

This article has different instructions for each platform/version: Computer, Android phone & tablet, iPhone & iPad. All versions are copied below.

## Version: Computer

Use the Salesforce app in Chat to search for accounts, contacts, leads, and opportunities in Salesforce.

### For Salesforce Admins: Learn how to integrate Salesforce with Google Chat

#### Salesforce & Google Chat Integration Guide for Salesforce Administrators

#### 1. Introduction

This guide provides step-by-step instructions for configuring your Salesforce organization to support the Google Chat integration. This integration uses a per-user authentication model, allowing users to securely connect their own accounts to use Salesforce functionalities directly from Google Chat.

#### 2. Prerequisites

- **Salesforce Edition:** Enterprise, Unlimited, Performance, or Developer Edition. API request limits and allocations are available at the following link: [*Salesforce API limits*](https://developer.salesforce.com/docs/atlas.en-us.salesforce_app_limits_cheatsheet.meta/salesforce_app_limits_cheatsheet/salesforce_app_limits_platform_api.htm)
- **Administrator Permissions:** You must be a Salesforce Administrator with permissions to create External Client Apps and Permission Sets.

#### 3. Configuration

###### Step 1: Install and Authorize Salesforce chat app

1.  Open Chat.
2.  Open a direct message with the app or go to a space with the app.
3.  Click the “Sign in” button. If you don’t see it, then initiate /sf_search command.
4.  In the opened dialog click configure.
5.  Sign in to Salesforce using your Salesforce admin account.
6.  At the "Allow Access" window, click Allow and then close your browser tab.

###### Step 2: Install Salesforce Connected app

1.  Sign in to Salesforce using your Salesforce admin account.
2.  Navigate to **Setup** and then **Apps** and then **Connected Apps** and then **Connected Apps OAuth Usage** menu item.
3.  Find **“Salesforce for Google Chat”** Connected app and **Install** the app

###### Step 3: Create a Custom Permission Set for Users

This Permission Set will grant users the specific object and field access needed to use the integration's features.

- **A. Create the Custom Permission Set:**
  1.  Navigate to **Setup** and then **Users** and then **Permission Sets**.
  2.  Click **New**.
  3.  Enter the following details:
      - **Label:** `Google Chat Integration Access`
      - **API Name:** `Google_Chat_Integration_Access`
  4.  Click **Save**.
- **B. Configure Object and Field Permissions:**
  1.  In the newly created Permission Set, click **Object Settings**.
  2.  For each object, click its name, click **Edit**, and configure the specified Object Permissions and Field-Level Security. To be searchable, objects must have **Read** access enabled.
  3.  Click **Save**.
- **C. Configure System Permissions:**

1.  In the newly created Permission Set, click **System Permissions**.
2.  Click **Edit**.
3.  Check the box for **API Enabled** and click **Save**. This permission is required for users to make any API calls.

For more comprehensive documentation, please refer to the following link: [*Create a Salesforce Permission Set*](https://help.salesforce.com/s/articleView?id=ind.task_create_a_sf_perm_set.htm&type=5)

###### Step 4: Assign Permissions to Users

Assign the new Permission Set to all users who need to use the Google Chat integration.

1.  Navigate back to the `Google Chat Integration Access` Permission Set.
2.  Click **Manage Assignments**.
3.  Click **Add Assignments**.
4.  Select the checkboxes next to all users who should have access to the integration.
5.  Click **Assign**.

###### Step 5: Post-Installation

Newly provisioned users may initially encounter limited or absent results when utilizing the /sf_search command within the Google Chat application. This occurs until a search activity profile is established within Salesforce, a process that typically spans a few days. To enable full functionality of the /sf_search command in Google Chat, users are required to perform searches via the Salesforce user interface during this initial period. To expedite this process, users can also [*pin the most important record types in the Salesforce classic search results*](https://www.youtube.com/watch?v=byC6ioDukzc).

### Before you begin

- You need permission to install apps from your Google Workspace administrator.
- Add the app to Chat. [Learn how to find apps and add them to Chat](https://support.google.com/chat/answer/7655820).
- You need a Salesforce account.
- To enable full-integration functionality, Salesforce admin must configure permissions in Salesforce.

### Set up the Salesforce app in Chat

1.  Open [Google Chat](https://chat.google.com).
2.  Open a direct message with the app or go to a space with the app.
    - You get a message with info about the app and a prompt to connect your Salesforce account.
3.  Click **Sign in**.
4.  Sign in to your Salesforce account.
5.  At the "Allow Access" window, click **Allow** and then close your browser.
6.  If the connection is successful, you can:
    - Find a list of available commands:
      1.  Select Menu .
      2.  Click **Help**.
          - Or, you can enter: `/salesforce`.
    - Get rich link previews and interactive cards once a link to a Salesforce record is shared.
    - Get record details when you enter `/sf_search`.
    - Create and attach notes to Salesforce records:
      1.  Open a Salesforce record through a rich link preview or interactive card.
      2.  Click **Add a note**.
      3.  Enter a title and body for your note.
      4.  Click **Save note**.
          - You’ll get a confirmation message in Google Chat.

*Google, Google Workspace, and related marks and logos are trademarks of Google LLC. All other company and product names are trademarks of the companies with which they are associated.*

## Version: Android phone & tablet

Use the Salesforce app in Chat to search for accounts, contacts, leads, and opportunities in Salesforce.

### For Salesforce Admins: Learn how to integrate Salesforce with Google Chat

#### Salesforce & Google Chat Integration Guide for Salesforce Administrators

#### 1. Introduction

This guide provides step-by-step instructions for configuring your Salesforce organization to support the Google Chat integration. This integration uses a per-user authentication model, allowing users to securely connect their own accounts to use Salesforce functionalities directly from Google Chat.

#### 2. Prerequisites

- **Salesforce Edition:** Enterprise, Unlimited, Performance, or Developer Edition. API request limits and allocations are available at the following link: [*Salesforce API limits*](https://developer.salesforce.com/docs/atlas.en-us.salesforce_app_limits_cheatsheet.meta/salesforce_app_limits_cheatsheet/salesforce_app_limits_platform_api.htm)
- **Administrator Permissions:** You must be a Salesforce Administrator with permissions to create External Client Apps and Permission Sets.

#### 3. Configuration

###### Step 1: Install and Authorize Salesforce chat app

1.  Open Chat.
2.  Open a direct message with the app or go to a space with the app.
3.  Click the “Sign in” button. If you don’t see it, then initiate /sf_search command.
4.  In the opened dialog click configure.
5.  Sign in to Salesforce using your Salesforce admin account.
6.  At the "Allow Access" window, click Allow and then close your browser tab.

###### Step 2: Install Salesforce Connected app

1.  Sign in to Salesforce using your Salesforce admin account.
2.  Navigate to **Setup** and then **Apps** and then **Connected Apps** and then **Connected Apps OAuth Usage** menu item.
3.  Find **“Salesforce for Google Chat”** Connected app and **Install** the app

###### Step 3: Create a Custom Permission Set for Users

This Permission Set will grant users the specific object and field access needed to use the integration's features.

- **A. Create the Custom Permission Set:**
  1.  Navigate to **Setup** and then **Users** and then **Permission Sets**.
  2.  Click **New**.
  3.  Enter the following details:
      - **Label:** `Google Chat Integration Access`
      - **API Name:** `Google_Chat_Integration_Access`
  4.  Click **Save**.
- **B. Configure Object and Field Permissions:**
  1.  In the newly created Permission Set, click **Object Settings**.
  2.  For each object, click its name, click **Edit**, and configure the specified Object Permissions and Field-Level Security. To be searchable, objects must have **Read** access enabled.
  3.  Click **Save**.
- **C. Configure System Permissions:**

1.  In the newly created Permission Set, click **System Permissions**.
2.  Click **Edit**.
3.  Check the box for **API Enabled** and click **Save**. This permission is required for users to make any API calls.

For more comprehensive documentation, please refer to the following link: [*Create a Salesforce Permission Set*](https://help.salesforce.com/s/articleView?id=ind.task_create_a_sf_perm_set.htm&type=5)

###### Step 4: Assign Permissions to Users

Assign the new Permission Set to all users who need to use the Google Chat integration.

1.  Navigate back to the `Google Chat Integration Access` Permission Set.
2.  Click **Manage Assignments**.
3.  Click **Add Assignments**.
4.  Select the checkboxes next to all users who should have access to the integration.
5.  Click **Assign**.

###### Step 5: Post-Installation

Newly provisioned users may initially encounter limited or absent results when utilizing the /sf_search command within the Google Chat application. This occurs until a search activity profile is established within Salesforce, a process that typically spans a few days. To enable full functionality of the /sf_search command in Google Chat, users are required to perform searches via the Salesforce user interface during this initial period. To expedite this process, users can also [*pin the most important record types in the Salesforce classic search results*](https://www.youtube.com/watch?v=byC6ioDukzc).

### Before you begin

- You need permission to install apps from your Google Workspace administrator.
- Add the app to Chat. [Learn how to find apps and add them to Chat](https://support.google.com/chat/answer/7655820).
- You need a Salesforce account.
- To enable full-integration functionality, Salesforce admin must configure permissions in Salesforce.

### Set up the Salesforce app in Chat

1.  Open the Chat app .
2.  Open a direct message with the app or go to a space with the app.
    - You get a message with info about the app and a prompt to connect your Salesforce account.
3.  Tap **Sign in**.
4.  Sign in to your Salesforce account.
5.  At the "Allow Access" window, tap **Allow** and then close your browser window.
6.  If the connection is successful, you can:
    - Find a list of available commands:
      1.  Select Menu .
      2.  Tap **Help**.
          - Or, you can enter: `/salesforce`.
    - Get rich link previews and interactive cards once a link to a Salesforce record is shared.
    - Get record details when you enter `/sf_search`.
    - Create and attach notes to Salesforce records:
      1.  Open a Salesforce record through a rich link preview or interactive card.
      2.  Tap **Add a note**.
      3.  Enter a title and body for your note.
      4.  Tap **Save note**.
          - You’ll get a confirmation message in Google Chat.

*Google, Google Workspace, and related marks and logos are trademarks of Google LLC. All other company and product names are trademarks of the companies with which they are associated.*

## Version: iPhone & iPad

Use the Salesforce app in Chat to search for accounts, contacts, leads, and opportunities in Salesforce.

### For Salesforce Admins: Learn how to integrate Salesforce with Google Chat

#### Salesforce & Google Chat Integration Guide for Salesforce Administrators

#### 1. Introduction

This guide provides step-by-step instructions for configuring your Salesforce organization to support the Google Chat integration. This integration uses a per-user authentication model, allowing users to securely connect their own accounts to use Salesforce functionalities directly from Google Chat.

#### 2. Prerequisites

- **Salesforce Edition:** Enterprise, Unlimited, Performance, or Developer Edition. API request limits and allocations are available at the following link: [*Salesforce API limits*](https://developer.salesforce.com/docs/atlas.en-us.salesforce_app_limits_cheatsheet.meta/salesforce_app_limits_cheatsheet/salesforce_app_limits_platform_api.htm)
- **Administrator Permissions:** You must be a Salesforce Administrator with permissions to create External Client Apps and Permission Sets.

#### 3. Configuration

###### Step 1: Install and Authorize Salesforce chat app

1.  Open Chat.
2.  Open a direct message with the app or go to a space with the app.
3.  Click the “Sign in” button. If you don’t see it, then initiate /sf_search command.
4.  In the opened dialog click configure.
5.  Sign in to Salesforce using your Salesforce admin account.
6.  At the "Allow Access" window, click Allow and then close your browser tab.

###### Step 2: Install Salesforce Connected app

1.  Sign in to Salesforce using your Salesforce admin account.
2.  Navigate to **Setup** and then **Apps** and then **Connected Apps** and then **Connected Apps OAuth Usage** menu item.
3.  Find **“Salesforce for Google Chat”** Connected app and **Install** the app

###### Step 3: Create a Custom Permission Set for Users

This Permission Set will grant users the specific object and field access needed to use the integration's features.

- **A. Create the Custom Permission Set:**
  1.  Navigate to **Setup** and then **Users** and then **Permission Sets**.
  2.  Click **New**.
  3.  Enter the following details:
      - **Label:** `Google Chat Integration Access`
      - **API Name:** `Google_Chat_Integration_Access`
  4.  Click **Save**.
- **B. Configure Object and Field Permissions:**
  1.  In the newly created Permission Set, click **Object Settings**.
  2.  For each object, click its name, click **Edit**, and configure the specified Object Permissions and Field-Level Security. To be searchable, objects must have **Read** access enabled.
  3.  Click **Save**.
- **C. Configure System Permissions:**

1.  In the newly created Permission Set, click **System Permissions**.
2.  Click **Edit**.
3.  Check the box for **API Enabled** and click **Save**. This permission is required for users to make any API calls.

For more comprehensive documentation, please refer to the following link: [*Create a Salesforce Permission Set*](https://help.salesforce.com/s/articleView?id=ind.task_create_a_sf_perm_set.htm&type=5)

###### Step 4: Assign Permissions to Users

Assign the new Permission Set to all users who need to use the Google Chat integration.

1.  Navigate back to the `Google Chat Integration Access` Permission Set.
2.  Click **Manage Assignments**.
3.  Click **Add Assignments**.
4.  Select the checkboxes next to all users who should have access to the integration.
5.  Click **Assign**.

###### Step 5: Post-Installation

Newly provisioned users may initially encounter limited or absent results when utilizing the /sf_search command within the Google Chat application. This occurs until a search activity profile is established within Salesforce, a process that typically spans a few days. To enable full functionality of the /sf_search command in Google Chat, users are required to perform searches via the Salesforce user interface during this initial period. To expedite this process, users can also [*pin the most important record types in the Salesforce classic search results*](https://www.youtube.com/watch?v=byC6ioDukzc).

### Before you begin

- You need permission to install apps from your Google Workspace administrator.
- Add the app to Chat. [Learn how to find apps and add them to Chat](https://support.google.com/chat/answer/7655820).
- You need a Salesforce account.
- To enable full-integration functionality, Salesforce admin must configure permissions in Salesforce.

### Set up the Salesforce app in Chat

1.  Open the Chat app .
2.  Open a direct message with the app or go to a space with the app.
    - You get a message with info about the app and a prompt to connect your Salesforce account.
3.  Tap **Sign in**.
4.  Sign in to your Salesforce account.
5.  At the "Allow Access" window, tap **Allow** and then close your browser window.
6.  If the connection is successful, you can:
    - Find a list of available commands:
      1.  Select Menu .
      2.  Tap **Help**.
          - Or, you can enter: `/salesforce`.
    - Get rich link previews and interactive cards once a link to a Salesforce record is shared.
    - Get record details when you enter `/sf_search`.
    - Create and attach notes to Salesforce records:
      1.  Open a Salesforce record through a rich link preview or interactive card.
      2.  Tap **Add a note**.
      3.  Enter a title and body for your note.
      4.  Tap **Save note**.
          - You’ll get a confirmation message in Google Chat.

*Google, Google Workspace, and related marks and logos are trademarks of Google LLC. All other company and product names are trademarks of the companies with which they are associated.*
