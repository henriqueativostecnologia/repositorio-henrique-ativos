---
fonte: https://support.google.com/appsheet/answer/16338286?hl=en
baixado: 2026-11-10
---

# Quick start: Categorize information using AI

In the [Quick start: Extract information from an image using AI,](https://support.google.com/appsheet/answer/15985259) you built an automation that updates the inventory at a car dealership by using AI to extract information from a car photo.

In this quick start, you'll extend the Update car inventory automation using AI to categorize the car by body style. This quick start also illustrates how to test a step in your automation.

------------------------------------------------------------------------

To update an automation to categorize the car by body style, do the following steps:

1.  [Complete the prerequisite quick start](#prerequisite)
2.  [Update the AppSheet database](#update-database)
3.  [Regenerate the table in the app](#regenerate-data-schema)
4.  [Add an automation step to categorize cars by body style using AI](#categorize)
5.  [Test the step in your automation](#test-step)

## Step 1: Complete the prerequisite quick start

As a prerequisite, you must complete [Quick start: Extract information from an image using AI](https://support.google.com/appsheet/answer/15985259).

## Step 2: Update the AppSheet database

Update the Car inventory AppSheet database, that you created in [Quick start: Extract information from an image using AI](https://support.google.com/appsheet/answer/15985259).

To update the AppSheet database, do the following:

1.  Open the Car inventory AppSheet database in the database editor, or navigate to its tab.
2.  In the AppSheet database editor, add a new body style column, as follows:
    1.  Click **+ Add column** in the column header.

        Click + Add column to dd column to AppSheet database
         
    2.  Change the **Name** field to **Body style**.
    3.  Set the **Type** field to **Enum**.
    4.  Set the **Item type** field to **Dropdown**.
    5.  Click in the first option field and enter **Sedan**.
    6.  Click **Add option**, enter **Coupe**, and set the color to white. 
    7.  Repeat step f to add the following options: **Hatchback**, **SUV**, **Pickup**, **Minivan**, **Other
        Note:** "Other" will be used to catch body styles that aren't in the list of options.
    8.  Click **Save**.

Next, you'll regenerate the app schema in the Car inventory app.

## Step 3: Regenerate the table in the app

Regenerate the Car inventory table in the Car inventory app, originally created in [Quick start: Extract information from an image using AI](https://support.google.com/appsheet/answer/15985259).

To regenerate the table in your app, do the following:

1.  Open the Car inventory app in the app editor, or navigate to its tab.
2.  In the app editor, in the left navigation, click  to display the Data pane (if it isn't already displayed).

    Click Data to open the Data pane

    Note that there is a warning message indicating that the app schema is out of sync with the data source. 

    Warning message for regenerate schema
     
3.  Click **Regenerate schema**  in the table header.

    Regenerate icon
     
4.  Click **Regenerate** to confirm the action.

AppSheet regenerates the Car inventory table to sync with the changes made to the AppSheet database and the warning message is removed. 

## Step 4: Add an automation step to categorize cars by body style using AI

To add a step to the automation to categorize cars by type using the Categorize AI task, do the following:

1.  In the app editor, go to **Automation** Automation icon ** **and select the **Update car inventory** bot.
2.  In the bot flow in the center pane, click **+ Add a step**.
3.  For Step name, enter **Categorize by body style** and click **Create a new step**.

    Add Categorize by body style step
4.  Edit the task configuration settings in the right pane, as follows: 
    1.  Set the task type to **AI task**.
    2.  In the **AI task** drop-down, select **Categorize**. This AI task type categorizes information.
    3.  Under **Input columns**:
        1.  Notice that the first column is added and set to **Make**. 
            Leave this column selection as is.
        2.  Click **Add** and select **Model** in the drop-down, if it's not already selected.
        3.  Click **Add** and select **Year** in the drop-down, if it's not already selected.
            **Note**: Don't select any other columns.

            The Input columns section appears as follows:

            Select Make, Model, and Year in the Input columns drop-down
    4.  Under **Output**:
        1.  Turn on **Save to table** (if it isn't already selected) to save the extracted information to the AppSheet database.
        2.  Click to open the drop-down and select **Body style**.
            Recall that Body style is an `Enum` column that defines the body styles that will be used to categorize the car.

            Turn on Save to table and keep Body style seelcted in the Output field  
    5.  In the **Additional instructions** field, enter: **If not sure of body style, set to "Other"**

        The Settings pane appears as follows:

        Categorize settings
5.   Click **Save** to save the app.

    ****************Save the app****************

## Step 5: Test the step in your automation

You can test a step in your automation--without updating any rows in your data source.

To test the step in your automation, do the following:

1.  Click  Test step icon  at the top of the right pane.

    Test icon in right pane of automation

    The Test step pane is displayed.
    **Note**: If you are prompted to refresh the data, click **Refresh**.

    The first (and only) row of app data is selected for the test input. 
    **Note**: If you had multiple rows of app data, you might click **Select row** to select a different row to test. 
2.  Click **Run test** at the bottom of the right pane to test the current row of data.

The Results section is updated to reflect the body style of the car.

Test step results showing Body style set to Pickup

------------------------------------------------------------------------

**Congratulations!** You have built an automation to categorize information using AI. 

**What's next?**

- Explore more Gemini-based [quick starts](https://support.google.com/appsheet/answer/16045284#quick-start) to learn about AI in automations.
- Explore other [quick starts](https://support.google.com/appsheet/answer/13474783) to learn about other AppSheet features.
