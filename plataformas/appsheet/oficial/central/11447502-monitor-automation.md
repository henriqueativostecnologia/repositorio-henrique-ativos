---
fonte: https://support.google.com/appsheet/answer/11447502?hl=en
baixado: 2026-11-10
---

# Monitor automation

Use AppSheet **automation monitor** to monitor automation in your apps and keep a track of the bot executions that were successful, encountered errors, and are still pending, as described in the following sections:

- [Get started](#get-started)
- [Access the automation monitor](#access-automation-monitor)
- [Monitor app metrics](#monitor-app-metrics)
- [Monitor bot execution](#monitor-bot-execution)
- [Monitor document parsing](#monitor-document-parsing)
- [Set the time range for monitoring](#set-time-range)

## Get started

Watch the following video to learn how to monitor automation.

Video: https://www.youtube.com/watch?v=3jwAaG2Hht8

## ****Access the automation monitor

To access the automation monitor:

1.  Open the app in the app editor.

2.  Perform one the of the following steps:

    - Click **Automation \> Bots,** expand the bot, and click **Monitor** in the bot header.

    - Select **Manage \> Monitor**, expand the **Automation Monitor** section, and click **Launch the automation monitor**.

Use the AppSheet automation monitor to monitor the following information for your apps:

- [App metrics](#monitor-app-metrics)
- [Bot execution](#monitor-bot-execution)
- [Document parsing](#monitor-document-parsing)

## ****Monitor app metrics

To monitor app metrics:

1.  [Access the automation monitor](#access-automation-monitor).
2.  [Set the time range](#set-time-range).
3.  Click **Metrics** in the bottom navigation bar.
4.  Click an app to inspect in the **Apps** column.

The **Metrics** page displays high-level aggregated and daily metrics for bots, including status and average time to completion.

 

Monitor app execution

## ****Monitor bot execution

To monitor bot execution:

1.  [Access the automation monitor](#access-automation-monitor).
2.  [Set the time range](#set-time-range).
3.  Click **Runs** in the bottom navigation bar.
4.  Click an app to inspect in the **Apps** column.

The **Runs** page displays bot execution details, including bot instances, events, processes, and step details.

Monitor bot execution

## ****Monitor document parsing

To monitor document parsing:

1.  [Access the automation monitor](#access-automation-monitor).
2.  [Set the time range](#set-time-range).
3.  Click **Document Parses**.
4.  Click an app to inspect in the **Apps** column.

The **Document Parses** page displays a summary of all document parsing for the selected app.

Monitor document parsing

The status value indicates whether the document parsing succeeded or failed, and might also indicate the level of confidence, as summarized below.

 

Successful and human-reviewed document parses will appear in your document-based app tables. All other status values indicate that there are issues that need to be resolved before they appear in your app tables.

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Status**                                                                    | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| `DISCARD`                                                                     | Document parse has been manually discarded. See [Discard the results of a     |
|                                                                               | document parse](#discard-results).                                            |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| `EXTRACTION_ERROR`                                                            | Content was not extracted. Typically caused by an unsupported document type   |
|                                                                               | or file format.                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| `HUMAN_REVIEWED`                                                              | Content has been manually inspected, updated, and marked as complete. See     |
|                                                                               | [Resolve issues with document parsing](#resolve-issues).                      |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| `POOR_QUALITY`                                                                | Indicates one or both of the following:                                       |
|                                                                               |                                                                               |
|                                                                               | -   Content was extracted but there is low confidence with the accuracy of    |
|                                                                               |     the information. See [How AppSheet measures extraction                    |
|                                                                               |     confidence](https:                                                        |
|                                                                               | //support.google.com/appsheet/answer/11447806#measure-extraction-confidence). |
|                                                                               |                                                                               |
|                                                                               | -   One or more critical fields are not available (for example the Total      |
|                                                                               |     Amount on an invoice).                                                    |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| `QUOTA_EXCEEDED`                                                              | Quota exceeded for the current cycle. The document parsing will be completed  |
|                                                                               | when quota is available.                                                      |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| `SUCCESS`                                                                     | Extraction was successful. There is strong confidence with the accuracy of    |
|                                                                               | the information. See [How AppSheet measures extraction                        |
|                                                                               | confidence](https:                                                            |
|                                                                               | //support.google.com/appsheet/answer/11447806#measure-extraction-confidence). |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

### Resolve issues with a document parse

To resolve issues with a document parse:

1.  On the **Document Parses** page, click the **edit** icon associated with the document parse. The details of the document parse are displayed.

    The extraction error appears in the left pane, in **bold**. For example:
    `Expected field missing: Address was not extracted.`

2.  Edit the parsed fields to correct the error.

3.  Click the **checkmark** icon in the top banner.

After being marked complete, the document parse appears in the app tables and its status is set to `HUMAN_REVIEWED`.

### Discard the results of a document parse

To discard the results of a document parse:

1.  On the **Document Parses** page, click the **edit** icon associated with the document parse.
2.  Click the **delete** icon in the top banner.

**Note**: If necessary, you can recover a discarded document parse by changing the status of the entry in Google Sheets from `DISCARD` to `HUMAN_REVIEWED`.

## ****Set the time range for monitoring

To set the time range for monitoring:

1.  Expand the **AppSheet Monitoring** menu in the top-left of the automation monitor.

    AppSheet Monitoring menu location

2.  Select **Settings**.

3.  Set the **Monitoring Time Range** to the desired value.
    If you select **Custom**, set the start and end values using the calendar selector.

    Monitor time range using custom values

4.  Select the app in the **App to Monitor** drop-down list.

5.  Click **Save**.
