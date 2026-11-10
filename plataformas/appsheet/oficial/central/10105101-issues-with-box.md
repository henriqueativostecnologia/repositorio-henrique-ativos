---
fonte: https://support.google.com/appsheet/answer/10105101?hl=en
baixado: 2026-11-10
---

# Issues with Box

[Box.com](http://box.com/) users tend to have corporate accounts and often see two specific errors:

1.  A 403 error may occur when you attempt to copy a sample application or make a new application. This error indicates that you do not have the right permissions to create the folder to hold the new or copied application. By default, AppSheet creates a folder for each application under the /appsheet/data path. The sample spreadsheet and data are copied into this folder. In many corporate Box installations, users do not have permissions to create a folder in this path. Instead, each user (say 'joe') has permissions to a path such as '/users/joe'. In this case, you must change the default folder path for your AppSheet account. You can do this as follows:
    1.  Click **My Account** in the top navigation bar.
    2.  Click **Settings**.
    3.  Set the **Default folder path** to a Box folder path where you are allowed to create folders and files.
2.  The other error reported by some of our Box users is that Excel spreadsheet files seem to be automatically converted into CSV files on some Box installations. Users can check this by simply trying to download the Excel file from Box to see if its format has been modified -- if so, consult with your Box admin.
