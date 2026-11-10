---
fonte: https://help.asana.com/s/article/asana-and-salesforce-process-automation?language=en_US
baixado: 2026-11-10
---

# Asana in Salesforce AppExchange (being deprecated)

> **On February 27, 2026, the** [Asana app in Salesforce’s AppExchange marketplace](https://appexchange.salesforce.com/appxListingDetail?listingId=a0N3A00000FR4NTUA1) **will be deprecated and removed from the marketplace. Customers should use the** [native "Salesforce in Asana” app going forward](https://help.asana.com/s/article/salesforce-in-asana-rules)**.** [Learn more about the deprecation](https://help.asana.com/s/article/salesforce-integration-deprecation-faq)**.**

Available on Asana [*Enterprise*](https://asana.com/enterprise) and [*Enterprise+*](https://asana.com/enterprise) tiers, as well as [*legacy tiers*](https://asana.com/pricing-legacy) Business and Legacy Enterprise. Visit our [*pricing page*](https://asana.com/pricing) for more information.

Asana for Salesforce helps your Sales teams collaborate with cross-functional team members throughout the entire sales cycle. This article covers how to set up automation between Asana and Salesforce. 

Video: https://fast.wistia.net/embed/iframe/klznd11r47?seo=true&videoFoam=false

## Setting up an automatic Asana project creation

#### To set up an automatic project creation:

1.  Head to the App picker on the top-left corner and type **Asana**
2.  Click **Set Up**
3.  Edit the automatic project creation by selecting a **Stage**, an **Asana team**, and an **Asana Custom Template**.
4.  Click **Save**

> Learn how to create [project templates](https://help.asana.com/s/article/project-templates?language=en_US).

For example, if you’ve selected the **Proposal/Price Quote** stage and **Legal** team. When an opportunity moves to the Proposal/Price Quote stage, a project will be created within the Legal team using the custom template you chose.

## Build automations using the Flow Builder

Set up automated workflows between Asana and Salesforce with the Flow Builder and automate any Asana work requests. With the Flow Builder, you can automatically trigger the creation of tasks and projects in Asana.

#### To set up a new process:

1.  Navigate to the Flow Builder in Salesforce
2.  Click **New**
3.  Fill out the **Process Name** and **API Name** fields
4.  For the process to run when an object changes, select **A record changes** for the **The process starts when** field
5.  Click **Save**

#### From here:

1.  Select the object that starts the process—for example, Opportunities, Campaigns, or a custom object, to mention a few.
2.  Add the criteria to determine if the process goes forward.
3.  Select the action that takes place. This would be creating a project or a task in Asana.

For example, in the image below, the object is an Opportunity. The criteria for executing actions is when conditions are met, and there are three conditions. When an opportunity is in the **Qualification**, **Needs Analysis**, or **Value Proposition** stage, an action will be triggered. This action can either **Create an Asana** task or **Create an Asana project**.

If you select Create Asana Projects as an action, you need to paste the project’s ID and the team’s ID in the **Value** field.

> Like what you see? Get started with a free Asana trial today. [Try for free](https://asana.com/create-account "Try for free")

## Process automation examples

### Automating the hand-off between the Sales and Post-Sales/Implementation teams

Once a deal is closed, you can streamline the hand-off between Sales and Post-Sales teams, reducing manual work and giving Sales teams visibility into the post-sales implementation progress contextually within Salesforce.

### Enable collaboration between Sales and Support teams

Sales teams can request help from Support teams without leaving Salesforce.

Sales teams can track the progress of Asana tasks within the proper context in Salesforce (e.g., a specific Salesforce opportunity).

 

[](https://forum.asana.com/c/forum-en/tips/6)
