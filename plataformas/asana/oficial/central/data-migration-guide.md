---
fonte: https://help.asana.com/s/article/data-migration-guide?language=en_US
baixado: 2026-11-10
---

# Data migration guide

When Asana performs a data migration, we copy data from one space to another. The organization or workspace that we copy the data from is referred to as the **source domain**, and the organization or workspace where the data is moved to is referred to as the **destination domain**.

The source domain is usually the space with the smallest number of tasks and projects. Occasionally the migration team might recommend an alternative depending on the tier of paid subscriptions and their current usage.

Once a source organization is migrated to a destination organization, the destination organization will automatically inherit the email domains associated with the source organization.

> It is a requirement that the company confirm that they **own** a domain before adding it to their organization.

## FAQs

### When is it possible to perform a migration?

- A migration is possible to perform once you have decided to fully migrate all data from the space of your choosing (organization or workspace) to another. It’s not possible to only migrate specific teams or projects as all exported data under the space must be included within the migration.

- Also important to note is that at least one of the spaces, either the source or destination, has to be an organization.

- A **Personal Projects** organization cannot be used as a source or destination domain.

> Although it’s possible to migrate a workspace into an organization, it is not possible to migrate an organization to a workspace. Only organizations can facilitate several teams. A workspace, however, can only support one team.

### What happens when a workspace is migrated into an organization?

In this instance, a new team is created in the organization containing all the data from the source workspace. Users of the source workspace who are not already a member of the destination organization will become guests and lose access to paid features.

### What happens when an organization is migrated into a workspace?

Although we've mentioned that it is not possible to migrate an organization into a workspace, it is more accurate to say that we cannot migrate an organization into a workspace without the workspace being converted into an organization.

When an organization is migrated to a workspace, firstly the email domain is carried over. This automatically converts the workspace into an organization, and also copies all of the teams and data into the newly converted organization. Users of the destination workspace who are not already a member of the source organization will become guests.

### What happens when one organization is migrated into another organization?

The email domain(s) associated with the source organization are added to the destination organization. All the members of the source organization are added as full members of the destination organization. All teams and their data will be copied into the destination organization.

## What are the caveats of a migration?

#### Process and duration

- During the migration process, the source domains will be taken offline and made inaccessible until the migration has been completed. Although the destination will remain available, **we do not recommend** making changes to the newly imported teams until the migration is complete.

- The duration of the migration may vary depending on the volume of data in the source domain. The migration team will be able to provide you with an estimation of the migration process.

> In rare cases, migrations get stuck or halted. In this instance, our engineering team located in San Francisco (Pacific Standard Time) will work on repairing the issue in question and resume the migration as soon as they are online.

#### Data Structure

- All objects within Asana have a unique ID. These IDs will change for all objects being copied over from the source domain.

- Deleted objects such as teams, projects and tasks will not be copied. Custom fields will be imported. However, if a custom field in the source domain has the **same name** as a custom field in the destination domain, we will attach a code to the field name. This is because two custom fields in the same organization cannot have the same name.

> This may break integrations and will change URLs for Asana forms as well as externally shared links including shareable invite links.

#### Privacy and security

- Our engineers may need to look at your data during the import, but our general privacy and security policies will still apply. We assure you that data will be kept on our secure servers and not downloaded to a laptop or any other external device.

- Teams will retain their source domains privacy setting, with both projects and tasks from the source domain remaining private.

- When your organization undergoes data migration, any existing API credentials will need to be updated to the new ones from the destination domain. This includes Personal Access Tokens (PATs), Service Accounts, OAuth tokens, and any other API authentication methods.

#### Paid plans

Please note that paid plans associated with the source domain are not migrated to the destination domain. As admin and super admin roles are part of a paid feature, these roles are also not carried over during the migration process.

If admin roles need to be retained post-migration, written confirmation from both stakeholders of the source and destination domains will be required to approve this request.

Our Migrations team will be happy to work with you to identify the best solution for any paid plans and related role configurations.

## Recommendations before beginning a migration

When migrating from an organization to another organization, make sure that users have **merged their accounts** to avoid duplicated memberships. If [Google SSO](https://asana.com/guide/help/api/google "Google SSO") or [SSO SAML](https://help.asana.com/s/article/global-authentication-settings?language=en_US "SSO SAML") are active within your organization, ensure that you have made the necessary changes on your end to prevent being locked out post-migration.

It is important to **notify your team** that the source domain will not be accessible and that recently copied data should not be altered before everyone has received confirmation that the migration has been successfully completed.

## How to request a migration

To schedule your migration, please fill out this [request form](https://form.jotform.com/asanawebdev/asana-migration-request "request form") and the migration team will be in touch within the next 24 business hours.

[](https://forum.asana.com/c/forum-en/tips/6)
