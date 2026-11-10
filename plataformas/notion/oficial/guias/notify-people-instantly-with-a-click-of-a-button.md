---
fonte: https://www.notion.com/help/guides/notify-people-instantly-with-a-click-of-a-button
baixado: 2026-11-10
---

# Notify people instantly — with just a click of a button

## Send instant notifications to teams and stakeholders with a single button click — perfect for urgent alerts, incident response, and streamlined workflows.

- Automations
- Project management
- Engineering

4 min read

Buttons with automations send notifications or emails to the right people

------------------------------------------------------------------------

Buttons are a powerful way to automate repetitive tasks, like regenerating templates or triggering database actions. But here's something you might not know—you can also use them to send instant notifications. When you need to quickly notify specific people or teams about urgent matters, skip the back-and-forth by setting up notifications through your preferred channel—in-app, Slack, or Gmail. With a single click, your team will be instantly notified when something needs attention.

## [Set up a button-triggered notification for critical issues](https://www.notion.com/help/guides/notify-people-instantly-with-a-click-of-a-button#set-up-a-button-triggered-notification-for-critical-issues)

When you're managing critical bugs with your engineering team, sometimes issues come up that need immediate attention outside your usual process. If you’re an incident manager, you may want to quickly bring together your on-call team and key stakeholders when critical incidents occur. That's where buttons come in handy—they make it super easy to notify your team right away, so everyone can jump in when it matters most.

Here's how you can incorporate this simple feature in your workflow:

- **Locate the spot where you want to place your button —** For our example, adding a button at the end of our bug report page may be an effective way to let the reporter decide if the bug needs escalation. Choose where to put your button based on how you'll use it.

Identify where you want to insert your button

- **Add some context —** Add a clear message box that explains what the button does and when people should use it. Write simple instructions that help users know the right time to click the button.

- **Create the button —** Setting up the button is easy! Simply press the forward slash key and type `/button`.

Insert a new button into your page or database by typing /button

- **Trigger an in-app notification to the on-call incident manager —** First, notify the incident manager on call, or whoever needs to review the issue immediately through an in-app notification. Select `send notification` to from the list of options. You can select up to 20 specific people and customize your message using formulas.

Customize your formulas to control who receives notifications and what messages they see

- **Trigger an email to the team leads —** You can also add an action to Send mail to to notify people by email. For example, you can send an email to your team leads when there's an urgent issue. You can write your own subject line and message for the email. Check out[ this guide](https://www.notion.so/help/guides/Create-streamlined-project-management-workflow-using-database-automations) to learn more about advanced formulas.

Customize your formulas to control who receives notifications and the body of the email.

- **Set up a confirmation popup —** Add a popup message that appears before sending notifications. This helps prevent mistakes by asking users to confirm their action first. Choose `Show confirmation` from the list of options and write your own message.

- **Add a confirmation note —** Add a message that shows up after clicking the button. Choose `insert block` and type in what you want people to see after they click.

Add a popup and ask users to confirm their action before proceeding

- **Arrange to perfection —** Make sure to put the confirmation popup at the top of your button actions list. Then review the order of all your other actions to make sure everything is in the right sequence.

Voila! Your notification button is ready to use.

## [Three powerful ways to enhance your buttons](https://www.notion.com/help/guides/notify-people-instantly-with-a-click-of-a-button#three-powerful-ways-to-enhance-your-buttons)

Buttons really shine when you connect them to multiple actions, creating smooth workflows that do more with less effort. Check out [our guide to get started with button automations](https://www.notion.so/help/guides/automatically-generate-blocks-pages-with-buttons). In this section, let's look at three ways to make your notification buttons even more helpful:

- **Use webhooks in buttons—** Say your engineering team uses Zendesk for issue tracking. You can set up a button to create support tickets automatically. One click sends all the details to Zendesk, makes a new ticket, and lets your team know—without ever leaving Notion.

Use webhooks in your button automations to trigger actions in third-party apps like Zendesk

- **Customize your button fields using custom formulas—** You can make your notifications smarter by using advanced formulas. To do this, click the formula icon to connect information from other databases to your notifications. For instance, if you keep track of who's on call in a separate on-call triage database, you can automatically send notifications to the right person based on the current schedule.

- **Set up multi-step content review workflows—** For example, when a content piece needs review from multiple teams, one click can notify the marketing manager. After their review, the button automatically alerts legal for compliance check, followed by executive sign-off. This creates a streamlined review process with clear status tracking for all stakeholders.

And there you have it! With buttons, your team can keep everyone informed without the usual ping-pong of messages. Just one click transforms complex communication chains into a simple notification.

Share this guide

------------------------------------------------------------------------
