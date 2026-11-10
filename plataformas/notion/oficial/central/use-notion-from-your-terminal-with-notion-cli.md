---
fonte: https://www.notion.com/help/use-notion-from-your-terminal-with-notion-cli
baixado: 2026-11-10
---

# Use Notion from your terminal with Notion CLI (beta)

In this help doc

## Learn the basics of using Notion from the command line, including how to get set up and common fixes.

[Jump to FAQs](https://www.notion.com/help/use-notion-from-your-terminal-with-notion-cli#faq)

------------------------------------------------------------------------

Notion CLI `ntn` is a tool that lets developers and AI coding agents work with Notion by typing commands in a terminal. You can read and write Notion content, and (if you have access) manage Workers from the command line.

You can also view Workers and read logs in Notion with [Developer Mode](https://www.notion.com/help/turn-on-developer-mode-to-use-developer-tools-in-notion). Use the CLI when you need to deploy Workers or change their code or setup.

This article is a high-level overview. For technical setup, see the [developer documentation](https://developers.notion.com/guides/get-started/overview).

Vídeo: https://www.youtube.com/watch?v=k-6ldiWIDsg

## [What to know before you start](https://www.notion.com/help/use-notion-from-your-terminal-with-notion-cli#what-to-know-before-you-start)

- The CLI is designed for developers and technical builders.

- The CLI is available on all plans. However, deploying and managing [Notion Workers](https://www.notion.com/help/run-custom-code-with-workers) requires a Business or Enterprise plan.

- Some developer platform features you use through the CLI may require specific plans or admin enablement.

- If something looks off, first make sure you are on the latest version of the CLI.

- If you only need to view a Worker, read logs, turn it off, or delete it, you can do that in Notion after you turn on [Developer Mode](https://www.notion.com/help/turn-on-developer-mode-to-use-developer-tools-in-notion).

## [Install the CLI](https://www.notion.com/help/use-notion-from-your-terminal-with-notion-cli#install-the-cli)

The CLI works on Mac, Linux, and Windows. On any of these, you can install it with `npm install -g ntn`.

For more info about installation, see the [developer documentation](https://developers.notion.com/cli/get-started/installation).

## [If something isn’t working](https://www.notion.com/help/use-notion-from-your-terminal-with-notion-cli#if-something-isn%E2%80%99t-working)

Start with these quick checks:

1.  **Update the CLI, then try again.** The CLI is designed to stay current, and older versions can behave differently.

2.  **Confirm you’re signed into the right Notion account.** If you have multiple accounts or workspaces, sign out and back in.

3.  **Check your access in Notion first.** If you can’t open the page or database in Notion, the CLI won’t be able to read or change it either.

4.  **If you’re trying to use Workers commands, confirm Workers are enabled.** Workers access can depend on your plan and whether a workspace owner has turned it on.

5.  **Still stuck?** Use the developer docs for the exact error and fix, since the steps can be different for each command.

------------------------------------------------------------------------

## FAQs

Do I need the CLI to use Notion?

No. The CLI is optional and meant for developer workflows.

Does the CLI work on mobile?

No. It runs in a terminal on desktop.

Where can I find the full command list?

Find the full command list in the [developer documentation](https://developers.notion.com/guides/get-started/overview)[.](https://developers.notion.com/guides/get-started/overview)

Does the CLI work on Windows?

Yes. The CLI works the same on Windows, Mac, and Linux. Workers you create on one platform show up the same everywhere.

Can I manage Workers in Notion instead of the CLI?

Partly. You can view Workers, read logs, turn Workers off, and delete Workers in Notion with [Developer Mode](https://www.notion.com/help/turn-on-developer-mode-to-use-developer-tools-in-notion). Use the CLI to deploy Workers or change their code or setup.

## Contents

- [What to know before you start](#what-to-know-before-you-start)
- [Install the CLI](#install-the-cli)
- [If something isn’t working](#if-something-isn’t-working)
