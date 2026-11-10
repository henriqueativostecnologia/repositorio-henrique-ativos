---
fonte: https://help.asana.com/s/article/use-dependencies-to-kick-work-off-at-the-right-time?language=en_US
baixado: 2026-11-10
---

# Use dependencies to kick work off at the right time

When building out a project we may know the order in which tasks need to be completed well in advance, but the exact dates and timing of deliverables may not be so easy to predict - especially if planning months in advance.

We can use dependencies to block tasks, meaning assignees won't accidentally begin work before they're due to start, avoiding wasted time and energy. We can also use dependencies within workflows, so that when tasks are no longer blocked, rules can move work forward automatically.

## Create a dependency between tasks

In the example below, Diana is working on some Japanese-language assets for an upcoming launch. Chris is working on the same project, but he designs the landing page for the event, and will use some of Diana's assets when building this out.

Chris can't actually begin work on his part until he has the deliverables from Diana, so he creates a dependency - using Diana's task to block his own.

To create a dependency, follow these steps:

1.  Open the task details pane and find the **Dependencies** field.
2.  Type the name of the blocking task into the typeahead, or paste the URL.
3.  Switch between **Blocked by** or **Blocking**, depending on the direction of the dependency.

The result is that one task now blocks another. A visual indicator that a task is blocked is the small hourglass symbol which replaces the usual checkmark beside a task name. Dependency details are also present in the task details pane.

## Create a rule triggered by dependency changes

Next, create a rule which uses the dependency change as a trigger. This way, Chris doesn't need to constantly monitor the status of the blocking task to find out when he should begin his work.

To set up the rule, follow these steps:

1.  Add a rule to the project by clicking the **Customize** button in the top-right corner.
2.  Select **+ Add rule** from the pop-out menu.
3.  Select the trigger **Task is no longer blocked**.
4.  Remove the **Check if** condition card by clicking **X**, unless needed for more precise rule control.
5.  Add actions such as setting a due date, moving the task, and adding collaborators.

The result is that when a task in the project is no longer blocked, the rule will automatically set a due date, move the task to the relevant section, and add the necessary collaborators.

In this case, when Diana completes her Japanese-language assets task, the task assigned to Chris will receive a due date among other updates, and Chris is informed through inbox notifications as well as spotting the task in his My tasks list.

A small workflow like this can reduce the need for manual oversight significantly, enabling team members to focus on their other tasks and be informed automatically when it's time for work to begin.

 

[](https://forum.asana.com/c/forum-en/tips/6)
