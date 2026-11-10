---
fonte: https://help.asana.com/s/article/admin-security-controls?language=en_US
baixado: 2026-11-10
---

# Admin security controls

In this article, you'll learn how to edit guest invite settings, controls for file attachments, team privacy settings, and how to define your organization's admins and super admins.

#### Related articles

- [ *How to access the admin console* ](https://help.asana.com/s/article/how-to-access-the-admin-console?language=en_US)
- [Managing password settings in the admin console](https://help.asana.com/s/article/managing-password-settings-in-the-admin-console?language=en_US)
- [Profile field editability controls](https://help.asana.com/s/article/profile-field-editability-controls?language=en_US)
- [Mobile apps security permissions](https://help.asana.com/s/article/mobile-apps-security-permissions?language=en_US)
- [Global authentication settings](https://help.asana.com/s/article/global-authentication-settings?language=en_US)
- [Managing teams through the admin console](https://help.asana.com/s/article/managing-teams-through-the-admin-console?language=en_US)
- [Billing settings in the admin console](https://help.asana.com/s/article/billing-settings-in-the-admin-console?language=en_US)
- [Managing organization settings](https://help.asana.com/s/article/managing-organization-settings?language=en_US)
- [Managing members in an organization](https://help.asana.com/s/article/managing-members-in-an-organization?language=en_US)
- [App management and integrations](https://help.asana.com/s/article/app-management-and-integrations?language=en_US)

## Manage organization admins

From your admin console, you can determine your organization’s [admins and super admins](https://help.asana.com/s/article/admin-and-super-admin-roles-in-asana?language=en_US). From the **Security** tab, **under Admin Controls**, click **Admin access** to determine the admins for your organization.

[](https://assets.asana.biz/transform/c8b9046e-65d4-44fb-9409-8c29869813c6/productui-helpcenter-security_and_permissions-admin-security-controls-001-en-us.png)

> Organization admins have edit access to the [company’s mission statement](https://asana.com/guide/help/premium/goals#gl-mission-statement "company’s mission statement").

## Guest invite settings

Super admins of Asana [Enterprise](https://asana.com/enterprise) and [Enterprise+](https://asana.com/enterprise) tiers, as well as [legacy tier](https://asana.com/pricing-legacy) Legacy Enterprise organizations or divisions can control who can invite organization guests (those without a company email address) into your Asana organization. Super admins can select one of these options:

- Admins only

- Admins and members

- Admins, members, and guests

To enable one of these options, navigate to the **Security tab** of the admin console, click **Admin Controls,** and click **Guest invite settings**. Once this has been enabled, those who no longer have the ability to invite organization guests will receive an error message when trying to do so.

> Ent+ tiers need to control permissions through the [Role-based access control](https://help.asana.com/s/article/role-based-access-control-with-custom-roles). To access guest invite settings, navigate to the admin console, click **Members**, and select **Manage roles**.

## Trusted guest domains

**Available on the Asana [*Enterprise+*](https://asana.com/enterprise) tier.
**
Admins and super admins can create a list of approved external domains from which users with guest invite permissions can invite guests.

Guest invites can only be sent to those email domains on the approved list, ensuring greater security and control over your organization's collaborations. If a user attempts to send a guest invite to someone from an unlisted domain, they will receive an error message.

#### Setting up trusted guest domains

> Trusted guest domains can only be enabled if guest invite permissions are set to **Admins and members** or **Admins, members, and guests**. The feature cannot be activated if guest invite permissions are set to **Admins only**.

 

####

1.  Navigate to the **Security** tab of the admin console
2.  Scroll down to **Membership & Invites**
3.  Click **Guest settings**
4.  Within the **Invite permissions** section, you can restrict guest invites to trusted domains
5.  Click **Add domains** and type in the domains you trust. Click **Add domains** again to confirm.

> Ensure the domains are an exact match. Adding the domain **acme.com** does not cover subdomains like **app.acme.com** or **acme.co.uk**. Such subdomains must be added separately.

#### Removing trusted guest domains

Find the domain in the list you want to remove, click the trash icon, and confirm your choice by pressing save.

#### Deactivating the trusted guest domains feature:

To revert the settings, simply switch the trusted guest domains control back to **Any domain**.

## Disabling file attachments

**The ability to disable file attachments is available to super admins on the Asana [*Enterprise+*](https://asana.com/enterprise) tier, as well as [*legacy tier*](https://asana.com/pricing-legacy) Legacy Enterprise.*
***

The disabling file attachments feature allows super admins to ensure that Asana implementations across their organization meet all security and consistency requirements related to blocking any file attachments that are restricted as per their company’s security policies and preferred file integrations.

This feature gives better controls at a domain level to ensure strict upload policies in accordance with their organizational requirements.

IT admins will also have a quick way to enable or disable one or more or all of computer, Dropbox, Google Drive, Box and Onedrive / Sharepoint upload sources as per their company’s IT security policies and have it applied across all Asana product surface areas where attachments can be added.

### How to access your file attachment options

Super admins can access their file attachments options settings through the **Security** tab of their admin console.

From the **Security** tab, scroll down to **Admin controls** and click **File attachment options**.

[](https://assets.asana.biz/transform/769960b2-9e78-4cbb-a69a-5654abeff938/productui-helpcenter-security_and_permissions-admin-security-controls-004-en-us.png)

> The default setting is all attachments are enabled.

[](https://assets.asana.biz/transform/7224fe6f-3849-4ddc-b7f5-f36b8d1e7e12/productui-helpcenter-security_and_permissions-admin-security-controls-005-en-us.png)

From the next window, you can select your file attachment preferences.

### Unchecking “Allow attachments from Asana apps, API, and other features”

[](https://assets.asana.biz/transform/900390ca-56e2-49e7-917d-534790b9e1ec/productui-helpcenter-security_and_permissions-admin-security-controls-006-en-us.png)

#### Deselecting this will disable attachment types on

- Web attachments
- Mobile
- API
- Copy and paste
- Forms
- Drag and drop
- Email forwarding

### Disabling attachments from third party apps

To prevent the ability to attach files from third-party apps, you can block them from the **Apps** tab or select the desired app from the pop-up window. This means that the ability to add attachments from Dropbox, Google Drive, Box, and OneDrive/ SharePoint will no longer be allowed.

### Disabling attachments on mobile

There’s no differentiation on the mobile app on attachments between uploads from third party apps and attachments from the device. This is because everything downloads to the device first.

The only way to disable on mobile is by disabling **allow attachments from Asana's apps, API, and other features**.

[](https://assets.asana.biz/transform/c26237b0-e44a-4a9f-99e4-ae8bc6cdb604/productui-helpcenter-security_and_permissions-admin-security-controls-007-en-us.png)

## Team privacy settings

Super admins for **[*Enterprise*](https://asana.com/enterprise)** and **[*Enterprise+*](https://asana.com/enterprise)**, as well as [*legacy tier*](https://asana.com/pricing-legacy) **Legacy Enterprise** organizations can set a default privacy level for teams in their organization.

When set, this will be the pre-selected option when creating a new team. Team creators can still create teams with other privacy levels as they choose.

To set your default privacy settings navigate to your admin console and click on the **Security** tab. Then, click on **Team privacy settings**.

[](https://assets.asana.biz/transform/dad45ee0-f823-49b2-84e9-d53422cdffea/productui-helpcenter-security_and_permissions-admin-security-controls-008-en-us.png)

From the next tab, you can select your default setting.

[](https://forum.asana.com/c/forum-en/tips/6)
