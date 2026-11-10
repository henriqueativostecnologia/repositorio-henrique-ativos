---
fonte: https://www.notion.com/help/guides/the-ultimate-quickstart-guide-to-notion-for-enterprise
baixado: 2026-11-10
---

# The ultimate quickstart guide to Notion for Enterprise

## Getting started with Notion for Enterprise gives you access to more customizability and control over admin, security, provisioning, and more. There are plenty of features to explore within your company workspace, so it’s important to understand the scope of what’s available.

- Enterprise
- External Agents
- Onboarding

20 min read

------------------------------------------------------------------------

## [Getting started with Notion Enterprise](https://www.notion.com/help/guides/the-ultimate-quickstart-guide-to-notion-for-enterprise#getting-started-with-notion-enterprise)

Getting started with Notion for Enterprise gives you access to more customizability and control over admin, security, provisioning, and more. There are plenty of features to explore within your company workspace, so it’s important to understand the scope of what’s available.

In this guide, we’ll discuss some of the most vital features available for Enterprise and a few best practices for building a clean, productive, and secure Notion workspace that meets your organization’s needs.

Learn more about security & compliance

For more information on security & compliance best practices on Notion Enterprise, check out this guide.

### [Setting up user types](https://www.notion.com/help/guides/the-ultimate-quickstart-guide-to-notion-for-enterprise#setting-up-user-types)

There are five types of users on Notion Enterprise, all consisting of varying levels of permissions, so it’s important to organize users based on their intended usage:

- **Organization owners** can manage organization level controls, Enterprise workspace owners need to first set up their organization and become or designate an Organization owner.

- **Workspace owners** have full access to all workspace settings and have elevated privileges, such as the ability to add new members. Every workspace must have at least one owner.

- A **Membership admin** is an administrative role built specifically for Enterprise user management that allows Workspace owners to delegate membership responsibilities. Ensuring members have access to the right workspace and relevant groups is often managed by IT teammates, Product Ops, or other functional Chiefs of Staff.

- **Members** are paid users and have full access to the workspace, including a personal section of the workspace. This is the default role when joining a workspace, and is a good role for most people at your company. All members are allowed to view, create, and share pages, and is a good way to maximize usage of Notion without granting additional administrative privileges.

- **Guests** are free users, but are limited to the specific pages that they’ve been granted access to and do not have a personal section of the workspace. These users are intended for external collaborators and are not supported by SSO & SCIM.

Notion has plenty of flexibility when it comes to user type delegation. As our customers grow on Notion, it’s a best practice to limit the number of workspace owners that have full access to all workspace settings (such as Audit Log, Content Search, and Identity & Provisioning) to a smaller administrative team.

### [Using teamspaces to organize information](https://www.notion.com/help/guides/the-ultimate-quickstart-guide-to-notion-for-enterprise#using-teamspaces-to-organize-information)

Teamspaces provide streamlined access to information by creating a dedicated area of your company’s workspace that can be customized to meet the requirements for a specific team or project.

Most organizations set up a company teamspace for all users, plus individual teamspaces for every department (like Product, Engineering, Marketing, Customer Success, etc.). Individual users can be added to specific teamspaces, limiting the information that is openly accessible.

Teamspaces can help organize information within and across departments at your organization.

**Creating Teamspaces**

To create a teamspace in Notion, you can click the `+` icon next to Teamspaces in the sidebar, or you can use the `New teamspace` button located in Settings \> Teamspaces.

Adding structure to teamspaces

To enforce a more structured workspace, you can limit teamspace creation to workspace owners only using the toggle under **Settings \> Teamspaces**.

