---
fonte: https://www.notion.com/help/google-calendar-ai-connector
baixado: 2026-11-10
---

# Google Calendar AI Connector

In this help doc

## Learn how to connect Google Calendar events to Notion AI.

[Jump to FAQs](https://www.notion.com/help/google-calendar-ai-connector#faq)

------------------------------------------------------------------------

- This feature is available on Business and Enterprise Plans.

## [Connect Google Calendar to Notion AI](https://www.notion.com/help/google-calendar-ai-connector#connect-google-calendar-to-notion-ai)

**Who can connect Google Calendar to Notion AI?**

- You must be a Google Workspace admin and Notion workspace owner.

- Your workspace must be on the Business or Enterprise Plan.

**How do I connect Google Calendar?**

To connect Google Calendar to your Notion workspace:

1.  Go to `Settings` → `Notion AI`.

2.  Select `+` next to `Google Calendar` and start the connection.

3.  You'll be taken to the Notion AI for Google Marketplace app in a new tab. Click `Install`. **Don't close Notion during this process!**

4.  Follow the instructions to continue setting up. We recommend you install for `All users in my organization` for better answers from Notion AI.

5.  You'll see a new modal on your screen. Click `Confirm connection` to complete your setup.

The connection will be instant, but you might need to refresh your page to see Google Calendar reflected in the `All sources` menu in Notion AI.

### [Which content from Google Drive can be connected to Notion AI?](https://www.notion.com/help/google-calendar-ai-connector#which-content-from-google-drive-can-be-connected-to-notion-ai)

Notion AI can read all calendar data in your selected Google Workspace orgs. We maintain strict cross-user security; no user will see any other user’s private events in their search.

## [Where can I use my Google Calendar AI Connector?](https://www.notion.com/help/google-calendar-ai-connector#where-can-i-use-my-google-calendar-ai-connector)

You can search Google Drive via Notion AI Connectors in the following places:

- The Notion AI chat in the bottom right of Notion.

- `Notion AI` in your sidebar.

- `Search` in your sidebar.

## [Best practices and example prompts](https://www.notion.com/help/google-calendar-ai-connector#best-practices-and-example-prompts)

The Google AI Connector is most helpful for:

- Finding events or specific events with key words or guests.

- Viewing and analyzing events across days, weeks, months, and other time ranges.

You could try prompting Notion AI with the following:

- "When is my next meeting with Richard?"

- “What were the dates that I was in Seoul last month?"

- "Brief me on my schedule for next week."

- “When are my doctor’s appointments in September?”

------------------------------------------------------------------------

## FAQs

What Google Calendar data does Notion AI get access to?

Notion AI can read all calendar data in your selected Google Workspace orgs. We maintain strict cross-user security; no user will see any other user’s private events in their search.

Does Notion AI respect my Google Calendar permissions?

Yes. Each Notion user’s AI searches only that user’s Google Calendar inbox — we use an exact email address match. See more details about our [Notion AI security and privacy practices](https://www.notion.so/help/notion-ai-security-practices).

How long does it take for the integration to complete and how far back does it look?

Once the Google Calendar integration is set up, Google Calendar search will be available immediately. The integration can search the entire calendar.

How long does it take for Notion AI to read new Google Calendar events?

New events may take up to 3 hours to be indexed by Notion AI before they appear in search results. Larger data volumes may take additional time.

Can I limit the scope of my search to only Google Calendar?

Yes! In your Notion AI chat, select `All sources` → `Google Calendar`.

Who can access Google Calendar content using Notion AI?

You must be both a Google Workspace and Google Calendar user, as well as a Notion workspace member, to use this integration. Notion AI automatically maps Google Workspace members to their corresponding Notion accounts by email address. The system syncs permission changes from Google Workspace immediately.

How does Notion store or reference my Google Calendar data in its systems?

We do not store Google Calendar data in vector databases like Turbopuffer, but we may temporarily cache calendar content via something like memcached to provide a faster search experience. See [this article](https://www.notion.so/help/notion-ai-security-practices) for more information.

Can I add connect multiple Notion workspaces to my Google Calendar?

Not currently.

How can I disconnect my Google Calendar from Notion?

To disconnect Google Calendar, go to `Settings` → `Notion AI`. Select `⚙️` next to Google Drive → `Settings` → `Disconnect`.

What happens to my Google Calendar data if I disconnect?

Notion handles your Google Calendar data following strict data minimization principles. When you disconnect Google Calendar from Notion AI, your content becomes unsearchable immediately. All associated data is then deleted within 24 hours of your disconnection request.

## Contents

- [Connect Google Calendar to Notion AI](#connect-google-calendar-to-notion-ai)
- [Which content from Google Drive can be connected to Notion AI?](#which-content-from-google-drive-can-be-connected-to-notion-ai)
- [Where can I use my Google Calendar AI Connector?](#where-can-i-use-my-google-calendar-ai-connector)
- [Best practices and example prompts](#best-practices-and-example-prompts)
