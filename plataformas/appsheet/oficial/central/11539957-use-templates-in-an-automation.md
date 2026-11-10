---
fonte: https://support.google.com/appsheet/answer/11539957?hl=en
baixado: 2026-11-10
---

# Use templates in an automation

Templates enable you to more precisely control the appearance of content sent from an automation bot. When configuring your bot, you build templates to customize the following content:

- [Email body and attachments](https://support.google.com/appsheet/answer/11447614)
- [SMS messages](https://support.google.com/appsheet/answer/11509435)
- [Files](https://support.google.com/appsheet/answer/11512511)
- [Webhooks](https://support.google.com/appsheet/answer/11511244)

Use templates in an automation in one of the following ways:

- [Build your template content](#build-template-content) directly in the editor when configuring your automation. See also [Build templates using the Template Assistant](https://support.google.com/appsheet/answer/15876372).
- [Use an external template](#use-external-templates). For example a template built using Google Docs or Microsoft Word.

## Build your template content

In general, you can include the following content in a template:

- Text
- Images
- [Variables](https://support.google.com/appsheet/answer/11539253) that refer to column values in your tables
- [Expressions](https://support.google.com/appsheet/answer/10104642) that yield computed values
- [Start expressions](https://support.google.com/appsheet/answer/11541779) that display the rows of a table
- [If expressions](https://support.google.com/appsheet/answer/11568425) that allow you to include or exclude portions of a template

The final result will contain the template contents with all variables and expressions resolved.

For additional template formatting tips and examples, see the following topics:

- [Display images, thumbnails, drawings, and signatures in templates](https://support.google.com/appsheet/answer/11547760)
- [Display Address, LatLong, and XY values in templates](https://support.google.com/appsheet/answer/11547559)
- [Use CONCATENATE(), Ampersand operators, and text expressions in templates](https://support.google.com/appsheet/answer/11577479)
- [Sample email templates](https://support.google.com/appsheet/answer/11544497)

## Use external templates

You can using an external template to [build your template content](#build-template-content) as described in the following sections:

- [Supported external template content types](#supported-external-template-content-types)
- [Create an external template](#create-external-template)
- [Manually create an external template](#manually-create-external-template)
- [Use an external template](#use-existing-external-template)
- [Configure the data sources for storing the external templates](#configure-data-source)

See also: [Use and troubleshoot custom fonts in templates](https://support.google.com/appsheet/answer/11572062)

### Supported external template content types

AppSheet supports the content types defined in the following table for external templates. Learn more about creating and customizing external templates for a particular content type using the links provided.

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Template**                                                                  | **Supported content types**                                                   |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Email body                                                                    | -   [Google Docs](https://support.google.com/appsheet/answer/11568965)        |
|                                                                               | -   [Microsoft Word](https://support.google.com/appsheet/answer/11572694)     |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Email attachment, file, or webhook                                            | -   [CSV](https://support.google.com/appsheet/answer/11575675)                |
|                                                                               | -   [FORM_URL_ENCODED](https://support.google.com/appsheet/answer/11576082)   |
|                                                                               |     (Webhooks only)                                                           |
|                                                                               | -   [Microsoft Excel](https://support.google.com/appsheet/answer/11575067)    |
|                                                                               |     (XLSX)                                                                    |
|                                                                               | -   [HTML](https://support.google.com/appsheet/answer/11575774)               |
|                                                                               | -   [JSON](https://support.google.com/appsheet/answer/11575775)               |
|                                                                               | -   PDF (source from [Google                                                  |
|                                                                               |     Docs](https://support.google.com/appsheet/answer/11568965) or [Microsoft  |
|                                                                               |     Word](https://support.google.com/appsheet/answer/11572694))               |
|                                                                               | -   [ICS/iCalendar calendar                                                   |
|                                                                               |     invitation](https://support.google.com/appsheet/answer/11575077)          |
|                                                                               | -   [XML](https://support.google.com/appsheet/answer/11575476)                |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| SMS                                                                           | [Text                                                                         |
|                                                                               | (.txt)](https://s                                                             |
|                                                                               | upport.google.com/appsheet/answer/11509435#manually-create-sms-body-template) |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

### Create an external template

Create an external template as described in the following table. See also [Create a Microsoft Word template on Google Drive](https://support.google.com/appsheet/answer/11572694#create-template-google-drive).

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Content**                                                                   | **Steps to create an external template**                                      |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Email body                                                                    | 1.  Create and save or open an existing **Send an email** task.               |
|                                                                               | 2.  Disable **Use default content?**                                          |
|                                                                               | 3.  Click **Create** adjacent to the **Email Body Template** property.        |
|                                                                               |                                                                               |
|                                                                               | For more information, see [Send an email from a                               |
|                                                                               | bot](https://support.google.com/appsheet/answer/11447614).                    |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Email attachment                                                              | 1.  Create or open an existing **Send an email** task.                        |
|                                                                               | 2.  Disable **Use default content?**                                          |
|                                                                               | 3.  Set the content type using the **Attachment Content Type** property.      |
|                                                                               | 4.  Set the **Attachment File Store** property to the file system where you   |
|                                                                               |     want your attachments to be saved.                                        |
|                                                                               | 5.  Click **Create** adjacent to the **Attachment Template** property.        |
|                                                                               |                                                                               |
|                                                                               | For more information, see [Send an email from a                               |
|                                                                               | bot](https://support.google.com/appsheet/answer/11447614).                    |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| File                                                                          | 1.  Create or open an existing **Create a new file** task.                    |
|                                                                               | 2.  Set the **HTTP Content Type** property to the desired value.              |
|                                                                               | 3.  Set the **File Store** property to the file system where you want files   |
|                                                                               |     to be saved.                                                              |
|                                                                               | 4.  Click **Create** adjacent to the **Template** property.                   |
|                                                                               |                                                                               |
|                                                                               | For more information, see [Create and save a file from a                      |
|                                                                               | bot](https://support.google.com/appsheet/answer/11512511).                    |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| SMS                                                                           | See [Manually create an SMS body                                              |
|                                                                               | template](https://su                                                          |
|                                                                               | pport.google.com/appsheet/answer/11509435#manually-create-sms-body-template). |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Webhook                                                                       | 1.  Create or open an existing a **Call a webhook** task.                     |
|                                                                               | 2.  Set the **HTTP Content Type** property to the desired value.              |
|                                                                               | 3.  Set the **Body Template Data Source** to the desired [data                |
|                                                                               |     sour](#configure-data-source)[ce](#configure-data-source).                |
|                                                                               | 4.  Click **Create** adjacent to the **Body Template** property.              |
|                                                                               |                                                                               |
|                                                                               | If you are using the webhook to invoke the AppSheet API, configure the        |
|                                                                               | webhook **URL** value when [configuring the                                   |
|                                                                               | webhook](https://support.google.com/appsheet/answer/11511244#add-configure)   |
|                                                                               | before clicking the **Create** button. AppSheet examines the webhook URL      |
|                                                                               | value to determine if the AppSheet API is being invoked. If so, AppSheet uses |
|                                                                               | the table name you specify following `/tables/` in the URL to determine the   |
|                                                                               | field values to include in the JSON body template.                            |
|                                                                               |                                                                               |
|                                                                               | If your table contains a List of Refs to related *child* records, the created |
|                                                                               | JSON Body Template file will include a Start expression that extracts the     |
|                                                                               | data values of all child records of the parent record. If the child table     |
|                                                                               | contains a List of Refs to related *grandchild* records, the created JSON     |
|                                                                               | Body Template file will include a Start expression that extracts the data     |
|                                                                               | values of all grandchild records of the child records. The created JSON Body  |
|                                                                               | Template file will extract the parent record, the child records, the          |
|                                                                               | grandchild records, the great grandchild records, and so on. This allow you   |
|                                                                               | to extract the entire hierarchy of records.                                   |
|                                                                               |                                                                               |
|                                                                               | For more information, see [Call a webhook from a                              |
|                                                                               | bot](https://support.google.com/appsheet/answer/11511244).                    |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

In each case, AppSheet creates the template and writes it to your default data source unless it is explicitly set. To explicitly set the data source, see [Configure the data sources for templates](#configure-data-source) (below).

By default, AppSheet uses the following file naming conventions similar to the following to ensure the template name is unique:
`Content/`*`task-name`*`_BodyTemplate_`*`yyyymmdd_hhmmss`*
`Content/`*`task-name`*`_AttachmentTemplate_`*`yyyymmdd_hhmmss`*

Click **View** to view the template and [customize the template](#customize-content), as required.

**Note**: The template properties reference a single template file. You cannot use an expression to specify the template file. If you need to choose between two or more template files, define a separate event for each template file and specify an expression in the **Condition** property to select which event to invoke.

### Manually create an external template

You can manually create an external template and upload it to one of the the data sources described in [Configure the data sources for templates](#configure-data-source). Then, follow the steps in the next section, [Use an existing external template](#use-existing-template).

### Use an existing external template

To use an existing external template:

1.  Create or open an existing task.
2.  Disable **Use default content?** (if applicable).
3.  Click the **Browse** icon adjacent to the template property.
4.  Select the data source using the **Get data from...** dialog box when prompted, then select an existing template file.
5.  Click **View** to view the template and [customize the template](#customize-content), as required.

### Configure the data sources for storing external templates

To use external templates, your account must include one or more of the supported data sources listed below. To add a new data source, see [Use multiple data sources](https://support.google.com/appsheet/answer/10106309).

AppSheet supports the following data source for **Google Doc** template formats:

- Google Drive

AppSheet supports the following data sources for **all other** template formats:

- Box
- Dropbox
- Google Drive
- Microsoft Office 365
- Microsoft OneDrive

An external template is stored on your default data source unless it is explicitly set. For example, if your default data source is Google, when you click **Create**, the new template is created on your Google Drive. Similarly, if your default data source is Box, Dropbox, Microsoft Office 365, or Microsoft OneDrive, when you click **Create**, the template file is created on that data source.

To explicitly set the data source to use for an external template:

- Set the associated **Data Source** or **File Store** property, if applicable.
- Click the **Browse** icon adjacent to the template property and select the data source using the **Get data from...** dialog box, then select an existing template file.
- **Note**: If you click **Create** after browsing for an existing template file, the new template will be saved to the data source you selected while browsing.

See also [Create a Microsoft Word template on Google Drive](https://support.google.com/appsheet/answer/11572694#create-template-google-drive).
