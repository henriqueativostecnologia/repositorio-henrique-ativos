---
fonte: https://help.asana.com/s/article/audit-suite-api-and-integration-support?language=en_US
baixado: 2026-11-10
---

# Compliance management: API and integration support

Read more about Asana’s support for Audit Log, Security Information and Event Management (SIEM), Data Loss Prevention (DLP), eDiscovery, Archiving, and Cloud Access Security Broker (CASB) use cases.

Asana’s Compliance Management APIs  and Apps support your organization’s security and compliance posture. You can read more about the full suite of Compliance Management addon features [here](https://help.asana.com/s/article/compliance-management-add-on?language=en_US). Our Compliance Management APIs currently offer: 

1.  An **Audit Log API** that captures over a hundred security-and-compliance events and can be supported by most **Security Information and Event Management (SIEM)** vendors.
2.  A Resource Export API that supports **Data Loss Prevention (DLP)**, **eDiscovery**, and **Archiving** use cases; and several third-party integration partnerships in these areas.
3.  Support for **Cloud Access Security Broker (CASB)** vendors.

**Currently these are only available to Asana Enterprise+ tier, Legacy Enterprise tier, or organization-wide Enterprise subscriptions with the purchase of the Compliance Management add-on. **

If you would like to learn more about our Compliance Management features, please contact your sales representative.

## Audit Log API

Asana’s Audit Log API provides super admins access to an immutable log of key events across their organization. Using the Audit Log API, super admins can capture and act upon important security and compliance related changes.

## How to use the Audit Log API

Super admins can use Asana’s Audit Log API to:

1.  Set up proactive alerting with a Security Information and Event Management (SIEM) tool like Splunk
2.  Conduct reactive investigations when a security incident takes place
3.  Visualize key domain data in aggregate to identify security trends

### Event categories

Asana’s audit log API includes dozens of events, including:

1.  Key changes made by admins in the admin console such as `workspace_export_started`, `workspace_password_requirements_changed`, and `user_workspace_admin_role_changed`
2.  Critical user access events such as `user_login_succeeded`, `user_login_failed`, `user_invited`,and `team_member_added`
3.  Deletion events such as `task_deleted`, `task_undeleted`, and `portfolio_deleted`
4.  Export events such as `project_csv_export_initiated` and `workspace_teams_export_started`
5.  Data and asset management events, such as `attachment_uploaded` and `attachment_downloaded`

For a full list and details around the API endpoint, visit the [API documentation](https://developers.asana.com/docs/audit-log-events "API documentation")

### Retention period

Asana stores audit logs for 90 days from the date of capture. Those who would like a longer retention period may choose to use their SIEM or another storage solution for continuous log ingestion.

### Accessing the Audit Log API endpoint

Audit logs are accessible to super admins via service accounts. To see a detailed description of the audit log API endpoint, check out our developer documentation here.

To learn more about using Asana’s audit log API via Asana’s Splunk integration, visit Splunkbase to begin the installation process.

To learn more about using Asana’s audit log API via Asana’s Panther integration, visit their Asana Apps page.

## Audit Log CSV export

You can export a CSV of audit log events directly from the admin console. This is useful when you need a quick snapshot for incident review or want to share event data with stakeholders without setting up the audit log API.

To export a CSV of audit log events:

1.  Navigate to the **Admin console**
2.  Click on **Security** from the sidebar
3.  **ClickAudit log export **under **Audit log**
4.  Choose a date range that you want the audit log to include
5.  In the **Event types** field, select the event types you want to audit. You can select these individually, select all events of a given type, or select all event types.

Once you are ready to export your audit log, click **Request export.** Your export will be emailed to you.

## Data Loss Prevention (DLP)

Customers may wish to regularly scan their Asana instances for data that affects or violates their organization-wide policies.

For example, an organization may wish to conduct a monthly audit to find any instances of passwords being inadvertently entered into Asana tasks.

For customers and developers, to see a full list of details around the Resource Export API endpoint, visit the [API documentation](https://developers.asana.com/reference/createresourceexport).

> For detail about Netskope’s integration with Asana, visit the [Asana Apps page](https://asana.com/apps/netskope "Asana Apps page").

## eDiscovery

Customers may wish to pull data from Asana into a third-party eDiscovery tool to proactively plan for or reactively respond to litigation.

For customers and developers, to see a full list of details around the Resource Export API endpoint, visit the [API documentation](https://developers.asana.com/reference/createresourceexport).

> Visit [Exterro’s](https://asana.com/apps/exterro "Exterro’s") and [Hanzo's](https://asana.com/apps/hanzo "Hanzo's") Asana Apps page to learn more about their third party integrations with Asana. Stay tuned for additional partnerships coming soon.

## Archiving

Customers in highly-regulated industries may wish to regularly pull/store objects or events related to changes on objects in Asana.

For customers and developers, to see a full list of details around the Resource Export API endpoint, visit the [API documentation](https://developers.asana.com/reference/createresourceexport).

> Learn more about Theta Lake's integration with Asana by visiting their [Asana Apps page](https://asana.com/apps/thetalake "Asana Apps page")

## Cloud Access Security Broker (CASB)

Customers may wish to control use of Asana via their Cloud Access Security Broker (CASB) provider. Asana currently offers a connector with Netskope and support for setting [approved workspaces](https://help.asana.com/s/article/manage-approved-workspaces). Please visit [this article](https://help.asana.com/s/article/manage-approved-workspaces) to learn more about managing approved workspaces.

> For detail about Netskope’s integration with Asana, visit the [Asana Apps page](https://asana.com/apps/netskope "Asana Apps page").

 

[](https://forum.asana.com/c/forum-en/tips/6)
