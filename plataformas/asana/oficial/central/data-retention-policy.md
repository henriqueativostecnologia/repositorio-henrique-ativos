---
fonte: https://help.asana.com/s/article/data-retention-policy?language=en_US
baixado: 2026-11-10
---

# Data retention policy

**Available on Asana [Enterprise+ o](https://asana.com/enterprise)r Enterprise with [Compliance Management addon](https://help.asana.com/s/article/compliance-management-add-on?language=en_US). Visit our [pricing page](https://asana.com/pricing) for more information.**

The data retention policy targets inactive work data for removal and will result in the deletion of inactive data. Users have the opportunity to recover trashed data within the first 30 days if the data is still needed.

## Data types affected

The policy currently covers the following data objects:

- Asana projects
- Tasks that are not in projects
- Messages between members

For more details on the scope of data coverage see visual below. 

## Duration for inactivity

Date will be eligible for deletion after a specified period of inactivity defined by organization admins. Generally inactivity includes any modifications to data

### What qualifies as inactive?

- None of the following project activities have occurred:
  - Edits to project fields - including updates or edits to name, description, archiving, project team/owner, status updates and messages, etc.,
  - Any activity in tasks within the project - see task activities listed below
  - Project due date is within retention period
- None of the following task activities have occurred:
  - Edits to task fields - including updates or edits to task name, assignee, due date, task dependencies, description, attachments, custom fields, comments, collaborators, likes, etc.,
  - Changes to task associations - including updates or edits to project associations, changes in task section, or new subtasks
  - Other actions - including task duplicated or undeleted
  - Task due date is within retention period
- None of the following message activities have occurred: 
  - Edits to message - updates to message description, collaborators, likes, etc.,
  - Comments to the message

## Data deletion

Inactive data deleted by the retention policy falls into the retention policy once it has reached the specified period of inactivity. Inactive data is deleted Data users have admin access to can be undeleted within 30 days; after that, they are permanently deleted. Super admin can view [audit logs](https://developers.asana.com/docs/audit-log-events) to see what was undeleted. 

Inactive data that is deleted can be recovered from the “deleted” view trashed and then permanently deleted after 30 days if not recovered. The deletion process will run in weekly batches.

Users who wish to recover data deleted by the policy will be able to do so by visiting the Deleted view in Asana, see details in this [help article](https://help.asana.com/s/article/recover-deleted-tasks-projects-and-more?language=en_US). Users have the option to restore deleted projects, messages, or tasks within 30 days of deletion.

## Admin configuration and notifications

This feature is only available to super admins of eligible organizations under the security settings in the admin console. From the data retention view, admins can set a retention period from 6 months to 10 years. Before enabling the policy we highly encourage admins to inform users via an [admin announcement](https://help.asana.com/s/article/admin-announcements?language=en_US). 

Once the admin saves the policy settings the process will commence in the following days. 

In the month following policy enablement, organization super admins will receive monthly email notifications with a summary of data deleted by the policy in the prior month. 

Super admins can view all data deleted by the policy by accessing the [deleted view](https://help.asana.com/s/article/recover-deleted-tasks-projects-and-more?language=en_US) via the [Work Access Mode](https://help.asana.com/s/article/work-access-mode?language=en_US). 

Data users have admin access to can be undeleted within 30 days; after that, they are permanently deleted. Super admin can view [audit logs](https://developers.asana.com/docs/audit-log-events) to see what was undeleted.

## Data inclusions

See the below diagram for the data types that are included in the policy’s scope. Certain data and functionalities such as teams, goals, and portfolios are currently excluded from the policy. 

[](https://forum.asana.com/c/forum-en/tips/6)
