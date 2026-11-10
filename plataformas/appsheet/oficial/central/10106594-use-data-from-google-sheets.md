---
fonte: https://support.google.com/appsheet/answer/10106594?hl=en
baixado: 2026-11-10
---

# Use data from Google Sheets

Use data from Google Sheets with AppSheet in the following ways:

- Create an app using a Google Sheet. See [Create apps: The Essentials](https://support.google.com/appsheet/answer/11980957).
- [Use the Google Sheets AppSheet add-on](#add-on) (described below)

## Use the Google Sheets AppSheet add-on

The [Google Sheets AppSheet add-on](https://workspace.google.com/marketplace/app/appsheet/376242260902) automatically converts a Google Sheet to an AppSheet app when you click **Go** from the AppSheet add-on pane in your Google Sheet. You'll be taken to [www.appsheet.com](http://www.appsheet.com/) to a working mobile app you can customize.

### Caveats and limitations

#### onEdit Triggers

Google Sheets allow you to create `onEdit` triggers: code functions that run whenever a Google Sheet is edited via Google's web interface. However, `onEdit` triggers do not fire when data is edited and synced to the spreadsheet via AppSheet. If you have important functionality that needs to run on updated data, we suggest moving it to a timed trigger (a different kind of trigger that Google supports). You can learn more about these different trigger types via the Google Docs page.

#### Filters

Do not use filters on your Google Sheets: it can make the filtered rows invisible to updates. Instead, use filter views, a Google Sheets feature that lets each user create and use their own filters without affecting other users of the spreadsheet.
