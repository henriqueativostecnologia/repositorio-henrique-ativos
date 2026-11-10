---
fonte: https://support.google.com/chat/answer/13790449?hl=en
baixado: 2026-11-10
---

# Use the Workday app in Google Chat

This article has different instructions for each platform/version: Computer, Android phone & tablet, iPhone & iPad. All versions are copied below.

## Version: Computer

You can complete Workday quick actions from Chat with Google Chat and Workday integration. To access features, a Workday admin has to configure the app for their domain or organization. You can then install the app from within Chat. A Workspace admin can also install the app on your behalf.

##### For Workday admins: Learn how to integrate Workday with Google Chat

#### Step 1: Configure Integration System and Credentials

1.  Sign in to Workday.
    1.  Go to your Workday tenant.
    2.  Sign in with your administrator account.
2.  Configure event subscriptions to enable notifications:
    - **Create integration system:**
      1.  In the search bar, enter “Create Integration System” and select the task.
      2.  When the window opens, enter a system name (for example, Chat_Integration).
      3.  For Template, select **Subscriber_Integration** from the list.
      4.  Select **OK**.
    - **Set up event subscription:**
      1.  In the created “Integration System View,” open the Related Actions menu. This is under the dot button located next to the System Name.
      2.  Select **Integration** **System** and then **Edit Subscriptions**.
      3.  Select **Subscribe to all Business Processes**.
      4.  Set Notification URL: [https://workday-bot-production.appspot.com/workdayEvent](https://workday-bot-production.appspot.com/workdayEvent)
      5.  Select **OK**.
    - **Enable OAuth 2.0 clients:**
      1.  In the search bar, enter “Edit Tenant Setup - Security”.
      2.  Select the task.
      3.  On the settings page, find the “OAuth 2.0 Settings” section.
      4.  Make sure the OAuth 2.0 Clients Enabled checkbox is selected.
      5.  Click **OK**.
3.  Create a new API client:
    1.  In the search bar, enter “Register API Client” and select the task.
    2.  You are prompted to set up the connection.
    3.  On the registration screen, fill out the following fields:
        - **Client Name:** Google Chat Workday Integration
        - **Client Grant Type:** Authorization Code Grant
        - **Access Token Type:** Bearer
        - **Redirection URI:** [https://workday-bot-production.appspot.com/authenticated/oauth2callback](https://workday-bot-production.appspot.com/authenticated/oauth2callback)
        - **Non-Expiring Refresh Tokens:** Checked
        - **Scope:** Contact Information, Staffing, Expenses, Time Off and Leave, Adaptive Planning for Financial Plans, Adaptive Planning for the Workforce, Tenant Non-Configurable, System
    4.  Save information from the following fields as you will need it later:
        - Client ID
        - Secret ID
        - Workday REST API Endpoint
        - Workday Token Endpoint
        - Workday Authorization Endpoint
4.  Create an ISU account: This special account handles the connection securely.
    1.  In the search bar, enter “Create Integration System User” and select the task.
    2.  You are prompted to set up the account.
    3.  On the setup screen, fill out the following fields:
        - **User Name:** Google Chat Workday ISU
        - **New Password:** Enter and verify new password
        - **Session Timeout Minutes:** 0
        - **Do Not Allow UI Sessions:** Should be unchecked
    4.  Select **OK**.
5.  Create a security group for the user (ISSG):
    1.  In the search bar, enter “Create Security Group” and select the task.
    2.  You are prompted to fill out the following fields:
        - **Select Type of Tenanted Security Group:** Integration System Security Group (Unconstrained)
        - **Name:** ISSG Google Chat Integration
    3.  Select **OK**.
    4.  Assign ISU to this ISSG.
6.  Assign ISSG permissions (domain security policy):
    1.  In the search bar, enter “Maintain Permissions for Security Group” and then select the task.
    2.  On the task page:
        - For “Operation,” select **Maintain**.
        - For “Source Security Group,” select the ISSG you just created (ISSG_GoogleChat_Integration).
    3.  Add the following Domain Security Policy Permissions to the ISSG:
        - **View or Modify Access:** View and Modify, **Domain Security Policy:** Workday Query Language, **Functional Areas:** System
        - **View or Modify Access:** View Only, **Domain Security Policy:** Worker Data: Public Worker Reports, **Functional Areas:** Staffing
        - **View or Modify Access:** View Only, **Domain Security Policy:** Business Process Administration, **Functional Areas:** System
        - **View or Modify Access:** View Only, **Domain Security Policy:** Worker Data: Current Management Level Information, **Functional Areas:** Staffing
    4.  Activate pending security policy changes.
        1.  In the search bar, enter “Activate Pending Security Policy Changes” and then select the task.
        2.  Enter a comment (for example, Permissions for Google Chat integration).
        3.  Select **OK**.
            - This applies all the permissions you just configured.
    5.  Continue with an ISU:
        1.  Log out of your Workday account.
        2.  Select **Next** to open the Workday setup.

#### Step 2: Provide API client details

1.  Prepare your API client details.
    - If you have not prepared the API client details, [refer to information in Step 1](#create-new-API-client).
2.  Fill in the following fields:
    - Client ID
    - Client Secret
    - Workday REST API Endpoint
    - Token Endpoint
    - Authorization Endpoint
3.  Select **Next**.

#### Step 3: Connect to Workday using an ISU account

This step securely authorizes Google Chat to access your Workday instance.

1.  Prepare your ISU account credentials.
    - If you have not created the ISU account, [refer to information in Step 1](#create-an-ISU-account).
2.  Select **Next**.
3.  Select **Configure Access** to open the Workday sign-in page in a new window.
4.  Sign in using your Integration System User (ISU) account credentials.
    - Use the Integration System User (ISU) account. Your personal Workday account is not supported for this step.
5.  After signing in and granting access in Workday, return to Google Chat.
6.  Select **Refresh**. This takes you to the final step.

#### Step 4: Sign in to Workday with your personal account

1.  Go to your Workday browser tab. If you see an error, an ISU session might still be active in another browser tab or window. Make sure you are only signed in to Workday with your personal account before continuing.
    1.  Sign out of the Integration System User (ISU) account.
    2.  Sign back in using your personal Workday account.
2.  Return to Google Chat.
3.  Select **Next**.
4.  Select **Configure Access**.
    - You are taken to a successful connection message.

### Before you begin

- You need permission from your Google Workspace administrator to install apps.
- You need to add the app to Chat. [Learn how to find apps and add them to Chat](https://support.google.com/hangoutschat/answer/7655820#addbots).
- Before you can set up your Workday app in Chat, your Workday Admin has to activate OAuth and create a new API client for the Google integration setup. Your Workday Admin will need the following information to proceed:
  - Client ID
  - Secret ID
  - Workday REST API Endpoint
  - Workday Token Endpoint
  - Workday Authorization Endpoint

### Set up the Workday app in Chat

1.  On your computer, open [Google Chat](https://chat.google.com).
2.  Open a direct message with the app.
    - You get a welcome message with info about the app and a prompt to connect your Workday account.
3.  To sign in to your Workday account and subdomain, click **Authorize**.
    **Tip:** To set up the app, you must sign in to a Workday account with Admin or Account owner permissions in the subdomain.
4.  Complete the sign in on the Workday website.
5.  Allow the Workday Chat app to access some Workday permissions.
6.  If prompted, select the correct Workday account to use.
7.  If the connection is successful:
    - To find a list of all available commands:
      1.  Select Menu .
      2.  Click the help command or type: `/workday`
    - Some examples of what you can do:
      - Submit, track, and review time off requests.
      - View your time-off balance.
      - Check company holidays.
      - Find contact details.
      - Start a new expense report.
      - Check tasks.
      - Get notifications when a new task is:
        - Assigned to you.
        - Completed.

### Related resources

- [Use apps in Google Chat](https://support.google.com/chat/answer/7655820)
- [Chat apps available from Google](https://support.google.com/chat/answer/9649420)

## Version: Android phone & tablet

You can complete Workday quick actions from Chat with Google Chat and Workday integration. To access features, a Workday admin has to configure the app for their domain or organization. You can then install the app from within Chat. A Workspace admin can also install the app on your behalf.

##### For Workday admins: Learn how to integrate Workday with Google Chat

#### Step 1: Configure Integration System and Credentials

1.  Sign in to Workday.
    1.  Go to your Workday tenant.
    2.  Sign in with your administrator account.
2.  Configure event subscriptions to enable notifications:
    - **Create integration system:**
      1.  In the search bar, enter “Create Integration System” and select the task.
      2.  When the window opens, enter a system name (for example, Chat_Integration).
      3.  For Template, select **Subscriber_Integration** from the list.
      4.  Select **OK**.
    - **Set up event subscription:**
      1.  In the created “Integration System View,” open the Related Actions menu. This is under the dot button located next to the System Name.
      2.  Select **Integration** **System** and then **Edit Subscriptions**.
      3.  Select **Subscribe to all Business Processes**.
      4.  Set Notification URL: [https://workday-bot-production.appspot.com/workdayEvent](https://workday-bot-production.appspot.com/workdayEvent)
      5.  Select **OK**.
    - **Enable OAuth 2.0 clients:**
      1.  In the search bar, enter “Edit Tenant Setup - Security”.
      2.  Select the task.
      3.  On the settings page, find the “OAuth 2.0 Settings” section.
      4.  Make sure the OAuth 2.0 Clients Enabled checkbox is selected.
      5.  Click **OK**.
3.  Create a new API client:
    1.  In the search bar, enter “Register API Client” and select the task.
    2.  You are prompted to set up the connection.
    3.  On the registration screen, fill out the following fields:
        - **Client Name:** Google Chat Workday Integration
        - **Client Grant Type:** Authorization Code Grant
        - **Access Token Type:** Bearer
        - **Redirection URI:** [https://workday-bot-production.appspot.com/authenticated/oauth2callback](https://workday-bot-production.appspot.com/authenticated/oauth2callback)
        - **Non-Expiring Refresh Tokens:** Checked
        - **Scope:** Contact Information, Staffing, Expenses, Time Off and Leave, Adaptive Planning for Financial Plans, Adaptive Planning for the Workforce, Tenant Non-Configurable, System
    4.  Save information from the following fields as you will need it later:
        - Client ID
        - Secret ID
        - Workday REST API Endpoint
        - Workday Token Endpoint
        - Workday Authorization Endpoint
4.  Create an ISU account: This special account handles the connection securely.
    1.  In the search bar, enter “Create Integration System User” and select the task.
    2.  You are prompted to set up the account.
    3.  On the setup screen, fill out the following fields:
        - **User Name:** Google Chat Workday ISU
        - **New Password:** Enter and verify new password
        - **Session Timeout Minutes:** 0
        - **Do Not Allow UI Sessions:** Should be unchecked
    4.  Select **OK**.
5.  Create a security group for the user (ISSG):
    1.  In the search bar, enter “Create Security Group” and select the task.
    2.  You are prompted to fill out the following fields:
        - **Select Type of Tenanted Security Group:** Integration System Security Group (Unconstrained)
        - **Name:** ISSG Google Chat Integration
    3.  Select **OK**.
    4.  Assign ISU to this ISSG.
6.  Assign ISSG permissions (domain security policy):
    1.  In the search bar, enter “Maintain Permissions for Security Group” and then select the task.
    2.  On the task page:
        - For “Operation,” select **Maintain**.
        - For “Source Security Group,” select the ISSG you just created (ISSG_GoogleChat_Integration).
    3.  Add the following Domain Security Policy Permissions to the ISSG:
        - **View or Modify Access:** View and Modify, **Domain Security Policy:** Workday Query Language, **Functional Areas:** System
        - **View or Modify Access:** View Only, **Domain Security Policy:** Worker Data: Public Worker Reports, **Functional Areas:** Staffing
        - **View or Modify Access:** View Only, **Domain Security Policy:** Business Process Administration, **Functional Areas:** System
        - **View or Modify Access:** View Only, **Domain Security Policy:** Worker Data: Current Management Level Information, **Functional Areas:** Staffing
    4.  Activate pending security policy changes.
        1.  In the search bar, enter “Activate Pending Security Policy Changes” and then select the task.
        2.  Enter a comment (for example, Permissions for Google Chat integration).
        3.  Select **OK**.
            - This applies all the permissions you just configured.
    5.  Continue with an ISU:
        1.  Log out of your Workday account.
        2.  Select **Next** to open the Workday setup.

#### Step 2: Provide API client details

1.  Prepare your API client details.
    - If you have not prepared the API client details, [refer to information in Step 1](#create-new-API-client).
2.  Fill in the following fields:
    - Client ID
    - Client Secret
    - Workday REST API Endpoint
    - Token Endpoint
    - Authorization Endpoint
3.  Select **Next**.

#### Step 3: Connect to Workday using an ISU account

This step securely authorizes Google Chat to access your Workday instance.

1.  Prepare your ISU account credentials.
    - If you have not created the ISU account, [refer to information in Step 1](#create-an-ISU-account).
2.  Select **Next**.
3.  Select **Configure Access** to open the Workday sign-in page in a new window.
4.  Sign in using your Integration System User (ISU) account credentials.
    - Use the Integration System User (ISU) account. Your personal Workday account is not supported for this step.
5.  After signing in and granting access in Workday, return to Google Chat.
6.  Select **Refresh**. This takes you to the final step.

#### Step 4: Sign in to Workday with your personal account

1.  Go to your Workday browser tab. If you see an error, an ISU session might still be active in another browser tab or window. Make sure you are only signed in to Workday with your personal account before continuing.
    1.  Sign out of the Integration System User (ISU) account.
    2.  Sign back in using your personal Workday account.
2.  Return to Google Chat.
3.  Select **Next**.
4.  Select **Configure Access**.
    - You are taken to a successful connection message.

### Before you begin

- You need permission from your Google Workspace administrator to install apps.
- You need to add the app to Chat. [Learn how to find apps and add them to Chat](https://support.google.com/hangoutschat/answer/7655820#addbots).
- Before you can set up your Workday app in Chat, your Workday Admin has to activate OAuth and create a new API client for the Google integration setup. Your Workday Admin will need the following information to proceed:
  - Client ID
  - Secret ID
  - Workday REST API Endpoint
  - Workday Token Endpoint
  - Workday Authorization Endpoint

### Set up the Workday app in Chat

1.  Open the Chat app or Gmail app .
2.  Open a direct message with the Workday app.
    - You get a welcome message with info about the app and a prompt to connect your Workday account.
3.  Below the welcome message, click **Help**.
4.  To sign in to your Workday account and subdomain, tap **Authorize**.
    **Tip:** To set up the app, you must sign in to a Workday account with Admin or Account owner permissions in the subdomain.
5.  Complete the sign in on the Workday website.
6.  Allow the Workday Chat app to access some Workday permissions.
7.  If prompted, select the correct Workday account to use.
8.  If the connection is successful:
    - To find a list of all available commands:
      1.  Select Menu .
      2.  Click the help command or type: `/workday`
    - Some examples of what you can do:
      - Submit, track, and review time off requests.
      - View your time-off balance.
      - Check company holidays.
      - Find contact details.
      - Start a new expense report.
      - Check tasks.
      - Get notifications when a new task is:
        - Assigned to you.
        - Completed.

### Related resources

- [Use apps in Google Chat](https://support.google.com/chat/answer/7655820)
- [Chat apps available from Google](https://support.google.com/chat/answer/9649420)

## Version: iPhone & iPad

You can complete Workday quick actions from Chat with Google Chat and Workday integration. To access features, a Workday admin has to configure the app for their domain or organization. You can then install the app from within Chat. A Workspace admin can also install the app on your behalf.

##### For Workday admins: Learn how to integrate Workday with Google Chat

#### Step 1: Configure Integration System and Credentials

1.  Sign in to Workday.
    1.  Go to your Workday tenant.
    2.  Sign in with your administrator account.
2.  Configure event subscriptions to enable notifications:
    - **Create integration system:**
      1.  In the search bar, enter “Create Integration System” and select the task.
      2.  When the window opens, enter a system name (for example, Chat_Integration).
      3.  For Template, select **Subscriber_Integration** from the list.
      4.  Select **OK**.
    - **Set up event subscription:**
      1.  In the created “Integration System View,” open the Related Actions menu. This is under the dot button located next to the System Name.
      2.  Select **Integration** **System** and then **Edit Subscriptions**.
      3.  Select **Subscribe to all Business Processes**.
      4.  Set Notification URL: [https://workday-bot-production.appspot.com/workdayEvent](https://workday-bot-production.appspot.com/workdayEvent)
      5.  Select **OK**.
    - **Enable OAuth 2.0 clients:**
      1.  In the search bar, enter “Edit Tenant Setup - Security”.
      2.  Select the task.
      3.  On the settings page, find the “OAuth 2.0 Settings” section.
      4.  Make sure the OAuth 2.0 Clients Enabled checkbox is selected.
      5.  Click **OK**.
3.  Create a new API client:
    1.  In the search bar, enter “Register API Client” and select the task.
    2.  You are prompted to set up the connection.
    3.  On the registration screen, fill out the following fields:
        - **Client Name:** Google Chat Workday Integration
        - **Client Grant Type:** Authorization Code Grant
        - **Access Token Type:** Bearer
        - **Redirection URI:** [https://workday-bot-production.appspot.com/authenticated/oauth2callback](https://workday-bot-production.appspot.com/authenticated/oauth2callback)
        - **Non-Expiring Refresh Tokens:** Checked
        - **Scope:** Contact Information, Staffing, Expenses, Time Off and Leave, Adaptive Planning for Financial Plans, Adaptive Planning for the Workforce, Tenant Non-Configurable, System
    4.  Save information from the following fields as you will need it later:
        - Client ID
        - Secret ID
        - Workday REST API Endpoint
        - Workday Token Endpoint
        - Workday Authorization Endpoint
4.  Create an ISU account: This special account handles the connection securely.
    1.  In the search bar, enter “Create Integration System User” and select the task.
    2.  You are prompted to set up the account.
    3.  On the setup screen, fill out the following fields:
        - **User Name:** Google Chat Workday ISU
        - **New Password:** Enter and verify new password
        - **Session Timeout Minutes:** 0
        - **Do Not Allow UI Sessions:** Should be unchecked
    4.  Select **OK**.
5.  Create a security group for the user (ISSG):
    1.  In the search bar, enter “Create Security Group” and select the task.
    2.  You are prompted to fill out the following fields:
        - **Select Type of Tenanted Security Group:** Integration System Security Group (Unconstrained)
        - **Name:** ISSG Google Chat Integration
    3.  Select **OK**.
    4.  Assign ISU to this ISSG.
6.  Assign ISSG permissions (domain security policy):
    1.  In the search bar, enter “Maintain Permissions for Security Group” and then select the task.
    2.  On the task page:
        - For “Operation,” select **Maintain**.
        - For “Source Security Group,” select the ISSG you just created (ISSG_GoogleChat_Integration).
    3.  Add the following Domain Security Policy Permissions to the ISSG:
        - **View or Modify Access:** View and Modify, **Domain Security Policy:** Workday Query Language, **Functional Areas:** System
        - **View or Modify Access:** View Only, **Domain Security Policy:** Worker Data: Public Worker Reports, **Functional Areas:** Staffing
        - **View or Modify Access:** View Only, **Domain Security Policy:** Business Process Administration, **Functional Areas:** System
        - **View or Modify Access:** View Only, **Domain Security Policy:** Worker Data: Current Management Level Information, **Functional Areas:** Staffing
    4.  Activate pending security policy changes.
        1.  In the search bar, enter “Activate Pending Security Policy Changes” and then select the task.
        2.  Enter a comment (for example, Permissions for Google Chat integration).
        3.  Select **OK**.
            - This applies all the permissions you just configured.
    5.  Continue with an ISU:
        1.  Log out of your Workday account.
        2.  Select **Next** to open the Workday setup.

#### Step 2: Provide API client details

1.  Prepare your API client details.
    - If you have not prepared the API client details, [refer to information in Step 1](#create-new-API-client).
2.  Fill in the following fields:
    - Client ID
    - Client Secret
    - Workday REST API Endpoint
    - Token Endpoint
    - Authorization Endpoint
3.  Select **Next**.

#### Step 3: Connect to Workday using an ISU account

This step securely authorizes Google Chat to access your Workday instance.

1.  Prepare your ISU account credentials.
    - If you have not created the ISU account, [refer to information in Step 1](#create-an-ISU-account).
2.  Select **Next**.
3.  Select **Configure Access** to open the Workday sign-in page in a new window.
4.  Sign in using your Integration System User (ISU) account credentials.
    - Use the Integration System User (ISU) account. Your personal Workday account is not supported for this step.
5.  After signing in and granting access in Workday, return to Google Chat.
6.  Select **Refresh**. This takes you to the final step.

#### Step 4: Sign in to Workday with your personal account

1.  Go to your Workday browser tab. If you see an error, an ISU session might still be active in another browser tab or window. Make sure you are only signed in to Workday with your personal account before continuing.
    1.  Sign out of the Integration System User (ISU) account.
    2.  Sign back in using your personal Workday account.
2.  Return to Google Chat.
3.  Select **Next**.
4.  Select **Configure Access**.
    - You are taken to a successful connection message.

### Before you begin

- You need permission from your Google Workspace administrator to install apps.
- You need to add the app to Chat. [Learn how to find apps and add them to Chat](https://support.google.com/hangoutschat/answer/7655820#addbots).
- Before you can set up your Workday app in Chat, your Workday Admin has to activate OAuth and create a new API client for the Google integration setup. Your Workday Admin will need the following information to proceed:
  - Client ID
  - Secret ID
  - Workday REST API Endpoint
  - Workday Token Endpoint
  - Workday Authorization Endpoint

### Set up the Workday app in Chat

1.  Open the Chat app or Gmail app .
2.  Open a direct message with the Workday app.
    - You get a welcome message with info about the app and a prompt to connect your Workday account.
3.  Below the welcome message, click **Help**.
4.  To sign in to your Workday account and subdomain, tap **Authorize**.
    **Tip:** To set up the app, you must sign in to a Workday account with Admin or Account owner permissions in the subdomain.
5.  Complete the sign in on the Workday website.
6.  Allow the Workday Chat app to access some Workday permissions.
7.  If prompted, select the correct Workday account to use.
8.  If the connection is successful:
    - To find a list of all available commands:
      1.  Select Menu .
      2.  Click the help command or type: `/workday`
    - Some examples of what you can do:
      - Submit, track, and review time off requests.
      - View your time-off balance.
      - Check company holidays.
      - Find contact details.
      - Start a new expense report.
      - Check tasks.
      - Get notifications when a new task is:
        - Assigned to you.
        - Completed.

### Related resources

- [Use apps in Google Chat](https://support.google.com/chat/answer/7655820)
- [Chat apps available from Google](https://support.google.com/chat/answer/9649420)
