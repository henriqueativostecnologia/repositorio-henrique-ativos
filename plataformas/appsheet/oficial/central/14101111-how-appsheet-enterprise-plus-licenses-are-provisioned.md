---
fonte: https://support.google.com/appsheet/answer/14101111?hl=en
baixado: 2026-11-10
---

# How AppSheet Enterprise Plus licenses are provisioned

Learn how AppSheet Enterprise licenses are provisioned.

- [Overview of AppSheet Enterprise licensing models](#oveview)
- [Benefits of assigned licensing](#benefits)
- [Comparison of features with each licensing model](#compare-models)

See also [About licensing in AppSheet for organizations](https://support.google.com/appsheet/answer/16563370).

## Overview of AppSheet Enterprise Plus licensing models

AppSheet Enterprise Plus licenses are provisioned in one of the following ways:

- [Assigned licensing (default model)](#assigned-licensing)
- [Pooled licensing](#pooled-licensing)
- [Team licensing (legacy model](#team-licensing))

### Assigned licensing (default model)

AppSheet Enterprise Plus customers with an existing Google Workspace account are required to assign licenses through the Google Admin console. See [Assign AppSheet licenses to users](https://support.google.com/a/answer/10569787).

If a Google Workspace user account hasn't been assigned an AppSheet Enterprise Plus license, then they retain their [AppSheet Core entitlement](https://support.google.com/appsheet/answer/10105400#core-editions), if applicable, or can use AppSheet for [free](https://support.google.com/appsheet/answer/10104499).

### Pooled licensing

Pooled licensing allows your AppSheet Enterprise Plus licenses to be granted to users when they sign in to AppSheet, eliminating the need to [assign licenses](#assigned-licensing) in the Google Admin Console.

You can define the **groups** of users that are allowed to use your pooled AppSheet Enterprise Plus licenses. By default, when pooled licensing is turned on, every user in your organization (that is, all the users that share your [verified domains](https://support.google.com/a/answer/60216)), will be granted an AppSheet Enterprise Plus license when they sign in. If you need to limit the number of users from your domain that have the ability to consume your AppSheet Enterprise Plus licenses, you can designate a group of users that are eligible to use your AppSheet Enterprise Plus licenses.

Changes to pooled licensing will take effect within 24 hours.

Because reporting on the Used tab of the [Licenses](https://support.google.com/appsheet/answer/14960110) page is historical, any changes made to your pooled licensing group won't cause any existing warnings to be removed until the following month. 

User within the selected scope can include:

- Users that have an AppSheet Core entitlement through their Workspace subscription
- Users that authenticate through non-Google sources
- Users that don't have any other paid Workspace license

You can track the consumption of AppSheet Enterprise Plus licenses on the [Licenses page](https://support.google.com/appsheet/answer/14960110) of the AppSheet Admin Console.

Before you turn on pooled licensing, ensure the following is true:

- You have AppSheet Enterprise Plus on an annual commit plan. Customers that have purchased AppSheet Enterprise Plus on a flex plan can't use pooled licensing.
- You have purchased AppSheet Enterprise Plus licenses for the expected number of *active users* in the calendar month. A user is considered active if they:
  - Access an AppSheet app
  - Edit an AppSheet app
  - Own an AppSheet app used by another user or with triggered or scheduled automations (regardless of whether the app owner has signed in to the AppSheet editor in the calendar month)

To turn on or off pooled licensing, see [Turn on or off pooled licensing for AppSheet Enterprise Plus](https://support.google.com/appsheet/answer/15617758#pooled-licensing).

**Note the following**:

- When pooled licensing is turned on, allowed users will be granted AppSheet Enterprise Plus when they sign in. However, only active users of your licenses for the calendar month are counted against the pool of purchased licenses reported in the AppSheet Admin Console.
- You can have pooled licensing turned on and still [assign licenses](#assigned-licensing) in the Google Admin Console.
- Unauthenticated users and users external to your Workspace organization that access apps created by the app creators in your organization can consume an AppSheet Enterprise Plus license.
- Because AppSheet will assign AppSheet Enterprise Plus licenses to users automatically, it's possible to exceed the number of AppSheet Enterprise Plus licenses purchased. 

### Team licensing (legacy model)

The legacy approach to provisioning AppSheet Enterprise Plus provides access to all users in the customer’s [verified domain](https://support.google.com/a/answer/60216).

Any user that shares the customer's domain in their email address gets access to AppSheet Enterprise Plus regardless of license assignment in the Google Admin console.

Legacy customers and non-Workspace customers can remain on the team licensing model, or can work with their [AppSheet Sales](https://cloud.google.com/contact/?direct=true&pre_product=appsheet) representative to switch to assigned licensing using the Google Admin console.

## Benefits of assigned licensing

Benefits of assigned licensing include the ability to do the following:

- Control access to the AppSheet Enterprise Plus subscription.
- Review and manage billing in the Google Admin console.
- Automatically assign licenses to organizational units, as required.
- Enable a dual-license environment (for example, AppSheet Core and AppSheet Enterprise Plus users).

## Comparison of features with each licensing model

The following table compares AppSheet features and their behaviors with each licensing model.

+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| **Feature**                           | **Assigned licensing**                | **Pooled licensing**                  | **Team licensing**                    |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| App creation and sharing              | Only users that have been assigned a  | Any user from your Google Workspace   | All users that share a domain with    |
|                                       | license have access to AppSheet       | [verified                             | the root admin have access to the     |
|                                       | Enterprise Plus.                      | domains](https://s                    | same AppSheet Enterprise Plus         |
|                                       |                                       | upport.google.com/a/answer/60216)have | entitlement.                          |
|                                       | App creators can share licenses with  | access to AppSheet Enterprise Plus    |                                       |
|                                       | users using the                       | when they sign in to AppSheet.        | App creators can share licenses with  |
|                                       | [Share](https://support               |                                       | users using the                       |
|                                       | .google.com/appsheet/answer/10104983) | App creators can share licenses with  | [Share](https://support               |
|                                       | dialog. It's up to the Workspace      | users using the                       | .google.com/appsheet/answer/10104983) |
|                                       | admin to ensure that they have the    | [Share](https://support               | dialog. It's up to the admin to       |
|                                       | required licenses.                    | .google.com/appsheet/answer/10104983) | ensure that they have the required    |
|                                       |                                       | dialog. It's up to the Workspace      | licenses.                             |
|                                       |                                       | admin to ensure that they have        |                                       |
|                                       |                                       | expected purchased licenses for the   |                                       |
|                                       |                                       | number of expected *active users* in  |                                       |
|                                       |                                       | the calendar month.                   |                                       |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| Access and billing                    | Customers on a **commit** plan are    | Customers on a **commit** plan are    | Customers on a **commit** plan are    |
|                                       | billed for a pre-negotiated number of | billed for a pre-negotiated number of | billed for the pre-negotiated number  |
|                                       | users regardless of usage.            | users regardless of usage.            | of users regardless of usage          |
|                                       |                                       |                                       |                                       |
|                                       | Customers on a **flex** plan are      | Not supported for customers on a      | Customers on a **flex** plan are      |
|                                       | billed for assigned licenses; only    | **flex** plan.                        | billed for assigned licenses; but any |
|                                       | users that have been assigned a       |                                       | user within the customer’s domain can |
|                                       | license can access and use AppSheet   |                                       | access and use AppSheet Enterprise    |
|                                       | Enterprise Plus.                      |                                       | Plus.                                 |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| Governance                            | You shouldn't expect to be able to    | You can govern (that is, enforce      | All users in a customer’s domain,     |
|                                       | govern (that is, enforce policies,    | policies, apply team settings, and so | regardless of the AppSheet Enterprise |
|                                       | apply team settings, and so on) users | on) users that are assigned an        | Plus license assignment, are subject  |
|                                       | that are not assigned an AppSheet     | AppSheet Enterprise Plus license.     | to governance policies and team       |
|                                       | Enterprise Plus license. For legacy   |                                       | management settings.                  |
|                                       | reasons, this restriction may not     |                                       |                                       |
|                                       | always be enforced, but to reliably   |                                       | Users that have AppSheet Core are     |
|                                       | govern a set of users they all need   |                                       | also subject to the policies and team |
|                                       | to be upgraded to AppSheet Enterprise |                                       | management settings defined by the    |
|                                       | Plus.                                 |                                       | admin with AppSheet Enterprise Plus.  |
|                                       |                                       |                                       |                                       |
|                                       | Users that have AppSheet Core are     |                                       |                                       |
|                                       | also subject to the policies and team |                                       |                                       |
|                                       | management settings defined by the    |                                       |                                       |
|                                       | admin with AppSheet Enterprise Plus.  |                                       |                                       |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
