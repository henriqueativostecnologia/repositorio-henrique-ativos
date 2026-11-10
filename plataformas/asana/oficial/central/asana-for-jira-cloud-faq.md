---
fonte: https://help.asana.com/s/article/asana-for-jira-cloud-faq?language=en_US
baixado: 2026-11-10
---

# Asana for Jira Cloud FAQ

**The Asana for Jira Cloud integration is available on Asana [*Starter*](https://asana.com/plan/starter), [*Advanced*](https://asana.com/plan/advanced), [*Enterprise*](https://asana.com/enterprise), and [*Enterprise+*](https://asana.com/enterprise) tiers, as well as [*legacy tiers*](https://asana.com/pricing-legacy) Premium, Business, and Legacy Enterprise.**

**Jira Cloud two-way sync functionality is available on Asana [*Advanced*](https://asana.com/plan/advanced), [*Enterprise*](https://asana.com/enterprise), and [*Enterprise+*](https://asana.com/enterprise) tiers, as well as [*legacy tiers*](https://asana.com/pricing-legacy) Business and Legacy Enterprise.**

**Visit our [*pricing page*](https://asana.com/pricing) for more information.
**

Install the [Asana for Jira Cloud integration](https://asana.com/apps/jiracloud) to create transparency between business and technical teams and build interactive, connected workflows.

The Asana for Jira Cloud integration allows business and product teams that plan work in Asana to collaborate and work seamlessly with engineering and technical teams who execute work in Jira.

## Data sync

### Can I manually trigger data sync for a task?

Yes. You do this by setting up the Data sync setting, and then you can manually add a Jira issue to a task to kick off data sync. Please ensure that the Jira project and the Issue type specified in the Data sync setting are the same as the Jira project and the Issue type of the Jira issue you are adding to the Asana task.

### If the integration is set up so that a Jira issue is created from an Asana task, can the Jira issue also be deleted from the Asana side?

Jira issues can only be removed from the Jira project by a user who has Delete access within Jira.

## Jira instances

### I want to use another Jira instance for the integration, but I can’t seem to be able to, even after deauthorizing the Jira Cloud app from Asana.

In this case, you must first go to your [Atlassian profile](https://id.atlassian.com/manage-profile/apps "Atlassian profile") and remove the Asana for Jira Cloud connection. Then go back to Asana and try authenticating again.

### Can I authenticate with multiple Jira instances?

You will need to navigate to [https://id.atlassian.com/manage-profile/apps](https://id.atlassian.com/manage-profile/apps "https://id.atlassian.com/manage-profile/apps"), remove the Asana app, and re-authenticate to the second instance from Asana.

### What if I want to connect multiple Jira domains to the same Asana domain?

You can do this by having one person authenticate with one Jira domain for one Asana project and another person authenticate with another domain for another Asana project.

## Custom fields

### My app's custom fields are missing after submitting the data sync form.

You’ve likely exceeded your custom field setting limit of 60 for the given project. To solve this issue, you need to remove custom fields from your project so that all custom fields from the sync are added.

### After submitting the data sync form, my app's custom fields are missing, but I haven’t exceeded my custom field setting limit.

You will need to install the Jira Cloud app in your domain first and then submit the data sync configuration a second time, which will fix the issue by creating the app's custom fields.

## Access and permissions

### I need clarity on the licensing necessary for this feature. Does each Jira account need an equivalent Asana license?

Only the users who want to set up the Jira Cloud integration and the data sync functionality in Asana need to have a Jira account. These users need at least **Edit permission** in the relevant Jira and Asana projects to set up data sync.

Once the Jira Cloud integration and the data sync functionality have been set up, anyone with read access to the project can see the latest data synced from Jira, and anyone with edit access can update the connected Asana tasks, which can result in changes in Jira, depending on the data sync configuration.

### What does the owner of the Jira board/project see once the integration is set up from Asana?

Whoever owns the correlating Jira project can access the integration management page in Jira and see that that specific Jira project has been connected to Asana.

### Will any other users in Jira see any changes or notifications once the integration is set up, or just the owner of the relevant project?

Only other collaborators on the relevant Jira project will receive a notification when a new Jira issue is created from a connected Asana task. No users besides the owner will see any changes in Jira relating to the integration setup.

 

[](https://forum.asana.com/c/forum-en/tips/6)
