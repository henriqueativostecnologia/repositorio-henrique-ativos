---
fonte: https://help.asana.com/s/article/jira-server-faq?language=en_US
baixado: 2026-11-10
---

# Jira Data Center FAQ

**Please note that the Asana for Jira Data Center integration is scheduled to be deprecated on December 31, 2026**

**Available on Asana [*Starter*](https://asana.com/plan/starter), [*Advanced*](https://asana.com/plan/advanced), [*Enterprise*](https://asana.com/enterprise), and [*Enterprise+*](https://asana.com/enterprise) tiers, as well as [*legacy tiers*](https://asana.com/pricing-legacy) Premium, Business, and Legacy Enterprise.**

**Visit our [*pricing page*](https://asana.com/pricing) for more information.**

For a list of common questions on the Asana for Jira Data Center integration, see below.

#### Related articles

- [Jira Data Center](https://help.asana.com/s/article/jira-server?language=en_US)
- [Asana for Jira Cloud](https://help.asana.com/s/article/asana-for-jira-cloud?language=en_US)
- [Asana for Jira Cloud FAQ ](https://help.asana.com/s/article/asana-for-jira-cloud-faq?language=en_US)

## The authorization model

- The integration uses OAuth as the authorization standard. Users will remain authenticated until the OAuth token expires or until someone revokes that token.

- In order to link existing Jira issues to an Asana task or to create a new Jira issue from Asana you need to be authorized into your Jira account.

## How to check if you are using Jira Data Center

- Go to the URL that you use to log in to your Jira account.

- If your URL has this structure: “.atlassian.net” then you are using Jira Cloud, and you are not eligible to use the Data Center integration. You will need to use the Cloud version.

- If your URL does **not** have this structure: “.atlassian.net” then you are using Jira Data Center and are eligible to use this integration.

## Jira integration initial initiation

A Jira Admin has to create an application link for your Data Center instance to be able to connect to Asana. This is a one time occurrence. Once done, users within Asana will be able to individually authenticate to add to projects.

### Is this a one-way or two-way integration?

- When a user creates a new Jira issue or links to an existing Jira issue from Asana, we push the following from Asana into Jira:

1.  **Task name**
2.  **Description**
3.  **Attachments**

- This data becomes part of that new Jira issue. However this Asana \> Jira data transfer is a one occasion only data push that happens during the creation of a new Jira issue; this is also the only time we are pushing data from Asana into Jira.

- After the Jira issue is created, the Jira widget shows read-only data from the linked Jira issue. So technically speaking, the widget is just syncing data directly from Jira to Asana. The Jira widget will also work the same way when you link an existing Jira issue to an Asana task.

## Permissions and how they work

- When creating a new Jira issue from Asana, the integration follows Jira’s permission model. So a user can only create a Jira issue if they have permissions to do so in Jira. This is the only scenario where a user can write data into Jira (in order to create a new Jira issue). Similarly, this is also the only scenario where the integration reads Asana data.

- The integration reads Asana data, and creates a new Jira issue by writing (optional) some of the Asana task data (task name, description, and attachments) into the new Jira issue’s fields (issue name, etc.).

- Similarly users can only link existing Jira issues to an Asana task if:

- They’re authorized into their Jira account

- They have access to those specific Jira issues in Jira

- Once an issue has been linked to an Asana task, then the read permissions are controlled by Asana’s permissions model. For example, if a user links a Jira issue to task XYZ, then Asana users with access to Asana task XYZ can only see (read-only) the linked Jira issue’s data. If you want to keep the Jira data private within Asana, you have the option to make your projects or tasks private.

### Can we create or link Asana tasks to Jira issues in Jira?

No. The integration requires you to create a task in Asana, and then link it to an existing Jira issue.

## How to deauthorize from the integration or switch Jira account

Users can deauthorize by revoking access to the Asana for Jira Data Center integration in Jira.

1.  Go to Account Settings \> Connected Apps \> click **Revoke Access**

Next time the user tries to attach or create a new Jira issue, they should be prompted to reauthorize.

To connect a different Jira Data Center instance to your Asana workspace, please contact [Asana Support](https://asana.com/support "Asana Support").

[](https://forum.asana.com/c/forum-en/tips/6)
