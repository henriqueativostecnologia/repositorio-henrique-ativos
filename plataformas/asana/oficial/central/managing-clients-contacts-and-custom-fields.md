---
fonte: https://help.asana.com/s/article/managing-clients-contacts-and-custom-fields?language=en_US
baixado: 2026-11-10
---

# Managing your client directories and custom fields

**To purchase Client Management, your organization must have an active Starter or Advanced base subscription. Client Management is not included in these plans by default.**

Asana Client Management gives your team three shared directories for organizing client work: **Clients**, **Contacts**, and **Projects**. Each directory is a central list where you can track records, add custom fields, and control who has access. This article explains how to manage each one.

## The client directory

The **Clients** directory is your central list of every client account you manage. Access it by clicking **Clients** in the sidebar.

At the top of the directory, you can switch between views:

- **All Clients**: Every client in your workspace.
- **My Clients**: Only the clients you own.
- **Custom**: Click the **+** icon to create a new view.

To filter, sort, or group records within any view, use the **Filter**, **Sort**, and **Group** options at the top of the directory.

> Custom views in the **Clients**, **Contacts**, and **Projects** directories are shared with everyone who has access to that directory. Members with **Editor** or **Admin** access can create, rename, reorder, or delete views. Members with **Viewer** access can use existing views but cannot create or modify them.

Select any client and click **View client** to open its record, where you will find its projects, contacts, and portal.

## Directory access

When Asana Client Management is enabled for your organization, existing domain admins are automatically granted admin access to all three directories: **Clients**, **Contacts**, and **Projects**. A directory admin can then grant any domain member one of three access levels, set independently for each directory.

| **Level**  | **Permissions**                                                                                                               |
|------------|-------------------------------------------------------------------------------------------------------------------------------|
| **Admin**  | All Editor permissions, plus add and manage custom fields on the directory, and grant or change other members' access levels. |
| **Editor** | Create, edit, and delete records; update standard and custom field values.                                                    |
| **Viewer** | View records and fields; cannot create, edit, delete, or manage access.                                                       |

### To grant directory access:

1.  Click into the directory and click **Share** on the top right.
2.  Find the person whose access you wish to update.
3.  Click the drop-down next to their name to select a role: **Admin**, **Editor**, or **Viewer**.

Directory access controls what someone can do in the directory itself. It does not automatically grant or remove their access to individual client, contact, or project records. 

Record-level access is managed separately on each record. If you need to fully remove someone's access to a specific client, contact, or project, remove them from that record directly.

## How to add a client

### To add a client:

1.  Open **Clients** and click **+ Create client**.
2.  Enter a name in the **Name your client** field.
3.  Optionally, add a description, website, address, client health status, start date, and renewal date.
4.  Click **Create**.

## How to add a contact

Contacts are the people at a client that you work with. They are stored on each client's **Contacts** tab, keeping the businesses you work with and the people inside them connected in one place.

### To add a contact from a client record:

1.  Click on a client and select **View client**.
2.  Open the **Contacts** tab.
3.  Click **Add contact**.
4.  Enter the contact's name, email, and consider populating any other fields you use.

You can also add contacts directly from the **Contacts** directory and associate them with the relevant client record.

> If a client has more than one contact, you can designate a primary contact using the **Point of contact** field.

## How to add custom fields

Custom fields let you capture information specific to your team, such as account tier, region, or contract value. Fields added at the directory level appear as columns across the entire list and on each individual record.

### To add a custom field to a directory:

1.  Open **Clients**, **Contacts**, or **Projects** in the sidebar.
2.  Click the **+** icon next to the existing fields.
3.  Create a new field or select an existing one from your team's field library.

Adding a field at the directory level makes it a column across the entire list and adds it to each individual record: the **Profile** tab for clients, the **Contacts** tab for contacts, and the **Projects** tab for projects.

> Only directory admins can add or manage custom fields. Editors can populate values on existing fields but cannot create new ones.

### How fields work across directories

Where you add a field determines how broadly it applies:

- **Clients**: Fields can only be added from the Clients directory. There is no option to create a field from inside an individual client record. Every field you add is automatically global across all clients.
- **Contacts**: Fields can only be added from the Contacts directory. Whether you access it from the sidebar or from inside a client's **Contacts** tab, the field applies to all contacts across all clients.
- **Projects**: Fields can be added from the Projects directory or from within an individual client's **Projects** tab. A field added from the Projects directory appears across all projects for all clients. A field added from inside a single client's **Projects** tab applies only to that client's projects. To add a local project field, you need Admin access on that specific client, not directory Admin access.**
  **
