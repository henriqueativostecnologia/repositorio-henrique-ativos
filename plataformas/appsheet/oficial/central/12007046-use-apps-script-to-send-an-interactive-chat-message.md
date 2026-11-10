---
fonte: https://support.google.com/appsheet/answer/12007046?hl=en
baixado: 2026-11-10
---

# Use Apps Script to send an interactive chat message

To use Apps Script to send an interactive chat message:

1.  [Create a webhook for a Google Chat space](#create-webhook)
2.  [Create an Apps Script project with a function to send data to the webhook](#create-apps-script-project)
3.  [Call Apps Script function from AppSheet Automation](#call-function)

## ****1. Create a webhook for a Google Chat space

To send rich messages to Chat, you can use the built-in [webhook functionality](https://developers.google.com/chat/how-tos/webhooks) to allow a Chat space to receive formatted data and post the message as a bot. Then, you can use Apps Script to call that webhook with data passed in from your AppSheet app.

First, we need to create the webhook our script will use. Go to [Chat](https://chat.google.com/), create a new space, and click **Manage webhooks**.

Select Manage webhooks in Chat

Step through the short wizard. At the end you are provided with a URL. Copy it to your clipboard. You now have a bot that can post to a Chat space. See the relevant [Chat documentation](https://developers.google.com/chat/how-tos/webhooks#define_an_incoming_webhook) for more details.

## ****2. Create an Apps Script project to send data to the webhook

### Quick start

Rather than create the Apps Script project manually, you can copy the sample project as a starting point for your own Apps Script project.

1.  Open the sample project:

    [Open Sample Project](https://script.google.com/home/projects/1PWw8pRKEBDUD23r2V4QyQZzMxQiZOdTioYNQme03CoY9Zhihu0uDPn08)
     
2.  Copy the project.

    Copy the project

### Create the Apps Script project

To create the Apps Script project:

1.  Go to the [Apps Script homepage](https://script.google.com/).
2.  Click **New Project**.

The Apps Script editor where you can write your code. Apps Script is written in Javascript with special Workspace API extensions. 

If you’ve never coded before or need a refresher, see the [Apps Script overview](https://developers.google.com/apps-script/overview) which has resources to help you learn more about Apps Script.

### Create a function to call the Chat webhook API

The Chat API is quite simple but also extensible if you want to create more complicated messages.

First, let's try with just a simple text message:

    const GOOGLE_CHAT_WEBHOOK_LINK = "https://chat.googleapis.com/v1/spaces/...";
    function sendMessage() {
        const payload = JSON.stringify({ text: "Hello World" });
        const options = {
            method: 'POST',
            contentType: 'application/json',
            payload: payload,
        };
        UrlFetchApp.fetch(GOOGLE_CHAT_WEBHOOK_LINK, options);
    }

For more information about `UrlFetchApp.fetch` method, see [Class UrlFetchApp](https://developers.google.com/apps-script/reference/url-fetch/url-fetch-app).

You can test executing the function from Apps Script by clicking **Debug**:

Apps Script project Debug button

The first time you do this, you'll need to authorize scopes the script needs to use the `UrlFetchApp` permission. .

If successful, you'll see a new message appear in your Chat space:

Hello World message displayed in the Chat space

### Add an argument

Now modify the function to accept an argument. Note that we are defaulting to `Sample text` if no argument is provided to simplify testing.

    function sendMessage(message) {
       const text = message instanceof String ? message : "Sample text";
       const payload = JSON.stringify({ text: text });
       ...
    }

 

At this point, you could send custom text to a chat room from AppSheet after it's hooked up to a task in an automation.

### Add card messages

If you want richer messages, you can extend the interface to include attachments and links.

For example, if you declare your payload as shown below it will result in a richer message with a link to open an order:

    const payload = JSON.stringify({
            "cards": [{
                "header": {
                    "title": "Order received",
                    "imageUrl": "https://www.gstatic.com/images/icons/material/system/2x/shopping_bag_gm_blue_48dp.png",
                    "imageStyle": "IMAGE"
                },
                "sections": [{
                    "widgets": [{
                            "textParagraph": {
                                "text": "A new order was placed on: " + new Date().toDateString(),
                            }
                        },
                        {
                            "buttons": [{
                                "textButton": {
                                    "text": "OPEN ORDER",
                                    "onClick": {
                                        "openLink": {
                                            "url": orderUrl
                                        }
                                    }
                                }
                            }]
                        },
                    ]
                }]
            }]
        });

To create more complicated messages for your automations, see the full [Cards API](https://developers.google.com/chat/api/reference/rest/v1/cards) as well as additional sample messages described in [Card messages](https://developers.google.com/chat/api/guides/message-formats/cards).

## ****3. Call Apps Script function from AppSheet Automation

After you have it set up, you can follow the instructions [Call Apps Script from an automation](https://support.google.com/appsheet/answer/11997142) to set up the task and automation bot inside AppSheet.

------------------------------------------------------------------------

We hope this helps you to get started with Apps Script tasks! See the [sample project](https://script.google.com/home/projects/1PWw8pRKEBDUD23r2V4QyQZzMxQiZOdTioYNQme03CoY9Zhihu0uDPn08) for the code covered in this guide.

## See also

- [Call Apps Script from an Automation](https://support.google.com/appsheet/answer/11997142)
- [Use the AppSheet Apps Script Examples Project](https://support.google.com/appsheet/answer/12008558) for more examples in this project
- [Use Apps Script to create a calendar event](https://support.google.com/appsheet/answer/12007551)
