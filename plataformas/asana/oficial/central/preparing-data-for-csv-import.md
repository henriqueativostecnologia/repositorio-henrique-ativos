---
fonte: https://help.asana.com/s/article/preparing-data-for-csv-import?language=en_US
baixado: 2026-11-10
---

# Preparing data for CSV import

Get started in Asana using your own data in an easy and fast way. The CSV Importer will help you move your workflow out of spreadsheet software such as Excel or Smartsheet to Asana, so you can get started right away on any project. You can also import data from [other work management tools](https://asana.com/guide/help/api/importing-csv-from-other-tools).

When preparing your data for CSV import into Asana, it's essential to ensure that your CSV file is correctly formatted. Below are detailed steps and important tips to help you successfully import your data.

#### Related articles

- [Advanced CSV import options](https://help.asana.com/s/article/advanced-csv-import-options?language=en_US)
- [Import data from other tools to projects in Asana](https://help.asana.com/s/article/import-data-from-other-tools-to-projects-in-asana?language=en_US)

## Organize the data in your spreadsheet

The order of columns in your CSV file must be precise. The **Task Name** must be the first column, followed by **Description**, **Sections**, and **Assignee**. Follow the order below for other fields.

1.  **Name**: use this column for the names of the tasks in your project.
2.  **Description**: use this column to provide details and context within the task.
3.  **Section**: a new section will be created once you manually move tasks into the desired section or column.
4.  **Assignee**: assign one owner to each task by adding the email address of an Asana user from your workspace or organization. Tasks created in Asana can only be assigned to one user.
5.  **Collaborators**: you can add several of your colleagues as collaborators on a task by adding email addresses of valid Asana users from your workspace or organization on a separate column. Take care to separate them with a comma and do not add any spaces in between.
6.  **Start Date**: add a separate column for start dates, available with a paid subscription. If you do not have a paid subscription, the information in the start date column will appear in the description of your task.
7.  **Due Date**: use the standard US date format of month/day/year to track the due date of each task.
8.  **Type**: set "Milestone” as a value to differentiate milestones from regular tasks in your project.
9.  **Dependents:** used to specify dependencies between tasks. To specify dependencies via the CSV Importer visit [this Help Center article](https://help.asana.com/s/article/advanced-csv-import-options?language=en_US#gl-dependencies).
10. **Other information**: additional column information will be listed from top to bottom in the task description field in the order of your columns.
11. **Parent Task**: when importing subtasks, it is critical to link them correctly to their parent tasks. This is particularly important when migrating from tools like Smartsheet, which can have many levels of subtasks. Ensure the naming is exact for subtasks to link to the correct parent task. For guidance on setting this up, please refer to [this Help Center article](https://help.asana.com/s/article/advanced-csv-import-options?language=en_US#gl-subtasks). Parent tasks must be listed before the subtask in the rows.

If any column contains incorrect data, such as an email address in the **Due Date** column, none of the due dates will import correctly. A new text-based field will be created instead.

> Always include a header row with column names so that the **CSV Importer** can recognize the type of data you are importing. The headers must use title case.

### Avoid small errors

Even the smallest errors can affect the import process. For instance, a space or a period after a number can cause issues. If you have 1,000 rows and one row has an extra space or character, it will not import correctly as a number custom field.

### Custom fields

When creating a new project via the CSV importer, custom fields are local, not global. To use these fields for reporting or future imports, convert them to [global custom fields](https://help.asana.com/s/article/custom-fields?language=en_US).

As a workaround, you can complete one import, convert your local fields to global custom fields and then [duplicate the project](https://help.asana.com/s/article/understanding-projects?language=en_US) without tasks or sections to retain only the global fields and then import the next CSV into that project. Ensure that the custom field options match exactly to avoid creating duplicate local custom fields.

### Multi-select values

To be detected as multiple options, multi-select values should have a comma (",") between them. If this is missed, all options are imported as a single block of text. This formatting needs to be done manually before importing.

## How to import a spreadsheet to Asana

There are three different opportunities to import data from a CSV file into Asana:

1.  When creating a new project from a team
2.  When using the Quick Add button
3.  When using the drop-down menu in an existing project.

> Importing data via CSV will not update any existing tasks in the project. The CSV importer can only add tasks to a project.

### Create a project for a team

1.  Navigate to the sidebar
2.  Click the arrow next to the team’s name
3.  Click **Create project**
4.  Select **Import spreadsheet**
5.  Select a CSV file to import
6.  Click **Make changes**
7.  Click **Continue to project**

### Using the quick add button

1.  Click the **Quick add** button
2.  Select **Project**
3.  Add your project details
4.  Click **Select file to import**
5.  Select a CSV file
6.  Click **Make changes**
7.  Click **Continue to project**

### Using the drop-down menu in an existing project** **

1.  Select the project header drop-down menu next to your project's name
2.  Hover over **Import**
3.  Choose **CSV**
4.  Select a CSV file to import
5.  Click **Make changes**
6.  Click **Continue to project**

### Previewing your project

After selecting your file to import, you can preview your project and make changes to it if necessary.

Always click **Make changes** before completing the import. This step allows you to review the data and correct any mistakes or change custom field types. If the desired custom field type is not available, it indicates a formatting issue in the CSV that needs fixing.

## Frequently asked questions

### What column order is required for CSV import into Asana?

The Task Name must be the first column, followed by Description, Sections, and Assignee, with other fields following in a specific order as outlined in the article.

### Are custom fields created during CSV import global or local?

Custom fields created via CSV import are local to the project, not global, and must be manually converted to global custom fields if you want to use them for reporting or future imports.

### How should collaborator email addresses be formatted in a CSV file?

Collaborator email addresses should be separated with a comma without any spaces between them in the Collaborators column.

### Can CSV import update existing tasks in an Asana project?

No, CSV import can only add new tasks to a project and cannot update any existing tasks.

> Looking for a better way to manage your work? Get started with a free Asana trial. [Try for free](https://asana.com/create-account "Try for free")
