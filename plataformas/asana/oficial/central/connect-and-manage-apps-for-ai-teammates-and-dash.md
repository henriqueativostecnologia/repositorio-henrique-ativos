---
fonte: https://help.asana.com/s/article/connect-and-manage-apps-for-ai-teammates-and-dash?language=en_US
baixado: 2026-11-10
---

# Connect and manage apps for AI Teammates and Dash

AI Teammates and [Asana Dash](https://help.asana.com/s/article/chat-with-dash?language=en_US) can connect to the tools you already use, such as Google Drive, Gmail, or Slack. Once an app is connected, your AI Teammates can pull in the context they need and take action in that tool without you leaving Asana.

Two steps must be taken before an AI Teammate can use an app:

| **Step**                                   | **Who does it**                                                                   |
|--------------------------------------------|-----------------------------------------------------------------------------------|
| 1\. Add the app to the AI Teammate         | The Teammate's admin or an editor                                                 |
| 2\. Connect your own account, once per app | Everyone who works with that Teammate, including the admin or editor who added it |

When you add an app, Asana prompts you to connect your account if you have not already.

You can add an app or connect from the AI Teammate's profile page, under **Customize \> Access \> Apps**, or directly from a task when a Teammate needs an app.

> Whenever an AI Teammate or Dash uses a connected app, it acts with the *triggering user's* access. It can only see and do what that user could already see and do in the connected app, and access is never shared between users. For more on the underlying permission model, see [Understanding access control, memories, integrations, and approvals for AI Teammates](https://help.asana.com/s/article/understanding-access-control-for-ai-teammates?language=en_US).

### Related articles

- [Understanding access control, memories, integrations, and approvals for AI Teammates](https://help.asana.com/s/article/understanding-access-control-for-ai-teammates?language=en_US)
- [Create custom MCP apps for AI Teammates](https://help.asana.com/s/article/create-custom-mcp-apps-for-ai-teammates?language=en_US)
- [Chat with Dash](https://help.asana.com/s/article/chat-with-dash?language=en_US)
- [App management and integrations](https://help.asana.com/s/article/app-management-and-integrations?language=en_US)
- [Triggering AI Teammates](https://help.asana.com/s/article/triggering-ai-teammates?language=en_US)

## Add an app to an AI Teammate

Available to an AI Teammate's admin or editors.

1.  Open the AI Teammate profile and select the **Customize** tab.
2.  In the **Access** card, select **Apps**.
3.  Select **+ Add apps**.
4.  Find the app you want and select **+** on its card.
5.  If you have not connected that app yet, follow the prompt to sign in and approve the requested permissions.

To review an app before adding it, select its card to open **App details**, then select **Add to Teammate**.

Adding an app applies to everyone who works with that Teammate. However, each person will connect their own account before a Teammate can use an app on their behalf.

To connect an app that is not listed using MCP, select **+ Custom MCP** in the **Add apps** dialog. See [Create custom MCP apps for AI Teammates](https://help.asana.com/s/article/create-custom-mcp-apps-for-ai-teammates?language=en_US) for setup steps.

## Connect your account

Authorize access to your account before an AI Teammate or Dash can use it on your behalf. 

### From the AI Teammate profile

1.  Open the AI Teammate profile and select **Customize**.
2.  In the **Access** card, select **Apps**.
3.  Find the app and select **Connect**.
4.  Sign in to the app and approve the requested permissions.

### From a task or chat

When an AI Teammate or Dash needs an app you have not yet authorized, it will prompt you to connect. Once connected, the AI Teammate or Dash will continue its work. If you are an admin or editor for a Teammate and the app has not been added yet, you can add and connect it from the same prompt.

Each app only needs to be connected once. Connecting Gmail, for example, makes that connection available to Dash and to every AI Teammate you work with that has Gmail added to it, including Teammates created later..

Apps connect as you, using your own credentials and permissions in that tool. Two people can work with the same Teammate and get different results, because the Teammate is using each person's own connection. Your connection is never shared, and a Teammate cannot use it to act for someone else.

## Manage app access

For each connected app, you control which actions are permitted and whether you want to be asked before an action runs. These preferences are yours alone and apply only to your connection.

To open them, go to **Customize \> Access \> Apps**, select the **...** menu beside the app, and choose **Manage access**. This opens **App details**, which has two tabs:

- **Dash.** How Dash may use your connection.
- **All AI Teammates.** How your AI Teammates may use your connection.

Many people give Dash more latitude, since Dash works only for them, and require more approvals for Teammates that operate in shared team workflows.

### Categories and defaults

Actions are grouped into two categories, each showing a count of how many actions it contains.

| **Category**             | **What it covers**                                             | **Default**    |
|--------------------------|----------------------------------------------------------------|----------------|
| **Read-only actions**    | Searching, reading, and retrieving information from the app    | Always allowed |
| **Write/delete actions** | Creating, modifying, sending, or removing something in the app | Needs approval |

New actions arrive set to these defaults, so a newly added write action will ask for your approval rather than running on its own.

### Action settings

Every action can be set to one of three states:

- **Always allowed.** The action runs without asking you.
- **Needs approval.** Work pauses and you are asked to approve or decline before the action runs. You will see the request where the work is happening, along with what the Teammate is trying to do. If you decline, the Teammate moves on without that action and will usually explain what it could not complete.
- **Not allowed.** The action is not available.

The dropdown beside a category header sets every action in that category at once, which is the fastest way to adjust a connection. When the actions in a category do not all share the same setting, the category dropdown reads **Custom**. Expand the category to see and adjust individual actions.

> Start at the category level, then adjust the handful of individual actions you care about.

## Remove an app or disconnect your account

Removing an app takes it away from one Teammate for everybody. Disconnecting removes your own connection everywhere.

Both are in the **...** menu, which you can open from the app's row on the profile page or from inside **App details**.

| **Option**                 | **Who can use it**               | **What it does**                                                                                                    |
|----------------------------|----------------------------------|---------------------------------------------------------------------------------------------------------------------|
| **Remove from teammate**   | The Teammate's admin or editors  | That Teammate can no longer use the app. Your connection stays, and Dash and your other Teammates are unaffected.   |
| **Disconnect me from app** | Anyone who has connected the app | Removes your connection from Dash and from all of your AI Teammates. They can no longer use the app on your behalf. |

Your action preferences are saved when you disconnect. If you reconnect the app later, your previous settings are restored rather than reset to the defaults.

## Admin controls

By default, all apps are allowed, and admins do not need to do anything for AI Teammates and Dash to use them.

Admins who want more control can use Asana’s [App management](https://help.asana.com/s/article/app-management-and-integrations?language=en_US) to block or only allow approved apps. Visit [App management and integrations](https://help.asana.com/s/article/app-management-and-integrations?language=en_US) for information on how to configure these, review connected apps, and export app activity.
