---
fonte: https://help.asana.com/s/article/managing-password-settings-in-the-admin-console?language=en_US
baixado: 2026-11-10
---

# Managing password settings in the admin console

This article explains Asana's enhanced password strength options and organization-wide password reset capabilities.

#### Related articles

- [How to access the admin console](https://help.asana.com/s/article/how-to-access-the-admin-console?language=en_US)
- [Profile field editability controls](https://help.asana.com/s/article/profile-field-editability-controls?language=en_US)
- [Mobile apps security permissions](https://help.asana.com/s/article/mobile-apps-security-permissions?language=en_US)
- [Global authentication settings](https://help.asana.com/s/article/global-authentication-settings?language=en_US)
- [Managing teams through the admin console](https://help.asana.com/s/article/managing-teams-through-the-admin-console?language=en_US)
- [Billing settings in the admin console](https://help.asana.com/s/article/billing-settings-in-the-admin-console?language=en_US)
- [Admin security controls](https://help.asana.com/s/article/admin-security-controls?language=en_US)
- [Managing organization settings](https://help.asana.com/s/article/managing-organization-settings?language=en_US)
- [Managing members in an organization](https://help.asana.com/s/article/managing-members-in-an-organization?language=en_US)
- [App management and integrations](https://help.asana.com/s/article/app-management-and-integrations?language=en_US)

## Password strength

Asana enforces the following requirements for all users:

1.  Passwords must have a minimum length of 8 characters.
2.  Passwords must have at least a "fair" strength as estimated by [entropy score](https://en.wikipedia.org/wiki/Password_strength#Entropy_as_a_measure_of_password_strength).
3.  Passwords must not appear on our list of previously compromised passwords.

For best results, we recommend using a *[passphrase](https://en.wikipedia.org/wiki/Passphrase#Compared_to_passwords)* or generating a random string with a *password manager*. 

For enhanced security, [Enterprise+](https://asana.com/enterprise) and [Legacy Enterprise](https://asana.com/pricing-legacy) super admins can increase the required minimum length to up to 20 characters. This setting can be found by clicking into the **Security** tab of your admin console and clicking on **Password strength**.

Changes to the password minimum length will only affect newly created passwords. The domain admin will have to force reset all user passwords in order for the new password requirements to apply to existing users.

##

## Organization-wide password reset

**Available on Asana [Starter](https://asana.com/plan/starter), [Advanced](https://asana.com/plan/advanced), [Enterprise](https://asana.com/enterprise), and [Enterprise+](https://asana.com/enterprise) tiers, as well as [legacy tiers](https://asana.com/pricing-legacy) Premium, Business, and Legacy Enterprise.**

**Visit our [pricing page](https://asana.com/pricing) for more information.**

You can force an organization-wide password reset for users that have access to your organization.

1\. Members or guests who have an Asana password will be logged out. They will then receive an email with a password reset link and be forced to choose a new password before logging in again.

2\. Members or guests who do not have an Asana password will only be logged out.

3\. Members or guests who log in with [SAML](https://help.asana.com/s/article/global-authentication-settings?language=en_US#h_01HQ11937EP9N6G9SERNXYC7YW) or [Google SSO](https://help.asana.com/s/article/global-authentication-settings?language=en_US#h_01HQ115GKJGDM3A4R18P4ZTYQT) and don't have an Asana password will only be logged out.

> Users who initially signed up to Asana by setting a password and have since upgraded to login with SAML or Google SSO will receive an email asking them to reset their password. This will have no effect on their SAML/Google SSO password.

## Individual password reset

Available on Asana [*Enterprise*](https://asana.com/enterprise) and [*Enterprise+*](https://asana.com/enterprise) tiers, as well as [*legacy tier*](https://asana.com/pricing-legacy) Legacy Enterprise. Super admins can reset an individual user's password via their member profile settings.

 

[](https://forum.asana.com/c/forum-en/tips/6)
