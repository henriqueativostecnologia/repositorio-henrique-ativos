---
fonte: https://support.google.com/appsheet/answer/14009539?hl=en
baixado: 2026-11-10
---

# Quick start: Create your first app by using an AppSheet database

In this Quick Start, you'll learn how to create an AppSheet app by using an AppSheet database.

An AppSheet database provides an easy and efficient way to build data models for any AppSheet app without needing to use an external data source solution such as cloud-based spreadsheets or databases. See [What is an AppSheet database?](https://support.google.com/appsheet/answer/12631542)

After completing this quick start tutorial, you'll have a better understanding of how to do the following:

- Create and customize a new AppSheet database by using existing data in a Google Sheet.
- Create an AppSheet app by using an AppSheet database.
- Customize the app by adding a table and a configuring a view to display the data.
- Regenerate the app when changes are made to the connected data source.

------------------------------------------------------------------------

To create your first app from an AppSheet database, perform the following steps:

1.  [Create an AppSheet database by importing a Sheet](#create-database).
2.  [Add a reference between tables](#add-reference).
3.  [Change the label column of the referenced table](#change-label).
4.  [Create an app by using the AppSheet database](#create-app).
5.  [Add a table to the app](#add-table).
6.  [Add a view to display the new table data](#add-view).
7.  [Preview your app](#preview).
8.  [Update the database and regenerate your app](#update-regenerate).

## Create an AppSheet database by importing a Sheet

To create an AppSheet database by importing a Sheet, perform the following steps.

1.  Make a copy of this public [*Google Sheet*](https://docs.google.com/spreadsheets/d/1zhdhmVLkCIhKlpJleuKvxdP4ok1KcXMhzYEUwH_yKrQ/edit?usp=sharing) and rename it as **My Project Tracker**.
    Notice that it has two tables, `Tasks` and `Owners`. For more information about copying a Google Sheet, see [Create, view, or download a file](https://support.google.com/docs/answer/49114).
2.  Sign in to [AppSheet](https://appsheet.com).
3.  Select **Create \> Database \> Import from Sheets**.

    Create an AppSheet database by importing from Sheets
4.  Navigate to and select the Sheet that you copied in step 1.

    After selecting the Sheet, a new AppSheet database is created by importing data from the Sheet and opened in the database editor. Its name defaults to the name of the Sheet from which it was copied (My Project Tracker). 
    If you have pop-ups blocked in your browser settings, the new AppSheet database might not be opened in the database editor after it is created. In this case, you'll need to click **Databases** in the top navigation and then click **My Project Tracker** to open it in the database editor.

    Open My Project Tracker database

    As shown in the following figure, both of the tables, `Tasks` and `Owners`, were imported and appear as *tabs* in the AppSheet database editor. Select a table's tab to view and manage its column and row data, and create an app.

    AppSheet database is created by importing data from the Google Sheet

If this is the first time you are accessing the AppSheet database editor, you might see one of the following dialogs:

- Welcome to AppSheet databases dialog. Click **Get started** to close the dialog.
- Dialog to step through a tour. Click **Start tour** to navigate through the tour or **Skip** to skip it.

Welcome tour dialog

## Add a reference between tables

Next, you'll add a reference to the `Owners` table from the `Tasks` table. This reference allows you to display owner information from the `Owners` table in a field in the `Tasks` table.

To add a reference between tables, perform the following steps:

1.  In the **Tasks** table in the AppSheet database, double-click the **Owner** column to edit its settings.
2.  In the **Text** field, select **Link to table \> Reference**.

    Change Owners column type to Reference
3.  Select **Owners** in the **Table to reference** list.

    Select Owners in the Table to reference field
4.  Click **Save**.
    A warning appears about changing the column type. In this example, the data in this column is compatible with the new column type so it's fine to proceed.
5.  Click **Yes**.
    Note the reference icon  now appears in the `Owner` column header.

    The AppSheet database processes the reference and attempts to match the corresponding rows in the `Owners` table with the names in the `Tasks` table. Since the data in the `Owners` table matches, the AppSheet database populates the `Owner` column with the correct references to the `Owners` rows.
6.  To test the reference, double-click a cell  in the **Owner** column and change it to another owner, such as **Sarah**. The contents of the drop-down is populated with owner information from the `Owners` table.

    Change owner by selecting from referenced list

## Change the label column of the referenced table

You can select a *label* column for any table in an AppSheet database. The label column allows you to specify which column you wish to appear in the referenced table. As shown in the following figure, instead of displaying the **`Name`** column from the `Owners` table in the `Tasks` table, you could display the **`Email`** column by setting the Email column as the label. 

Owner with Name column as label versus Owner with Email column as label

To change the label column of the referenced table:

1.  Click the **Owners** tab to display the table.

    Select Owners tab
2.  in the **Email** column header, select More ** \> Use column as label**.

    Use column as label

To confirm the current label column is `Email`:

- Note the label icon  appears in the `Email` column header.

  Label icon in Email column header
- In the `Tasks` table note that the `Owner` column now displays the owner's email instead of their name.

## Create an app by using the AppSheet database

After you've completed the AppSheet database customizations, create an AppSheet app by using the database by performing the following steps:

1.  Click **Apps** in the top right corner of the database editor.

    Show apps in the database editor

    The Apps using Tasks pane displays.

2.  Click **New AppSheet app**.

    Create a new AppSheet app using the database

    A new app is created using the selected table and opened in the AppSheet app editor. By default, the app is named using the table name: **Tasks App** 

    The following figure shows the app editor and its layout.

    AppSheet app editor showing navigate, learn and customize, and preview app
     

    As shown in the previous figure, the app editor includes three main areas that enable you to:

    - Navigate the app editor to select the section you want to customize.
    - Based on the section selected in the navigation bar, access the learning center (shown) and customize your app to change the styles, control how your data is presented or navigated, configure security requirements, and more.
    - Preview your **live** app to interact with and make changes. 

    You can also quickly track down warnings or errors in your app.

3.  Click  Warning icon  in the tools panel.

    Tools panel showing warning icon

    The **Errors & Warnings** dialog displays.

    Errors and warning dialog

    This warning is displayed because the `Tasks` table has a reference to the `Owners` table, which hasn't been added to the app. 

4.  Click **Go to problem** in the Errors & Warnings dialog.
    AppSheet navigates to the Data page, as shown in the following figure.

    Data pane also showing warning

    Notice that the warning message is repeated, in context, and the `Owner` column is highlighted in the table. You'll add the `Owners` table in the next step, to resolve this issue.

## Add a table to the app

To address the warning message in the UI, you'll add the `Owners` table to the app.

1.  In the top header of the Data navigation pane, click **+**.

    Click + to add data

    The Add data dialog displays. 
2.  In the Add data dialog, click **AppSheet Database**.

    Select AppSheet Database in the Add data dialog
3.  In the Select database dialog, select **My Project Tracker**. 

    Select database

    Note that the **Connected** flag indicates that this data source is already in use by the app. 
4.  In the My Project Tracker dialog, make sure that the **Owners** table is selected in the list with **Update, Add, Delete** permissions (it should be selected by default) and click **Add to app **to add the `Owners` table to your app.

    Add the Owners table to your app
5.  Click the **Owners** table in the Data navigation pane.

    Click Owners table
6.  Notice that there is a warning message that indicates that the `Email` column might contain personally identifiable information. This informational warning message is temporary and can be ignored.
    **Table 'Owners' may contain sensitive data in column(s): Email**

    In this case, AppSheet automatically turns on its **PII** setting for the `Email` column, which will prevent the information from being retained in the system logs. (To view the PII setting, you might need to scroll the configuration content in the center pane to the right.)

    PII setting in table configuration

## Add a view to display the new table data

Now that the `Owners` table has been added, you can create a view to display its data. You can choose from several different views types to display your data. In this case, you'll use a deck view to show information for each row in a "deck-of-cards" format.

1.  Select **Apps ** App icon **\> Views **in the navigation bar.

    Show views for the app

    The Views page is displayed.

2.  In the Data navigation pane, click **+** next to **Primary Navigation.**

    Add a view to primary navigation

    The Add a new view dialog is displayed.

3.  Click **Create a new view**.

    Add a new view dialog

    A **New View** is created as shown in the following figure.

    New view

4.  Edit the New View, as follows:

    - Change the **View name** field to **Owners.**
    - In the **For this data** drop-down, select **Owners.**
    - For **View type**, click **deck.**

    The updates are shown in the following figure. Owners view with updates

     

    You might notice that the app preview, in the right pane, is updating as you make changes. You'll preview your changes in the next step. 

5.  In the top level toolbar, click **Save** to save the changes to your app.

    Save app
     
    Remember to save your app anytime you make changes!

You'll preview the app in the next step.

## Preview the app

The app preview that is located in the right pane of the AppSheet app editor allows you to view and interact with your **live** app.

Any changes that you make in the app preview are saved to the data source, in this case the My Project Tracker AppSheet database. 

The following figure shows the various actions you can take in the app preview.

App preview with callouts

As highlighted in the figure, using app preview you can do the following:

- Turn on the **Edit** toggle to [use the visual editing tools](https://support.google.com/appsheet/answer/13684531#visual-editing) while previewing the live app. Turn off the **Edit** toggle to preview the live app without showing the visual editing tools.
- Preview the live app in **mobile**, **tablet**, or **desktop** format.
- Set the email to use when previewing the live app. See also [Test apps](https://support.google.com/appsheet/answer/11998579).
- Access the view or table currently displayed. 

While previewing the app, you might want to turn off the **Edit** toggle.

To interact with your live app, you might click the row for Tom to view the list of tasks and corresponding status and due date. 

App preview details

Then, click **Tasks** in the primary navigation bar (shown for mobile devices in the following figure) to display tasks organized by their status.

App preview tasks

You can continue to explore the app preview on your own.

## Update the database and regenerate your app

In the following steps, you'll learn how to regenerate the AppSheet app when changes are made to the connected data source.

1.  Return to the browser tab that shows the **AppSheet database editor**. 

2.  In the **Due Date** column header, click **More**  Three-dot menu vertical **\> Edit column**.
    Alternatively, you can double-click the **Due Date** header.

3.  In the **Type** drop-down, select **Date and Time \> Date**.

    Select Date and time \> Date

4.  Click **Save**.
    The following confirmation is displayed:

    Change column type confirmation

5.  Click **Yes** to proceed.
    After a few moments, the column values are updated to `Date` column types.

6.  Return to the browser tab that shows the **AppSheet app editor**.

7.  Select **Data ** in the navigation bar, and then select the **Tasks** table.

    Select Tasks table

    Notice the following warning message is displayed:
    **App Schema for table 'Tasks' is out of sync with the schema in AppSheet database. Please regenerate the table structure.**

8.  In the **Tables** toolbar in the center pane, click .

    Regenerate icon

    A confirmation dialog displays.

9.  Click **Regenerate** in the confirmation dialog to confirm the action.

10. Notice that the **Due Date** column type has changed to **Date** in the `Tasks` table.

    Due Date is changed to Date column type

------------------------------------------------------------------------

**Congratulations!** You have created your first AppSheet app by using an AppSheet database, and learned how to customize your app and regenerate it when changes are made to the connected data source. 

**What's next?** You can access more [quick starts](https://support.google.com/appsheet/answer/13474783) to learn about other AppSheet features.
