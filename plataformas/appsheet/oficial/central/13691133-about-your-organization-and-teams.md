---
fonte: https://support.google.com/appsheet/answer/13691133?hl=en
baixado: 2026-11-10
---

# About your organization and teams

Learn about organization and teams in the following sections:

- [What is an organization?](#organization)
- [What is a team?](#team)
- [About the system-generated teams](#system-generated-teams)
- [Supported roles for an organization and teams](#supported-roles)

## What is an organization?

An AppSheet **organization** provides organization administrators with a centralized tool to manage all of the teams in the organization and delegate team management responsibilities to team administrators.

For Google Workspace users with verified domains, an AppSheet organization is created for you and is based on the Workspace organization. By default, the AppSheet organization is named after your primary domain, such as `mycompany.com`.

## What is a team?

An AppSheet **team** is a group of AppSheet users who are members of a *business unit*. Teams provide team root and administrator accounts with centralized tools for managing governance, security, policies, analytics, and billing of team members to ensure that AppSheet is compliant with the business unit's requirements. Common assets like data sources and user domains can be defined once by the team root or administrator and used by all app creators in the team. 

**Team root** privileges are automatically assigned to Google Workspace admins with: 

- AppSheet Enterprise accounts.
- [AppSheet service admin privileges](https://support.google.com/a/answer/1219251) (as defined by Workspace). Super Admins and Workspace Service Admins include these privileges, by default. See [Prebuilt administrator roles](https://support.google.com/a/answer/2405986).

See also [Assign AppSheet admin privileges to Workspace admins](https://support.google.com/appsheet/answer/14368331).

## About the system-generated teams

An AppSheet organization includes the following system-generated teams by default:

- Workspace organization team that includes all Google authenticated users in your organization
- Domain-based teams for all verified [domains](https://support.google.com/a/answer/177483) associated with your Workspace account allowing users to sign in with non-Google authentication methods 

All users in a domain-based team will receive an email notification when the team is added to an AppSheet organization.

If a Workspace organization has no verified domains, then no users on domain-based teams are added to the AppSheet organization.

You aren't obligated to use the system-generated teams. You can create your own teams using **Google Groups** or **Microsoft Groups** as long as each team has a root admin. See [Add teams to an organization](https://support.google.com/appsheet/answer/13690945#add-teams).

You can assign root admins using the Workspace Admin Console or AppSheet Admin Console, as described in the following sections:

- [Assign AppSheet admin privileges to Google Workspace admins](https://support.google.com/appsheet/answer/14368331)
- [Assign team member roles](https://support.google.com/appsheet//answer/13690945#assign-roles) on the Manage organization page

**To determine the best option for your organization, consider the following**: 

- System-generated team names can't be changed. Group-based team names are based on the name of the group.
- You can't move a user from one system-generated team to another system-generated team. A user can only be moved to another team if they are included in a Google Groups-based team and authenticate through Google.
- Any users that authenticate through non-Google or non-Microsoft authentication methods (such as Okta, and so on) will be automatically added to a domain-based team.
- If there was no verified Workspace organization when a user first signed in to AppSheet, then they might be added to a domain-based team instead of the Workspace organization-based team.

## Supported roles for an organization and teams

 The following figure shows the hierarchical relationship between an organization, and its teams and members. 

Organization hierarchy

Supported roles and permissions for an organization and its teams are summarized in the following table.

 

+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **Role**                                           | **How many?**                                      | **Permissions**                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Organization administrator                         | One or many per organization                       | -   [View all teams and team members in an         |
|                                                    |                                                    |     organization](https://su                       |
|                                                    |                                                    | pport.google.com/appsheet/answer/13690945#explore) |
|                                                    |                                                    | -   [Add a team to the                             |
|                                                    |                                                    |     organization](https://supp                     |
|                                                    |                                                    | ort.google.com/appsheet/answer/13690945#add-teams) |
|                                                    |                                                    |     that is based on Google Groups or Microsoft    |
|                                                    |                                                    |     Groups                                         |
|                                                    |                                                    | -   See the number of apps created by app creators |
|                                                    |                                                    |     on any team                                    |
|                                                    |                                                    | -   [Update the team member                        |
|                                                    |                                                    |     roles](https://support.google.com/             |
|                                                    |                                                    | appsheet/answer/13690945#update-team-member-roles) |
|                                                    |                                                    |     for any team to delegate team administration   |
|                                                    |                                                    | -   [Delete teams in an                            |
|                                                    |                                                    |     organization](https://support                  |
|                                                    |                                                    | .google.com/appsheet/answer/13690945#delete-teams) |
|                                                    |                                                    | -   [Define organization, team, and account        |
|                                                    |                                                    |     governance                                     |
|                                                    |                                                    |     policies](ht                                   |
|                                                    |                                                    | tps://support.google.com/appsheet/answer/11948767) |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Team root                                          | One or many per organization                       | -   [Define](https://su                            |
|                                                    |                                                    | pport.google.com/appsheet/answer/11938918#define), |
|                                                    |                                                    |     [remove](https://su                            |
|                                                    |                                                    | pport.google.com/appsheet/answer/11938918#remove), |
|                                                    |                                                    |     and                                            |
|                                                    |                                                    |     [delete](https://s                             |
|                                                    |                                                    | upport.google.com/appsheet/answer/11938918#delete) |
|                                                    |                                                    |     team members in your current team              |
|                                                    |                                                    | -   [View team member account                      |
|                                                    |                                                    |     details](https://support.                      |
|                                                    |                                                    | google.com/appsheet/answer/11938918#view-details), |
|                                                    |                                                    |     including number of apps                       |
|                                                    |                                                    | -   For apps owned by team members:                |
|                                                    |                                                    |     -   View app definitions in the editor (but    |
|                                                    |                                                    |         not edit them)                             |
|                                                    |                                                    |     -   Use apps                                   |
|                                                    |                                                    |     -   Receive an emailed summary report          |
|                                                    |                                                    | -   [View and share resources with team            |
|                                                    |                                                    |     members](ht                                    |
|                                                    |                                                    | tps://support.google.com/appsheet/answer/10104795) |
|                                                    |                                                    |     (sample apps, databases, data stores, and so   |
|                                                    |                                                    |     on)                                            |
|                                                    |                                                    | -   [View security for your                        |
|                                                    |                                                    |     team](ht                                       |
|                                                    |                                                    | tps://support.google.com/appsheet/answer/11948802) |
|                                                    |                                                    | -   [Monitor your                                  |
|                                                    |                                                    |     team](ht                                       |
|                                                    |                                                    | tps://support.google.com/appsheet/answer/11918345) |
|                                                    |                                                    |     app activity, usage, and billing information,  |
|                                                    |                                                    |     and download membership data                   |
|                                                    |                                                    | -   Configure team settings including:             |
|                                                    |                                                    |     -   [Restrict who can create                   |
|                                                    |                                                    |         apps](https://support.google.              |
|                                                    |                                                    | com/appsheet/answer/11918568#restrict-create-apps) |
|                                                    |                                                    |     -   [Restrict the recipient list for outgoing  |
|                                                    |                                                    |         email](https://support.google.com/         |
|                                                    |                                                    | appsheet/answer/11918568#outgoing-email-allowlist) |
|                                                    |                                                    |     -   [Set the public app                        |
|                                                    |                                                    |         owner](https://support.goo                 |
|                                                    |                                                    | gle.com/appsheet/answer/11918568#public-app-owner) |
|                                                    |                                                    |     -   [Set the AppSheet session                  |
|                                                    |                                                    |         length](https://support.go                 |
|                                                    |                                                    | ogle.com/appsheet/answer/11918568#session-length)  |
|                                                    |                                                    | -   [Define team and account governance            |
|                                                    |                                                    |     policies](htt                                  |
|                                                    |                                                    | ps://support.google.com/appsheet/answer/11948767), |
|                                                    |                                                    |     and view organization governance policies.     |
|                                                    |                                                    | -   [Export team audit logs to Big                 |
|                                                    |                                                    |     Query](ht                                      |
|                                                    |                                                    | tps://support.google.com/appsheet/answer/12469223) |
|                                                    |                                                    | -   [Transfer apps and databases between team      |
|                                                    |                                                    |     members](ht                                    |
|                                                    |                                                    | tps://support.google.com/appsheet/answer/12007391) |
|                                                    |                                                    | -   [Automate the removal of team user             |
|                                                    |                                                    |     accounts](ht                                   |
|                                                    |                                                    | tps://support.google.com/appsheet/answer/11579184) |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Team administrator                                 | One or many per team                               | -   [Define](https://support.google.com/appsheet/a |
|                                                    |                                                    | nswer/11938918#define) and [remove](https://suppor |
|                                                    |                                                    | t.google.com/appsheet/answer/11938918#remove) team |
|                                                    |                                                    |     members in your current team                   |
|                                                    |                                                    | -   [View team member account                      |
|                                                    |                                                    |     details](https://support.                      |
|                                                    |                                                    | google.com/appsheet/answer/11938918#view-details), |
|                                                    |                                                    |     including number of apps                       |
|                                                    |                                                    | -   For apps owned by team members:                |
|                                                    |                                                    |     -   View app definitions in the editor (but    |
|                                                    |                                                    |         not edit them)                             |
|                                                    |                                                    |     -   Use apps                                   |
|                                                    |                                                    |     -   Receive an emailed summary report          |
|                                                    |                                                    | -   [View and share resources with team            |
|                                                    |                                                    |     members](ht                                    |
|                                                    |                                                    | tps://support.google.com/appsheet/answer/10104795) |
|                                                    |                                                    |     (sample apps, databases, data stores, and so   |
|                                                    |                                                    |     on)                                            |
|                                                    |                                                    | -   [View security for your                        |
|                                                    |                                                    |     team](ht                                       |
|                                                    |                                                    | tps://support.google.com/appsheet/answer/11948802) |
|                                                    |                                                    | -   [Monitor your                                  |
|                                                    |                                                    |     team](ht                                       |
|                                                    |                                                    | tps://support.google.com/appsheet/answer/11918345) |
|                                                    |                                                    |     app activity, usage, and billing information,  |
|                                                    |                                                    |     and download membership data                   |
|                                                    |                                                    | -   Configure team settings including:             |
|                                                    |                                                    |     -   [Restrict who can create                   |
|                                                    |                                                    |         apps](https://support.google.              |
|                                                    |                                                    | com/appsheet/answer/11918568#restrict-create-apps) |
|                                                    |                                                    |     -   [Restrict the recipient list for outgoing  |
|                                                    |                                                    |         email](https://support.google.com/         |
|                                                    |                                                    | appsheet/answer/11918568#outgoing-email-allowlist) |
|                                                    |                                                    |     -   [Set the public app                        |
|                                                    |                                                    |         owner](https://support.goo                 |
|                                                    |                                                    | gle.com/appsheet/answer/11918568#public-app-owner) |
|                                                    |                                                    |     -   [Set the AppSheet session                  |
|                                                    |                                                    |         length](https://support.go                 |
|                                                    |                                                    | ogle.com/appsheet/answer/11918568#session-length)  |
|                                                    |                                                    | -   [Define team and account governance            |
|                                                    |                                                    |     policies](htt                                  |
|                                                    |                                                    | ps://support.google.com/appsheet/answer/11948767), |
|                                                    |                                                    |     and view organization governance policies.     |
|                                                    |                                                    | -   [Export team audit logs to Big                 |
|                                                    |                                                    |     Query](ht                                      |
|                                                    |                                                    | tps://support.google.com/appsheet/answer/12469223) |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Team member                                        | One or many per team                               | -   Use AppSheet to create apps                    |
|                                                    |                                                    | -   [View team member account                      |
|                                                    |                                                    |     details](https://support                       |
|                                                    |                                                    | .google.com/appsheet/answer/11938918#view-details) |
|                                                    |                                                    | -   [View and share resources with team            |
|                                                    |                                                    |     members](ht                                    |
|                                                    |                                                    | tps://support.google.com/appsheet/answer/10104795) |
|                                                    |                                                    | -   [View your organization and team governance    |
|                                                    |                                                    |     policies](ht                                   |
|                                                    |                                                    | tps://support.google.com/appsheet/answer/11948767) |
|                                                    |                                                    | -   [Define governance policies for your           |
|                                                    |                                                    |     account](ht                                    |
|                                                    |                                                    | tps://support.google.com/appsheet/answer/11948767) |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
