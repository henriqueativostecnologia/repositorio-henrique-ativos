---
fonte: https://www.notion.com/help/guides/everything-about-setting-up-and-managing-an-organization-in-notion
baixado: 2026-11-10
---

# Everything you need to know about setting up and managing an organization in Notion

## Level-up how you manage your company with Notion’s organization level controls. Learn how to configure your settings and permissions effectively for your entire organization in one central place to manage users, permissions, and security settings. Finally, a streamlined way to keep everything secure and in sync at scale.

- Enterprise

12 min read

Organization level controls let you manage all your members, guests, and security settings in one place across multiple workspaces.

------------------------------------------------------------------------

As your team grows on Notion, keeping track of multiple workspaces and settings shouldn't slow you down. If different admins are running different workspaces, getting everyone on the same page can become an administrative maze. Without a birds-eye view, you may waste valuable time untangling confusing setups instead of focusing on more strategic work.

Notion's organization level controls unify everything you need in one place – from people to security settings and beyond. As an organization owner, you'll have a clean, intuitive admin console that lives outside the main product, giving you complete visibility and control over organization-wide settings across all your workspaces. Think of it as your command center — a single source of truth where you can see everything that's happening and make adjustments with just a few clicks.

In this guide, you'll learn how to:

- Set up your organization and assign organization owners to centralize your settings management

- Understand differences between organization owners and workspace owners

- Use the admin console to get a bird's-eye view of everything happening across your workspaces

- Use Notion's recommended settings to maximize your organization's security

## [Set up your organization](https://www.notion.com/help/guides/everything-about-setting-up-and-managing-an-organization-in-notion#set-up-your-organization)

