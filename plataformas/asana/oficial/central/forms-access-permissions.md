---
fonte: https://help.asana.com/s/article/forms-access-permissions?language=en_US
baixado: 2026-11-10
---

# Forms access permissions

The forms access permissions feature allows [super admins](https://asana.com/guide/help/premium/admin-console-admin-roles#gl-super-admin-vs-admin) to restrict form access to people who have an email address from their organization’s domain.

#### Related articles

- [Forms ](https://help.asana.com/s/article/forms?language=en_US)
- [Permissions overview](https://help.asana.com/s/article/permissions-overview?language=en_US)

## Admin controls

Super admins can set form access permissions for their entire domain on the Asana [Enterprise+](https://asana.com/enterprise) tier, as well as [legacy tier](https://asana.com/pricing-legacy) Legacy Enterprise.

#### To set form access permissions:

1.  Click on your profile photo
2.  Select **Admin console**

 

#### From the **Security** tab, you can:

1.  Head to **Admin Controls**
2.  Click on **Form access permissions**

 

#### From **Form access permissions**, you can:

- Allow project members to set form link sharing permissions. Forms in the domain may be public with no authentication required or internal-only requiring authentication before viewing or submitting a form, based on the settings configured by users for individual projects.
- Restrict access to emails associated with the organization domain.

> Allowing project members to set form link sharing permissions is suggested when there is a mix of internal and external use cases for forms.

When restricting access to emails associated with the organization domain, all new and existing forms in the domain will be ‘internal-only’ requiring authentication before viewing or submitting a form.

The authentication method depends on what the admin has enabled for the domain (Google SSO, SAML, or no authentication method). If no authentication method has been enabled, forms recipients must log in or sign up to view the form.

> Modifying this setting to **Organization only** could disrupt existing forms and workflows. Before making the change, we recommend notifying team leads and providing them time to review and adjust their workflows as necessary.

## Project level controls

**Setting form access permissions for projects is available** **on Asana [*Starter*](https://asana.com/plan/starter), [*Advanced*](https://asana.com/plan/advanced), [*Enterprise*](https://asana.com/enterprise), and [*Enterprise+ *](https://asana.com/enterprise)tiers, as well as [*legacy tiers*](https://asana.com/pricing-legacy) Premium, Business, and Legacy Enterprise.**

Form access permissions are available to users when the admin setting for the domain is set to **Allow project members to set form link sharing permissions**.

#### To set the form’s access permissions, project members need to:

1.  Click on **Share form**
2.  Select **Anyone with link** to set the form as public, with no authentication required to view or submit a form. This will allow you to share the form externally.
3.  Select **Organization only** to share it with organization members only. This will require the link recipient to authenticate before viewing or submitting a form.
4.  Click on **Done**

## Authentication for forms recipients

Forms recipients receiving a form with organization-only access enabled can access the form.

### For non-Asana members

Non-Asana members can authenticate with the identity provider for the domain to access the form, and will not be billed unless they complete their sign up for Asana. For domains with a password login, non-members of Asana must log in or sign up for Asana to access the form.

### For Asana members

They can access the form by signing in to their Asana account.

 

[](https://forum.asana.com/c/forum-en/tips/6)
