---
fonte: https://help.asana.com/s/article/rule-triggers?language=en_US
baixado: 2026-11-10
---

# Automation triggers

[Automations](https://help.asana.com/s/article/rules?language=en_US) allow you to streamline routine tasks and establish workflows with ease. This article will cover the various automation triggers in more detail. For information on automation actions, please visit [this Help Center article](https://help.asana.com/s/article/rule-actions?language=en_US).

#### Related articles:

- [Automations](https://help.asana.com/s/article/rules)
- [Automation permissions](https://help.asana.com/s/article/rule-permissions)
- [Automation actions](https://help.asana.com/s/article/rule-actions)
- [Conditions and branching in automations](https://help.asana.com/s/article/conditions-and-branching-in-rules)

## What is a trigger?

An automation trigger in Asana is an event that activates a predefined automation, causing an automated action to occur. For an automation to work, it needs two main components: a trigger and an action. The trigger activates the automation so that the action can be performed automatically.

#### Trigger

This is the event that initiates the automation. Example triggers include:

- When a task is marked as complete
- When a due date is set
- When a task is added to a project.

#### Action

This is what happens automatically once the trigger event occurs. Example actions include:

- Assigning the task to a specific person
- Moving the task to a different section
- Creating a subtask

Let’s take a look at an example:

An automation can be created to automatically assign a task to someone (this would be the action) when a due date is set (this would be the trigger).

- Trigger: Due date is set
- Action: Assign task to ...

## Choose a trigger

Choose a automation trigger by following the steps below:

1.  Open your project and click on the **Customize** button on the top right.
2.  Click **Automations.**
3.  Click **Add.**
4.  Select **Start from scratch**.
5.  Click into the **+ What starts this workflow** card and choose where trigger happens
6.  Then, choose an option

## Trigger examples

### Date-based example

**Trigger: Task is overdue**

The **Task is Overdue** trigger can be chosen when creating a custom automation. You can choose from a few preset options or click **Custom** for more options.

With the **Custom** option, you can specify the number of minutes, hours, days, or weeks after the task becomes overdue for the automation to trigger.

If you choose **days** or **weeks** when setting up your trigger, it will ignore due times and fire based on due dates only. However, if you choose **minutes** or **hours**, it will respect due times.

**Additional notes**

- This trigger fires based on the moment a task becomes overdue, not simply because a task is overdue.
- This trigger will not retroactively fire upon automation creation for all of the existing tasks in the project that match its criteria. They will only fire for due events that happen after automation creation.
- These triggers only fire for incomplete tasks.
- Automations with day or week precision will not execute precisely at midnight. Rather, these automations will execute in the window between 00:00 and 01:00.

### Task-based example

**Trigger: Task moved**

These **Task moved** triggers will run the automation in the following situations:

1.  A task is moved to a specific section within the project where the automation is configured.
2.  A new task is added to the project where the automation is configured.

### Custom field change example

**Trigger: Custom field is changed**

You can create a custom automation based on custom field changes. This trigger monitors changes to the selected custom field and runs the automation when its value is changed. 

> It may be helpful to use coupled conditions in these cases. Coupled conditions allow you the option to combine a trigger and a condition in certain scenarios. Coupling enables the creation of more intuitive automations and simplifies the process of creating certain types of automations by reducing the number of setup steps required. You can learn more about coupled conditions [here](https://help.asana.com/s/article/conditions-and-branching-in-rules#:~:text=the%20workflow%20builder.-,Coupled%20triggers%20and%20conditions,-Coupled%20conditions%20for).

 

[ ](https://forum.asana.com/c/forum-en/tips/6)
