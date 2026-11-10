---
fonte: https://help.asana.com/s/article/global-authentication-settings?language=en_US
baixado: 2026-11-10
---

# Global authentication settings

This article explains how organizations can configure authentication settings to streamline access and enhance security, including **Google sign-in**, **Microsoft SSO**, and **SAML**.

#### Related articles

- [How to access the admin console](https://help.asana.com/s/article/how-to-access-the-admin-console?language=en_US)
- [Managing password settings in the admin console](https://help.asana.com/s/article/managing-password-settings-in-the-admin-console?language=en_US)[](https://help.asana.com/s/article/profile-field-editability-controls?language=en_US)
- [Admin security controls](https://help.asana.com/s/article/admin-security-controls?language=en_US)
- [Managing members in an organization](https://help.asana.com/s/article/managing-members-in-an-organization?language=en_US)
- [Microsoft Single Sign-On](https://help.asana.com/s/article/microsoft-single-sign-on)

## Google sign-in

Google sign-in is available for paid organizations, and is not supported for paid divisions. Super admins must first log in with their Google account in order to enable Google SSO. If you logged in with email and password, simply log out and in again using the blue **Use Google Account** button instead.

[](https://assets.asana.biz/transform/0259f5e0-11c1-47bd-b4fe-cffbcea8ea7b/productui-helpcenter-security_and_permissions-global-authentication-settings-001-en-us.png)

#### From the **Security** tab:

1.  Navigate to **Global authentication settings**
2.  Click **Google sign-in**
3.  Set Google Sign-in as either **Optional** or **Required for all members, except guests**
4.  Once you've chosen an option, click **Save changes**

> Organization guests can always login with email and password, regardless of whether Google SSO is required for members or not.

## SAML authentication

Asana [*Enterprise*](https://asana.com/enterprise) and [*Enterprise+*](https://asana.com/enterprise) organizations, as well as organizations on [*legacy tier*](https://asana.com/pricing-legacy) Legacy Enterprise can enable SAML from the security tab of their admin console.

[](https://assets.asana.biz/transform/7713def9-e9d5-414d-b0aa-8cc921383535/productui-helpcenter-security_and_permissions-global-authentication-settings-002-en-us.png)

#### From the **Security** tab:

1.  Navigate to **Global authentication settings**
2.  Click **SAML authentication**

## SAML session timeout

Super admins can set SAML session timeout between 1 hour and 30 days in the admin console. Members will be automatically logged out and asked to log in again after the specified timeout set.

 

[](https://assets.asana.biz/transform/5e799d55-988a-4a55-bdbb-496e0701f04a/productui-helpcenter-security_and_permissions-global-authentication-settings-003-en-us.png)

## Microsoft SSO

Asana supports **Microsoft Single Sign-On (SSO)**, which allows organization members to sign in using their Microsoft account credentials. Organization admins can also set **Microsoft SSO** as the required login method for all members, except guests. For full setup instructions, see [Microsoft Single Sign-On](https://help.asana.com/s/article/microsoft-single-sign-on).

 

[](https://forum.asana.com/c/forum-en/tips/6)
