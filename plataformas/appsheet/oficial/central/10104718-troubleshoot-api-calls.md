---
fonte: https://support.google.com/appsheet/answer/10104718?hl=en
baixado: 2026-11-10
---

# Troubleshoot API Calls

Troubleshoot API calls using the guidance provided in the following sections.

## Why isn't my API call working?

Use [Audit History](https://support.google.com/appsheet/answer/10104794) to troubleshoot API problems, as follows:

1.  Open your app in the editor.
2.  Go to **Manage \> Monitor** and expand **Audit History**.
3.  Click **Launch log analyzer**.
    The Audit History log displays.
4.  Look for audit records with an **`Action`** value of **`REST API invoke`**.
    **Note**: You may need to wait for up to five minutes for an audit record to appear in Audit History. AppSheet groups audit records and periodically writes the grouped audit records to reduce overhead. This can result in a delay before an audit record appears in the Audit History. Click **Get audit history records** periodically until you see the audit record.
5.  Click the **Details** icon to see the outcome of the API call.
6.  If the API call failed, the Details provides the reason for failure.
7.  If you see `"`**`Result": "Success"`** at the end of the audit record, then the API call succeeded.

## Error: Row having key not found

The error `Row having key '<key value>' not found` indicates that the record with the specified key could not be found when performing an update or delete. This can occur if your table has a [security filter](https://support.google.com/appsheet/answer/10104488) that excludes the record. 

The REST API request runs under the user ID you specify in the REST API `UserId` property. If no `UserId` is specified, the REST API request runs under the User ID of the app owner. See [Invoke the AppSheet API](https://support.google.com/appsheet/answer/10105398).

## Error: Value cannot be converted to type

The error `Value '<value>' in field '<field name>' cannot be converted to type '<type>'` indicates that the data value in the field is invalid or is not in the expected format. 

The [Locale](https://support.google.com/appsheet/answer/10105398) property is used when validating `Date`, `Time`, `DateTime`, `Decimal`, `Percent`, and `Price` data values. For example, when `Locale` is `en-US`, date values must be entered in `MM/DD/YYYY` format. When Locale is `en-GB`, date values must be entered in `DD/MM/YYYY` format. When no `Locale` is specified, `Locale en-US` is assumed and date values must be entered in `MM/DD/YYYY` format.

## Error: AppSheet Webhook action depth reached

The error `AppSheet Webhook action depth reached` indicates that an automation webhook is attempting to invoke the REST API repeatedly and has reached the recursive calling depth limit of 5.

This error typically arises in the following circumstance.

1.  The application contains an automation bot that invokes a webhook that calls the REST API to add, update, or delete one or more records in a table.
2.  When the REST API is called, it adds, updates, or deletes the appropriate records. It then triggers any events associated with those records. This may include events that invoke a webhook that calls the REST API. This can lead to intended or unintended recursion.
3.  Unintended recursion occurs when a webhook calls the REST API, which triggers a webhook that calls the REST API, which triggers a webhook that calls the REST API, and so forth indefinitely. This is a form of *infinite recursion*. To stop infinite recursion, AppSheet maintains a counter to detect and prevent it. When the calling depth limit of 5 is reached, AppSheet displays the error `AppSheet Webhook action depth reached` and prevents further recursion.

## Add or update of an EnumList field reports "failed Valid_If condition"

If you Add or Update a record having an `EnumList` field, the Add or Update may fail with the error:

`"Error: Row having key '<key value>' in table '<table Name>' containing value '<enumList field value>' failed Valid_If condition"`

This happens when the `EnumList` field specifies a `Valid_If `expression containing a list of valid values. If you attempt to store a record containing two or more values in the `EnumList` field, the `Valid_If `condition will fail. This is the result of a long standing shortcoming in the server expression system.

For example, the `EnumList` field might specify the `Valid_If` expression:

`LIST("A", "B", "C", "D")`

The system automatically converts that `Valid_If` expression into the following equivalent `Valid_If` expression. Note that `[_THIS]` refers to the value of the current field; in this case, the `EnumList` field.

`IN([_THIS], LIST("A", "B", "C", "D")`

When the server expression system evaluates the `IN()` expression, it fails to detect that the `EnumList` field may contain a `LIST()` of values. It mistakenly treats the value in the `EnumList` field as a single value which it compares to each value in the `LIST()`. For example, if the `EnumList` field contains `"A , C"`, it compares `"A , C"` to the `LIST()` values `"A"`, then `"B"`, then `"C"`, and finally `"D"`. The `EnumList` value "A , C" does not match any of these values, so the `Valid_If` condition fails.

**Note**: We are investigating how to fix this shortcoming in the server expression system. This is more difficult than it seems because we need to fix the problem without breaking customers who may be advertently or inadvertently relying on the current behavior. We are not aware of any way to avoid this problem other than removing the `Valid_If `expression for the `EnumList` field.
