---
fonte: https://support.google.com/appsheet/answer/11948767?hl=en
baixado: 2026-11-10
---

# Define governance policies

When you start creating multiple apps, either as an individual app creator or as a member of a team or organization, there are typically constraints and guidelines that should be applied to every app created. **App governance policies** are the means by which to express these constraints and guidelines.

The typical reasons to set up app policies are:

- Design consistency
- Corporate compliance

Manage policies as described in the following sections:

- [What is a policy?](#what-is)
- [Who can add policies?](#who-can-add)
- [When are policies auto applied in the app editor?](#auto-apply)
- [Access the Policies page](#access-policies-page)
- [Add a predefined policy](#add-predefined-policy)
- [Add a custom policy](#add-custom-policy)
- [Configure the policy](#configure-policy)
- [Review policy compliance](#policy-compliance)
- [Edit a policy](#edit-policy)
- [Delete a policy](#delete-policy)

## What is a policy?

A policy is a rule that limits how AppSheet apps are created, managed, and distributed. For example, policies might define the following limits:

- Every app must require users to sign in.
- Data can't be deleted though an AppSheet app.
- Only certain people can mark apps as deployed.
- Apps can only be shared to a specific email domain.

Policies can be applied at the organization, team, or individual level.

When you [configure a policy](#configure-policy), you define three important components:

- **Condition**: A constraint that is checked on each app. See also [Condition expression reference for governance policies](https://support.google.com/appsheet/answer/13265290). 
- **Severity**:  Error or warning. This tells the platform how to handle the condition if not satisfied. 
- **Stage**: When should the policy be checked? 

There are also some other options, including descriptive messages

You can add a [predefined policy](#add-predefined-policy) or a [custom policy](#add-custom-policy). See also [Predefined policy templates](https://support.google.com/appsheet/answer/13390789).

## Who can add policies?

- Any individual AppSheet user account has permission to add individual policies.
- Team root and team admin accounts can create and manage team policies, and can view organization policies.
- Organization admin accounts can create and manage organization and team policies.

Organization-level policies take precedence over team-level policies, but do act as "and" clauses for team policies that have the same target (component). AppSheet will always apply the **most restrictive** policy statement that can be produced when combining the conditions of organization and team policies on the same component. 

For example:

- If an organization policy restricts all external users and team A’s policy restricts external users only from `foo.com`, then all external users are restricted for all users in the organization.

- If a organization policy restricts external users from `foo.com` and team A’s policy restricts all external users, then all external users are restricted for members of team A and only external users from `foo.com` are restricted for other teams (B, C, and so on).

Suggestions:

- When you add a policy, start by defining a lower severity level (such as Warning), so you don't immediately block users that may already be out of compliance. This is important if you want to preserve the availability of the apps they created.
- Experiment with the predefined policies. If you want to define a policy that is not predefined, try using the custom policies. Contact [AppSheet Support](https://www.appsheet.com/Support/Contact) if you need assistance. 

**Note**: Existing apps will continue to function for users until they attempt an activity that is in violation of the policy. If you want a policy to take effect right away, set [Stage](#stage) to **Enforce always**.

## When are policies auto applied in the app editor?

AppSheet auto applies a policy on app editor load if the [Condition](#condition) setting is defined using the following format: `[`*`field`*`] = `*`constant`*` `This includes policies whose Condition setting contains multiple `[`*`field`*`] = `*`constant` *statements that are combined together in an `AND` function.

For example, the Require sign-in policy has the following condition:

    [AuthRequired] = true

This condition will be auto applied in your app and turn on (and prevent you from changing) the [Require user signin?](https://support.google.com/appsheet/answer/10104975#how-to) setting in the app editor. 

Similarly, the Enforce FedRAMP compliance policy has the following condition:

    AND(
       [EnableFirebase]=false,
       [EnableMapsAndGeocoding]=false,
       [ScanningServiceName]="System Default: Google MLKit"
    )

The condition will be auto applied and configure (and prevent you from changing) the following [External service](https://support.google.com/appsheet/answer/10104999/appsheet/answer/10104999#external-services) settings:

- Turn off the **Allow Firebase** setting to prevent the use of [Firebase for branding apps](https://support.google.com/appsheet/answer/10104711)
- Turn off the **Allow maps and geocoding** setting to prevent the use of [maps and geocoding](https://support.google.com/appsheet/answer/10106601)
- Restrict the **Barcode/QRcode scanning service** setting to **System Default** to prevent the use of external [barcode scanners](https://support.google.com/appsheet/answer/10106618#enable)

## Access the Policies page

Organizations are only supported for **Google Workspace** users with **AppSheet Enterprise** accounts. Teams are only supported for users with **AppSheet Enterprise** accounts. See [AppSheet pricing](https://about.appsheet.com/pricing/).

Access the Polices page to view and manage the policies that are in effect for your account, team, or organization by opening the AppSheet app editor:

- **Admin \> Policies** in the top navigation 
- **Policies** from the account profile drop-down

In addition, AppSheet admins can select **Policies** in the left navigation of the [AppSheet Admin Console](https://support.google.com/appsheet/answer/14951726) (preview).

The Policies page displays.

Policies page showing account policies

As highlighted in the figure, the Policies page allows admins to:

- View the policies that are in effect for your account, team, or organization
- Add a new [predefined](#add-predefined-policy) or [custom](#add-custom-policy) policy for your account, team, or organization
- [Edit](#edit-policy) or [delete](#delete-policy) a policy

Only organization admin accounts can add, edit, or delete organization policies. Only organization admin, team root, or team admin accounts can add, edit, or delete team policies.

## Add a predefined policy

To add a predefined policy:

1.  [Access the policies page](#access-policies-page).
2.  Select the scope: **Organization**, **Team**, or **Account**.
3.  Click **+ Organization policy**,  **+ Team Policy**, or **+ Account Policy** to add an organization, team, or account-specific policy, respectively.
4.  Select a [*predefined policy template*](https://support.google.com/appsheet/answer/13390789) from the **Policy Template** drop-down.
5.  Click **Next**.
6.  [Configure the policy](#configure-policy).
7.  [Review policy compliance](#policy-compliance).
8.  Click **Save**.

## Add a custom policy

The custom policy template lets you create a rule based on a specific component of the AppSheet service. 

To create a custom policy:

1.  [Access the policies page](#access-policies-page).
2.  Select the scope, **Organization**, **Team**, or **Account**.
3.  Click **+ Organization policy**,  **+ Team Policy**, or **+ Account Policy** to add an organization, team, or account-specific policy, respectively.
4.  Select **Custom policy** from the **Policy Template** drop-down.
5.  Click **Next**.
6.  [Configure the policy](#configure-policy).
7.  [Review policy compliance](#policy-compliance).
8.  Click **Save**.

## Configure the policy

Configure the policy settings described in the following table.

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Setting**                                                                   | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Name                                                                          | Name of the policy that will appear on the Policies page.                     |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Component                                                                     | Custom policies only. Select the AppSheet component impacted by the custom    |
|                                                                               | policy. Almost every aspect of the app definition can be governed by          |
|                                                                               | policies.                                                                     |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Condition                                                                     | Constraint that is checked on each app. For the predefined templates, the     |
|                                                                               | condition is defined. For example, the **Require sign-in policy** has the     |
|                                                                               | condition: `[AuthRequired] = true`                                            |
|                                                                               |                                                                               |
|                                                                               | Modify the condition expression, if required.                                 |
|                                                                               |                                                                               |
|                                                                               | For a list of column names that you can include in the condition expression   |
|                                                                               | and the list of functions that are not supported for use in the condition     |
|                                                                               | expression, see [Condition expression reference for governance                |
|                                                                               | policies](https://support.google.com/appsheet/answer/13265290).               |
|                                                                               |                                                                               |
|                                                                               | **Note**: The syntax for conditions is identical to the expression syntax     |
|                                                                               | used in the rest of AppSheet.                                                 |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Severity                                                                      | Flag that specifies how to handle the condition if not satisfied. Valid       |
|                                                                               | values are **Error** or **Warning**.                                          |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Target                                                                        | Apps that are targeted by the policy. Valid values include **All Apps**,      |
|                                                                               | **Prototype Apps**, or **Deployed Apps**.                                     |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Stage                                                                         | Stage that the policy should be checked. Valid values include:                |
|                                                                               |                                                                               |
|                                                                               | -   **Check on App Edit **- Flags non-compliant behavior when the app is      |
|                                                                               |     edited.                                                                   |
|                                                                               | -   **Check on Deployment **- Flags non-compliant behavior when the app is    |
|                                                                               |     deployed.                                                                 |
|                                                                               | -   **Enforce always** - Flags non-compliant behavior at runtime as soon as   |
|                                                                               |     the policy is saved.                                                      |
|                                                                               |                                                                               |
|                                                                               | Enforce always is the default for most policies. However, for a subset of     |
|                                                                               | policies, Check on Deployment may be more appropriate to make                 |
|                                                                               | sure an activity is completed before the app is deployed (such as, Apps must  |
|                                                                               | have documentation).                                                          |
|                                                                               |                                                                               |
|                                                                               | Note the following:                                                           |
|                                                                               |                                                                               |
|                                                                               | -   Do not set this value to **Check on Deployment** if **Target** is set to  |
|                                                                               |     **Deployed Apps**.                                                        |
|                                                                               | -   If Stage is set to **Enforce always:**                                    |
|                                                                               |     -   It can take up to 15 minutes before the policy is enforced.           |
|                                                                               |     -   At this time, apps that use files or images may not be completely     |
|                                                                               |         shut down. Contact [AppSheet                                          |
|                                                                               |         Support](https://www.appsheet.com/Support/Contact) if you need        |
|                                                                               |         assistance.                                                           |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Description                                                                   | Description of the policy that will appear on the Policies page.              |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Success Message                                                               | Message to be displayed if policy is successfully adhered to.                 |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Failure Message                                                               | Message to be displayed if the policy is violated.                            |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

## Review policy compliance

When you [configure the policy](#configure-policy), in the right pane of the Define an App Policy dialog, you can review policy compliance to confirm the results are as expected for each [version](https://support.google.com/appsheet/answer/10104708) (latest and stable) of your app before you save the policy. 

For example:

Policy check showing compliant and non-compliant apps

As shown, apps are organized into two categories: **Non-compliant** and **Compliant. **For non-compliant apps, the impact to the app is dependent on the policy [severity](#severity) and [stage](#stage) settings.

|                     |                                                                                                                            |
|---------------------|----------------------------------------------------------------------------------------------------------------------------|
| **Policy severity** | **Description**                                                                                                            |
| Error               | App is prevented from being deployed or edited. The app may become unavailable to users if Stage is set to Enforce Always. |
| Warning             | Warning will be shown when deploying or editing the app.                                                                   |

If an app version is unexpectedly compliant or non-compliant, review the app or policy configuration to ensure that it is operating as originally intended.

To download policy compliance details for compliant or non-compliant policies, select  **More** **\> Export CSV **adjacent to the policy compliance header.

## Edit a policy

**Note**: You must have an organization admin account to be able to edit organization policies. You must have an organization admin, team root, or team admin account to be able to edit team policies.

To edit a policy:

1.  [Access the policies page](#access-policies-page).
2.  Select the scope: **Organization**, **Team**, or **Account**.
3.  Select More **\> Edit** for the policy you want to edit.
    The Define an App Policy dialog displays.
4.  Edit the [policy configuration](#configure-policy), as desired.
5.  [Review policy compliance](#policy-compliance).
6.  Click **Save**.

## Delete a policy

**Note**: You must have an organization admin account to be able to delete organization policies. You must have an organization admin, team root, or team admin account to be able to delete team policies.

To delete a policy:

1.  [Access the policies page](#access-policies-page).
2.  Select the scope: **Organization**, **Team**, or **Account**.
3.  Select More **\> Delete** for the policy you want to delete.
    The Define an App Policy dialog displays.
4.  Click **Delete Policy** to confirm the action.
