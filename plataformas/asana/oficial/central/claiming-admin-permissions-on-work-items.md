---
fonte: https://help.asana.com/s/article/claiming-admin-permissions-on-work-items?language=en_US
baixado: 2026-11-10
---

# Claiming admin permissions on work items

**Available on Asana [Starter](https://asana.com/plan/starter), [Advanced](https://asana.com/plan/advanced), [Enterprise](https://asana.com/enterprise), and [Enterprise+](https://asana.com/enterprise) tiers, as well as [legacy tiers](https://asana.com/pricing-legacy) Premium, Business, and Legacy Enterprise.**

When work items in Asana (such as projects, portfolios, teams, custom fields, and bundles) lose their admin, other users with appropriate access can claim admin permissions. This feature ensures continuity of work management when original admins are deprovisioned or have their access removed. By claiming admin permissions, users can maintain control over important work items and continue managing them effectively.

#### Related articles

- [Project permissions](https://help.asana.com/s/article/project-permissions)
- [Team permissions](https://help.asana.com/s/article/team-permissions)
- [Portfolio privacy and sharing](https://help.asana.com/s/article/portfolio-privacy-and-sharing)

## How admin permissions work in Asana

Most work items in Asana have designated admins who have full control over the object. These include:

- Projects
- Portfolios
- Teams
- Custom fields
- Bundles

Admins can manage permissions, edit settings, and control who has access to these items. However, when admin users leave the organization or have their access removed, work items can be left without an admin.

## How to claim admin permissions

How to claim admin permissions on a work item:

1.  Navigate to the work item (project, portfolio, team, etc.)
2.  Open the share modal by clicking **Share** in the top right corner
3.  If there are no current admins, you'll see a notification indicating this
4.  Click **Become admin** to claim admin permissions

For teams specifically:

1.  Click the team name to open team details
2.  Navigate to the **Members** tab
3.  Look for the notification that the team does not have an admin
4.  Click **Become team admin**

## Who can claim admin permissions

Not everyone can claim admin permissions. The following conditions must be met:

- You must be a member of the organization, and not a guest
- You must already have access to the work item
- You must have the next highest level of access to the item

For example:

- If a project has no admins but has editors, any editor can become an admin
- If a project has no admins and no editors, any commenter could become an admin
- If a team has no admins, any team member can become a team admin

In each case described, it is not possible for a guest to become an admin.

## Special considerations for super admins

Organization super admins can gain access to any work item through:

- A [service account](https://help.asana.com/s/article/service-accounts)
- [Work access mode](https://help.asana.com/s/article/work-access-mode)

Once a super admin has access to the item, they can claim admin permissions following the same process described above.

## Frequently asked questions

### What happens if I claim admin permissions on a work item?

You'll gain full control over the item, including the ability to manage permissions, edit settings, and control access.

### Can I claim admin permissions on any work item?

You can only claim admin permissions on items you already have access to and where you have the next highest level of access after admin.

### Can guests claim admin permissions?

No, only domain users (users with your organization's email domain) can claim admin permissions.

### What if I accidentally claim admin permissions?

If you claim admin permissions by mistake, you can assign admin permissions to another appropriate user. The other admin can then change your permission level. You may also leave the item, and you will no longer be an admin.

### Will claiming admin permissions notify the original admin?

No, claiming admin permissions does not send notifications to previous admins.

## Troubleshooting tips

### I don't see the **Become admin** option

- Verify that the work item definitely has no admins
- Check that you have the appropriate level of access to the item
- Confirm you are an organization member, not a guest

### I need to claim admin permissions but don't have access to the item

- Contact your organization's super admin
- The super admin can use [work access mode](https://help.asana.com/s/article/work-access-mode) to gain access and then claim admin permissions or grant you access

[](https://forum.asana.com/c/forum-en/tips/6)
