---
fonte: https://support.google.com/appsheet/answer/14836137?hl=en
baixado: 2026-11-10
---

# Prevent app creators from using Google Forms

You must be a **Google Workspace user** to build AppSheet automations with Google Forms. See [Add AppSheet to Google Workspace](https://support.google.com/a/answer/10447197).

If you are using your Google Workspace account, the [Google Workspace Terms of Service](https://workspace.google.com/terms/premier_terms/) govern your use of Google Forms. Otherwise, refer to the [Google Terms of Service](https://policies.google.com/terms).

Prevents app creators from [using Google Forms](#prevent-using-google-forms) or [building automations using Google Forms](#prevent-build-automations-using-google-forms) in apps, as described in the following sections. For more information, see [Define governance policies](https://support.google.com/appsheet/answer/11948767).

## Prevent app creators from using Google Forms

To prevent app creators from [creating apps using Google Forms](https://support.google.com/appsheet/answer/14824665) or [adding tables](https://support.google.com/appsheet/answer/10105821#add) based on forms from Google Forms:

1.  Select **My account \> Policies**.
2.  Click **+ Organization Policy** or **+ Team Policy** to add an account or team policy, respectively.
3.  Select **Disable Google Forms Table** from the **Policy Template** drop-down.
4.  Click **Next**.
5.  The policy is preconfigured for you. You can modify any of the field values. See [Add a predefined policy](https://support.google.com/appsheet/answer/11948767#add-predefined-policy) for a description of each field. 
    **Important**: If you modify the **Condition** field, ensure that you retain the functionality defined below: `NOT([SourceType] = 'FORMS')`
6.  Click **Save**.

## Prevent app creators from building automations using Google Forms

To prevent app creators from building automations using Google Forms:

1.  Select **My account \> Policies**.
2.  Click **+ Organization Policy** or **+ Team Policy** to add an account or team policy, respectively.
3.  Select **Disable Google Forms Events** from the **Policy Template** drop-down.
4.  Click **Next**.
5.  The policy is preconfigured for you. You can modify any of the field values. See [Add a predefined policy](https://support.google.com/appsheet/answer/11948767#add-predefined-policy) for a description of each field. 
    **Important**: If you modify the **Condition** field, ensure that you retain the functionality defined below:
     `NOT([EventType] = 'Forms')`
6.  Click **Save**.