When you set up an organization in Notion, claiming your company domain gives you better control and visibility over anyone or any space affiliated with that domain across Notion. Domain verification is your first step in managing organization level controls. It enables essential security and administrative capabilities — including consolidating multiple workspaces associated with your domain to your organization. It also unlocks domain management settings like [configuring SAML SSO](https://www.notion.so/help/saml-sso-configuration) for your workspace, using Notion integrations using [link previews](https://www.notion.so/help/link-previews-and-synced-databases#link-previews), and [controlling who can create workspaces](https://www.notion.so/help/domain-management#workspace-creation-permissions). Check out our [reference article](https://www.notion.com/help/domain-management#claim-workspaces) to learn more.

Select Add domain from the Identity settings sidebar to verify a domain for your workspace.

Once you've claimed your company domain, you can assign organization owners to handle all your organization-wide settings and controls.

## [Assign **organization owners for centralized control**](https://www.notion.com/help/guides/everything-about-setting-up-and-managing-an-organization-in-notion#assign)

Think of organization owners as super admins who have full control over organization-wide settings and permissions, including workspaces they aren't a part of. They also oversee other administrators, like workspace and teamspace owners, to ensure everything runs efficiently. Check out our helpful reference article to learn more about setting up organization owners.

Navigate to individual member settings to check if someone is an org owner.

For example, if your company has workspaces spread across North America, Europe, and Asia, updating basic security settings like password policies requires logging into each workspace separately. Without the right permissions, you'll need to ask other workspace owners to make even simple changes. With organization owners at the helm, you get a streamlined way to keep things consistent and running smoothly.

You can have multiple organization owners, but it's important to establish clear guidelines for working together. This helps keep everyone in sync when managing settings and permissions.

## [Organization owners Vs. Workspace owners](https://www.notion.com/help/guides/everything-about-setting-up-and-managing-an-organization-in-notion#organization-owners-vs.-workspace-owners)

With multiple roles in play, it's important to understand the key differences between organization owners and workspace owners:

- **Organization owners** serve as super admins with the highest level of control. They have authority over organization-wide settings and permissions, including workspaces they don't directly manage.

- **Workspace owners** manage their specific workspace with admin privileges, but face certain limitations when their workspace is part of an organization. Organization owner settings may restrict some of their controls.

Organization owners maintain a birds-eye view of organization settings and permissions through the hierarchical structure.

We recommend having organization owners serve as the primary decision makers for organization-wide settings and policies. To help them work smoothly with workspace owners, here are some helpful practices:

- **Document decision frameworks—** Write clear, simple guidelines about which decisions happen at which level - this helps avoid any confusion.

- **Set up feedback channels—** Create easy ways for workspace owners to share thoughts about policies and decisions that affect their teams.

- **Make changes simple—** Have a clear process for workspace owners to request changes to settings when they need to.

- **Keep everyone in the loop—** Let workspace owners know ahead of time about any changes that might affect their workspaces.

While organization-level controls help keep everything secure and running smoothly, they shouldn't get in the way of granular workspace settings. By following these practices, you can maintain security while giving workspace owners the flexibility they need to effectively manage their teams.

## [Our recommendations for managing organization level settings with the admin console](https://www.notion.com/help/guides/everything-about-setting-up-and-managing-an-organization-in-notion#our-recommendations-for-managing-organization-level-settings-with-the-admin-console)

When you take the wheel as an organization owner, the admin console serves as your dashboard, giving you a bird's-eye view of your people, share settings, security and compliance controls, and audit logs all in one centralized location.

To access the admin console, open the workspace switcher and select `Manage organization`.

Click "manage organization" in the sidebar to access the admin console.

The home screen lets you navigate through five key categories— **General**, **People**, **Security**, **Data & Permissions**, and **Analytics**. Here's how you can make the most of each setting:

### [**1. General settings**](https://www.notion.com/help/guides/everything-about-setting-up-and-managing-an-organization-in-notion#1.-general-settings)

The General tab gives you quick access to key organization settings. You can edit your organization's name, avatar, verified email domains, workspaces, team spaces, manage [SAML SSO](https://www.notion.com/help/guides/the-ultimate-quickstart-guide-to-notion-for-enterprise#managing-users-in-notion), and handle SCIM provisioning—all from one central location.

Manage your organization from the general settings to configure SCIM provisioning and SAML SSO settings.

Under this tab, when you select Manage workspaces, you'll see all workspaces connected to your organization. Click into any workspace to view and adjust its enabled features. For example, you can enable Notion AI for specific teams while keeping it disabled for others. The best part? You can manage all settings from one cohesive view—no more jumping between workspaces.

Admins can configure workspace-level settings directly from the admin console.

Notion’s recommended general settings

Here are our recommended settings based on common organizational needs—

- **Turn on** **`Enable SSO`—** SSO helps IT admins streamline user access across systems while giving end users a single, seamless access point.

- **Set your login method to** **`Only SAML SSO`—** This enforces SAML as the only login method, simplifying the experience for both end users and IT admins. You will be able to set up SAML SSO at the organization level, but keep in mind that at this time, we can only support one Identity Provider (IDP) per organization, so all your workspaces must be on the same IDP.

- **Turn off** **`Automatic account creation`—** This prevents new users from automatically creating Notion accounts through SSO, which helps when rolling out Notion in phases.

- **Turn on** **`Suppress invite emails from SCIM provisioning`—** This gives you control over how the Notion rollout is communicated internally and prevents automatic emails when you're not ready to announce the launch.

### [**2. People settings**](https://www.notion.com/help/guides/everything-about-setting-up-and-managing-an-organization-in-notion#2.-people-settings)

The `People` tab let’s you easily manage how members and guests appear and function within your organization. This includes managing user sessions and account access settings, like password resets and the ability to log out all users. Check out our reference article to learn more about the available settings.

The `Manage members` section lets you see everyone in your organization and which workspaces they belong to. This view is super helpful for keeping track of your members and managing billing. Instead of having to export member lists from each workspace and manually remove duplicates, you can see everything in one place. That way, if someone is in multiple workspaces, you can be assured they’ll only be accounted for once in a given billing cycle.

See which members belong to each workspace by filtering them by organization.

You can also click into any member to see their profile across all workspaces at once, which saves you from having to piece together their information from different places.

Click into any member to see their profile across all workspaces at once.

Configure guest settings at scale

### [**3. Security settings**](https://www.notion.com/help/guides/everything-about-setting-up-and-managing-an-organization-in-notion#3.-security-settings)

The security tab helps you protect your teams' information. You'll be able to set and manage security settings across all your workspaces - like who can share content externally, export pages, or add new team members. You can also control which apps and integrations your team can connect to keep everything secure.

Manage security settings like publishing pages, members, guests and integrations in the security tab.

Get alignment with workspace owners

The admin console lets you set organization-level settings that automatically cascade down through bulk apply. You can also designate some settings as workspace managed, giving you clear visibility into which settings apply where.

Let's say one of your workspaces, Shrimps Inc., contains highly confidential information. You want to prevent members from accidentally publishing sites and forms. In this case:

- Navigate to the Shrimps Inc. workspace row where it says `Enable for everyone `and change it to `Disable for everyone`

- When you do so, a `Bulk apply `option appears. Click on it to automatically apply the setting to all teamspaces associated with this workspace.

- When you're ready, click `Save changes `at the top right corner of the page

When you make bulk changes at a workspace level, they will cascade down to corresponding teamspaces. You can then manually tweak as needed.

When you make changes in bulk, they'll take effect right away across all the settings within that entity. For example if you apply the settings in bulk to a workspace, they will cascade down to all the teamspaces within. Remember, you can always fine-tune settings for individual team spaces later.

Configure security and data settings at the organization level

- **Turn on** **`Disable publishing sites and forms`**- This keeps your workspaces secure by limiting publishing to specific team spaces where needed. Only users who are both workspace and team space owners can enable publishing in their team space.

- **Turn on** **`Disable duplicating pages`**- This helps keep your content secure by preventing members from copying pages to other workspaces.

- **Turn on** **`Disable export`**- We suggest turning this off workspace-wide and enabling it only in team spaces that need it. Team space owners who are also workspace owners can enable this when needed.

- **Turn on** **`Allow guest invite requests`**- While members can't directly add guests, they can request to add them. This lets you review who gets access to what content.

- **Turn on** **`Allow member invite requests`**- Let members request to add new people to the workspace. You can review these requests in the Members section.

- **Turn off** **`Allow membership requests`**- We suggest using SSO to handle all user management, which works better than having users request to join.

We recommend disabling settings like publishing sites and forms at the workspace level first. Specific team spaces can then be granted these permissions as needed, balancing security with flexibility.

### [**4. Data & Compliance settings**](https://www.notion.com/help/guides/everything-about-setting-up-and-managing-an-organization-in-notion#4.-data-&-compliance-settings)

The `Data & Compliance` tab allows organization owners to access tools for content search and audit logs to ensure data governance and meet regulatory requirements.

The audit log is particularly helpful for understanding actions taken at both organization and workspace levels in a single view. For example, if you need to track workspace setting changes over time, the audit log provides a convenient timeline showing who made which changes and when.

Org owners can access detailed information about data and safety-related activity across multiple workspaces through audit logs.

### [5. Analytics settings](https://www.notion.com/help/guides/everything-about-setting-up-and-managing-an-organization-in-notion#5.-analytics-settings)

The `Analytics` tab helps you understand how your team uses Notion. You'll find helpful metrics like User Engagement that give you a clear picture of active members and guests. This makes it super easy to see how different teams are using Notion, track adoption, and keep an eye on guest access.

You can also explore detailed stats about how people interact with content across all your workspaces.

Org owners track page popularity and views across multiple workspaces to gain insight into content performance.

## [Notion’s recommended workspace settings](https://www.notion.com/help/guides/everything-about-setting-up-and-managing-an-organization-in-notion#notion%E2%80%99s-recommended-workspace-settings) 

- **Turn on** **`Limit teamspace creation to only workspace owners `—** Keep things organized by having only workspace owners create teamspaces. This helps prevent too many teamspaces from popping up and makes it easier to maintain a clear structure.

- **Turn on** **`Save and display page view analytics `—** See how your team is using Notion across the workspace. Everyone can check analytics for pages they have access to, making it easier to understand what's working well.

- **Remove all allowed email domains —** Keep your workspace secure by managing access through SSO only. We recommend making SSO your only sign-in method so you can control who joins through your identity provider. This is especially helpful if you're planning to roll out Notion to your team step by step.

Turn on page analytics and other workspace settings to optimize your experience.

Additional resources for enterprise admin tools

At its core, good organization management is about finding the right balance between security, flexibility, and ease of use. Our admin console puts all your settings in one place, making it simple to maintain this balance. This means you can keep your workspace secure and under control, while still keeping things easy and efficient for your team.

Share this guide

------------------------------------------------------------------------
