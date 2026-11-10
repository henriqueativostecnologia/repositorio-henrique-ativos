---
fonte: https://help.asana.com/s/article/read-only-links?language=en_US
baixado: 2026-11-10
---

# Read-only links

Read-only links are a shareable, view-only link that you can create for your timeline, list, calendar, and board views in projects with [team only](https://help.asana.com/s/article/project-permissions?language=en_US) and [shared with organization](https://help.asana.com/s/article/project-permissions?language=en_US) privacy settings within Asana organizations. They are not available in workspaces. Read-only links dynamically reflect the latest updates on projects and provide a living source of truth for all cross-functional teams to stay aligned.

The content and URL of these read-only links are not searchable or indexed in any search engine.

## Creating a shareable link

Read-only links are available for list, board, calendar and timeline view.

To create a public link, navigate to the project in question and click on your desired view.

1.  Click the project actions drop-down next to your project's name
2.  Click **Sync/Export**
3.  Click **Create a public link**

Only project admins can create read-only links.

#### From here you have the option to:

1.  Select who can access the link
2.  Copy the link
3.  Preview the link
4.  Turn off public sharing

## Previewing a shareable link

Preview your link before sending to see what it will look like for recipients.

Click on **Preview**  and a window will then open showing you a preview of your link. Previewing the link will offer you the option to join the project.

 

Recipients who are organization members can join the project to view task details, create new tasks, and collaborate with the team.

## Deactivating a shareable link

You can deactivate your shareable link at any time. This makes it inaccessible to anyone with the link. To do so, click **Turn off public sharing**. Next, confirm the deactivation by clicking **Deactivate link**.

If the read-only view is re-created, the link is refreshed meaning anyone with the old link will not be able to access it.

## Toggling link sharing permissions on and off

Admins can access **link sharing permissions** in the **Security** tab of their admin console.

 Organization admins can turn on or off read-only links directly in the admin console, whereas division admins will be prompted to open a [support request](https://help.asana.com/hc/en-us#chat).

Billing owners for paid team plans can [contact our Support team](https://help.asana.com/hc/en-us#chat) for further clarification.

## Access permissions for read-only links

This feature allows super admins and users to restrict read-only link access to people within their organization.

### Admin controls

The benefit is that super admins have the option to implement enhanced data security for their domain. Super admins of Starter, [Advanced](https://asana.com/plan/advanced), [Enterprise](https://asana.com/enterprise), [Enterprise+](https://asana.com/enterprise), and [legacy tiers](https://asana.com/pricing-legacy) **Premium**, **Business** and **Legacy Enterprise** organizations may still disable the read-only link feature for their entire domain, meaning users will not be able to create or share read-only links with anyone.

Super admins of **Enterprise**, **Enterprise+** and **Legacy Enterprise** organizations may set one of two access permission options for read-only links for their entire domain.

#### Option 1: Restrict access to email addresses associated with the organization’s domain

New and existing read-only links will be set to **organization only**, requiring authentication before access is granted. The authentication method required depends on which method the super admin has set for the domain (Google SSO, any SAML identity provider such as Okta, or none at all).

If no authentication method has been set, anyone attempting to access a read-only link must log in to Asana or sign up for Asana with their organization email address to gain access. This is the preferred option if restricting access to organization members only is required.

Users will not have the ability to make read-only views public to those outside the organization.

> Changing this setting to **organization only** could disrupt existing read-only links that have already been shared outside the organization. Before making the change, we recommend notifying team leads and providing some lead time to review and adjust workflows as necessary.

#### Option 2: Allow project members to set read-only link sharing permissions

Based on the settings configured by users for individual projects, read-only links in the domain may be set to **public** with no authentication required, or **organization only** with authentication required before accessing a read-only link.

This is the preferred option when users in the domain have a mix of internal and external use-cases for read-only links, such as regularly needing to share a read-only view of their project with an external partner, a consultant, or prospective client.

> With this option set, permissions for newly created views will be **organization only by default**, but project members have the option to make views public.

### Project-level controls

Users with Starter, [Advanced](https://asana.com/plan/advanced), [Enterprise](https://asana.com/enterprise), [Enterprise+](https://asana.com/enterprise), and [legacy tiers](https://asana.com/pricing-legacy) **Premium**, **Business** and **Legacy Enterprise** subscriptions can set access permissions for read-only links on a project-by-project basis.

Users can access these settings when the super admin enables domain-wide read-only project view sharing permissions for members.

This feature gives project members the option to implement additional security in cases where read-only views contain sensitive information or are intended for internal use only. The default permission setting for all newly created views is **People in your company**.

### People in your company

When this option is selected, the project read-only link will be internal-only, requiring the recipient of a read-only link to authenticate themselves before accessing the read-only view. The authentication method required depends on the method set for the domain (Google SSO, any SAML identity provider such as Okta, or none at all).

If no authentication method has been set, anyone attempting to access a read-only link must log in to Asana or sign up for Asana with their organization email address to gain access. This is the preferred option if restricting access to organization members only is required.

### Anyone with the link

When this option is selected, the project read-only link will be public, with no authentication required to access the read-only view. This is the preferred option if read-only links will be shared externally, such as with clients, vendors, or members of the public.

### Authentication for recipients of read-only links

Recipients of read-only links with **organization only** permission settings can access the view by authenticating themselves.

**People in your organization who have an Asana account** can authenticate themselves by signing into their Asana account.

**People in your organization who do not have an Asana account** can authenticate themselves in one of two ways:

- First, ensure people in your organization have access to Asana via your domain's identity provider (e.g., Okta, Google SSO). Once this is set, they can authenticate themselves upon receiving a read-only link. This does not require signing up for an Asana account. Read-only link recipients that authenticate with the identity provider to access the link are not considered full members and, therefore, cannot impact billing unless they go on to complete their sign-up.

- By signing up for an Asana account with an email address in the company domain, if the organization does not have an identity provider enabled.

Link recipients receiving a read-only link with **Anyone with the link** permission settings can access the read-only view without authentication.

## Limits

The number of tasks shown in a read-only link is limited to a maximum of 200. Sorts and filters can be used to maximize the number of relevant tasks within this limit.

> Like what you see? Get started with a free Asana trial today. [Try for free.](https://asana.com/create-account "Try for free")
