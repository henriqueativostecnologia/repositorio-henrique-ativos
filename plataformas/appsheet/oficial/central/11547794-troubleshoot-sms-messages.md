---
fonte: https://support.google.com/appsheet/answer/11547794?hl=en
baixado: 2026-11-10
---

# Troubleshoot SMS messages

Resolve the most common bot SMS problems using the guidance provided in the following sections.  See also [Send an SMS message from a bot](https://support.google.com/appsheet/answer/11509435) and [Troubleshoot bots](https://support.google.com/appsheet/answer/11547467).

## Why are SMS messages only sent to the app creator?

While the app is in test mode (that is, it has not passed a [deployment check](https://support.google.com/appsheet/answer/10104389)), any SMS messages sent from a bot are delivered to the app creator only. This ensures that you do not inadvertently send email messages, SMS messages, or notifications, or post HTTP messages while debugging your bot.

## Why are SMS messages not being sent?

The SMS message may not have been sent for several reasons. In all cases the [audit history log](https://support.google.com/appsheet/answer/10104794) will contain an error message describing why the SMS message was not sent.

When you are testing your bot, be aware of the following restrictions.

- SMS messages are only sent for deployed apps. If you app is not deployed, no SMS message is sent and an appropriate error is written to the Audit History. See [Perform a deployment check](https://support.google.com/appsheet/answer/10104389).
- SMS messages are only sent if you are on a pricing plan that supports SMS. If you are not enrolled in a [pricing plan](https://solutions.appsheet.com/pricing) that supports SMS, no SMS message is sent and an appropriate error is written to the Audit History. Despite this, you can use the values that are logged in Audit History to verify that your SMS messages are working properly.

## Why are SMS messages not being delivered?

If the [audit history log](https://support.google.com/appsheet/answer/10104794) indicates that the SMS message was sent but the SMS message was not delivered, and the SMS message was sent from your personal Twilio account, do the following:

1.  Sign in to your [Twilio account](https://www.twilio.com/login).
2.  On the Home page, click **Logs** to view the Product Logs page.
3.  Under **Programmable SMS Logs**, click **Messages**.
4.  Look for the SMS message matching the values displayed in the AppSheet Audit History. This will show you whether the SMS message was delivered. If not, a Twilio error message will be displayed.

## Why are SMS messages being rejected?

If you attempt to send an SMS message to a phone number that has replied with **STOP** to one of your previous messages, no further messages will be delivered to that user. You will not be able to send SMS messages to the phone number until the subscriber identified by the phone number responds with **START**.

If you are using the AppSheet Twilio account, the **START** message should be sent to the AppSheet SMS phone number `1 425 287 5900`. (You can omit the 1 if calling from the United States.) If you are using your personal Twilio account, the **START** message should be sent to your personal Twilio SMS phone number.

To test the **START** message on an iPhone, do the following:

1.  Open the iPhone **Messages** app.
2.  Click **New Message** (pencil icon) at the top right of the screen
3.  In the **To** field enter the SMS phone number.
    For example, enter the AppSheet Twilio account phone number `1 425 287 5900`.
4.  In the body field enter **START.**
5.  Click **Send** (up arrow icon).

You should receive a response similar to the following:

    You have successfully been re-subscribed to messages from this number. Reply HELP for help. Reply STOP to unsubscribe.

## Why is the SMS \<\<\_ROW_WEB_URL\>\> not working?

Ensure that the SMS message length does not exceed the 160 character message length limit when using the AppSheet Twilio account or the 1600 character message limit when using your personal Twilio accounts. If the SMS message length exceed the limit, the SMS message will be truncated which may truncate the URL.
