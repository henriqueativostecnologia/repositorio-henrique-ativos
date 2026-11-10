---
fonte: https://help.asana.com/s/article/rule-permissions?language=en_US
baixado: 2026-11-10
---

# Automation permissions

[Automations](https://help.asana.com/s/article/rules?language=en_US), much like custom fields, are editable by other members of the project by default. This article covers automation permissions, including who can enable, disable and trigger automations.

#### Related articles:

- [Automations](https://asana.com/guide/help/premium/rules)
- [Automation triggers](https://help.asana.com/s/article/rule-triggers?language=en_US)
- [Automation actions](https://help.asana.com/s/article/rule-actions?language=en_US)

## Important notes on automation permissions

- Users with sufficient permissions on a project or portfolio will be able to assign themselves ownership of automations, and edit automations. See “Who can edit and claim ownership of an automation.”
- When updating automations on projects and templates, the editor must have the correct permissions to save all of the automations. For example, if the automation adds tasks to another project, then the editor must also have edit permissions in that other project.
- When an automation is duplicated via project duplication, the duplicating user becomes the owner with insufficient privileges. In this instance, the automation is disabled, but the owner still has editing access.
- automations are designed to keep running even when the owner's access control permissions change. For example, if an automation is set up to add tasks to a project and you later lose access to that project, the automation will continue to have access to that project.
- When an automation is copied or duplicated via project templates, the user who creates a project from the template will become the automation owner. Here, the automation will only be disabled if the template duplicator has insufficient access control permissions for the automation. For example, you cannot edit a project to which the automation wants to add tasks.
- If a user leaves a project, the automation will not break. However, if there are no other users interacting with the project the automation will be disabled.

## Who can enable or disable an automation?

Any user with access to edit workflows on a project in which an automation is running will be able to enable or disable an automation created by someone else.

Users with this access are also the only ones that can view the change history.

## Who can edit and claim ownership of an automation

Permissions to edit automations will be based on a user’s project or portfolio permissions. That means users with access to edit workflows on a project or portfolio can edit any automations that live in that project or portfolio. automation creators cannot restrict users with project or portfolio permissions from editing automations.

Users with access to edit workflows can claim ownership of an automation by navigating to the automation’s **Settings** tab and clicking **Become owner**. The current automation owner will receive an email and inbox notification letting them know the ownership of the automation has changed.

## Who can edit automations with external actions or triggers

An automation with external triggers or actions can only be edited by the automation owner. An editor can only remove the app components of an app automation. To replace or add app components, the editor must take ownership of the automation.

## How can I further restrict who can modify automations?

As a paid user, you can restrict other users to view or comment on projects without giving them access to them. Read more about [individual project permissions](https://help.asana.com/s/article/individual-project-permissions). Enterprise and Enterprise+ users can further restrict this by allowing only project admins to modify project's workflow and appearance.

## When an automation owner leaves Asana

When an automation owner is deprovisioned, the automation ownership will be automatically passed to a project admin, provided that the automation has no external actions or triggers.

If there is no project admin, ownership will be passed to a project owner, or if no project admin exists, a project editor. 

## Triggering automations

You can trigger an automation from anywhere (web, mobile, external integrations). If you update something on a task, we check to see if that task is in any projects with automations, and if your action is the trigger on any of those automations. Anyone can trigger an automation, including [guests](https://asana.com/guide/help/organizations/guests).

### Projects you don't have access to

You can trigger automations on projects that you don’t have access to, but the yellow lightning bolt icon will not be displayed to indicate that an automation is running.

## Guest permissions

[Guests](https://help.asana.com/s/article/guests-faq?language=en_US) cannot create or own automations, but they can trigger automations.

 

[ ](https://forum.asana.com/c/forum-en/tips/6)
