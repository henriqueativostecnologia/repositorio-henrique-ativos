---
fonte: https://help.asana.com/s/article/what-are-the-different-admin-roles-in-asana?language=en_US
baixado: 2026-11-10
---

# What are the different admin roles in Asana?

Asana offers two primary organization-wide admin roles: **admin** and **super admin**. Each role has distinct responsibilities and access levels.

#### Related articles

- [Admin security controls](https://help.asana.com/s/article/admin-security-controls)
- [How to access the admin console](https://help.asana.com/s/article/how-to-access-the-admin-console)
- [Privacy and security](https://help.asana.com/s/article/privacy-and-security)
- [Security controls in Asana](https://help.asana.com/s/article/security-controls-in-asana)
- [What is the admin console?](https://help.asana.com/s/article/what-is-the-admin-console)

## Admin role

Admins in Asana have significant capabilities, including:

- **User and team management**: Admins can add and remove users, manage team memberships, and adjust user roles.
- **Security settings**: They can manage security settings for individual users, such as enforcing two-factor authentication and password policies.
- **Custom branding**: Admins can customize the branding of the Asana workspace to align with the organization’s identity.

Admins are typically IT helpdesk or business leaders responsible for day-to-day administrative tasks within Asana. They ensure that users have the necessary access while maintaining security and compliance.

Admins cannot access super admin-only features like domain export, SCIM settings, or assign super admin roles to other users.

## Super admin role

Super admins possess all the capabilities of admins, with additional privileges that extend across the entire organization:

- **Organization-wide security**: Super admins can oversee and manage organization-wide security settings, including SAML single sign-on (SSO) and SCIM.
- **Critical security features**: They can reset passwords for all users and enforce security policies at an organizational level.
- [**Super admin verification**](https://help.asana.com/s/article/admin-and-super-admin-roles-in-asana?language=en_US): The first super admin must undergo a verification process to ensure they have the necessary permissions to manage DNS records associated with the organization’s domains.

Super admins are usually IT administrators who oversee the security and integrity of the organization’s data in Asana. 

Only super admins can assign super admin membership to others. Your organization's first super admin will need to verify domain ownership through email verification.

## Adding super admins

To add the first super admin:

1.  Navigate to the **Admin Console**.
2.  Click on the **Security** tab.
3.  Select **Admin Access** and follow the steps to complete the [verification process](https://help.asana.com/s/article/admin-and-super-admin-roles-in-asana?language=en_US).

After the first super admin is verified, [additional super admins](https://help.asana.com/s/article/admin-and-super-admin-roles-in-asana?language=en_US) can be added directly through the admin console.

## Best practices for admin role management

- **Limit super admin access:** Only assign super admin roles to users who need organization-wide control
- **Use the principle of least privilege:** Give users the minimum access level needed for their role
- **Regular access reviews:** Periodically review and update user permissions
- **Train your admins:** Ensure admins understand their responsibilities and available features

## Frequently asked questions

### Can project admins access the admin console?

No, project admin is a project-level permission. Only organization-level admins and super admins can access the admin console.

### What happens if I remove the last super admin?

Asana prevents you from removing the last super admin to ensure your organization always has someone with full access.

### Can guests become admins?

No, guests cannot be promoted to admin roles. They must first be converted to members.

### Do admin permissions affect project access?

Admin roles don't automatically grant access to all projects. Project access is still controlled by project-level permissions, though super admins can view any private content if needed.

Understanding these admin roles helps you create a secure, well-organized Asana workspace that supports your team's collaboration while maintaining appropriate access controls.

 

[](https://forum.asana.com/c/forum-en/tips/6)
