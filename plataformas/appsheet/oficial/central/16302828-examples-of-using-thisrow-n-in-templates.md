---
fonte: https://support.google.com/appsheet/answer/16302828?hl=en
baixado: 2026-11-10
---

# Examples of using [_THISROW-n] in templates

The following example shows how to use `[_THISROW-n]` to access columns in child and grandparent records. See also [Use Start expressions in templates](https://support.google.com/appsheet/answer/11541779).

#### Template

The following template example filters the `Grandchild` records based on a condition that is determined using a value in the `Child` row. Let’s assume we have a number column`[Top]` in the `Child` table that determines how many `Grandchild` records to select.

`<<Start: [Related Children]>> <<[Child]>>`

|                                                                                            |                 |                      |                           |
|--------------------------------------------------------------------------------------------|-----------------|----------------------|---------------------------|
| **ID**                                                                                     | **Created**     | **ParentID/ChildID** | **Child**                 |
| `<<Start: SELECT([Related Grandchildren][ID],[OrderNumber]<=[_THISROW-1].[Top])>><<[ID]>>` | `<<[Created]>>` | `<<[ChildID]>>`      | `<<[Grandchild]>><<End>>` |

`<<End>>`

#### Result

Note that the `SELECT()` expression is using `[_THISROW-1]` to reference the `Top` column in the `Child` table. If you use `[_THISROW`\], it would refer to the `Top` column in the `Parent` table, which doesn’t exist.
