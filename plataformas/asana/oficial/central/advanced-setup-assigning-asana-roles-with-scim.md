---
fonte: https://help.asana.com/s/article/advanced-setup-assigning-asana-roles-with-scim?language=en_US
baixado: 2026-11-10
---

# Advanced setup: assigning Asana roles with SCIM

Beyond creating and updating members, SCIM can automatically assign Asana roles — Admin, Member, Guest, or a custom role — based on group membership or attributes in your identity provider. This article covers setup for **Okta** and **Microsoft Entra ID**; role mapping via SCIM isn't currently documented for Google Workspace or OneLogin.

## Related articles

- [SCIM provisioning for Asana](https://help.asana.com/s/article/scim-provisioning-for-asana)
- [Basic setup: provisioning and deprovisioning users with SCIM](https://help.asana.com/s/article/provisioning-and-deprovisioning-users-with-scim)
- [Advanced setup: provisioning View-only licenses with SCIM](https://help.asana.com/s/article/advanced-setup-provisioning-scim)
- [Role-based access control (RBAC) with custom roles](https://help.asana.com/s/article/role-based-access-control-with-custom-roles)
- [Setting SAML group mapping for licenses](https://help.asana.com/s/article/setting-saml-group-mapping-for-licenses)
- [SAML group mapping and SCIM interaction](https://help.asana.com/s/article/saml-group-mapping-and-scim-interaction)

## Before you begin

- You've already set up basic SCIM provisioning — see [Basic setup: provisioning and deprovisioning users with SCIM](https://help.asana.com/s/article/provisioning-and-deprovisioning-users-with-scim).
- **Super Admin roles can't be assigned through SCIM**, under either IdP. To designate a super admin, use the Asana admin console after completing super admin verification. SCIM can assign Admin, Member, Guest (Okta: not supported — see below), and custom roles only.
- Asana currently supports **one role per member**. If a member is eligible for more than one role through your IdP's group setup, you'll rank roles by priority (covered in each IdP section below) so the higher-priority role wins.
- **Role and attribute values can't contain spaces** — use an underscore in their place (for example, `custom_role_1`, not `custom role 1`).
- **If you also provision View-only vs. Enterprise licenses via IdP groups** (see [Advanced setup: provisioning View-only licenses with SCIM](https://help.asana.com/s/article/advanced-setup-provisioning-scim)), license groups must be prioritized above role groups wherever both live in the same priority-ordered list.
- Pick one system of record for roles — Asana's admin console, or your IdP. If you manage roles via SCIM, manual role changes made directly in the Asana admin console will be silently overridden the next time your IdP pushes an update for that member.

## Set up in Okta

### Requirements

- You've completed [Basic setup: provisioning and deprovisioning users with SCIM](https://help.asana.com/s/article/provisioning-and-deprovisioning-users-with-scim) for Okta.
- You're an Okta administrator with permission to add and update groups and applications, and to create custom attributes.

### Setting up the 'roles' attribute

1.  In the Asana application in Okta, go to **Provisioning \> Profile Editor \> Add Attribute**.
2.  Configure the attribute:
    1.  **Data type:** string array
    2.  **Display name:** role
    3.  **Variable name:** asana_role
    4.  **External name:** roles.^\[primary==true\].value
    5.  **External namespace:** urn:ietf:params:scim:schemas:core:2.0:User
    6.  Check **Define enumerated list of values**.
3.  In **Attribute members**, add one entry per role you plan to assign via SCIM — at minimum Admin and Member, plus any custom roles. **Guest** **isn't supported as an SCIM-assigned role in Okta.** Because guests use an external email domain, they can't be assigned a role through Okta SCIM for Asana.
4.  In the Asana Admin Console, go to **Manage roles**, and for each role click the three-dot icon and select **Copy ID**. Paste each role's ID into the matching **Attribute members** entry's **Value** field in Okta.
5.  Set **Attribute Type** to **Group** and **Group Priority** to **Combine values across groups**, then click **Save**.

Leaving **Attribute Type** as Group lets you manage roles on a group basis. Choose **Personal** if you'd rather manage roles per-member only.

### Setting up Okta assignment groups and mapping them to your custom attribute

1.  Go to **Directory \> Groups \> Add Group** and create one group per role (Admin, Member, and any custom roles).
2.  For each group, go to **Applications \> Assign applications**, assign the Asana integration, and set the **Role** attribute value to match that group's role.
3.  Click **Save and Go Back**, and repeat for every role group.

Only select one role per group.

### Assigning role groups to people

1.  Open a role group's **People** tab (Okta's term for your organization's members) and click **Assign people**.
2.  Use **Advanced search** to bulk-assign members, or search and add individually.
3.  Click **Done** once you've assigned everyone who needs that role.

### Changing roles individually

1.  Go to **Directory \> People** and search for the member.
2.  Open their **Groups** tab, find their current role group, and click the **x** icon to remove them from it.
3.  Add them to a different role group using the steps above — their Asana role updates to match on the next sync.

### Ranking role priorities

Asana supports one role per member. If a member is assigned to Okta groups mapping to more than one role, Asana uses whichever role group is highest in priority order.

- Rank roles with more permissions higher — for example, Admin above Member — so overlaps resolve to the more powerful role. Apply the same logic to custom roles.
- To reorder, go to **Applications \> Asana \> Assignments \> Groups** and drag groups into priority order using the handle on each group card.

If you also use Okta groups to manage Asana licenses (Enterprise vs. View-only — see [Advanced setup: provisioning View-only licenses with SCIM](https://help.asana.com/s/article/advanced-setup-provisioning-scim)), place license groups above role groups in this same priority list (for example: Enterprise, then View Only, then Admin, then Member).

## Set up in Microsoft Entra ID

### Requirements

- Asana's integration must already be set up in your Microsoft Entra ID account — see [Basic setup: provisioning and deprovisioning users with SCIM](https://help.asana.com/s/article/provisioning-and-deprovisioning-users-with-scim).
- Custom attribute creation must be enabled for the Asana application. Open the Entra portal with the schema editor forced on: [https://portal.azure.com/?Microsoft_AAD_Connect_Provisioning_forceSchemaEditorEnabled=true](https://portal.azure.com/?Microsoft_AAD_Connect_Provisioning_forceSchemaEditorEnabled=true) (or append ?Microsoft_ADD_Connect_Provisioning_forceSchemaEditorEnabled=true#view/ to your existing Entra URL).

### Set up the roles attribute and attribute mapping in Entra ID

1.  On the **Provisioning** tab of your connected Asana application, expand **Mappings** and click **Provision Microsoft Entra ID Users**.
2.  Check **Show advanced options**, then click **Edit attribute list for Asana**. (If this option isn't available, revisit the schema editor prerequisite above.)
3.  Add a new user attribute called **rbacRoles**, type **String**, and save.
4.  Back on **Attribute Mapping**, click **Add New Mapping**:
    - **Mapping type:** Expression
    - **Expression:** a Join/IIF/Instr formula that checks appRoleAssignments for each role value (for example "admin", "member", or a custom role's value) and outputs the matching Asana role ID:

`Join(",",`

`  IIF(Instr(Join("", AppRoleAssignmentsComplex([appRoleAssignments])), "\"value\":\"admin\"", , )>"0", "<asana_role_id>", ""),`

`  IIF(Instr(Join("", AppRoleAssignmentsComplex([appRoleAssignments])), "\"value\":\"custom_role\"", , )>"0", "<asana_role_id>", ""),`

`  IIF(Instr(Join("", AppRoleAssignmentsComplex([appRoleAssignments])), "\"value\":\"member\"", , )>"0", "<asana_role_id>", "")`

`)`

 

- **Target attribute:** rbacRoles
- **Match objects using this attribute:** No
- **Apply this mapping:** Always
- Skip the default value.

5.  To get each \<asana_role_id\>: in Asana, go to **Manage roles**, use the dropdown next to each role, and select **Copy custom ID**. Do this for every standard role (Member, Admin, Guest) and every custom role you plan to assign via SCIM. Super Admin is excluded — it's assigned only in the Asana admin console.

6.  Click **OK**, then **Save**.

**The order of roles in the expression sets assignment priority.** Roles listed first have higher priority — if a member belongs to multiple mapped groups, they get the highest-priority role listed. For example, a member in both a Member group and an Admin group receives the Admin role in Asana.

Role names can't contain spaces — use an underscore instead.

### Set up app roles

1.  In Entra, go to **Manage \> Users and groups**, then **application registration**.
2.  Click **Create app role** once per role, matching the roles configured in the expression above:

| **Role**    | **Display name**           | **Value**       | **Description**       |
|-------------|----------------------------|-----------------|-----------------------|
| Member      | Asana Members              | `member`        | Asana member role     |
| Admin       | Asana Admin                | `admin`         | Asana admin role      |
| Custom role | Asana `<custom role name>` | `custom_role_1` | Asana custom role \#1 |

Check **Enable this app role** for each, and click **Apply**.

Values set here must exactly match the naming used in the Expression mapping above — no spaces, underscores in their place.

### Create an Entra group for each Asana role and assign the role to the group

1.  Create one Entra security group per Asana role.
2.  Under the Asana enterprise application's **Users and groups**, click **Add user/group** and map each group to its corresponding app role.
3.  Add members to the appropriate groups. Once the next provisioning cycle runs (or you trigger [on-demand provisioning](https://learn.microsoft.com/en-us/entra/identity/app-provisioning/provision-on-demand)), Asana reflects the assigned role.

**Sequencing warning for first-time provisioning:** if you're assigning both a license and a role via Entra groups at the same time for a member being provisioned for the first time, do it sequentially — assign one (license or role) first, confirm the member is successfully provisioned, then assign the other. If you assign both at once, Entra will only register one of the two as an "update" for that member.

## Combining role and license provisioning

If you're also provisioning View-only vs. Enterprise licenses via SCIM (see [Advanced setup: provisioning View-only licenses with SCIM](https://help.asana.com/s/article/advanced-setup-provisioning-scim)), you're managing two attributes — license and role — in the same IdP, and in Okta's case, through the same priority-ordered group list. Here's what the end state looks like once both are set up correctly.

**In Okta**, both license groups and role groups live in the same **Applications \> Asana \> Assignments** priority list. License groups must rank above role groups, and within each category, rank higher-permission groups above lower-permission ones. For an organization with Enterprise/View-only licensing and Admin/Member roles, the final priority order should read, top to bottom:

1.  Asana - Enterprise *(license)*
2.  Asana - View only *(license)*
3.  Asana - Admin *(role)*
4.  Asana - Member *(role)*

A member in the Enterprise and Admin groups gets an Enterprise license and the Admin role. A member in only the View-only and Member groups gets a View-only license and the Member role, and so on — the highest-ranked group in each category wins if there's any overlap within that category.

**In Microsoft Entra ID**, license (userType) and role (rbacRoles) are two independent attribute mappings, each driven by its own set of app roles and Entra groups — they don't share a single priority list the way Okta's groups do. The one place they interact is during first-time provisioning: if you're assigning both a license and a role to a member for the first time, do it sequentially (assign one, confirm it applied, then assign the other) per the sequencing warning above, rather than assigning both Entra groups at once.

## Known limitations

- Role mapping via SCIM is currently documented only for Okta and Microsoft Entra ID — not Google Workspace or OneLogin.
