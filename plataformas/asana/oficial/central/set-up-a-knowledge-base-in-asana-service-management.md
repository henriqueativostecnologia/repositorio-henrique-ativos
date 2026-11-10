---
fonte: https://help.asana.com/s/article/set-up-a-knowledge-base-in-asana-service-management?language=en_US
baixado: 2026-11-10
---

# Set up a knowledge base in Asana Service Management

A knowledge base helps your team keep useful information in one place that can be used to resolve requests. 

By default, admins can create knowledge bases. You can also give knowledge base creation access to members through [role-based access controls](https://help.asana.com/s/article/control-queue-and-knowledge-base-creation-with-rbac).

Whether a knowledge base is public or private determines who can see it and whether [Service AI](https://help.asana.com/s/article/service-AI-and-your-knowledge-base?language=en_US) can use it. Public knowledge bases are visible to everyone in your organization, and Service AI draws on their published articles to resolve tickets. Private knowledge bases are visible only to the people you add, and Service AI does not use their content. 

## Create a knowledge base

To create a knowledge base:

1.  Click **Knowledge base** on the sidebar
2.  Click **+ Add folder**

Give it a clear name, then click **Share** and choose who should have **Admin** or **Editor** access. 

## Add articles to your knowledge base

After your knowledge base is set up, open **Knowledge base** and select **New article**. From here, you can select **Create new article**, **Import a CSV**, or **Upload a file**.

If you already have content somewhere else, you can upload files or import existing knowledge. This can make it easier to move established documentation into Asana Service Management without recreating everything manually.

If your content already lives in Google Drive, you can [sync a Google Drive folder](https://help.asana.com/s/article/import-knowledge-from-google-drive-into-asana-service-management) instead of uploading files one at a time. Asana keeps a read-only copy of your files and updates it when they change in Google Drive.

If you choose the **Create new article** option, you can write content directly in the article and format it with headings, lists, and attachments.

## Share a knowledge base

You can share a knowledge base using the standard share modal, or change who can access it in the share modal’s privacy settings.

Organization admins or users with the appropriate RBAC permissions create knowledge bases, while knowledge base admins own and manage individual knowledge bases. People who are added through sharing receive editor access by default.

> Permissions to edit or administer a knowledge base must be explicitly granted.

## Restrict access with a private knowledge base

A private knowledge base is visible only to the people and teams you add to it. Service AI does not use the contents of a private knowledge base to resolve tickets or suggest edits, which makes this option useful for content such as HR policies or private team procedures.

### Create a private knowledge base

Every knowledge base you create is private by default. Follow the steps in [**Create a knowledge base**](https://help.asana.com/s/article/set-up-a-knowledge-base-in-asana-service-management?language=en_US#create-a-knowledge-base) and add the people or teams who should have access.

A private knowledge base shows **Members** in the **Visibility** column and **Inactive** in the **Service AI** column. 

### Change a public knowledge base to private

You can restrict a knowledge base that is visible to your organization at any time. Only invited members can then find and open it, and everyone else loses access, including Service AI.

1.  Click **Knowledge base** on the sidebar, then open the knowledge base you want to restrict.
2.  Click **Share**.
3.  In the **Privacy** section, click the drop-down and select **Private to members**.
4.  In the confirmation window, click **Make private**.

### Change a private knowledge base to public

If a private knowledge base no longer needs to be restricted, you can give your organization access to it. Everyone in your organization can then find it, and Service AI can use its published articles to resolve tickets.

1.  Click **Knowledge base** on the sidebar, then open the private knowledge base.
2.  Click **Share**.
3.  In the **Privacy** section, click the drop-down and select your organization’s name.
4.  In the confirmation window, click **Give access**.

## Delete an article

If an article is outdated or no longer accurate, you can edit it or delete it. Deleted articles are no longer used for AI resolution and cannot be recovered.

At this time, articles cannot be unpublished or archived. If you want an article to stop being used, delete it or update the content so it stays accurate.

## Understand permissions

What people can do in a knowledge base depends on whether it is private and on their permission level. Only people who have been added to a private knowledge base can see its folders and articles.

There are three permission levels: **Viewer**, **Editor**, and **Admin**. Viewers can search and read published articles but cannot create or edit content. Editors can open the share modal, edit articles, and approve and publish them. In knowledge bases that are visible to your organization, publishing determines what content Service AI draws on when resolving tickets.

Knowledge base admins, who are separate from your organization’s admins, have all editor capabilities and can also grant admin access, rename or delete a knowledge base, and manage membership more broadly. The table below shows what each level can do.

|                                                       |            |                                |                                      |
|-------------------------------------------------------|------------|--------------------------------|--------------------------------------|
| **Action**                                            | **Viewer** | **Editor **                    | **Admin **                           |
| View knowledge base folder/articles                   | Yes        | Yes                            | Yes                                  |
| Create new knowledge bases                            | No         | No                             | No                                   |
| Open knowledge base share modal                       | No         | Yes                            | Yes                                  |
| Default share invite level                            | N/A        | Editor                         | Editor                               |
| Grant Editor membership                               | No         | Yes                            | Yes                                  |
| Grant Admin membership                                | No         | No                             | Yes                                  |
| Grant Viewer membership                               | No         | Yes                            | Yes                                  |
| Edit/delete knowledge base articles created by others | No         | Yes                            | Yes                                  |
| Rename/delete knowledge base                          | No         | No                             | Yes                                  |
| Manage knowledge base members                         | No         | Can grant Editor/Viewer access | Can grant Editor/Admin/Viewer access |

## What happens when an article is published

Once an article is published in a knowledge base that is visible to your organization, it is available to Service AI straight away and can be used to resolve incoming tickets automatically. Articles in a private knowledge base are never used by Service AI, even after they are published.

Unpublished drafts are not available to Service AI in either type of knowledge base and will not be used.
