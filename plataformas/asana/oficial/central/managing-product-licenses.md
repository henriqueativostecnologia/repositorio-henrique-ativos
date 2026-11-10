---
fonte: https://help.asana.com/s/article/managing-product-licenses?language=en_US
baixado: 2026-11-10
---

# Managing product licenses

**Available on paid organization plans for users who have been assigned the** [**admin role**](https://help.asana.com/s/article/admin-and-super-admin-roles-in-asana?language=en_US)**.**

When your organization purchases multiple Asana products, each one is licensed separately. A single user can hold a different license, or no license at all, for each product your organization uses. From the [admin console](https://help.asana.com/s/article/what-is-the-admin-console?language=en_US), admins control exactly who can access each product and at what level. 

## How product licensing works

Each Asana product supports two license types. 

A full license (paid) unlocks complete access to the product and counts toward your bill. Full licenses are named after your organization's paid tier for that product. 

A limited license (free) grants limited access or capabilities and does not count toward your bill. Limited licenses are unlimited and named after what they allow someone to do.

When you assign a product license to a user, you choose whether that person gets full access, limited access, or no access at all.

## License types by product

The full license names below reflect the Enterprise tier. The exact name shown in your admin console will match your organization's purchased tier for each product.

| **Product**                   | **Full license**                   | **Limited license** |
|-------------------------------|------------------------------------|---------------------|
| Agentic Work Management (AWM) | Agentic Work Management Enterprise | View only           |
| Asana Service Management      | Service Management Enterprise      | Requester           |
| Command by Asana              | Command Enterprise                 | View only           |
| Timesheets and budgets        | Timesheets and budgets             | None                |
| Asana Client Management       | Client Management Enterprise       | Client              |

## How licenses affect billing

Full licenses are the only ones that count toward your subscription costs. You can assign limited licenses to as many users as you need at no additional charge.

## Base license requirements

Some products require another product's license as a foundation before they can be assigned. If a user does not have the required base license in place, you will not be able to assign them a license for the dependent product.

| **To assign this license**         | **Base license required**                       |
|------------------------------------|-------------------------------------------------|
| Agentic Work Management Enterprise | None                                            |
| Agentic Work Management View Only  | None                                            |
| Service Management Enterprise      | Agentic Work Management Enterprise              |
| Service Management Requester       | Agentic Work Management Enterprise or View only |
| Command Enterprise                 | Agentic Work Management Enterprise or View only |
| Command View Only                  | Agentic Work Management Enterprise or View only |
| Timesheets and budgets             | Agentic Work Management Enterprise              |
| Client Management Enterprise       | None                                            |
| Client Management Client           | None                                            |

A domain can have either Agentic Work Management or Client Management, but not both. Whichever one your organization has purchased acts as the base license, and the same dependency requirements apply regardless of which one it is.

## Licenses and access

A user's access to each product depends on the license assigned to them. 

If a user has no license for a product, they will be blocked when they try to access it and will need to contact their admin to request one. 

A limited license grants access to the capabilities tied to that license type, such as requester access in Service Management or view only access in Agentic Work Management or Command. 

A full license gives the user complete access to that product.

## Managing licenses in the admin console 

Admins manage all product licenses from the admin console. You can update licenses through any of the following methods:

### Update a license from a user's profile settings

1.  Navigate to the **Users** page in your admin console.
2.  Find the user and click into their profile settings.
3.  Click on the **Licenses** tab.
4.  For each available product, select the license you want to assign.
5.  Click **Save changes**.

### Update licenses in bulk

1.  Navigate to the **Users** page in your admin console.
2.  Select multiple users using the checkboxes.
3.  When the bulk actions bar appears at the bottom of the page, select **Change license**.
4.  Choose the product and license type to apply to all selected users. You can also remove licenses from users in this action.
5.  Click **Save changes**.

### Assign licenses when inviting a new user

1.  Navigate to the **Users** page in your admin console and click **Invite Users**.
2.  Enter the email address for each person you wish to invite.
3.  In the **Licenses** drop-down, select which licenses you want to assign them.
4.  Click **Send**. The licenses will be assigned once the user accepts their invite.

### Other provisioning methods

Licenses can also be assigned in bulk through [**CSV import**](https://help.asana.com/s/article/csv-user-import?language=en_US) or automatically through SCIM provisioning.

## Controlling AI spending per user

Alongside product licenses, admins can control each user's access to pooled AI spending. AI Studio credits cover automations built in AI Studio Pro, while AI requests cover agentic collaboration through AI Teammates, Dash, and Meetings. Turning off either toggle blocks that user from drawing on the corresponding spending pool without affecting their product license.

These controls appear on the same screens used to manage licenses: a user's profile settings, the bulk license editor, and the invite flow.

## FAQs:

**Can guest users be assigned licenses in the same way?**

Guest users can only be assigned Agentic Work Management and Client Management product licenses, and this will not affect your bill.

**What happens if I pause a user’s licenses?**

Pausing a user's account suspends their access, and any licenses assigned to them will not count toward your bill for the duration of the pause.

**Can division admins assign licenses?**

Only users with the admin role can assign licenses. If a division admin does not have the admin role, they can only move users in and out of their division.

**How do I turn off AI Teammates?**

Who can use AI Teammates is determined at the individual user level. Users who have access to consume AI requests will be able to use AI Teammates, while users who have this permission disabled will not.

To update this setting for a specific user, navigate to the admin console, select **Users**, and click into the **Licenses** column. Under the **AI spending** subheading, you will be able to toggle on or off the user's ability to consume AI requests, which will control the user's ability to use AI Teammates.

If you wish to update this control for multiple users at once, you can use the Import/Export CSV functionality to update users in bulk.
