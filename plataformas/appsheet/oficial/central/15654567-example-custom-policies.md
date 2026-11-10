---
fonte: https://support.google.com/appsheet/answer/15654567?hl=en
baixado: 2026-11-10
---

# Example custom policies

The following sections provide examples of custom policies:

- [Restrict access to team data sources](#restrict-access-team-data-sources)
- [Restrict access to only the stable version of an app](#restrict-access-to-stable-version)
- [Define custom policy exceptions](#policy-exception)

See also [Configure team settings](https://support.google.com/appsheet/answer/11918568) and the following sections that describe how to use the predefined policies:

- [Control which app creators can use AI in automations](https://support.google.com/appsheet/answer/16052764) 
- [Disable AppSheet databases](https://support.google.com/appsheet/answer/12629371)   
- [Prevent app creators from adding email attachments in automations](https://support.google.com/appsheet/answer/11447614#prevent-email-attachments)
- [Prevent app creators from enabling Chat apps with AppSheet](https://support.google.com/appsheet/answer/13198694#prevent-chat-apps)
- [Prevent app creators from enabling the API](https://support.google.com/appsheet/answer/10105769#prevent-enabling-api)
- [Prevent app creators from using external authentication domains](https://support.google.com/appsheet/answer/10105757#prevent-auth-domains)
- [Prevent app creators from using external data sources](https://support.google.com/appsheet/answer/13579362)
- [Prevent app creators from using Google Forms](https://support.google.com/appsheet/answer/14836137)
- [Prevent app creators from using webhooks](https://support.google.com/appsheet/answer/13573588)

##  Restrict access to team data sources

Restrict access to team data sources to only specific team members by defining a governance policy. When naming team data sources, AppSheet includes the string: `:Team:` 

For example: `google_cloud_identity-1:Team:1234567`

Using the `:Team:` string in a policy condition, you can restrict the team members that can access any of the team data source. 

To restrict access to team data sources, do the following

1.  [Add a predefined organization or team policy](https://support.google.com/appsheet/answer/11948767#add-predefined-policy).

2.  In the Policy template drop-down, select **Restrict data sources**.

3.  Click **Next**.

4.  Update the policy definition, as follows:

    +-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Field**                                                                     | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Name                                                                          | Enter a name for the policy that will appear on the Policies page.            |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Condition                                                                     | Update the condition, as follows:                                             |
|                                                                               |                                                                               |
|                                                                               | `OR(NOT(CONTAINS(DataSourceName], ":Team:")                                   |
|                                                                               | ), IN(USEREMAIL(), LIST("`*`emailaddress1`*`", "`*`emailaddress2`*`", ...)))` |
|                                                                               |                                                                               |
|                                                                               | Where:                                                                        |
|                                                                               |                                                                               |
|                                                                               | -   *`emailaddressN`*: Approved team member email addresses.                  |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

    Modify the other fields, as required. See [Configure the policy](https://support.google.com/appsheet/answer/11948767#configure-policy). 

    For example:

    Policy for restricting access to team data sources

5.  [Review policy compliance](https://support.google.com/appsheet/answer/11948767#policy-compliance).

6.  Click **Save**.

## Restrict access to only the stable version of an app

When you set a [stable version](https://support.google.com/appsheet/answer/10104791) of an app, you can define a policy to restrict access to only that version.

**Note**: When this policy is defined, the app creator will see an error when viewing the latest version. This error won't impact access to the stable version of the app by users.

To restrict access to only the stable version of an app, do the following:

1.  [Add a custom policy](https://support.google.com/appsheet/answer/11948767#add-custom-policy).

2.  In the Policy template drop-down, select **Custom policy**.

3.  Click **Next**.

4.  Update the policy definition, as follows:

    +-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Field**                                                                     | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Name                                                                          | Enter a name for the policy that will appear on the Policies page.            |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Component                                                                     | Select **AppSettings** in the drop-down.                                      |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Condition                                                                     | Update the condition, as follows:                                             |
|                                                                               |                                                                               |
|                                                                               | `IF(CONTEXT("AppName")="`*`appname`*`",[version]=`*`version`*`,true)`         |
|                                                                               |                                                                               |
|                                                                               | Where:                                                                        |
|                                                                               |                                                                               |
|                                                                               | -   *`appname`*: App name defined by the `appName` query parameter in the app |
|                                                                               |     URL when viewing the app in the editor or accessing the app in your       |
|                                                                               |     desktop browser. (It is **not** equivalent to the Short Name of the app   |
|                                                                               |     defined in Settings.)                                                     |
|                                                                               | -   *`version`*: Stable version of the app. See [View or restore a version of |
|                                                                               |     your app](https://support.google.com/appsheet/answer/10105387).           |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

    Modify the other fields, as required. See [Configure the policy](https://support.google.com/appsheet/answer/11948767#configure-policy). 

    For example:

    Policy that restricts access to stable version only

5.  [Review policy compliance](https://support.google.com/appsheet/answer/11948767#policy-compliance).

6.  Click **Save**.

## Disable the export of a CSV file

To disable the export of a CSV file, do the following:

1.  [Add a custom policy](https://support.google.com/appsheet/answer/11948767#add-custom-policy).

2.  In the Policy template drop-down, select **Custom policy**.

3.  Click **Next**.

4.  Update the policy definition, as follows:

    +-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Field**                                                                     | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Name                                                                          | Enter a name for the policy that will appear on the Policies page.            |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Component                                                                     | Select **Actions** in the drop-down.                                          |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Condition                                                                     | Update the condition, as follows:                                             |
|                                                                               |                                                                               |
|                                                                               | `[ActionType]<>"EXPORT_VIEW"`                                                 |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

    Modify the other fields, as required. See [Configure the policy](https://support.google.com/appsheet/answer/11948767#configure-policy). 

    For example:

    Policy to disable the export of a CSV file

5.  [Review policy compliance](https://support.google.com/appsheet/answer/11948767#policy-compliance).

6.  Click **Save**.

## Define custom policy exceptions

Custom policy exceptions can be defined based on [app name](#app-name), [signed-in user email](#signed-in-user), [owner ID or app name](#ower-id-or-app-name), [users from a domain](#domain), and more.

### Define a custom policy exception by app name

To define a policy exception by app name, you can use the [`CONTEXT(AppName)`](https://support.google.com/appsheet/answer/10107885) in the condition statement regardless of the component. To access the app name to allow, view the `appName` parameter in the AppSheet URL. For example:
`appsheet.com/Template/AppDef?appName=`**`ShiftSchedule-6428568`**`&appId=aa10fb5c-1a6e-40a`

The following custom policy limits the types of automation tasks unless the app name is on the approved list.

Custom policy that limits the types of automation tasks unless the app name is on the approved list

### Define a custom policy exception based on signed-in user email

To define a policy exception by signed-in user email, you can use the [`USEREMAIL()`](https://support.google.com/appsheet/answer/10108210) function to return the email of the signed in user. The `USEREMAIL()` function can be used in the condition statement for any policy. If you set the `Stage` to `Check on App Edit`, when the app is being edited AppSheet will check if the signed-in user’s email address is in the approved list. 

**Note**: The` USEREMAIL()` function is evaluated based on the signed-in user. This means the policy could evaluate differently for an app owner versus an app collaborator.

The following custom policy limits the types of automation tasks unless the signed-in user is on the approved list.
 

### Define a custom policy exception to restrict who can deploy an app

By setting the `Stage` to `Check on Deployment`, you can define a policy exception to restrict who can deploy an app. The following custom policy restricts who can deploy an app based on the app [owner ID](https://support.google.com/appsheet/answer/13265290) or full name of the app using [`CONTEXT(AppName)`](https://support.google.com/appsheet/answer/10107885).

Define a custom policy exception to restrict who can deploy an app

### Define a custom policy exception to allow specific users from a domain

You can define a custom policy exception to allow sharing with only specific people from an external domain. The following custom policy allows sharing with users if their email domain matches `yourdomain.com` or if the user's email is listed in the [`IN()`](https://support.google.com/appsheet/answer/10107681) expression.

Custom policy exception to allow specific users from a domain or a list of emails

##
