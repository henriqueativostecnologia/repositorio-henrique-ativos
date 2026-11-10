---
fonte: https://help.asana.com/s/article/conditions-and-branching-in-rules?language=en_US
baixado: 2026-11-10
---

# Conditions and branching in automations

**Available on Asana [*Starter*](https://asana.com/plan/starter), [*Advanced*](https://asana.com/plan/advanced), [*Enterprise*](https://asana.com/enterprise), and [*Enterprise+*](https://asana.com/enterprise) tiers, as well as [*legacy tiers*](https://asana.com/pricing-legacy) Business, and Legacy Enterprise.**

**Visit our [*pricing page*](https://asana.com/pricing) for more information.**

Conditions and branching give you more control over how your [automations](https://help.asana.com/s/article/rules?language=en_US) run and what actions they perform. By setting conditions within a path, you can create branches inside a single automation so that different actions happen depending on the state of a task when the automation is triggered.

## Adding conditions to your automation

Once you have set up your trigger, you can add conditions to control when your automation runs.

1.  Click **Add step** to open the **What happens next?** panel.
2.  Under **Flow controls**, select **Paths**. A **Check if** node appears on the canvas and a **Path** configuration panel opens on the right.
3.  Give your path a name that describes the condition you are checking for.
4.  Set the scope.
5.  Under **Conditions**, click **+ Add condition** to define what must be true for this path to run. You can search for a condition or select one from the list, which is grouped by category.

Once your condition is set, click **Add step** in the automation builder to add the actions that should run when that condition is met.

## Adding multiple conditions

You can add more than one condition to a path by clicking **+ Add condition** again. When multiple conditions are added, all of them must be met for the path to run. The canvas summarizes all active conditions on the path so you can see at a glance what is being checked.

## Adding branches

Branches let you define what happens under different conditions, all within the same automation. Once you have configured your first path, click **+ Add branch** on the canvas to add a second path. Give it a name, add its conditions, and configure its actions independently.

 

 

## The else path

If you want an action to run when none of your other conditions are met, you can use an else path. Click **+ Add branch** and in the **Path** panel set the condition to **No other path is matching**. This path will only run as a fallback when no other path conditions are satisfied.

## Removing a condition

To remove a condition from a path, open the **Path** panel and hover over the condition you want to remove. Click the trash icon that appears on the right.

## Removing a path

To remove a path entirely, click the three dot icon and select **Delete**.

[](https://forum.asana.com/c/forum-en/tips/6)
