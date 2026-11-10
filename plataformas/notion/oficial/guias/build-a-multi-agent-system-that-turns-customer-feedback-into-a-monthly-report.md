---
fonte: https://www.notion.com/help/guides/build-a-multi-agent-system-that-turns-customer-feedback-into-a-monthly-report
baixado: 2026-11-10
---

# Build a multi-agent system that turns customer feedback into a monthly report

## Learn how to build and connect five Custom Agents that capture customer feedback, group similar requests, and turn them into a monthly report with supporting quotes, sources, and business impact.

- Notion AI

20 min read

Vídeo: https://www.youtube.com/watch?v=ndTwYKuWjlE

------------------------------------------------------------------------

Every week, customers tell you what they need on sales calls, in support tickets, over Slack, and sometimes in passing at the end of a demo. One conversation is easy to follow. Hundreds are not. As those interactions add up, important requests can get buried, making it harder to see which needs come up most often and where the strongest signals are coming from.

In this guide, you’ll build five Custom Agents that work together through a shared database (**Gong FR Pipeline)**. Each agent handles one step, moving feedback from a Gong call into a monthly report. The report shows which requests came up most often, who asked for them, their potential business impact, and the customer quotes behind each one.

## [What you'll build](https://www.notion.com/help/guides/build-a-multi-agent-system-that-turns-customer-feedback-into-a-monthly-report#what-you'll-build)

At a glance, here’s how the five agents work together:

- **Intake agent:** Identifies feature requests in Gong calls.

- **Extractor agent:** Pulls the exact customer quote and source for each request.

- **Matcher agent:** Checks whether the request already exists in your **Feature Request database**, then recommends updating an existing entry or creating a new one. It can also reference product plans, documentation, and PRDs stored in Notion.

- **Logger agent:** Adds the request, customer quote, and source to your **Feature Request database** based on the Matcher agent’s recommendation.

- **Reporter agent:** Creates a monthly report of the top requests, ranked by signals such as request volume, customer count, and customer spend, with supporting quotes for added context.

If your data lives outside Notion, bring it in with a Notion Worker

## [Who this is for](https://www.notion.com/help/guides/build-a-multi-agent-system-that-turns-customer-feedback-into-a-monthly-report#who-this-is-for)

Anyone across EPD (engineering, product, and design), GTM (go-to-market), or leadership who needs a clear, evidence-backed view of what customers are asking for. This includes product and engineering managers, product marketing, solutions engineering, customer success, sales, and executive teams.

## [How you’ll build each Custom Agent](https://www.notion.com/help/guides/build-a-multi-agent-system-that-turns-customer-feedback-into-a-monthly-report#how-you%E2%80%99ll-build-each-custom-agent)

You’ll create each Custom Agent using the same flow:

1.  Go to `Agents` in your sidebar, then select `+` to start a new chat.

2.  Describe what you want the agent to do. Use the example prompts in each section as a starting point.

3.  Review the draft setup. Notion will suggest the agent’s `instructions`, `triggers`, and `Tools and access`, which you’ll configure in the steps that follow.

Click +New Agent in the sidebar, then describe what you want your agent to build.

You’ll repeat this process for each Custom Agent. The sections below will guide you through the setup unique to each one. You’ll build each agent the same way: set up the databases, give it a prompt, then set the trigger and access.

## [1. Build the Intake agent](https://www.notion.com/help/guides/build-a-multi-agent-system-that-turns-customer-feedback-into-a-monthly-report#1.-build-the-intake-agent)

The Intake agent reads each new customer call and flags the ones that contain a real, customer-voiced feature request. It creates one entry per call in your shared pipeline database and passes anything worth pursuing to the Extractor agent.

Vídeo: https://www.youtube.com/watch?v=ndTwYKuWjlE&t=27s

#### 1.1 Set up the databases

The Intake agent works with two databases, one it reads from and one it writes to:

- **Gong Transcripts database** is where your customer calls live. The agent uses `Call Title` to name each pipeline entry and reads **Transcript** inside the page to determine whether the call contains a feature request. Capture transcripts with Notion AI Meeting Notes or sync data from Gong using a Notion Worker—any transcript database will work.

