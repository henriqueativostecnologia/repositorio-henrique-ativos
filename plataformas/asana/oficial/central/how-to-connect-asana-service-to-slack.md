---
fonte: https://help.asana.com/s/article/how-to-connect-asana-service-to-slack?language=en_US
baixado: 2026-11-10
---

# How to connect Asana Service to Slack

Asana Service Management lets requesters get help without leaving Slack. When you connect a queue to a Slack channel, Service AI can respond to requests, queue members can manage tickets in Asana, and requesters can follow updates in the same Slack thread.

## Connect a queue to Slack

Make sure the Asana app has been added to the Slack channel that you want to connect. If it has not been added, the channel will not appear as an option during setup.

Setup happens at the queue level. After you connect a Slack channel, it becomes an intake channel for the queue, and messages posted there can become tickets in the queue.

1.  Navigate to the queue.
2.  Select **Settings** in the top-right corner.
3.  Scroll to **Routing**.
4.  Select **Slack channel integration**.
5.  Select **Connect**.
6.  Follow the instructions to connect Asana to Slack.
7.  Choose the Slack channel that should receive requests and updates, then complete the connection.

After you connect the channel, Service AI can respond using your knowledge base and approved web sources. Queue members can manage tickets in Asana, prioritize work by SLA, and review the full ticket context.

## Manage requests from Slack

Requests created through Slack connect directly to the queue, just like requests created through the portal or email. Comments and updates sync between the Slack thread and the Asana ticket, so a reply in either place keeps the other view up to date.

When a conversation becomes a ticket, it appears in the queue for follow-up by a queue member. Most team members will still work the queue from Asana, where they can prioritize by SLA and see full ticket context, but they can also take quick action directly from Slack without switching tools.

## Use emoji shortcuts in Slack

Queue members with an Enterprise license can use emoji reactions in Slack to take action without leaving the thread:

1.  **✅** resolves the ticket.
2.  **👀** assigns the ticket to the queue member.
3.  **🔗** displays the Asana ticket URL to the queue member.

Depending on the state of the thread, the **👀** reaction can also convert an active conversation to a ticket. To give Service AI time to help the requester, wait for the requester to ask for live support before assigning the conversation to yourself.

## Troubleshoot the Slack connection

**The Slack channel does not appear as an option.** Make sure the Asana app has been added to the channel. Then return to the queue setup and check the channel list again.

**Updates are not syncing.** Try uninstalling and reinstalling the Asana app in Slack. If the Slack workspace requires admin approval for app permissions, ask a Slack admin to authorize any requested permissions during the reinstall.

**Emoji actions are not working.** Confirm that the Asana app is installed in the channel and that the queue member has an Enterprise license. If the issue continues, reinstall the Asana app and try the reaction again.
