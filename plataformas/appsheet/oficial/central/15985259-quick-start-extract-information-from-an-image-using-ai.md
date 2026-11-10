---
fonte: https://support.google.com/appsheet/answer/15985259?hl=en
baixado: 2026-11-10
---

# Quick start: Extract information from an image using AI

Imagine you are the owner of a car dealership and you need to frequently update your sales inventory. Using AI in automation, the process can be greatly simplified for the end user. Here’s what the experience could be for them:

1.  Take a photo of the new car on a mobile device.
2.  Upload the image to your AppSheet app.

Using AI, AppSheet extracts data from the photo, such as car make, model, color, and year.

Take a photo, upload it to the AppSheet app, and AppSheet extracts information using AI

In this Quick start, you'll build an automation that uses AI to update the inventory at a car dealership. Specifically, you'll create an AppSheet database and use it to create an app, then build an automation using AI to extract information from a car photo and categorize the car by body style.

See also the [Car identification with Gemini](https://www.appsheet.com//template/showdef?appId=CarIdentificationwithGemini-2078346&quickStart=False)sample app which demonstrates a more comprehensive scenario. 

------------------------------------------------------------------------

To build an automation to extract information from a car photo and categorize the car by body style, do the following steps:

1.  [Create an AppSheet database](#create-database)
2.  [Create an app using the AppSheet database](#create-app)
3.  [Build an automation to extract information from a photo using AI](#build-automation)
4.  [Customize the input form](#customize-input-form)
5.  [Run the automation in the app preview](#test-automation)

## Step 1: Create an AppSheet database

First, you'll  create an AppSheet database and add the columns you need to store information about the car, such as make, model, year, description, and so on, and an `Image` column that will be used to upload a photo of the car.

AppSheet apps are all about the data. Though it may be time consuming, carefully designing and setting up your data is a fundamental step in your app development. 

To create an AppSheet database, do the following:

1.  Sign in to [*AppSheet*](https://appsheet.com/)**.**
    The My Apps page is displayed.

2.  Select **Create \> Database \> New database**.
    A new AppSheet database is created and opened in the database editor

3.  Click within the name, **Untitled database**, and change the name of the database to: **Car inventory**

    Change AppSheet databse name to Car inventory

4.  Change the name of the Table 1 table:
    1.  Position your cursor in the **Table 1** tab and select **More ************************ \> Table settings**.

        Select More \> Table settings
    2.  Change the table name to: **Car inventory**

        Table settings with name changed to Car inventory
    3.  Leave all other fields set to the default values.
    4.  Click **Save**.

5.  Delete the dummy rows in the table, as follows:
    1.  Click in column 1 and drag the cursor to highlight all rows in the table. 

        Highlight dummy values in table
    2.  Right-click on the selected rows and select **Delete rows**.

        Select Delete rows when you right-click
        A confirmation dialog displays to confirm the delete operation.
    3.  Click **OK** to confirm the operation.

6.  Edit the columns in the table as indicated in the following table:

    +-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Edit column**                                                               | **Steps**                                                                     |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Change **Title** to **Make**                                                  | Do the following:                                                             |
|                                                                               |                                                                               |
|                                                                               | 1.  Position your cursor in the **Title** column header and select **More  \> |
|                                                                               |     Edit column**                                                             |
|                                                                               |                                                                               |
|                                                                               |     Edit name of column in AppSheet database                                  |
|                                                                               |                                                                               |
|                                                                               | 2.  Change the **Name** field to **Make** and click **Save**.                 |
|                                                                               |                                                                               |
|                                                                               |     Change Name to Make and click Save                                        |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Change **Assignee** to **Model**                                              | Do the following:                                                             |
|                                                                               |                                                                               |
|                                                                               | 1.  Position your cursor in the **Assignee** column header and select         |
|                                                                               |     **More ******** \> Edit column**.                                         |
|                                                                               |                                                                               |
|                                                                               | 2.  Change the **Name** field to **Model**.                                   |
|                                                                               |                                                                               |
|                                                                               | 3.  Key the **Type** field set to **Name**.\                                  |
|                                                                               |     This indicates that the content is a proper name. Alternatively, you      |
|                                                                               |     could set this to Text.                                                   |
|                                                                               |                                                                               |
|                                                                               | 4.  Click **Save**.                                                           |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Change **Status** to **Color**                                                | Do the following:                                                             |
|                                                                               |                                                                               |
|                                                                               | 1.  In the **Status** column header, select **More ******** \> Edit column**. |
|                                                                               | 2.  Change the **Name** field to **Color**.                                   |
|                                                                               | 3.  Leave the **Type** field set to **Enum** and the **Item type** field set  |
|                                                                               |     to **Dropdown**.                                                          |
|                                                                               | 4.  Edit the three Enum options as follows:                                   |
|                                                                               |     1.  Double-click in the **Not started** option field and change the       |
|                                                                               |         name to **White**.                                                    |
|                                                                               |     2.  Double-click in the **In Progress** option field and change the       |
|                                                                               |         name to **Green**. Then, click the color setting to the left of the   |
|                                                                               |         name and choose the green color block.\                               |
|                                                                               |         \                                                                     |
|                                                                               |         Add another color option. Enter green and select green as the color.  |
|                                                                               |     3.  Double-click in the **Complete** option field and change the name to  |
|                                                                               |         **Yellow**. Then, click the color setting to the left of the name and |
|                                                                               |         choose the yellow color block.                                        |
|                                                                               | 5.  Add more Enum color options, as required, and an Other option to account  |
|                                                                               |     for colors that aren't defined:                                           |
|                                                                               |     1.  Click **Add option** and enter **Orange. **\                          |
|                                                                               |         The color setting should be set to orange automatically. If it's not, |
|                                                                               |         then, click the color setting to the left of the name and choose the  |
|                                                                               |         orange color block.                                                   |
|                                                                               |     2.  Click **Add option** and enter **Red. **\                             |
|                                                                               |         The color setting should be set to red automatically. If it's not,    |
|                                                                               |         then, click the color setting to the left of the name and choose the  |
|                                                                               |         red color block.                                                      |
|                                                                               |     3.  Click **Add option** and enter **Blue. **Then, click the color        |
|                                                                               |         setting to the left of the name and choose the blue color block.      |
|                                                                               |     4.  Click **Add option** and enter **Silver. **Then, click the color      |
|                                                                               |         setting to the left of the name and choose the silver (or grey) color |
|                                                                               |         block.                                                                |
|                                                                               |     5.  Click **Add option** and enter **Black**.** **Then, click the color   |
|                                                                               |         setting to the left of the name and set the color to black by         |
|                                                                               |         clicking **Set custom color**, in the **Hex** field                   |
|                                                                               |         entering **#000000**, and clicking **Select**. \                      |
|                                                                               |         \                                                                     |
|                                                                               |     6.  Click **Add option**, enter **Other**. Then, click the color setting  |
|                                                                               |         to the left of the name and choose the white color block.             |
|                                                                               |         **Note:** "Other" will be used to catch colors that aren't defined in |
|                                                                               |         the list of options. You could then update the Enum options later to  |
|                                                                               |         include any colors that were set to Other.                            |
|                                                                               |                                                                               |
|                                                                               |         The Color Enum settings appear as follows:\                           |
|                                                                               |     7.  Click **Save**.                                                       |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Change **Date** to **Year**                                                   | Do the following:                                                             |
|                                                                               |                                                                               |
|                                                                               | 1.  In the **Date** column header, select **More ******** \> Edit column**.   |
|                                                                               | 2.  Change the **Name** field to **Year**.                                    |
|                                                                               | 3.  Change the **Type** field to **Number**.                                  |
|                                                                               | 4.  Click **Save**.\                                                          |
|                                                                               |     **Note**: When prompted, click **Yes** to confirm the column type change. |
|                                                                               |     The information doesn't apply in this case since there's no data in the   |
|                                                                               |     table.                                                                    |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

7.  Add a new Description column, as follows:
    1.  Click **+ Add column** in the column header.
    2.  Change the **Name** field to **Description**.
    3.  Set the **Type** field to **Text**.
    4.  Click **Save**.

        Add Description column

8.  Add a new Image column, as follows:
    1.  Click **+ Add column** in the column header.
    2.  Change the **Name** field to **Car photo**.
    3.  Set the **Type** field to **Attachments \>** **Image**.
    4.  Click **Save**.

        Add Image column named Car photo

The columns in the AppSheet database appear as shown:

AppSheet database named Car inventory with columns including Make, Model, Color, Year, and Car photo

Next, you'll create an app using the AppSheet database.

## Step 2: Create an app using the AppSheet database

To create an app using the AppSheet database, do the following:

1.  In the top-right corner of the database editor, click **Apps**.

    Click Apps in the database editor to create an app

    The Apps using Car inventory pane displays. No apps are listed.
2.  Click **New AppSheet app**.
    The AppSheet app is created and opened in the app editor in a new tab.
3.  In the app editor, in the left navigation, click  to display the Data pane (if it isn't already displayed).

    Click Data button in the left navigation bar

    The **Car inventory** table is displayed. Notice that the source is the Car inventory table in the AppSheet database that you created in the previous step.

    The Data page of the app in the app editor
4.  To change the name of the app, click in the app name field in the top left corner of the app editor and change the name to **Car inventory**.

    Rename the app to Car inventory
5.  To edit the Year column properties, click **Edit**  adjacent to the **Year** column.

    Click the pencil icon to edit the Year column properties
6.  Turn off **Show thousands separator **-- since this value will depict the year the car was built which doesn't require a separator.

    Turn off Show thousands separator in the Year column properties
7.  Click **Done**.

Next, you'll build an automation to extract information from a photo using AI.

## Step 3: Build an automation to extract information from a photo using AI

To build an automation to extract information from a photo of a car using the Extract AI task , do the following:

1.   In the app editor, go to **Automation** Automation icon **.**

    Click automation in the left navigation pane

2.  Click **+** in the top header of the Bots pane.

    Click + to add a new bot

3.  In the Add a new bot dialog, click **Create a new bot**.

    Click Create a new bot in the Add a new bot dialog

    A new empty bot is created and displayed in the center pane of the app editor.

4.  Edit the name of the bot.
    1.  Position your cursor over the New Bot in the left navigation pane.
    2.  Select **More  \> Rename**.

        Select Rename in the More menu to rename the bot
    3.  Rename the bot to **Update car inventory** and press **Enter**.

5.  In the new bot flow in the center pane, click **Configure event.**

    Click Configure event in the bot flow in the center pane

6.  For Event name, enter **Update car inventory** and click **Create a new event**.

    The Settings pane opens in the right side of the app editor.

7.  Configure the event by defining a condition to ensure that a car photo is uploaded before triggering the automation. as follows:
    1.  Click in the **Condition** field.
        The Expression Assistant opens.
    2.  In the text box enter: `ISNOTBLANK([Car photo])`

        Expression Assistant with ISNOTBLANK() expression

        This expression ensures that `Car photo` column is not blank and contains a photo of the car.
    3.  Click **Save**.
    4.  Leave all other settings set to the defaults.

        The Settings pane appears as follows:

        Event settings

8.  In the bot flow in the center pane, click **+ Add a step**.

    Click Add a step in the bot flow

9.  For Step name, enter **Extract from photo** and click **Create a new step**.

    Set step name to Extract from photo and click Create a new step

    The Extract from photo task is added and the configuration settings are displayed in the right pane.
     
    You might need to select the task in the center pane to view the configuration settings.

10. Edit the task configuration settings in the right pane, as follows: 
    1.  Set the task type set to **AI task**.
    2.  Leave the **AI task** field set to **Extract**. This AI task type extracts information from a photo, PDF, or text.
    3.  Leave the **Input column** field set to **Car photo**. This is the `Image` column that is used to upload a car photo.
    4.  Under **Output**:
        1.  Select **Save to table** to save the extracted information to the AppSheet database.
        2.  Notice that the first column is added and set to **Make**. 
            Leave this column selection as is.
        3.  Click **Add** and select **Model** in the drop-down, if it's not already selected.
        4.  Click **Add** and select **Color** in the drop-down, if it's not already selected.
        5.  Click **Add** and select **Year** in the drop-down, if it's not already selected.
        6.  Click **Add** and select **Description** in the drop-down, if it's not already selected.

            The Output section appears as follows:

            Turn on Save to tabl, and select all columns and click Select 4 columns
    5.  In the **Additional instructions** field, enter:
         
        **If not sure of Make, Model, or Year, make best guess
        If not sure of Color, set to "Other"**
        **For** **Description, add 2 to 3 sentences**

        The Settings pane appears as follows:

        Settings pane for Extract AI task

11. Click **Save** to save the app.

    ****Save the app****

Next, you'll customize the input form that is used by app users to upload a car photo.

## Step 4: Customize the input form

When you created your app, AppSheet auto-generated two views--a form view to add a new car to the inventory and a detail view to view the car details. In this step, you'll edit the form view to customize the fields that display in the input form that is used by app users to upload a car photo. 

To customize the input form, do the following:

1.  Go to **App ** App icon **\> Views**.

    Select App \> Views
2.  In the left navigation pane, under the **System-Generated** views click **Car inventory_Form** to open its configuration in the center pane. 

    Select Car inventory_Form in the nav pane
3.  In the center pane, in the Column order field select **Manual**. 

    Select Manual for Column order
4.  In the column order list, select all columns except Car photo and click **Remove.**

    Select all but Car photo in the columns list and click Remove

Notice that the input form is updated in the app preview to only show the Car photo field.

Updated input form in app preview

Next, you'll run automation in the app preview.

## Step 5: Run the automation in the app preview

When using the app preview, any changes that you make are saved to your data source. 

To run the automation in the app preview, do the following:

1.  Before you proceed, you'll need a photo of a car. Take a photo of your own car or download one from the internet.
2.  In the app preview, Click in the **Car photo** field.

    Click in the Car photo field to upload a photo
3.  Navigate to the car photo in you local drive and click **Open**.
4.  Click **Save**.

    Upload car photo and click Save

    The car photo image is uploaded. AppSheet syncs the app, as indicated by the sync notification:

    AppSheet sync indicator

    As AppSheet syncs the app, AI extracts information from the photo to populate the remaining fields. When the sync completes, the car is added to the inventory.
5.  Click **Car inventory** to navigate to the car inventory list.
6.  After the sync completes, click the new car item in the list to view the details. 

    Click to view car details

    Notice that the Make, Model, Color, Year, and Description fields have been auto-populated .

    Car details with auto-populated fields

------------------------------------------------------------------------

**Congratulations! **You have built an automation using AI to extract information from an image. 

**What's next? **

- Extend this automation to categorize the car by body style. See [Quick start: Categorize information using AI](https://support.google.com/appsheet/answer/16338286).  
- Explore more Gemini-based [quick starts](https://support.google.com/appsheet/answer/16045284#quick-start) to learn about AI in automations.
- Explore other [quick starts](https://support.google.com/appsheet/answer/13474783) to learn about other AppSheet features.
