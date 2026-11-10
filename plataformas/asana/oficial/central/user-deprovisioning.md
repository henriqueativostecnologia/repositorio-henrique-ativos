---
fonte: https://help.asana.com/s/article/user-deprovisioning?language=en_US
baixado: 2026-11-10
---

# User deprovisioning

Have you recently deprovisioned a user and are wondering what happens to their tasks and projects? Read below to find out more.

#### Related articles

- [Workspaces and organizations FAQ](https://help.asana.com/s/article/workspaces-and-organizations-faq?language=en_US)
- [Accounts FAQ](https://help.asana.com/s/article/accounts?language=en_US)
- [Tasks and subtasks FAQ](https://help.asana.com/s/article/tasks-and-subtasks?language=en_US)
- [Accidental deletion](https://help.asana.com/s/article/accidental-deletion?language=en_US)
- [Access and permissions](https://help.asana.com/s/article/access-and-permissions?language=en_US)
- [Navigation and display ](https://help.asana.com/s/article/navigation-and-display?language=en_US)

## Deactivated users and their tasks

When a user is deactivated through an identity provider like Okta or manually via the admin console, a project is auto-generated for the tasks that were assigned to the deactivated user. Super admins become members of this auto-generated project and have access to the deactivated user’s tasks.

### Who becomes the project owner?

One of the organization’s super admins will become the project owner. The project owner will be notified about the project's creation via a task in Asana.

A new setting in the admin console allows the super admin of an organization to define which super admin becomes the owner of the project carrying a deprovisioned user’s previously assigned tasks after they have been [deprovisioned via SCIM](https://asana.com/guide/help/premium/scim "deprovisioned via SCIM") or the API.

### Who is notified when that project is created?

The super admin who has been chosen as project owner will be assigned a task to review the project once it is generated.

### What happens to projects, portfolios, and dashboards that are owned by deactivated users when there are no other members present?

Deactivation does not currently transfer data ownership for projects, portfolios or dashboards.

[](https://forum.asana.com/c/forum-en/tips/6)
