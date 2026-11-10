---
fonte: https://www.notion.com/help/guides/self-improving-answer-bot
baixado: 2026-11-10
---

# Build a self-improving answer bot

## Learn how to build a self-improving answer bot. Questions go in. Useful answers come out. Every miss becomes a clue about what the system should learn next.

Guide

------------------------------------------------------------------------

Someone asks a question in Slack. You know the answer exists somewhere. Maybe it’s in a meeting note, an out-of-date wiki, or—worst case scenario—it lives in one person’s head.

Eventually someone finds the answer, shares it, and everyone moves on. Great for now, but the answer stays in the thread, the knowledge isn’t captured, and the question comes back again next week.

This guide turns that cursed loop into a Self-improving answer bot. Questions go in. Useful answers come out. Every miss becomes a clue about what the system should learn next.

You’ll build it in two parts:

- **(Part 1) The Q&A Agent** — Use Notion’s guided setup to create your Q&A Agent. Once it’s ready, review the Q&A Log, Learning Log, and Playbook created behind the scenes.

- **(Part 2) The Self-Improving Agent** — Follow this cookbook to build an agent that reviews the Q&A Log and trusted sources. The agent then drafts targeted updates and applies them only after human approval.

By the end, every question your team asks will make the next answer better.

**Build time**: About 90 minutes once prerequisites are confirmed. Allow additional time for testing and troubleshooting.

**Reading time**: About 45 minutes.

## [What you’ll build](https://www.notion.com/help/guides/self-improving-answer-bot#what-you%E2%80%99ll-build)

[TABLE]

## [Part 1: Getting started](https://www.notion.com/help/guides/self-improving-answer-bot#part-1-getting-started)

### [Choose a use case and check readiness](https://www.notion.com/help/guides/self-improving-answer-bot#choose-a-use-case-and-check-readiness)

Start with the questions your team is tired of answering. The ones that send someone digging through Slack and scattered tools or tagging in the same expert over and over again. That’s the loop you’ll fix.

Here are a few common examples:

IT

\#it-help, \#access-requests

**Example questions**

- How do I connect to the VPN?

- Which software is approved for screen recording?

- How do I set up a new laptop?

**Trusted sources**

- Setup guides

- Troubleshooting pages

- Supported-software policies

- Known issues

Product

\#product-questions, \#roadmap-help

**Example questions**

- What changed in the latest release?

- What did we decide about this feature?

- Is this feature available to Enterprise customers?

**Trusted sources**

- PRDs and decision logs

- Project databases

- Meeting notes

- Issue trackers

People

\#people-help, \#new-hire-questions

**Example questions**

- How do I enroll in benefits?

- What is our parental leave policy?

- Where can I find the new-hire checklist?

**Trusted sources**

- Employee handbook

- Benefits and office guides

- Onboarding documentation

- Approved FAQs

Sales and enablement

\#sales-questions, \#sales-enablement

**Example questions**

- What’s our approved answer when a prospect asks about data residency?

- How do we position our product against a competitor?

- Which customer story should I share with a healthcare prospect?

**Trusted sources**

- Approved messaging

- Sales playbooks

- Competitive battlecards

- Customer stories

### [Confirm prerequisites](https://www.notion.com/help/guides/self-improving-answer-bot#confirm-prerequisites)

A little prep before we start cooking. Make sure Custom Agents are enabled, Slack is connected, and you have the right permissions to build and test the entire system.

**Custom Agent creation is enabled**

- A workspace owner has enabled creation in `Settings` → `Notion AI `→ `Agents`.

- There is no fixed credit number for this build. Credits vary with source reading, actions, model choice, and run frequency. Measure real test runs in Insights before turning on broad triggers or schedules.

**Slack is connected**

- A Slack admin has connected Slack to Notion.

- For Slack Enterprise Grid, Custom Agents can view and post messages is set to `Read and post messages`.

- The Slack account used for the connection has the same email address as the Notion account. A mismatch can cause triggers to fail without an error.

**Check that you have the right permissions**

- You are able to edit and share every trusted source.

- The Q&A Agent will be able to read and view every trusted source.

- The Self-Improving Agent is able to edit trusted sources.

## [Build the Q&A Agent](https://www.notion.com/help/guides/self-improving-answer-bot#build-the-q&a-agent)

A question lands in Slack. Instead of hunting for the answer across different tools, the Q&A Agent searches the sources your team trusts and brings the answer back to the conversation.

