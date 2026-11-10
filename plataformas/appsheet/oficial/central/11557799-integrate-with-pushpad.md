---
fonte: https://support.google.com/appsheet/answer/11557799?hl=en
baixado: 2026-11-10
---

# Integrate with Pushpad

[Pushpad](http://pushpad.xyz/) is a service that allows you to send push notifications to your web site or web app. You can create a bot in your AppSheet app that will send a Pushpad notification.

**Note**: If instead you'd like to send push notifications to your users on mobile devices, see [Send notifications from a bot](https://support.google.com/appsheet/answer/11513089)[.](https://help.appsheet.com/behavior/workflow-introduction/sending-push-notifications-from-a-workflow-rule)

To set up an integration with Pushpad:

1.  Create a Pushpad account.
    You will receive a Pushpad `auth_token` and `project_id`.

2.  [Call a webhook from a bot](https://support.google.com/appsheet/answer/11511244) in your AppSheet app. Configure the webhook action as follows:

    - Set the **URL** to:
      `https://pushpad.xyz/projects/<project_id>/notifications`
      Where `<project_id>` is the `project_id` issued to you by Pushpad.

    - In the **Body** field, enter:
      **`{ "notification": { "body": "Hello World", "title": "My Title" } }`**
      Customize the body to include your own text. You can include [variables](https://support.google.com/appsheet/answer/11539253) and [expressions](https://support.google.com/appsheet/answer/10104642) that use data from the updated record.

    - In the **Headers** field, enter:
      `Authorization: "Token token=""<auth_token>"""`
      Where `<auth_token>` specifies the `auth_token` value obtained from Pushpad.

3.  Run the app [deployment check](https://support.google.com/appsheet/answer/10104389) and mark the app as **Deployable**, otherwise the bot won't actually execute the actions.

4.  Make an update to the app so that the bot fires. Verify from the [audit history log](https://support.google.com/appsheet/answer/10104794) that the bot succeeded. A short while later, Pushpad will send a notification.
