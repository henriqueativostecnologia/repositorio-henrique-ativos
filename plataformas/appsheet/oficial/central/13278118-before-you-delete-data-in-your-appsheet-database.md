---
fonte: https://support.google.com/appsheet/answer/13278118?hl=en
baixado: 2026-11-10
---

# Before you delete data in your AppSheet database

Before you delete data from an AppSheet database, follow the recommended guidance below. Otherwise, the apps may no longer execute as expected.

- Before you [delete a database](https://support.google.com/appsheet/answer/12636914), be sure to remove any related tables from existing apps.
- Before you [delete a table](https://support.google.com/appsheet/answer/12725680#delete-table), be sure to remove the table from any existing apps.
- Before you [delete a column](https://support.google.com/appsheet/answer/12726090#delete-column), consider the impact the delete operation will have on any apps that are using it. Deleting a column may also impact the filter or group by view configuration.

To determine the apps that are using a particular table, see [Access the apps that are using a table](https://support.google.com/appsheet/answer/12728278).