Notion's guided setup will walk you through the initial build and get your agent up and running.

To get started:

- Open **Agents** in your sidebar and click `+ New Agent`.

- Choose `Self-improving answer bot` to launch the guided setup.

### [Set up your Q&A Agent](https://www.notion.com/help/guides/self-improving-answer-bot#set-up-your-q&a-agent)

Start by choosing what your agent should answer and where it should look for answers.

**1.1 Choose the questions your agent will answer**

- Pick from common use cases like Product, IT, Sales, People, or Office.

- Have a different use case in mind? Choose `Custom` to define your own.

**1.2 Choose where your agent will answer questions**

- Pick an existing Slack channel or create a new one right from the guided setup.

**1.3 Connect your trusted knowledge sources**

- By default, your agent can access public Notion pages and Slack channels.

- Review which sources it can access. Keep it focused on sources your team trusts.

Once you've got the ingredients in place, click `Create agent` and let Notion take it from here.

### [Review and fine-tune your agent's setup](https://www.notion.com/help/guides/self-improving-answer-bot#review-and-fine-tune-your-agent's-setup)

The guided setup takes you to your agent’s setup page. Take a peek behind the scenes and make a few tweaks before testing.

**2.1 Review your Q&A Log database**

The Q&A Log is a database that keeps a history of questions, answers, and unresolved requests so you can track how your agent is performing.

**Best practices:**

- The database comes with properties like request `status`, `question type`, `requester`, and `related Slack thread`. Think about what else your team might want to track and adjust the properties as needed.

- Use question types to spot recurring requests and statuses to identify questions that still need attention.

**2.2 Review your Learning Log database**

The Learning Log is a database where your agent saves new knowledge and memories you share with it. Each entry includes details like its source, scope, and confidence.

**Best practices:**

- Your log will be empty at first. Test your agent by asking a few questions your team is likely to ask.

- Review new entries to make sure the information comes from reliable sources and applies to the right situations.

- Correct outdated information or remove anything your agent should no longer rely on. Nobody wants stale ingredients in the mix!

**2.3 Fine-tune your Playbook**

Think of the Playbook as your agent's recipe for answering questions. It's a Notion page that guides your agent on how to find answers and when to ask for help.

**Best practices:**

- Tell your agent which sources to check first. For example, you might want it to search your internal knowledge base before digging through Slack conversations.

- Be clear about what your agent should never do and when to escalate a question rather than guess.

- Give your agent guidance on how to respond and what to do when someone corrects an answer.

You can edit the Q&A Log, Learning Log, and Playbook directly. You can also ask your agent to update them.

### [Test your Q&A Agent](https://www.notion.com/help/guides/self-improving-answer-bot#test-your-q&a-agent)

Time for a taste test! The guided setup will first ask whether your agent has enough context to answer questions. If anything's missing, you can share more knowledge or connect additional sources.

**3.1 Test your agent with real questions**

Choose one of the suggested questions or write your own. Start with questions your team usually asks, then try a few trickier ones where information might be missing or conflicting.

As you review the answers, check that your agent:

- Used the question and relevant thread context.

- Found a source-supported answer.

- Kept the response concise.

- Linked to supporting sources.

- Created a log record only when there was something worth capturing.

**3.2 Try your agent in Slack and review the Q&A Log**

