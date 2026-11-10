---
fonte: https://www.notion.com/help/guides/automate-client-follow-up-emails-with-custom-agents
baixado: 2026-11-10
---

# Automate client follow-up emails with Custom Agents

## Learn how to build a Custom Agent that turns your client meeting notes into a follow-up email with the key topics, decisions, and next steps.

5 min read

Vídeo: https://www.youtube.com/watch?v=OR2zYx842Q4

------------------------------------------------------------------------

## [What you'll build](https://www.notion.com/help/guides/automate-client-follow-up-emails-with-custom-agents#what-you'll-build)

A Client Meeting Follow-Up Agent that helps you move fast after a customer call. It reads your meeting notes and drafts a follow-up email that captures the key topics, decisions, and next steps, so you can quickly edit and send instead of starting from a blank page.

### [Who this is for](https://www.notion.com/help/guides/automate-client-follow-up-emails-with-custom-agents#who-this-is-for)

Any customer-facing team member who runs client calls and needs to follow up quickly, especially in sales, customer success, and professional services.

Have these ready before you build

- A Notion database where your client meeting notes or transcripts live (one page per meeting)

- A customer accounts database the agent can reference for deal context (stage, size, contacts)

- A destination for your email draft: a connected email platform (Gmail, Outlook), or a Notion page where the agent can drop the draft for you to copy and send.

## [1. Prompt the agent](https://www.notion.com/help/guides/automate-client-follow-up-emails-with-custom-agents#1.-prompt-the-agent)

In this step, you will set the agent's direction: what to extract from your client meeting notes, what to write, and the style and preferences it should follow every time.

PromptYou're a Sales Follow-Up Assistant for an AE running client calls across multiple deal stages. After each call, pull the transcript and the customer's account context (deal stage, deal size, contacts, prior interactions) and draft a follow-up email in my voice. Tailor each draft to where the deal sits, whether that's discovery, demo, proposal, negotiation, or post-close. Keep each draft under 150 words, open with a real moment from the conversation, and include the most relevant resource from my video library when a prospect asks for one. At the end of the day, surface all drafts for review along with a prioritized task list and the two or three follow-ups that need my attention first.[Try it\!→](https://app.notion.com/?target=new_custom_agent&prefill=You're%20a%20Sales%20Follow-Up%20Assistant%20for%20an%20AE%20running%20client%20calls%20across%20multiple%20deal%20stages.%20After%20each%20call%2C%20pull%20the%20transcript%20and%20the%20customer's%20account%20context%20(deal%20stage%2C%20deal%20size%2C%20contacts%2C%20prior%20interactions)%20and%20draft%20a%20follow-up%20email%20in%20my%20voice.%20Tailor%20each%20draft%20to%20where%20the%20deal%20sits%2C%20whether%20that's%20discovery%2C%20demo%2C%20proposal%2C%20negotiation%2C%20or%20post-close.%20Keep%20each%20draft%20under%20150%20words%2C%20open%20with%20a%20real%20moment%20from%20the%20conversation%2C%20and%20include%20the%20most%20relevant%20resource%20from%20my%20video%20library%20when%20a%20prospect%20asks%20for%20one.%20At%20the%20end%20of%20the%20day%2C%20surface%20all%20drafts%20for%20review%20along%20with%20a%20prioritized%20task%20list%20and%20the%20two%20or%20three%20follow-ups%20that%20need%20my%20attention%20first.)

1.  Open `Agents` from your sidebar and click `+` to start a new chat.

2.  Describe what you want the agent to do (the*Try this prompt* callout above is a good starting point).

3.  The agent will draft `instructions`, suggest `triggers`, and flag the `Tools and access` it needs. You'll fine-tune each of these in the next steps.

4.  Answer any quick follow-ups, like where your call notes or transcripts live and where you want the agent to draft the email.

Vídeo: https://www.youtube.com/watch?v=OR2zYx842Q4&t=50s

Helpful tips

## [2. Set triggers](https://www.notion.com/help/guides/automate-client-follow-up-emails-with-custom-agents#2.-set-triggers)

In this step, you will choose when the agent runs. You can trigger it on demand by @mentioning it, or you can set a scheduled trigger so it drafts emails for every call at the end of your day.

1.  Click `Add trigger`.

2.  Under `Recurring`, choose `On a schedule`. Set it to run after your client calls wrap, for example weekdays at 3:30 p.m. in your local time zone.

3.  Click `Add trigger` to save.

Vídeo: https://www.youtube.com/watch?v=OR2zYx842Q4&t=99s

Helpful tips

## [3. Connect tools and pages](https://www.notion.com/help/guides/automate-client-follow-up-emails-with-custom-agents#3.-connect-tools-and-pages)

Connect the right tools and pages so your agent has the context it needs. It can reference the call, pull in account details, and include relevant resources to draft a more personalized follow-up.

1.  Open your agent settings and go to `Tools and access`.

2.  Click `Add` and connect the pages and databases that have customer context, like your customer accounts database (`Can view`).

3.  Connect your meeting transcripts or call notes database (`Can edit content`).

4.  Connect your preferred email platform so the agent can create drafts in your inbox (`Read inbox`, `Draft emails`, and `Send emails`).

Vídeo: https://www.youtube.com/watch?v=OR2zYx842Q4&t=128s

Helpful tips

## [4. Review output](https://www.notion.com/help/guides/automate-client-follow-up-emails-with-custom-agents#4.-review-output)

Before you rely on the agent for real follow-ups, do a test run and review the draft. You'll want to confirm that it is accurate to the call, specific to the customer, follows the structure you set, and is written in your voice.

1.  Open your agent settings and click `Run agent` to do a test run.

2.  If you have multiple triggers, pick the one you want to test first, like the end-of-day scheduled trigger.

3.  If the agent asks for what to use as input, point it to a recent call or meeting transcript.

4.  Open the draft it creates and review it.

Vídeo: https://www.youtube.com/watch?v=OR2zYx842Q4&t=196s

## [5. Provide feedback](https://www.notion.com/help/guides/automate-client-follow-up-emails-with-custom-agents#5.-provide-feedback)

Now refine the output in chat. Tell the agent what to change, approve any instruction updates, and then run it again. The goal is to get to a draft that is accurate, in your voice, and ready to send with minimal edits.

1.  Reply in chat with what you want changed, and then ask the agent to try again.

2.  If the agent asks to update its instructions, approve the change.

3.  Run it again and compare the new draft.

Vídeo: https://www.youtube.com/watch?v=OR2zYx842Q4&t=226s

Keep tuning your agent over time as your customers and relationships evolve, so drafts stay sharp.

More resources

- To keep improving your agent over time, read our [Custom Agent best practices guide](https://www.notion.com/help/guides/best-practices-for-improving-your-custom-agent).

- If you want to build a fuller mail workflow, see how to [manage your inbox and calendar automatically with Custom Agents](https://www.notion.com/help/guides/manage-your-inbox-and-calendar-with-custom-agents).

- Explore more Custom Agent workflows on [Notion Academy](https://academy.notion.com/page/notion-ai-catalogue).

Share this guide

------------------------------------------------------------------------
