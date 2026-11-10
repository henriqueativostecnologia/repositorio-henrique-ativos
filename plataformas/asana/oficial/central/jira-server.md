---
fonte: https://help.asana.com/s/article/jira-server?language=en_US
baixado: 2026-11-10
---

# Jira Data Center

**Please note that the Asana for Jira Data Center integration is scheduled to be deprecated on December 31, 2026**

**Available on Asana [*Starter*](https://asana.com/plan/starter), [*Advanced*](https://asana.com/plan/advanced), [*Enterprise*](https://asana.com/enterprise), and [*Enterprise+*](https://asana.com/enterprise) tiers, as well as [*legacy tiers*](https://asana.com/pricing-legacy) Premium, Business, and Legacy Enterprise.**

**Visit our [*pricing page*](https://asana.com/pricing) for more information.**

Asana for Jira Data Center is an integration that allows collaboration and visibility between teams working in Asana and Jira.

This integration brings the value of the Jira Cloud integration to users who use Jira Jira Data Center.

It allows business and product teams (*that spend the majority of their time planning and actioning on work in Asana*) to collaborate and track work seamlessly with engineering teams (*who plan and execute work in Jira*). Its purpose is to optimise scheduling by tracking sprints *and* ultimately providing Asana users visibility into the development stage in Jira.

Asana for Jira Data Center bridges the gap between the planning stages in Asana and the development phases in Jira, from execution to delivery.

It creates and monitors the status of Jira issues inside Asana tasks.

#### Related articles

- [Jira Data Center FAQ](https://help.asana.com/s/article/jira-server-faq?language=en_US)
- [Asana for Jira Cloud](https://help.asana.com/s/article/asana-for-jira-cloud?language=en_US)
- [Asana for Jira Cloud FAQ ](https://help.asana.com/s/article/asana-for-jira-cloud-faq?language=en_US)

## Requirements for installation

### Asana requirements:

The Jira Admin must have the following available for the first steps of installation:

- An Asana account
- A paid plan

> Looking for a better way to manage your work? Get started with a free Asana trial. [Try for free](https://asana.com/create-account "Try for free").

### Jira requirements:

Jira Data Center instances are supported, and configured according to requirements linked below. For specific version support, please reference the [Jira Marketplace](https://marketplace.atlassian.com/apps/1223378/asana-for-jira-server?hosting=server&tab=overview "Jira Marketplace") listing.

> If you use Jira Cloud, use the [Asana for Jira Cloud integration](https://asana.com/apps/jiracloud "Asana for Jira Cloud integration")

## How to install

The Jira Admin needs to create the application link by installing the plug-in from the Jira Data Center Marketplace. The Jira Admin will need to complete the first steps, then the end users in Asana will be able to add the integration to any projects they have access to.

#### Jira Admin Install:

- Navigate to this [GitHub repository](https://github.com/Asana/jira-server-plugin "GitHub repository") for details on supported configurations of Jira Data Center to allow external connections
- After configuring your Data Center instance accordingly, navigate to the [Jira Sever Marketplace listing for 'Asana for Jira Data Center'](https://marketplace.atlassian.com/apps/1223378/asana-for-jira-server?hosting=server&tab=overview "Jira Sever Marketplace listing for 'Asana for Jira Server'") and install it.

Next, the Jira Admin needs to authenticate the application by clicking **Connect to Asana**

- You will be prompted to Auth with Asana
- Once granted please choose the appropriate Asana domain to connect to the new integration
- Once you see a confirmation in Jira, the steps needed from the Data Center are complete, and the rest can be completed by users in Asana

#### Asana users:

1.  In Asana, go to the project you want to add the integration to
2.  On the top right of your screen click **Customize**, scroll down in the menu and click **Add app**
     

> During authentication if you get the message "Your Asana has not been added to Jira Data Center" go back to "Jira Admin Install" step and make sure the Asana Org is authenticated, the relevant workspace has been selected and is showing up in the Jira Data Center Administration.

Once complete, the app will be added to the project, and users should see a **Jira Data Center** field on tasks where they can add existing or create new Jira issues from within Asana.

> If this is the first time you have tried to add the App to a project, you will go through a series of Jira and Asana authentication flows. After completion you will be able to link issues to tasks in the relevant project.

## OAuth 2.0 for Jira Data Center

OAuth 2.0 is supported for Jira Data Center from version 8.22 and above.

There are [two ways to install an integration](https://confluence.atlassian.com/adminjiraserver/link-to-other-applications-938846918.html "two ways to install an integration") for Jira Data Center. With the **OAuth 1.0** installation process, customers are required to install the Asana for Jira Data Center add-on from the Atlassian Marketplace.

Using **OAuth 2.0** does not require this step to enable the installation process, meaning that a Jira Admin can complete the entire installation process directly from their Jira instance.

### Step-by-step installation instructions

This process can only be carried out by Jira Administrators.

1.  Generate the application link credentials:

- Open the **Applications** dropdown menu by clicking on the gear icon
- Open **Application links** on the dropdown menu
- Create a new incoming application link with the following parameters:
  - Application type: External application
  - Direction: Incoming
  - Redirect URL: [https://jira-api.integrations.asana.plus/setup/callback/jira](https://jira-api.integrations.asana.plus/setup/callback/jira "https://jira-api.integrations.asana.plus/setup/callback/jira")
  - Permission: Write

1.  After you hit **Save**, the resulting page provides you with the credentials: **Client ID** and **Client secret**. Keep this page open as you will need this information in step 5.
2.  Open the setup page by entering [https://jira-api.integrations.asana.plus/setup](https://jira-api.integrations.asana.plus/setup "https://jira-api.integrations.asana.plus/setup") in a separate tab on your browser.
3.  Log in with your Asana account and confirm your approval to grant permissions by clicking **Allow**. After successful login, select an Asana workspace with which you want to integrate your Jira instance.
4.  You are asked to enter the following information:

- Jira domain: The Jira domain you’d like to connect to. Your Jira instance needs to be accessible from the public internet; if your Jira instance is only accessible via your corporate network or a VPN, this will not work.
- Client ID: From step 2.
- Client secret: From step 2
- Click **Save**

2.  You are then asked to grant permission for Asana to access your Jira domain. Click **Allow** if you’d like to proceed.

## Features

The integration can now be used to link an existing Asana task to an existing Jira issue or create a new issue.

### Link Asana task to existing Jira issue

From the dropdown menu at the Jira Data Center field you can add an existing issue.

Then enter the URL of the Jira issue, or simply type in the name of the issue in the text field.

From here you can open a Jira issue, give feedback and remove an issue from a task.

###  Create Jira issue from Asana task

Select **Create new issue** from the Jira Data Center field within the task in Asana.

A new dialog pop up will next appear for you to fill in. Please try and fill in all fields (**specifically project and issue type**). You can also attach files from the Asana task.

Click **Create issue**.

Asana will load the relevant details from the completed fields to create the issue.

> After you’ve created or linked an issue, you’ll see the updated details about the issue within the task in Asana. You can only add one Jira issue per each Asana task.

Once the Jira Issue is created a real-time Jira widget is available providing you with the Status, Priority, and Assignee of the Jira Issue. Click into it to see more.

Any changes made to the issue in Jira will be reflected in Asana at the next page load.

## Key functionality

- **Bridge the gap between the planning stage and the hand-off**: Project Managers can seamlessly create a Jira issue from Asana when tasks are engineering ready. The planning has already happened in Asana and the product manager is ready to transfer over to the engineering department with ease to do their sprint planning in Jira. This integration saves time and avoids data inconsistencies.

- To save steps and optimize your workflow, you can automate the creation of Jira issues via our Rules feature. [Learn how](https://asana.com/guide/help/premium/rules#gl-integrations "Learn how").

#### From the **Add rule** pop up:

1.  Under Jira Data Center click **Create new issue**
2.  Fill out *all the fields* in the **Create new issue** box
3.  Click on **Create rule** to automate the creation of Jira Data Center issues

- **Transparency in development work in Jira**: Asana users have visibility to work happening in Jira so they can update stakeholders and important clients on key release dates, bug fixes, etc. Similarly, the product manager wants the flexibility to be able to track, plan, and execute Jira work within Asana. It's a win-win.

> For a list of common questions on the Asana for Jira Data Center integration, see our [FAQ article](https://help.asana.com/s/article/jira-server-faq?language=en_US).

 

[ ](https://forum.asana.com/c/forum-en/tips/6)
