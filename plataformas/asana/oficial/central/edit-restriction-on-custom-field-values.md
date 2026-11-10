---
fonte: https://help.asana.com/s/article/edit-restriction-on-custom-field-values?language=en_US
baixado: 2026-11-10
---

# Edit restriction on custom field values

**Available on Asana [Enterprise](https://asana.com/enterprise) and [Enterprise+](https://asana.com/enterprise) tiers, as well as the [Legacy Enterprise](https://asana.com/pricing-legacy) tier.**

**Visit our [pricing page](https://asana.com/pricing) for more information.**

Restricted custom field values give project admins control over who can modify specific custom field values in a project. This feature ensures data integrity, making Asana suitable for workflows that require it, such as preventing edits to custom fields created via intake forms or protecting sensitive information like budget values from unauthorized changes.

### Related articles:

- [Custom fields](https://help.asana.com/s/article/custom-fields?language=en_US)
- [Project permissions](https://help.asana.com/s/article/project-permissions?language=en_US)

## Setting custom field value permissions

Permissions are set at the project level and only affect the specific project where they're applied.

A project admin can change a custom field's editing permissions by following these steps:

1.  Click the drop-down arrow beside the project name.
2.  Select **Manage project permissions** from the menu.
3.  Under **Fields**, click **Add restriction**.
4.  Select the fields you wish to restrict.
5.  Choose who can edit them: **project admins only**, or **project admins and editors**.

In the specific project where the field is restricted, only those who have been granted permission will be able to change or edit the value of that custom field. Other users such as commenters, viewers, and task collaborators will not have editing access.

Global fields that are used in multiple projects will not be impacted anywhere else besides the project where the restriction is set.

> You can also apply these edit restrictions to **Assignee** and **Due Date** fields, limiting who can update task assignments and due dates to reduce accidental changes and improve governance.

## Disabling multi-homing to fully lock down a custom field

To fully lock down a custom field, project admins have the option to turn off multihoming capabilities for tasks in that project. Disabling multihoming prevents tasks from being moved in or out of the project by users who are not project admins, ensuring that permissions remain consistent and secure across all tasks. Project admins can still multi-home tasks in the project when multi-homing is disabled for others.

While disabling multihoming is optional, it can provide additional peace of mind by maintaining consistent access levels for all users. When tasks are multi-homed, users with different access levels in different projects may inadvertently gain custom field editing rights.

## Restricted custom field value FAQs

### Does this feature restrict who can create custom fields in a project?

No, the feature that restricts who can create a custom field already exists in Asana and should not be confused, see the article on [Custom field access levels](https://help.asana.com/s/article/custom-field-access-levels) for more information. Project admins can restrict field creation in a project to just admins by navigating to the **manage** **project permissions** and changing the **workflow management** setting to **admins only**.

### Will there be any changes to the default settings of who can edit custom field values?

There will be no changes to the default settings for editing custom field values. By default, all users can view and edit new and existing custom fields. This means that unless you adjust the settings, anyone with edit access to the project can modify the fields.

### Does this feature work on portfolio custom fields?

No, restricted custom field values are not currently supported for portfolio custom fields.

[](https://forum.asana.com/c/forum-en/tips/6)
