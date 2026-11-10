---
fonte: https://support.google.com/appsheet/answer/12629371?hl=en
baixado: 2026-11-10
---

# Disable AppSheet databases

Disable AppSheet databases to prevent use by your team.

To fully prevent access to AppSheet databases, you must do **both** of the following:

- [Define the team policy](#team-policy) to prevent app creators from using AppSheet database tables and end users from using apps that are built with AppSheet databases
- [Enable the team setting](#team-setting) to prevent app creators on your team from using AppSheet databases in their apps

**Note: **You must have team root or admin privileges to define team policies and enable team settings.

## Define the team policy

Define the **Disable AppSheet databases** team policy to prevent:

- App creators from using AppSheet database tables in their apps
- End users from using apps that are built with AppSheet databases

When the team policy is in effect, if an AppSheet database table is used in an app the following error message displays in the app editor to indicate that use of AppSheet database tables is prevented.

Error displayed in app editor when team policy is in effect

To define the team policy:

1.  Select **My account \> Policies**.
2.  Click **+ Team Policy** to add a team policy.
    Do not add the policy as an individual account policy.
3.  Select **Disable AppSheet databases** from the **Policy Template** drop-down.
4.  Click **Next**.
5.  The policy is preconfigured for you. You can modify any of the field values. See [Add a predefined policy](https://support.google.com/appsheet/answer/11948767#add-predefined-policy) for a description of each field. 
6.  Click **Save**.

## Enable the team setting

Enable the team setting to prevent app creators on your team from using AppSheet databases in their apps. In this case, access to the AppSheet database editor is blocked with the following message:

Disabled AppSheet databases error

To enable the team setting:

1.  Select **My Team \> Settings**.
2.  Enable the **Disable AppSheet databases** setting.
3.  Click **Save.**
