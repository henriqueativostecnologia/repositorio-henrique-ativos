---
fonte: https://help.asana.com/s/article/service-accounts?language=en_US
baixado: 2026-11-10
---

# Service accounts

**Available on Asana [*Enterprise*](https://asana.com/enterprise) and [*Enterprise+*](https://asana.com/enterprise) tiers, as well as [*legacy tier*](https://asana.com/pricing-legacy) Enterprise.** **Visit our [*pricing page*](https://asana.com/pricing) for more information.**

**Service accounts are not available to divisions.**

Service accounts enable Asana **super admins** to have complete access to all data in their organization and export it through the Asana [API](https://asana.com/guide/help/api/api "API"), allowing for more powerful reporting options and building automations and integrations more easily.

Admins can also limit service accounts access to specific uses, such as user provisioning through SCIM. This limited access reduces security risks associated with the API token’s usage.

Find more information on how to use Asana API [here](https://developers.asana.com/).

### Use service accounts to:

- Create periodic data backups
- Automate user and access management based on your company's policies
- Provide automation for recurring administrative tasks like team member management and cleaning up inactive projects
- Add customized business rules triggered by actions within Asana
- [Export](https://developers.asana.com/docs/organization-exports "Export") your organization's data using the Asana API
- Build organization-specific integrations between other internal tools and Asana, and much more

Super admins can view the list of service accounts through the **Apps** tab of their admin console at any time and rename or deauthorize accounts that are no longer needed. You can provide service accounts with a name and profile picture, and action items as you would from a regular user account.

> Use service account tokens as organization-level substitutes for [Personal Access Tokens](https://help.asana.com/s/article/api?language=en_US "Personal Access Tokens").

## Adding service accounts

#### To add a service account:

1.  Click the **Apps** tab from with your admin console
2.  Click **Service accounts**
3.  Click the **Add Service account** button

From here you can choose scoped or full permissions.

 

1.  Click scoped permissions to limit access and check the boxes you want the app to have access to. Read more about the scoped permissions below.
2.  Click full permissions to give access to all data.

### Scoped permissions overview

#### User provisioning (SCIM)

This set of permissions allows access to Asana’s system for cross-domain identity management (SCIM) API endpoints. Identity provider integrations use SCIM to manage a user’s lifecycle in Asana, including provisioning and deprovisioning users, updating user attributes in Asana, and syncing Asana team memberships. Read Asana’s [SCIM documentation](https://developers.asana.com/docs/scim) for more detail.

- Users: Read
- Users: Create and modify
- Teams: Read
- Teams: Create and modify

#### Audit logs

The Audit logs permission is available to Enterprise+ domains and gives access to the [audit log events API endpoint](https://developers.asana.com/docs/audit-log-events). This API powers Security information and event management (SIEM) tools like [Splunk](https://asana.com/apps/splunk) and [Sumo Logic](https://help.sumologic.com/docs/integrations/saas-cloud/asana/) which can monitor and alert on suspicious activity in Asana.

#### Exporting

This set of permissions is available to Enterprise+ domains and gives access to [organization exports](https://developers.asana.com/reference/organization-exports) and object exports over the API. These endpoints can be used to extract information from Asana and power some Reporting and eDiscovery tools.

- Organization Export API
- Object Export API

#### Workspace Events

Provides access to the Workspace Events API, a continuous stream of workspace-level change events. Use for activity monitoring, security and compliance workflows, as well as for keeping external systems in sync. Available on Enterprise+ or Enterprise with Compliance Management add-on.

#### AI Studio Usage API

Provides read-only access to the AI Studio Usage API, which includes two endpoints: credit utilization (showing AI Studio runs with details about what ran, who owns it, the model used, and credits consumed) and seats (showing a current snapshot of who holds an AI Studio seat, at what tier, and in what state).

## Managing service accounts

Click the three dot icon next to an existing service account and click **Edit**.Service accounts with full permissions have full programmatic access to your organization's data. Make sure not to hardcode service account tokens into your programs, and regularly review and deauthorize tokens no longer in use.

From the **Edit service account** window, you can save your edits or delete the service account.

> You will not be able to log in to Asana as a service account. Service accounts only interact with your organization through the Asana API.

[](https://forum.asana.com/c/forum-en/tips/6)
