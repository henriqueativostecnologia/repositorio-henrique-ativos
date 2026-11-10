---
fonte: https://support.google.com/appsheet/answer/11539253?hl=en
baixado: 2026-11-10
---

# Use variables in templates

You can use the following types of variables in your templates:

- [Column name variables](#column-name)
- [Expression variables](#expression)
- [Built-in variables](#built-in-variables)

When using variables within an HTML block, they must be HTML encoded. For example, the **\<** character is HTML encoded as **&lt;** and the **\>** character is HTML encoded as **&gt;**. For example `<<[Order Number]>>` must be specified as: 
`<html>`

`...`

`&lt;&lt;[Order Number]&gt;&gt;`

`...`

`</html>`

## Column name variables

Column name variables allow you to display or retrieve the value of a data column. The column name must exactly match the column name in your table and be enclosed in square brackets. The column name variable is replaced by the value of that column.

For example, to display the value of the `Order Number` column in your email template:

    Order Number is <<[Order Number]>>

**Note**: When a data column value is displayed in an HTML document, it is always HTML encoded. See [Prevent cross-site scripting attacks using HTML encoding](#prevent-cross-site-scripting-attacks).

You can also display the value of a column both [before and after](https://support.google.com/appsheet/answer/11547057) it is updated.

## Expression variables

Expression variables allow you to compute values. You can use any [expression](https://support.google.com/appsheet/answer/10104642) in an expression variable. The expression variable is replaced by the result of the expression's evaluation.

For example, you can display the result of the `Amt` column value times the `Qty` column value as follows:

    <<[Amt] * [Qty]>>

**Dereference expression variables**

Use a [dereference expression](https://support.google.com/appsheet/answer/10107396) to display the value of a column in a referenced record using the following format:

    [Column Containing Reference].[Column in Referenced Table]

For example, the following expression retrieves the product's price from the `Products` table:

    <<[Product].[Price]>>

In this example, `Product` is the name of a column of type `Ref` in the `Order Details` table that refers to the `Products` table. `Price` is the name of the column in the `Products` table that contains the product's price.

You can use dereference expressions when computing values. For example:

    Total Amount: <<[Product].[Price] * [Quantity]>>

## Built-in variables

Built-in variables enable you to access a set of values provided by AppSheet. Built-in variable names always begin with an underscore (\_).

Built-in variables can be used only in templates and when configuring certain automation properties, such as an [email](https://support.google.com/appsheet/answer/11447614) or [SMS message](https://support.google.com/appsheet/answer/11509435) body. They cannot be used in expressions.

AppSheet provides the following built-in variables. 

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Built-in variable**                                                         | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| `<<_APPID>>`                                                                  | Application GUID (Globally Unique Identifier) that uniquely identifies your   |
|                                                                               | app.                                                                          |
|                                                                               |                                                                               |
|                                                                               | **Example**: \                                                                |
|                                                                               | `8c26466f-1db0-4032-9c0f-40c2a588cf50`                                        |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| `<<_APPNAME>>`                                                                | Name of your app.                                                             |
|                                                                               |                                                                               |
|                                                                               | **Example: **\                                                                |
|                                                                               | `MyApp-10301`                                                                 |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| `<<_APPOWNER>>`                                                               | Owner ID of your app.                                                         |
|                                                                               |                                                                               |
|                                                                               | **Example: **\                                                                |
|                                                                               | `10301`                                                                       |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| `<<_ATTACHMENTFILENAME>>`                                                     | Archive attachment filename. See [How the archive attachment filename is      |
|                                                                               | form                                                                          |
|                                                                               | ed](https://support.google.com/appsheet/answer/11538747#how-filename-formed). |
|                                                                               |                                                                               |
|                                                                               | **Example**:\                                                                 |
|                                                                               | `MyAttachmentName20190207_133355_804`.pdf                                     |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| `<<_ATTACHMENTFILE_URL>>`                                                     | Archive attachment file URL.                                                  |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| `<<_ATTACHMENTFILE_WEB_LINK>>`                                                | Link to the archive attachment file. The attachment name is used as the       |
|                                                                               | hyperlink text.                                                               |
|                                                                               |                                                                               |
|                                                                               |                                                                               |
|                                                                               |                                                                               |
|                                                                               | **Note**: This variable can be used in a body or attachment template. It      |
|                                                                               | cannot be used in the **Body** property.                                      |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| `<<_ATTACHMENTNAME>>`                                                         | Email attachment name.                                                        |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| `<<_ROWKEY>>`                                                                 | Key value of the added, deleted, or updated record.                           |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| `<<_ROW_WEB_LINK>>`                                                           | Link to the added or updated record in your app. For example, you can include |
|                                                                               | this URL in an email to allow the email recipient to easily open the added or |
|                                                                               | updated record.                                                               |
|                                                                               |                                                                               |
|                                                                               |                                                                               |
|                                                                               |                                                                               |
|                                                                               | **Note**: This variable can be used in a body or attachment template. It      |
|                                                                               | cannot be used in the **Body** property.                                      |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| `<<_ROW_WEB_URL>>`                                                            | URL that refers to the added or updated record in your app. For example, you  |
|                                                                               | can include this URL in an email to allow the email recipient to easily open  |
|                                                                               | the added or updated record. The full URL is displayed.                       |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| `<<_RULENAME>>`                                                               | Name of the automation component (such as, the task).                         |
|                                                                               |                                                                               |
|                                                                               | **Example**:\                                                                 |
|                                                                               | `Send an email`                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| `<<_TABLENAME>>`                                                              | Name of your table.                                                           |
|                                                                               |                                                                               |
|                                                                               | **Example**:\                                                                 |
|                                                                               | `Orders`                                                                      |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| `<<_UPDATEMODE>>`                                                             | Name of the operation that triggered the automation rule.                     |
|                                                                               |                                                                               |
|                                                                               | **Example**:\                                                                 |
|                                                                               | `Add`, `Delete`, or `Update`                                                  |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

## Prevent cross-site scripting attacks using HTML encoding

AppSheet always HTML encodes field values when they are displayed in an HTML document. HTML encoding ensures that field values are displayed as simple text by the browser and that field values are not interpreted by the browser as HTML. This is essential to prevent [Cross-site Scripting](https://en.wikipedia.org/wiki/Cross-site_scripting) (XSS) attacks when a user enters JavaScript in a field, such as:

    <script type="text/javascript">
        function doSomethingEvil() { /* ... */ }
    </script>
