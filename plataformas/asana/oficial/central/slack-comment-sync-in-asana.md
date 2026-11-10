---
fonte: https://help.asana.com/s/article/slack-comment-sync-in-asana?language=en_US
baixado: 2026-11-10
---

# Slack comment sync in Asana

**This feature is in Early Access and is only available to select customers.**

Slack comment sync keeps a Slack thread and an Asana task connected, so teams can continue the conversation in either tool. Replies in the Slack thread appear in the task’s synced comment thread, and replies in that Asana thread are sent back to Slack. 

## Create a synced task from Slack

There are 4 ways to [create Asana tasks from Slack](https://help.asana.com/s/article/slack-and-asana?language=en_US) – from the **overflow menu**, **slash command**, **emoji react**, or from **at-mentioning @asana)**. Asana tasks created from Slack will have comment syncing enabled between the message thread and the Asana comment thread.

**Overflow menu**

From a supported Slack message, click the **three dot icon** and click **Create a task**. The task creation window opens with comment syncing enabled by default.

Leave **Sync future replies in this thread as task comments** selected to connect replies in the Slack thread with the Asana task. Then click **Create**.

After you select **Create**, Slack posts the Asana task as a Work Object in the thread and confirms that task comments are synced with replies in the thread.

### Slash command

Use  /asana create to create a new Asana task. These new tasks will be synced with the slack message thread.

### Emoji react to create Asana tasks

You can turn Slack messages into Asana tasks by using the :memo: 📝 emoji. To do so, react to any message with the 📝 emoji. The message content and any thread replies are automatically included in your task description, and will be synced.

## Reply to a synced conversation

Reply in the same Slack thread to add the message to the task’s synced Asana comment thread. Slack-originated comments are visually identified in Asana and can include the commenter’s Slack name and avatar with a via Slack label.

In Asana, open the task’s designated synced comment thread. Select **Reply in thread to send messages to Slack** to send your response to Slack, then select **Post to Slack** when prompted. Asana-originated comments appear in the linked Slack thread with the author’s Asana identity.

> To keep a comment in Asana, post a top-level comment or use a different comment thread. Only comments in the designated synced thread are sent to Slack.

## To stop syncing

Navigate to the synced Asana task to stop the comment syncing.

## Requirements

- Users are required to authenticate their Asana accounts via the application.
- Comment syncing is supported in public and private channels, but not in direct messages.
- You must manually add the Asana app to the specific Slack channel.

## Privacy and sync limitations

By enabling comment syncing, discussion details may become visible to more individuals across both the Slack and Asana platforms (this will depend on who can see the created Asana task or slack channel).

Removing messages from either tool is attempted on a best-effort basis. If the connection is severed through uninstallation,token revocation, or synchronization fails to complete due to other technical errors, data synchronization may stop and existing records may remain.

Identity considerations: if a user modifies their Slack profile details, their Asana identity (including avatar and name) will reflect those changes alongside the **via Slack** indicator.

## FAQ

### How does this differ from comment syncing through rules?

The synced task is not bound to a specific project and slack channel that rule 2-way comment syncing is. This feature also has improved user attribution for synced comments.
