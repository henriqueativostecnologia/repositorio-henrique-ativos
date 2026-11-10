---
fonte: https://help.asana.com/s/article/formula-custom-fields?language=en_US
baixado: 2026-11-10
---

# Formula custom fields

**Available on Asana [Advanced](https://asana.com/plan/advanced), [Enterprise](https://asana.com/enterprise "https://asana.com/enterprise") and [Enterprise+](https://asana.com/enterprise "https://asana.com/enterprise") tiers, as well as [legacy tiers](https://asana.com/pricing-legacy "https://asana.com/pricing-legacy") Business and Legacy Enterprise.**

**Visit our [pricing page](https://asana.com/pricing "https://asana.com/pricing") for more information.**

With formula custom fields, you can perform calculations directly in Asana, making managing data easier and significantly enhancing your productivity.

#### Related articles

- [Custom fields](https://help.asana.com/s/article/custom-fields?language=en_US)
- [Filtering and sorting custom fields ](https://help.asana.com/s/article/filtering-and-sorting-custom-fields?language=en_US)
- [Custom field types and limitations](https://help.asana.com/s/article/custom-field-types-and-limitations?language=en_US)
- [Custom field access levels](https://help.asana.com/s/article/custom-field-access-levels?language=en_US)

Some examples of when you can use formula custom fields are:

|                     |                                                                    |
|---------------------|--------------------------------------------------------------------|
| **Example**         | **Formula**                                                        |
| Capacity management | Effort = \[Quantity of weeks\] \* \[Allocation\]                   |
| Time to complete    | \[Completed at\] – \[Created at\]                                  |
| Time/amount overdue | \[Completed at\] – \[Due date\]                                    |
| Billing             | \[Amount per hour\] \* \[Total hours\]                             |
| Estimated hours     | (\[Due Date\] – \[Start Date\]) \* \[Hrs per week\]                |
| Burn rate           | (\[Starting Balance\] – \[Ending Balance\]) / \[Number of months\] |
| Prioritization      | (\[Weight\] \* \[Input\]) + (\[Weight\] \* \[Input\])              |

You can add these new formula custom fields to your domain’s global custom field library.

## Functions

+-------------------------------+-------------------------------+-------------------------------+-------------------------------+-------------------------------+
| **Function**                  | **Definition**                | **Syntax**                    | **Examples**                  | **Available in**              |
+-------------------------------+-------------------------------+-------------------------------+-------------------------------+-------------------------------+
| Add                           | Add two values                | Add(value1, value2)           | Add(\[BudgetA\], \[BudgetB\]) | Basic                         |
|                               |                               |                               |                               |                               |
|                               |                               | Add(\[value\], number)        | Add(\[Subtotal\], 3)          |                               |
|                               |                               |                               |                               |                               |
|                               |                               | \[value1\] + \[value2\]       | \[BudgetA\] + \[BudgetB\]     |                               |
|                               |                               |                               |                               |                               |
|                               |                               | \[value\] + number            | \[Subtotal\] + 3              |                               |
+-------------------------------+-------------------------------+-------------------------------+-------------------------------+-------------------------------+
| Subtract                      | Subtract two values           | Subtract(value1, value2)      | Subtract(Budget, Spend)       | Basic                         |
|                               |                               |                               |                               |                               |
|                               |                               | \[value1\] - \[value2\]       | Subtract(Due date, Start      |                               |
|                               |                               |                               | date)                         |                               |
|                               |                               |                               |                               |                               |
|                               |                               |                               | \[Budget\] - \[Spend\]        |                               |
|                               |                               |                               |                               |                               |
|                               |                               |                               | \[Due date\] - \[Start date\] |                               |
+-------------------------------+-------------------------------+-------------------------------+-------------------------------+-------------------------------+
| Multiply                      | Multiply two values           | Multiply(value1, value2)      | Multiply(Hours, Rate)         | Basic                         |
|                               |                               |                               |                               |                               |
|                               |                               | \[value1\] x \[value2\]       | \[Hours\] \* \[Rate\]         |                               |
+-------------------------------+-------------------------------+-------------------------------+-------------------------------+-------------------------------+
| Divide                        | Divide two values             | Divide(value1, value2)        | Divide(Remaining, Total)      | Basic                         |
|                               |                               |                               |                               |                               |
|                               |                               | \[value1\] / \[value2\]       | \[Remaining\] / \[Total\]     |                               |
+-------------------------------+-------------------------------+-------------------------------+-------------------------------+-------------------------------+
| DateAdd                       | Add days to a date            | DateAdd(date, number)         | DateAdd(\[Due date\], 3)      | Advanced                      |
+-------------------------------+-------------------------------+-------------------------------+-------------------------------+-------------------------------+
| DateSubtract                  | Subtract days to a date       | DateSubtract(date, number)    | DateSubtract(\[Due date\], 3) | Advanced                      |
+-------------------------------+-------------------------------+-------------------------------+-------------------------------+-------------------------------+
| Rollup                        | Sum up all subtasks in a new  | Rollup(value1)                | Rollup(#Field1) + (#Field1)   | Advanced                      |
|                               | field.\                       |                               |                               |                               |
|                               | To include main task values,  |                               | Rollup(#Field1)               |                               |
|                               | add the field again as shown  |                               |                               |                               |
|                               | in the first example.         |                               |                               |                               |
+-------------------------------+-------------------------------+-------------------------------+-------------------------------+-------------------------------+

 

## Inputs

Inputs are the various data types that can be referenced within a formula to perform calculations or generate dynamic content. Most of the available inputs will be the fields that exist on a project or portfolio.

### Fields

- Date and number custom fields added to a project or portfolio can be used as input to a formula.
- Metadata or attribute fields can also be used for formulas such as:
  - Due date: Allows you to incorporate task due dates into your formulas, enabling dynamic calculations based on deadlines.
  - Start date: Allows you to incorporate the start dates of tasks into your formulas.
  - Created on: Allows you to reference the creation date of tasks within your formulas.
  - Completed on: Allows you to reference task completion dates within your formulas.

> When used in formulas, these fields are always UTC timestamps.

### Today input

The "Today" input lets you reference the current date in a formula. This is particularly useful for creating date-based calculations and automatically updating project timelines.

- The "Today" formula is a midnight timestamp of today’s date.
- Timezone consideration: The date calculation is influenced by the timezone of the person who created or last edited the formula. This is similar to how time zones are handled in Asana's rules.
- Dynamic refresh: The value of the "Today" formula refreshes when any user views or loads the project where the formula is being applied. This ensures that the date remains current and up-to-date.

## Adding basic formula custom fields

By leveraging the add, subtract, multiply, and divide operators, you can perform a wide range of calculations within Asana and gather powerful insights about your work. Use these formulas to efficiently manage numerical data when creating budgets, analyzing sales figures, calculating capacity, and many more scenarios.

#### To add a formula custom field:

1.  You can add a formula custom field from the **Customize** menu or by clicking **+Add field** on the column header
2.  Select **Formula** as the field type
3.  In the **Formula builder**, you can use any existing numerical custom fields
4.  Choose from **Add**, **Subtract**, **Multiply**, or **Divide**
5.  Click **Create field**

 

Here, the Event manager wanted to compare resources. To do so, they calculated the difference between the budget and what they spent, so they created the **Difference** formula custom field. The formula they used in the formula builder was **Budget minus (-) Spend**.

Another example of when you can use a formula custom field is when you’re trying to calculate your team’s capacity.

 

Here, the Event manager calculated the difference between the **Estimated time** and the **Actual time** for each task to see which task took more or less time than expected. The formula they used in the formula builder was **Estimated time minus (-) Actual time**.

Other examples of when you can use formula custom fields are:

- Capacity management: Quantity of weeks times (x) Allocation = Effort
- Time to complete: Completed at minus (-) Created at
- Time/amount overdue: Completed at minus (-) Due date
- Billing: Amount per hour times (x) Total hours (by person)

> You can add these new formula custom fields to your domain’s global custom field library.

## Adding advanced formula custom fields

With advanced formula custom fields, you can create more complex formulas with more than one operator.

#### To add an advanced formula custom field:

1.  Add a formula custom field from the **Customize** menu or by clicking **+Add field** on the column header
2.  Select **Formula** as the field type
3.  In the **Formula builder**, click **Switch to advanced mode**
4.  From here, you can start typing a function or field or select them from the **Functions** and **Fields** menu

## Formula chaining

With formula chaining, you can use existing formula custom fields as inputs to another formula you're creating.

For example, if you have an existing formula that's calculating **Budget Remaining,** you can use this value to build another formula (i.e. Burn Rate = Budget Remaining / Total Budget).

### Error messages and limits

Some things to keep in mind as you're building more complex formulas:

- Both fields must be the same type. If you're using a numeric based formula, other inputs must be numeric based too.
- Date fields can only be subtracted.
- You can use up to 10 existing formula custom fields as inputs to a new formula.
- Formula custom fields that are shared globally with your domain can only use other shared formula custom fields as inputs. Keep in mind that adding a global formula custom field will also add formula input fields to your project as well (you can have up to 100 custom fields in a single project).
- A formula that contains another formula cannot be dependent on itself. For example, if Formula C = (Formula A) + (Formula B), you won't be able to use Formula C as input to Formula A or B.

You can create up to two layers of formulas when creating a new formula:

- Valid: Formula 1 = Custom field A + Custom field B
- Valid: Formula 2 = Formula 1 / Custom field C (1st layer)
- Valid: Formula 3 = Formula 2 \* Formula 1 (2nd layer)
- Not possible: Formula 4 = Formula 3 \* Formula 1

## Sorting numeric custom fields

You can sort your formula custom fields by ascending or descending.

#### To sort:

1.  Click **Sort**
2.  Select the custom field you want to sort by
3.  Select **Ascending** or **Descending**
4.  Click **Apply**
5.  You can also click on the drop-down next to the custom field to sort

## Reporting on formula custom fields

Use formula custom fields when creating charts to visualize data.

#### To create a chart using formula custom fields:

1.  Navigate to the **Dashboard** tab
2.  Click **+Add chart**
3.  On the **Y-axis**, select the formula custom field
4.  Click **Create**

> Learn more on how to create charts with our [Reporting](https://help.asana.com/s/article/universal-reporting?language=en_US "Reporting") Help Center article.

## Using formula custom fields as effort in workload

You can use formula custom fields as the [effort](https://help.asana.com/s/article/portfolio-workload-and-universal-workload?language=en_US#gl-effort "effort") when creating [universal or portfolio workloads](https://help.asana.com/s/article/portfolio-workload-and-universal-workload?language=en_US "universal or portfolio workloads").

For example, here we are using the formula custom field **Capacity** as the team's effort.

## Using formulas in portfolios

Portfolios allow you to oversee multiple projects and gain a comprehensive view of your organization's initiatives. By incorporating formula custom fields into portfolios, you can perform calculations, track key metrics, and generate insights across various projects. Formula custom fields enable you to enhance decision-making, optimize resource allocation, and gain a holistic understanding of your portfolio.

Add a basic or advanced formula custom field to your portfolios through the **+** button or **Customize** menu.

## Using formulas in bundles

Bundles are powerful tools for standardizing processes and ensuring consistency across multiple projects. By incorporating formula custom fields within bundles, you can perform calculations and track key metrics specific to your standardized processes.

#### [](https://github.com/Asana/asanadotcom/blob/master/_content/guide/07-help/11-premium/04-formula-custom-fields.md#to-add-a-global-formula-to-a-bundle)To add a global formula to a bundle:

1.  From the **Customize** menu, navigate to bundles
2.  Choose the bundle you want to edit
3.  Click **Edit**
4.  Scroll down to **Fields** and click **+Add custom field**
5.  From here, you can create a new formula custom field or choose an existing global formula custom field from the library
6.  Click **Continue** and then **Apply changes**

## Formatting

Formula custom fields support the same formatting as numerical custom fields. This allows you to display your calculation results with the appropriate units and formatting.

When creating or editing the formula field, click **Formatting** to select your preferred format and decimal places.

[](https://forum.asana.com/c/forum-en/tips/6)
