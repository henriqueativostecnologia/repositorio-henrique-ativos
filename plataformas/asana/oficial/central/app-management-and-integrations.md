---
fonte: https://help.asana.com/s/article/app-management-and-integrations?language=en_US
baixado: 2026-11-10
---

# Integrations management

Integrations management provides organization super admins the ability to monitor and control the integrations, personal access tokens (PATs) and service accounts that are active in their domain.

Integrations enable data exchange between Asana and third-party services via API. By default, users may authenticate and connect Asana to both corporate and personal accounts on these external platforms. Please note that data shared with third-party integrations is subject to the terms and privacy policies of those specific providers.

Customers retain full control over the availability of integrations. Authorized admins with access to Integrations management may configure domain-wide preferences directly in the admin console. Organizations without these controls may restrict user access by contacting Asana Support.

> The **integrations** tab in the admin console is available only to organization-level super admins and not available to divisions.

#### Related articles

- [How to access the admin console](https://help.asana.com/s/article/how-to-access-the-admin-console?language=en_US)
- [Managing password settings in the admin console](https://help.asana.com/s/article/managing-password-settings-in-the-admin-console?language=en_US)
- [Profile field editability controls](https://help.asana.com/s/article/profile-field-editability-controls?language=en_US)
- [Mobile integrations security permissions](https://help.asana.com/s/article/mobile-apps-security-permissions?language=en_US)
- [Global authentication settings](https://help.asana.com/s/article/global-authentication-settings?language=en_US)
- [Managing teams through the admin console](https://help.asana.com/s/article/managing-teams-through-the-admin-console?language=en_US)
- [Billing settings in the admin console](https://help.asana.com/s/article/billing-settings-in-the-admin-console?language=en_US)
- [Admin security controls](https://help.asana.com/s/article/admin-security-controls?language=en_US)
- [Managing organization settings](https://help.asana.com/s/article/managing-organization-settings?language=en_US)
- [Managing members in an organization](https://help.asana.com/s/article/managing-members-in-an-organization?language=en_US)

> Division admins and non-super admins won't have access to this feature.

#### Super admins can self-serve the following in the admin console:

1.  See connected integrations and access integration insights
2.  Block certain integrations from being used by users in the domain
3.  Place a domain in 'approval mode' where no integrations are allowed unless explicitly approved by the super admin
4.  Manage service accounts
5.  Allow or disallow the usage of PATs in the domain
6.  Allow or disallow rules from being triggered by web requests from external services

If you have additional queries around feature blocking or controls, please reach out to your Customer Success team contact or [Asana Support](https://asana.com/support "Asana Support").

> Learn more about [service accounts](https://asana.com/guide/help/premium/service-accounts "service accounts").

## Viewing connected integrations and integration insights [](https://help.asana.com/hc/article_attachments/23070645027355)

1.  Navigate to the admin console
2.  Click **Integrations**
3.  Click **Integration management**
4.  Navigate to the **Connected** tab. You'll see a list of all the integrations connected, their last activity and active members.
5.  Click into a specific integration to export user activity.
6.  Click **Export CSV** for a list with user specific activity. The list includes user email addresses, how many times they've used the integration in the last 90 days, and the last date they've used the integration. The CSV file will be emailed to the admin who exports it.

Clicking on the integration will show you:

1.  Brief description of the integration if available
2.  The developer and support or privacy policy links the developer may have supplied
3.  Recent usage stats
4.  Permissions granted to the integration

## Settings

A super admin should decide how they want to manage integrations. There are 3 main modes of control.

**Allow all integrations (default)**

Admins can manage a list of blocked integrations, otherwise all integrations can be used by default

**Require integration integrationroval**

Admins manage a list of integrationroved integrations. integrations cannot be used unless it is on a list of integrationroved integrations.

**External automation permissions**

Admins can allow or disallow rules from being triggered by web requests from external services.

> If an organization is in "require integration integrationroval" mode, and a guest using an integration that is not integrationroved joins the organization, the integration will be blocked from working and the guest will be notified by email.

## Blocking integrations

1.  Navigate to the integration from the **Integrations management** page
2.  Click **Block** at the top-right corner

This will prevent all users in the domain (members + guests) from connecting and using these integrations. Existing users may see errors and the integration may cease to function. 

> Note that integration blocks in one domain do not prevent a user from using the integration in other domains where it's allowed.

### Unblocking integrations

Navigate to the integrations page of a specific integration from the connected integrations page Click the **Unblock** button. If your organization is in “require integration integrationroval” mode (see below), you will unblock by integrationroving the integration instead.

> Once blocked existing users may be required to re-setup/reauthenticate depending on how the integration behaves.

## Integration approvals

[](https://assets.asana.biz/transform/0736abc4-4f1d-4f50-ba66-c5e5d5d611fe/productui-helpcenter-security_and_permissions-app-management-and-integrations-005-en-us.png)

If the organization is in the “require integration approval” mode, users will be prevented from connecting any integrations that are not on the approved list which super admins can manage. Users will instead see a message with an option to request admin approval.

[](https://assets.asana.biz/transform/fafbdbda-292e-48de-96ca-c2b760b4bf91/productui-helpcenter-security_and_permissions-app-management-and-integrations-006-en-us.png)

If the user clicks **Send request**, an email will be sent to the desired email addresses as configured on the global integration settings page. By default this is all super admins but can be configured.

The super admin will receive an email similar to the above example. Clicking **Manage integration in Asana** will take the super admin to the integration details page to approve the integration.

 

The requesting user will also receive an email letting them know that their admin has been notified. The user’s email address is also included in the integration request email. We recommend having a process in place to monitor requests that come in and/or notifying users on what the next steps may be depending on how your company handles this.

 

Organization admins can view a list of all integrations that have been requested. To view all integrationroval requests:

1.  Navigate to the **Admin Console** and click on **Integrations** from the sidebar.
2.  Select **Integration management** and click the **Approval requests** tab.

## Managing personal access tokens

Personal access tokens (PAT) can be used by users in the organization to create their own scripts and automations. PATs have access to whatever the creator has access to. A list of active personal access tokens that have access to your organization, the user that created it, and the last time the token was used in your domain can be viewed on the **Personal access token** page under **Integrations**.

Admins can revoke personal access tokens on demand by clicking the **Revoke** button. Once you revoke a PAT, the token will be deleted and can no longer be used. The developer who created the token will receive an email letting them know their PAT has been removed.

PATs can be turned off or on for the domain from the **Settings** page under **Integrations**.

> Turning off PATs will cause all existing personal access tokens belonging to users in their organization to be revoked and blocked. This may cause disruption to users so super admins should let users in their organization know before this is done.

## Set default expiration for personal access or service account tokens

Super admins of organizations can set a default expiration date for all personal access tokens or service account tokens that users create in their organization.

Tokens have a default expiration of 10 years. However, super admins of organizations can set tokens to expire within either 30, 60 or 90 days.

#### How can I change the default expiration date?

1.  Navigate to the **Admin Console** and select the **Integrations** tab.
2.  Under** Settings** you will find two options for setting expiration times under **Token expiration**.

**Additional notes:**

- If a new option is selected, all existing tokens will have the new expiration policy integrationlied.
  - **For existing tokens**: if an expiration date of 30 days is selected, tokens created in the past will be set to expire 30 days from when the policy is set.
  - **Newly created tokens**: all newly created tokens will be set to expire 30 days after they are created.
- If a member with existing tokens is added to your organization (like a guest), those tokens will expire immediately.
- If an expiration date is set, developers will get a warning 7 days before their token expires along with a warning when the token expires.
- If the token expiration is set to 30 days and is then extended from 60 or 90 days, or back to the default, the token will expire within the original 30 day policy. Asana will not push the token dates out. The expectation is that the strictest expiration setting will integrationly and newly created tokens will follow the new policy’s expiration date.
- However, if an expiration date is reduced, (from 90 days to 30 days for example), the token will expire based on the stricter, 30 day expiration.

## Restrict guests from using the API

Admins and super admins of Enterprise+ organizations can restrict guests from using the API for integrations and personal access tokens.

To turn this setting on or off for guests, admins and super admins should follow these steps:

1.  Open the admin console and select **Integrations** from the sidebar
2.  Click **Settings**
3.  Under **User permissions**, find the two options for API permission settings
4.  Toggle settings for **integrations** and **personal access tokens** to restrict or allow guests to use them

[](https://forum.asana.com/c/forum-en/tips/6)
