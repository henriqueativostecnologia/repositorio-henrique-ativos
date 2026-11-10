---
fonte: https://support.google.com/appsheet/answer/14368331?hl=en
baixado: 2026-11-10
---

# Assign AppSheet admin privileges to Google Workspace admins

This method of assigning admin privileges takes precedence over the [role assignment in the AppSheet organization](https://support.google.com/appsheet/answer/13690945#assign-roles).

Assign AppSheet admin privileges to Google Workspace admins as described in the following sections:

- [Auto-assignment of AppSheet admin privileges (AppSheet Enterprise Plus only)](#auto-assignment)
- [Assign AppSheet admin privileges by using the Google Admin console](#assign)
- [Assign AppSheet admin privileges without using the Google Admin console](#assign-without-console)

The following table compares the features available in the AppSheet Admin Console for Google Workspace admins with AppSheet admin privileges based on whether they have an AppSheet Enterprise Plus license or not. For more information, see [Manage using the AppSheet Admin Console](https://support.google.com/appsheet/topic/14951414).

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **AppSheet service privilege +\                                               | **AppSheet service privilege**                                                |
| AppSheet Enterprise Plus**                                                    |                                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Full access to AppSheet Admin Console, including:                             | Access to the following features in the AppSheet Admin Console:               |
|                                                                               |                                                                               |
| -   View overview and summary pages                                           | -   View overview and summary pages                                           |
| -   View account detail and app detail pages                                  |                                                                               |
| -   Transfer, copy, or delete apps                                            | **Doesn't include **the following features in the AppSheet Admin Console:     |
| -   Set governance policies                                                   |                                                                               |
| -   Configure all team settings                                               | -   View account detail or app detail page                                    |
|                                                                               | -   Transfer, copy, or delete apps                                            |
|                                                                               | -   Set governance policies                                                   |
|                                                                               | -   Configure all team settings                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

## Auto-assignment of AppSheet admin privileges (AppSheet Enterprise Plus only)

AppSheet [organization administrator](https://support.google.com/appsheet/answer/13691133#supported-roles) privileges are automatically assigned to Google Workspace admins with: 

- AppSheet Enterprise accounts
- [AppSheet service admin privileges](https://support.google.com/a/answer/1219251) (as defined by Google Workspace)

**Super Admins** and **Service Admins** include AppSheet service admin privileges, by default. See [Prebuilt administrator roles](https://support.google.com/a/answer/2405986).

For the full set of privileges, see team root in [Supported roles for an AppSheet organization and teams](https://support.google.com/appsheet/answer/13691133#supported-roles).

## Assign AppSheet admin privileges by using the Google Admin console

Assign AppSheet admin privileges, specifically [AppSheet service admin privileges](https://support.google.com/a/answer/1219251), to Google Workspace admins by using the Google Admin console.

To assign AppSheet admin privileges by using the Google Admin console, do the following steps:

1.  Navigate to the Google Admin console.

2.  Assign AppSheet admin privileges to the user by using one of the following methods:

    - Assign a prebuilt system role that has [AppSheet service admin privileges](https://support.google.com/a/answer/1219251). By default, **Super Admins** and **Service Admins** include AppSheet service admin privileges. See [Prebuilt administrator roles](https://support.google.com/a/answer/2405986).
    - Create and assign a custom role that has [AppSheet service admin privileges](https://support.google.com/a/answer/1219251). In this case, you need to create the role first. Go to [Create a custom role](https://support.google.com/a/answer/2406043#create).

    For more information, see [Assign specific admin roles](https://support.google.com/a/answer/9807615). 

## Assign AppSheet admin privileges without using the Google Admin Console 

If you don't have access to the Google Admin console, you can sign up for Cloud Identity Free and then assign the [AppSheet service admin privileges](https://support.google.com/a/answer/1219251) to the appropriate user. 

Complete the following steps to gain access to the Google Admin console and assign AppSheet admin privileges:

1.  Create an admin account using Cloud Identity Free:
    1.  Go to the [Cloud Identify Free sign-up page](https://workspace.google.com/gcpidentity/signup?sku=identitybasic).

        Cloud Identity Free wizard
    2.  Step through the instructions to [create your Cloud Identity account and first time admin user](https://support.google.com/cloudidentity/answer/7390066).
    3.  [Verify ownership](https://support.google.com/a/answer/60216) of the specified domain.
2.  Sign in to the Google Admin Console using the admin user account.
3.  [Assign one license](https://support.google.com/a/answer/1727173) to the appropriate user account.
    For full monitoring and governance capabilities, make sure to assign an AppSheet Enterprise Plus license.
4.  Assign AppSheet admin privileges to the user by using one of the following methods:
    - Assign a prebuilt system role that has [AppSheet service admin privileges](https://support.google.com/a/answer/1219251). By default, **Super Admins** and **Service Admins** include AppSheet service admin privileges. See [Prebuilt administrator roles](https://support.google.com/a/answer/2405986).
    - Create and assign a custom role that has [AppSheet service admin privileges](https://support.google.com/a/answer/1219251). In this case, you need to create the role first. Go to [Create a custom role](https://support.google.com/a/answer/2406043#create).

For more information, see [Assign specific admin roles](https://support.google.com/a/answer/9807615)
