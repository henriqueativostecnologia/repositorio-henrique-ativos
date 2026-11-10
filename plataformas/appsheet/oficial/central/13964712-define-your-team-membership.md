---
fonte: https://support.google.com/appsheet/answer/13964712?hl=en
baixado: 2026-11-10
---

# Define your team membership

Define your team membership based on the following:

- [**Google Workspace organization**](#workspace-org-private-domain) - All users in a Google Workspace account, regardless of organizational unit, domain, or group, are team members. 
- [**Private domain**](#workspace-org-private-domain) - All users in a private domain (such as @mycompany.com). **Note**: Only private domains are supported at this time; adding a public domain to a team is not supported.
- [**Google Group**](#google-microsoft-groups) - Users in a Google Group within your organization are team members.
- [**Microsoft Group**](#google-microsoft-groups) - Users in a Microsoft Group within your organization are team members.
  **Note**: To define your team membership using a Google Group or Microsoft Group, you must have:

  - **Team root** permissions
  - An auth domain that has permissions to list Google Groups and members, or Microsoft Groups and members

Define your team membership as described in the following sections:

- [Define team membership using a Google Workspace organization or private domain](#workspace-org-private-domain)
- [Define team membership using a Google Group or Microsoft Group](#google-microsoft-groups)
- [Troubleshoot issues with team membership](#troubleshoot)

## Define team membership using a Google Workspace organization or private domain

If your team membership is defined using a **Google Workspace organization** or **private domain**, it will be set up automatically for you and at least one user will be assigned as team root. **No further action is required**.

## Define team membership using a Google Group or Microsoft Group

Each team must have at least one user assigned as team root. When you create a new team, your account is automatically moved to the new team and assigned as team root. **If you are the only team root account on the existing team, before you define a new team you need to contact support and request a second user be assigned as team root**. Otherwise, you will be prevented from defining a new team and the following message will be displayed: 

`Creating a new team is not allowed because it would leave your current team without a root user.`

When connecting to a Google group in your organization, AppSheet uses the **group ID** and not the group name. If the group ID changes for any reason (for example, if you delete and recreate the Google group), this connection will need to be reconfigured. See [Connect AppSheet to the groups in your organization](https://support.google.com/appsheet/answer/10104381#connect-appsheet).

To define team membership using a **Google Group** or **Microsoft Group**:

1.  Sign in to [AppSheet](http://www.appsheet.com).
2.  Do one of the following:
    - Select **Admin Console** in the account profile drop-down, go to the **Accounts** page, and select **More**  **\>** **Create a team**.
    - Select **My team** in the account profile drop-down and do the following:
      1.  Click the **Members** tab.
      2.  Click **Manage Team**.
      3.  Select **Create team from group**.
3.  Select your Auth Domain (or add a new source).
    **Note**: You must select an auth domain that you have added. If you select a team-shared auth domain that you don't own, the following error is displayed: `Failed to retrieve groups`
4.  Select the Google Group or Microsoft Group from the list of available groups.
5.  Confirm the team changes.
    The Confirm Changes page shows the list of new team members.
    Only users that have signed into AppSheet at least once are added when you create a team based on a Microsoft Group. Additional users will be added to the team once they sign in to AppSheet. 
6.  Click **Create Team**.

## Troubleshoot issues with team membership 

Troubleshoot issues with team membership.

## Why is a team member not able to see their team after signing in to AppSheet?

When [defining team membership using a Google group](#google-group), if there are members of your team that aren't also in the Google group, then the auth domain used to create the team must be set as the **default auth domain for the team**. See [Share integrations with your team](https://support.google.com/appsheet/answer/10104795#share-integrations).

Make team default

##  Why don't I see the option to create a team based on a Microsoft Group?

You need to [add an authentication domain](https://support.google.com/appsheet/answer/10105757#add) before you can create a team based on a Microsoft Group. 

## When setting up a team based on a Microsoft Group, why don't I see all users on the confirmation page?

Only users that have signed into AppSheet at least once are added when you create a team based on a Microsoft Group. Additional users will be added to the team once they sign in to AppSheet.
