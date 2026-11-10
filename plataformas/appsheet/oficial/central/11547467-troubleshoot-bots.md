---
fonte: https://support.google.com/appsheet/answer/11547467?hl=en
baixado: 2026-11-10
---

# Troubleshoot bots

Resolve the most common bot problems using the guidance provided in the following sections.

  

A subset of features, such as [sending emails](https://support.google.com/appsheet/answer/11447614) or [triggering bots with schedule events](https://support.google.com/appsheet/answer/11432969#schedule) using AppSheet automation, are not fully supported until you [purchase a subscription](https://support.google.com/appsheet/answer/15011908). That is, you can configure these features, but they won't execute as expected.

For more information, see [What can I do with a free plan?](https://support.google.com/appsheet/answer/10105400#free-plan) 

## Why isn't my bot working?

If you are having a problem with the execution of your bot, always start by [checking the audit history log](https://support.google.com/appsheet/answer/10104794).

Customize the dashboard settings and look for the audit record that is relevant to the bot. Click the **Details** icon for more information. If there was an issue with the bot execution, the reason will be provided. If you see "`Result": "Success"`, then the bot execution was successful.

**Note**: You may need to wait for up to five minutes for the audit record to appear. AppSheet groups audit records before writing them to the audit history log to reduce overhead. This can result in a delay before an audit record appears in the audit history. If you don't see an audit record, click **Search** periodically to refresh the audit history log.

If you see the `Action blocked by policy violation` error, check with your admin to determine if the AppSheet Core security setting  is turned on. See [Control access to AppSheet](https://support.google.com/a/answer/16018438).

## Can AppSheet alert me automatically if a bot fails?

You can subscribe to automatically receive an email alert each time an error is recorded in Audit History, and alert you when a bot fails to execute. To enable automatic alerts, see [Configure alerts on Audit History errors](https://support.google.com/appsheet/answer/10104794#alerts).

## Why isn't my bot running on the schedule I specified?

Always start by checking the Audit History as described in [Why isn't my bot working?](#why-bot-not-working)

Your bot will only run automatically on the specified schedule *after* your application has been deployed and you are on a paid pricing plan.

If you application is not deployed or you are not enrolled in a **paid pricing plan**, your bot will not run on the specified schedule. However, you can invoke your bot by clicking **Test** on the **Automation \> Bots** pane.

## Why isn't the bot Test button working?

If clicking **Test** on the **Automation \> Bots** pane does not invoke your bot for testing, make certain that your browser is not blocking pop-up windows.

If you are using the Google Chrome browser:

1.  Click the **Customize and control Google Chrome** button on the top right of the browser's toolbar.

2.  Select **Settings** from the drop-down.

3.  Under **Privacy and security**, expand **Site settings**.

4.  Under **Content**, expand **Pop-ups and redirects**.

5.  Add **https://www.appsheet.com:443** to the **Allow** list.

## Why is the error "Request cancelled: took too long to process" occurring?

AppSheet has a mechanism to prevent runaway applications from consuming too much time and impeding other applications that are running at the same time.

When starting an Add, Update, or Delete request, AppSheet starts a timer that runs for 2 minutes. AppSheet expects the request to finish within that 2-minute time limit. This includes the time to perform the Add, Update, of Delete as well as the time to perform any bot triggered by that Add, Update, or Delete.

AppSheet checks the time limit when:

- Computing virtual columns

- Applying security filters
  For example, when evaluating an expression that requires reading a table and applying a security filter to it.

- Fetching values from a table
  For example, if you have virtual columns that contain expressions that refer to other tables. AppSheet must read the tables, apply the security filters for the tables, and compute the virtual column values for the tables.

Time limits may be exceeded if you app has:

- A large number of virtual columns that have AppFormulas that are expensive to evaluate.

- Virtual columns that have AppFormulas that require reading other tables. When evaluating the AppFormulas, AppSheet must read the other tables, apply security for the tables, and compute the value of the virtual columns for those tables.

- Bots that are expensive to perform. Bots that have complex email body or attachment templates can be expensive. For example, if they include Start expressions that require reading other tables, applying security filters for the tables, and computing the values of the virtual columns for the tables.
