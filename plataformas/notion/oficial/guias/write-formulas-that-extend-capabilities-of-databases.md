---
fonte: https://www.notion.com/help/guides/write-formulas-that-extend-capabilities-of-databases
baixado: 2026-11-10
---

# How to write Notion formulas that extend the capabilities of your databases

## Learn how to write formulas in Notion databases to extract useful data, run calculations, and more. This guide covers formula terminology, how to write a formula, troubleshooting, and lots of beginner examples.

12 min read

Formulas add functionality to already powerful Notion databases. In this guide we'll cover how to get started writing formulas.

------------------------------------------------------------------------

Tempted to dip your toes into formulas, but not sure where to start?

Formulas make your databases even more powerful. You can extract useful data, run calculations and go beyond Notion’s out-of-the-box options to build custom database properties showing exactly what you need to see.

In this guide, you’ll discover how to write formulas and different ways to use them.

Already a formulas user?

## [See the information you need using database formulas](https://www.notion.com/help/guides/write-formulas-that-extend-capabilities-of-databases#see-the-information-you-need-using-database-formulas)

Notion has a wide range of database properties that help you organize and store information. Formulas multiply the power of properties by letting you run calculations and perform operations using the information entered in properties. Results appear across the entire database, and can save you spending time on manual data entry.

To add a formula to your database, select Formula in the properties menu, and click `Edit property` to start writing your formula. Formulas apply across the whole row of a database to calculate, modify or reformat information.

Before we get into examples of formulas, we’ll start by defining some Notion formula terminology.

## [Notion formulas terminology](https://www.notion.com/help/guides/write-formulas-that-extend-capabilities-of-databases#notion-formulas-terminology)

Notion formulas work on existing properties in your database to produce an output. Unlike a spreadsheet, the formula applies to the entire property.

In the formula editor, you’ll find all the different components (think of them like recipe ingredients) you can combine to produce your desired results. You can either select these ingredients from the menu on the left, or type out your formula in the box above.

Notion's formula editor contains properties, functions, and more.

### [The components of a formula](https://www.notion.com/help/guides/write-formulas-that-extend-capabilities-of-databases#the-components-of-a-formula)

At the highest level, formulas perform actions on your existing database properties. These actions can be anything from simple mathematical operations — like adding number columns — to complex, pre-defined functions like finding the amount of time between two dates.

When writing a formula, you have to choose inputs (the properties you want to perform operations or functions on) then explain the action you want to perform. Then, your output (or result) will be displayed in the database.

### [Input properties](https://www.notion.com/help/guides/write-formulas-that-extend-capabilities-of-databases#input-properties)

To begin your formula, you need to have inputs. These can either be database properties, constants such as `pi`, or literal values that you will type in.

When you use database properties as inputs, the results will change according to how those properties are completed, and will show different results in each row if property values are different.

### [Functions](https://www.notion.com/help/guides/write-formulas-that-extend-capabilities-of-databases#functions)

Functions are the instructions of your formula that explain the actions you want to perform on the inputs.

This could be anything from multiplying one value by another, subtract one from another, or modifying or reformatting an input in some way.

Operators can be arithmetic calculations, or comparisons testing one input value against another — for example to see whether one value is larger or not, or whether a Status property is marked as Complete.

A concatenation operator combines text or numbers, for example to combine a first and last name.

You can select any properties in the database as inputs. Then, you can perform actions on these using the following elements:

- **Functions** — Predefined formulas that you can combine into a larger formula. These are more advanced operators that already include inputs, such as `dateAdd` to add a certain number of days, months, or years to a date, `toNumber() `to convert text to a number, or `replaceAll()` to search text for a pattern and replaces all matches with some other text.

- **Built-ins** — Built-in operators and values you can use in formulas. Operators can be arithmetic (`+`, `-`, etc), comparisons (`>` to show to greater of two values, `==` to test if two values are the same) or concatenations (`+` when used on text will combine both values). Built-in values include `true` and `false`.

