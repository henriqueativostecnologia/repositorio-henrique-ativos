---
fonte: https://help.asana.com/s/article/task-permissions?language=en_US
baixado: 2026-11-10
---

# Task permissions

Access to a task in Asana is contextual and there are a variety of situations that affect who can access a task. This article explains how to identify a task's permission settings and how to provide or limit access to a task.

|                                                                                                                   |                                                                             |
|-------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| **Task**                                                                                                          | **Accessible by**                                                           |
| Private task                                                                                                      | Only task collaborators                                                     |
| Public task                                                                                                       | All organization members                                                    |
| Task in a [private to members](https://help.asana.com/s/article/project-permissions?language=en_US) project       | Task collaborators and project members                                      |
| Task in a [team only](https://help.asana.com/s/article/project-permissions?language=en_US) project                | Task collaborators, project members, and team members                       |
| Task in a [shared with organization](https://help.asana.com/s/article/project-permissions?language=en_US) project | Task collaborators, project members, team members, and organization members |

## Private tasks

Private tasks that don't belong to a project are only visible to collaborators. A banner at the top and the project field displays privacy information and project association. Tasks created in My tasks default to private.

Below is an example of a private task with no project association, only visible to collaborators.

Give access to private tasks by making the task public, adding it to a project with other members, or adding someone as a collaborator. Before adding the task to a project, be sure to note the [project's permissions](https://asana.com/guide/help/permissions/project-permissions "project's permissions").

To limit access to a task, remove it from any project, remove all collaborators, or make it private. Do not remove yourself as a task collaborator or you'll lose access to the task as well.

 

##

## Public tasks

Public tasks are visible to everyone in your organization. The project field indicates whether the task belongs to a project.

## Task access level capabilities

Your ability to interact with a task is primarily inherited from your membership level in the project.

**1. Project-based permissions**

If a task is in a project, your project-level role determines your task permissions:

- **Project Editors:** Can modify all task fields, including title, description, and custom fields.
- **Project Commenters:** Can post comments and attachments. They generally *cannot* edit task details unless they are assigned the task (see **Assigned-Task Elevation** below).
- **Project Viewers:** Can see the task but cannot edit or comment on it.

**2. Task collaborator default (Task SAL)**

Projects can be configured to set a default access level for task collaborators.

- **Can Edit:** Collaborators added to a task default to full editing rights.
- **Can Comment:** Collaborators added to a task default to comment-only rights.
- *Admins can adjust this in the Project Settings under the "Permissions" tab.*

### Special permission rules

**Assigned-task elevation**

Being assigned a task grants you temporary "elevated" permissions while you are the assignee, even if your project-level access is restricted.

- **For Commenters:** If a Commenter is assigned a task, they can complete it, change the assignee, and adjust the due date for that task.
- **For Viewers:** If a Viewer is assigned a task, they can comment on and like it.

Multi-homed task permissions

When a task lives in multiple projects (multi-homing), Asana applies the **highest permission** level across all those projects.

- *Example:* If you are a "Viewer" in Project A but an "Editor" in Project B, and the task lives in both, you will have "Editor" permissions for that task.

Capability summary table

|                          |                 |                 |                    |
|--------------------------|-----------------|-----------------|--------------------|
| **Action on a task **    | **Task Editor** | **Task Viewer** | **Task Commenter** |
| Edit Title/Description   | ✅              | ❌              | ❌                 |
| Change Custom Fields     | ✅              | ❌              | ❌                 |
| Post Comments/Likes      | ✅              | ✅              | ✅                 |
| Change Assignee/Due Date | ✅              | ❌              | ✅                 |
| Complete Task            | ✅              | ❌              | ✅                 |
| Delete task              | ✅              | ❌              | ❌                 |

Related resources

To learn more about specific access levels and how to manage your team’s privacy, visit these articles:

- [Individual Project Permissions Overview](https://asana.com/guide/help/permissions/project-permissions)
- [Understanding Editor Access Level](https://www.google.com/search?q=https://asana.com/guide/help/permissions/editor)
- [Understanding Viewer Access Level](https://www.google.com/search?q=https://asana.com/guide/help/permissions/viewer)

## Managing task permissions

### Giving access to a public task that doesn't belong to a project

Adding someone as a task collaborator provides them access to a task. Organization members already have access via search.

Adding the task to the project gives project members access. Before adding the task, note the [project's permissions](https://asana.com/guide/help/permissions/project-permissions "project's permissions") and project members.

Limiting access to a public task that doesn't belong to a project?

By removing all task collaborators, except yourself, organization members will no longer receive task notifications, but can still access the task by searching for it.

Click the task actions button from the task details pane, and select **Make private**. Since the task doesn't belong to any project, it will only be visible to you and the collaborators.

### Tasks in a project that is **shared with organization** or **team only**

To verify that a task is in a project with the **shared with organization** or **team only** privacy setting, the project field indicates the project the task belongs to. Within the project, the [header](https://asana.com/guide/help/fundamentals/navigating-asana#gl-header "header") indicates the project privacy.

### Who can see tasks in a **team only** or **shared with organization** project?

### Who can see tasks in a **team only** or **shared with organization** project:

**Team only**: Project members, task collaborators, and members of the team the project lives in.

**Shared with organization**: All members of the organization.

### How can I give access to tasks in a **team only** project?

**Add someone as a task collaborator** — This will provide them with updates on the task. If they're already a project member or team member, then they can already access the task.

**Add someone as a project member** — This gives them access to all tasks in the project. If they're a team member, then they can already access the task.

**Add someone as a member of the team** — This gives them access to all tasks in the project.

### How can I give access to tasks in a **shared with organization** project?

Tasks in projects that have the **shared with organization** privacy setting are already accessible by every organization member.

How do I limit access to this task?

- **Remove task collaborators** — they will no longer receive task notifications. Project or team members can still access the task.
- **Remove project members** — they will no longer receive task and project notifications. However, if they are also a member of the team in which the project exists, they can view the task and other tasks in the project because it is public.
- **Remove the task from the project** — project members will no longer have access to the task, but task collaborators can still access the task.
- **Make the project private** — team members will no longer have access to the task or the overall project, but project members and task collaborators will still have access to the task.

### Tasks in a project which is **private to members**

### Verifying a task is in a project that is **private to members**:

1.  The project field in the task details pane indicates the project the task belongs to. Click the project's name to load the project.
2.  After loading the project, the header will indicate that the project is **Private to project members**.

### Who can see this task?

Project members and task collaborators can see this task.

### How can I give access to tasks in a private to members project?

1.  **Add someone as a task collaborator** — This provides access to just this task. If they're a project member, they already have access.
2.  **Add someone as a project member** — This provides access to all tasks in the project.
3.  **Make the project public to its team by changing privacy settings to team only** — This allows members of the team to access the project and its tasks.
4.  **Make the project public to the organization by changing privacy settings to shared with organization** — This will provide access to all organization members.

### How do I limit access to this task?

- **Remove task collaborators** — they will no longer have access to the task. However, if they are also a project member, they can access the task again from the project.
- **Remove project members** — they will no longer have access to the task, or any tasks in the project unless they are still a collaborator.
- **Remove the task from the project** — project members will no longer have access to the task, but task collaborators still do.

### Request access to a private task

You can reach out to the assignee of a private task to request access:

1.  Click the link to the private task. You will see the above screen.
2.  Click on **Request access** to request access from the assignee.
3.  The assignee is notified and has the option to add you as a collaborator.

If the task has no assignee, the request goes to the task creator, if they still have edit access. If the creator doesn't have edit access, the first collaborator with edit access receives the request. If the task is accessible to members of a project, the request will go to the project owner. If the project doesn't have an owner, the request goes to a member with edit access in that project.

 

Looking for a better way to manage your work? Get started with a free Asana trial. [Try for free](https://asana.com/create-account "Try for free")
