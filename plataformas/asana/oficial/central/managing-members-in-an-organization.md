---
fonte: https://help.asana.com/s/article/managing-members-in-an-organization?language=en_US
baixado: 2026-11-10
---

# Managing members in an organization

The **Members** tab offers admins a comprehensive overview of the organization's membership, including the ability to invite new members, assign administrative privileges, and deactivate or remove members as needed.

#### Related articles

- [How to access the admin console](https://help.asana.com/s/article/how-to-access-the-admin-console?language=en_US)
- [Managing password settings in the admin console](https://help.asana.com/s/article/managing-password-settings-in-the-admin-console?language=en_US)
- [Profile field editability controls](https://help.asana.com/s/article/profile-field-editability-controls?language=en_US)
- [Mobile apps security permissions](https://help.asana.com/s/article/mobile-apps-security-permissions?language=en_US)
- [Global authentication settings](https://help.asana.com/s/article/global-authentication-settings?language=en_US)
- [Managing teams through the admin console](https://help.asana.com/s/article/managing-teams-through-the-admin-console?language=en_US)
- [Billing settings in the admin console](https://help.asana.com/s/article/billing-settings-in-the-admin-console?language=en_US)
- [Admin security controls](https://help.asana.com/s/article/admin-security-controls?language=en_US)
- [Managing organization settings](https://help.asana.com/s/article/managing-organization-settings?language=en_US)
- [App management and integrations](https://help.asana.com/s/article/app-management-and-integrations?language=en_US)

## Manage all members in an organization

The Members tab gives you a clear overview of the people in your organization, with columns that highlight important account details at a glance.

- Name: Shows the user's name and email address
- Role: Indicates whether the person is a member, guest, admin, or unclaimed user
- Status: Shows whether the user is active, paused, invited, or removed from Asana
- License: Shows which license type is assigned to the user (for example, Enterprise or View only)
- Add-on: Shows any add-ons assigned to the user
- Last activity: Shows the most recent date the user was active in Asana
- Invited by: Shows how the user joined the organization

> Filtering actions are rolling out incrementally in late 2025 and early 2026. You may not see these options immediately in the admin console.

### Bulk actions within the members list

> Bulk actions are rolling out incrementally in late 2025 and early 2026. You may not see these options immediately in the admin console.

Bulk actions are available from the **Members** page. Admins can select multiple rows using the checkboxes, or by using:

- **Shift** to select a range of consecutive rows

- **Cmd (Mac) / Ctrl (Windows)** to select multiple non-consecutive rows

When one or more rows are selected, the bulk actions bar appears at the bottom of the page. From here, admins can:

- **Change status:** Pause or unpause a user, or remove or restore a user

- **Change license:** Assign an Enterprise or View only license

- **(Coming soon) Manage invites:** Resend or cancel invites

- **(Coming soon) Add to team**

## Deactivating a member in your organization

To remove a person from your organization, navigate to the **Members** tab of your admin console. Click the three dot icon next to the person's name and select **Remove**.

#### From the next tab, you can:

1.  Create a new private to members project for the tasks of the member you're removing
2.  Choose the member you want to reassign the project to
3.  Click **Remove member** to confirm the deactivation

The deactivated member will then show in your member’s list as **Removed**.

### What happens to a deprovisioned person’s tasks?

After you have deprovisioned someone from your organization, a private to members project containing their previously assigned tasks will be auto-generated. You can assign this to yourself or another member of your organization. This allows you to easily assign pending tasks to the appropriate person to manage.

A simple next step solution to delegating would be to multi-select deprovisioned tasks, where you can take mass actions on tasks and even [bulk assign](https://help.asana.com/s/article/save-time-in-asana?language=en_US) them to yourself or other organization members.

You can read more about this in our [FAQ article](https://help.asana.com/s/article/user-deprovisioning?language=en_US "FAQ article").

> The time of the deactivation will appear in the **Last activity** column.

## Restoring a deactivated member or guest

### [Automatic reactivation](#h_01HSGRJ8E184QM2BGG4THDNDEJ)

Available on paid plans, automatic reactivation means that previously deactivated users returning to Asana have access to their previous data including projects and teams, provided they return with the same email address as used previously.

Automatic reactivation can be configured in the **Security** tab in the sidebar and then clicking **Reactivation** **settings**. Here you can select to turn this feature on or off for members or guests. If you choose to turn this setting off, you will still be able to restore data access manually. Only super admins can turn this feature back on once it's switched off.

> User's reactivation only happens after the user accepts their invite or completes signing up for Asana on the website. Inviting a user by itself doesn't reactivate the user.
>
> Automatic reactivation will only be available for users who were deactivated less than two years ago.

### [Manual Reactivation](#h_01HSGRMYE6ZT3NRR50B55W1ATB)

Restore a deactivated member by finding their name in your member’s tab. Then click the three dot icon and select **Restore**.

[](https://assets.asana.biz/transform/c5039485-c857-468d-865d-7e17acee0b7e/productui-helpcenter-managing_your_subscription-managing-members-in-an-organization-004-en-us.png)

 

If your reactivation fails, the admin for your organization will receive a task asking them to reach out to our [Support team](https://asana.com/support).

## Filter by member type

To filter your member list by member type, click the drop-down arrow next to the member type filter.

## Team access

The **Team access** tab on a member's profile settings gives admins insight into what specific users have access to and the ability to edit membership status.

From **Edit profile settings** admins can navigate to a member's **Profile settings** to access and manage teams. To access a member's settings click the **three dot icon** and click **Edit profile settings.**

From here, navigate to the **Team Access** tab where you can browse teams, edit team access and add or remove members from teams.

[](https://assets.asana.biz/transform/520ba2c1-69b1-4975-bc2a-7e29bf5069d7/productui-helpcenter-managing_your_subscription-managing-members-in-an-organization-006-en-us.png)

Click on **Team Access** to:

1.  View the teams a user belongs to
2.  Add a user to any team in the organization
3.  Untick to remove the user from any team
4.  Save changes after any updates

## Export membership data to CSV

To export membership data to CSV, click **Export CSV** at the top right corner. You will then receive an email message with the link to download.

The CSV file downloaded has the following fields:

- Name
- Email address
- Department
- Date joined organization
- Invited by
- Inviter email
- First login date
- Login method
- MFA state
- Last activity
- Type
- Number of teams
- Teams
- Number of projects
- Projects

> Need help managing organization members in Asana? [Ask the Community](https://forum.asana.com/c/forum-en/tips/6).

[](https://forum.asana.com/c/forum-en/tips/6)
