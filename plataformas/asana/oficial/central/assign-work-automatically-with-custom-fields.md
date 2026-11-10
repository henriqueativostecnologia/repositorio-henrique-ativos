---
fonte: https://help.asana.com/s/article/assign-work-automatically-with-custom-fields?language=en_US
baixado: 2026-11-10
---

# Assign work automatically with custom fields

One of the most important parts of any workflow is ensuring that information gets to the right people at the right time. By using a combination of rules and custom fields, we can ensure that tasks are assigned to the relevant person without manual intervention or the need to search for the right stakeholder.

This article shows how to add a custom field to a project, select the relevant values, and leverage rules to assign tasks to the right people based on those value selections. It uses the example of a bug tracking project, where colleagues report on bugs that have been found in-product.

## Add a custom field to your project

To get started, you'll need to add a custom field to the project and select some field values. These values will allow the rule to be triggered later on.

1.  In your project, click **+ Add field**.
2.  Choose a **Field title**, **Field type**, and **Description**.
3.  Add some custom field value options for people to choose from.

Now you've added the **Bug area** custom field to your project, the field and the field value selected will be displayed on each task in the project. This sets the stage for leveraging rules to automatically assign tasks to the relevant people.

## Add a rule to your project

Next, add a rule by clicking the **Customize** button in the top-right of your project.

Select **+ Add rule** from the pop-out menu.

## Use conditions and branching to automatically assign work

The rule that is implemented is fairly straightforward, though it does contain a number of branches for a number of different scenarios. When the custom field changes, the task is assigned to someone based on the particular value selected.

Looking at the workflow in detail, when the custom field value for **Bug area** is changed, Asana checks which value has been selected; one of **Performance**, **Billing**, **Privacy**, **Integrations**, or **Navigation** in this example. When the relevant value is selected, the action taken by the rule is to assign the task to the person responsible for that area.

This is how a workflow can use custom fields and rules together to automatically assign tasks to the right people.

[](https://forum.asana.com/c/forum-en/tips/6)
