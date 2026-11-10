---
fonte: https://support.google.com/appsheet/answer/11509435?hl=en
baixado: 2026-11-10
---

# Send an SMS message from an automation

To send an SMS message from an automation bot, add and configure the **Send an SMS** task as described in the following sections:

- [Add and configure the Send an SMS task](#add-configure)
- [Configure your SMS account](#configure-sms-account)
- [Add phone numbers](#add-phone-numbers)
- [Manually create an SMS body template](#manually-create-sms-body-template)

## Add and configure the Send an SMS task

Add and configure the **Send an SMS** task by performing the following steps:

1.  Add the **Send an SMS **task to a bot, as described in [Add a task to a bot](https://support.google.com/appsheet/answer/11445301#add-task).
2.  Configure the **Send an SMS** task by setting the properties described in the following tables.
3.  When you are done, save the app by selecting one of the following:
    - **Save** - Save the app.
    - **Save & verify data** - Save the app and verify that it is runnable based on external dependencies.

After you save the app, you can reuse task in other bots.

Configure the **Send an SMS** task by using the settings described in the following tables.

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Property**                                                                  | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Linking                                                                       | Enable or disable reuse of this component by expanding the **Linking** panel  |
|                                                                               | and toggling the **Linking** setting. See [Reuse automation                   |
|                                                                               | components](https://support.google.com/appsheet/answer/12193489).             |
|                                                                               |                                                                               |
|                                                                               | Expand the Linking panel and toggle the Linking setting to enable or disable  |
|                                                                               | component reuse                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Task name                                                                     | Name of the task. It must be unique within your app.                          |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Table name                                                                    | Table defined in the                                                          |
|                                                                               | [event](https://support.google.com/appsheet/answer/11445188) and used by the  |
|                                                                               | task.                                                                         |
|                                                                               |                                                                               |
|                                                                               | To view or edit the structure of the selected table, position your cursor in  |
|                                                                               | the field and click Edit icon  . See [Tables: The                             |
|                                                                               | Essentials](https://support.google.com/appsheet/answer/10105821) for more     |
|                                                                               | information.                                                                  |
|                                                                               |                                                                               |
|                                                                               | **Note**: To use a table that is different from the table defined in the      |
|                                                                               | event, add a [Call a                                                          |
|                                                                               | process](https://s                                                            |
|                                                                               | upport.google.com/appsheet/answer/11463007#step-type&zippy=%2Ccall-a-process) |
|                                                                               | step.                                                                         |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Via channel                                                                   | Account used to send the SMS message.                                         |
|                                                                               |                                                                               |
|                                                                               | Select one of the following values:                                           |
|                                                                               |                                                                               |
|                                                                               | -   **\_AppSheet_Default_SMS** - Use AppSheet's default SMS account.          |
|                                                                               |     (Supported only in the US and Canada.)                                    |
|                                                                               |                                                                               |
|                                                                               |     The default SMS channel will no longer be available after April 21, 2025. |
|                                                                               |     Connect a custom Twilio account to send an SMS notification.              |
|                                                                               |                                                                               |
|                                                                               |     This account **doesn't support**:                                         |
|                                                                               |                                                                               |
|                                                                               |     -   MMS messages.                                                         |
|                                                                               |     -   Sending the SMS message to contacts outside of the US and Canada.     |
|                                                                               |                                                                               |
|                                                                               |     You must use your own custom Twilio account to send messages with media   |
|                                                                               |     files or send messages to contacts outside the US and Canada.             |
|                                                                               |                                                                               |
|                                                                               | -   **\_Custom_Twilio_SMS** - Use your own custom Twilio account. You will    |
|                                                                               |     need to provide additional custom Twilio settings, as described in [Use   |
|                                                                               |     your personal Twilio account](#personal-twilio).                          |
|                                                                               |                                                                               |
|                                                                               | See [Configure your SMS account](#configure-sms-account) for more             |
|                                                                               | information.                                                                  |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| To                                                                            | List of SMS recipients (phone numbers). Click **Add** to add a phone number   |
|                                                                               | or an expression using the Expression Assistant. Repeat to add additional     |
|                                                                               | phone numbers.                                                                |
|                                                                               |                                                                               |
|                                                                               | See [Add phone numbers](#add-phone-numbers) for more information.             |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Use default content?                                                          | Toggle to indicate whether you want to use the default email content or       |
|                                                                               | provide customized content. If enabled, the task uses default content. If     |
|                                                                               | disabled, customize the content using the additional properties displayed, as |
|                                                                               | described below.                                                              |
|                                                                               |                                                                               |
|                                                                               | This property is enabled by default.                                          |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

If you disable the **Use default content?** property, customize the content using the additional properties displayed, as described below.

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Property**                                                                  | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Body                                                                          | Body of the SMS message.                                                      |
|                                                                               |                                                                               |
|                                                                               | To define the SMS body, do **one** of the following:                          |
|                                                                               |                                                                               |
|                                                                               | -   Enter the SMS body in this property, including text,                      |
|                                                                               |     [variables](https://support.google.com/appsheet/answer/11539253), and     |
|                                                                               |     [expressions](https://support.google.com/appsheet/answer/10104642).       |
|                                                                               | -   Leave this property blank and specify a **Body Template** (see below).    |
|                                                                               | -   Leave this property and **Body Template** property blank to use the       |
|                                                                               |     default content.                                                          |
|                                                                               |                                                                               |
|                                                                               | **Note**: The **Body Template** property (if specified) takes precedence over |
|                                                                               | this property.                                                                |
|                                                                               |                                                                               |
|                                                                               | Defaults to:\                                                                 |
|                                                                               | `"UpdateMode: <<_UPDATEMODE>>, Application: <<_                               |
|                                                                               | APPNAME>>, TableName: <<_TABLENAME>>, UserName: <<_USERNAME>>, At: <<_NOW>>"` |
|                                                                               |                                                                               |
|                                                                               | **Example**:\                                                                 |
|                                                                               | `"UpdateMode: Update, Application: MyAppN                                     |
|                                                                               | ame, TableName: MyEmployees, UserName: Adam Smith, At: 6/2/2016 12:06:50 AM"` |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Body Template                                                                 | Template to use for more precise control of the email body. See [Manually     |
|                                                                               | create an SMS body template](#manually-create-sms-body-temlate) and the       |
|                                                                               | **Body** property description (above).                                        |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Body Template Data Source                                                     | Data source used for the body template.                                       |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Media URLs                                                                    | List of URLs that reference media files to be attached to the SMS messaeg.    |
|                                                                               | Media URLs can be drawings, images, signatures, thumbnails, and so on. Only   |
|                                                                               | GIF, PNG, or JPEG media file formats are supported. You can add up to 10      |
|                                                                               | media URLs. Each media file must not exceed 5MB.                              |
|                                                                               |                                                                               |
|                                                                               | Click **Add** to attach drawings, images, signatures, thumbnails, or files to |
|                                                                               | be attached to the SMS message. Specify text or                               |
|                                                                               | [expressions](https://support.google.com/appsheet/answer/10104642). Repeat to |
|                                                                               | add additional media URLs.                                                    |
|                                                                               |                                                                               |
|                                                                               | **Examples**:                                                                 |
|                                                                               |                                                                               |
|                                                                               | -   `https://www.google.com/images//googlelogo_color_272x92dp.png`            |
|                                                                               | -   `MyPhoto.jpeg`                                                            |
|                                                                               | -   `[MyImage]`                                                               |
|                                                                               | -   `IF([Age] < 30, [MyImage1], [MyImage2])`                                  |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

 

 Expand and customize the **Advanced** settings, as described below.

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Setting**                                                                   | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Inputs                                                                        | Add inputs to dynamically configure a task. For details, see [Set input       |
|                                                                               | values dynamically in                                                         |
|                                                                               | tasks](https:                                                                 |
|                                                                               | //support.google.com/appsheet/answer/11445301#set-input-values-dynamically).  |
|                                                                               |                                                                               |
|                                                                               | 1.  Expand the **Advanced** section.                                          |
|                                                                               | 2.  Click **Add** under Inputs.                                               |
|                                                                               | 3.  Enter the name of the input value in the **Name** field.                  |
|                                                                               | 4.  Select the data type from the **Type** drop-down.\                        |
|                                                                               |     Only a subset of data types are supported for inputs.                     |
|                                                                               | 5.  To add an initial value or edit any fields:                               |
|                                                                               |     1.  Click  to open the Input dialog.                                      |
|                                                                               |     2.  Add a value or expression in the **Initial value** field.\            |
|                                                                               |         If you don't specify an initial value, then the input value will be   |
|                                                                               |         required. If an initial value is specified, then the input value is   |
|                                                                               |         optional.                                                             |
|                                                                               |         Use of `[_THIS]` or `[_INPUT]` are not supported in the Initial value |
|                                                                               |         field.                                                                |
|                                                                               |     3.  Edit other fields, as required.                                       |
|                                                                               |     4.  Click **Done**.                                                       |
|                                                                               | 6.  Repeat to add additional input values.                                    |
|                                                                               |                                                                               |
|                                                                               | Then, use the following expressions to access the input values from the       |
|                                                                               | current step: `[_INPUT].[`*`inputname`*`]`                                    |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

The following sections provide more information about configuring the **Send an SMS** task:

- [Configure your SMS account](#configure-sms-account)
- [Add phone numbers](#add-phone-numbers)
- [Manually create an SMS body template](#manually-create-sms-body-template)

## Configure your SMS account

You can use AppSheet's Chime account (United States and Canada only) or your personal Twilio account, as described in the following sections.

### Use the AppSheet Chime account

The default SMS channel will no longer be available after April 21, 2025. Connect a [custom Twilio account](#personal-twilio) to send an SMS notification.

To use the AppSheet Chime account, select **\_AppSheet_Default_SMS** in the **Via channel** property when configuring the Send an SMS task (as described above).

 

Consider the following when using the AppSheet Chime account:

- The AppSheet Chime account works only in the United States and Canada.
- All Chime SMS-related charges are paid by AppSheet.
- You must be enrolled in an AppSheet Starter, Core, Publisher Pro, Enterprise Standard, or Enterprise Plus subscription plan.
- You can send SMS messages to phone numbers located in the United States and Canada.
- You cannot send SMS messages to [premium-rate](https://en.wikipedia.org/wiki/Premium-rate_telephone_number) phone numbers having area codes that begin with 9xx.
- The SMS message body may contain at most 160 characters.

### Use your personal Twilio account

Sign in to your personal Twilio account to access account information and upgrade your account (if required):

1.  Sign in to your personal [Twilio account](https://www.twilio.com/login).
    If you do not have a Twilio account, complete the sign up process. It may ask you to verify a phone number. This is used for security purposes only.

2.  After you are signed in, under **Account Summary** ([https://www.twilio.com/console/account/settings](https://www.twilio.com/console/account/settings)) locate your **Twilio Account SID** and your **Twilio Auth Token** under **LIVE Credentials**. (View the Twilio Auth Token using the More menu.) You will need this information when configuring SMS using AppSheet.

3.  If required, upgrade your Twilio account from a trial account by clicking [https://www.twilio.com/console/billing](https://www.twilio.com/console/billing). You can then click **add funds** and turn on **auto renew** based on your projected usage. You can also create alerts and auto recharges, as well.

4.  Choose your Twilio phone number by navigating to **[https://www.twilio.com/user/account/phone-numbers/search](https://www.twilio.com/user/account/phone-numbers/search)**. From here, search for a phone number that you would like to use for your account to confirm its availability. Twilio recommends searching by area code when searching for a phone number. After you find a phone number that is available click **buy**.

To use a your personal Twilio account, when configuring the Send an SMS task (described above), select **\_Custom_Twilio_SMS** in the **Via channel** property, and customize the Twilio settings using the additional properties displayed, as described below.

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Field**                                                                     | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| AccountSid                                                                    | Your Twilio account ID.                                                       |
|                                                                               |                                                                               |
|                                                                               | Available under your personal Twilio Account Summary at:                      |
|                                                                               | [https://www.twilio.c                                                         |
|                                                                               | om/console/account/settings](https://www.twilio.com/console/account/settings) |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| AuthToken                                                                     | Your Twilio account Auth token.                                               |
|                                                                               |                                                                               |
|                                                                               | Available under your personal Twilio Account Summary at:                      |
|                                                                               | [https://www.twilio.c                                                         |
|                                                                               | om/console/account/settings](https://www.twilio.com/console/account/settings) |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| CountryCodes                                                                  | List of [ISO 3166-1                                                           |
|                                                                               | Alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1#Current_codes) two-letter   |
|                                                                               | country codes used to validate phone numbers.                                 |
|                                                                               |                                                                               |
|                                                                               | Click **Add** to add an ISO 3166-1 two-letter Country Code. Repeat to add     |
|                                                                               | two-letter country codes for each country having a **To** or **From** phone   |
|                                                                               | number.                                                                       |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| From                                                                          | Phone number used as the source of the SMS. Specify text and                  |
|                                                                               | [expressions](https://support.google.com/appsheet/answer/10104642).           |
|                                                                               |                                                                               |
|                                                                               | See [Add phone numbers](#add-phone-numbers) for more information.             |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

Consider the following when using your personal Twilio account:

- All Twilio SMS-related charges appear on your personal Twilio account.
- You must be enrolled in an AppSheet Starter, Core, Publisher Pro, Enterprise Standard, or Enterprise Plus subscription plan.
- You can send SMS messages to phone numbers located in the countries you specify in your SMS automation rule.
- For your protection, you cannot send SMS messages to [premium-rate](https://en.wikipedia.org/wiki/Premium-rate_telephone_number) phone numbers for which higher rates are charged. For example, premium-rate phone numbers in the United States often begin with 9xx. This restriction does not apply to valid, non-premium-rate phone numbers such as those within area code 912 in the United States, for example.
- The SMS message body may contain at most 1600 characters.

## Add phone numbers

The following provides guidelines for adding phone numbers in the **To** property when configuring the Send an SMS task:

- **Enter a specific phone number**, such as `4255551212` or `+14255551212`.
  To enter a phone number that contains special characters such as hyphens, parentheses, or spaces, you must enclose the phone number in quotes. For example:
  `"(425) 555-1212"`
  `"425-555-1212"`
  `"425 555 1212"`

- **Use a field in a record that is being modified**.
  For example, when a new order is received, you can send an SMS message to the customer who created the order. In this scenario, enter the name of the field that contains the customer's phone number. For example, if the `CustomerPhone` field in the order record contains the customer's phone number, enter the following expression: `[CustomerPhone]`

- **Use a field in a record that is referenced by the record being modified**.
  For example, when a new order is received, you can send an SMS message to the customer who created the order. Each order record might contain a reference to a customer record that contains the customer's phone number. In this scenario, enter the name of the order record field that references the customer record followed by the name of the customer record field that contains the customer's phone number. For example, if the order record field that references the customer record is `CustRef` and the name of the customer record field containing the customer's phone number is `CustPhone`, specify the customer's phone number by entering the expression: `[CustRef].[CustPhone]`

- **Use an entire column in another table**.
  For example, each time a new order is added, you can send an SMS message to all of the people defined in another table. In this scenario, enter the name of the table followed by the field that contains the phone number. For example, if you create a table called `PeopleToInform` that contains two columns, `Name` and `Phone`, each time a new order is added, you can send SMS messages to all of the people in the `PeopleToInform` table by entering the expression: `PeopleToInform[Phone]`

## Manually create an SMS body template

**Note**: To support the use of SMS body templates, Google must be a [supported data source](https://support.google.com/appsheet/answer/10106309).

Manually create an SMS template file by creating an empty text file, entering valid content, and saving the file using a `.txt` extension. For information about customizing the template, see [Customize content using templates](https://support.google.com/appsheet/answer/11539957#customize-content).

The following provides an example of an SMS body:

    Congratulations <<[FirstName]>> <<[LastName]>>.
    Your order for <<[Qty]*[Price]> shipped <<TODAY()>>.
    <<If: [Expedited] = true>>
    You order will arrive in one business day.
    <<EndIf>>
    <<If: [Expedited] = false>>
    You order will arrive in three to five business days.
    <<EndIf>>

The resulting SMS message contains the content with all variables and expressions evaluated and replaced with the appropriate values.

**Note**: You must ensure that the resulting SMS message length does not exceed the maximum SMS message length of 160 characters when using the AppSheet Chime account or 1600 characters when using your personal Twilio account.

After the template file is saved to your computer, upload it to **Google Drive** as follows.

1.  Ensure that the **Convert uploaded files to Google Docs editor format** option is **disabled**, as described in [Upload .txt templates to Google Drive](https://support.google.com/appsheet/answer/11547093).
2.  Open Google Drive and navigate to the Google Drive folder where you wish to upload the file.
3.  Click **New** and then click **File upload**.
4.  When the file open dialog appears, navigate to the template file on your computer, select the file, and click **Open**.

After the template file is uploaded, use it as described in [Use an existing template](https://support.google.com/appsheet/answer/11539957#use-existing-template).

Each time you modify the SMS template you must upload the template file to Google Drive. Google Drive will retain the original DocId. AppSheet will use the last uploaded version of the template file as the attachment template.

### View the SMS body template

After uploading the template, click **View** adjacent to the template property to view the template.

### Edit the SMS body template

To edit the template:

1.  Download the template file from your data source to your computer.
2.  Edit the template file on your computer using the text editor of your choice.
3.  Upload the edited template file from your computer to your data source.
