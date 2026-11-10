---
fonte: https://support.google.com/appsheet/answer/10104702?hl=en
baixado: 2026-11-10
---

# Concurrent usage with multiple users

AppSheet apps allow multiple users to add, update, and delete data concurrently. This leads to the natural question -- how do we deal with multiple people updating the same data at the same time?

The simple rule is that **the last writer wins**.

- When a user adds, updates, or deletes a record on their mobile device, the user's change is queue in the client device or browser. When the client syncs their change, the client submits the add, update, or delete request to the server.
- When the server receives the add, update, or delete request resulting from the client's sync, the server performs that request. If two or more client requests arrive for the same table at or near the same time, the server normally serializes the client requests and performs them one by one. As a result, the second client request is only performed after the first client request is completely performed.
- The unit of change is a single row. Fortunately, many applications work so that no two clients are likely to update the same row at the same time. For example, one client may be updating a record for one customer while a second client is updating a record for a different customer. These two concurrent updates will not collide.
- If two clients happen to change the same row at nearly the same time, the last client's change is what persists. This is referred to as "the last writer wins" conflict resolution strategy.
- Even if someone updates the data directly in the spreadsheet (not through the app), this is treated like any other data update.

There are three cases during client sync when "the last writer wins" conflict resolution strategy may be used.

### UpdateExistingRecord on add

If the user adds a row when a row with the same key already exists, then that row is updated with the data contained in the second client's add request. When this occurs, the Audit History record for the second Add operation will include the `UpdateExistingRecord` property. This property contains the key of the existing record that was updated.

This can sometimes occur if a single client submits the same add request multiple times. For example, the client might submit the add request and then lose network connectivity before the server can respond to the original add request. This leaves the client uncertain if the add request was received and processed by the server. In this case, the client resubmits the add request when network connectivity is later restored.

The server attempts to detect and properly respond to duplicate client requests. The server remembers the most recent request from each client for up to 24 hours. If the client resubmits the same request again, the server detects the duplicate request and responds with the same answer it would have returned for the original request. By remembering the most recent request and response for each client, the server attempts to handle duplicate client requests gracefully. It avoids performing the client's add request twice.

If the client loses network connectivity for longer than 24 hours, the server may no longer remember the original client request. If the client resubmits the add request thereafter, the server will attempt to perform the add request for a second time. When it performs the add request and detects that the record already exists, it will include the `UpdateExistingRecord` property in Audit History for the second add request. The `UpdateExistingRecord` property will contain the key of the original record.

If your application contains automation workflow rules that are triggered by add operations, those rules will be triggered again when the second client add request is submitted more than 24 hours after the first client add request.

You can detect when this has occurred by looking at the Audit History `Stop` record for the second add request. If it contains the `UpdateExistingRecord `property, then the add has been submitted by the client twice with a delay of 24 hours or more between the first and second add request. You will also see that the add `start` Audit History records for both client add requests contain the same `clientId` and `requestId` property values.

### DeleteDeletedRecord on delete

If the user deletes a row but no row with that key exists, then that change is ignored. When this occurs, the Audit History record for the delete operation will include the `DeleteDeletedRecord` property which contains the key of the already deleted record.

### UpdateDeletedRecord on update

If the user edits a row but no row with that key exists, then that change is ignored because clearly some other user explicitly deleted it first. When this occurs, the Audit History record for the edit operation will include the `UpdateDeletedRecord` property which contains the key of the deleted record.
