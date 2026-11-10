---
fonte: https://help.asana.com/s/article/setting-up-asana-roles-in-microsoft-entra-id-with-scim?language=en_US
baixado: 2026-11-10
---

# Setting up Asana roles in Microsoft Entra ID with SCIM

> Super Admin roles cannot be assigned through SCIM. To designate a super admin, use the Asana admin console after completing super admin verification. SCIM can assign admin and member roles only.

## Before you begin

- Make sure that [Asana’s integration has already been added to your Microsoft Entra ID account and is set up](https://help.asana.com/s/article/provisioning-and-deprovisioning-users-with-scim?language=en_US#gl-provisioning).
- You must enable the creation of custom attributes for the Asana application in Microsoft Entra ID. To do so, use the [this link](https://portal.azure.com/?Microsoft_AAD_Connect_Provisioning_forceSchemaEditorEnabled=true) to open the Microsoft Entra ID portal with the schema fully enabled.
  - Alternatively, append this bolded string to your URL
  - Add the /?Microsoft_AAD_Connect_Provisioning\_**forceSchemaEditorEnabled=true**\#view/

##

## Set up the roles attribute and attribute mapping in Entra ID

Once your Asana domain is connected, go to the **Provisioning** tab.

Expand **Mappings**, and under that, click **Provision Microsoft Entra ID Users**

Scroll to the bottom of the **Attribute Mapping** page, and check **Show advanced options**. This will display a few more options. Click **Edit attribute list for Asana**.

If this is not available to you, make sure that you have followed the step in [Before you begin](https://help.asana.com/s/article/setting-up-asana-roles-in-microsoft-entra-id-with-scim#before-you-begin) to open Microsoft Entra ID with the schema fully enabled.

On the **Edit Attribute List** page, add a new user attribute called **rbacRoles** as a **String type**. Save the attribute list.

Back on the **Attribute Mapping** page, click, **Add New Mapping.**

Set the **Mapping type** to **Expression**

Set the **Expression** to

- Join(",",
        IIF(Instr(Join("", AssertiveAppRoleAssignmentsComplex([appRoleAssignments])), "\"value\":\"admin\"", , )>"0", "1234567890", ""),
        IIF(Instr(Join("", AssertiveAppRoleAssignmentsComplex([appRoleAssignments])), "\"value\":\"custom_role\"", , )>"0", "1234567890", ""),
        IIF(Instr(Join("", AssertiveAppRoleAssignmentsComplex([appRoleAssignments])), "\"value\":\"member\"", , )>"0", "1234567890", "")
      )

In this expression, you are setting up the role name and grabbing the corresponding custom role ID from Asana to replace the set of numbers. The role IDs must be parametrized - the IDs (the numbers) are placeholder for demonstration and must be replaced by your own Asana custom IDs.

- **Important** - the role name cannot have a space - use an underscore in its place.

**Important** - the order of the role in the expression will determine the priority of role assignment. Roles at the top will have higher priority. Later, if a user is in multiple role groups, they will get the highest priority role as defined here.

- Based on this example, if an user is in both a **member** and **admin** role group in Entra ID, they will receive the **admin** role in Asana.

Skip the **Default value** field

Set **Target attribute** to **rbacRoles**, which is what we just created

Set **Match objects using this attribute** to **No**

Set **Apply this mapping** to **Always**

### To get the custom IDs from Asana

Navigate to the **Manage roles** page, click on the drop down to the right of each role, and click **copy custom ID**. Repeat this process for each standard role you plan to assign with SCIM, such as Asana member or admin, and for any custom role you have created. Super Admin roles are assigned only in the Asana admin console, not through SCIM.

The result should look like this:

Click **OK**, and **Save**.

## Set up app roles

Go to **Users and groups** under **Manage** in the left navigation pane. Click on **application registration** on this screen.

We’ll create app roles that match the roles you have set up. Click **Create app role**.

> Values set in each app role created here must match the naming in the Expression set above. The value cannot have a space. Use an underscore in the place of a space.

### Standard Asana roles

Member

- Display name: Asana Members
- Allowed member types: Users/Groups
- Value: member
- Description: Asana member role
- Make sure **Enable this app role** is checked

Admin

- Display name: Asana Admin
- Allowed member types: Users/Groups
- Value: admin
- Description: Asana admin role
- Make sure **Enable this app role** is checked

Custom roles: create more custom app roles to match all the custom roles you have set up

- Display name: Asana \<custom role\>
- Allowed member types: Users/Groups
- Value: custom_role_1
- Description: Asana custom role \#1
- Make sure **Enable this app role** is checked

Click **Apply** to save the app roles.

Add all other roles from your domain.

The result will look like this:

## Create an Entra group for each Asana role and assign the role to the group

Now, create an Entra group for each Asana role

Now we’ll assign the role to the group. Go to **Enterprise application** \> **Asana application** \> **Manage** \> **User and groups**:

Click on **Add user/group** and associate each group to their corresponding role:

The result will look like this:

Now the setup is complete and you can add the users to their corresponding groups to assign roles. When the next provisioning cycle runs, this configuration will assign the corresponding role to the users (alternatively, you can provision on demand) and you will see this reflected in Asana.

> If you are provisioning users for the first time, and are looking to assign **both license and role through Entra ID groups**, please do this sequentially - provision users into one of license or role groups first, and then once the user is successfully provisioned, then you can assign the other license or role group to the user. If not, Entra will only assign one attribute and does not read the other as an ‘update’ to the user.