Once you're happy with the answers, select `Looks right - I'm ready to try it in Slack`.

Ask a few questions in your chosen Slack channel and check that your Q&A Log captures each outcome correctly.

- **Supported answers** should appear in the Answers view with the question, answer, and source Slack thread.

- **Missing information** should produce an honest “I don't know” and a record in the Requests view, with the answer left empty.

- **Conflicting information** should be acknowledged without guessing, with the unresolved question captured in the Requests view.

- **Corrections** should prevent the agent from repeating unsupported information and create a Requests record for follow-up.

**3.3 Troubleshoot common issues**

Even the best recipes don't always turn out perfectly on the first try, and that's okay! If something isn't working as expected, here are a few things to check.

- **Answer failures**

  - The agent provided an answer even though its trusted sources did not support a reliable response.

  - The agent said the answer was missing, even though it exists in a configured trusted source.

  - The answer was too long or did not link to supporting sources.

- **Q&A Log failures**

  - A relevant question did not create a Q&A Log record.

  - A supported answer did not appear in the Answers view.

  - An unsupported, incomplete, or conflicting answer did not appear in the Requests view.

  - The record’s `Question`, `Answer`, or `Source Slack thread` was inaccurate or missing.

  - In a direct-chat test, the agent invented a Slack thread, source, or other evidence that wasn’t provided.

Tell your agent what went wrong and ask it to make the necessary adjustments. Then, try the same question again to see if the fix worked.

### [Publish and share your Q&A Agent](https://www.notion.com/help/guides/self-improving-answer-bot#publish-and-share-your-q&a-agent)

Your Q&A Agent is ready to meet the team! Before rolling it out, a few finishing touches can help make the introduction smoother.

- Publish your agent and confirm it's responding in the right Slack channel.

- Share your Q&A Agent with other agent managers who can help maintain it and handle unresolved questions.

- Let your team know how to flag incorrect answers or share feedback.

- Review the Q&A Log regularly to spot recurring questions and opportunities to improve.

## [Part 2: Make your Q&A system self-improving](https://www.notion.com/help/guides/self-improving-answer-bot#part-2-make-your-q&a-system-self-improving)

You now have a complete Q&A system.

Your Q&A Agent can answer questions in Slack, show the sources it used, and record every answer or unresolved request in the Q&A Log. The log gives your team a clear view of what people are asking and where the available knowledge falls short.

If you arrived from the in-product guided setup, you already have this Part 1 foundation. Continue below to add the Self-Improving Agent.

Part 1 helps with the question in front of you. Part 2 makes every miss useful.

## [Build the Self-Improving Agent](https://www.notion.com/help/guides/self-improving-answer-bot#build-the-self-improving-agent)

### [Turn loose ends into better knowledge](https://www.notion.com/help/guides/self-improving-answer-bot#turn-loose-ends-into-better-knowledge)

The Q&A Log shows you exactly where the system gets stuck. The Self-Improving Agent picks up those loose ends, gathers evidence, and drafts the smallest useful fix. A person still decides what becomes trusted knowledge.

### [Create the Self-Improving Agent](https://www.notion.com/help/guides/self-improving-answer-bot#create-the-self-improving-agent)

Now build the second half of the loop.

### [Expand the Q&A Log](https://www.notion.com/help/guides/self-improving-answer-bot#expand-the-q&a-log)

Part 1 needed only Question, Answer, and Source Slack thread. Before configuring the Self-Improving Agent, add the following properties to the Q&A Log database by pasting this prompt into the Notion Agent:

PromptUpdate the Q&A Log database schema with the following: Update type (Select) — New article or Update existing article. Proposed destination (URL) — The existing article to update, or the proposed location for a new article. Reviewer (Person) — The person accountable for reviewing the draft. Status (Status) — Needs agent review, Needs human review, Approved, Published, Archived. Applied at (Date) — When the approved update was applied. Organize Status into these groups: - To-do: Needs agent review - In progress: Needs human review, Approved - Complete: Published, Archived

The proposal itself lives in the Q&A Log page body, not in a property. Use this structure:

Prompt\## Proposed knowledge update \[Draft the proposed new article or focused update here.\] \## Supporting evidence - \[Source and relevant evidence\]

Reviewers edit the draft directly or leave page comments. When the draft is ready to apply, they change Status to Approved.

#### 1. Create a starter agent

Time to close the loop and turn those knowledge gaps into trusted knowledge. Start with a draft agent, then teach it where to look, what to change, and how to ask for approval.

Open Agents in the sidebar and click +, then paste in this prompt.

PromptCreate a draft Custom Agent named “Self-Improving Agent” with no active triggers. The Self-Improving Agent reviews unresolved Requests in a Q&A Log, which will be connected later. It prepares focused, evidence-backed new articles or updates in each Request page body for human review. It proposes one Update type, one Proposed destination, and one Reviewer. It never edits a trusted source before a person approves the draft. After approval, it applies only the approved change and records that the update was completed. Match the destination’s existing style and structure. Keep proposed and applied changes concise and limited to what the evidence supports. Consolidate only clear duplicate Requests while preserving unique evidence.

Alternatively, you can just [click this link](https://www.notion.so/ai?aq=Create%20a%20draft%20Custom%20Agent%20named%20%E2%80%9CSelf-Improving%20Agent%E2%80%9D%20with%20no%20active%20triggers.%0A%0AThe%20Self-Improving%20Agent%20reviews%20unresolved%20Requests%20in%20a%20Q%26A%20Log%2C%20which%20will%20be%20connected%20later.%20It%20prepares%20focused%2C%20evidence-backed%20new%20articles%20or%20updates%20in%20each%20Request%20page%20body%20for%20human%20review.%0A%0AIt%20proposes%20one%20Update%20type%2C%20one%20Proposed%20destination%2C%20and%20one%20Reviewer.%20It%20never%20edits%20a%20trusted%20source%20before%20a%20person%20approves%20the%20draft.%20After%20approval%2C%20it%20applies%20only%20the%20approved%20change%20and%20records%20that%20the%20update%20was%20completed.%0A%0AMatch%20the%20destination%E2%80%99s%20existing%20style%20and%20structure.%20Keep%20proposed%20and%20applied%20changes%20concise%20and%20limited%20to%20what%20the%20evidence%20supports.%20Consolidate%20only%20clear%20duplicate%20Requests%20while%20preserving%20unique%20evidence.). Save it, then continue to the next step.

#### 2. Finish the setup

**2.1 Add Notion triggers**

In Triggers, set three Notion triggers:

1.  Page added to database: Run when any page is added to the Q&A Log. The Self-Improving Agent stops when Answer is present and reviews the entry when Answer is empty.

2.  Property updated in database: Run when Status changes to Needs agent review so the Agent can reread the edited draft and page comments, then revise the same proposal.

3.  Property updated in database: Run when Status changes to Approved so the Agent can apply the approved draft.

**2.2 Add the Q&A Log and trusted sources**

Add the Q&A Log with Can edit access.

In Tools & Access, add the same trusted sources as you did for the Q&A Agent.

- Add Notion pages with Can edit access.

- Add connections with Read and write access

**2.3 Update the job and instructions**

Now that you’ve added the trusted sources, Q&A Log, and Notion triggers, you can update the Self-Improving Agent’s instructions.

Identify the person who should review proposed changes. They’ll be notified in real-time by the Self-Improving Agent.

Replace the placeholder below with their actual Notion @mention, then paste this prompt into the Notion Agent from the Self-Improving Agent settings page:

PromptYou are the Self-Improving Agent. You review unresolved Requests in the configured Q&A Log, prepare evidence-backed improvements to trusted sources, and apply only changes a person approves. Default reviewer: \[REPLACE WITH THE HUMAN REVIEWER’S ACTUAL NOTION @MENTION\] When a page is added to the Q&A Log or Status changes to Needs agent review: 1. Read Question, Answer, Source Slack thread, the current page body, page comments, and Reviewer. 2. If Answer is not empty, this is a completed Answer. Do not prepare a knowledge update and stop. 3. Review related Q&A Log records, the Slack thread when available, and the relevant trusted sources. 4. If the Request duplicates something already addressed, preserve any unique evidence in the more complete record, set the duplicate’s Status to Archived, and stop. 5. Otherwise, prepare the smallest change supported by the evidence. Write or revise the draft under “Proposed knowledge update” in the page body. List the evidence used under “Supporting evidence.” 6. Set Update type to New article or Update existing article. Set Proposed destination to the single existing article or proposed wiki location that should receive the approved change. 7. Keep the existing Reviewer. If Reviewer is empty, set it to the default reviewer. 8. Set Status to Needs human review, then leave a comment mentioning the Reviewer. Ask them to edit the draft directly or leave comments, then set Status to Approved when it is ready. If they want the Agent to revise it, ask them to set Status to Needs agent review. 9. Stop without editing a trusted source. When Status changes to Approved: 1. Confirm that the page body contains a draft and supporting evidence, and that Update type and Proposed destination are present. 2. Apply only the approved page-body draft to Proposed destination, following Update type and matching the destination’s existing style and structure. 3. Record the current date in Applied at and set Status to Published. 4. If anything required is missing, do not edit a trusted source. Leave a comment mentioning the Reviewer and state what is needed. Keep proposed and applied changes clear, concise, and limited to what the evidence supports.

Optional: If you’d like to group reviewer notifications, choose either Daily or Weekly, update the placeholder, then paste this prompt into Notion Agent from the Self-Improving Agent settings page.

PromptUpdate this Self-Improving Agent to group reviewer notifications \[DAILY OR WEEKLY\] instead of sending them immediately. Remove the instruction to comment when each entry moves to Needs human review. Keep setting Reviewer and Status = Needs human review. Add a recurring trigger for the selected cadence. For each scheduled run, group all Needs human review entries by Reviewer. For each reviewer, leave one comment on their oldest pending entry that mentions them and links to every draft awaiting review. Reviewers should edit the page-body draft directly or leave comments. They set Status to Approved when the draft is ready, or Needs agent review when they want another Agent revision. Do not send both immediate and grouped notifications. Do not change any other instructions or triggers.

**2.4 Don’t forget to save**

Click the blue Save button at the top right.

#### 3. Test your Self Improving Agent

The Self-Improving Agent works through Requests in the Q&A Log, so that’s where you’ll test it.

**3.1 Confirm setup is complete**

The Self-Improving Agent has Can edit access to the Q&A Log and trusted Notion sources.

Connected trusted sources have Read and write access.

All three Notion triggers point to the Q&A Log, use the correct events, and remain toggled off:

- A page is added.

- `Status` changes to `Needs agent review`.

- `Status` changes to `Approved`.

The default reviewer is an actual Notion @mention.

Instructions tell the Self-Improving Agent how to:

- Draft or revise the proposal in the page body with supporting evidence.

- Set `Update type `and `Proposed destination`.

- Assign or retain the `Reviewer` and mention them when review is needed.

- Read direct edits and comments before revising the same draft.

- Consolidate clear duplicates without losing unique evidence.

- Wait for human approval before changing a trusted source.

- Apply only the approved draft, record `Applied at`, and set `Status` to `Published`.

**3.2 Test it out with real entries**

Set up testing with Notion Agent. From the Self-Improving Agent settings page, paste the prompt below into Notion Agent.

PromptPrepare this Self-Improving Agent for testing. 1. Create a temporary Notion page named “Self-Improving Agent test source.” Add a short, clearly labeled piece of sample knowledge that is safe to change. 2. Add that page to this Self-Improving Agent in Tools & Access with Can edit access. 3. Review the Self-Improving Agent’s current job, instructions, Q&A Log, trusted sources, and Notion triggers. 4. Create a concise four-step test plan using the temporary source page. Include one test for each path: - Proposal - Reviewer feedback - Duplicate - Approved change For each test, use the exact Q&A Log property names and Status values in this setup. Return: \[TEST\] \[TRIGGER TO TURN ON\] \[EXACT WIKI DATABASE ACTION\] \[EXPECTED RESULT\] Use clearly labeled test records. Keep the temporary source unchanged until the Approved change test. Do not run the tests, enable triggers, create Q&A Log records, change the Self-Improving Agent’s instructions, or edit any existing trusted source. After creating and connecting the temporary source page, return only the four test steps.

When Notion Agent finishes, click Save. Turn on only the trigger you’re testing, then turn it off before testing the next path.

Confirm that:

- Proposal: The Self-Improving Agent writes a focused draft and supporting evidence in the page body, sets `Update type` and `Proposed destination`, assigns or retains the `Reviewer`, sets `Status` to `Needs human review`, mentions the reviewer, and leaves the trusted source unchanged.

- Reviewer edits or comments: Edit the page-body draft or leave a comment, then set `Status `to `Needs agent review`. Confirm the Agent revises the same draft, returns it to `Needs human review`, and mentions the reviewer again without changing the trusted source.

- Duplicate: The Agent preserves unique evidence and archives only the clear duplicate.

- Approved change: The Agent changes only the temporary source according to `Update type` and `Proposed destination`, records `Applied at`, and sets `Status` to `Published`.

**3.3 Troubleshoot common issues**

Something will probably get weird, but that’s okay! That’s what testing is for.

Check only the failures you observed:

- **Trigger failures**

  - Adding a record did not start the Self-Improving Agent.

  - Changing `Status` to `Needs agent review` did not start a revision.

  - Changing `Status` to `Approved` did not apply the change.

- **Proposal and review failures**

  - The proposal was unsupported, too broad, or missing its evidence, destination, or reviewer.

  - The Self-Improving Agent changed a source before approval.

  - The reviewer was not mentioned.

  - Reviewer feedback did not produce a revised proposal.

- **Duplicate and approved-change failures**

  - A clear duplicate was not archived, or unique evidence was lost.

  - A record that merely overlapped or conflicted was incorrectly archived.

  - An approved change modified unrelated content.

  - The completed record did not include `Applied at `or `Status = Published`.

Paste the checked failures into the Notion Agent prompt below, then paste the prompt into a new Notion Agent chat from the Self-Improving Agent settings page.

PromptFix this Self-Improving Agent based on these failures: \[PASTE THE CHECKED FAILURES\] Review the Self-Improving Agent’s current job, instructions, Q&A Log, trusted sources and access, and Notion triggers. Diagnose trigger and access problems separately from instruction problems, then make the smallest necessary fix. Change the instructions only when the failure is instructional. Reinforce these requirements only where the failures show they are needed: - Use only the Q&A Log record, its page body and comments, the Slack thread when available, and trusted sources. - Prepare the smallest supported proposal in the page body and include supporting evidence. - Set one Update type and one Proposed destination. - Never edit a trusted source before human approval. - Mention the Reviewer when human review is required. - Revise the same page-body draft after reviewer edits or comments. - Archive only clear duplicates after preserving unique evidence. - Apply only an approved draft to the named destination. - Record Applied at and set Status to Published after write-back. If a trigger or access setting must be fixed manually, tell me exactly what to change. Do not enable triggers, edit test records, modify trusted sources, change the Q&A Log schema, change the default reviewer, or change unrelated instructions. Return only the failures to retest and any settings I must fix manually.

Save the changes and rerun only the failed paths with fresh test records.

#### 4. Publish the Self-Improving Agent

The loop is ready. The Agent can turn Requests into drafts, wait for a person, then apply only what gets approved.

Publish it. Turn on all three Notion triggers and click Save.

Optional: Share the Self-Improving Agent. Share it with any other agent managers who will help maintain it.

Introduce the Self-Improving Agent to the knowledge owners. Let the people responsible for its trusted sources know how drafts, comments, and approvals work. You can use this draft message as a starting point.

PromptMeet @\[AGENT NAME\], our new Self-Improving Agent for \[WIKI AREA\]. It reviews Requests in \[Q&A LOG\], drafts focused updates in each Request page, and tags the proposed reviewer when a draft is ready. Edit the draft directly or leave comments. If you want the Agent to revise it, set Status to Needs agent review. When the draft is ready to apply, set Status to Approved. After approval, the Agent will update only the proposed destination, record Applied at, and set Status to Published.

## [Ship the full system](https://www.notion.com/help/guides/self-improving-answer-bot#ship-the-full-system)

#### Put the whole loop to work

This is where the pieces start behaving like a system. A question can become an answer, a Request, a reviewed draft, and better source material without disappearing between tools. The Q&A Log keeps the handoffs visible, and people still decide what becomes trusted knowledge.

#### 1. Turn on the full system

Turn on the Q&A Agent’s Slack trigger.

Turn on all three Self-Improving Agent triggers:

- A page is added to the Q&A Log.

- `Status` changes to `Needs agent review`.

- `Status` changes to `Approved`.

Save both agents.

Confirm both agents use the same Q&A Log and the reviewer can open every record assigned to them.

#### 2. Review proposals in the Q&A Log

When a record reaches `Needs human review`, the Self-Improving Agent mentions the assigned `Reviewer`.

The reviewer should check:

- `Question` and `Answer` for context.

- `Source Slack thread` and `Supporting sources` for evidence.

- `Proposed change` for the exact update.

- `Source to update` for the intended destination.

Then choose one path:

- Approve the proposal: If the evidence, wording, and destination are correct, set `Status = Approved`. The

  Self-Improving Agent will apply the change, record `Applied at`, and set `Status = Published`.

- Request changes: Add specific guidance to `Feedback from reviewer`, then set `Status = Needs agent review`. The agent will revise the proposal and return the record to `Needs human review`.

Reviewers should not set `Status = Published`. That status confirms the approved change was actually applied.

#### 3. If a run fails

- Open the failed run and confirm that the expected Slack message or database status triggered it.

- Check trusted-source, Q&A Log, Slack, and destination access before changing the instructions.

- Confirm the Q&A Log record contains the required evidence, `Reviewer`, `Status`, and `Source to update`.

- Fix one issue, then rerun the failed case.

#### 4. Maintain and optimize

- Keep the workflow moving: Check the Q&A Log for records stuck in `Needs agent review`, `Needs human review`, or `Approved`. Make sure every proposal has a reviewer and every approved record reaches `Published`.

- Improve run quality: Review failed, slow, or unnecessary runs. Fix trigger scope, access, or source quality before rewriting instructions.

- Control credit use: Check Insights regularly. Reduce trigger frequency, source breadth, model cost, or unnecessary actions when usage rises without improving outcomes.

- Protect reliability: Rerun the relevant test outcomes after changing instructions, tools, permissions, triggers, or sources.

- Expand gradually: Add one source, Slack channel, reviewer group, or use case at a time. Expand only when quality and cost are stable.

Share this guide

------------------------------------------------------------------------