- **Gong FR Pipeline database** is the backbone of the workflow and the database you’ll most likely create yourself. Each entry represents one call moving through the system. **Status** is the key property because it passes the entry from one agent to the next. The Intake agent fills in the remaining details as it works.

The Gong FR Pipeline properties to start with

PromptYou are the Intake Agent, the first agent in the Gong FR Pipeline. Your job is to screen customer calls and flag the ones that contain a feature request. You run automatically whenever a new page is created in the Gong Transcripts database. Each page includes a Call Title. When you run, complete the following steps in order. First, create a pipeline card. Add exactly one new page to the Gong FR Pipeline database. Title it Processing: {Call Title}, relate it to the transcript that triggered you using the Gong Transcripts relation, and set Status to 📥 Intake, Max Loops to 2, and Last Agent to Intake. Next, open the related transcript and read it in full. Determine whether it contains an explicit, customer-voiced feature request: a clear ask for a new or changed capability, rather than praise or vague feedback. Finally, record your decision on the pipeline card only. Do not edit the Gong transcript page. Set FR Detected to true or false, Screening Confidence to a score from 1 to 10, and Screening Notes to the customer’s ask as a quote or near-quote, followed by a brief rationale. If you detect a request, move Status to ✂️ Extraction. If the transcript is missing or does not contain enough information, move Status to ⏸️ Blocked and explain why. In these prompts, “pipeline card” refers to an entry in your Gong FR Pipeline.

#### 1.2 Configure trigger and access

Now, you'll set the Intake agent to run whenever a new Gong call arrives. From then on, each new call will be screened automatically.

**Set the trigger:**

- In the agent's settings, select `Add trigger`.

- Choose `Notion` → `Page added to database`.

- Select your **Gong Transcripts** database, then `Entire database` and `Any page added`.

The remaining agents use the same trigger setup, so later sections will focus only on what changes.

**Set the access:**

- **Gong Transcripts** (`view access`): Only reads calls.

- **Gong FR Pipeline** (`full access`): Creates and updates entries there.

Test the Intake agent

------------------------------------------------------------------------

## [2. Build the Extractor agent](https://www.notion.com/help/guides/build-a-multi-agent-system-that-turns-customer-feedback-into-a-monthly-report#2.-build-the-extractor-agent)

The Extractor agent finds the exact customer quote behind each feature request and saves it for the rest of the workflow to use. It picks up where the Intake agent left off, reading the related Gong transcript and saving the verbatim quote to a new **Snippets database**.

Vídeo: https://www.youtube.com/watch?v=ndTwYKuWjlE&t=51s

#### 2.1 Set up the databases

The Extractor agent works with the two databases from Section 1, plus a new **Snippets database** it fills itself:

- **Gong Transcripts database** is the same call database from Section 1. The agent reads the full **Transcript** to find the customer’s exact words.

- **Gong FR Pipeline database** is where the Intake agent left off. The agent reads **Screening Notes**, then writes back the quote and links the **Snippet** it creates. It needs three new properties: **Verbatim Quote** *(`Text`* *property)*, **Snippet** *(`Relation`* *property)*, and

  **Error Log** *(`Text`* *property)*, which records why an entry was blocked.

- **Snippets** is the new database you need to create yourself or ask Notion AI to build it. Each entry holds one customer quote, along with the source and account behind it. The quote itself becomes the entry title, and the agent fills in the remaining details as it works.

The full Snippets database property list

