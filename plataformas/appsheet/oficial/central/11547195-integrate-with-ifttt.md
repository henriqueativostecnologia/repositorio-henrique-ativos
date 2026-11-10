---
fonte: https://support.google.com/appsheet/answer/11547195?hl=en
baixado: 2026-11-10
---

# Integrate with IFTTT

[IFTTT](https://www.ifttt.com/) ([www.ifttt.com](https://www.ifttt.com/)) is a service that lets you connect events with actions via simple `If-Then` rules. Each such rule is called a *recipe*.

You can create a bot in your AppSheet app that will trigger the `If` event of an IFTTT recipe. The event can also carry some data from your app that can be passed along to some other service via the IFTTT recipe.

Here is a simple [IFTTT recipe](https://ifttt.com/recipes/426317-integrate-your-appsheet-app) to show this integration. The recipe receives a message from an AppSheet bot, and then sends it by email to the owner of the IFTTT account.

To set up an integration with IFTTT:

1.  Create and sign in to your IFTTT account.

2.  Open the following URL: [https://ifttt.com/recipes/426317-integrate-your-appsheet-app](https://ifttt.com/recipes/426317-integrate-your-appsheet-app)
    This will copy the recipe into your account.

3.  Add the Maker source to your account. Provide an event name (for example, `MyTrialEvent`). Click **Add** to add the recipe to your account. Go to [https://ifttt.com/maker](https://ifttt.com/maker) to obtain your key. It will be similar to the following: `dMJSI4dCVowUxpVFrqjG8d`

4.  [Call a webhook from a bot](https://support.google.com/appsheet/answer/11511244) in your AppSheet app. Configure the webhook action as follows.

    - Set the **URL**: **`https://maker.ifttt.com/trigger/{eventName}/with/key/{IFTTTkey}`** For example, `https://maker.ifttt.com/trigger/MyTrialEvent/with/key/dMJSI4dCVowUxpVFrqjG8d`

    - Leave the **HTTP Headers** blank.

    - In the **Body** field, enter **`{"value1":"hello", "value2":"there", "value3":"<_APPNAME>"}`**. You can use any data from the updated record and the rest of the app data using AppSheet expressions.

5.  Run the app [deployment check](https://support.google.com/appsheet/answer/10104389) and mark the app as **Deployable**, otherwise the bot won't actually execute the actions.

6.  Make an update to the app so that the bot fires. Verify from the [audit history log](https://support.google.com/appsheet/answer/10104794) that the bot succeeded. Go to your IFTTT recipe page and verify from the recipe log that the recipe was triggered. A short while later, your IFTTT recipe will send an email to your account.
