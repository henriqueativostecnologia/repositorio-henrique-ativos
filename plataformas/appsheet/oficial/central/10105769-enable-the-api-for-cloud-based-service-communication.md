---
fonte: https://support.google.com/appsheet/answer/10105769?hl=en
baixado: 2026-11-10
---

# Enable the API for cloud-based service communication

**Note**: This feature is supported for Enterprise plans only. 

Enable the API to allow cloud-based services like Looker Studio and Zapier to communicate with your app.

**Note**: Every API request **must** include an Application Access Key. AppSheet verifies the Application Access Key before performing the API call. This ensures that only authorized API calls are performed.

-  [Enable the API](#enable-api)
- [Prevent app creators from enabling the API](#prevent-enabling-api)

## Enable the API

To enable the API:

1.   Open the app in the app editor.
2.  Select **Settings \> Integrations**.
3.  Under **IN: from cloud services to your app**, enable the **Enable** toggle.
    This enables the API for the application as a whole.
4.  Ensure that at least one unexpired **Application Access Key** is present.
    Otherwise, click **Create Application Access Key**.
5.  Save the app.

We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

 

## If you are using the legacy navigation

 To configure AppSheet integrations:

1.  Open the app in the editor
2.  Go to the **Manage \> Integrations** pane.
3.  Expand **IN: from cloud services to your app**.
4.  Enable the **Enable** toggle.
    This enables the API for the application as a whole.
5.  Ensure that at least one unexpired **Application Access Key** is present.
    Otherwise, click **Create Application Access Key**.
6.  Save the app.

## Prevent app creators from enabling the API

Prevent app creators from enabling the API by using the "Disable external integration through app API" policy, as described below. For more information, see [Define governance policies](https://support.google.com/appsheet/answer/11948767).

To app creators from enabling the API:

1.   Sign in to [AppSheet](https://www.appsheet.com).
2.   Select your account from the account profile drop-down to go to the **My account** page.

    Access the My account page
3.  Select the **Policies** tab.
4.  Click **+ Account Policy** or **+ Team Policy** to add an account or team policy, respectively.
5.  Select **Disable external integration through app API** from the **Policy Template** drop-down.
6.  Click **Next**.
7.  The policy is preconfigured for you. You can modify any of the field values. See [Add a predefined policy](https://support.google.com/appsheet/answer/11948767#add-predefined-policy) for a description of each field. 
    **Important**: If you modify the **Condition** field, ensure that you retain the functionality defined below:
    `[EnableAPI]=false`
8.  Click **Save**.