PromptYou are the Extractor Agent, the second agent in the Gong FR Pipeline. Your job is to find the exact customer quote behind each feature request and save it to the Snippets database. You do not decide whether a request is valid (the Intake Agent already did that) or search for matches (the Matcher Agent does that next). You run automatically whenever a pipeline card’s Status is set to ✂️ Extraction. When you run, do the following in order. First, gather your inputs. Open the pipeline card and read its Screening Notes, then open the related call using the Gong Transcripts relation. Next, find the verbatim quote. Locate the customer’s exact words that ground the feature request. Use a true, word-for-word quote from the customer, never a paraphrase or an internal speaker’s words. Then, create a Snippet. Add a new entry to the Snippets database with the verbatim quote as its title, and fill in the Gong Transcript relation, Customer Account relation, Source Name, Source Title, and Source Date. Finally, update the pipeline card. Write the quote to the Verbatim Quote field, link the new Snippet, set Last Agent to Extractor, and move Status to 🔗 Matching. If a required input is missing (Gong Transcript relation, Screening Notes, or Customer Account relation) or you cannot find a verbatim quote, record the problem in the Error Log, set Last Agent to Extractor, move Status to ⏸️ Blocked, and stop without creating a Snippet.

#### 2.2 Configure trigger and access

You set the trigger and access the same way you did in Section 1, so here we'll focus on what's different for the Extractor.

**Set the trigger:** Instead of running when a new page is created, this agent picks up an entry mid-pipeline:

- Add a `Property updated in database` trigger to your **Gong FR Pipeline**.

- Set it to run when **Status** changes to **✂️ Extraction**.

The Intake agent applies this status when it detects a request, so the Extractor picks up the entry automatically.

**Set the access:**

- **Gong Transcripts** (`view access`): Reads calls to find the customer's exact words.

- **Gong FR Pipeline** (`full access`): Reads the screening notes and writes back the quote and status.

- **Snippets** (`full access`): Creates a Snippet entry for each quote it extracts.

Test the Extractor agent

------------------------------------------------------------------------

## [3. Build the Matcher agent](https://www.notion.com/help/guides/build-a-multi-agent-system-that-turns-customer-feedback-into-a-monthly-report#3.-build-the-matcher-agent)

The Matcher agent takes the extracted quote and decides whether it matches a feature request you're already tracking or whether it's something new.

It steps in after extraction is complete, comparing the quote against your **Feature Request database**. It can also draw on extra product context, like your knowledge base, upcoming launches, or shared docs, and you can give it web access if a lot of your product information lives online.

Vídeo: https://www.youtube.com/watch?v=ndTwYKuWjlE&t=71s

#### 3.1 Set up the databases

The Matcher agent doesn't create a new database. It reads from ones you already have and writes its recommendation back to the pipeline:

- **Feature Request database** is where the Matcher agent looks for existing feature requests. You can either build one from scratch if you don’t have one yet and populate with a few recent feature requests or use an existing database in your workspace.

- **Knowledge Base** (optional) gives the Matcher agent more context about your product and existing features. This helps it decide whether a request matches something you already support or should be treated as new. At Notion, we connect the Matcher agent to our internal knowledge base for this reason.

- **Gong FR Pipeline database** is where the Extractor agent left off. The Matcher agent reads **Verbatim Quote** and **Screening Notes**, then adds its match and recommendation. For this step, add four new properties to your Gong FR Pipeline database: **FR Match** *(`Relation`* *property)*, **Match Type** *(`Select`* *property)*, **Matching Notes** *(`Text`* *property)*, and **Recommended Action** *(`Select`* *property)*.

PromptYou are the Matcher Agent, the third agent in the Gong FR Pipeline. Your job is to decide whether each feature request already exists in your Feature Request database, has already shipped as a GA feature, or is committed to an upcoming launch. You do not extract quotes (the Extractor Agent already did that) or log the request (the Logger Agent does that next). You run automatically whenever a pipeline card's Status is set to 🔗 Matching. When you run, do the following in order. First, gather your inputs. Open the pipeline card and read its Title, Verbatim Quote, and Screening Notes. Do not open the full transcript, since everything you need is already on the card. Next, search for a match. Look through your Feature Request database for entries that match the request, and classify each as an Exact Match, Partial Match, or No Match. Draw on your Knowledge Base and any upcoming launch databases to tell whether the capability already exists as GA or is committed to launch. Then, decide on a recommendation. If a match is completed or already live, recommend Reject (Already Exists/Launched). If it maps to an open request, recommend Add to Existing FR. If nothing matches, recommend Create New FR. Finally, update the pipeline card. Fill in the FR Match relation, Match Type, Matching Notes, and Recommended Action, set Last Agent to Matcher, and move Status to 📝 Logging if you are adding to an existing request or 🚦 Review: Triage for any other outcome. If a required input is missing, record the problem in the Error Log, set Last Agent to Matcher, and move Status to ⏸️ Blocked.