- **Person and page metadata** — Reference metadata that isn't part of the database, including a person’s email address or name (`person.email()`, `person.name()`), and individual page blocks (`block.prop("Created By")`, `block.prop("Last Edited Time")`)

[Outputs](https://www.notion.so/help/formulas#formula-data-types) from your formulas can be in any of the following formats, which include many property types in databases:

- Text

- Numbers

- Boolean/checkbox (true or false values)

- Dates

- People

- Pages

- Lists

Pay attention to the data type you are working with.

## [How to write a Notion formula](https://www.notion.com/help/guides/write-formulas-that-extend-capabilities-of-databases#how-to-write-a-notion-formula)

In order to write functioning formulas that return a correct value you need to know how to compose formulas.

Formulas can range from one simple input to an combination of several calculations that produce a single value.

Your formula will need to contain different elements depending on the value you want to produce, and most formulas will contain several operations that must be nested and sequenced correctly.

Here’s how to write a Notion formula in 3 steps:

- **Step 1: Define what you want to achieve** — Before you write the formula you must define the output or result you’re hoping for. Remember that outputs can be in the form of any Notion data type — text, people, number, checkbox, block or date.

- **Step 2: Figure out the inputs you need** — Consider what values and information you need to input in order to produce your desired result. Think about the existing properties in the database — are there any more properties you need to add? Your formula can contain a mixture of properties, operators and functions.  
  Some useful operators and functions you might include in your formulas:

  - `dateAdd `— dateAdd takes a date input and adds to it, returning a new date. Similar functions are `dateSubtract` and `dateBetween`.

  - `if` — Allows you to write **if-then** statements in a Notion formula. These statements contain a condition to be evaluated for truthfulness, plus a `then` statement (if the condition is true) and an `else` statement (if the condition is false.)

  - `contains` — tests whether the first argument contains the second argument (only accepts text.)

  - `format` — Use `format()` to reformat dates, booleans, numbers and more to text.

All formula components

- **Step 3: Write and test your formula** — Use the built-in and help center documentation to compose your formula, test and check your results to make sure it works! Pro-tip: test your formula in smaller bits to make sure you’re getting the desired output at each step.

Nesting functions in your formulas

Now we’ve gone through formula fundamentals, here are 5 examples you can try out in your own databases.

## [1. Calculate sums of money](https://www.notion.com/help/guides/write-formulas-that-extend-capabilities-of-databases#1.-calculate-sums-of-money)

If you have two or more properties in your database you can run calculations like add, subtract, divide multiply, etc.

Calculations save you from manually entering data (and reduce the risk of human error.)

In a database where you enter all your invoices, create a number property to introduce the net amount of each invoice and another for the percentage of tax.

Next, create a formula property to calculate the amount of tax per invoice.

> `prop("Net ") * prop("Tax (%)")`

Using another formula property, calculate the gross by adding the tax to the net amount.

> `prop("Net ") + prop("Tax ($)")`

Use formulas to run calculations on sums of money, like for an invoice tracker.

Calculations can be used in many other ways, like calculating commission on sales or converting units of measurement, such as centimeters to feet and inches or Celsius to Fahrenheit.

Notion formulas perform calculations across properties

## [2. Count and display the number of tags or people](https://www.notion.com/help/guides/write-formulas-that-extend-capabilities-of-databases#2.-count-and-display-the-number-of-tags-or-people)

If you use a Notion database to collect ideas and feedback, you can use an Upvote formula to easily count the number of votes for each entry.

In a database containing new feature ideas, topic suggestions for a meeting, or product updates that need to be prioritized, people can “Upvote” entries by tagging themselves in a Person property.

Once you’ve added a Person property called “Upvoted by”, you can then enter the following formula:

> `length(prop("Upvoted by")) `or `prop("Upvoted by").length()`

This will add up the number of people in the “Upvoted By” column, and display that as a number.

You could modify this formula to count the number of attendees at a meeting or event, or show how many people are collaborating on a project.

## [3. Show time between two dates](https://www.notion.com/help/guides/write-formulas-that-extend-capabilities-of-databases#3.-show-time-between-two-dates)

With date formulas, calculate the amount of time passed since a date, days to go until a future date, or amount of time between two dates.

You can also use dynamic dates in formulas — last year, next month, a week from today, etc.

In a project or task management database, use a formula like this to calculate how much time you have left until a project is due.

> `dateBetween(prop("Due date"), now(), "days")`

Use a formula to calculate how many days are left before a project's due date.

Date formulas are versatile, and they could also be used in a team database to calculate everyone’s age by subtracting their date of birth from today’s date, and to calculate how long each team member has been at the company.

> `format(round(dateBetween(now(), prop("Joined"), "days") / (365 / 12) * 10) / 10) + " months"`

## [4. Combine text](https://www.notion.com/help/guides/write-formulas-that-extend-capabilities-of-databases#4.-combine-text)

The `+` operator can combine text, or numbers (by first converting the number to text). In a team’s People database, you might have two columns for first and last names. Then, a third “Full name” column, a formula would combine both names.

> `prop("First name") + " " + prop("Last name")`

Use formulas to calculate employee tenure and names.

Another use case for this is generating URLs by converting different tags to text, then combining them into a URL. Like in the case of this UTM link generator:

> `ifs(empty(prop("URL")),"", empty(prop("UTM Source")) or empty(prop("UTM Medium")) or empty(prop("UTM Campaign")),`  
> `"You must enter medium, source and campaign name.",`  
> `prop("URL") + "?utm_source=" + prop("UTM Source") + "&utm_medium=" + prop("UTM Medium") + "&utm_campaign=" + prop("UTM Campaign"))`

## [5. Filter relation data](https://www.notion.com/help/guides/write-formulas-that-extend-capabilities-of-databases#5.-filter-relation-data)

Relation properties bring information from one database into another. If you want to filter the information coming into your database through a relation, you can do so using a formula.

For example, you may have a projects database that’s related to your meetings database, and want to filter the related meetings to only show upcoming meetings.

You can filter related meetings where the date is later than “now”.

> `prop("Meetings").filter(current.prop("Date") > now())`

## [How to troubleshoot errors](https://www.notion.com/help/guides/write-formulas-that-extend-capabilities-of-databases#how-to-troubleshoot-errors)

If your formulas aren’t written correctly, you’ll get an error message when you try to click save. Sometimes, Notion will give you a hint as to what might be wrong - whether it’s a missing bracket or input, or incorrect operation.

However, if you’re not sure why a formula isn’t working, here are some things you can try:

- **Check that you’ve correctly nested operations into parentheses** — If your formula contains several functions, you need to make sure each action is separated and contained with a set of brackets.

- **Reference database properties accurately** — The formula editor is case sensitive, and will only recognize inputs that are exactly the same. When referencing a property, make sure to type it exactly as it is in the database, or just select it from the menu.

- **Check for list data types** — When you’re trying to perform a calculation on a list data type (like people properties or relation properties), you may need to first map your data so that the calculation can be preformed one list “entry” at a time.

- **Ensure data types match up** — Check that your data types match in your formula. You can’t perform calculations with numbers that are contained in text, or join numbers and text without converting the format first. If you’ve mixed data types in a formula you may get a “Type mismatch” error message.

- **Test your formulas** — You may not be able to tell if a formula is working if there’s only one or two entries in a database. Try changing the inputs (property values) or adding more database entries to check that your formula is working as it should.

All formulas resources

- An intro to formulas terminology [here](https://notion.so/help/formulas).

- A beginner guide on how to write formulas [here](https://notion.so/help/guides/write-formulas-that-extend-capabilities-of-databases).

- A guide on what’s new with formulas 2.0 [here](https://notion.so/help/guides/new-formulas-whats-changed).

- A list of all the functions Notion formulas supports [here](https://notion.so/help/formula-syntax).

Share this guide

------------------------------------------------------------------------
