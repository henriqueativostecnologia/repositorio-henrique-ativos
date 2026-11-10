---
fonte: https://www.notion.com/help/set-up-enterprise-managed-connections-for-notion-mcp
baixado: 2026-11-10
---

# Set up enterprise-managed connections for Notion MCP

In this help doc

## Learn how to turn on enterprise-managed connections for Notion MCP and manage who can use it.

[Jump to FAQs](https://www.notion.com/help/set-up-enterprise-managed-connections-for-notion-mcp#faq)

------------------------------------------------------------------------

Enterprise-managed connections let your IT team manage how third-party AI tools like Claude connect to Notion, all in one place. Instead of each person approving the connection themselves, an admin sets it up once for everyone. Notion still checks each person's access and your workspace's admin settings on every request. You can set this up two ways: with your own identity provider, such as Okta, or by trusting Claude to confirm who's on your team, so any single sign-on provider works.

## [What to know before you start](https://www.notion.com/help/set-up-enterprise-managed-connections-for-notion-mcp#what-to-know-before-you-start)

- Your workspace needs to be on the Enterprise plan.

- You'll choose one issuer, which is the system that vouches for your members:

  - **Your own identity provider**, such as Okta. Your Notion sign-in must run on that provider.

  - **Claude auto-connect (beta)**, which confirms who's on your team. Your Notion sign-in can run on any SAML single sign-on provider.

- For the Claude path, you'll also need SAML single sign-on set up in Notion (any identity provider works) and email domains verified by your Notion organization.

- The AI tool needs to support enterprise-managed connections. Today, Claude is the only AI tool with this one-click setup.

- To set this up, you'll need a Notion organization owner (or a workspace owner if your workspace isn't part of an organization) and a Claude admin. If you set up with Okta, you'll also need an Okta admin.

## [How it works](https://www.notion.com/help/set-up-enterprise-managed-connections-for-notion-mcp#how-it-works)

Notion MCP normally asks each person to approve the connection between their app and their Notion account. With enterprise-managed connections, that approval step goes away for your team.

There are two ways this can work, depending on the issuer you pick.

**With your own identity provider (such as Okta):**

1.  A member signs in to Claude with your company's Okta SSO.

2.  When Claude needs Notion, Okta checks the rules your admin set and confirms the connection is allowed.

3.  Notion checks that the request really came from Okta, matches the member to their Notion account, and gives Claude the same access to Notion that the member already has. Nothing more.

**With Claude as the issuer:**

1.  A member uses Notion in Claude.

2.  Claude checks that the person is a current member of your Claude organization using their email address. It doesn't check a sign-in at your identity provider or multi-factor authentication.

3.  Notion checks that the member's email domain is verified by your organization, matches them to their Notion account, and gives Claude the same access to Notion the member already has. Nothing more.

Members won't see a Notion approval screen. Each connection stays active for up to eight hours at a time, and Notion checks your workspace's settings on every request. If you remove someone's access in Okta or remove them from your Claude organization, they won't be able to start a new connection, but a connection that's already active can keep working until it expires. To stop someone's access right away, disconnect them in Notion.

## [Set up enterprise-managed connections](https://www.notion.com/help/set-up-enterprise-managed-connections-for-notion-mcp#set-up-enterprise-managed-connections)