#### 3.2 Configure trigger and access

**Set the trigger:** The Matcher joins the workflow after extraction is complete, so it runs when an entry reaches the right status.

- Add a `Property updated in database` trigger to your **Gong FR Pipeline**.

- Set it to run when **Status** changes to **🔗 Matching**.

The Extractor applies this status after saving the verbatim quote, which hands the entry to the Matcher automatically.

**Set the access:** The Matcher needs to read the customer feedback, compare it with existing requests, and write its recommendation back to the pipeline.

- **Gong FR Pipeline** (`full access`): Reads the quote and screening notes, then adds the match and recommended action.

- **Feature Request database** (`view access`): Searches the requests you’re already tracking for a match.

- **Knowledge Base** (`view access`, optional): Provides extra product context to help distinguish an existing request from a new one.

Test the Matcher agent

------------------------------------------------------------------------

## [4. Build the Logger agent](https://www.notion.com/help/guides/build-a-multi-agent-system-that-turns-customer-feedback-into-a-monthly-report#4.-build-the-logger-agent)

The Logger agent takes the Matcher’s recommendation and files the request in your **Feature Request database**. It either updates an existing request or creates a new one, attaching the customer quote, source, and relevant account (optional).

Matches to an existing request reach the Logger automatically. New requests first pass through **🚦 Review: Triage** so a person can confirm them, then move to **📝 Logging** once approved.

Vídeo: https://www.youtube.com/watch?v=ndTwYKuWjlE&t=88s

#### 4.1 Set up the databases

Like the Matcher, the Logger works with databases already in the workflow. It reads the recommendation from the pipeline, then files the request in your existing **Feature Request database**.

- **Gong FR Pipeline database** is where the Matcher agent left off. The Logger agent reads **Recommended Action**, **Verbatim Quote**, and the linked sources, then moves the entry to **✅ Logged**. For this step, add one new Number property to the Gong FR Pipeline database: **Logging Confidence**, a score from 1 to 10 that flags where human review is most useful.

- **Feature Request database** is where the Logger agent either updates an existing request or creates a new one, with the quote and sources attached.

- **Customer Accounts** (optional) is a CRM database built in your Notion workspace or synced from your external CRM. Connecting it allows the Logger agent to link each request to the right account and include customer spend. At Notion, we use a Salesforce Sync Worker database called **Customer Accounts** for this.

PromptYou are the Logger Agent, the fourth agent in the Gong FR Pipeline. Your job is to file each request into your Feature Request database using everything the previous agents assembled on the pipeline card. You do not extract quotes (the Extractor Agent did that) or decide on a match (the Matcher Agent did that). You run automatically whenever a pipeline card's Status is set to 📝 Logging. When you run, do the following in order. First, gather your inputs. Open the pipeline card and read its Recommended Action, Verbatim Quote, and FR Match relation, along with the linked Snippet and transcript. Next, file the request. If the recommendation is Add to Existing FR, tag the customer account on the matched request and link the related transcript and Snippet. If it is Create New FR, create a fresh entry with the account tagged, the verbatim quote preserved, and every supporting source linked. Then, score your confidence. Set a Logging Confidence from 1 to 10 so your team can prioritize human review where it is needed most. Finally, close out the card. Set Last Agent to Logger and move Status to ✅ Logged. If a required input is missing, record the problem in the Error Log, set Last Agent to Logger, and move Status to ⏸️ Blocked.

#### 4.2 Configure trigger and access

**Set the trigger:** The Logger joins the workflow after the Matcher recommends filing a request.

