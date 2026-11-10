---
fonte: https://help.asana.com/s/article/control-queue-and-knowledge-base-creation-with-rbac?language=en_US
baixado: 2026-11-10
---

# Control queue and knowledge base creation with RBAC

**Available on Asana Enterprise+ or Asana Enterprise with the Permissions Management Add-On.**

If your team uses Asana Service Management, role-based access control (RBAC) helps you decide who can create queues and knowledge bases. This gives admins a simple way to manage these actions at the organization level.

By default, admins in your organization can create queues and knowledge bases. Members cannot create them unless an admin assigns a role that includes those permissions.

## Create a custom role for queue and knowledge base creation

To give someone permission to create queues or knowledge base:

1.  Navigate to the **admin console** 
2.  Go to the **Users** tab 
3.  Click **Manage roles** 
4.  Click **Create role**
5.  Scroll down to **Services** 
6.  From here you can select the **Create service queues** and **Create knowledge bases** permissions
7.  Click **Create role**, then assign it to the users who should be able to create these resources** **

> Read more about [using RBAC to customize permissions](https://help.asana.com/s/article/role-based-access-control-with-custom-roles).

## Understand organization-wide and object-specific permissions

RBAC custom roles apply across your organization. This is the right approach when you want to control who can create new queues or knowledge bases in Asana Service Management.

Queues and knowledge bases can also have their own permissions. These settings only apply to an individual queue or knowledge base, so they do not change access across your entire organization.

## When to use each permission type

Use an organization-wide custom role when you want to control who can create new queues or knowledge bases. Use queue-specific or [knowledge base-specific permissions](https://help.asana.com/s/article/set-up-a-knowledge-base-in-asana-service-management) when you want to manage access within a particular queue or knowledge base after it exists.
