---
fonte: https://support.google.com/appsheet/answer/10104696?hl=en
baixado: 2026-11-10
---

# Limit users to particular tables, views, and actions

We have already seen that an app can show different data or presentation to users based on their identity or settings. In some situations, you may also want the app to provide different or restricted functionality to certain classes of users. There are three distinct cases to consider:

1.  There are a small number of user classes (typically just two, for example, such as regular users and admins). One user class needs a few extra features exposed. 
2.  There are a small number of user classes but they need very different capabilities.
3.  There are a large number of user classes, each requiring very different capabilities.

For cases 2 and 3, the answer in AppSheet is to build a different apps for each class of users. It is easy to build multiple apps which use the same underlying data. You can control data change permissions, as described in [Control add, update, and delete operations](https://support.google.com/appsheet/answer/10106345). However, you will need to manage these different apps.

Case 1 is pretty common and in this case, you may wish to have different types of functionality per user class. At the app level, there are different ways to differentiate user classes. For example:

1.  **Control what fields a user can view or update in a table or a slice**. Instead of statically defining whether someone can view or update (Add/Edit/Delete/ReadOnly) a column in the table definition, define the `Show?` and `Editable?` expressions in the [column properties](https://support.google.com/appsheet/answer/10106509#column-properties).
2.  **Control which views are shown to the user.** Use the [`Show if` constraint expression](https://support.google.com/appsheet/answer/10106688#show-if) as part of the view definition.
3.  **Control which actions a user can invoke.** Configure the **Only if this condition is true** setting in the [Behavior](https://support.google.com/appsheet/answer/10107706#behavior) section for an action to control which rows show the action.

In these expressions, the email of the current user ([`USEREMAIL()`](https://support.google.com/appsheet/answer/10108210)) or options defined in the user settings ([`USERSETTINGS()`](https://support.google.com/appsheet/answer/10108291)) should be used to differentiate users into appropriate user classes. For example, to dynamically control the update mode of the table, here is a sample expression to control user access permissions based on the user's email. See [`SWITCH()`](https://support.google.com/appsheet/answer/10107700).

`SWITCH(USEREMAIL(),`
`"admin@mycompany.com", "ALL_CHANGES",`
`"manager@mycompany.com", "UPDATES_ONLY",`
`"READ_ONLY")`
