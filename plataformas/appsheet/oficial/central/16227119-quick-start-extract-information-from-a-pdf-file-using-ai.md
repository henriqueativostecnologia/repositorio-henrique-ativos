---
fonte: https://support.google.com/appsheet/answer/16227119?hl=en
baixado: 2026-11-10
---

# Quick start: Extract information from a PDF file using AI

Imagine that you are on the Information Technology (IT) team for your company, Acme, and are responsible for tracking service requests made by employees to maintain the company's technology systems.

Using AI in automation, the process can be greatly simplified for the end user. Here’s what the experience could be for them:

1.  Receive a service ticket request as a PDF document.
2.  Upload the PDF document to your AppSheet app.

Using AI, AppSheet extracts data from the PDF file, such as title, ticket ID, description, and incident date.

Quick start flow for extracting information from a PDF

In this Quick start, you'll build an automation that uses AI to open a service ticket request. Specifically, you'll create an AppSheet database and use it to create an app, then build an automation using AI to extract information from a PDF file and open a service ticket that specifies a severity rating.

------------------------------------------------------------------------

To build an automation to extract information from a PDF file and open a service ticket request, do the following steps:

1.  [Create an AppSheet database](#create-database)
2.  [Create an app using the AppSheet database](#create-app)
3.  [Build an automation to extract information from a PDF file using AI](#build-automation)
4.  [Run the automation in the app preview](#test-automation)

## Step 1: Create an AppSheet database

First, you'll  create an AppSheet database and add the columns you need to store information about the service ticket request, such as title, ticket ID, description, incident date, and so on.

AppSheet apps are all about the data. Though it may be time consuming, carefully designing and setting up your data is a fundamental step in your app development. 

To create an AppSheet database, do the following:

1.  Sign in to [*AppSheet*](https://appsheet.com/)**.**
    The My Apps page is displayed.
2.  Select **Create \> Database \> New database**.
    A new AppSheet database is created and opened in the database editor
3.  Click within the name, **Untitled database**, and change the name of the database to: **Service request**

    Rename the database to Service request
4.  Change the name of the Table 1 table:
    1.  Position your cursor in the **Table 1** tab and select **More ******************************************************** \> Table settings**.

        Select More \> Table settings
    2.  Change the table name to: **Service request**
    3.  Leave all other fields set to the default values.
    4.  Click **Save**.
5.  Delete the dummy rows in the table, as follows:
    1.  Click in column 1 and drag the cursor to highlight all rows in the table. 

        Highlight dummy values in table
    2.  Right-click on the selected rows and select **Delete rows**.

        Select Delete rows when you right-click
        A confirmation dialog displays to confirm the delete operation.
    3.  Click **OK** to confirm the operation.
6.  Edit the column **Assignee** column by doing the following:
    1.   Position your cursor in the **Assignee** column header and select **More ******************************************************** \> Edit column**.
    2.  Change the **Name** field to **Ticket ID**.
    3.  Change the **Type** field to **Text**.
    4.  Click **Save**.

        Update column to Ticket IDF of type Text
7.  Add a new Description column, as follows:
    1.  Click **+ Add column** in the column header.

        Click Add column to add a new column to table
    2.  Change the **Name** field to **Description**.
    3.  Set the **Type** field to **LongText**.
    4.  Click **Save**.

        Add Description column and set as LongText type.
8.  Add a new Severity column, as follows:
    1.  Click **+ Add column** in the column header.
    2.  Change the **Name** field to **Severity**.
    3.  Set the **Type** field to **Enum**.
    4.  Set the **Item type** field to **Dropdown**.
    5.  Click in the first option field and enter **Low**.
    6.  Click **Add option**, enter **Medium**, and set the color to white. 
    7.  Click **Add option**, enter **High**, and set the color to white. 
    8.  Click **Save**.

        Severity enum
9.  Add a new Document column, as follows:
    1.  Click **+ Add column** in the column header.
    2.  Change the **Name** field to **Document**.
    3.  Set the **Type** field to **Attachments \>** **File**.
    4.  Click **Save**.

        Document file column

The columns in the AppSheet database appear as shown:

Service request table

Next, you'll create an app using the AppSheet database.

##  Step 2: Create an app using the AppSheet database

To create an app using the AppSheet database, do the following:

1.  In the top-right corner of the database editor, click **Apps**.

    Click Apps in the database editor to create an app

    The Apps using Service request pane displays. No apps are listed.
2.  Click **New AppSheet app**.
    The AppSheet app is created and opened in the app editor in a new tab.
3.  In the app editor, in the left navigation, click  to display the Data pane (if it isn't already displayed).

    Click Data to view the Data page in the editor

    The **Service request** table is displayed. Notice that the source is the Service request table in the AppSheet database that you created in the previous step.

    Service request table

Next, you'll build an automation to extract information from a PDF file using AI.

##  Step 3: Build an automation to extract information from a PDF file using AI

To build an automation to extract information from a PDF file using the Extract AI task , do the following:

1.   In the app editor, go to **Automation** Automation icon **.**

    Click automation in the left navigation pane

2.  Click **+** in the top header of the Bots pane.

    Click + to add a new bot

3.  In the Add a new bot dialog, click **Create a new bot**.

    Click Create a new bot

    A new empty bot is created and displayed in the center pane of the app editor.

4.  Edit the name of the bot.
    1.  Position your cursor over the New Bot in the left navigation pane.
    2.  Select **More ******** \> Rename**.

        Select Rename in the More menu to rename the bot
    3.  Rename the bot to **Track service request** and press **Enter**.

5.  In the new bot flow in the center pane, click **Configure event.**

    Click Configure event in the bot flow in the center pane

6.  For Event name, enter **Track service request **and click **Create a new event**.

    Enter Track service request for Event name and click Create a new event

    The Settings pane opens in the right side of the app editor.

7.  Configure the event by defining a condition to ensure that a document file is uploaded before triggering the automation. as follows:
    1.  Click in the **Condition** field.
        The Expression Assistant opens.
    2.  In the text box enter: `ISNOTBLANK([Document])`

        Type ISNOTBLANK(\[Document\]} in the Expression Assistant

        This expression ensures that `Document` column is not blank and contains a PDF file.
    3.  Click **Save**.
    4.  Leave all other settings set to the defaults.

8.  In the bot flow in the center pane, click **+ Add a step**.

    Click Add a step in the bot flow

9.  For Step name, enter **Extract from PDF** and click **Create a new step**.

    Enter Extract from PDF in Step name field and click Create a new step

    The Extract from PDF task is added and the configuration settings are displayed in the right pane.
    **Note**: You might need to select the task in the center pane to view the configuration settings.

10. Edit the task configuration settings in the right pane, as follows: 
    1.  Set the task type set to **AI task**.
    2.  Leave the **AI task** field set to **Extract**. This AI task type extracts information from a photo, file, or text.
    3.  Leave the **Input column** field set to **Document**. This is the `File` column used to upload a PDF file.
    4.  Under **Output**:
        1.  Select **Save to table** to save the extracted information to the AppSheet database.
        2.  Notice that the first column is added and set to **Title**. 
            Leave this column selection as is.
        3.  Click **Add** and select **Ticket ID** in the drop-down. (It should be selected by default.)
        4.  Click **Add** and select **Description** in the drop-down.
        5.  Click **Add** and select **Severity** in the drop-down.
        6.  Click **Add** and select **Status** in the drop-down.
        7.  Click **Add** and select **Date** in the drop-down.
    5.  In the **Additional instructions** field, enter:
         
        **Set the title to a short sentence from the description. Set the severity to "High" for serious incidents.**
        For best practices on setting the Additional instructions field, see [Best practices for using AI in automations](https://support.google.com/appsheet/answer/16052759).

        The Settings pane appears as follows:

        AI task settings

11. Click **Save** to save the app.

    ********Save the app********

Next, you'll test your automation using the app preview.

##  Step 4: Run the automation in the app preview

You can run the automation in the app preview located in the right pane.

When using app preview, any changes that you make are saved to your data source. We'll show you how to test a step in an automation without saving any changes later in this quick start.

To run the automation in the app preview, do the following:

1.  Before you proceed, download the [Acme Service Ticket Request - Example 1](https://drive.google.com/file/d/1l1nadhjcQcbSAhpYgcSGIfyMSbL-8qeM/view?usp=drive_link) PDF file to your local directory.
2.  At the top of the right pane, click Mobile app preview icon to display the mobile app preview.

    Click mobile in the app preview
3.  Turn off **Edit** in the app preview, if necessary. This will make it easier to interact with the app in the preview pane.

    Turn off Edit in app preview to make it easier to preview app
4.  Click **+** in the app preview.

    Click + in app to add a service ticket
5.  Scroll down and click in the **Document** field. 

6.  Navigate to the PDF file in your local drive, downloaded in step 1, and click **Open**.
7.  Click **Save**.

    The PDF file is uploaded. AppSheet syncs the app, as indicated by the sync notification:

    AppSheet sync indicator

    As AppSheet syncs the app, AI extracts information from the PDF file to populate the remaining fields. When the sync completes, the service request is added to the inventory.
8.  After the sync completes, click the service request in the list to view the details. 

    Click service ticket to view details

    Notice that the Title, Ticket ID, Status, Description, Date, and Severity fields have been auto-populated. The Title and Severity fields are set based on your additional instructions.

    Note that the fields have been auto-populated

------------------------------------------------------------------------

**Congratulations!** You have built an automation using AI to extract information from a PDF. 

**What's next?**

- Explore more Gemini-based [quick starts](https://support.google.com/appsheet/answer/16045284#quick-start) to learn about AI in automations.
- Explore other [quick starts](https://support.google.com/appsheet/answer/13474783) to learn about other AppSheet features.
