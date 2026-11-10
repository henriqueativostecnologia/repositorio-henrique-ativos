---
fonte: https://www.notion.com/help/formulas
baixado: 2026-11-10
---

# Intro to formulas

In this help doc

## In a Notion database, you can add a formula property that lets you run all kinds of calculations and functions based on other properties. You can use formulas to manipulate existing data and arrive at many other helpful values.

------------------------------------------------------------------------

Notion formulas can perform helpful calculations using your existing database properties, built-ins, and functions.

## [Formula examples](https://www.notion.com/help/formulas#formula-examples)

Let’s look at a few different ways to use formulas. If you’re ready to get started building your own, jump to our instructions on creating a formula [below →](https://www.notion.com/help/formulas#create-a-formula)

### [Example 1: Project management](https://www.notion.com/help/formulas#example-1-project-management)

In this example, we’ll use three formulas to track the progress of projects.

You can explore and play with the formula setups for this example by duplicating [this page](https://notion.notion.site/formulaexample1?pvs=4) to your workspace!

[TABLE]

### [Example 2: Project brainstorming](https://www.notion.com/help/formulas#example-2-project-brainstorming)

In this example, we’ll use two formulas to brainstorm project ideas, calculate a priority score for each of them, and count the number of upvotes each project receives.

You can explore and play with the formula setups for this example by duplicating [this page](https://notion.notion.site/formulaexample2?v=1a5efdeead0580e3bacf000ce6a750db&pvs=4) to your workspace! For another setup that uses the RICE framework, check out this [template](https://www.notion.com/templates/rice-prioritization-worksheet?srsltid=AfmBOoqhi5UnMlxoMXorqFotrYl9c5-Ht90B6ZuKD5zPMMaD7ZsgIyLF).

[TABLE]

### [(Advanced) Example 3: Task management automation](https://www.notion.com/help/formulas#(advanced)-example-3-task-management-automation)

In this example, we’ll use some formulas in a database [automation](https://www.notion.com/help/database-automations) (another kind of database property) to make it easier to manage projects and tasks as they’re completed by marking a parent task as `Done` when all its subtasks are `Done`.

Database automations have triggers and actions that are taken based on those triggers. Formulas allow you to define variables that you can then use in your actions.

You can explore and play with the formula setups for this example by duplicating [this page](https://notion.notion.site/formulasexample3?v=1a5efdeead0580d08754000c5ef09165&pvs=4) to your workspace!

[TABLE]

**More formula inspiration**

- [This Notion template](https://www.notion.com/templates/time-between-dates-calculator) calculates the time between two dates with a formula property.

- [This Notion template](https://www.notion.com/templates/brainstorming-with-upvotes) uses a formula to count upvotes for different ideas.

- You can find even more example formulas [here →](https://www.notion.com/help/guides/write-formulas-that-extend-capabilities-of-databases)

## [Where formulas can be used](https://www.notion.com/help/formulas#where-formulas-can-be-used)

In Notion, you can use formulas in a few different ways:

- As a database property, which is what this article primarily covers.

- In a [button](https://www.notion.com/help/buttons#mentions-and-formulas-in-button-actions) action.

- In a [database button](https://www.notion.com/help/database-buttons) action.

- In a [database automation](https://www.notion.com/help/database-automations) action.

## [Create a formula](https://www.notion.com/help/formulas#create-a-formula)

To create a formula database property:

1.  Select the slider icon at the top of a database → `Edit properties` → `New property`.

2.  Select `Formula`.

3.  Give your property a name if you’d like.

4.  Select `Edit formula`.

## [Edit a formula](https://www.notion.com/help/formulas#edit-a-formula)

Once you’ve created a formula in a database or button, you’ll be able to build and edit that formula in the formula editor, which looks like this:

The field at the top is where you enter and edit your formula. As you write your formula at the top of the editor, the editor will let you know what’s missing, or what the formula expects in order to return a value to you.

The panel on the left side of the edit shows the elements that you can use in the formula — in other words, the properties, built-ins, and functions that are available to you.

The panel on the right side defines formula elements as you hover over them in the left panel. It also gives you examples of how you might use those elements and how they should be structured.

If you open the formula editor from a database row, you'll see a live preview of the result of the formula for that row.

Having trouble with your formula? Learn about common formula errors and how to troubleshoot them in [this article →](https://www.notion.com/help/common-formula-errors)

## [Create and edit formulas with Notion AI](https://www.notion.com/help/formulas#create-and-edit-formulas-with-notion-ai)

- This feature is available on Business and Enterprise Plans.

Know what you want your formula to do, but not quite sure how to build it? Want to make some tweaks to an existing formula? See an error in your formula, but don’t know how to fix it? Notion AI can help.

When you’re in the formula editor, you’ll see a field containing the Notion AI face. Click into this field and tell Notion AI what you want your formula to do, or ask questions about the formula to understand it better.

Here are some example prompts you can give Notion AI:

- “Turn the title property into a URL slug.”

- “Return ⚠️ if the due date has passed.”

- “Add one day to the date property and make the output green and bold.”

- “Return the date property from the related database” (Notion AI knows about your relations’ properties too!)

- “Italicize the output of this formula.”

- “Fix the errors in this formula.”

- “Make this formula handle edge cases.” (For example, Notion AI could add an if statement so that the formula doesn’t fail when a field is empty.)

- “What does this formula do?”

Once you enter your prompt, Notion AI will generate a formula or respond to your query about it. You can also see a preview of your formula output as well as toggle on `Show types` to see the output type (for example, text), so you can make sure everything looks the way you want. You can undo Notion AI's changes, give it further prompts, or give a thumbs up or thumbs down to let us know how it did.

When you’re creating and editing formulas using Notion AI, note that Notion AI currently doesn’t support the following:

- Iterative logic (like `for` loops).

- Random generations that would require a `random()` function, which Notion formulas don’t have. A prompt like “Generate a random number between 1 and 10” wouldn’t work.

- Remembering previous prompts.

Notion AI can help you with formula properties as well as formulas inside [buttons](https://www.notion.com/help/buttons#mentions-and-formulas-in-button-actions), [database buttons](https://www.notion.com/help/database-buttons), and [database automations](https://www.notion.com/help/database-automations).

## [What formulas are made of](https://www.notion.com/help/formulas#what-formulas-are-made-of)

Formulas can be created using a combination of:

- Properties.

- Built-ins, or operators and booleans that are used to set up a specific calculation. Some examples include `+` (add), `false`, and `or`.

- Functions, or actions that the formula can take to return a certain output. Some examples include `replace`, `sum`, and `sort`.

A full list of the built-ins and functions that are available in formulas is available [here →](https://www.notion.com/help/formula-syntax)

## Contents

- [Formula examples](#formula-examples)
- [Example 1: Project management](#example-1-project-management)
- [Example 2: Project brainstorming](#example-2-project-brainstorming)
- [(Advanced) Example 3: Task management automation](#(advanced)-example-3-task-management-automation)
- [Where formulas can be used](#where-formulas-can-be-used)
- [Create a formula](#create-a-formula)
- [Edit a formula](#edit-a-formula)
- [Create and edit formulas with Notion AI](#create-and-edit-formulas-with-notion-ai)
- [What formulas are made of](#what-formulas-are-made-of)
