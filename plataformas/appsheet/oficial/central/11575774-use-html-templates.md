---
fonte: https://support.google.com/appsheet/answer/11575774?hl=en
baixado: 2026-11-10
---

# Use HTML templates

Customize contents using HTML templates as described in the following sections:

- [Customize content using an HTML template](#customize-content)
- [View the template](#view-template)
- [Edit the template](#edit-template)
- [Manually create an HTML template](#manually-create)

See also [Use templates in a bot](https://support.google.com/appsheet/answer/11539957).

## Customize content using an HTML template

When configuring a [Send an email](https://support.google.com/appsheet/answer/11447614), [Call a webhook](https://support.google.com/appsheet/answer/11511244), or [Create a new file](https://support.google.com/appsheet/answer/11512511) task, customize content using an HTML template by performing one of the following tasks:

- Create an **HTML** template, as described in [Create a template](https://support.google.com/appsheet/answer/11539957#create-template).
- [Manually create an HTML template](#manually-create) in your cloud file system and use it, as described in [Use an existing template](https://support.google.com/appsheet/answer/11539957#use-existing-template).

For information about customizing the template, see [Customize content using templates](https://support.google.com/appsheet/answer/11539957#customize-content) and the tips provided below.

## View the template

After creating or selecting the template, click **View** adjacent to the template property to view the template.

## Edit the template

Edit the template using your preferred method.

To edit the template on your local computer:

1.  Download the template file from your data source to your computer.
2.  Edit the template file on your computer using the text editor of your choice.
3.  Upload the edited template file from your computer to your data source.

## Manually create an HTML template

Manually create an HTML template file by creating an empty text file, entering valid HTML, and saving the file using an `.html` extension.

Template variables like `<<FirstName>>` must be HTML encoded. For example, the **\<** character is HTML encoded as **&lt;** and the **\>** character is HTML encoded as **&gt;**.

The following provides an example HTML file with HTML encoding:

    <html>
      <head>
      </head>
      <body>
          <h1>MyTable</h1>
             <p>UpdateMode: &lt;&lt;_UPDATEMODE&gt;&gt;</p>
             <p>Application: &lt;&lt;_APPNAME&gt;&gt;</p>
             <p>TableName: &lt;&lt;_TABLENAME&gt;&gt;</p>
             <p>UserName: &lt;&lt;_USERNAME&gt;&gt;</p>
             <p>LastName: &lt;&lt;[LastName]&gt;&gt;</p>
             <p>FirstName: &lt;&lt;[FirstName]&gt;&gt;</p>
             <p>Age: &lt;&lt;[Age]&gt;&gt;</p>
             <p>Computed Total: &lt;&lt;[Qty]*[Price]&gt;&gt;</p>
             <p>ComputedName: &lt;&lt;[_ComputedName]&gt;&gt;</p>
      </body>
    </html>

 

After the template file is saved to your computer, upload it to one of the data sources described in [Configure the data sources for storing templates](https://support.google.com/appsheet/answer/11539957#configure-data-source).

For example, you can upload the template file to Google Drive, as follows.

1.  Ensure that the **Convert uploaded files to Google Docs editor format** option is **disabled** as described in [Upload .txt templates to Google Drive](https://support.google.com/appsheet/answer/11547093).
2.  Open Google Drive and navigate to the Google Drive folder where you wish to upload the file.
3.  Click **New** and then click **File upload**.
4.  When the file open dialog appears, navigate to the template file on your computer, select the file, and click **Open**.

After the template file is uploaded, use it as described in [Use an existing template](https://support.google.com/appsheet/answer/11539957#use-existing-template).

Each time you modify the HTML template you must upload the template file to Google Drive. Google Drive will retain the original DocId. AppSheet will use the last uploaded version of the template file as the attachment template.
