---
fonte: https://help.asana.com/s/article/scim-provisioning-for-asana?language=en_US
baixado: 2026-11-10
---

# SCIM provisioning for Asana

**Some SCIM capabilities (like assigning roles or view-only licenses automatically) require Enterprise+. **

SCIM (System for Cross-domain Identity Management) lets you automate how members are added to, updated in, and removed from your Asana organization by syncing directly from your identity provider (IdP). Instead of manually inviting members or updating their access one at a time, super admins can connect Asana to an IdP like Okta or Microsoft Entra ID and let user and group changes flow into Asana automatically.

This article is a starting point. Use it to understand what SCIM can do in Asana, confirm you're eligible, and find the right setup guide for what you're trying to accomplish.

### Related articles

- [Provisioning and deprovisioning users with SCIM](https://help.asana.com/s/article/provisioning-and-deprovisioning-users-with-scim)
- [Advanced setup: provisioning View-only licenses with SCIM](https://help.asana.com/s/article/advanced-setup-provisioning-scim)
- [Advanced setup: assigning Asana roles with SCIM](https://help.asana.com/s/article/advanced-setup-assigning-asana-roles-with-scim)
- [Service accounts](https://help.asana.com/s/article/service-accounts)
- [Setting SAML group mapping for licenses](https://help.asana.com/s/article/setting-saml-group-mapping-for-licenses)
- [SAML group mapping and SCIM interaction](https://help.asana.com/s/article/saml-group-mapping-and-scim-interaction)
- [Role-based access control (RBAC) with custom roles](https://help.asana.com/s/article/role-based-access-control-with-custom-roles)

## What SCIM can do in Asana

When connected to a supported identity provider, SCIM can:

- Create members in Asana automatically when they're assigned to the Asana app in your IdP
- Update member profile attributes (such as name, title, and department) to keep them in sync with your IdP
- Deactivate members in Asana when they're unassigned or deactivated in your IdP
- Provision teams: import Asana teams into your IdP, push IdP groups into Asana as teams, or link existing teams to IdP groups
- Assign licenses (Enterprise vs. View-only) automatically based on IdP group or attribute — see [Advanced setup: provisioning View-only licenses with SCIM](https://help.asana.com/s/article/advanced-setup-provisioning-scim)
- Assign Asana roles (Admin, Member, Guest, and custom roles) automatically based on IdP group or attribute — see [Advanced setup: assigning Asana roles with SCIM](https://help.asana.com/s/article/advanced-setup-assigning-asana-roles-with-scim)

SCIM does not currently support:

- Reactivating a member who was deactivated via SCIM
- Deleting a team in Asana (use the Admin Console's Teams tab instead)
- Assigning the Super Admin role (this always requires the Asana admin console and super admin verification, regardless of IdP)

## Supported identity providers

Asana supports SCIM 2.0 provisioning with:

- **Okta**
- **Microsoft Entra ID**
- **Google Workspace**
- **OneLogin**

Basic provisioning (creating, updating, and deactivating members) is available on all four for organizations on an Enterprise, Enterprise+, or Legacy Enterprise plan. Automatic role assignment via SCIM requires **Okta or Microsoft Entra ID** and an **Enterprise+** plan. Automatic View-only license provisioning via SCIM also requires **Okta or Microsoft Entra ID**, but is available on **Enterprise or Enterprise+** — it doesn't require Enterprise+ specifically.

> SCIM is available for organization-wide plans. It is not available for divisions.

A note on terminology: Asana calls provisioned people "members." Your identity provider may use a different term for the same thing — Okta calls them "People," Microsoft Entra ID calls them "Users." The setup guides below use each provider's own terminology when describing steps in that provider's console.

## SCIM capability matrix

| **Identity provider** | **Basic provisioning**                                      | **View-only licensing** | **Role mapping** |
|-----------------------|-------------------------------------------------------------|-------------------------|------------------|
| Okta                  | ✅                                                          | ✅                      | ✅               |
| Microsoft Entra ID    | ✅                                                          | ✅                      | ✅               |
| Google Workspace      | Supported — no first-party walkthrough yet; contact support | Not documented          | Not documented   |
| OneLogin              | ✅ (configured in OneLogin's own console)                   | Not documented          | Not documented   |

## Find the right setup guide

| **I want to...**                                                                  | **Go to**                                                                                                                                        |
|-----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Automatically create, update, and deactivate members as they change in my IdP     | [Basic setup: provisioning and deprovisioning users with SCIM](https://help.asana.com/s/article/provisioning-and-deprovisioning-users-with-scim) |
| Automatically assign Enterprise vs. View-only licenses as I provision members     | [Advanced setup: provisioning licenses with SCIM](https://help.asana.com/s/article/advanced-setup-provisioning-scim)                             |
| Automatically assign Admin, Member, Guest, or custom roles as I provision members | [Advanced setup: assigning Asana roles with SCIM](https://help.asana.com/s/article/advanced-setup-assigning-asana-roles-with-scim)               |
| Provision an add-on license (AI Teammates, Compliance management, etc.)           | [Advanced setup: provisioning licenses with SCIM](https://help.asana.com/s/article/advanced-setup-provisioning-scim)                             |
| Set a licensing division for DIPO                                                 | [Advanced setup: assigning a licensing division with SCIM](https://help.asana.com/s/article/setting-up-licensing-division-id-with-scim)          |

Most organizations start with basic setup, then layer on role or license automation once basic provisioning is confirmed working.

## Before you connect an identity provider

A few things apply no matter which IdP or which guide above you follow:

- **You'll need a Service Account.** Every SCIM integration authenticates using an Asana Service Account token, generated once from the Admin Console. See [Set up an Asana Service Account for SCIM](https://help.asana.com/s/article/provisioning-and-deprovisioning-users-with-scim) in the basic setup guide.
- **Attribute data synced via SCIM feeds all downstream Asana features**, including AI features like Asana Intelligence (Dash). If you don't want a specific attribute to surface in those features, remove or unmap it in your identity provider before it syncs to Asana — Asana doesn't provide a separate control to exclude individual synced attributes.
- **Provisioned members' email addresses must match your organization's domain.** Guests (external-domain members) are provisioned, deprovisioned, and managed only through the Admin Console's Members tab, not through SCIM.
