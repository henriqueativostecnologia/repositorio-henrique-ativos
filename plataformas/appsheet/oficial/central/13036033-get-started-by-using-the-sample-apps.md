---
fonte: https://support.google.com/appsheet/answer/13036033?hl=en
baixado: 2026-11-10
---

# Get started by using the sample apps

Get started with AppSheet by using the sample apps that demonstrate common use cases. The sample apps are summarized in the following table. 

See also the product [App templates](https://www.appsheet.com/templates).

To use a sample app, click its link to open it in the AppSheet editor (in a new tab). Then, do one of the following:

- View and interact with the app to learn more about the sample use case and its implementation. (The sample app is read-only.)
- [Copy the app](https://support.google.com/appsheet/answer/12491039) to use it as a an initial starting point for your own app.

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Sample app**                                                                | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Activity                                                                     | Track a student's extracurricular activities.                                 |
| schedule](h                                                                   |                                                                               |
| ttps://www.appsheet.com/template/showdef?appId=ExtracurricularSchedule-71626) | Students use the app to track schedules as well as important notes for each   |
|                                                                               | individual activity.                                                          |
|                                                                               |                                                                               |
|                                                                               | Note the following about the sample app:                                      |
|                                                                               |                                                                               |
|                                                                               | -   The app uses two worksheets within one workbook: a table for `Activity`   |
|                                                                               |     and a table for `Notes`. See [How to use multiple sheets in your          |
|                                                                               |     app](https://support.google.com/appsheet/answer/10106507).                |
|                                                                               |                                                                               |
|                                                                               | -   The tables each have a `_ComputedKey` row of type                         |
|                                                                               |                                                                               |
|                                                                               | [`MultiColumnKey`](https://support.google.com/appsheet/answer/10106435#other) |
|                                                                               |     that combines `Activity` and `Day` for the `Activity` table and           |
|                                                                               |     `Activity` and `Date` for the `Notes` table using the                     |
|                                                                               |     [`CONCATENATE()`](https://support.google.com/appsheet/answer/10107400)    |
|                                                                               |     function. The combined values of each of the columns form a unique key    |
|                                                                               |     AppSheet can use to uniquely identify each row. In the `Notes` worksheet, |
|                                                                               |     notice that each activity is listed with a day next to it.                |
|                                                                               |                                                                               |
|                                                                               | -   The `Notes` table defines a                                               |
|                                                                               |     [`Ref`](https://support.google.com/appsheet/answer/10106510) column,      |
|                                                                               |     `Activity`, that is a reference to the `Activity` table. When the user    |
|                                                                               |     adds a note to an activity, the drop-down displays the `_ComputedKey`     |
|                                                                               |     values that combine `Activity: Day`. For example:                         |
|                                                                               |     `Swim Practice: Monday` and `Swim Practice: Friday`. So it's quick and    |
|                                                                               |     easy to reference which activity on which day you want to write a note    |
|                                                                               |     for.                                                                      |
|                                                                               |                                                                               |
|                                                                               | -   The Notes [reference                                                      |
|                                                                               |     view](https://support.google.com/appsheet/answer/10106516) and its        |
|                                                                               |     associated system-generated views (Notes_Detail, Notes_Form, and          |
|                                                                               |     Notes_Inline) enable users to view or add notes to a student's activity   |
|                                                                               |     details.\                                                                 |
|                                                                               |     \                                                                         |
|                                                                               |     Notes reference view displayed in activity details                        |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Add multiple                                                                 | Add multiple photos to a single row.                                          |
| photos](https://www.appsheet.com/template/showdef?appId=PhotoGallery-71626)   |                                                                               |
|                                                                               | In the `Animal` table, each animal has multiple animal photos.To support      |
|                                                                               | this, there is a table called `Animal Photo` that has a                       |
|                                                                               | [reference](https://support.google.com/appsheet/answer/10106510) to the       |
|                                                                               | `Animal` table. The `Ref` column has **Is a part of?** turned on, so that     |
|                                                                               | when adding a new animal, a nested form is displayed to enable users to add   |
|                                                                               | multiple photos.                                                              |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [At most one value                                                            | Prevent setting more than one status value to `Yes`.                          |
| tr                                                                            |                                                                               |
| ue](https://www.appsheet.com/template/showdef?appId=AtMostOneValueTrue-71626) | The sample app has a column called `Status` of type `Yes/No`. The             |
|                                                                               | following [Valid if](https://support.google.com/appsheet/answer/10107949)     |
|                                                                               | expression is applied to this column so that at most one row in the table can |
|                                                                               | have `Status` set to `Yes`:                                                   |
|                                                                               |                                                                               |
|                                                                               | `OR(`\                                                                        |
|                                                                               | `    [Status] = FALSE,`\                                                      |
|                                                                               | `    COUNT(`\                                                                 |
|                                                                               | `        FILTER(`\                                                            |
|                                                                               | `            "Data",`\                                                        |
|                                                                               | `            AND(`\                                                           |
|                                                                               | `                [Key] <> [_THISROW],`\                                       |
|                                                                               | `                [Status] = TRUE`\                                            |
|                                                                               | `            )`\                                                              |
|                                                                               | `        )`\                                                                  |
|                                                                               | `    ) = 0`\                                                                  |
|                                                                               | `)`                                                                           |
|                                                                               |                                                                               |
|                                                                               | If the current row's status is set to `No`, then the row is always valid      |
|                                                                               | (since there is no restriction on the status `No`). If the current row's      |
|                                                                               | status is set to `Yes`, then the row is  valid only if there are 0 other rows |
|                                                                               | whose status is `Yes` as calculated by the                                    |
|                                                                               | [`COUNT()`](https://support.google.com/appsheet/answer/10107676) expression.  |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Att                                                                          | Track attendance by clicking thumbs up or thumbs down icons.                  |
| endance](https://www.appsheet.com/template/showdef?appId=AttendanceApp-71626) |                                                                               |
|                                                                               | The app defines                                                               |
|                                                                               | [actions](https://support.google.com/appsheet/answer/10107706) to trigger the |
|                                                                               | following updates:                                                            |
|                                                                               |                                                                               |
|                                                                               | -   Change an attendee's status to Present or Absent                          |
|                                                                               | -   Allow you to set the Building and Room for attendance tracking.           |
|                                                                               |                                                                               |
|                                                                               | The `Roster` table keeps track of the most recent data. The                   |
|                                                                               | `Attendance Records` table keeps track of all attendance records.             |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Bulk                                                                         | Apply an action to multiple rows using bulk select.                           |
| actions](https://www.appsheet.com/template/showdef?appId=Bulkactions-71626)   |                                                                               |
|                                                                               | Click the checkbox in the upper-right corner of the app to select multiple    |
|                                                                               | rows. Then, click More  to select an action. On mobile devices, you can long  |
|                                                                               | press on a row to enable bulk action mode. See also [Use bulk                 |
|                                                                               | actions](https://support.google.com/appsheet/answer/10107372).                |
|                                                                               |                                                                               |
|                                                                               | The sample app:                                                               |
|                                                                               |                                                                               |
|                                                                               | -   Defines three                                                             |
|                                                                               |     [slices](https://support.google.com/appsheet/answer/10106592) of `Tasks`  |
|                                                                               |     data, Not Started, Started, and Finished, with the Row filter condition   |
|                                                                               |     based on the `Status` column value.                                       |
|                                                                               | -   Provides [table                                                           |
|                                                                               |     views](https://support.google.com/appsheet/answer/10106514) for viewing   |
|                                                                               |     each slice of data.                                                       |
|                                                                               | -   Defines [actions](https://support.google.com/appsheet/answer/10107706) to |
|                                                                               |     change an item's status from Not Started to Started and from Started to   |
|                                                                               |     Finished. You can also edit an item directly to change its status.        |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Calculate                                                                    | Calculate the distance from a user's current location to a designated         |
| distanc                                                                       | location (such as the location of a building), identified as a                |
| es](https://www.appsheet.com/template/showdef?appId=Calculatedistances-71626) | [`LatLong`](https://support.google.com/appsheet/answer/10106435#mappable).    |
|                                                                               |                                                                               |
|                                                                               | The sample app:                                                               |
|                                                                               |                                                                               |
|                                                                               | -   Calculates the distance using the                                         |
|                                                                               |     [`DISTANCE()`](https://support.google.com/appsheet/answer/11587699)       |
|                                                                               |     function based on the user's current location                             |
|                                                                               |     ([`HERE()`](https://support.google.com/appsheet/answer/10107405)) and the |
|                                                                               |     `LatLong` value.                                                          |
|                                                                               | -   Provides a Distances [deck                                                |
|                                                                               |     view](https://support.google.com/appsheet/answer/10106514) that lists the |
|                                                                               |     users and their distance from the `LatLong` location.                     |
|                                                                               | -   Provides a Map [map                                                       |
|                                                                               |     view](https://support.google.com/appsheet/answer/10106601) that           |
|                                                                               |     identifies a user's location as a point on a map.                         |
|                                                                               | -   Requires location services to be turned on.                               |
|                                                                               |                                                                               |
|                                                                               |     At this time distances can only be computed between `LatLong` data types. |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Change                                                                       | Record the timestamp when specific columns are changed.                       |
| columns](https://www.appsheet.com/template/showdef?appId=ChangeColumns-71626) |                                                                               |
|                                                                               | [Change type columns](https://support.google.com/appsheet/answer/10106528)    |
|                                                                               | are useful for keeping track of how many changes have happened to a row and   |
|                                                                               | when they happened.                                                           |
|                                                                               |                                                                               |
|                                                                               | A set of columns are used to track changes to the `Color` and `Decimal`       |
|                                                                               | columns using the `ChangeTimestamp` and `ChangeCounter` data                  |
|                                                                               | types. Change the Color and Decimal values to see a demo.                     |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Change view on row                                                           | Dynamically change views based on row selection.                              |
| selection](ht                                                                 |                                                                               |
| tps://www.appsheet.com/template/showdef?appId=ChangeViewonRowSelection-71626) | This sample app defines an                                                    |
|                                                                               | [action](https://support.google.com/appsheet/answer/10107706) called Change   |
|                                                                               | View that uses the                                                            |
|                                                                               | [                                                                             |
|                                                                               | `LINKTOVIEW()`](https://support.google.com/appsheet/answer/10108105) function |
|                                                                               | to change the current view based on the `View Name` column in the             |
|                                                                               | `Views` table. The action is bound to the view's Row Selected event.          |
|                                                                               |                                                                               |
|                                                                               | Change view to Letters View or Numbers View                                   |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Chart of related                                                             | Display a chart view                                                          |
| records](https://www.appsheet.com/template/showdef?appId=Chartperrow-71626)   | (                                                                             |
|                                                                               | [histogram](https://support.google.com/appsheet/answer/10107874#chart-types)) |
|                                                                               | of the related records for a particular row.                                  |
|                                                                               |                                                                               |
|                                                                               | Each row in the `Item` table is associated with a particular `Person` row     |
|                                                                               | using the `Owner` column.                                                     |
|                                                                               |                                                                               |
|                                                                               | The sample app provides the following views:                                  |
|                                                                               |                                                                               |
|                                                                               | -   Person [table view](https://support.google.com/appsheet/answer/10106514)  |
|                                                                               |     that lists each person and the number of related items.                   |
|                                                                               | -   Chart [chart view](https://support.google.com/appsheet/answer/10107847)   |
|                                                                               |     (histogram) that displays the related items for the person by size.       |
|                                                                               |                                                                               |
|                                                                               | Try selecting a person to see a chart of the person's related items by size.  |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Click to send                                                                | *Description coming soon. See the [app                                        |
| e                                                                             | documentat                                                                    |
| mail](https://www.appsheet.com/template/showdef?appId=ClickToSendEmail-71626) | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Conditional format                                                           | *Description coming soon. See the [app                                        |
| rules](https://www.appsheet.com/template/showdef?appId=Formatrules-71626)     | documentat                                                                    |
|                                                                               | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Contractor                                                                   | Keep track of contractor project costs.                                       |
| costs](https://www.appsheet.com/template/showdef?appId=Contractor-71626)      |                                                                               |
|                                                                               | The sample app is connected to a spreadsheet where all the project            |
|                                                                               | information, including costs, is tracked for a project. The contractor can    |
|                                                                               | track the project estimate, actual costs, and progress of the different jobs  |
|                                                                               | performed in the project.                                                     |
|                                                                               |                                                                               |
|                                                                               | Each view displays a                                                          |
|                                                                               | [slice](https://support.google.com/appsheet/answer/10106592) of the `Remodel` |
|                                                                               | data that excludes the `Total Cost Overrun` value. This allows the contractor |
|                                                                               | to share the app with the customer so they can track expenditures and overall |
|                                                                               | progress, but not data the contractor regards as more sensitive.              |
|                                                                               |                                                                               |
|                                                                               | The sample app allows you to do the following:                                |
|                                                                               |                                                                               |
|                                                                               | -   View a [chart](https://support.google.com/appsheet/answer/10107847) of    |
|                                                                               |     type [Col                                                                 |
|                                                                               |     Series](https://support.google.com/appsheet/answer/10107874#chart-types)  |
|                                                                               |     that shows the actual costs.                                              |
|                                                                               | -   List data by status or by area (as a [table                               |
|                                                                               |     view](https://support.google.com/appsheet/answer/10106514)).              |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Custom map                                                                   | *Description coming soon. See the [app                                        |
| pins](https://www.appsheet.com/template/showdef?appId=Mapicons-71626)         | documentat                                                                    |
|                                                                               | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Custom                                                                       | *Description coming soon. See the [app                                        |
| maps](https://www.appsheet.com/template/showdef?appId=Custommaps-71626)       | documentat                                                                    |
|                                                                               | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Custom                                                                       | *Description coming soon. See the [app                                        |
| reports](https://www.appsheet.com/template/showdef?appId=Customreport-71626)  | documentat                                                                    |
|                                                                               | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Custom tour                                                                  | *Description coming soon. See the [app                                        |
| guide](https://www.appsheet.com/template/showdef?appId=WAAgritourism-71626)   | documentat                                                                    |
|                                                                               | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Deep links](https://www.appsheet.com/template/showdef?appId=Deeplinks-71626) | *Description coming soon. See the [app                                        |
|                                                                               | documentat                                                                    |
|                                                                               | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Dependent                                                                    | *Description coming soon. See the [app                                        |
| drop-dow                                                                      | documentat                                                                    |
| ns](https://www.appsheet.com/template/showdef?appId=DependentDropdowns-71626) | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Distinct                                                                     | *Description coming soon. See the [app                                        |
| pair                                                                          | documentat                                                                    |
| s](https://www.appsheet.com/template/showdef?appId=ItemCharacteristics-71626) | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Distinct value                                                               | *Description coming soon. See the [app                                        |
| drop-d                                                                        | documentat                                                                    |
| own](https://www.appsheet.com/template/showdef?appId=Onlyallowdistinct-71626) | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Drill-down](https://www.appsheet.com/template/showdef?appId=Drilldown-71626) | *Description coming soon. See the [app                                        |
|                                                                               | documentat                                                                    |
|                                                                               | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Drop-downs](https://www.appsheet.com/template/showdef?appId=Dropdowns-71626) | *Description coming soon. See the [app                                        |
|                                                                               | documentat                                                                    |
|                                                                               | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Dynamic form                                                                 | *Description coming soon. See the [app                                        |
| act                                                                           | documentat                                                                    |
| ion](https://www.appsheet.com/template/showdef?appId=DynamicFormAction-71626) | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Dynamic                                                                      | *Description coming soon. See the [app                                        |
| inven                                                                         | documentat                                                                    |
| tory](https://www.appsheet.com/template/showdef?appId=Dynamicinventory-71626) | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Dynamic inventory with                                                       | *Description coming soon. See the [app                                        |
| quantity](https:                                                              | documentat                                                                    |
| //www.appsheet.com/template/showdef?appId=Dynamicinventorywithquantity-71626) | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Employee                                                                     | Give visual instructions to employees of a company on how to administer CPR   |
| trai                                                                          | in the event of a medical emergency.                                          |
| ning](https://www.appsheet.com/template/showdef?appId=EmployeeTraining-71626) |                                                                               |
|                                                                               | The app uses a spreadsheet with four rows: `Step`, `Title`, `Details`, and    |
|                                                                               | `Image`.                                                                      |
|                                                                               |                                                                               |
|                                                                               | One of the most important aspects of this sample app is the **images** it     |
|                                                                               | features that show employees exactly how to perform each step. The            |
|                                                                               | spreadsheet includes an `Image` column that define the file names of each     |
|                                                                               | image that corresponds to the step.                                           |
|                                                                               |                                                                               |
|                                                                               | The sample app provides a Steps [deck                                         |
|                                                                               | view](https://support.google.com/appsheet/answer/10106514) that allows you to |
|                                                                               | view each step in a specific order. This is necessary as it could be a matter |
|                                                                               | of life and death if steps are not followed in the correct order. In the      |
|                                                                               | Steps deck view, the app gives general information; clicking each item gives  |
|                                                                               | a more detailed description of how to perform the step.                       |
|                                                                               |                                                                               |
|                                                                               | By contrast, the [gallery                                                     |
|                                                                               | view](https://support.google.com/appsheet/answer/10106770) sets items         |
|                                                                               | adjacent to each other and would not be appropriate for this particular app.  |
|                                                                               |                                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Enum vs                                                                      | Builds the following drop-downs from a simple list of values:                 |
| En                                                                            |                                                                               |
| umList](https://www.appsheet.com/template/showdef?appId=EnumvsEnumList-71626) | -   Select **one** type of fruit from a list (using an `Enum`)                |
|                                                                               | -   Select **multiple** types of fruit from a list (using an `EnumList`)      |
|                                                                               |                                                                               |
|                                                                               | The following illustrates how the drop-downs appear in the app.               |
|                                                                               |                                                                               |
|                                                                               | For more information, see [Display a drop-down with a simple list of          |
|                                                                               | values](https://support.google.com/appsheet/answer/10107878).                 |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Equipment                                                                    | *Description coming soon. See the [app                                        |
| inspections]                                                                  | documentat                                                                    |
| (https://www.appsheet.com/template/showdef?appId=EquipmentInspections2-71626) | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Export CSV](https://www.appsheet.com/template/showdef?appId=ExportCSV-71626) | *Description coming soon. See the [app                                        |
|                                                                               | documentat                                                                    |
|                                                                               | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Export CSV of filtered                                                       | *Description coming soon. See the [app                                        |
| rows](h                                                                       | documentat                                                                    |
| ttps://www.appsheet.com/template/showdef?appId=ExportCSVoffilteredrows-71626) | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Field                                                                        | *Description coming soon. See the [app                                        |
| survey](https://www.appsheet.com/template/showdef?appId=SiteInspection-71626) | documentat                                                                    |
|                                                                               | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Formatting                                                                   | *Description coming soon. See the [app                                        |
| dates](https://www.appsheet.com/template/showdef?appId=Dayoftheweek-71626)    | documentat                                                                    |
|                                                                               | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Form with                                                                    | *Description coming soon. See the [app                                        |
| tabs](https://www.appsheet.com/template/showdef?appId=FormwithTabs-71626)     | documentat                                                                    |
|                                                                               | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [                                                                             | *Description coming soon. See the [app                                        |
| Geofencing](https://www.appsheet.com/template/showdef?appId=Geofencing-71626) | documentat                                                                    |
|                                                                               | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Hide field in                                                                | *Description coming soon. See the [app                                        |
| form](https://www.appsheet.com/template/showdef?appId=OnlyShowinForm-71626)   | documentat                                                                    |
|                                                                               | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Hierarchical                                                                 | *Description coming soon. See the [app                                        |
| menu](https://www.appsheet.com/template/showdef?appId=HierarchicalMenu-71626) | documentat                                                                    |
|                                                                               | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Histogram](https://www.appsheet.com/template/showdef?appId=Histogram-71626)  | *Description coming soon. See the [app                                        |
|                                                                               | documentat                                                                    |
|                                                                               | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Home                                                                         | *Description coming soon. See the [app                                        |
| ins                                                                           | documentat                                                                    |
| pection](https://www.appsheet.com/template/showdef?appId=HomeInspector-71626) | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [How to sort](https://www.appsheet.com/template/showdef?appId=Sorting-71626)  | Sort your data by a column.                                                   |
|                                                                               |                                                                               |
|                                                                               | The sample app provides two [table                                            |
|                                                                               | views](https://support.google.com/appsheet/answer/10106514), one that sorts   |
|                                                                               | by values in the `Price` column and one that sorts alphabetically by values   |
|                                                                               | in the `Name` column.                                                         |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [How to use                                                                   | *Description coming soon. See the [app                                        |
| slices](https://www.appsheet.com/template/showdef?appId=Slice-71626)          | documentat                                                                    |
|                                                                               | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [                                                                             | *Description coming soon. See the [app                                        |
| Hyperlinks](https://www.appsheet.com/template/showdef?appId=Hyperlinks-71626) | documentat                                                                    |
|                                                                               | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Icon main                                                                    | *Description coming soon. See the [app                                        |
| menu](https://www.appsheet.com/template/showdef?appId=IconMainMenu-71626)     | documentat                                                                    |
|                                                                               | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [ICS                                                                          | *Description coming soon. See the [app                                        |
| example](https://www.appsheet.com/template/showdef?appId=ICSExample-71626)    | documentat                                                                    |
|                                                                               | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Image                                                                        | *Description coming soon. See the [app                                        |
| annotat                                                                       | documentat                                                                    |
| ions](https://www.appsheet.com/template/showdef?appId=Imageannotations-71626) | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Images in                                                                    | Include an image in a form that is not stored in your data.                   |
| forms](https://www.appsheet.com/template/showdef?appId=Imagesinforms-71626)   |                                                                               |
|                                                                               | Images in forms sample app                                                    |
|                                                                               |                                                                               |
|                                                                               | The app includes a table with a [`Show`                                       |
|                                                                               | type](https://support.google.com/appsheet/answer/12463320) column called      |
|                                                                               | `Show Image`. In the Type Details for the column, the Category is set to      |
|                                                                               | `Image` and Content is set to the URL of the image.                           |
|                                                                               |                                                                               |
|                                                                               | Category is set to Image, Content is set to the URL of the image.             |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Images in                                                                    | *Description coming soon. See the [app                                        |
| sheets](https://www.appsheet.com/template/showdef?appId=Imagesinsheets-71626) | documentat                                                                    |
|                                                                               | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Initialize to nearest                                                        | *Description coming soon. See the [app                                        |
| location](https                                                               | documentat                                                                    |
| ://www.appsheet.com/template/showdef?appId=InitializetoNearestLocation-71626) | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Inspection app                                                               | *Description coming soon. See the [app                                        |
| u                                                                             | documentat                                                                    |
| pgrade](https://www.appsheet.com/template/showdef?appId=InspectionApp2-71626) | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Inspection                                                                   | *Description coming soon. See the [app                                        |
| templa                                                                        | documentat                                                                    |
| te](https://www.appsheet.com/template/showdef?appId=InspectionTemplate-71626) | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Interactive                                                                  | *Description coming soon. See the [app                                        |
| dashboard                                                                     | documentat                                                                    |
| ](https://www.appsheet.com/template/showdef?appId=InteractiveDashboard-71626) | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Interactive map                                                              | Develop an interactive dashboard view using a map. (View app in full-screen   |
| dashboa                                                                       | mode.)                                                                        |
| rd](https://www.appsheet.com/template/showdef?appId=WorldHeritageSites-71626) |                                                                               |
|                                                                               | The sample app provides the following views:                                  |
|                                                                               |                                                                               |
|                                                                               | -   Dash [dashboard                                                           |
|                                                                               |     view](https://support.google.com/appsheet/answer/10106384) that allows    |
|                                                                               |     you to display multiple views in one place; specifically, the Countries   |
|                                                                               |     and Sites Map views.                                                      |
|                                                                               | -   Countries [table                                                          |
|                                                                               |     view](https://support.google.com/appsheet/answer/10106514) that displays  |
|                                                                               |     the list of countries. Select a country to focus the map view.            |
|                                                                               | -   Sites Map [map view](https://support.google.com/appsheet/answer/10106601) |
|                                                                               |     that displays location and details for world heritage sites.              |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Item                                                                         | *Description coming soon. See the [app                                        |
| reserv                                                                        | documentat                                                                    |
| ation](https://www.appsheet.com/template/showdef?appId=Itemreservation-71626) | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Lead                                                                         | *Description coming soon. See the [app                                        |
| tracking](https://www.appsheet.com/template/showdef?appId=LeadTracking-71626) | documentat                                                                    |
|                                                                               | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Link to                                                                      | *Description coming soon. See the [app                                        |
| f                                                                             | documentat                                                                    |
| orm](https://www.appsheet.com/template/showdef?appId=LinktoformExample-71626) | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Local events                                                                 | *Description coming soon. See the [app                                        |
| calenda                                                                       | documentat                                                                    |
| r](https://www.appsheet.com/template/showdef?appId=LocalEventsCalendar-71626) | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Log chart                                                                    | *Description coming soon. See the [app                                        |
| viewer](https://www.appsheet.com/template/showdef?appId=LogChart-71626)       | documentat                                                                    |
|                                                                               | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Lookup                                                                       | Access the value of a column that corresponds to the column value in the same |
| function](https://www.appsheet.com/template/showdef?appId=Lookup-71626)       | row.                                                                          |
|                                                                               |                                                                               |
|                                                                               | In the `Form` table, the following                                            |
|                                                                               | [`LOOKUP()`](https://support.google.com/appsheet/answer/10107410) functions   |
|                                                                               | find the row of `Lookup Table` whose `Email` column equals the email address  |
|                                                                               | entered by the user. Then, it returns the `Name` or `Color` value for that    |
|                                                                               | row.                                                                          |
|                                                                               |                                                                               |
|                                                                               | `LOOKUP([Chosen Email], "Lookup Table", "Email", "Name")`\                    |
|                                                                               | `LOOKUP([Chosen Email], "Lookup Table", "Email", "Color")`                    |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Lookup                                                                       | *Description coming soon. See the [app                                        |
| table](https://www.appsheet.com/template/showdef?appId=LookupTable-71626)     | documentat                                                                    |
|                                                                               | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Media                                                                        | Review budgeting data by time period and by media type.                       |
| budget](https://www.appsheet.com/template/showdef?appId=MediaBudget-71626)    |                                                                               |
|                                                                               | You can view how a marketing budget has been spent in different media and the |
|                                                                               | total amount of marketing budget by quarter. The app also lets you review all |
|                                                                               | items in the budget and update them if necessary. The app doesn't let you add |
|                                                                               | data but it lets you edit any entry to the budget section. Additionally, it   |
|                                                                               | enables you to search the key partners involved in each marketing initiative  |
|                                                                               | and details their duties.                                                     |
|                                                                               |                                                                               |
|                                                                               | The sample app provides the following views:                                  |
|                                                                               |                                                                               |
|                                                                               | -   Items [table view](https://support.google.com/appsheet/answer/10106514)   |
|                                                                               |     shows all the items in the budget for review.                             |
|                                                                               | -   By Media [chart                                                           |
|                                                                               |     view](https://support.google.com/appsheet/answer/10107847) lets the user  |
|                                                                               |     filter information by quarter when they select the filters in the top of  |
|                                                                               |     the chart. This is a quick way to see how expenditures will be made over  |
|                                                                               |     time and a quick way to compare between different media.                  |
|                                                                               | -   By Quarter chart view allows the user to compare expenditures by          |
|                                                                               |     different type of media in a specific quarter. This is a quick way to     |
|                                                                               |     review all expenditures happening over the same period and helps the user |
|                                                                               |     compare quarter to quarter information.                                   |
|                                                                               | -   Key Partners table view in the hamburger menu enables users to see which  |
|                                                                               |     projects partners are working as well as to see the main duties each      |
|                                                                               |     partner is assigned to.                                                   |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Most recent child                                                            | *Description coming soon. See the [app                                        |
| r                                                                             | documentat                                                                    |
| ow](https://www.appsheet.com/template/showdef?appId=MostRecentChildRow-71626) | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Most recent                                                                  | *Description coming soon. See the [app                                        |
| value](https://www.appsheet.com/template/showdef?appId=MostRecentValue-71626) | documentat                                                                    |
|                                                                               | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Multi-page                                                                   | *Description coming soon. See the [app                                        |
| forms](https://www.appsheet.com/template/showdef?appId=Multi-PageForms-71626) | documentat                                                                    |
|                                                                               | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Nested                                                                       | *Description coming soon. See the [app                                        |
| forms](https://www.appsheet.com/template/showdef?appId=Nestedforms-71626)     | documentat                                                                    |
|                                                                               | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [OCRTEXT()                                                                    | *Description coming soon. See the [app                                        |
| demo](https://www.appsheet.com/template/showdef?appId=OCRTEXTDemo-71626)      | documentat                                                                    |
|                                                                               | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Order capture                                                                | Manage customers, products, and orders.                                       |
| how-                                                                          |                                                                               |
| to](https://www.appsheet.com/template/showdef?appId=OrderCaptureHow-to-71626) | The sample app allows you to:                                                 |
|                                                                               |                                                                               |
|                                                                               | -   Create and edit a customer list.                                          |
|                                                                               | -   Create and edit a product list.                                           |
|                                                                               | -   Create orders associated with a customer. Orders can have three statuses: |
|                                                                               |     Open, Complete, or Canceled                                               |
|                                                                               | -   Add products to each order, specifying an amount. The app will calculate  |
|                                                                               |     the total value of the order and the total cost per product.              |
|                                                                               |                                                                               |
|                                                                               | The sample app leverages the following AppSheet features:                     |
|                                                                               |                                                                               |
|                                                                               | -   [References between                                                       |
|                                                                               |                                                                               |
|                                                                               |    tables](https://support.google.com/appsheet/answer/10106510). `Customers`, |
|                                                                               |     `Orders`, and O`rder Details` are connected by references between tables. |
|                                                                               |     When an order is created, there's a drop-down listing all the customers.  |
|                                                                               |     That list is dynamically updated every time the customer list is updated. |
|                                                                               |     Additionally, every time the user opens the details of a customer, a new  |
|                                                                               |     order can be created from that view.                                      |
|                                                                               | -   [Spreadsheet                                                              |
|                                                                               |     formulas](https://support.google.com/appsheet/answer/10099797). A set of  |
|                                                                               |     formulas are calculated after the app is synced with the spreadsheet. The |
|                                                                               |     Order Total formula in the Orders view is calculated after the            |
|                                                                               |     spreadsheet is synced with the app.                                       |
|                                                                               | -   [Slices](https://support.google.com/appsheet/answer/10106592) to access   |
|                                                                               |     open orders, open orders by customer, open order details, and closed      |
|                                                                               |     order details.                                                            |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Ordered                                                                      | *Description coming soon. See the [app                                        |
| drop                                                                          | documentat                                                                    |
| -down](https://www.appsheet.com/template/showdef?appId=OrderedDropdown-71626) | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Out of office                                                                | *Description coming soon. See the [app                                        |
| app](https://www.appsheet.com/template/showdef?appId=OutofOfficeApp-71626)    | documentat                                                                    |
|                                                                               | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Part                                                                         | *Description coming soon. See the [app                                        |
| itioning](https://www.appsheet.com/template/showdef?appId=Partitioning-71626) | documentat                                                                    |
|                                                                               | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Pie chart](https://www.appsheet.com/template/showdef?appId=PieChart-71626)   | *Description coming soon. See the [app                                        |
|                                                                               | documentat                                                                    |
|                                                                               | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Project                                                                      | *Description coming soon. See the [app                                        |
| m                                                                             | documentat                                                                    |
| anagement](https://www.appsheet.com/template/showdef?appId=ProjectPlan-71626) | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Property                                                                     | *Description coming soon. See the [app                                        |
| management]                                                                   | documentat                                                                    |
| (https://www.appsheet.com/template/showdef?appId=PropertyManagementApp-71626) | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Quote                                                                        | *Description coming soon. See the [app                                        |
| calc                                                                          | documentat                                                                    |
| ulator](https://www.appsheet.com/template/showdef?appId=RateCalculator-71626) | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Quote and                                                                    | *Description coming soon. See the [app                                        |
| prop                                                                          | documentat                                                                    |
| osal](https://www.appsheet.com/template/showdef?appId=QuoteandProposal-71626) | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Ref list                                                                     | *Description coming soon. See the [app                                        |
| filter](https://www.appsheet.com/template/showdef?appId=FilterRefList-71626)  | documentat                                                                    |
|                                                                               | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Reference                                                                    | Use reference actions.                                                        |
| ac                                                                            |                                                                               |
| tions](https://www.appsheet.com/template/showdef?appId=ReferenceAction-71626) | Reference actions are used to modify a row in one table using an action       |
|                                                                               | defined in another table. In this sample app:                                 |
|                                                                               |                                                                               |
|                                                                               | -   The Parent table has an action called **+1 All** that adds 1 to the       |
|                                                                               |     `Number` column of its associated children records. The action is of type |
|                                                                               |     [Data: execute an action on a set of                                      |
|                                                                               |     rows](https://support.                                                    |
|                                                                               | google.com/appsheet/answer/10107706#data-execute-an-action-on-a-set-of-rows). |
|                                                                               | -   The Child table has an action called **+1** that adds 1 to the `Number`   |
|                                                                               |     column of the current record. The action is of type [Data: set the values |
|                                                                               |     of some columns in this                                                   |
|                                                                               |     row](https://support.google.                                              |
|                                                                               | com/appsheet/answer/10107706#data-set-the-value-of-some-columns-in-this-row). |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Reminders](https://www.appsheet.com/template/showdef?appId=Reminders-71626)  | *Description coming soon. See the [app                                        |
|                                                                               | documentat                                                                    |
|                                                                               | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Repair                                                                       | Provide an instruction manual to employees or customers.                      |
| manual](https://www.appsheet.com/template/showdef?appId=RepairManual-71626)   |                                                                               |
|                                                                               | The app is created from three tables. In each case:                           |
|                                                                               |                                                                               |
|                                                                               | -   The `Title` column contains the name of each step, while the              |
|                                                                               |     `Description` column contains the actual instructions on how to perform   |
|                                                                               |     the step.                                                                 |
|                                                                               |                                                                               |
|                                                                               | -   The `Image` column automatically activates the `Image` type in the app    |
|                                                                               |     editor and app. In this case, images are being rendered using publicly    |
|                                                                               |     hosted URLs. Images can also be rendered with a filename that exactly     |
|                                                                               |     matches the filename in the app’s folder in the cloud provider. See       |
|                                                                               |     [Display images and                                                       |
|                                                                               |     documents](https://support.google.com/appsheet/answer/10107317).          |
|                                                                               |                                                                               |
|                                                                               | -   All tables in the app are marked as *read-only* so the app user can view  |
|                                                                               |     the contents but can't edit, add, or delete any data.                     |
|                                                                               |                                                                               |
|                                                                               | The [deck view](https://support.google.com/appsheet/answer/10106514) displays |
|                                                                               | steps in a vertical presentation in the order that they are intended to be    |
|                                                                               | performed accompanied by helpful images that demonstrate the step.            |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Repair                                                                       | *Description coming soon. See the [app                                        |
| requests](http                                                                | documentat                                                                    |
| s://www.appsheet.com/template/showdef?appId=MaintenanceOverview-114348-71626) | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Row labels and                                                               | *Description coming soon. See the [app                                        |
| keys](https://www.appsheet.com/template/showdef?appId=Rowlabelsandkeys-71626) | documentat                                                                    |
|                                                                               | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Safety                                                                       | *Description coming soon. See the [app                                        |
| reporti                                                                       | documentat                                                                    |
| ng](https://www.appsheet.com/template/showdef?appId=SafetyReportingApp-71626) | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Sales                                                                        | *Description coming soon. See the [app                                        |
| reporting](https://www.appsheet.com/template/showdef?appId=SalesReport-71626) | documentat                                                                    |
|                                                                               | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Search in                                                                    | *Description coming soon. See the [app                                        |
| form](https://www.appsheet.com/template/showdef?appId=SearchinForm-71626)     | documentat                                                                    |
|                                                                               | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Search using a                                                               | *Description coming soon. See the [app                                        |
| form]                                                                         | documentat                                                                    |
| (https://www.appsheet.com/template/showdef?appId=Untitledspreadsheet-71626-3) | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Share                                                                        | *Description coming soon. See the [app                                        |
| button](https://www.appsheet.com/template/showdef?appId=ShareButton-71626)    | documentat                                                                    |
|                                                                               | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Ship                                                                         | *Description coming soon. See the [app                                        |
| inspect                                                                       | documentat                                                                    |
| ion](https://www.appsheet.com/template/showdef?appId=ShipInspectionApp-71626) | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Slice based on user                                                          | *Description coming soon. See the [app                                        |
| input](http                                                                   | documentat                                                                    |
| s://www.appsheet.com/template/showdef?appId=Interactivedashboardfilter-71626) | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Slice by                                                                     | *Description coming soon. See the [app                                        |
| date](https://www.appsheet.com/template/showdef?appId=SlicebyDate-71626)      | documentat                                                                    |
|                                                                               | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Sliders](https://www.appsheet.com/template/showdef?appId=Sliders-71626)      | *Description coming soon. See the [app                                        |
|                                                                               | documentat                                                                    |
|                                                                               | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Split on                                                                     | *Description coming soon. See the [app                                        |
| n                                                                             | documentat                                                                    |
| ewline](https://www.appsheet.com/template/showdef?appId=SplitonNewline-71626) | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Sum by                                                                       | *Description coming soon. See the [app                                        |
| date](https://www.appsheet.com/template/showdef?appId=Sumbydate-71626)        | documentat                                                                    |
|                                                                               | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [SUM() and                                                                    | *Description coming soon. See the [app                                        |
| CO                                                                            | documentat                                                                    |
| UNT()](https://www.appsheet.com/template/showdef?appId=SUMIFandCOUNTIF-71626) | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Switch                                                                       | *Description coming soon. See the [app                                        |
| expressi                                                                      | documentat                                                                    |
| ons](https://www.appsheet.com/template/showdef?appId=SwitchExpressions-71626) | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Table                                                                        | *Description coming soon. See the [app                                        |
| references](h                                                                 | documentat                                                                    |
| ttps://www.appsheet.com/template/showdef?appId=Referencesbetweentables-71626) | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Time                                                                         | *Description coming soon. See the [app                                        |
| clock](https://www.appsheet.com/template/showdef?appId=Timesheet-71626-2)     | documentat                                                                    |
|                                                                               | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Timer                                                                        | *Description coming soon. See the [app                                        |
| app](https://www.appsheet.com/template/showdef?appId=TimerExample-71626)      | documentat                                                                    |
|                                                                               | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Top related                                                                  | *Description coming soon. See the [app                                        |
| items](https://www.appsheet.com/template/showdef?appId=Toprelateditems-71626) | documentat                                                                    |
|                                                                               | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [United states                                                                | *Description coming soon. See the [app                                        |
| population](                                                                  | documentat                                                                    |
| https://www.appsheet.com/template/showdef?appId=UnitedStatesPopulation-71626) | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Video                                                                        | *Description coming soon. See the [app                                        |
| columns](https://www.appsheet.com/template/showdef?appId=VideoColumns-71626)  | documentat                                                                    |
|                                                                               | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Video                                                                        | *Description coming soon. See the [app                                        |
| comments](https://www.appsheet.com/template/showdef?appId=Commenting-71626)   | documentat                                                                    |
|                                                                               | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [View                                                                         | Count the number of times a row has been viewed in your app.                  |
| counter](https://www.appsheet.com/template/showdef?appId=ViewCounter-71626)   |                                                                               |
|                                                                               | Each row has a `Counter` column that holds the view count. When you click on  |
|                                                                               | a row in the table view, it increments the counter.                           |
|                                                                               |                                                                               |
|                                                                               | The app defines custom actions to override the default behavior when you      |
|                                                                               | click a row in a table view, including:                                       |
|                                                                               |                                                                               |
|                                                                               | -   Navigate: Navigates to the detail view of the row. The action type is     |
|                                                                               |     [App: go to another view within this                                      |
|                                                                               |     app](https://support                                                      |
|                                                                               | .google.com/appsheet/answer/10107706#app-go-to-another-view-within-this-app). |
|                                                                               | -   Increment: Increments the counter of the row. The action type is Data:    |
|                                                                               |     set the values of some columns in this row.                               |
|                                                                               | -   Increment and Navigate: Does both of the above actions. The action type   |
|                                                                               |     is Grouped: execute a sequence of actions, namely the Increment and       |
|                                                                               |     Navigate actions.                                                         |
|                                                                               |                                                                               |
|                                                                               | The Row Selected behavior in the View Counter1 view is configured to call the |
|                                                                               | Increment and Navigate action.                                                |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Wind turbine                                                                 | *Description coming soon. See the [app                                        |
| inspect                                                                       | documentat                                                                    |
| ion](https://www.appsheet.com/template/showdef?appId=WindyPowerCompany-71626) | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| [Workflow when children                                                       | *Description coming soon. See the [app                                        |
| added](https://www.appsheet.com/template/showdef?appId=Nestedforms-71626-2)   | documentat                                                                    |
|                                                                               | ion](https://support.google.com/appsheet/answer/10106613#app-documentation).* |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
