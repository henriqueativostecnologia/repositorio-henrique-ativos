---
fonte: https://help.asana.com/s/article/profile-field-editability-controls?language=en_US
baixado: 2026-11-10
---

# Profile field editability controls

**Available on Asana [*Enterprise*](https://asana.com/enterprise) and [*Enterprise+*](https://asana.com/enterprise) tiers, as well as [*legacy tier*](https://asana.com/pricing-legacy) Legacy Enterprise.**

**Visit our [*pricing page*](https://asana.com/pricing) for more information.**

Asana has [SCIM integrations](https://help.asana.com/s/article/provisioning-and-deprovisioning-users-with-scim?language=en_US) with leading identity provider platforms that enable customers to import user profile information such as **title** and **department** into Asana. As this information is imported from identity systems, admins may want to control whether or not users can edit this information in Asana using profile field controls.

#### Related articles

- [How to access the admin console](https://help.asana.com/s/article/how-to-access-the-admin-console?language=en_US)
- [Managing password settings in the admin console](https://help.asana.com/s/article/managing-password-settings-in-the-admin-console?language=en_US)
- [Mobile apps security permissions](https://help.asana.com/s/article/mobile-apps-security-permissions?language=en_US)
- [Global authentication settings](https://help.asana.com/s/article/global-authentication-settings?language=en_US)
- [Managing teams through the admin console](https://help.asana.com/s/article/managing-teams-through-the-admin-console?language=en_US)
- [Billing settings in the admin console](https://help.asana.com/s/article/billing-settings-in-the-admin-console?language=en_US)
- [Admin security controls](https://help.asana.com/s/article/admin-security-controls?language=en_US)
- [Managing organization settings](https://help.asana.com/s/article/managing-organization-settings?language=en_US)
- [Managing members in an organization](https://help.asana.com/s/article/managing-members-in-an-organization?language=en_US)
- [App management and integrations](https://help.asana.com/s/article/app-management-and-integrations?language=en_US)

Super admins can choose which profile fields users can edit by going to **Admin console** \> **Security** \> **SCIM-related settings** \> **User profile settings**

[](https://assets.asana.biz/transform/ab788aa4-5b4a-460b-9a46-3b943308ae1e/productui-helpcenter-security_and_permissions-profile-field-editability-controls-001-en-us.png)

> We only recommend restricting users from editing this information in Asana if your organization is syncing user profile fields via SCIM to Asana. Otherwise, users will lack the ability to add this information to their profiles.

Admins can still update locked attributes on behalf of other users by making changes to the users’ profiles from the **Members** tab in the admin console.

[](https://assets.asana.biz/transform/b0519f4c-7ba9-4f6c-af05-74cb0f667536/productui-helpcenter-security_and_permissions-profile-field-editability-controls-002-en-us.png)

Super admins can toggle profile field editability controls on or off for **Job title** or **Department or team**.

[](https://assets.asana.biz/transform/bb55f116-efaa-4651-b9ad-75b368258eb9/productui-helpcenter-security_and_permissions-profile-field-editability-controls-003-en-us.png)

When super admins have restricted edits to **Job title** and **Department or team** fields, users will see these fields locked for edits when they go to their profile settings.

[](https://forum.asana.com/c/forum-en/tips/6)