- Add a `Property updated in database` trigger to your **Gong FR Pipeline**.

- Set it to run when **Status** changes to **📝 Logging**.

The Matcher applies this status when a request is ready to be added to your **Feature Request database**.

**Set the access:** The Logger needs to read the pipeline entry, connect the supporting sources, and file the request.

- **Gong FR Pipeline** (`full access`): Reads the recommendation, quote, and linked sources, then marks the entry complete.

- **Feature Request database** (`full access`): Updates an existing request or creates a new one.

- **Gong Transcripts** (`view access`): Links the source call to the request.

- **Snippets** (`view access`): Links the saved customer quote to the request.

- **Customer Accounts** (`view access`, optional): Connects the request to the right account and includes customer spend. This is typically a CRM database built in Notion or synced from your external CRM.

Test the Logger agent

------------------------------------------------------------------------

## [5. Build the Reporter agent](https://www.notion.com/help/guides/build-a-multi-agent-system-that-turns-customer-feedback-into-a-monthly-report#5.-build-the-reporter-agent)

Once the other agents have logged requests throughout the month, the Reporter brings them together in a single, data-backed report. It highlights top requests, supported by real customer quotes, cited sources, and their potential business impact.

In this workflow, the Reporter runs on the first day of every month, so you get a clear view of what customers are asking for without reviewing hours of calls.

Vídeo: https://www.youtube.com/watch?v=ndTwYKuWjlE&t=104s

#### 5.1 Set up the databases

The Reporter reads from the databases the earlier agents filled in and writes the final output to one new database:

- **Feature Request database** supplies the logged requests the agent ranks.

- **Snippets database** supplies the customer quotes and sources behind each request.

- **Customer Accounts** (optional) adds business context from your CRM, such as customer spend.

- **Monthly Report database** stores the finished report and is the database you need to create. Start with a simple template that includes rank, request volume, and ARR, followed by a breakdown of each request.

PromptYou are the Reporter Agent, the fifth and final agent in the Gong FR Pipeline. Your job is to turn a month of logged requests into a single “GTM Top 10” report. You do not log or match requests (the earlier agents did that); you rank what is already in the Feature Request database and present it. You run automatically on the first of every month. When you run, do the following in order. First, gather your inputs. Read the Feature Request database for requests logged over the past month, along with their linked Snippets and customer accounts. Next, rank the top requests. Order them by signal strength, such as request volume, number of distinct customers, and customer spend, then keep the top 10. Then, build each entry. For every request, show its rank, how often it came up, the accounts behind it and their spend, and a supporting customer quote with its source. Finally, write the report. Create a new entry in your Monthly Report\* database using the same structure, headings, callouts, toggles, and tables as your report template. \*Be specific about the report format in your prompt. Tell the agent how many requests to include, how to rank them, and what each entry should show, since that shapes the final deliverable.

#### 5.2 Configure trigger and access

**Set the trigger:** Unlike the other agents, the Reporter runs on a schedule rather than waiting for a pipeline status.

- Add a `scheduled` trigger.

- Set it to repeat `Monthly` on the `1st`.

**Set the access:** The Reporter needs to read the logged requests and their supporting context, then create the finished report.

- **Feature Request database** (`view access`): Reads and ranks your logged requests.

- **Snippets** (`view access`): Pulls in the customer quotes and their sources.

- **Customer Accounts** (`view access`, optional): Adds business context from your CRM, such as customer spend.

- **Monthly Report** (`full access`): Creates and writes the final report.

Test the Reporter agent

This multi-agent system you built gives customer feedback somewhere to go, carrying each useful comment from its original transcript through a shared pipeline while keeping the request, the customer’s words, its source, and the business context intact.

From here, make the workflow your own by connecting the feedback sources your team relies on, tracking the signals you trust, and shaping the final report around how your team makes product decisions.

Want to build this for your team?

Connect with our team to explore how Custom Agents can support your workflows and help you turn this example into a system that works for your organization.

[Contact sales](/contact-sales)

Share this guide

------------------------------------------------------------------------
