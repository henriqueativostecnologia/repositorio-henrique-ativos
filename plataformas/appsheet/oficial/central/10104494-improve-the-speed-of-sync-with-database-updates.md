---
fonte: https://support.google.com/appsheet/answer/10104494?hl=en
baixado: 2026-11-10
---

# Improve the speed of Sync with database updates

Data captured or updated by the app on a device needs to be sent via the AppSheet server to the cloud provider. This can be one of the slowest aspects of the Sync process because the changes have to be made sequentially (to ensure correctness). Conceptually, there are four ways to improve this aspect of Sync performance:

1.  [Reduce the **number of updates**](#reduce-number-of-udpates)
2.  [Reduce the **amount of data** sent with each update](#reduce-amount-of-data) (for example, images captured per row)
3.  [Reduce the **amount of computation**](#reduce-computation) that must happen with each update
4.  [Sync changes **in the background**](#sync-in-background) so that the user does not need to wait for them to complete

## 1. Reduce the number of updates

The design of the app sometimes increases the number of updates that are created. For example, if three different column values of the same row are modified using Quick Edit, this creates three different updates. However, using a form to edit the row and make all three changes produces just a single update.

Similarly, be cautious with the use of app actions that make changes to a large number of rows. While these changes appear instantaneously to the app user, they all have to be synced to the backend.

## 2. Reduce the amount of data sent

Rows that involve images add significantly to the amount of data sent per update. We have seen customers build apps with more than ten image columns per row. This adds inefficiency not just to the initial Add Row action but also to subsequent updates to the row.

You can control the resolution of uploaded images using an option on the **UX \> Options** page. Obviously, if you choose to upload images at a higher resolution, this significantly increases the amount of data transferred during Sync. 

## 3. Reduce the amount of computation

There are two sources of computation when an update is synced. The first source is the use of any spreadsheet formulas. For example, Google Sheets will recompute all affected spreadsheet formulas on every single update. if you have expensive formulas (eg: computing aggregates across all the entries in the spreadsheet), this can add significant delays.

Automations are the other source of computation overhead. On every update, the automations in your app have to be evaluated. Depending on the logic in the condition and action, this could be a trivial overhead or it could be significant. In particular, automations that make data changes to other rows can add significant overhead to each update that is synced.

While these delays may be insignificant for a single update, you should consider the actual usage patterns of your app and the cumulative effect of these overheads. For example, if a user expects to collect many data changes during the day with Delayed Sync enabled, then come back to the office to sync all the changes, it may take quite a while for the sync to complete.  

## 4. Sync changes in the background

You can turn on [automatic updates](https://support.google.com/appsheet/answer/10107437). When these are turned on, local changes by a user will be sent to the server. It takes about 30 minutes to read back the latest data from other users' changes.
