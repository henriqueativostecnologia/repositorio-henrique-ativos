---
fonte: https://help.asana.com/s/article/team-csv-import?language=en_US
baixado: 2026-11-10
---

# CSV import for custom fields on users

You can add custom field information for users, such as skills, office locations, or start dates, within your Asana teams in bulk through a CSV import. This allows you to populate and maintain those valuable details with ease.

## Preparing your CSV file

To ensure a smooth import, your CSV file needs to be formatted correctly:

- **Email address:** You must have a column titled "Email Address". This column will match users in the CSV file with users in your Asana team.
- **Custom field headers:** To successfully import data for custom fields within a team, first confirm that these fields have been created in the team's "Members" tab. Creating new fields via import is not possible. The subsequent column headers in your CSV should correspond to the names of the custom fields you have set up in your team's "Members" tab.
  - For example, if you have custom fields for "Coding Languages" and "Office Location" in your team, your CSV headers would look like: Email Address, Coding Languages, Office Location.
- **Data Formatting for Field Types:**
  - **Single-select and multi-select fields:** For these field types, the CSV importer will create new options if the values in your CSV do not already exist in the field's settings. For multi-select fields, use semicolons to separate multiple values within a single cell (e.g., "Python;JavaScript;HTML").
  - **Text, number fields:**  For text or number fields, simply enter the desired text or numbers in each cell.
  - **Date fields:** Enter the values using ISO timestamp. The ISO timestamp format (ISO 8601) is a standardized way to represent dates and times, typically appearing as YYYY-MM-DDTHH:MM:SSZ or similar, ensuring clarity and global consistency by including year, month, day, hour, minute, second, and often timezone information. 
  - **People fields:** Enter the email address of the user (e.g: bob@mydomain.com). 
- **Handling blank values:** If a cell in your CSV is blank for a particular custom field, the existing value for that field in Asana will not be overwritten or cleared.

## How to import your CSV file

To upload a CSV file:

1.  Click the drop-down arrow next to the team’s name
2.  Select **Import CSV**
3.  Select the file you want to import
4.  Click **Import**

> You can click **Download template** to learn how to structure your information.

The import process will respect all existing access controls for custom fields. You can only update fields and values via CSV which you would typically have permission to edit.

## Confirmations and error handling

When you upload your file, the system will perform a basic check. If headers are not formatted correctly or the "Email Address" column is missing, the UI will show a warning.

The UI will immediately confirm that your file upload was successful if everything is formatted correctly.

The actual updating of user custom fields happens as an asynchronous background job. Once all the records in your uploaded file have been processed, Asana will email the user who uploaded the CSV, notifying them the records successfully processed and any errors.

## Frequently asked questions

### Can the CSV import create new custom fields (i.e., new columns) if they don't already exist in my team?

No. You need to ensure that the custom fields (column headers in your CSV, e.g., "Office Location") are already set up in the team's "Members" tab before you attempt to import data for them. 

### Who can use this CSV import feature?

Anyone who has permission to edit custom fields on users within the team's "Members" tab can use the CSV import feature. The import respects existing access controls.

### What happens when I import my CSV file?

The system will match users by their email address and update the custom field values in Asana based on the information in your CSV. If someone is not present in the team, it will add them to the team (and invite them to your domain) if needed. 

### How does the import handle existing custom field values? Will it overwrite my data?

Yes, the CSV import is designed to override existing data. If a cell in your CSV contains a value for a custom field, it will update and overwrite the existing value for that user in Asana. However, if a cell in your CSV is blank for a particular custom field, the existing value in Asana will not be changed.

### Can I use the CSV import to delete or clear custom field values?

No. Leaving a cell blank in the CSV will not clear Asana's existing value. 

### Can I export user custom field data to a CSV from Asana?

Not at this time.

### How should I format values for different custom field types, like multi-select? Is it case-sensitive?

For multi-select fields, separate values within a single cell using semicolons (e.g., "ValueA;ValueB;ValueC"). The handling of different custom field types will generally follow the same behavior as CSV imports for projects in Asana. The case sensitivity of custom field values will also align with how project CSV imports handle this.

### What if a custom field referenced in my CSV (e.g., "Office Location") is a single-select, but my CSV contains a value that isn't already an option for that field?

The import process will create any necessary new option values for single-select or multi-select fields. So, if "London" isn't an existing option for your "Office Location" single-select field, the import will add "London" as an option and assign it to the relevant users.

 

[](https://forum.asana.com/c/forum-en/tips/6)
