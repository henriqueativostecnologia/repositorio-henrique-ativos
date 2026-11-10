---
fonte: https://www.notion.com/help/guides/how-to-set-up-claude-agents-on-your-teams-notion-task-board
baixado: 2026-11-10
---

# How to set up Claude agents on your team's Notion task board

## Learn how to use Claude agents in Notion to bring coding work into your team's workflow. Keep tasks, pull requests, updates, and collaboration connected in one place.

10 min read

Vídeo: https://www.youtube.com/watch?v=CF71b7sq0lI

------------------------------------------------------------------------

## [How do External Agents work in Notion?](https://www.notion.com/help/guides/how-to-set-up-claude-agents-on-your-teams-notion-task-board#how-do-external-agents-work-in-notion)

Custom Agents are AI agents your team configures inside Notion. Each one carries its own instructions, the Notion pages and connections it can access, and the triggers that decide when it runs.

External Agents build on that foundation. Set up a tool like Claude or Cursor as a Custom Agent, and it inherits all of those settings.

For engineering and product teams, this means specs, decisions, implementation plans, and agent outputs live on the task itself. A teammate can open it, see what Claude did, and respond in the same place.

External Agents let you bring tools like Claude and Cursor into Notion as teammates, so you can @-mention them, hand off tasks, and follow every run inline.

### [What Claude agents can do in Notion](https://www.notion.com/help/guides/how-to-set-up-claude-agents-on-your-teams-notion-task-board#what-claude-agents-can-do-in-notion)

Once Claude is set up as a Custom Agent, it works the same way a teammate would in your Notion workspace, whether you're chatting with it directly, @-mentioning it in a comment, or handing it a task from the board. It can:

- **Talk and plan with you:** Answer questions about a connected codebase, scope work into a technical plan, and take direction mid-run from comments or follow-ups.

- **Work in your codebase:** Read connected GitHub repos, open pull requests with diffs and screenshots, and break larger work into smaller task cards, each with its own technical plan.

- **Work in your Notion workspace:** Create and update pages, post progress comments on the task it's working from, and generate files like PowerPoint decks or Excel spreadsheets from any page.

- **Runs within your guardrails:** It only sees the pages, databases, and connections you grant it, and its Notion credit usage is tracked in the Notion credits dashboard and each agent's `Insights` section.

## [What you'll build](https://www.notion.com/help/guides/how-to-set-up-claude-agents-on-your-teams-notion-task-board#what-you'll-build)

A shared task board where Claude picks up work when a task moves into a `Ready for Agent `column, whether that's a bug fix, a small feature, or a research question. Claude works through it, posts updates to the task, and teammates can review, redirect, or step in without leaving Notion.

Have these ready before you build

- A Notion Business or Enterprise workspace

