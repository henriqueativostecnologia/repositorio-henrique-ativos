---
fonte: https://support.google.com/appsheet/answer/13690945?hl=en
baixado: 2026-11-10
---

# Add, update, or delete the teams in your organization

As an organization administrator, you can add, update, or delete the teams in an organization using the Manage organization page. You can add teams based on Google Groups or Microsoft Groups.

The Microsoft auth domain provides AppSheet with access to any available Microsoft groups including Microsoft 365 Groups, security groups, and distribution groups. No special Microsoft permissions are required for an admin to have access to existing groups.

 

Google Workspace admins [manage Google Groups for an organization](https://support.google.com/a/answer/33329).  Microsoft admins manage Microsoft Groups using the [Microsoft 365 Admin Center](https://support.microsoft.com/en-us/office/microsoft-365-admin-center-simplified-view-1d204046-baef-4b21-b00e-f1cbd1c3883a).

## Explore the Manage organization page

**Note**: You need to be an **organization administrator** to access the Manage organization page.

To access My team to manage your team, select:

- **Admin \> My organization** in the top navigation
- **My organization** from the account profile drop-down

The Manage organization page displays.

Manage organization page

As highlighted in the figure above, the Manage organization page enables an organization administrator to:

- View all teams in the organization
  For information about the default teams, see [About the system-generated teams](https://support.google.com/appsheet/answer/13691133#system-generated-teams).
- [Add](#add-teams) and [delete](#delete-teams) teams in an organization
- View and manage team members for the selected team, including:
  - View team member information, including email address, last active date, status (app creator or user), number of apps created by an app creator, and current role
  - [Assign team member roles](#assign-roles)

## Add teams to an organization

Add a team to an organization using Google Groups or Microsoft Groups.  

**Note**: An [*org admin*](https://support.google.com/appsheet/answer/14368331) must add their Google or Microsoft credentials as an auth domain.

  To add a team to an organization:

1.  [Access the Manage organization page](#explore).
2.  In the left navigation panel, select **+ \> Create team**.
3.  Select the **Auth domain** that defines the group.
    Alternatively, you can [add a new Auth domain to your account](https://support.google.com/appsheet/answer/10105757).
4.  For Google Groups:
    1.  Select a group from the list.
    2.  Click **See Team Changes**.
    3.  Confirm the team changes.
    4.  Click **Create and update memberships**.
5.  For Microsoft Groups:
    1.  Select a group from the list.
    2.  Review the users that will be added to the team.
    3.  Click **Create Team**.

See also [Define your team membership](https://support.google.com/appsheet/answer/11938918#define).

## Assign team member roles 

[Assigning AppSheet admin privileges to Workspace admins](https://support.google.com/appsheet/answer/14368331) through Google Workspace, either by auto-assignment or manually using the Google Admin Console, takes precedence over the role assigned through the AppSheet organization, as described in this section.

Assign team member roles to delegate the administration of each team to team administrators (team root and admin).  

  To update team member roles:

1.  [Access the Manage organization page](#explore).
2.  Select the team for which you want to assign roles in the left navigation panel.
3.  In the **Role** column, select the new role from the drop-down for one or more members of the team. See [Supported roles for organization and teams](https://support.google.com/appsheet/answer/13691133#supported-roles).

## Delete teams in an organization

**Note**: A team must be empty in order for it to be deleted from an organization.

  To delete a team in an organization:

1.  [Access the Manage organization page](#explore).
2.  Select the team you want to delete in the left navigation panel.
3.  In the team header, select More **\> Delete**.
4.  Confirm the delete operation at the prompt.
