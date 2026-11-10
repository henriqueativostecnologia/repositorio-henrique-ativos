---
fonte: https://support.google.com/appsheet/answer/16563370?hl=en
baixado: 2026-11-10
---

# About licensing in AppSheet for organizations

If you own a private domain and have multiple users that need access to use AppSheet, those users can be managed centrally through an AppSheet organization. An AppSheet organization is automatically generated when you verify ownership of your domains through Google Workspace and provides a greater degree of monitoring and control of your users. It also provides additional licensing options to support a wide variety of deployments. For more information, see [About your organization and teams](https://support.google.com/appsheet/answer/13691133).

Learn more about licensing in AppSheet for organizations:

- [AppSheet license types for organizations](#types)
- [License rules for organizations](#rules)
- [License provisioning options for organizations](#provisioning-options)
- [Restrict user access](#restrict-access)
- [Additional notes](#additional-notes)

## AppSheet license types for organizations

Organizations have access to three license types that can be applied to internal and external users. Organizations are not required to have one license type for all of their users.

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **License**                                                                   | **Usage allowed**                                                             |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| AppSheet Core                                                                 | Build and use apps with Core features. AppSheet Core users are subject to     |
|                                                                               | AppSheet Core Security setting. See [Control access to AppSheet               |
|                                                                               | features](https://support.google.com/a/answer/16018438).                      |
|                                                                               |                                                                               |
|                                                                               | Many Google Workspace licenses include access to AppSheet Core. See [Which    |
|                                                                               | Google Workspace editions include AppSheet                                    |
|                                                                               | Core?](https://support.google.com/appsheet/answer/10105400#core-editions)     |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| AppSheet Enterprise Plus                                                      | Build and use apps with Enterprise features. AppSheet Enterprise Plus users   |
|                                                                               | are subject to [AppSheet governance                                           |
|                                                                               | policies](https://support.google.com/appsheet/answer/11948767), [team         |
|                                                                               | settings](https://support.google.com/appsheet/answer/11918568), and [app      |
|                                                                               | transfers](https://support.google.com/appsheet/answer/12007391).              |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| AppSheet User Pass                                                            | Use one app per license used. Users that consume a User Pass license are not  |
|                                                                               | independently subject to Core or Enterprise governance features. See [Allow   |
|                                                                               | app access with AppSheet User                                                 |
|                                                                               | Pass](https://support.google.com/appsheet/answer/15657053).                   |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

## License rules for organizations 

The following lists the license rules for organizations. To learn more about monitoring the licenses used by your organization, see [View the licenses purchased, assigned, and used in your team or organization](https://support.google.com/appsheet/answer/14960110).

- AppSheet Core and AppSheet Enterprise Plus licenses grant a user the ability to build, share, and use AppSheet apps within their respective license tier unless otherwise restricted by their admin.
- A license is used anytime someone accesses an app owned by a member of your organization. The license required to use an app depends exclusively on the app creator's license. AppSheet Core creators require users to have an AppSheet Core or AppSheet User Pass license. AppSheet Enterprise Plus creators require users to have an AppSheet Enterprise Plus or AppSheet User Pass license.
- External users including unauthenticated users of AppSheet apps owned by a member of your organization use the same license as the app owner. If AppSheet User Pass licenses have been purchased, external users can use that license as long as pooled licensing has not been enabled for all app users of the organization.
- Once used, a license remains with the user through the end of the calendar month unless the user consumes a license from a higher tier (Core \< User Pass \< Enterprise).
- Your organization will not be charged for excess usage, but user access may be restricted after consecutive months where your organization's usage exceeds the licenses purchased. If your organization exceeds the number of licenses purchased, you can view [*license warnings*](https://support.google.com/appsheet/answer/16003327) in the AppSheet Admin Console.

## License provisioning options for organizations 

The following lists the license provisioning options for organizations. See also [How AppSheet Enterprise Plus licenses are provisioned](https://support.google.com/appsheet/answer/14101111).

|                                                                                              |                                                                                                                                                                                                                                                                                   |
|----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Licensing option**                                                                         | **Description**                                                                                                                                                                                                                                                                   |
| [Assigned licensing](https://support.google.com/appsheet/answer/14101111#assigned-licensing) | Users are assigned AppSheet Core or AppSheet Enterprise Plus using the Google Admin Console.                                                                                                                                                                                      |
| [Pooled licensing](https://support.google.com/appsheet/answer/14101111#pooled-licensing)     | Users are automatically granted an AppSheet Enterprise Plus or AppSheet User Pass license when they sign in to AppSheet. Admins can turn pooled licensing on using the AppSheet Admin Console  Access can be granted to every app user or limited to a Google or Microsoft group. |

## Restrict user access

The following lists the methods available to restrict user access. See also How to limit [AppSheet license consumption](https://support.google.com/appsheet/answer/15990700).

|                                |                                   |                                                                                                                                                                                                                                                                                                                    |
|--------------------------------|-----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Restrict user access**       | **Methods**                       | **Description**                                                                                                                                                                                                                                                                                                    |
| All users                      | License provisioning              | You can assign licenses to users directly or through organization units in the Google Admin Console to limit who can build and use apps built by members of your organization. See [Manage AppSheet licenses](https://support.google.com/a/answer/10569787).                                                       |
|                                | AppSheet service setting (on/off) | You can turn access to AppSheet service on or off for any user in your Workspace organization. Only Workspace users with the service turned on will use a license. See [Turn AppSheet on or off for users](https://support.google.com/a/answer/10216943).                                                          |
| AppSheet Core users            | Core Security setting             | You can restrict app sharing with users outside of your organization. Only users within your organization will use an AppSheet Core license. See [Control access to AppSheet features](https://support.google.com/a/answer/16018438).                                                                              |
| AppSheet Enterprise Plus users | AppSheet policies                 | You can use AppSheet policies for fine grain controls on access to any app, creator or user. These restrictions will prevent a user from using any features or apps that you specify. See [Define governance policies](https://support.google.com/appsheet/answer/11948767).                                       |
|                                | Pooled license group              | You can use a pooled license group to restrict who can build and use AppSheet Enterprise. Users outside of the group will not be permitted to use an enterprise license. See [Turn on or off pooled licensing for AppSheet Enterprise Plus](https://support.google.com/appsheet/answer/15617758#pooled-licensing). |
|                                | App creator group                 | You can restrict which users in your organization are allowed to build apps. See [Restrict who can create apps](https://support.google.com/appsheet/answer/11918568#restrict-create-apps).                                                                                                                         |

## Additional notes

Note the following: 

- In contrast to licensing for individual accounts where licenses are managed through [*appsheet.com*](http://appsheet.com) on the Billing tab, licensing for organizations is managed through Google Workspace exclusively.
- Customers should not have individual and organization billing at the same time to avoid paying for users multiple times.
- It is highly recommended that customers that assign their licenses [turn off pooled licensing](https://support.google.com/appsheet/answer/15617758#pooled-licensing) to avoid confusion about the license source for each user. 
- There are some cases where enterprise features are exposed to core creators. The AppSheet team is aware and will notify creators before any restrictions are implemented.
