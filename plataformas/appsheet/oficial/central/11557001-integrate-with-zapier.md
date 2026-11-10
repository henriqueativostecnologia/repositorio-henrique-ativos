---
fonte: https://support.google.com/appsheet/answer/11557001?hl=en
baixado: 2026-11-10
---

# Integrate with Zapier

[Zapier](http://www.zapier.com/) is a service that allows non-technical users to connect a triggering event from one service with one or more actions in other services. There are hundreds of services connected to Zapier and each connection between services is called a *Zap*.

Here, we'll show you how to build a Zap, set up a bot in an AppSheet app to fire an event to trigger the Zap and send an email. Instead, you could use any of the hundreds of other Zapier actions.

To integrate with Zapier:

1.  Create a Zapier account.
2.  Click **Create Zap** to create a new Zap.
3.  Replace **Name your zap** with your Zap name in the top left.
4.  Set the Trigger to **Webhook**.

    Select Trigger page
     
5.  Select **Catch Hook** in the **Trigger Event **drop-down and click **Continue**.

     
6.  Click **Copy next to the Custom Webhook URL** to the copy the URL. Then, click **Continue**.

     
7.  In the AppSheet app editor [Call a webhook from a bot](https://support.google.com/appsheet/answer/11511244) in your app.
8.  Paste the Zapier webhook URL copied in the previous step into the **URL** field of the Call a webhook task.
9.  Save your app.
10. In your AppSheet application, make a data update and save it to trigger the AppSheet webhook.
    You can do this by deploying and running your app or using the Test feature to execute the Call a webhook task.
11. In Zapier click on **Test trigger**. This tells Zapier that you've sent a trial webhook to the Zap to trigger it.

     
12. If Zapier receives the webhook from your AppSheet app successfully, it displays the message `We found a request!` followed by the JSON webhook body sent by your AppSheet webhook. For example:

     
13. Click **Continue**.
14. Choose an action for the Zap, such as an **Email by Zapier**.
15. Click **Continue**.
16. Configure the action.
    **Note**: You can use any of the fields from the updated record in AppSheet as they are all available in the payload sent from AppSheet.

     
17. Click **Continue**.
18. Click **Test & Continue** to test the Zap.
19. Click **Turn on Zap**.
20. Enable your AppSheet app to integrate it with the world via Zapier!
