---
fonte: https://help.asana.com/s/article/rules-integrations-for-cloud-storage-and-file-sharing?language=en_US
baixado: 2026-11-10
---

# Automations integrations for cloud storage and file sharing

Automations and integrations work together to handle routine tasks and keep work moving across your team’s favorite tools. This article shows how to use automations with Dropbox, Box, and Microsoft OneDrive so attachments reach your cloud storage without manual uploads. For help building an automation, see [Automations](https://help.asana.com/s/article/rules).

#### Related articles

- [Automations integrations and widgets](https://help.asana.com/s/article/rules-integrations-and-widgets?language=en_US)
- [Automations integrations for productivity and communication](https://help.asana.com/s/article/rules-integrations-for-productivity-and-communication?language=en_US)
- [HubSpot automations integration](https://help.asana.com/s/article/rules-integrations-for-sales-and-services?language=en_US)
- [PagerDuty automations integration](https://help.asana.com/s/article/rules-integrations-for-operations-and-support?language=en_US)

## Dropbox

With automations, teams can automatically upload task attachments to a specific Dropbox folder to streamline sharing, storage, and collaboration. For example, teams can use Asana to work on asset approvals and, following approval, automatically upload the task attachment to a specific Dropbox folder so final assets end up in the right place.

Automations that trigger on a task with more than 10 attachments upload only the 10 most recent. If a file has the same name as one already in the Dropbox folder, it is renamed automatically and still uploads. For best results, avoid special or non-English characters in the folder name.

#### To add a Dropbox action to an automation:

1.  In your project, click **Customize**, select **Automations**, then click **+ Add** and select **Start from scratch**.
2.  Under **What starts this workflow?**, select **Asana**, then choose a trigger. This article uses **Task is moved to a section** as an example.
3.  Click **Add step**, then select **Apps**.
4.  Select **Dropbox** from the list, or search for it by name.
5.  Click **Connect to Dropbox**, then click **Allow** to give Asana access to your files and folders.
6.  When you see the **Authorization succeeded** message, close the window and return to Asana.
7.  Paste the URL of your Dropbox folder into the **URL of folder** field.
8.  Click **Publish**.

## Box

Use automations to upload content to Box automatically when certain actions take place in Asana. Teams can save time by setting triggers that transfer attachments from Asana tasks to Box. For example, design teams working on assets can create an automation that uploads the attachment to Box once the task moves to the “Final approved assets” section.

Automations that trigger on a task with more than 10 attachments upload only the 10 most recent. If a file has the same name as one already in the Box folder, the automation returns an error. To fix this, rename the existing file, edit and save the automation, and trigger the upload again.

#### **To add a Box action to an automation:**

1.  In your project, click **Customize**, select **Automations**, then click **+ Add** and select **Start from scratch**.
2.  Under **What starts this workflow?**, select **Asana**, then choose a trigger. This article uses **Task is moved to a section** as an example.
3.  Click **Add step**, then select **Apps**.
4.  Select **Box** from the list, or search for it by name.
5.  Click **Connect to Box** and follow the prompts to give Asana access to your Box account.
6.  Paste the URL of your Box folder into the **URL of folder** field.
7.  Click **Publish**.

## Microsoft OneDrive

With automations, teams can automatically upload task attachments to a specified OneDrive or SharePoint folder to streamline sharing, storage, and collaboration, while reducing manual work. For example, teams can use Asana to work on asset approvals and, following approval, automatically upload the task attachment to a specified OneDrive folder so final assets end up in the right place.

Automations that trigger on a task with more than 10 attachments upload only the 10 most recent. If a file has the same name as one already in the folder, it replaces the existing file. If you want to keep both, give your files different names.

#### **To add a OneDrive action to an automation:**

1.  In your project, click **Customize**, select **Automations**, then click **+ Add** and select **Start from scratch**.
2.  Under **What starts this workflow?**, select **Asana**, then choose a trigger. This article uses **Task is moved to a section** as an example.
3.  Click **Add step**, then select **Apps**.
4.  Select **OneDrive** from the list, or search for it by name.
5.  Click **Connect to OneDrive**, then sign in with your Microsoft account and approve access.
6.  Copy the URL of your OneDrive or SharePoint folder from your browser and paste it into the **OneDrive or SharePoint folder URL** field.
7.  Click **Publish**.

> Please note that an admin needs to grant consent through the API permissions page of the application registration in the Microsoft Entra admin center.

[](https://forum.asana.com/c/forum-en/tips/6)

##
