---
fonte: https://help.asana.com/s/article/license-assignment-in-divisions?language=en_US
baixado: 2026-11-10
---

# License assignment in divisions

Domains that contain divisions are called mixed domains, because they can have a mix of free and licensed users in them. This article outlines how licenses are assigned and removed in these mixed domains.

#### Related articles:

- [A guide to divisions in Asana](https://help.asana.com/s/article/a-guide-to-divisions-in-asana?language=en_US)
- [Divisions](https://help.asana.com/s/article/divisions)
- [Advanced division management](https://help.asana.com/s/article/advanced-division-management?language=en_US)
- [Division access and management FAQ](https://help.asana.com/s/article/division-access-and-management-faq?language=en_US)
- [Security and billing for divisions](https://help.asana.com/s/article/security-and-billing-for-divisions)
- [Managing members and teams in a division](https://help.asana.com/s/article/managing-members-and-teams-in-a-division)

## How licenses are assigned to users

Licenses are assigned directly to the user, meaning they’ll have access to paid features anywhere they go in Asana. Users can be added and removed from your division at any time via the admin console. For example, if a user needs to access Advanced features for a 3 month project, you can add them to your Advanced division and remove the user from the division later if they no longer have a need for Advanced features.

There are two primary ways licenses can be assigned:

1.  Admins can manually add licenses to users within the admin console via the **Invite members** icon in the **Members** tab.
2.  Certain collaborative actions will trigger automatic license assignment. This ensures collaboration in Asana is seamless for both the sharer of a work object (project, portfolio) and the person the object is shared with. This is what we call “Automatic license assignment”

### How automatic license assignment works:

When a licensed user shares an object (project, portfolio, or goal) with a free user or invites a free user to a team, the free user is automatically granted a paid license in the same division as the licensed user. Also, when a free user's request to join a team is approved by a paid user, that will automatically add a license to the division that user is in.

The division that houses a team, project, or portfolio determines which license a member receives when they are added or connected. 

### Adding members to higher-tier teams and projects

When you add a member from a lower-tier division, such as Asana Starter, to a team, project, or portfolio housed within a higher-tier division, such as Asana Advanced, Asana automatically upgrades that member's license to the higher tier. For example, if you add a Starter member to an Advanced team, that member receives an Advanced license.

### Connecting lower-tier projects to higher-tier objects

Connecting a Starter project to an Advanced-only object, such as a portfolio or workflow, also triggers automatic license assignment. Before you attach a lower-tier project to a portfolio or workflow, check whether that object is available only in the higher-tier division.

### Host shared work in the lower-tier division

To help prevent unexpected license upgrades, host shared teams and projects in the lower-tier division. For example, if Starter and Advanced members need to collaborate, place the shared team or project in the Starter division. Starter members who join that work keep their current license.

Members of a higher-tier division can join and collaborate in lower-tier teams and projects without changing their paid status or creating extra seat charges. This approach keeps shared work in the lower-tier division while giving everyone the access they need.

## Check how a user's license has been assigned

If you are ever wondering how a user ended up in your division, you can see this by viewing the license section at the bottom of the user’s profile settings page.

## Removing a user’s license

Admins and billing owners can remove a user’s license via the **Members** tab of the division admin console.

The first option removes the user from your bill. The user is still associated with the same objects they were shared with (teams, projects, etc). 

> The user remains a member of the team, but they lose access to paid features.

The second option removes them from your bill and deprovisions them from the broader organization, meaning they no longer have access to Asana.

## New admin console Teams tab functionality

The **Teams** tab in the division admin console now mirrors the functionality of the organization-level admin console, providing comprehensive team management capabilities.

From the **Teams** tab, division admins can:

- **Create new teams**
- **View comprehensive team information** including:
  - Team name and member count
  - Privacy permissions and settings
  - Creation date and creator information
- **Edit team settings** by hovering over the three dot icon next to the **Created by** field and clicking **Edit item**
- **Manage team memberships** centrally across the division
- **Export team data to CSV** for reporting an analysis

This enhanced Teams tab functionality allows division admins to assign licenses to all users in a team efficiently, as well as monitor team structure and membership. They can also maintain centralized control over team access and permissions.

> Adding a user from a team **does not** remove them from your division. You need to remove them from the admin console as licenses are assigned to users directly.

[](https://forum.asana.com/c/forum-en/tips/6)
