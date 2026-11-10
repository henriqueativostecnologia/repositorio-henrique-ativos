---
fonte: https://support.google.com/appsheet/answer/12282002?hl=en
baixado: 2026-11-10
---

# Restrict sharing of apps

Restrict the number of users an app creator can share an app with using the following governance policies:

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Policy**                                                                    | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Require direct sharing                                                        | Requires that access is only granted to users explicitly shared to an app in  |
|                                                                               | the [*sharing                                                                 |
|                                                                               | dialog*](ht                                                                   |
|                                                                               | tps://support.google.com/appsheet/answer/10104983#share-restricted-audience). |
|                                                                               | Only [*individual                                                             |
|                                                                               | users*                                                                        |
|                                                                               | ](https://support.google.com/appsheet/answer/10104983#share-individual-users) |
|                                                                               | users added directly to an app can access it, ensuring that sign-in is        |
|                                                                               | required and all access is explicitly managed through the sharing dialog.     |
|                                                                               | Restricts app access as follows:                                              |
|                                                                               |                                                                               |
|                                                                               | -   [Require user                                                             |
|                                                                               |     sign-in](https://support.google.com/appsheet/answer/10104975)             |
|                                                                               | -   Prevent all signed-in users from accessing the app (disable [Allow all    |
|                                                                               |     signed-in                                                                 |
|                                                                               |                                                                               |
|                                                                               |  users](https://support.google.com/appsheet/answer/10104983#share-signed-in)) |
|                                                                               | -   Disable [Require domain                                                   |
|                                                                               |     authentication](https                                                     |
|                                                                               | ://support.google.com/appsheet/answer/10104381#require-domain-authentication) |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Restrict app sharing                                                          | Restricts app sharing as follows:                                             |
|                                                                               |                                                                               |
|                                                                               | -   Prevents the sharing of apps with an entire domain using the Share dialog |
|                                                                               | -   Limits the number of users that the app can be shared with using the      |
|                                                                               |     Share dialog (defaults to 5, but can be customized)                       |
|                                                                               |                                                                               |
|                                                                               | See also: [Share: The                                                         |
|                                                                               | Essentials](https://support.google.com/appsheet/answer/10104983)              |
|                                                                               |                                                                               |
|                                                                               | The Restrict app sharing policy applies to the app itself and doesn't         |
|                                                                               | necessarily restrict automation events that are triggered by changes made to  |
|                                                                               | external sources (e.g., automations triggered by submissions to a Google Form |
|                                                                               | by external users).                                                           |
|                                                                               |                                                                               |
|                                                                               | App creators can configure their apps in ways that prevent AppSheet from      |
|                                                                               | identifying who is triggering the automation event. It is always the app      |
|                                                                               | creator's responsibility to ensure that external sources comply with their    |
|                                                                               | organizational rules and policies as well as AppSheet terms of service        |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

For example, the following error is returned if the number of users in the domain exceeds the maximum number of users the app can be shared with.

Share app dialog showing the Restrict Prototype Sharing error message

**Notes**:

- To fully restrict sharing, **both policies must be set and active.** 
- You can  restrict sharing of all, prototype, or deployed apps by adjusting the **Target** setting to **All Apps**, **Prototype Apps**, or **Deployed Apps**, respectively.
- Existing apps will continue to function for users until they attempt an activity that is in violation of the policy. For example, if a user attempts to save an app that has been shared with more than 5 users, they will need to reduce the number of shared users (to 5 or below) in the Share dialog before they can save the app. 

To restrict sharing of apps:

1.  Access the Policies page by selecting one of the following:
    - **Admin \> Policies** in the top navigation 
    - **Policies** from the account profile drop-down
2.  Select the scope, **Team** or **Account**.
3.  Click **+ Account Policy** or **+ Team Policy** to add an account or team policy, respectively.
4.  Select **Require direct sharing** from the **Policy Template** drop-down.
5.  Click **Next**.
6.  The policy is preconfigured for you. You can modify any of the field values. See [Add a predefined policy](https://support.google.com/appsheet/answer/11948767#add-predefined-policy) for a description of each field. 
    **Important**: If you modify the **Condition** field, ensure that you retain the functionality defined below:
    `AND([AuthRequired] = true, [DomainAuthRequired] = false, [AllowAllSignedInUsers] = false)` 
7.  Click **Save**.
8.  Click **+ Account Policy** or **+ Team Policy** to add an account or team policy, respectively.
9.  Select **Restrict app sharing** from the **Policy Template** drop-down.
10. Click **Next**.
11. The policy is preconfigured for you. You can modify any of the field values. See [Add a predefined policy](https://support.google.com/appsheet/answer/11948767#add-predefined-policy) for a description of each field. 
    **Important**: If you modify the **Condition** field, ensure that you retain the functionality defined below:
    `AND(COUNT([Users]) <= 5, COUNT([AllowListDomains]) = 0)` 
12. Click **Save**.
