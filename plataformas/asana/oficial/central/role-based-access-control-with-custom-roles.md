---
fonte: https://help.asana.com/s/article/role-based-access-control-with-custom-roles?language=en_US
baixado: 2026-11-10
---

# Role-based access control (RBAC) with custom roles

**Available to organizations and divisions on [Enterprise+](https://asana.com/enterprise) (or Enterprise with the Permissions Management Add-on).**

**RBAC support for divisions is part of an early-access program and is available only to selected customers.**

Role-based access control (RBAC) with custom roles allows organizations to create and manage organization-level custom user roles, providing centralized control over what users can do in Asana. Super admins can define roles with specific permission sets and assign these roles to users—helping organizations meet security and compliance requirements and standardize how users work in Asana.

#### Related articles

- [Setting up Asana roles in Microsoft Entra ID with SCIM](https://help.asana.com/s/article/setting-up-asana-roles-in-microsoft-entra-id-with-scim)
- [Setting up Asana roles in Okta with SCIM](https://help.asana.com/s/article/setting-up-asana-roles-in-okta-with-scim)

## Benefits of RBAC

1.  **Centralized control**: Manage organization-level permissions from the admin console
2.  **Enhanced security and compliance**: Meet security and compliance requirements with granular control over role permissions
3.  **Standardized workflows**: Create standardized ways of working across your organization by defining appropriate access levels by role
4.  **Reduced administrative burden:** Delegate user management to specified admin users and simplify admin workflows by integrating with a supported IDP for automated role assignment

## How RBAC works

With RBAC, permissions are associated with roles rather than individual users, making it easier to manage access across your organization.

### User roles

- **Standard roles:** Asana includes a set of standard roles that have both inherent, non-configurable permissions and a set of configurable permissions. Custom roles are based on standard roles and inherit the non-configurable permissions and configurable permission defaults.
  - **Super admin**: This is the top-level administrator role with full control over the Asana organization, including managing users. Permissions for this role cannot be modified and custom roles may not be created based on this role.
  - **Admin**: Organization admins have access to the admin console and have access to admin settings, including managing teams and members, and limited control over domain settings. Super admins can adjust user management permissions for this role, including delegating role management to the admin or custom admin role.
    - The Admin standard role is only available in organizations, and not available in Divisions.
  - **Member**: This is the default role for users with an internal email address (e.g., @yourcompany.com). Members have standard access to collaborate within your Asana organization.
  - **Guest**: This is the default role for users with an external email address (e.g., @yourclient.com). Guests are intended for collaboration with people outside your primary organization and have [limited inherent permissions](https://help.asana.com/s/article/guests-faq?language=en_US#h_01HSJYXMKJQ4TRJMQ1H3MFV13B). External users can only be assigned the guest role or custom roles based on the guest role. Similarly, internal users cannot be assigned the guest role.
- **Custom roles:** Super admins, division admins, and admins given the permissions to manage roles can create custom user roles based on the standard roles and modify the configurable permissions.

### RBAC permissions

Control what actions users can perform across Asana, including creation, deletion, account permissions and more. Visit our [permissions overview](https://help.asana.com/s/article/permissions-overview) article for more information.

## Getting started with RBAC

Follow the steps below to set up roles and permissions for your organization.

### Step 1: Accessing RBAC settings

You can view and configure all user roles in one place from the Manage roles page in the admin console.

1.  Navigate to the admin console in Asana.
2.  Click the **Manage roles** tab in the Members section of the left navigation bar.
3.  Here you’ll see the list of roles for your organization along with some basic information about them, including the role description and the members list for each role.
4.  When you first get started, only the standard roles will appear here; once you’ve created custom roles you’ll be able to view them from this page as well. RBAC settings

### Step 2: Creating a custom role

Custom roles should be created when more precise controls over the permissions  a user or group of users should have in Asana are needed.

1.  From the **Manage roles** tab, click **Create role** in the top right corner.
    1.  Division admins can only create custom roles with Member or Guest as the template. The admin role as a template is only available at the organization level.
2.  Provide a name and description for the custom role (e.g., "Project manager", "Marketing team member"). 
    1.  Tip: Specific names and clear descriptions can be helpful later on as your list of roles increases or if you plan to delegate role management to other admins.
3.  Select the standard role to base the new custom role on. This will affect the non-configurable and configurable permissions available to the role, as well as the type of user that can be assigned into the role (internal vs. external).
4.  Configure the permissions to grant to this role.
5.  Click **Create role**.
6.  You’re now ready to begin assigning users to this role

### Step 3: Modifying roles

Roles should be modified as your organization needs change.

1.  Select the role you wish to modify from the **Manage roles** tab.
2.  Review the current permissions associated with the role on the **Edit role** page.
3.  Edit the role details and permissions as needed.
4.  Save your changes.
5.  Updated permissions settings will now apply to all users with the role.

### Step 4: Role assignment

Assigning users to user roles gives control over the permissions a user or groups of users has in Asana.

1.  In the admin console, click **Manage members** on the left navigation bar.
2.  Locate the user you want to assign a new role to.
3.  Click the **Role** drop down.
4.  Select the new role to assign.
    1.  ***Tip: Learn more about managing member role assignment at scale through our IDP integration - if you’re managing roles through the IdP, your IdP will be the source of truth for user roles and will override changes in the admin console.***
        1.  Learn how to set up [Asana roles in Okta](https://help.asana.com/s/article/setting-up-asana-roles-in-okta-with-scim).
        2.  Learn how to set up Asana roles in [Microsoft Entra ID](https://help.asana.com/s/article/setting-up-asana-roles-in-microsoft-entra-id-with-scim).

> You can bulk assign roles through CSV user import. [Learn more](https://help.asana.com/s/article/csv-user-import).

### Step 5: Set role defaults

Role defaults set the role new users receive when joining Asana 

1.  In the admin console, click **Security** on the left navigation bar. 
2.  Locate the **Role defaults** setting. 
3.  Select the default roles for internal and external users. 

***Tip:*** *Role defaults apply when people sign up to join your organization, are invited by other users and in less common scenarios where automatic role assignment occurs. Select default roles with permissions you are comfortable with any user receiving by default. Users’ roles may always be adjusted from the Members tab in the Admin Console.*

## Frequently asked questions

### Role management 

**Who can create, manage and assign roles?**

By default, only super admins can create and manage roles for an organization. The standard admin role (and custom roles based on admin) can assign users to an existing user role, but cannot create new custom roles or modify role permissions. Super admins can manage admin user management permissions to either grant the ability to manage roles or restrict the ability to assign roles. 

Division Admins can create and manage custom roles for their division.

**Can the permissions of standard roles be modified?**

Yes, super admins can modify the configurable permissions associated with standard roles to better fit their organization's needs.

**If I create a custom role based on "Member" and updates are later made to the "Member" standard role, will my custom role also change?**

 No, the configurable permissions for custom roles are independent after creation. Changes to the configurable permissions of a standard role will not automatically apply to existing custom roles based on it. New custom roles created after changes are made to standard roles will use the current permissions of the standard role as the starting default. 

**Can a user have a unique role for each division they are a part of?**

No, a user has one role in the organization and cannot have a unique role for every division they are a part of. This role's permissions extend across all divisions for users that are in multiple divisions.

**Can an admin change the role of a user that is in multiple divisions?**

If an Admin changes the role of a user and that user belongs to multiple divisions, the admin would be displayed a warning that changing the user's role will apply to the user across all divisions they are a part of.

**Can I rename the standard roles to better fit my organization's terminology?**

No, standard roles may not be renamed.

**Can I customize the standard "Super Admin" role?** 

No, the permissions for the Super Admin role are fixed and cannot be modified.

**Can division admins manage roles within their specific division?** 

Yes, Division Admins can manage users' roles and create custom roles specific to their division within division admin console.

**Can I prevent a division admin from managing roles?**

If you are a super admin, you can set a domain configuration under **Security** that prevents division admins from managing or creating roles for users within their division.

### Role assignment

**Can I change the default role assigned to new internal or external users?** 

Yes, this can be done using the ‘Default role’ setting in the security tab of the admin console. Additionally, there are role-level defaults that set the role for new users invited by users with that role. We recommend using these defaults thoughtfully to avoid permission escalation.

**Can multiple roles be assigned to a single user?**

No, each user can only have one role assigned at a time.

**What user role does a user get assigned to?**

Everyone in Asana has a user role. Here are the different ways role assignment can happen:

- For existing users: When you transition over to using RBAC to manage user roles, users will retain their existing user role by default (Super admin, Admin, Member or Guest). From there, Super admins and Admins with user management permissions can add additional custom roles and assign users to roles. 
- For new users, the role the user receives can vary based on how they join your org:
  - Invited users: 
    - In-app invites: When users are invited to Asana from the app, the role the new user receives is the default member or guest role.
    - Admin console: When users are invited from the admin console, super admins and admins with role assignment permissions are able to set the role for the new user during the invite step 
  - Sign ups: When new users sign up from [Asana.com](http://asana.com) to join your org, they will receive the org-wide default role. This role starts out as the standard member role, but can be configured through the domain wide settings 
  - SCIM integration: if you’re managing roles through the IdP, your IdP will be the source of truth for user roles and will override changes in the admin console. Learn how to set up [Asana roles in Okta](https://help.asana.com/s/article/setting-up-asana-roles-in-okta-with-scim).  
- There are a few less common scenarios where users may receive a role automatically:
  - Domain migration: When a domain migration occurs, users from the source domain are assigned the target domain's org-wide default role. Changes to verified org emails: When a verified email address is added or removed from an organization, this can change existing users’ role type from external (guest) user to internal user or vice versa. When this happens, affected users will receive the org default role corresponding to their new role type. 
- **Tip: Manage role defaults to keep your org secure by ensuring that new users always have the right level of access to your org from the start.**

**What role will a user receive if they are invited by multiple users before accepting their invite?**

If a user is invited by multiple users before accepting their invite, they will receive the role from the first invite. If the user is invited by an admin from the admin console, this role assigned by the admin will take precedence over any other invite role. Super admins or admins with the role assignment permission can view pending invites and change users’ role in the admin console.

**If a user's role is changed, are they automatically notified?**

No, users are not automatically informed about role or permissions changes. 

**Are users able to see their role or request role changes from the Asana app?**

No, users are not able to see their user role and there is currently no way to request upgraded permissions through Asana. The user experience differs based on the permission; in some cases, features are completely hidden whereas for others, users see the feature in a disabled state.

**Can I assign custom roles** **that are made in other divisions within my organization?**
No, division admins can only assign custom roles that were created within their division to members of their division.

### Organization settings

**How do organization default settings interact with user roles?**

Organization default settings are in place for some of the permissions that may also be customized at the role level via RBAC. These settings can be accessed in the admin console in the Security and App settings tabs. They include:

- Guest invite and trusted domain setting 
- Upload files 
- Download files to mobile app 
- Use personal access tokens 
- Use Apps

If a permission is disabled or modified at the organization level using the organization default setting, this will override role permissions and it will not be configurable at the role level. In order to configure the setting at the role level, the org default setting must be turned on.

**I have previously used organization settings to change permissions in my domain. Will these defaults remain in place when I start using RBAC?**

Yes, when you begin using RBAC, the permissions settings that have been configured already for your domain will remain in place and be reflected in the permissions for RBAC roles. This means your starting defaults for standard roles may be different from what the Asana default for each role looks like. 

### Overall permissions framework

**How do user roles interact with permissions on projects or other work objects in Asana?**

The RBAC user role and permissions determine a user's capabilities across an entire Asana instance, whereas object access level permissions determine a user's capabilities specific to a particular Asana object. The Asana permissions system works together to address a range of access control use cases. 

The following table compares RBAC user roles with object access levels 

+---------------------------------------------+--------------------------------------------------------+--------------------------------------------------------+
| **Comparison**                              | **RBAC User Role **                                    | **Object Access Level**                                |
+---------------------------------------------+--------------------------------------------------------+--------------------------------------------------------+
| Who assigns the role?                       | Org super admin                                        | Object admin                                           |
|                                             |                                                        |                                                        |
|                                             | Division admin                                         |                                                        |
+---------------------------------------------+--------------------------------------------------------+--------------------------------------------------------+
| Where is the role managed?                  | Org admin console                                      | Object share modal or settings                         |
|                                             |                                                        |                                                        |
|                                             | Division admin console                                 |                                                        |
+---------------------------------------------+--------------------------------------------------------+--------------------------------------------------------+
| What is the scope of the role permissions?  | Applies org wide, across all objects                   | Applies to a single object                             |
+---------------------------------------------+--------------------------------------------------------+--------------------------------------------------------+
| Example permissions                         | -   Invite guests to Asana                             | -   Manage membership to the object                    |
|                                             |                                                        |                                                        |
|                                             | -   Delete anything in Asana                           | -   Delete the object                                  |
|                                             |                                                        |                                                        |
|                                             | -   Create teams                                       | -   Manage object settings                             |
+---------------------------------------------+--------------------------------------------------------+--------------------------------------------------------+

**How does a user’s license interact with their role?**

License and role are independent of each other but both affect what a user can ultimately do in Asana. 

- User access to features in Asana is determined by their license. 
- User permissions in Asana are defined by their role. 

In order to take an action in Asana, a user needs both a sufficient license and role. 

As an example, two users may be assigned the project manager custom user role in Acme org. This role has ‘Create company goal’ permissions on.

- User A has a full Enterprise license and can create company goals 
- User B has a View only license and may not create company goals because they are restricted by license type. User B must be upgraded in order to take all actions permitted by their role

## Troubleshooting tips

**Users can't perform actions despite having the appropriate role**

1.  Check if the action is restricted at the object level
2.  Verify that the permission is enabled for their assigned role
3.  Verify that the user has the proper license

## AI permissions

Asana's AI Permissions within RBAC allow admins to manage deployment of AI features on a role-by-role basis.

Admins can currently control four AI-related permissions within RBAC:

**Asana AI:** Disabling the top-level Asana AI permission disables the sub-permissions (e.g., Core AI, Proactive AI, etc.) for members of a particular role.

1.  **Core AI:** This sub-permission allows members of a particular role to engage with core Asana AI features for on-demand content creation, summarization, and analysis (e.g., smart chat, smart summaries, and smart editor).
2.  **Proactive AI: **This sub-permission allows members of a particular role to engage with Asana AI features that proactively generate content without direct user prompting (e.g., proactive summaries on goals or projects).
3.  **AI Automations:** This sub-permission allows members of a particular role to create and modify rules or automations using generative AI (e.g., AI Studio). If disabled, AI Automations owned by members of this role will not run.
4.  **Create and edit AI Teammates:** Controls whether members of the role can create and deploy agentic AI users within their domain.

### How do role-based AI permissions interact with organization-wide settings?

Organization-wide AI settings enable and disable Asana AI for all users within an organization, while RBAC AI Permissions enable similar choices solely for members of a particular role. Organization-wide AI settings can be found in the "Asana AI" section of the admin console. Organization-wide AI settings take priority over AI permissions within RBAC. This means that, for any user to access AI features, those features must first be enabled for the entire organization. If you have disabled Asana AI overall, no one can use it within your domain, regardless of their role-specific permissions.

### What is the default setting for AI permissions on my existing roles?

By default all AI permissions are **enabled** for all standard and custom roles. You must edit a role to disable these permissions and restrict access. If a user has AI permissions but the organization has turned off AI, the user will not be able to use AI features.

### What do users see if an AI permission is disabled for their role?

If a user's role does not include an AI permission, they will either not see the entry point for that feature, or the feature will appear as disabled. This indicates that their access has been restricted by an admin.

### Do these controls prevent users from interacting with AI entirely?

No — these controls are not intended to entirely shield users from AI. For example, users without AI RBAC permissions may be able to trigger AI Studio rules created and owned by others. If you wish to disable AI for your organization, use the organization-wide setting.

[](https://forum.asana.com/c/forum-en/tips/6)
