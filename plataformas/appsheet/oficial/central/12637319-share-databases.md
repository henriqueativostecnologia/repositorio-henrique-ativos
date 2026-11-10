---
fonte: https://support.google.com/appsheet/answer/12637319?hl=en
baixado: 2026-11-10
---

# Share databases

Share a database with individual users or the owner's team to allow them to edit or use the databases in an app.

- [Understand the database permissions](#database-permissions)
- [Share a database with individual users](#share)
- [Share a database with the database owner's team](#share-team)
- [Manage permissions for individual users ](#manage-permissions)
- [Send users a link to the database](#send%20link)
- [Restrict external database sharing](#restrict-external-sharing)

## Understand the database permissions

The following permissions are supported for AppSheet databases.

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Permission**                                                                | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Viewer                                                                        | -   View the database only; can't edit content                                |
|                                                                               | -   Can *temporarily* adjust grouping, filtering, and sorting (doesn’t impact |
|                                                                               |     other users)                                                              |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Writer                                                                        | -   View database                                                             |
|                                                                               | -   Edit **row** data                                                         |
|                                                                               | -   Connect an app to a database                                              |
|                                                                               | -   Can't change table structure (columns, views, etc.)                       |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Editor                                                                        | -   View and edit database                                                    |
|                                                                               | -   Share databases with others                                               |
|                                                                               | -   Connect an app to a database                                              |
|                                                                               | -   Can't delete database or tables                                           |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Owner                                                                         | -   View and edit database                                                    |
|                                                                               | -                                                                             |
|                                                                               | -   Share databases with others                                               |
|                                                                               | -   Connect an app to a database                                              |
|                                                                               | -   Delete a [database](https://support.google.com/appsheet/answer/12636914)  |
|                                                                               |     or                                                                        |
|                                                                               |     [table](https://support.google.com/appsheet/answer/12725680#delete-table) |
|                                                                               | -   [Change the owner of a                                                    |
|                                                                               |     database](https://support.google.com/appsheet/answer/12637822)            |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

## Share a database with individual users

To share a database with individual users:

1.  [Open the database in the database editor](https://support.google.com/appsheet/answer/12632559).
2.  Click **Share**.
3.  Enter the email address of the individual user with whom you want to share your database, such as ahamilton@example.com.
4.  Repeat to share with additional users.
5.  Select one of the [database permissions](#database-permissions).
6.  Optionally, click **Copy link to database** to share with users.
7.  Click **Save**.

## Share a database with the database owner's team

Team members are not notified when a database is shared with a team. You can view the databases that are shared with your team, even if you haven't accessed them, by clicking the **Shared with me** filter on the [My Apps page](https://support.google.com/appsheet/answer/12392972).

To share a database with the database owner's team:

1.  [Open the database in the database editor](https://support.google.com/appsheet/answer/12632559).
2.  Click **Share**.
3.  Select one of the [database permissions](#database-permissions) for **Everyone in the owner's team**. 
4.  Click **Save**.

## Manage permissions for individual users

To change the owner, see [Change the owner of a database](https://support.google.com/appsheet/answer/12637822).

To manage permissions for individual users:

1.  [Open the database in the database editor](https://support.google.com/appsheet/answer/12632559).
2.  Click **Share**.
3.  Change the [database permissions](#database-permissions) for an individual user.
4.  Click **Save**.

## Send users a link to a database

To send users a link to your database:

1.  [Open the database in the database editor](https://support.google.com/appsheet/answer/12632559).
2.  Click **Share**.
3.  Click **Copy link to database**.
4.  Click **Done**.
5.  Send the link to users using your preferred method.

## Restrict external database sharing

Restrict the sharing of AppSheet databases to only emails or domains internal to the domain belonging to the app owner's organization. For an [AppSheet organization](https://support.google.com/appsheet/answer/13691133), this includes all secondary domains managed by the parent Google Workspace account, if applicable.

Restrict external database sharing:

1.  Access the Policies page by selecting one of the following:
    - **Admin \> Policies** in the top navigation 
    - **Policies** from the account profile drop-down
2.  Select the scope, **Team** or **Account**.
3.  Click **+ Account Policy** or **+ Team Policy** to add an account or team policy, respectively.
4.  Select **Restrict external database sharing** from the **Policy Template** drop-down.
5.  Click **Next**.
6.  The policy is preconfigured for you. You can modify any of the field values. See [Add a predefined policy](https://support.google.com/appsheet/answer/11948767#add-predefined-policy) for a description of each field. 
    **Important**: If you modify the **Condition** field, ensure that you retain the functionality defined below:
    `NOT([IsSharedExternally])` 
7.  Click **Save**.
