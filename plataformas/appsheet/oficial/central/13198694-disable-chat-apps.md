---
fonte: https://support.google.com/appsheet/answer/13198694?hl=en
baixado: 2026-11-10
---

# Disable Chat apps

Disable Chat apps in one of the following ways:

- [Turn off Chat apps in your app](#disable-chat-apps-app)
- [Prevent app creators from enabling Chat apps with AppSheet](#prevent-chat-apps)

See also [Turn chat on or off for your organization](https://support.google.com/a/answer/9071576) in the Google Workspace Admin documentation.

## Turn off Chat apps in your app

To turn off Chat apps in your app:

1.   Open the app in the app editor.
2.  Click Chat apps  in the left navigation.

    Click Chat in the left navigation
3.   Turn off the **Enable Chat app** setting**.**

    Disable Chat app
4.  To clean up resources, you may also want to delete the Google Cloud project associated with the app if it is no longer required. See [Shutting down (deleting) projects](https://cloud.google.com/resource-manager/docs/creating-managing-projects#shutting_down_projects). This step is optional.

## Prevent app creators from enabling Chat apps with AppSheet

Prevents app creators from enabling their AppSheet apps to run as Chat apps by using the "Disable Chat apps" policy, as described below. For more information, see [Define governance policies](https://support.google.com/appsheet/answer/11948767).

To app creators from enabling Chat apps with AppSheet:

1.  Select **My account \> Policies**.
2.  Click **+ Account Policy** or **+ Team Policy** to add an account or team policy, respectively.
3.  Select **Disable Chat apps** from the **Policy Template** drop-down.
4.  Click **Next**.
5.  The policy is preconfigured for you. You can modify any of the field values. See [Add a predefined policy](https://support.google.com/appsheet/answer/11948767#add-predefined-policy) for a description of each field. 
    **Important**: If you modify the **Condition** field, ensure that you retain the functionality defined below:`[EnableChatbot] = false`
6.  Click **Save**.
