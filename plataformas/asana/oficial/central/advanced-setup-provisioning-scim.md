---
fonte: https://help.asana.com/s/article/advanced-setup-provisioning-scim?language=en_US
baixado: 2026-11-10
---

# Advanced setup: provisioning licenses with SCIM

Beyond manually inviting members or using [CSV user import](https://help.asana.com/s/article/csv-user-import), super admins can automatically assign work management, work management view only, and add-on licenses as part of SCIM provisioning — so members get the right license type the moment they're created, based on their identity provider group or attribute.

### Related articles

- [SCIM provisioning for Asana](https://help.asana.com/s/article/scim-provisioning-for-asana) 
- [Basic setup: provisioning and deprovisioning users with SCIM](https://help.asana.com/s/article/provisioning-and-deprovisioning-users-with-scim)
- [Advanced setup: assigning Asana roles with SCIM](https://help.asana.com/s/article/advanced-setup-assigning-asana-roles-with-scim)
- [View only](https://help.asana.com/s/article/view-only)
- [Service accounts](https://help.asana.com/s/article/service-accounts)

## How it works

Asana supports SCIM 2.0 provisioning of licenses using the licenses attribute. Your identity provider sends a list of values for each provisioned member. 

Set licenses as a comma separated list with no additional whitespace in alphabetical order to prevent needless provisioning cycles. This will allow your IdP to appropriately identify when the data with Asana does not match that of the IdP.

For example:
For an enterprise user with the Timesheets and budgets and AI Requests add ons:

`"licenses":"ai requests,timesheets and budgets,work management"`

For a Asana Work Management view only user:

`"Licenses":"work management view only"`

All valid values can be found at [https://developers.asana.com/docs/scim](https://developers.asana.com/docs/scim).

You configure this by creating a custom licenses attribute in your IdP, mapping it to group membership or app role assignment, and letting your normal provisioning cycle apply it.

## Prerequisites

- An Enterprise or Enterprise+ plan with View-only licenses enabled.
- An Asana Service Account configured for SCIM — see [Set up an Asana Service Account for SCIM](https://help.asana.com/s/article/provisioning-and-deprovisioning-users-with-scim) in the basic setup guide.
- A SCIM connector already set up with your identity provider — see [Basic setup: provisioning and deprovisioning users with SCIM](https://help.asana.com/s/article/provisioning-and-deprovisioning-users-with-scim).

## Set up in Okta

### Requirements

- You're a super admin in Asana.
- You're an Okta administrator with permission to add custom attributes, groups, and application assignments.
- You've completed [Set up an Asana Service Account for SCIM](https://help.asana.com/s/article/provisioning-and-deprovisioning-users-with-scim) and basic Okta provisioning (above).

### Steps

1.  In the Asana application in Okta, under the **Provisioning** tab, confirm **Update User Attributes** is enabled.
2.  On the same tab, open **Profile Editor** and click **Add Attribute**. Enter:
    1.  **Display name:** Licenses
    2.  **Variable name:** licenses
    3.  **External name:** licenses
    4.  **External namespace:** urn:ietf:params:scim:schemas:core:2.0:User
    5.  **Description:** License provisioning
    6.  \[Optional\] Check **Define enumerated list of values**, and add attribute members for each desired license state. Examples:
        1.  Display name: enterprise, Value: ai teammates,work management
        2.  Display name: view only, Value: work management view only
        3.  Display name: timesheet users, Value: ai requests,timesheets and budgets,work management
    7.  **Attribute type:** Group
    8.  Click **Save**.

 

3.  Under **Directory \> Groups**, create groups for each license state — for example, **Asana - Enterprise** and **Asana - View only** — and assign members to whichever group matches the license they should receive.

4.  Open **Asana - Enterprise**, go to **Applications \> Assign applications**, assign the Asana integration to this group, and set the **Licenses** field to Enterprise (or whatever value is desired). Click **Save and go back**. Do so for each group you wish to provision.

5.  Under **Applications \> Asana \> Assignments**, reorder the groups so that the license state you wish to take precedence is listed first.

This ordering matters: if a member ends up in both groups, Okta applies the license from whichever group is highest in the priority list. Placing an Enterprise above View-only means Enterprise wins in a conflict — order them the other way if you'd rather View-only take precedence.

**Also assigning roles via SCIM in Okta?** License groups and role groups (see [Advanced setup: assigning Asana roles with SCIM](https://help.asana.com/s/article/advanced-setup-assigning-asana-roles-with-scim)) share the same Assignments priority list. License groups must be ranked above role groups. See the worked example in that article's "Combining role and license provisioning" section for what the full, correctly-ordered group list looks like.

6.  To assign or change a member's license, go to **Directory \> People** (Okta's term for your organization's members), find the member, and add or move them between the two groups from their profile.

## Set up in Microsoft Entra ID

### Requirements

- You're a super admin in Asana.
- You're a global administrator in Microsoft Entra ID.
- You've completed [Set up an Asana Service Account for SCIM](https://help.asana.com/s/article/provisioning-and-deprovisioning-users-with-scim) and basic Entra ID provisioning (above).

### Steps

1.  Enable custom attribute editing for the Asana application by opening the Entra portal with the schema editor forced on: [https://portal.azure.com/?Microsoft_AAD_Connect_Provisioning_forceSchemaEditorEnabled=true](https://portal.azure.com/?Microsoft_AAD_Connect_Provisioning_forceSchemaEditorEnabled=true)

2.  Connect your Asana domain to Entra using a Service Account, following steps 1–4 and 5.1–5.8 of [Microsoft's Asana provisioning tutorial](https://learn.microsoft.com/en-us/entra/identity/saas-apps/asana-provisioning-tutorial).

3.  On the **Provisioning** tab of your Asana–Entra application, click **Edit attribute mappings**, then **Provision Microsoft Entra ID Users** under **Mappings**.

4.  Click **Advanced Options**, then click **Edit Asana user attributes**

 

5.  Add a new attribute called **licenses**, type **String**, and click **Save**.

 

6.  Click **Add New Mapping** and configure:

- **Mapping type:** Expression

- **Expression:**

`Switch(SingleAppRoleAssignment([appRoleAssignments]), "work management view only", "Asana Enterprise", "ai requests,work management", "Asana View Only", "work management view only")`

- Skip the default value.

- **Target attribute:** licenses

- Click **OK**, then **Save**.

This expression checks the user’s app role in Entra. If the user has an Enterprise app role, it sends the “ai requests,work management” value to the licenses attribute. If the user does not have an app role assignment or are in the view only app role, it sends "work management view only". 

The result of the expression can be adjusted to work with additional licenses by changing the result of the expressions or by adding further app roles to check.

**Default when a member has both roles:** the expression above assigns **enterprise** if a member is assigned to both the Enterprise and View-only app roles (for example, if they belong to two groups with different roles). 

7.  Under **Manage \> Users and groups**, open **application registration**, then **Create app role** for each license state you wish to support. Their **Display Name** should match whta is used in the expression if you would like the expression to work. For the example expression above we would create two::

- Display name: **Asana Enterprise**; Value: enterprise; Description: Asana enterprise license; Allowed member types: Users/Groups; enabled

- Display name: **Asana View Only**; Value: view_only; Description: Asana view only license; Allowed member types: Users/Groups; enabled

Display names are case-sensitive — make sure they match the expression above exactly.

8.  From the **Users and Groups** page of the Asana–Entra application, select a user or group and click **Edit assignment** to assign the Enterprise or View-only app role. The license takes effect in Asana once Entra's next provisioning cycle completes.

If you wish to have more roles with different license states you will need to extend the Switch expression in step 7 with the role name and then the licenses value you desire.

Let's imagine that I want the default value for those without an app role or whose app role doesn't match any of the options to be **"service management requester"**

I want to have a role named **"IT support"** where its members receive an enterprise work management license and a service management license

I want to have a role named **"Timesheets users"** where its members receive an enterprise work management license and a variety of add ons.

The switch would look like the below:

`Switch(SingleAppRoleAssignment([appRoleAssignments]), "service management requester", "Asana Enterprise", "ai requests,work management", "Asana View Only", "work management view only", "IT support", "service management,work management", "Timesheets users", "ai requests,ai studio,timesheets and budgets,work management")`

## Additional resources

- [SCIM API documentation](https://developers.asana.com/docs/scim) — technical reference for developers
- [Basic setup: provisioning and deprovisioning users with SCIM](https://help.asana.com/s/article/provisioning-and-deprovisioning-users-with-scim) — general SCIM setup
- [CSV user import](https://help.asana.com/s/article/csv-user-import) — for one-time or manual bulk provisioning instead of ongoing IdP sync

Changes to a member's license type through SCIM may take a few minutes to take effect in Asana.

## Known limitations

- No guidance yet on rate limits or bulk-provisioning limits for license changes via SCIM.
- View-only license provisioning via SCIM is currently documented only for Okta and Microsoft Entra ID — not Google Workspace or OneLogin.

For scenarios not covered above, contact your account executive or [Asana support](https://help.asana.com/s/#chat).
