---
fonte: https://www.notion.com/help/enterprise-connection-settings
baixado: 2026-11-10
---

# Enterprise connection settings

In this help doc

## Enterprise connection settings empower workspace owners with granular control. Manage member access, approve connections, and streamline your Notion workspace's integration ecosystem — all from one centralized dashboard.

------------------------------------------------------------------------

**Note:** This feature is only available to users on the Enterprise Plan. Domain verification is not required to enable this feature.

Workspace owners on the Enterprise Plan have access to additional settings for managing connections within the workspace.

## [Restrict members from installing connections](https://www.notion.com/help/enterprise-connection-settings#restrict-members-from-installing-connections)

1.  If you’re a workspace owner, go to `Settings` → `Connections.`

2.  Select the `Manage `tab.

3.  Click the dropdown next to **Limit which connections members can install** to access options:

- `No restrictions`: All workspace members can install any connection in the workspace.

- `Approved & recommended`: Workspace members can install approved connections and connections recommended by Notion.

- `Approved only`: Workspace members can only install connections pre-approved by a workspace owner. If a workspace owner installs an integration that isn't already on the approved list, it'll automatically be added to the approved list afterwards.

These settings are separate from any limit the developer set on their own connection. A developer can build a connection that only certain workspaces are allowed to install. For someone in your workspace to install a connection, both have to allow it. Your workspace has to be on the developer's list, and your approval settings have to allow the connection.

### [Auto-approve connections built by Notion](https://www.notion.com/help/enterprise-connection-settings#auto-approve-connections-built-by-notion)

- If `From approved list` is selected, workspace owners will see an additional option to auto-approve connections that are built by Notion. [See the full list of these connections here →](https://www.notion.so/integrations/all?collection=made-by-notion)

### [Approved connections list](https://www.notion.com/help/enterprise-connection-settings#approved-connections-list)

1.  Click the `+ Add approved connection` button to approve additional connections for members in your workspace.

    **Note:** Before you can approve a connection for the rest of your workspace, you or another admin will have to install it first! Only connections already installed in the workspace will show up in the `+ Approved connection` dropdown.

    Instructions for installing connections are specified [below](https://www.notion.com/help/add-and-manage-connections-with-the-api#install-public-integrations-from-developers).

2.  Under the `Approved connections` heading, workspace owners will see a full list of connections that have been approved and installed in the workspace.

3.  To the right of each connection's name, the name(s) of the users who have installed the connection in the workspace are listed.

4.  Click the `•••` menu to:

    - Filter by user.

    - Revoke specific users' access to a connection.

    - Disconnect all users.

    - Remove the connection from the approved list.

### [View members with connections](https://www.notion.com/help/enterprise-connection-settings#view-members-with-connections)

In the `Manage` tab, select any connection to see which workspace members have it installed. You can disconnect individual members or all members at once.

## [Disable webhook actions in a workspace](https://www.notion.com/help/enterprise-connection-settings#disable-webhook-actions-in-a-workspace)

Workspace owners on an Enterprise Plan can also disable the `Send webhook` action for your entire workspace. Learn more about webhook actions [here →](https://notion.so/help/webhook-actions)

To turn off webhook actions for your workspace:

1.  Go to `Settings` in your sidebar.

2.  Open the `Connections` tab.

3.  Toggle off `Allow webhooks in automations`.

Once you’ve turned this feature off, members of your workspace won’t be able to select `Send webhook` as an action for any automations they set up.

## Contents

- [Restrict members from installing connections](#restrict-members-from-installing-connections)
- [Auto-approve connections built by Notion](#auto-approve-connections-built-by-notion)
- [Approved connections list](#approved-connections-list)
- [View members with connections](#view-members-with-connections)
- [Disable webhook actions in a workspace](#disable-webhook-actions-in-a-workspace)
