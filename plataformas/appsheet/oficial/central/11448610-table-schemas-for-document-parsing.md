---
fonte: https://support.google.com/appsheet/answer/11448610?hl=en
baixado: 2026-11-10
---

# Table schemas for document parsing

For document extraction to work properly, the table schemas for document parsing must match the content fields to be extracted. As a result, the tables schemas for document parsing are immutable and can't be altered by app editors.

A user may still edit the UX of the table views to suit their needs but must ensure that required fields are present for the creation of entries into these tables.

The following sections summarize the schemas for the tables that are generated during document processing, based on the document type.

- [Invoice table summary](#invoice)

- [Receipt table summary](#receipt)

- [W-9 Form table summary](#w-9)

- [Line items table summary](#line-items)

## **Invoice table summary**

The following table summarizes the information extracted for each **invoice**.

|                    |            |                               |            |
|--------------------|------------|-------------------------------|------------|
| **Column**         | **Format** | **Column**                    | **Format** |
| `_RowNumber`       | Number     | `Supplier Address`            | Text       |
| `_ID`              | Text       | `Receiver Name`               | Text       |
| `File`             | File       | `Receiver Address`            | Text       |
| `Invoice Number`   | Text       | `Ship To Name`                | Text       |
| `Invoice Date`     | Date       | `Ship To Address`             | Text       |
| `Total Amount`     | Decimal    | `Remit to Name`               | Text       |
| `Net Amount`       | Decimal    | `Remit to Address`            | Text       |
| `Total Tax Amount` | Decimal    | `Carrier`                     | Text       |
| `Currency Code`    | Text       | `Delivery Date`               | Text       |
| `Purchase Order`   | Text       | `Supplier Tax Id`             | Text       |
| `Due Date`         | Date       | `Customer Tax Id`             | Text       |
| `Payment Terms`    | Text       | `Related receipts_line_items` | List       |
| `Supplier Name`    | Text       |                               |            |

## **Receipt table summary**

The following table summarizes the information extracted for each **receipt**.

|                 |            |                                          |            |
|-----------------|------------|------------------------------------------|------------|
| **Column**      | **Format** | **Column**                               | **Format** |
| `_RowNumber`    | Number     | `Supplier Name`                          | Text       |
| `_ID` (Key)     | Text       | `Supplier Address`                       | Text       |
| `File`          | File       | `Supplier City`                          | Text       |
| `Receipt Date`  | Date       | `Purchase Time`                          | Text       |
| `Total Amount`  | Decimal    | `Related receipts `*`name`*`_line_items` | List       |
| `Currency Code` | Text       |                                          |            |

## **W-9 Form table summary**

The following table summarizes the information extracted for each **W-9 form**.

|                 |            |                              |            |
|-----------------|------------|------------------------------|------------|
| **Column**      | **Format** | **Column**                   | **Format** |
| `_RowNumber`    | Number     | `EIN`                        | Date       |
| `_ID` (Key)     | Text       | `Federal Tax Classification` | Text       |
| `File`          | File       | `LLC Tax Classification`     | Text       |
| `Name`          | Text       | `Exempt FATCA Code`          | Text       |
| `Address`       | Text       | `Exempt Payee Code`          | Text       |
| `City`          | Text       | `Account Numbers`            | Text       |
| `State`         | Text       | `Form Revision Date`         | Text       |
| `Zip`           | Text       | `Has Signature`              | Yes/No     |
| `Business Name` | Text       | `Has Signature Date`         | Yes/No     |
| `SSN`           | Text       |                              |            |

## **Line items table summary**

The following table summarizes the information extracted for each **line item** in an **invoice** or **receipt**.

|                |            |              |
|----------------|------------|--------------|
| **Column**     | **Format** | **Notes**    |
| `_RowNumber`   | Number     |              |
| `_ID`          | Ref        |              |
| `Amount`       | Decimal    |              |
| `Description`  | Text       |              |
| `Product Code` | Text       |              |
| `Unit Price`   | Decimal    | Invoice only |
| `Quantity`     | Number     | Invoice only |
| `Unit`         | Text       | Invoice only |
