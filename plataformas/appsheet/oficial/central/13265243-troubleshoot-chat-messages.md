---
fonte: https://support.google.com/appsheet/answer/13265243?hl=en
baixado: 2026-11-10
---

# Troubleshoot Chat messages

The following sections provide tips for troubleshooting Chat messages.See also [Troubleshoot Chat apps](https://support.google.com/appsheet/answer/12992541).

 

------------------------------------------------------------------------

 [Expand all](#expand)** ** \|** **[Collapse all](https://support.google.com/appsheet/answer/13265243)

#### Error: There was a problem fetching Chat spaces for the Google Cloud project ID

To support asynchronous interactions with your Chat app and enable AppSheet to fetch Chat spaces when [sending a Chat message from an automation](https://support.google.com/appsheet/answer/12981549), you need to [grant IAM access to run automations](https://support.google.com/appsheet/answer/12849362#set-iam-policy-for-async-messages). Otherwise, no Chat spaces will be available for selection when configuring the task and the following error message displays in the app editor:

`There was a problem fetching Chat spaces for the GCP project ID`

#### Why do I see "Open in app" message in Chat app?

If a feature that is not supported for Chat apps with AppSheet is used in your app, app users are prompted to open the web version of the app to view or edit the feature.

 For example, to edit a `Color` type field, app users need to open the web version of the app:

Color data type field used in Chat app; prompted to open in app to edit the field

In addition, a warning message similar to the following displays:

`This view contains certain column types which cannot be edited in Google Chat`

#### Slash command returns error

 When you add slash commands for Chat apps in the Chat API, make sure you enable the **Opens a dialog** option.

Chat app inventory log slash command

#### Why is my Chat app not sending messages to a Google Chat space?

If your Chat app is not sending messages to a Chat space:

- Check the [automation monitor](https://support.google.com/appsheet/answer/11447502) for any warnings or errors.
- Check with your organization admin to confirm that the app is allowlisted in the Chat App or Marketplace settings. See [Allow users to install Chat apps](https://support.google.com/a/answer/7651360).