- External Agents enabled in your workspace (a Workspace Owner can turn this on; see our [help doc](https://www.notion.com/help/use-claude-agents-in-notion#workspace-admin-controls) for setup instructions)

  - **Note:** Claude is disabled by default in HIPAA workspaces and in workspaces with Anthropic model restrictions.

- A GitHub Personal Access Token (PAT), required for the coding workflow in this guide

- Notion Credits available in your workspace (see our [help doc](https://www.notion.com/help/buy-and-track-notion-credits-for-custom-agents) to learn more about credits)

### [1. Set up your Claude agent and connect to GitHub](https://www.notion.com/help/guides/how-to-set-up-claude-agents-on-your-teams-notion-task-board#1.-set-up-your-claude-agent-and-connect-to-github)

In this step, you'll create your Claude agent and connect it to your codebase. With GitHub connected, the agent can read repositories, propose changes, and open pull requests from your task board.

1.  Open `Agents` in your sidebar and click `+ New Agent`.

2.  Select `Claude` as the model, then choose the `Coding task board `use case. To build the agent from scratch instead, start with a blank prompt.

3.  Open `Tools and access` and connect `GitHub`. When prompted, paste a Personal Access Token with `read and write` permissions for both `Contents` and `Pull Requests` (see [GitHub's documentation](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) to create one). Without those permissions, the agent can read code but can't open pull requests.

4.  Choose which repositories the agent can access.

Vídeo: https://www.youtube.com/watch?v=CF71b7sq0lI&t=31s

Helpful tips

Beyond the **Coding task board** used in this guide, here are three other starting points:

- **General task board:** Choose this if your team's work isn't centered on code, like marketing campaigns, content production, or research.

- **Codebase Q&A:** Choose this if you want the agent to answer questions about a repository without making changes, like onboarding new engineers, reviewing how something is implemented, or explaining patterns across a large codebase.

- **Create blank Claude agent:** Choose this if your workflow doesn't fit the templates above, or if you want full control over how the agent behaves.

### [2. Trigger your Claude agent on your task board](https://www.notion.com/help/guides/how-to-set-up-claude-agents-on-your-teams-notion-task-board#2.-trigger-your-claude-agent-on-your-task-board)

The `Coding task board` use case gives your team a shared task board. Each card represents a piece of work, like a bug report, a small feature, or a code change, and moves through `Backlog`, `Ready for Agent`, `In Progress`, `In Review`, and `Done`.

There are three ways to hand work off to Claude from the `Ready for Agent` column:

1.  **Move a task into the** **`Ready for Agent`** **column:** Drag a card into the column and Claude picks it up automatically. It's the most common trigger, since it fits how your team already moves work.

2.  **@-mention** **`@Claude `(or agent name) in a comment on a task:** Leave a comment on a task and tag the agent with any instructions you want it to follow. Useful when the work doesn't fit a column move, or when you want to add context before the run.

3.  **Move several cards at once:** Drag a batch of tasks into `Ready for Agent` together, and Claude works through them in parallel.

Vídeo: https://www.youtube.com/watch?v=CF71b7sq0lI&t=100s

Helpful tips

- These triggers come pre-configured when you choose the `Coding task board` use case. To customize them or add new ones, open your agent's settings (covered in step 5).

- The `Ready for Agent` column is just a status on the task board. Any database with a status or stage property works the same way. For example, trigger Claude when a PRD moves to `Ready for review` so it can flag missing detail or risky scope.

### [3. Track your agent's progress](https://www.notion.com/help/guides/how-to-set-up-claude-agents-on-your-teams-notion-task-board#3.-track-your-agent's-progress)

While Claude works, it posts updates to the task card so anyone with access can follow along. Three ways to stay in the loop:

1.  **Read Claude's comments on the task:** As the agent works, it posts plain-language updates, like which file it's editing, what it discovered, or what it plans to try next. This is enough context for most check-ins.

2.  **Open the live session for full detail:** Click `Claude is working` at the top of the task to expand the agent's transcript, including its reasoning and tool calls in real time. Useful for debugging an unexpected result.

3.  **Jump in mid-run:** Leave a comment on the task to redirect the agent, ask a clarifying question, or add context. Anyone with access can do this, so a teammate watching the run can step in without taking over.

Vídeo: https://www.youtube.com/watch?v=CF71b7sq0lI&t=160s

Helpful tips

- If a run doesn't go as expected, check the live session to see the exact steps and tool calls Claude made.

- Review Claude's task comments first. Open the full session only when you need more detail.

- If Claude gets stuck or asks a question, leave a comment with the missing context. The agent will read it and pick the work back up.

### [4. Review the output: pages, tasks, and pull requests](https://www.notion.com/help/guides/how-to-set-up-claude-agents-on-your-teams-notion-task-board#4.-review-the-output-pages-tasks-and-pull-requests)

When Claude finishes a run, results land back on the task, or for code changes, in GitHub. Claude picks the format that fits the task, so you don't have to decide upfront. Three common outputs:

1.  **Pages:** For research or summary tasks, Claude writes a new Notion page (like a summary of a repo) and links it from the task. Open it to read what the agent gathered, edit as needed, and share with your team.

2.  **Tasks:** Claude can break work into smaller task cards, each with its own technical plan. Move them through the columns like any other task, including back through `Ready for Agent` to hand implementation off to Claude.

3.  **Pull requests:** For code changes, Claude opens a pull request in the connected repo and links it from the Notion task. The PR includes the diff, a description, and (when relevant) a screenshot from the agent running the app in a browser. If your deploy platform (like Vercel) attaches a live preview, you can verify the change end to end before merging.

Vídeo: https://www.youtube.com/watch?v=CF71b7sq0lI&t=187s

Helpful tips

- Treat the first few runs as drafts. Look for places where Claude missed context, ignored an instruction, or didn't have access to something it needed.

- You can stop a run or ask Claude to keep going. Stop a run from the live session if it's heading the wrong direction. To continue a paused run, leave a comment telling it to keep going.

- Use page version history to undo Claude's edits. Open the page's history and restore an earlier version.

- When Claude creates a task with a technical plan, review it before sending the task back to `Ready for Agent`. The plan is a useful checkpoint between scoping the work and writing code.

- Keep your normal pull request review process in place. Claude can open the PR, but a teammate should still check the diff, review the preview, and approve the merge.

### [5. Improve your Claude agent as needed](https://www.notion.com/help/guides/how-to-set-up-claude-agents-on-your-teams-notion-task-board#5.-improve-your-claude-agent-as-needed)

Open your Claude agent from `Agents` in the sidebar, or the share menu on your task board. You'll land on a chat interface with the settings panel beside it.

From here, you can:

1.  **Chat with the agent directly:** Ask questions about the codebase, kick off a one-off run, or get a feel for how the agent behaves. To change how it behaves long-term, edit its instructions in the settings panel.

2.  **Edit triggers:** Adjust the rules that decide when the agent runs. The `Coding task board` use case sets up a trigger for the `Ready for Agent` status, but you can add others, like running on a comment mention or a different stage.

3.  **Edit instructions:** Rewrite the default prompt to match how your team works. Adding constraints like coding style, branch naming, or PR description format usually pays off quickly.

4.  **Manage tools and access:** Add the Notion pages and connections the agent can read or edit. Specs, design docs, or style guides are good starting points.

5.  **Switch the model or repos:** Change the AI model or expand the GitHub repos the agent can access.

Vídeo: https://www.youtube.com/watch?v=CF71b7sq0lI&t=280s

Helpful tips

- The settings panel works the same across all Custom Agents. What you learn here applies to any other agent your team builds.

- After updating instructions, run a small test task before relying on the agent for important work.

- Create multiple Claude agents when workflows need different instructions, triggers, or access. That way, instructions for one workflow don't leak into another.

### [6. Create files from your Notion workspace](https://www.notion.com/help/guides/how-to-set-up-claude-agents-on-your-teams-notion-task-board#6.-create-files-from-your-notion-workspace)

Your Claude agent isn't limited to the task board. When you need to share progress outside of it, like prepping a deck for a stakeholder review or exporting data for a partner team, the agent can generate files directly from any Notion page.

To create a file from any Notion page:

1.  Open the Notion page you want to use as the source. Project briefs, status updates, and research notes all work well.

2.  Leave a comment on the page and @-mention your Claude agent. Tell it what you want, like "Turn this into a PowerPoint deck."

3.  When the permission pop-up appears, grant the agent access to the page.

4.  The agent works in the background and embeds a link to the completed file at the bottom of the page.

Vídeo: https://www.youtube.com/watch?v=CF71b7sq0lI&t=362s

Helpful tips

- Start with a well-structured source page. Clear headings, organized sections, and bullet points help the agent create cleaner presentations and spreadsheets.

- Be specific about the output. Instructions like "one slide per section" or "group the data by quarter" get you closer to a finished result.

- Generated files live in your workspace. Anyone with access to the source page can open, review, and download them.

## [Tips for adopting Claude agents with your team](https://www.notion.com/help/guides/how-to-set-up-claude-agents-on-your-teams-notion-task-board#tips-for-adopting-claude-agents-with-your-team)

- **Start with one workflow and stay there for a few weeks:** For example, try bug triage. Claude investigates, a teammate confirms, and you expand to more workflows once Claude's PRs come back without rework or scope corrections.

- **Be explicit about what Claude owns and what stays with humans:** Write it into the agent's instructions. For example: "Claude opens PRs for bug fixes and small features; refactors of shared infrastructure are drafted as comments for a human to own."

- **Treat the first few weeks as a tuning period:** Read every PR and technical plan Claude produces, watch for patterns (missing test coverage, wrong file structure, off-style code), and update instructions when one shows up.

More resources

- Learn how [Custom Agents](https://www.notion.com/help/custom-agents) work, including triggers, instructions, resources, and agent runs.

- Explore the [Claude agent help doc](https://www.notion.com/help/use-claude-agents-in-notion) for details on configuration, admin controls, and model options.

Share this guide

------------------------------------------------------------------------
