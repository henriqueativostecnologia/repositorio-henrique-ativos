---
fonte: https://support.google.com/appsheet/answer/11575775?hl=en
baixado: 2026-11-10
---

# Use JSON templates

Customize content using JSON templates as described in the following sections:

- [Customize content using a JSON template](#customize-content)
- [View the template](#view-template)
- [Edit the template](#edit-template)
- [Manually create a JSON template](#manually-create-template)

See also [Use templates in a bot](https://support.google.com/appsheet/answer/11539957).

## Customize content using a JSON template

When configuring a [Send an email](https://support.google.com/appsheet/answer/11447614), [Call a webhook](https://support.google.com/appsheet/answer/11511244), or [Create a new file](https://support.google.com/appsheet/answer/11512511) task, customize content using a JSON template by performing one of the following tasks:

- Create an **JSON** template, as described in [Create a template](https://support.google.com/appsheet/answer/11539957#create-template).
- [Manually create a JSON template](#manually-create-template) in your cloud file system and use it, as described in [Use an existing template](https://support.google.com/appsheet/answer/11539957#use-existing-template).

For information about customizing the template, see [Customize content using templates](https://support.google.com/appsheet/answer/11539957#customize-content) and the tips provided below.

## View the template

After creating or selecting the template, click **View** adjacent to the template property to view the template.

## Edit the template

Edit the template using your preferred method.

To edit the template on your local computer:

1.  Download the template file from your data source to your computer.
2.  Edit the template file on your computer using the text editor of your choice.
3.  Upload the edited template file from your computer to your data source.

For example, to download the template file from Google Drive to your computer:

1.  In the AppSheet Editor click **View** adjacent to the template name.
2.  Download the template file to your computer.
    For example, if you are using the Google Chrome browser:
    1.  Download the template file to your computer by clicking the **Download** button at the top right of the browser screen.
    2.  You will see the downloaded file in the bottom left of the browser screen. Click **^** to the right of the downloaded template name and select **Show in Finder**.

To edit the template file on your computer:

1.  Open the template file in the text editor of your choice. For example, on Windows you might use Notepad.
2.  Edit the template file and save your changes.

To upload the edited template file from your computer to Google Drive:

1.  In the AppSheet Editor click **View** adjacent to the template name.
2.  If you are using the Google Chrome browser, click **More actions** in the top right of the browser screen and select **Details**.
3.  Click the folder name link to the right of the **Location** property to open the Google Drive folder containing the template file.
4.  Drag and drop the updated template file from the folder on your computer to the **Content** folder on Google Drive. The template file will retain its original DocId on Google Drive.

## Manually create a JSON template

Manually create a JSON template file by creating an empty text file, entering valid JSON, and saving the file using an `.json` extension.

The following provides an example JSON file:

    {
      "MyTable": [
      <<Start: Select(MyTable[MyKey], TRUE)>>
          {
             "UpdateMode": "<<_UPDATEMODE>>",
             "Application": "<<_APPNAME>>,
             "TableName": "<<_TABLENAME>>,
             "UserName": "<<_USERNAME>>,
             "LastName": "<<[LastName]>>",
             "FirstName": "<<[FirstName]>>",
             "Age": "<<[Age]>>",
             "Computed Total": "<<[Qty]*[Price]>>",
             "ComputedName": "<<_ComputedName>>"
          },
       <<End>>
       ]
    }

 

After the template file is saved to your computer, upload it to one of the data sources described in [Configure the data sources for storing templates](https://support.google.com/appsheet/answer/11539957#configure-data-source).

For example, you can upload the template file to Google Drive, as follows.

1.  Ensure that the **Convert uploaded files to Google Docs editor format** option is **disabled** as described in [Upload .txt templates to Google Drive](https://support.google.com/appsheet/answer/11547093).
2.  Open Google Drive and navigate to the Google Drive folder where you wish to upload the file.
3.  Click **New** and then click **File upload**.
4.  When the file open dialog appears, navigate to the template file on your computer, select the file, and click **Open**.

After the template file is uploaded, us it as described in [Use an existing template](https://support.google.com/appsheet/answer/11539957#use-existing-template).

Each time you modify the JSON template you must upload the template file to Google Drive. Google Drive will retain the original DocId. AppSheet will use the last uploaded version of the template file as the attachment template.
