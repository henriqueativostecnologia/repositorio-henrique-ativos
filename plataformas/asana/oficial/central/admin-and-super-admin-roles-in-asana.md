---
fonte: https://help.asana.com/s/article/admin-and-super-admin-roles-in-asana?language=en_US
baixado: 2026-11-10
---

# Admin and super admin roles in Asana

**Available on Asana [*Starter*](https://asana.com/plan/starter), [*Advanced*](https://asana.com/plan/advanced), [*Enterprise*](https://asana.com/enterprise), and [*Enterprise+*](https://asana.com/enterprise) tiers, as well as [*legacy tiers*](https://asana.com/pricing-legacy) Premium, Business, and Legacy Enterprise.**

**Visit our [*pricing page*](https://asana.com/pricing) for more information.**

In Asana there are two organization-wide admin roles - **admin** and **super admin**. **Admins** have access to user and team management features as well as security settings for individual users. **Super admins** have access to the full set of admin features as well as security settings for the entire organization.

#### Related articles

- [How to access the admin console](https://help.asana.com/s/article/how-to-access-the-admin-console?language=en_US)
- [Admin security controls](https://help.asana.com/s/article/admin-security-controls?language=en_US)

As super admins can oversee organization-wide security features, the super admin role should be given to an IT administrator. The first super admin for an organization must go through a verification process. Once verified, super admins can then also give others super admin status without verification. This process restricts access to critical security settings to a limited number of users.

Only **organization members** can hold admin or super admin roles; guests cannot.

> Asana also supports team admins, though they do not have organization wide control, so are not discussed in this article. Learn more about team admins [here](https://help.asana.com/s/article/team-admin "here").

## Super admin vs admin

If you need to access additional controls, proceed with the super admin verification process.

- **Super admins** are usually IT administrators of an organization. They oversee capabilities such as SCIM and organization-wide password reset.

- **Admins** tend to be IT helpdesk or business leaders. They can access individual password reset and custom branding, as well as user- and team-management features.

> Like what you see? Get started with a free Asana trial today. [Try for free](https://asana.com/create-account)

### Admin and super admin permissions

Here is the transcribed table from the image in Markdown format, ready to copy and paste:

## Admin and Super Admin Permissions

| **Category**                        | **Capability**                                 | **Organization: Super Admin** | **Organization: Admin** | **Division: Super Admin** | **Division: Admin** |
|-------------------------------------|------------------------------------------------|-------------------------------|-------------------------|---------------------------|---------------------|
| **User Management**                 | Manage teams list                              | Yes                           | Limited                 | Limited                   | Limited             |
|                                     | View and edit profile settings                 | Yes                           | Yes                     | Yes                       | Yes                 |
|                                     | Edit a user's teams                            | Yes                           | Limited                 | Yes                       | Limited             |
|                                     | Remove individual users                        | Yes                           | Yes                     | Yes                       | Yes                 |
|                                     | View private tasks after deprovisioning a user | Yes                           | No                      | Yes                       | No                  |
| **Data**                            | Export CSV for teams and members               | Yes                           | Limited                 | Yes                       | Limited             |
|                                     | Export domain data                             | Yes                           | No                      | No                        | No                  |
| **Security**                        | Set Universal Reporting permissions            | Yes                           | No                      | Limited                   | No                  |
|                                     | Set default for team privacy settings          | Yes                           | No                      | No                        | No                  |
|                                     | Block integrations                             | Yes                           | No                      | Limited                   | No                  |
|                                     | Restrict Guest invites                         | Yes                           | No                      | Limited                   | No                  |
|                                     | Manage SAML authentication                     | Yes                           | No                      | Limited                   | No                  |
|                                     | Require Google Sign-in                         | Yes                           | No                      | No                        | No                  |
|                                     | Set org-wide password strength                 | Yes                           | No                      | Limited                   | No                  |
|                                     | Reset passwords org-wide                       | Yes                           | No                      | Limited                   | No                  |
|                                     | Reset individual passwords                     | Yes                           | Yes                     | Limited                   | Limited             |
|                                     | Log out individual users                       | Yes                           | Yes                     | Limited                   | Limited             |
|                                     | Reset 2FA for individual users                 | Yes                           | Yes                     | Limited                   | Limited             |
|                                     | Manage file attachment options                 | Yes                           | No                      | Limited                   | No                  |
|                                     | Manage SCIM                                    | Yes                           | No                      | No                        | No                  |
|                                     | RBAC                                           | Yes                           | Yes                     | Limited                   | Limited             |
| **Consistency and Standardization** | Set org-wide time periods for Goals            | Yes                           | Yes                     | Yes                       | No                  |
|                                     | Customize organization name                    | Yes                           | Yes                     | Yes                       | No                  |
|                                     | Customize organization branding                | Yes                           | Yes                     | Yes                       | No                  |
|                                     | Share org-wide announcements                   | Yes                           | Yes                     | No                        | No                  |
| **General Settings**                | Manage associated email domains                | Yes                           | Yes                     | Yes                       | No                  |
| **Integrations**                    | Manage service accounts                        | Yes                           | No                      | No                        | No                  |

### Permissions when enabling and disabling Asana AI features

Super admins of organizations can enable on or disable Asana AI features as outlined [here](https://help.asana.com/s/article/asana-ai-features-and-admin-controls?language=en_US). Admins of organizations that do not have any super admins can disable these features, but cannot enable them again. To enable them, you will need to complete the super admin verification process or contact the [Support team](https://asana.com/support). A warning banner will be displayed in-product before an admin makes this change. This also applies to divisions in Asana as divisions do not have super admins. In order to enable Asana AI features for a division, a division admin would need to complete the super admin verification process and become a super admin of the organization.

## View and manage admins and super admins

You can view and manage admins and super admins directly from the **Admin console**.

### View admins and super admins

1.  Click your profile picture and open the **Admin console**.
2.   Click the [**Members**](https://asana.com/guide/help/premium/admin-console#gl-members) tab.
3.   Use the **Member type** filter to view **Admins** and **Super admins**

This list shows the people in your organization who currently hold admin or super admin roles.

 

### Manage admins and super admins

From the same **Members** page, you can change roles, downgrade admins or super admins, or remove them from your organization.

1.  In the **Members** tab, find the person whose role you want to change. 
2.  Click the three-dot icon to open the actions menu. 
3.  Select **Change role** to update their role, or choose **Remove** to remove them from your organization.

Your options depend on whether the person is currently a member, admin, or super admin, and whether they meet the requirements to hold an admin or super admin role.

## Change admins

Use this section when you want to change who is an admin in your organization or adjust an existing admin’s role.

To change an admin:

1.  Open the **Admin console** and go to the **Members** tab. 
2.  Search for the person whose admin role you want to change. 
3.  Click the three-dot icon to open the actions menu. 
4.  Select **Change role**. 
5.  Choose **Admin**, **Super admin**, or **Member**, then save your changes.

If you change someone from admin or super admin to member, they will lose access to the admin console and any admin-only settings.

## Add an admin

You can make someone an admin when you invite them or by updating the role for an existing member.

To add an admin from the Members page:

1.  Open the **Admin console** and select the **Members** tab. 
2.  Click **Invite members** to add a new person, or search for an existing member in the list. 
3.  Click the three-dot icon next to their name and select **Change role**. 
4.  Set their role to **Admin**, then save your changes.

Only organization members are eligible to become admins. Guests cannot be admins.

## Add a super admin

The first super admin in your organization must complete a verification process that proves control of your organization’s domain. After at least one person is verified as a super admin, they can add additional super admins without repeating the verification.

### Super admin verification

In most cases, you will not need a super admin in your domain; if you do, you’ll see a message in the admin console that will guide you through verification. If you would like to pre-verify, you can do so by navigating to the admin console and clicking the **Security** tab, then click **Admin Access** and select to add a new super admin.

To protect the security and privacy of your company’s data within Asana, we require the first super admin in an organization to complete a verification process. This involves demonstrating the ability to modify the DNS records associated with the domains associated with your company’s Asana. Specifically, we will ask you to add a TXT record in a way that does not impact the operation of your website but does prove your ownership.

> In organizations, only the first user wishing to become super admin must undergo this verification process. That super admin can then add additional super admins once verified. DNS records can be deleted after verification.

### Adding the first super admin

To add your organization’s first super admin, click the **Add a super admin** button in the **Admin Access** section of your **Security** page in the admin console.

### The super admin verification process

1.  You will then receive instructions via email, similar to the above, from Asana, which will request that you add a DNS TXT record to one of the domains associated with your company’s Asana. The email from Asana will outline the steps you’ll need to complete.
2.  Once you’ve updated the DNS records, you will need to wait for the changes to become visible, which may take up to 48 hours but often happens much faster.
3.  Once the DNS changes are visible, use the link from the email you received to return to the admin console. Reopen the **Admin Access** section of the **Security** page and click on **Check Verification**.
4.  If you have successfully updated the DNS records, you will be promoted to super admin.

> If unsuccessful, you will be shown an error message and a link to contact our support page. Verification attempts expire after one week.

### Adding further super admins

In organizations, super admins can add other super admins

To add additional super admins, click the **Add a super admin** button in the **Admin Access** section of your **Security** page in the admin console.

## Troubleshooting super admin verification

### Troubleshooting and solutions for common issues

#### I'm receiving a verification error

* *

 

**If you receive an error after adding the TXT record, check the following in your DNS settings:**

- Check your entries for typos.
- Remove any extra spaces or characters.
- Make sure the record type is **TXT**, not CNAME or another type.
- Add the record to the domain you are verifying, not a subdomain or a different domain.
- In the **Host/Name** field, enter @ or leave it blank (depending on your DNS provider) to apply the record to your root domain, for example yourcompany.com. Do not type the domain name again if your provider adds it automatically, because that creates yourcompany.com.yourcompany.com.
- Make sure the TXT value matches the code exactly, with no added spaces. Do not type quotation marks yourself unless your provider requires them. Example: asv=xxxxxxxxxxxx
- Keep your existing TXT records (such as SPF). Add a separate record rather than replacing them.
- Remove any old or duplicate Asana verification records, and make sure the code in DNS is the most recent one.
- Save or publish your changes if your DNS provider requires it.
- Confirm that your DNS is hosted where you made the change. If your domain's nameservers are managed by a different provider, the record will not be visible.
- Wait and try again. DNS changes can take anywhere from a few minutes to 48 hours to take effect.

If the verification code has expired, generate a code and update the record.

 

#### How can I ensure the TXT was added correctly to my DNS?

1.  Go to **MXToolbox SuperTool**.
2.  Enter the email domain where you added the record (for example, yourcompany.com) in the search bar.
3.  In the dropdown next to the search bar, select **TXT Lookup**, then click the button.
4.  In the results, look for a TXT record containing asv=code.

**Tip:** You can also type `txt:yourcompany.com` directly in the search bar.

 

If the record does not appear, it might be due to an error as mentioned in the section above.

 

If your record still does not appear in MXToolbox after you have checked the items above, contact your DNS provider's support team for help. Asana cannot access your DNS settings, so your provider is best placed to troubleshoot this step.

## Remove or downgrade an admin or super admin

You can remove someone’s admin or super admin access by changing their role. You can also remove them from your organization entirely.

To downgrade an admin or super admin:

1.  Open the **Admin console** and go to the **Members** tab.  
2.  Find the person whose role you want to change.  
3.  Click the three-dot icon and select **Change role**.  
4.  Choose **Member** and save your changes.

To remove someone from your organization:

1.  In the **Members** tab, find the person you want to remove.  
2.  Click the three-dot icon.  
3.  Select **Remove** and follow the prompts.

Removing or downgrading someone changes what they can access. After this change, they lose any admin-only permissions and their access is updated based on their new role.

## Requirements and restrictions

Only organization members can be admins or super admins. Guests cannot hold either role.

The first super admin in an organization must complete domain verification before they can enable certain security controls or add more super admins. Once verification is complete, that super admin can add additional super admins without repeating the verification process.

If your company uses identity providers or SCIM, make sure your internal process for assigning admin and super admin roles matches how you want those roles to appear in Asana.

### Super admin roles with division plans

If your organization uses division plans, there are important considerations when managing super admin access.

With division plans, you pay for a subset of your organization rather than the full organization. Division admins can only see and manage members within their paid division, even after completing the super admin verification process.

### Understanding division admin visibility

**Division admin console access**: Super admins on division plans access the division admin console, not the organization admin console
**Limited member visibility**: You can only view and manage users who are part of your paid division
**Expected behavior**: Users outside your division (including those on free plans or other paid divisions) will not be visible in your admin console

### Adding super admins in division plans

The most straightforward approach is adding someone who is already a member of your paid division.

If the person you want to designate as super admin is currently in a different division:

- First add them as a member to your division (this assigns them a paid license)
- Then follow the standard super admin verification or assignment process

## View admins as an organization member

To view the admins for your organization:

1.  Click your profile picture in the upper-right corner
2.  Select **About my organization**
3.  Click **Admin access** to view a list of admins and super admins for the organization

# Frequently asked questions

### What is the difference between admin and super admin in Asana?

Admins can manage individual users and teams, reset individual passwords, and configure custom branding, while super admins can additionally manage organization-wide security features like SCIM and organization-wide password resets.

### Can guests become admins or super admins in Asana?

No, only organization members can hold admin or super admin roles—guests cannot be assigned either role.

### Does the first super admin in an organization require verification?

Yes, the first super admin must complete a DNS verification process by adding a TXT record to prove control of the organization's domain, though additional super admins can be added afterward without repeating verification.

### Can division admins view and manage all members in their organization?

No, division admins can only view and manage members within their paid division, even after completing super admin verification—users outside their division remain invisible in the admin console.

> Find best practices for admins shared in the [forum](https://forum.asana.com/c/forum-en/tips/6).

[](https://forum.asana.com/c/forum-en/tips/6)
