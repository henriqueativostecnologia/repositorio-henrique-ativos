---
fonte: https://help.asana.com/s/article/request-a-task-review-with-a-simple-automation?language=en_US
baixado: 2026-11-10
---

# Request a task review with a simple automation

Requesting feedback on work before it proceeds to the next stage is a common workflow. For example, you may need a legal team to review marketing copy before it gets published. This article outlines how to set up a simple automation using rules to automatically request reviews on tasks when needed.

## Add a custom field

First, you'll need to add a custom field to your project to indicate which tasks require review. For this example, we'll use a custom field called **Needs review** with the options **Yes** and **No**.

1.  Click the **Customize** button in the top right of your project.
2.  Under **Add**, select **Fields**.
3.  In the new window, enter **Needs review** as the field title.
4.  Choose **Single-select** as the field type.
5.  Finally, click **Create field**.

Now that the custom field is added to the project, it's possible to indicate which tasks require review and which don't, with a couple of clicks. This also means we can use the custom field value as a trigger for a rule.

## Set up the simple automation

Next, we'll set up a rule which reassigns the task, adds a comment asking for review, and sets a due date. All of this is performed automatically when the **Needs review** field value is set to **Yes**.

1.  Within the **Customize** menu, under **Add**, select **Rules** to open the rule builder.
2.  Click the card named **When**, to add a trigger.
3.  Browse the options on the right side of the rule builder and locate the trigger **Custom field is changed**. Click the option **Needs review is changed**.
4.  Next, click the card named **Check if**, to add a condition.
5.  On the right side of the rule builder click the condition **Custom field is…** Next, choose the condition **Needs review is set to...** and set the option to **Yes**.
6.  Finally, click the card named **Do this...** to set an action for the rule to perform.
7.  Under **Change task field to…**, change the assignee to a member of the legal team, and change the due date to a few days in the future.
8.  Under **Add to task**, you can add a comment to give the legal team some context.
9.  When finished, click **Publish rule**.

Now when any project member sets the **Needs review** field to **Yes**, the rule will automatically add a comment requesting review and take any other configured actions. Reviewers can then provide feedback via comments or by updating the task details as needed.

See the below example. Alan has simply changed the Needs review field value and Asana has automatically chosen the assignee, due date, and added a comment.

You can continue to build on this automation by adding further rules to move the task to the next stage once the review is complete. This simple automation helps streamline the review process by automatically notifying reviewers when their input is needed, without requiring manual intervention. It provides a standardized way to request reviews across your organization.

 

[](https://forum.asana.com/c/forum-en/tips/6)
