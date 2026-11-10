---
fonte: https://help.asana.com/s/article/security-controls-in-asana?language=en_US
baixado: 2026-11-10
---

# Security controls in Asana

Asana provides a comprehensive set of security controls to help organizations safeguard their data and ensure compliance with security policies.

Admins and super admins can manage various security settings to protect their organization. These controls include managing user access, setting permissions, and configuring advanced security measures.

Here’s an overview of the key security features available.

#### Related articles

- [Member and team management](https://help.asana.com/s/article/member-and-team-management)
- [Admin security controls](https://help.asana.com/s/article/admin-security-controls)
- [Privacy and security](https://help.asana.com/s/article/privacy-and-security)
- [Mobile apps security permissions](https://help.asana.com/s/article/mobile-apps-security-permissions)
- [App management and integrations](https://help.asana.com/s/article/app-management-and-integrations)

## Authentication and access controls

**Google SSO** allows members to sign in using their Google accounts, streamlining the login process while maintaining security.

**SAML authentication** provides integration with identity providers like Okta, Azure Active Directory, and OneLogin. Administrators can configure SAML to be:

1.  **Optional**: Members can choose to use SAML or regular login
2.  **Required**: All members (except guests) must use SAML authentication

When configuring SAML, you can set session timeout durations and mobile session timeout settings to control how long users stay logged in.

**Two-factor authentication (2FA)**

Two-factor authentication adds an extra layer of security by requiring a second form of identification. Available on all paid plans, 2FA can be:

1.  **Optional**: Members can choose to enable 2FA
2.  **Required**: All members and guests must use 2FA 

This setting doesn't impact users who sign in with Microsoft SSO, Google SSO or SAML, as these methods provide their own security layers.

### Password controls

Asana's default **password strength requirements** ensure that passwords are at least 8 characters and have a "fair" entropy score. For enhanced security, admins can increase the minimum length to up to 20 characters.

**Password reset** allows administrators to force a password reset for all members in the organization. This immediately signs out all users and requires them to create new passwords via email.

## Mobile apps controls

The Asana [mobile app](https://help.asana.com/s/article/mobile-apps-security-permissions?language=en_US) ensures data security with features like biometric authentication (fingerprint and facial recognition), and controlled app permissions. Admins can manage permissions to restrict screen captures, attachments, and limit copy and paste. These measures help protect your organization’s information on mobile platforms.

## Admin controls and permissions

### Guest access management

Control who can invite guests to your organization:

1.  **Admins only**: Only administrators can invite guests
2.  **Admins and members**: Both admins and regular members can invite guests
3.  **Anyone**: All users, including guests, can invite new guests

### File attachment controls

Manage which file attachment types are allowed in your organization. Administrators can disable specific attachment methods or restrict all file attachments if needed for security compliance.

### Team and project privacy settings

Set default privacy levels for new teams and projects:

1.  **Public to organization**: Teams and projects are visible to all organization members
2.  **Membership by request**: A member has to request to join the team

### Read-only link sharing permissions

Control how project views and timelines can be shared:

1.  **Public sharing allowed**: Members can share read-only project views externally
2.  **Organization sharing only**: Members can only share read-only project views within your organization
3.  **Turn off read-only view sharing**: No one can share read-only project views

By leveraging these security controls, organizations can effectively protect their data, maintain compliance with security policies, and provide a secure working environment for their teams.

 

[](https://forum.asana.com/c/forum-en/tips/6)
