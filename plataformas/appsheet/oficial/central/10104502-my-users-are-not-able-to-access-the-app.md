---
fonte: https://support.google.com/appsheet/answer/10104502?hl=en
baixado: 2026-11-10
---

# My users are not able to access the app

If a user can't access your app, it might be due to one of the following issues:

- [User doesn't have permission to access app](#user-permission)
- [App is not runnable](#app-not-runnable)
- [One or more tables in the app require "as app user" access](#as-app-user-access)

## User doesn't have permission to access app

This can occur if one or more of the following are true:

- You have required user authentication for your app and the user's email doesn't match any entry in the user allow list for the app. The email address associated with the user's sign-in account must match the email address in the allow list. See [Share: The Essentials](https://support.google.com/appsheet/answer/10104983).

- A [team shared resource](https://support.google.com/appsheet/answer/10104795), such as a data source or auth domain, is no longer available. This can occur if the team root or admin removed access to the team shared resource or if the app user is not in the same group-based team as the shared resource. In this case, the following error message is returned when accessing the app: 
  `User XXXXX does not have access to data source`

- You've [defined your team membership using a Google Group](https://support.google.com/appsheet/answer/13964712#google-group), but the app owner doesn't have permission to view other members in the Google Group. AppSheet recommends giving the **entire organization** permission to view other members, as shown:

  Google group view member settings

## App is not runnable 

When there's an error in the app definition, the user will see a message indicating the app isn't runnable, with direction to contact the app creator. As the app creator, to resolve the issue [view the errors and warnings in the app editor](https://support.google.com/appsheet/answer/14217425) and go to the problem.

See also: [Error: The App is not runnable](https://support.google.com/appsheet/answer/10104803)

## One or more tables in the app require "as app user" access

This occurs when there's a security option you may have explicitly enabled. If you do so, the user's account must have permissions to access the underlying data for the table (such as, a spreadsheet in cloud storage). Often, app creators invite a user to try their app but forget to give the user appropriate permissions. For this reason, we recommend the **Use app** app permissions be used sparingly and only when absolutely necessary. See [Set access mode as app creator or app user](https://support.google.com/appsheet/answer/10105756).
