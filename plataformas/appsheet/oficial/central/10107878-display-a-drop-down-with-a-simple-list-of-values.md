---
fonte: https://support.google.com/appsheet/answer/10107878?hl=en
baixado: 2026-11-10
---

# Display a drop-down with a simple list of values

Display a drop-down with a simple list of values for columns of the following type:

|                 |                                                                           |
|-----------------|---------------------------------------------------------------------------|
| **Column type** | **Description**                                                           |
| `Enum`          | Users can select **one** value from the list of allowed values.           |
| `EnumList`      | Users can select **zero or more values** from the list of allowed values. |

The following sections describe how to [configure the drop-down](#configure) and [explore a sample app](#explore-template-app) that demonstrates the use of the drop-downs in an app.

## Configure the drop-down

To configure the drop-down:

1.  Open the app in the editor.

2.  Go to **Data**  and select the table to which you want to add barcode scanning in the Data panel.
    We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
    You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

     
    ## If you are using the legacy editor

    Go to **Data**, click **Columns**, and expand the table to which you want to add barcode scanning.

3.  Click the **edit (pencil) icon** to the left of the column name you wish to make a drop-down list.

4.  Enable the **Show?** toggle to show the information in the app.

5.  Select **Enum** or **EnumList** in the **Type** field to configure a single or multiple selection drop-down, respectively.

6.  In the **Values** field, click **Add** to add the list of values.

7.  Consider enabling the following options:

    - **Allow other values** - enables users to enter other values in addition to the allowed values displayed in the drop-down list.

    - **Auto-complete other values** - auto-completes previously entered values to encourage consistency and minimize typos.

8.  For **Input mode**, click **Dropdown** to format the list as a drop-down.

9.  Configure other column properties, as required. See [*Configure column properties*](https://support.google.com/appsheet/answer/10106509).

10. Click **Done**.

## Explore a sample app

The [*Enum versus EnumList*](https://www.appsheet.com/template/showdef?appId=EnumvsEnumList-71626) sample app demonstrates how to build the following drop-downs from a simple list of values:

- Select **one** type of fruit from a list (using an `Enum`)
- Select **multiple** types of fruit from a list (using an `EnumList`)

The following illustrates how the drop-downs appear in the app.

If you look at the column configuration for each drop-down shown above, you'll notice that the only difference between them is the **Type** setting, **Enum** versus **EnumList**. 

The following table summarizes the column configuration settings for each drop-down for quick reference.

|                            |                             |                            |
|----------------------------|-----------------------------|----------------------------|
| **Property**               | **Single-select drop-down** | **Multi-select drop-down** |
| Column name                | Enum                        | EnumList                   |
| Show?                      | Enabled                     | Enabled                    |
| Type                       | **Enum**                    | **EnumList**               |
| Values                     | Apple, Banana, and Orange   | Apple, Banana, and Orange  |
| All other values           | Disabled                    | Disabled                   |
| Auto-complete other values | Enabled                     | Enabled                    |
| Base type                  | Text                        | Text                       |
| Input mode                 | Dropdown                    | Dropdown                   |

For a description of each configuration property, see [*Configure column properties*](https://support.google.com/appsheet/answer/10106509).

See also: [Drop-downs](https://www.appsheet.com/Template/AppDef?appName=Dropdowns-71626&appId=Dropdowns-71626#Data.Columns.Dropdowns_Schema) sample app
