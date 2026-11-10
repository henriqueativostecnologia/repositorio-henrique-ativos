---
fonte: https://support.google.com/appsheet/answer/10105386?hl=en
baixado: 2026-11-10
---

# Upgrade an app

During the lifecycle of an app, you might occasionally want to work on a new version of the app. The new version may have very different data and a different user experience from the current version of the app. Clearly, you'd want to keep your users on your current version until the new version is ready for deployment, and then seamlessly swap them over.

We call this an a*pp upgrade* and here's how you can achieve this behavior (this is part of the Core pricing plan).

1.  Make a copy of your app.
2.  Work on the app copy, making any desired changes and testing them with your test users.
3.  When the new app is ready for deployment, run a deployment check and mark it as **Deployed**.
4.  Open the original app in the app editor, go to **Manage \> App Versions \> App Upgrade**, and provide the name of the app copy to upgrade from. The app name is a unique name that includes a user ID suffix (something like `SalesReport-10305`). You can find the app name in the URL of an app when you open it in the app editor.
5.  Click the **Upgrade** button. This button is only displayed if you are enrolled in a Core pricing plan.

There are two very important issues to keep in mind during the app upgrade process:

1.  How do you handle the data? For read-only apps, this is a non-issue because the new version can simply start with a copy of the existing data and evolve independently. However, for apps that capture or update data, it is important that the new version and the current version stay aligned on their data. One possible approach is to have an external mechanism (for example, a periodic copy process) that moves data from the current version to the new version. AppSheet provides no built-in mechanism for this purpose.

2.  If your new version has a different column structure from the old version, and there are active users with the old version, then it is possible that one of these users has queued up a data change and that change will fail right after you upgrade to the new version. For example, if there is a table with 5 columns in the old version and a user has captured a new row. However that user is offline so the new row has not yet been synced with the backend. At the same time, you upgrade the app on the backend and the table now has 7 columns. When that user is finally online and tries to sync the update, it will fail. To avoid this situation, inform your users that a change is coming and try to perform your upgrade overnight or at a time when your users do not have outstanding data changes.
