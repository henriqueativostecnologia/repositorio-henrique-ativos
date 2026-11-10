---
fonte: https://support.google.com/appsheet/answer/10104377?hl=en
baixado: 2026-11-10
---

# Sensitive Personally Identifiable Information (PII) data policy

If your app processes personal or sensitive data, you can mark it as containing Personally Identifiable Information (or PII), which will prevent it from being retained in the system logs. You can do this either on per-column or per-app basis.

## App-level setting

In the app editor, under the **Security \> Options** tab, enable the **Treat all data columns as Sensitive** property. This will override and disable the column-level setting, and will automatically treat all columns and data in the app as sensitive, no longer logging it in the app audit history, instead writing the value `_PII_` to the cell.

## Column-level setting

When the app-level **Treat all data columns as Sensitive** setting is disabled, you can designate specific columns as containing sensitive data or PII.

To mark a column as PII, select **Data \> Columns**, expand the table, and enable the **PII? **toggle for the column.

Once correctly configured, if you update a record with a PII column, its data will not be logged in our system or shown in your audit log. They simply get passed along to the back-end source of data.

We recommend you evaluate all of the safeguards and features that the AppSheet platform includes in order to decide if these features meet your compliance criteria.
