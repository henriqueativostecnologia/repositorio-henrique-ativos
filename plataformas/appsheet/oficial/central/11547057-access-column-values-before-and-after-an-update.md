---
fonte: https://support.google.com/appsheet/answer/11547057?hl=en
baixado: 2026-11-10
---

# Access column values before and after an update

Within the context of a data change, when a record is updated you can access the value of each column both before and after it is updated.

About Before and After values

- [Before value](#before-value)
- [After value](#after-value)

Use Before and After values:

- [Use the Before and After values in an automation](#use-in-automation)
- [Display the Before value of a column](#display-before)
- [Display the After value of a column](#display-after)
- [Display the Before and After values of a column](#display-before-after)
- [Compare the Before and After values of a column](#compare-before-after)
- [Check for specific Before or After values](#check-for-before-after)

## Before value

The *Before* value is captured just before a record is updated. It contains the field values obtained from the worksheet or database record just before the update is applied.

The Before value includes all virtual column values. The virtual column values are recomputed when the Before value is retrieved. This ensures that the virtual column values reflect the most current field values.

The Before value may not be the same record value that was present on the client device when it made the update. If you have two or more client devices, the following situation can arise:

1.  Client device 1 reads the record.
2.  Client device 2 reads the same record.
3.  Client device 2 updates its copy of the record and syncs its update to the server.
4.  Client device 1 updates its copy of the record and syncs its update to the server.

In this case, the Before value for the update synced by Client device 1, will contain the changes made by Client device 2. This is rarely a problem, but you should be aware that it can occur.

## After value

The *After* value is captured just after a record is updated. It contains the field values obtained from the worksheet or database record just after the update is applied.

The After value includes all virtual column values. The virtual column values are recomputed when the After value is retrieved. This ensures that the virtual column values reflect the most current field values.

The After value also includes all field values that are computed by Google Sheets, Excel, or SmartSheet worksheet formulas. This allows you to display or reference the field values that were computed by these worksheet formulas. We support this by re-reading the Added or Updated row after the Google Sheets, Excel, or SmartSheet provider has recomputed its worksheet formulas.

When used in an automation, if a bot invokes any Data Change Actions, the effects of these Data Change Actions are not reflected in the After value. The After value only reflects the changes made by the add or update that triggered the bot. However, the effects of all Data Change Actions are reflected in the current field value. In summary:

1.  You can compare the Before and After values to see the changes made by the update that triggered the bot.

2.  You can compare the Before and current `[FieldName]` values to see all changes including both the update that triggered the bot and all subsequent Data Change Actions.

## Use the Before and After values in an automation

You can use the Before and After values in an automation the following ways:

- You can display the Before and After values in the Body template and Attachment template.
- You can display the Before and After values in the Body, Subject, PreHeader, From Display, and Attachment Name properties.
- You can use the Before and After values in `<<If>>` expressions in the Body template and Attachment template. This allows you to conditionally include or exclude portions of the template depending on the Before and After values.
- You can use the Before and After values in the **IF THIS IS TRUE** expression to control whether the bot is triggered. This is often used to trigger a bot when a field's value is changed, or is changed to a specific value.

### Limitations

Your bot can only see the Before and After values of the record that triggered it. You cannot see the Before and After values for the child records of the updated record.

This limitation exists because AppSheet performs each record update independently. For example, if you update a parent record and one of its child records, AppSheet performs two independent updates. One update affects the parent record. A second independent update affects the child record. The bot invoked when the parent record is updated, can't see the Before and After values of the child record update.

If you define a bot for the child record, it can see the Before and After values of the child record that triggered it. However, it can't see the Before and After values of its parent record.

## Display the Before value of a column

When a record is updated, you can display the Before value of a column. For example, to display the Before value of the `Priority` column in your template:

    The old value of the Priority columns was <<[_THISROW_BEFORE].[Priority]>>

## Display the After value of a column

When a record is updated, you can display the After value of a column. For example, to display the After value of the `Priority` column in your template.

    The new value of Priority is <<[_THISROW_AFTER].[Priority]>>

## Display the Before and After values of a column

You can display both the Before and After values of a column to show how the column's value has changed. For example, your template can include:

    The old Priority value was <<[_THISROW_BEFORE].[Priority]>> and the new Priority value is << [_THISROW_AFTER].[Priority]>>

## Compare the Before and After values of a column

You can compare the Before and After values of a column to determine if the column's value has changed. For example, you can trigger a data change when the Before and After value of the `Priority` column has changed by specifying the following **Condition** property:

    [_THISROW_BEFORE].[Priority] <> [_THISROW_AFTER].[Priority]

## Check for specific Before or After values

You can check for specific Before or After values. For example, you can trigger a data change when the After value of the `Priority` column is `High` by specifying the following **Condition** property:

    AND([_THISROW_AFTER].[Priority] = "High", [_THISROW_BEFORE].[Priority] <> [_THISROW_AFTER].[Priority])
