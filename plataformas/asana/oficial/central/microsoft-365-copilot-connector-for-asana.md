---
fonte: https://help.asana.com/s/article/microsoft-365-copilot-connector-for-asana?language=en_US
baixado: 2026-11-10
---

# Microsoft 365 Copilot connector for Asana

The Microsoft 365 Copilot connector for Asana helps Copilot use your Asana work context in Copilot agent chat and Microsoft apps such as Teams or Outlook. This article explains how the connector gets Asana data, who can see that data afterward, and what the connector can and can't do. It also walks you through the Asana side of the setup.

> Microsoft builds and maintains the connector. To troubleshoot indexing, sync schedules, Copilot answers, identity mapping, or connector settings, contact Microsoft support through the Microsoft 365 admin center. Asana Support can help you create and configure the OAuth app in the Asana developer console that the connector requires.

## How the connector works

A single Asana user authorizes the connector once, during setup. After that, Microsoft's service uses that one person's OAuth credentials to crawl Asana on a set schedule. By default, it runs a quick update about every 15 minutes and a full refresh once a day. The data it reads is copied into Microsoft's search index, and Copilot answers questions from that index.

This design has two important consequences.

### Copilot only knows about work the authorizing user can see

The connector sees Asana exactly as the authorizing user does. If a task, project, or team is private and that user isn't a member, the connector never reads it, and it never shows up in Copilot. Work that other people in your organization can see, but the authorizing user can't, will be missing from Copilot. This is the most common reason Copilot claims it "can't find" an Asana task.

### Anything the connector reads may be visible to everyone it's rolled out to

Once data is in Microsoft's index, Asana's permissions no longer control who sees it. Visibility in Copilot is decided on the Microsoft side, by the connector's rollout and access settings, not by each person's Asana permissions. In practice, a task that only the authorizing user can open in Asana may be surfaced through Copilot to colleagues who have no access to it in Asana.

Review Microsoft's access permissions and identity mapping settings carefully. Confirm the behavior with Microsoft before you roll the connector out widely.

## Authentication best practices

The account used to authorize the connector decides what data enters Copilot and, potentially, who can see it. Keep three risks in mind.

A broad account means broad exposure. If an Asana admin or another user with wide access authorizes the connector, everything that person can see may be indexed. That can include sensitive projects, such as those for HR, finance, or leadership planning, and that content could then reach everyone who has the connector.

A narrow account means gaps. If the account can see very little, Copilot will miss a lot of your organization's work.

The connector depends on one account. The OAuth app and its authorization belong to an individual Asana user. If that person leaves, is deprovisioned, loses access to projects, or revokes the app, syncing stops or Copilot quietly loses content.

We recommend using a dedicated Asana account that belongs only to the teams and projects you're comfortable sharing with everyone who will have the connector. The same person should create the OAuth app and authorize the connector, as Microsoft's guide requires.

## The connector reads data but doesn't act in Asana

The connector is a one-way, read-only feed for search and summaries. Copilot can use the indexed data to answer questions, summarize work, and prepare briefings. For example, Copilot can answer "What's overdue in the Website Launch project?" The connector can't create, assign, update, complete, or comment on tasks, or change anything else in Asana.

Keep in mind that Copilot works from a copy of your data. Changes, including completed or deleted tasks and permission changes, may not appear until the next sync.

## Set up the Asana side

Sign in to Asana as the account that will authorize the connector, then complete these steps.

1.  Open the Asana developer console at [https://app.asana.com/0/my-apps](https://app.asana.com/0/my-apps).
2.  Select **Create new app**. When asked for an app type, choose a standard API app. Give the app a recognizable name, for example, "Copilot Connector."
3.  In the sidebar, select **OAuth**, and add the redirect URL for your Microsoft environment. For Microsoft 365 Enterprise, use [https://gcs.office.com/v1.0/admin/oauth/callback](https://gcs.office.com/v1.0/admin/oauth/callback). For Microsoft 365 Government, use [https://gcsgcc.office.com/v1.0/admin/oauth/callback](https://gcsgcc.office.com/v1.0/admin/oauth/callback).
4.  Still under **OAuth**, find **Permission scopes** and turn on **Full permissions**. Microsoft's connector expects this setting. Full permissions gives the app access to all API endpoints rather than a limited set of scopes.
5.  In the sidebar, select **Manage distribution**. Choose **Specific workspace**, select **+ Add workspace**, and add the workspace or organization you want to index. Without a distribution setting, nobody can authorize the app.
6.  On the **OAuth** tab, copy the **Client ID** and **Client secret**. Treat the client secret like a password.
7.  If your organization requires admin approval for third-party apps, ask your Asana admin to approve the app in the admin console.

Once you finish these steps, the Asana part of the setup is complete. The rest of the setup happens in the Microsoft 365 admin center. There, you enter the client ID and secret, authorize the connection, and set the display name, rollout audience, access permissions, and identity mapping. Follow Microsoft's guide, [Deploy the Asana connector](https://learn.microsoft.com/en-us/microsoft-365/copilot/connectors/asana-deployment), for these steps.

When Microsoft asks you to select **Authorize**, sign in to Asana with the account you want to use to crawl your Asana workspace. Review the authentication best practices above before you choose that account.

## Consider the Microsoft Teams + Asana app

If you want to work with Asana from inside Microsoft 365, and you want each person to see only what they're allowed to access in Asana, consider the first-party [Microsoft Teams + Asana app](https://asana.com/apps/microsoft).

The main difference is authorization. Each person connects the app with their own Asana login, so the app always acts on their behalf and follows their own Asana permissions.

With the app, people can turn Teams conversations and meetings into tasks, create and assign tasks during meetings, and search and share Asana tasks and projects. Shared links expand with details. People can also get Asana notifications in Teams, and Asana automations can send messages to Teams channels.

To get started, check that your Teams admin allows Asana app usage in your organization. Then, in Teams, open **Apps**, search for Asana, select **Add**, and sign in to your Asana account when the bot asks. For details, see the [Microsoft Teams and Asana integration article](https://help.asana.com/s/article/microsoft-teams-and-asana-integration).