First, choose your issuer. If you use Okta to sign in to Notion, follow the Okta steps below. If you'd rather have Claude confirm who's on your team, skip ahead to [set up Claude auto-connect (beta)](https://www.notion.com/help/set-up-enterprise-managed-connections-for-notion-mcp#set-up-claude-auto-connect-(beta)) below.

Setting up with Okta takes three steps:

- Connect the apps in Okta

- Turn it on in Notion

- Turn on the connector in Claude

## [Connect the apps in Okta](https://www.notion.com/help/set-up-enterprise-managed-connections-for-notion-mcp#connect-the-apps-in-okta)

An Okta admin can follow the steps below to connect Claude and Notion MCP:

1.  In the Okta Admin Console, make sure SSO is turned on for both your Claude and Notion apps, and that Cross App Access is available.

2.  Add the connection between Claude and Notion MCP, and assign the users or groups it should cover.

3.  Note your Okta org's issuer URL (for example `https://acme.okta.com`). You'll enter it in Notion next.

For details, see [Configure Cross App Access](https://help.okta.com/oie/en-us/content/topics/apps/apps-cross-app-access.htm) in Okta's help center.

## [Turn it on in Notion](https://www.notion.com/help/set-up-enterprise-managed-connections-for-notion-mcp#turn-it-on-in-notion)

A Notion organization owner (or workspace owner, if you're not using organizations) can follow the steps below to connect your Okta account to your Notion workspace:

1.  Go to `Settings` → `Identity` → `Enterprise-managed connections`. If SAML is managed by a Notion organization, open the linked organization console.

2.  Turn on enterprise-managed connections and confirm your Okta issuer URL. It must match the Okta address that runs your Notion SAML SSO.

3.  Choose the one workspace this connection manages, then select `Turn on`.

## [Turn on the connector in Claude](https://www.notion.com/help/set-up-enterprise-managed-connections-for-notion-mcp#turn-on-the-connector-in-claude)

A Claude admin can follow the steps below to add Notion as an organization connector:

1.  In Claude's admin settings, go to `Connectors` and add the Notion connector (`https://mcp.notion.com/mcp`).

2.  Turn on `Enterprise managed authentication` for the connector.

3.  Run the connection test. When all checks pass, members can use Notion in Claude right away.

## [Set up Claude auto-connect (beta)](https://www.notion.com/help/set-up-enterprise-managed-connections-for-notion-mcp#set-up-claude-auto-connect-(beta))

If you don't use Okta, you can have Claude confirm who's on your team instead. You set this up from Claude, and nothing is copied by hand.

Before you start, you'll need:

- The Enterprise plan.

- SAML single sign-on set up in Notion. Any identity provider works.

  - If your organization has more than one SAML identity provider in Notion,

    `Connect Notion`

    can't pick one and stops with an error. Tell admins to contact Support.

  - An organization with one SAML identity provider can use Claude for one workspace. If that provider already manages another workspace, disconnect it there first.

- Email domains verified by your Notion organization.

- A Claude admin on a Team or Enterprise plan. This can be the same person as the Notion owner.

Setup starts in Claude, where a Claude admin follows these steps:

1.  In Claude, go to `Organization settings` → `Connectors` → `Notion` → `Managed authorization`, then select `Set up`.

2.  Choose `Claude-issued` as the identity source, then click `Connect Notion`.

3.  Approve the connection in Notion. A Notion organization owner (or workspace owner, if you're not using organizations) approves, and one person can do both steps. An organization custom admin with permission to manage enterprise-managed connections can also approve. When you see

    `Trust Claude to connect members?`, pick the workspace this connection will manage, then click `Trust Claude`.

4.  Back in Claude, click `Run test`.

5.  When every check passes, click `Enable and continue`, then choose who gets the connector.

6.  Members whose email domain is verified by your organization can now use Notion in Claude.

**Who can connect**

Only members whose email domain is verified by your Notion organization can connect, and their Claude email must match their Notion email. If a member can't connect, check that their domain is verified and their Claude and Notion emails match.

**One issuer per workspace**

Each workspace trusts one issuer at a time. To switch, first remove the current setup in Notion's Identity settings, then set up the new one. Each Claude issuer can connect to only one Notion workspace or organization.

You set this up from Claude, not by typing anything into Notion settings. Claude issuers that were pasted in earlier keep working. If `Connect Notion` doesn't work, contact Support.

## [Manage & monitor access](https://www.notion.com/help/set-up-enterprise-managed-connections-for-notion-mcp#manage-&-monitor-access)

- **Turn it off any time.** Turn off the connection in `Enterprise-managed connections`. Notion blocks any new requests and disconnects members who were connected this way. If you set up with Claude, turn it off in Claude under `Managed authorization` → `Disable`. To stop trusting Claude completely, also turn it off in Notion.

- **Remove one person.** Remove them from the connection in Okta so they can't reconnect. To end an active connection right away, disconnect the member from the *Disconnected members* list in Identity settings (or the MCP client roster). If you set up with Claude, remove the person from your Claude organization so they can't reconnect, then disconnect them in Notion to end access right away. Claude's directory sync removes deleted users, not suspended ones, so make sure the person is deleted from Claude.

- **Reusing an email address.** Notion matches members by email. Before you give a former member's email address to someone new, remove the former member's Notion account so the new person doesn't pick up their old access.

- **See who's connected.** Managed connections appear in your workspace's connected AI apps list, marked with the *IdP-managed* badge.

- **Audit everything.** Each member's first managed connection is recorded in the [workspace audit log](https://www.notion.com/help/audit-log) and sent to your security monitoring tools if you've set up the audit log event stream.

## [Troubleshoot the Claude setup](https://www.notion.com/help/set-up-enterprise-managed-connections-for-notion-mcp#troubleshoot-the-claude-setup)

In Claude, click `Run test` to check the connection. It runs a few checks, and each one points to what to fix.

[TABLE]

------------------------------------------------------------------------

## FAQs

Do members have to do anything?

No. Members just use Notion in Claude, with no approval screen.

What happens when someone leaves the company?

Remove them in Okta as usual, and they won't be able to start new connections. A connection that's already active can keep working for up to eight hours, so disconnect the member in Notion if their access needs to stop sooner. If you set up with Claude, remove the person from your Claude organization instead of Okta, then disconnect them in Notion to cut access right away. Claude's directory sync removes deleted users, not suspended ones, so make sure the person is fully deleted from Claude.

We already use Notion MCP with individual connections. What changes?

Members covered by the managed connection stop seeing approval prompts for Claude. Individual connections from other AI tools keep working as before.

Our Notion SSO doesn't run on Okta. Can we use this?

Yes. If you set up with Claude as the issuer, Claude confirms who's on your team, so your SAML single sign-on can run on any identity provider. If you use the Okta path instead, Okta must be the provider that runs your Notion SAML SSO.

What can Claude access?

Claude can access what each member can access in Notion. Enterprise-managed connections change how the connection is approved, not what it can access. Your existing Notion MCP admin controls, like the allowed AI apps list, still apply.

A member can't connect with Claude. What's wrong?

For a member to connect, two things must be true: their email domain must be verified by the same Notion organization that trusts Claude, and their Claude email must match their Notion email. Notion shows a general error that doesn't say which one failed, so check both.

A few other things can also block a member, like having no Notion account with that exact email, being a guest instead of a member, or being on the *Disconnected members* list. For the full list, see the Exchange for access token row in the troubleshooting table.

I see "this issuer is already connected to another workspace." What now?

That Claude issuer is already attached to another Notion workspace or organization. Each Claude issuer can connect to only one. Contact Support to sort it out.

Which AI tools are supported?

Claude organization connectors are supported. Support for more AI tools is coming.

## Contents

- [What to know before you start](#what-to-know-before-you-start)
- [How it works](#how-it-works)
- [Set up enterprise-managed connections](#set-up-enterprise-managed-connections)
- [Connect the apps in Okta](#connect-the-apps-in-okta)
- [Turn it on in Notion](#turn-it-on-in-notion)
- [Turn on the connector in Claude](#turn-on-the-connector-in-claude)
- [Set up Claude auto-connect (beta)](#set-up-claude-auto-connect-(beta))
- [Manage & monitor access](#manage-&-monitor-access)
- [Troubleshoot the Claude setup](#troubleshoot-the-claude-setup)
