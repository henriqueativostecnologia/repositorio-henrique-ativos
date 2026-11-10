---
fonte: https://support.google.com/appsheet/answer/10106508?hl=en
baixado: 2026-11-10
---

# Private tables

By default, all tables in an app are owned by the app creator and shared across all users of the app. For example, in an Order Capture sales app, the `Products`, `Customers`, and `Orders` tables are all common to all the users of the app (salespeople who work for the organization). This is a familiar database application pattern: the tables (in spreadsheets) correspond to a central shared database of information. it is the prevalent pattern for corporate apps.

However, there are apps that require individual per-user data. Here are some examples:

1.  **A product catalog with a note-taking feature**: There is a common shared product catalog, but each user can use the app to take notes about the individual products. The notes are private to each user.
2.  **A school test practice app**: There is a common shared set of questions, but each student's answers remain private to that student.
3.  **An exercise app**: There are common shared workout routines, but each user can record their own progress.

This ability to have per-user private data is particularly relevant when an app creator builds an app and distributes it widely. The users of the app may not know the app creator, and certainly do not intend the app creator to access their private information.

AppSheet supports private data using **private tables**.

## Configure a private table

A private table is defined just the same as any other table in an AppSheet app. It has a column structure, and is defined by a spreadsheet (or other data source). However, the table is explicitly marked as private (not shared).

To configure a private table:

1.  Open the app in the app editor.
2.  Go to **Data **, select the table you want to configure in the list, and click **Table settings**  Table settings icon  in the table header.
    ## If you are using the legacy editor

     

    Go to **Data \> Tables** and expand the table that you want to configure.
3.  Expand the **Security** section.
4.  Disable the **Shared?** option.
5.  Save your changes.

An app with private tables must [require user sign-in](https://support.google.com/appsheet/answer/10104975).

Every user who uses the app gets a private copy of each private table in the app. The copy is stored in the user's cloud storage account and initialized with the data provided by the app creator in the original table definition. The private table's name is in the form `{appTemplate.Name}_{appTable.Name}`. The data in the private table is accessible only to the specific user who created it. Each user's changes are made independently.

If the same user accesses the app from different devices using the same account to sign in, then the same private table is used from each device. This is a benefit of storing the private table in cloud storage, rather than locally on each device.

In all other ways, the app acts in the same manner as any other.

## Restrictions and notes

A private table must be the only worksheet in the workbook. Your app can have a number of workbooks and worksheets, but each private table must be the only worksheet in its own workbook.

Another thing to consider is that private tables can make app changes more complicated. When a user starts using an app with private tables, they will get a copy of the original worksheet as it exists at that moment, including the current column structure. If the app owner wants to update that column structure (add, remove, or reorder columns), these changes will not propagate to existing users. This has the potential to break an app for existing users. You should make sure your column structure is finalized and unlikely to change in the future before giving users an app with private tables.