*To learn more about how workspace owners can set up teamspaces,* [read our guide here](https://www.notion.com/help/guides/how-workspace-owners-can-set-up-teamspaces-for-their-organization)*.*

**Adding and Managing Teamspace Members**

By default, workspace members won’t see new teamspaces, though it’s easy to add members to specific teamspaces. In Teamspace settings \> Members, you can search existing workspace members or groups or add members manually via email.

Once a member is added to a teamspace, their role can be toggled between member or teamspace owner for additional privileges.

**Teamspace-Specific Settings**

Each teamspace has its own settings (separate from workspace settings) so you can control more granular options for each area that you create.

For organizations focused on ensuring that information stays secure within their workspaces, check the following settings to make sure they align with your needs:

- **Disable public page sharing** *—* dictates whether a page can be published to the web.

- **Disable guests** — limits sharing of current teamspace to workspace members only.

- **Disable export** — ** turns off the ability for users to export pages from this teamspace.

## [An Introduction to Workspace Settings](https://www.notion.com/help/guides/the-ultimate-quickstart-guide-to-notion-for-enterprise#an-introduction-to-workspace-settings) 

As a workspace owner, you can easily build out your organization’s Notion instance in a way that’s custom to your company. **Settings** is where you can control the finer details, like access and membership, permissions, plan and billing information, security, and more.

Before you start working in Notion, it’s important to understand what settings exist for your workspace and what they do. Let’s cover a few basics, then we’ll dive into specific sections in more detail later in this guide.

The Settings panel gives you access to in-depth workspace settings to customize Notion for your needs.

### [Settings *(Workspace owners only)*](https://www.notion.com/help/guides/the-ultimate-quickstart-guide-to-notion-for-enterprise#settings) 

This section is the starting point for many companies, as it’s where you set up a few of the most important basic settings that appear internally and externally.

- **Name** ** *—* set the name of your company’s workspace. This is often just your company name (we set ours to read *Notion*), but can be customized to what fits best.

- **Icon** — upload an image (usually your company logo) for your workspace.

- **Workspace Domain** — create a personalized domain for your workspace. This domain is used for two reasons:

  - Pages shared to the web will be shared using this domain (*\[domain\].notion.site*)

  - Anyone with an allowed email domain can join the workspace using this domain (*app.notion.com/\[domain\]*)

- **Allowed Email Domains** — add your workspace’s allowed email domains. Any users with email addresses that belong to the domain(s) listed here can automatically join your workspace. For most organizations, this is their company email domain (i.e., `acmeinc.com`). To get started, there needs to be at least one confirmed member with the domain before it can be added.

*For more information, continue on to the* [Allowed Email Domains](https://www.notion.com/help/guides/the-ultimate-quickstart-guide-to-notion-for-enterprise#user-provisioning) *section below.*

Widely-used public domains such as [gmail.com](http://gmail.com/) and [outlook.com](http://outlook.com/) can’t be set as allowed email domains.

### [Teamspaces *(Workspace owners only)*](https://www.notion.com/help/guides/the-ultimate-quickstart-guide-to-notion-for-enterprise#teamspaces) 

General teamspace settings allow you to control settings that apply globally to your workspace.

- **Default teamspaces** — choose the teamspaces that all new and current workspace members automatically join.

- **Limit teamspace creation** — toggle this setting on to only allow workspace owners the ability to create teamspaces.

- **Manage all teamspaces** ** — this section is where you can manage all teamspaces and their respective settings. See members, security settings, and access levels by teamspace.

### [Members *(Workspace owners & Membership admins only)*](https://www.notion.com/help/guides/the-ultimate-quickstart-guide-to-notion-for-enterprise#members)

Here is where Workspace owners and Membership admins can view and manage members, groups, and guests in the workspace.

- **Manage members and access** — make sure all members in your workspace have the right level of access and that they are in the correct teamspaces.

- **Set up permissions groups** — these allow you to easily manage page permissions and teamspace access in bulk, rather than on an individual member basis.

Managing permissions groups with an IdP

If you plan to leverage SCIM, we recommend creating and managing groups from your IdP to ensure they sync properly with Notion. Some SCIM applications may not support importing groups, meaning they won’t pull any groups created in Notion.

- **Monitor guest access** — **** review any guests that currently have access to your company’s workspace, and revoke access if necessary.

Adding guests in Notion

Guests can only be added at the page level via the Share menu.

- **View and manage users who have recently left the workspace** — **** view the log of members that left the workspace in the last 30 days. To prevent data loss, you can transfer ownership of those users’ private pages to another member (i.e., to their manager).

- **Manage workspace and guest requests** — **** members can request new people to be added as members or guests into your workspace. Workspace owners and membership admins can approve or decline these requests here. You can find more information about guest invite requests here.

Adding members without an IdP

If you aren’t using an Identity Provider (IdP), this is where you can also manually add/remove members.

### [Billing *(Workspace owners only)*](https://www.notion.com/help/guides/the-ultimate-quickstart-guide-to-notion-for-enterprise#billing) 

Workspace plan and billing information can be found here to help manage all aspects of billing in Notion.

- For customers on automated billing, you can update your plan and billing intervals (monthly vs annually) here

- For customers on quarterly true-ups via the Sales team, please work with your dedicated Account Management team for any questions about your Enterprise license

Billing with Allowed Email Domains enabled

The cost for any members who have joined the workspace via Allowed Email Domains will be added to your Enterprise License.

### [Security *(Workspace owners only)*](https://www.notion.com/help/guides/the-ultimate-quickstart-guide-to-notion-for-enterprise#security)

*Learn more about your workspace security settings in our guide here.*

### [Other Settings for Workspace Owners](https://www.notion.com/help/guides/the-ultimate-quickstart-guide-to-notion-for-enterprise#other-settings-for-workspace-owners)

**Identity & provisioning**

Verify your domain, manage workspaces that belong to your domain, and configure SAML SSO & SCIM in the `Identity & provisioning` tab. For more information, continue to the [Managing Users in Notion](https://www.notion.com/help/guides/the-ultimate-quickstart-guide-to-notion-for-enterprise#managing-users-in-notion) section below.

**Content Search**

Filter and search the workspace content and manage permissions on pages as needed. For more information, continue to the [Content Search](https://www.notion.com/help/guides/the-ultimate-quickstart-guide-to-notion-for-enterprise#content-search) section below.

**Connections**

With Notion’s API, you can connect other software tools to your workspace for even more functionality within your workspace. There are additional settings for managing these connections on the Enterprise plan so workspace owners can regulate who in the workspace can install them:

- **No restrictions** — all workspace members can install connections in the workspace

- **Only from approved list** — workspace members can only install connections that are pre-approved by a workspace owner

To learn more about managing connections in your workspace, please refer to our Help Center article here.

**Audit Log**

Provides an overview of a large range of events that have occurred in the workspace. For more information, continue to the [Audit Log](https://www.notion.com/help/guides/the-ultimate-quickstart-guide-to-notion-for-enterprise#audit-log) section below.

Make sure your Notion workspace is HIPAA compliant

Manage your settings at an organization level

If you're an organization owner, you can manage your security, data, and compliance settings at the organization level. Navigate to the workspace switcher and select `Manage organization`. Check [our guide](https://www.notion.com/help/guides/everything-about-setting-up-and-managing-an-organization-in-notion) to learn more.

## [Managing Users in Notion](https://www.notion.com/help/guides/the-ultimate-quickstart-guide-to-notion-for-enterprise#managing-users-in-notion) 

There are multiple ways to manage users in Notion depending on your organization’s preferences and needs.

### [User Authentication through SAML SSO](https://www.notion.com/help/guides/the-ultimate-quickstart-guide-to-notion-for-enterprise#user-authentication-through-saml-sso) 

Notion’s SAML SSO is built upon the SAML 2.0 standard, connecting your Identity Provider (IdP) and workspace(s) for an easier, more secure login experience. Notion supports official configurations for SAML SSO with: Azure, Google, Gusto, Okta, OneLogin, and Rippling.

To get started using SAML SSO with Notion, you will need to complete the following steps:

- **Verify domain(s)** — to use advanced security features, you must verify ownership of your email domain. This is an automated process that involves adding a TXT record onto your domain’s DNS to verify your ownership of it.

- **Enable SAML SSO** — **** this will toggle the feature on and complete the configuration. *For more information on completing the SAML SSO configuration, please refer to our* [IDP-specific guides](https://dev.notion.so/help/saml-sso-configuration)*.*

- **Change default login method** — once SAML SSO is enabled for the first time, the default login method will be set to `Any method`, meaning that users have the option of logging in via SAML or their normal login method. By setting this to `Only SAML SSO`, this enforces SAML as the login method for your workspace.

- **Link additional workspaces (optional)** — if you have more than one workspace you’d like to configure with SSO, you can do so by reaching out to [\[email protected\]](/cdn-cgi/l/email-protection#2d59484c406d404c4648434259444243034e4240).

Once properly configured, any members signing into your workspace(s) will need to use the verified domain and will need to be authenticated through your identity provider. Enterprise workspace owners are able to bypass by using an alternative login method in case there’s an IdP/SAML SSO failure.

Guests are not supported through SAML SSO or SCIM.

### [User Provisioning](https://www.notion.com/help/guides/the-ultimate-quickstart-guide-to-notion-for-enterprise#user-provisioning)

While most of our Enterprise customers leverage an Identity Provider (IdP) to provision new users, there are many ways to add a new user account to your workspace:

**Manually by Email**

Workspace owners and Membership admins can add a new member to the workspace by email under **Settings** \> **Members**.

**Allowed Email Domains**

Any users that login to Notion with your domain(s) listed in the Allowed Email Domains setting will be able to join the workspace as a member, and the additional cost will be added to your Enterprise License.

Allowed Email Domains and IdP

If you’re planning to manage the members that get added to your workspace strictly via your IdP, we recommend removing any domains listed in the Allowed Email Domains setting in **Settings \> Members.**

**Just-in-time (JIT) Provisioning**

Notion supports Just-in-Time provisioning when using SAML SSO. When **Automatic account creation** is enabled in **Settings \> Identity & provisioning**, any user who logs into Notion for the first time via your SAML SSO connection will have a new member account generated using the name and e-mail on the SAML response.

Using JIT and SCIM

We don't recommend enabling Just-in-Time provisioning if you are using SCIM, as there could be a mismatch between membership in your IDP and in Notion.

**Invite Link**

Under **Settings** \> **Members**, you’ll find an option to enable an invite link. Once enabled, you may share this link and anyone that visits it will be able to join your workspace automatically without the need for you to enter their email manually.

Notion’s SCIM API allows you to provision, manage, and de-provision members and groups in Notion.

**SCIM API**

Notion has a SCIM API which can be used to provision, manage, and de-provision members and groups. Workspace owners can find the required API key by going to **Settings** \> **Identity & provisioning** \> **SCIM Configuration** and clicking to view the token.

Please see [our SCIM documentation](https://www.notion.com/help/provision-users-and-groups-with-scim) for the latest information on how you can interact with Notion’s SCIM API. Notion supports official SCIM applications with Azure, Google, Gusto, Okta, OneLogin, and Rippling.

Getting started with SCIM

Configure and enable SCIM provisioning *prior* to assigning members to the application to ensure provisioned user identifiers are captured correctly.

Details about SCIM applications

The Google SCIM application does not support Group provisioning and de-provisioning. For other IdPs without an official application, you can reference our [SCIM API documentation](https://www.notion.so/help/provision-users-and-groups-with-scim) to set up a custom SCIM connection.

When setting up SCIM for multiple workspaces, while you can have one IdP tenant for SSO setup, you will need a separate application for each workspace as the API keys for SCIM operate only at the workspace level.

### [User De-provisioning](https://www.notion.com/help/guides/the-ultimate-quickstart-guide-to-notion-for-enterprise#user-de-provisioning)

When it’s necessary to de-provision a member, it’s important to remove them from a workspace and transfer their content to an existing member.

**Manually in Members tab**

Workspace owners and Membership admins can remove a user from the workspace under **Settings \> Members**. Sessions for these users are immediately terminated and they can’t rejoin a workspace themselves and must be added back manually or via SCIM.

**Automatically via SCIM**

SAML SSO doesn’t include automatic de-provisioning of users by itself. For this use case, you must be using our SCIM API with your Identity Provider to send requests for de-provisioning.

*Please see* [our SCIM documentation](https://app.notion.com/p/Provision-Users-and-Groups-with-SCIM-8797619fd6124a19aa280095f2ab9a95) *for the latest information on how you can interact with Notion’s SCIM API.*

**Transferring user content**

When a member leaves a workspace, they will appear under **Settings \> Members** in the **Recently Left** tab. From here, you can transfer their private pages to another user.

These pages will be packaged under one document now located under the newly selected member’s **Private** section in the left sidebar.

### [Visibility & controls for managed users](https://www.notion.com/help/guides/the-ultimate-quickstart-guide-to-notion-for-enterprise#visibility-&-controls-for-managed-users)

Enterprise workspace owners have additional settings that can help add more granularity and control over how their managed users work in Notion. Find these settings under **Settings \> Identity & provisioning \> User Management**.

Understanding "managed users" in Notion

A "managed user" includes any account created with the organization's verified email domain. Continue to the Managing your domain in Notion section below for more detail.

**Settings for managing users accounts**

Admins have access to multiple important settings that help manage and control user accounts in Notion.

- **Allow users to change account information —** set if users can change their preferred name, email address, and profile photo.

- **External workspace access —** control if managed users are able to join workspaces that are not owned by your organization.

- **Prevent managed users support access —** control which users can allow Notion support to remote login for troubleshooting. For more information on what Notion support can view, look at our terms of service.

- **Session Duration —** set how long a user can be logged in before they will be required to re-authenticate. This includes all devices a user is logged in on.

Changing default session duration

Notion has a default session duration of 90 days, but workspace owners can change this to a number of options from 1 hour to 90 days

- **Log out all users —** force all users to log out immediately.

- **Reset passwords for all users —** force all users to reset their passwords.

**Dashboard of managed users**

Click the `View dashboard` button to get an overview of all users in your verified domain. There, you’ll find information about each user, like their name, email address, workspaces, last activity date, and two-step authentication status.

Within each specific user account in this dashboard, workspace owners can perform the following actions:

- Suspend users

- Delete users

- Change user's name and email address

  - *Note: The new email must belong to the verified domain*

- Log out users

- Reset passwords

- Remove user from external workspaces

## [Managing your domain in Notion](https://www.notion.com/help/guides/the-ultimate-quickstart-guide-to-notion-for-enterprise#managing-your-domain-in-notion)

In addition to being a prerequisite to configure SAML SSO on Notion, once you’ve verified a domain, you can regulate and manage workspaces that belong to your verified domain(s). To do so, click `Browse workspaces` under **Settings \> Identity & provisioning \> Domain Management.**

To help mitigate concerns and confusion for future users, after a domain is verified, every time a new workspace is created using the verified domain, an email notification will be sent to the respective workspace owner alerting them that their workspace is eligible for domain management.

Initially verifying your domain

When you first verify a domain, there’s a 14-day notification period to inform all users that belong to that domain that their workspace(s) are eligible for domain management actions by their Enterprise workspace owners. During this period, you will not be able to act on any of the workspaces in the domain management view.

### [Customize workspace creation permissions](https://www.notion.com/help/guides/the-ultimate-quickstart-guide-to-notion-for-enterprise#customize-workspace-creation-permissions)

To help regulate the workspaces created using your verified domain, you can customize the permissions for who can create workspaces under **Identity & provisioning \> Domain management \> Workspace creation** and select Only workspace owners.

This setting only applies to workspace owners from the primary domain-verified workspace.

### [View unmanaged workspaces](https://www.notion.com/help/guides/the-ultimate-quickstart-guide-to-notion-for-enterprise#view-unmanaged-workspaces)

Once a domain is verified, Enterprise workspace owners can click `Browse workspaces` to view all non-Enterprise workspaces that users have created with their verified domain. There will be a tab for single member and multi-member workspaces. The following information will be provided in the view for each workspace:

- Workspace name

- Plan type

- Number of members

- Workspace owners

- Created at

- Created by

The actions available will show on the far right side.

### [Single member workspace actions](https://www.notion.com/help/guides/the-ultimate-quickstart-guide-to-notion-for-enterprise#single-member-workspace-actions)

In the single member tab in the workspace view, you will see all the personal workspaces that have been created using your verified domain.

#### Require account ownership change

For some customers to meet compliance requirements, they don’t want any work projects being stored in single member (personal) workspaces. In the workspace view, you will see the option to `Require account change` next to each single member workspace. This will require that the owner of the single member workspace provide a non-corporate email address for the user account before they can access the workspace again. This is a great option for employees that may have created a single member workspace with their company email, but mostly have non-work projects they’d like to keep for personal use . As a best practice, we recommend working with the respective workspace owners and to move any work related pages to a sanctioned Enterprise workspace prior to requiring the account owner change.

#### Delete workspaces

To help clean up stale single member workspaces that were owned by a former employee, you can delete the workspace from the workspace view under **Domain Management**.

When you delete a workspace, an email notification will be sent to the respective workspace owner informing them of this and providing your email address as the contact for any questions. Users will have the option for a one-time-only extension on the deletion period for an additional 30 days.

Domain management support

Notion’s support team cannot override any domain management actions by Enterprise workspace owners. If a user reaches out to Notion with questions, we will provide the email of the Enterprise workspace owner so the user can reach out directly.

#### Restore deleted workspaces

If needed, the workspace can be restored by the Enterprise workspace owner in the domain management view within 30 days.

The following content can not be recovered:

- Favorites

- Guest access

- Configured connections (Bots)

- Domains (custom Notion domains)

If the single member workspace is associated with a current employee, we advise caution before deleting the workspace in case it would be better to `Require account change` to a non-corporate email address and preserve the workspace settings.

Understand your workspace's data retention rules

### [Multi-member workspace action](https://www.notion.com/help/guides/the-ultimate-quickstart-guide-to-notion-for-enterprise#multi-member-workspace-action)

In the multi-member tab in the workspace view, you will see all the Plus and Business plan workspaces that are eligible to claim:

- Workspace was created using your verified domain

- Has at least one workspace owner (could be the creator or another workspace owner) still in the workspace that belongs to your verified domain

- Not on the Enterprise plan

#### Claim workspaces

To establish governance over authorized workspaces, you can claim eligible workspaces and upgrade them to the Enterprise plan. Once the claim is complete:

- An invoice for the Enterprise upgrade is sent to the billing contact you provided.

- The workspace becomes part of your organization and can be managed alongside your other claimed workspaces.

- Existing workspace roles and member access remain unchanged. Workspace owners remain owners, and members keep their current permissions.

- The workspace is now governed by [organization-level settings](https://www.notion.com/help/organization-level-controls), such as security policies and organization admin visibility. Domain claim does **not** change workspace ownership, members' roles, or their access to content within the workspace.

**Reminder:** Assign Membership Admins to claimed workspaces as needed to manage members and groups.

## [Workspace consolidation](https://www.notion.com/help/guides/the-ultimate-quickstart-guide-to-notion-for-enterprise#workspace-consolidation)

After claiming ownership of your workspaces and adding them to your Enterprise license, you may want to consider consolidating your users and content. Consolidating into a single, primary workspace (or small set of production workspaces) adds two primary benefits:

- **Standard and secure admin controls:** With all users and content in one place, it's easier to streamline admin controls and user management, instead of managing both across multiple workspaces.

- **More discoverable content and collaboration:** Since content will live in one workspace, it will be easier for users to find and access all of the content they need and collaborate in a single tool.

You can request a consolidation through your dedicated Account Management team. If you don’t have a dedicated Account Manager, you can reach out to our Support team at [\[email protected\]](/cdn-cgi/l/email-protection) for more information.

## [Data, Reporting, & Auditing](https://www.notion.com/help/guides/the-ultimate-quickstart-guide-to-notion-for-enterprise#data-reporting-&-auditing)

Enterprise workspace owners have access to additional data and reporting for greater insights into content and overall workspace usage. Whether you’re looking to export information, track and audit events, or search existing content, there are options available to help you do so.

For more information on data, reporting, and auditing, check out our guide on security & compliance here.

Share this guide

------------------------------------------------------------------------
