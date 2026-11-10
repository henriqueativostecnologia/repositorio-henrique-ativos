---
fonte: https://help.asana.com/s/article/email-domain-management-for-asana-organizations?language=en_US
baixado: 2026-11-10
---

# Email domain management for Asana organizations

An email domain is what comes after the @ in an email address. Companies typically have email domains featuring their names to ease identification. For example, John Smith works for a company named ACME. His email address is john.smith@acme.com, so the email domain in this case is acme.com. Your company must own and have full control over the email domains that are associated with your Asana organization. Public email domains such as @gmail.com, @hotmail.com, etc. are not eligible

- An organization can have multiple email domains

- Each email domain can only be tied to a single organization

- If an organization has already been created using the email domain you wish to add, the support team will guide you through the different solutions.

#### Related articles

- [Managing an organization](https://help.asana.com/s/article/managing-an-organization?language=en_US)
- [Data migration guide](https://help.asana.com/s/article/data-migration-guide?language=en_US)

## Manage your organization's email domains

Admins and super admins can manage an organization's email domains via the admin console.

> If there aren’t super admins in your organization, admins will need to go through a [super admin verification process](https://help.asana.com/s/article/admin-and-super-admin-roles-in-asana?language=en_US#gl-super-admin-verification). If you require assistance with this process, please contact your IT team.

To add a domain through the admin console:

1.  Click your profile photo and select **Admin console**
2.  Navigate to the **Security** tab
3.  Under **Roles** **and** **access**, click **Associated email domains**
4.  Select **Add email domain**
5.  Enter the domain you wish to add and click **Add**

## What is a DNS TXT verification?

To prove ownership of a domain, Asana uses DNS verification, which involves adding a specific record to the domain's DNS settings. This security measure ensures that only the legitimate owner can make configuration changes associated with that domain within your Asana organization.

If you are unsure on how to navigate your DNS system or how to add a TXT record, please get in touch with your IT team to assist with these changes.

## Verify the domain

1.  Add the provided TXT record to your domain's DNS settings ([view this section for a detailed guide](https://help.asana.com/s/article/email-domain-management-for-asana-organizations?language=en_US#adding-a-txt-entry-to-your-dns-system))
2.  Return to the admin console and click **OK**
3.  You can check the status of your domain by going back to the **Associated email domains **window

To view the TXT record again, navigate to the **Associated email domains **window, click the three dot icon of the pending email domain, and select **View TXT record**.

The DNS TXT record proves your ownership of the domain without affecting your website's operation. Once verified, the new domain will automatically be added to your organization.

To remove an email from your domain, click the three dot icon next to the email and click **Remove**. You’ll then have to follow the verification steps outlined above.

**Important considerations**:

- You must be a [super admin](https://help.asana.com/s/article/what-are-the-different-admin-roles-in-asana)
- You must have access to modify DNS records for the domain you wish to verify
- DNS changes may take up to 72 hours to become visible
- Verification attempts expire after 28 days
- When associating a new domain with an organization, all users who have created or will create an Asana account with a matching email address will be added as full members of your organization.
- Adding a new email domain to your organization may impact the number of seats needed on your organization's subscriptions. If this is the case, approval from all billing owners will be needed to proceed.
- Following the addition of an email domain to your organization, you may see some duplicate accounts in your organization. To resolve this, users with duplicate accounts will have to [merge them](https://help.asana.com/s/article/multiple-accounts-and-merging?language=en_US).

> You may need IT assistance for the process of adding and verifying email domains.

## Adding a TXT entry to your DNS system

1.  Copy the TXT entry generated within the admin console 
2.  You will then need to add the TXT entry to your domain host. If you're unsure what is your domain host, try one of the following methods:
    1.  Reach out to your IT department to complete these steps
    2.  Use the official [ICANN Lookup website](https://lookup.icann.org/)
        1.  Enter the new domain in the box (not your current domain)
        2.  Click lookup.
        3.  Your domain host is listed under **Registrar Information**
3.  Sign into the administrative site for the domain host you identified in Step 2
4.  Go to the page for managing DNS records. This might be called something similar to **DNS Management**, **Name Server Management**, **Control Panel**, or **Advanced Settings**.
5.  Select the option or click on the button for adding a new record
6.  For record type, select **TXT**
7.  For Name/Host/Alias, enter the value generated within the **Name, host or alias** field within the admin console 
8.  In the **Time to Live (TTL)** field, enter 86400 or leave the default value
9.  For the Value/Answer/Destination field, enter the code we’ve generated in your admin console within the **Record or data field** (asv=XXXXX).
10. Save the record
11. You may see a warning; don’t worry, adding a TXT record won’t damage your website or other settings

## Remove associated email domains

Email domains can’t be removed if they have active members.

> If you want to replace your domain, first add the new domain and then remove the old one.

To remove an email domain:

1.  Navigate to the **Settings** tab

2.  Under **Domain settings**, click **Associated email domains**

3.  Click the three dot icon next to the domain you wish to remove

4.  Click **Remove**

> Domains cannot be removed if their removal results in members turning into guests. To prevent this, you can add an email address from an alternative domain already associated with the organization. Learn how to [add email addresses](https://help.asana.com/s/article/account-settings).

## Adding domains with active guest users

If you add a domain that is being used by guests, under **Pending email domains** you’ll see a message saying “X users will be added from this domain” and will prompt you to confirm. If you confirm, the guest will be converted into a fully licensed user.

## Verification fails

If verification fails, you will see an error message with a link to contact support. You can try the verification process again or reach out to support for assistance.

## Common use cases

### Replacing an email domain

My company **Acme.com** is rebranding into **Acme-international.com,** and staff will receive new acme-international.com email addresses.

- Go through the [DNS verification](https://help.asana.com/s/article/email-domain-management-for-asana-organizations) to add the new domain to your organization.
- Once the domain has been successfully added, ask the members of your organization to add their new “@acme-international.com” email address to their account. Steps on how to do so are outlined [here](https://help.asana.com/s/article/account-settings#h_01HA4RE7XMSBH2JHFH3EG8SGZA).
- Remove the @acme.com domain.

### Adding additional email domains

My company **Acme.com** is acquiring new email domains: Acme.net & Acme.io

- Go through the [DNS verification](https://help.asana.com/s/article/email-domain-management-for-asana-organizations) to add the new domain to your organization.

### Merge two or more Asana organizations

Our companies are merging, and we both have existing Asana organizations. We'd like to merge our Asana data:

- Our migration team will guide you through the steps to migrate the data from one organization into the other. You can learn more about data migration in [this article.](https://asana.com/guide/help/organizations/data-migration)
- [](https://asana.com/guide/help/organizations/data-migration)Remember you still need to go through the [verification process](https://help.asana.com/s/article/email-domain-management-for-asana-organizations).

[](https://forum.asana.com/c/forum-en/tips/6)
