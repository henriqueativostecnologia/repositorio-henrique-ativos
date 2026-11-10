---
fonte: https://www.notion.com/help/guides/share-social-media-posts-from-notion-with-webhook-actions
baixado: 2026-11-10
---

# Share social media posts from Notion with webhook actions

## Learn how to automate your social media workflows by connecting Notion with your favorite platforms using webhook actions.

- Automations
- Project management
- Social media

4 min read

Use webhook actions to automatically publish social media posts.

------------------------------------------------------------------------

Work happens across many different tools. That's why we've made it simple to connect Notion with [hundreds of your favorite apps](https://www.notion.so/integrations/all) — so you can bring everything into one united workspace. When your tools work together smoothly, you can focus on what matters. And with webhooks, you can do even more — connecting Notion's automation features with any tool you need, even beyond our integration library.

Think of webhook actions as digital bridges connecting Notion to other tools you use. They provide a simple way to link Notion with other apps—no coding needed. With tools like Zapier or Make, you can set up automatic workflows that handle tasks for you.

In this guide, we’ll walk you through how to publish social media posts using webhook actions and share some helpful ways to make your workflow easier.

## [How do webhook actions work with Notion?](https://www.notion.com/help/guides/share-social-media-posts-from-notion-with-webhook-actions#how-do-webhook-actions-work-with-notion)

When something happens in Notion (like marking a task complete), these messengers instantly notify your other apps—keeping everything in sync without you having to do the work.

Let's break down how webhook actions work in Notion—they're simpler than you might think! When you set up a webhook action, Notion sends updates (HTTP events) to other apps (that's just tech-speak for sending data securely over the internet).

There are two easy ways to trigger webhook actions in Notion:

- Through database automations—like when you check off a task

- Using button blocks—for when you want to trigger an action manually

## [Automated social media posting with webhook actions](https://www.notion.com/help/guides/share-social-media-posts-from-notion-with-webhook-actions#automated-social-media-posting-with-webhook-actions)

Let's say you manage your team's social media workflow in Notion. Wouldn't it be great if posts could automatically go live once they're approved? Instead of manually checking for approvals and publishing content, you can use webhook actions to handle it for you. For example, when the final reviewer marks a post as "Approved" in your social media database, webhook actions can automatically trigger the publishing process. In our example, we'll see how Notion and Make work together to have something posted automatically on LinkedIn.

### [Generate a webhook URL](https://www.notion.com/help/guides/share-social-media-posts-from-notion-with-webhook-actions#generate-a-webhook-url)

Before you set up automations in Notion, you'll need a webhook URL from Make or your preferred third-party app. This will look slightly different in every tool, but the end result should be a URL that you can paste into your Notion automation. Check out the documentation of your preferred tool to learn more.

Now whenever Make gets a signal from Notion, it'll automatically share your content on LinkedIn.

### [Set up in Notion](https://www.notion.com/help/guides/share-social-media-posts-from-notion-with-webhook-actions#set-up-in-notion)

Remember that webhook URL from Make? You'll need it for the next part. Let's set up your automation in Notion:

- Open your social media database and click the lightning bolt (⚡️) icon in the top right

- Click `New automation `to get started

Click the lightning bolt icon and name your automation

- Set up your trigger—choose "Status" and "approved" so your automation runs whenever a post is marked as approved

- In the "do" section, pick "Send webhook" from the dropdown

- Paste your Make webhook URL into the URL field

- Select the properties you want to send—in this case, "Final Copy"

Paste your webhook URL in the box and select the properties you want to publish

Voilà! Now whenever you mark a post as `Approved`, Notion will automatically share the text from the `Final Copy` property and tell Make to post it on LinkedIn.

## [Go further with buttons and webhook actions to automate your workflows](https://www.notion.com/help/guides/share-social-media-posts-from-notion-with-webhook-actions#go-further-with-buttons-and-webhook-actions-to-automate-your-workflows)

Buttons are an easy way to streamline your workflow and trigger automations with just a few clicks. Here are two practical ways you can use buttons with webhook actions:

- **Use buttons to directly post social media content—** As a content reviewer, you can proofread the final copy of a blog post before sharing it on platforms like "X" or "Threads". By adding a button to your social media post's review page, you can automatically publish the content with one click — just use the same setup from above!

Add webhooks directly to button automations

- **Use buttons to automate support tickets—**Let's say you manage a database tracking issues from your team, while your engineering team handles fixes in a different tool, like Zendesk. By adding a button to your bug reports page, you can automatically create a ticket in Zendesk and get a confirmation email right away. This streamlined process lets you notify your support team without having to switch tools—all from within Notion.

You can connect webhook actions to third-party tools like Zendesk and generate tickets automatically with a click of a button in Notion

Webhook actions open up so many possibilities-- from setting up workflows that save you time to keeping everyone in the loop across different tools. Start small with something simple, then build from there as you get the hang of it. The goal is to make your work flow more smoothly, one automation at a time.

Share this guide

------------------------------------------------------------------------
