---
fonte: https://support.google.com/appsheet/answer/16279304?hl=en
baixado: 2026-11-10
---

# Examples of using Start expressions in templates

The template examples demonstrate how the placement of the `Start` and `End` expressions can impact the table formatting or even result in errors. The scenarios used in the template examples consists of an app that has three related tables: `Parent`, `Child`, and `Grandchild`

See also [Use Start expressions in templates](https://support.google.com/appsheet/answer/11541779).

------------------------------------------------------------------------

[Expand all](#expand)** ** \|** **[Collapse all](https://support.google.com/appsheet/answer/16279304)

#### Example 1: Start and End expressions are inside of the table

#### Template

The `Start` and `End` expressions are inside of the table.

|                                         |                 |                  |                      |
|-----------------------------------------|-----------------|------------------|----------------------|
| **ID**                                  | **Created**     | **ParentID**     | **Child**            |
| `<<Start: [Related Children]>><<[ID]>>` | `<<[Created]>>` | `<<[ParentID]>>` | `<<[Child]>><<End>>` |

#### Result 

Generates the header row and multiple rows for each `Child` record.

|            |                         |              |            |
|------------|-------------------------|--------------|------------|
| **ID**     | **Created**             | **ParentID** | **Child**  |
| `ff8844ce` | `5/13/2025 12:11:18 PM` | `795954c3`   | `Child A1` |
| `0a4f4a3d` | `5/13/2025 12:11:29 PM` | `795954c3`   | `Child A2` |
| `258218bc` | `5/13/2025 12:11:42 PM` | `795954c3`   | `Child A3` |

#### Example 2: Start and End expressions are outside of the table

#### Template

The `Start` and `End` expressions are outside of the table.

`<<Start: [Related Children]>>`

|            |                 |                  |               |
|------------|-----------------|------------------|---------------|
| **ID**     | **Created**     | **ParentID**     | **Child**     |
| `<<[ID]>>` | `<<[Created]>>` | `<<[ParentID]>>` | `<<[Child]>>` |

`<<End>>`

#### Result

Generates the header row and multiple rows for each `Child` record.

|            |                         |              |            |
|------------|-------------------------|--------------|------------|
| **ID**     | **Created**             | **ParentID** | **Child**  |
| `ff8844ce` | `5/13/2025 12:11:18 PM` | `795954c3`   | `Child A1` |
| **ID**     | **Created**             | **ParentID** | **Child**  |
| `0a4f4a3d` | `5/13/2025 12:11:29 PM` | `795954c3`   | `Child A2` |
| **ID**     | **Created**             | **ParentID** | **Child**  |
| `258218bc` | `5/13/2025 12:11:42 PM` | `795954c3`   | `Child A3` |

To add additional space between the tables, add a blank line after the last `End` expression.

#### Example 3: Start expression is outside of the table and End expression is inside of the table

#### **Template** 

The `Start` expression is outside of the table and the `End` expression is inside of the table.

`<<Start: [Related Children]>>`

+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| **ID**                                | **Created**                           | **ParentID**                          | **Child**                             |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+
| `<<[ID]>>`                            | `<<[Created]>>`                       | `<<[ParentID]>>`                      | `<<[Child]>>`\                        |
|                                       |                                       |                                       | `<<End>>`                             |
+---------------------------------------+---------------------------------------+---------------------------------------+---------------------------------------+

 

#### **Result**

AppSheet throws an error, which you can view in the [Audit History](https://support.google.com/appsheet/answer/10104794).

`Expression 'End' is invalid due to: Constant text \"END\" should not be wrapped in \"<<\" \">>\".`

#### Example 4: Start expression is inside of the table and End expression is outside of the table

#### Template

The `Start` expression is inside of the table and the `End` expression is outside of the table.

|                                         |                 |                  |               |
|-----------------------------------------|-----------------|------------------|---------------|
| **ID**                                  | **Created**     | **ParentID**     | **Child**     |
| `<<Start: [Related Children]>><<[ID]>>` | `<<[Created]>>` | `<<[ParentID]>>` | `<<[Child]>>` |

`<<End>>`

#### Result

AppSheet throws an error, which you can view in the [Audit History](https://support.google.com/appsheet/answer/10104794).

`Expression '[ParentID]' is invalid due to: Can't find column \"ParentID\". Did you mean \"Parent\"?. Error: Task 'New step' Attachment template. Expression '[Child]' is invalid due to: Can't find column \"Child\". Did you mean \"ID\"?."`

#### Example 5: Two Start and End expressions inside of the same table

#### Template

Two `Start` and `End` expressions inside of the same table.

|                                              |                 |                  |                           |
|----------------------------------------------|-----------------|------------------|---------------------------|
| **ID**                                       | **Created**     | **ParentID**     | **Child**                 |
| `<<Start: [Related Children]>><<[ID]>>`      | `<<[Created]>>` | `<<[ParentID]>>` | `<<[Child]>>`             |
| `<<Start: [Related Grandchildren]>><<[ID]>>` | `<<[Created]>>` | `<<[ChildID]>>`  | `<<[Grandchild]>><<End>>` |
|                                              |                 |                  | `<<End>>`                 |

#### Result

AppSheet throws an error, which you can view in the [Audit History](https://support.google.com/appsheet/answer/10104794).

`Expression '[ParentID]' is invalid due to: Can't find column \"ParentID\". Did you mean \"Parent\"?. Error: Task 'New step' Attachment template. Expression '[Child]' is invalid due to: Can't find column \"Child\". Did you mean \"ID\"?. Error: Task 'New step' Attachment template. Expression '[Related Grandchildren]' is invalid due to: Can't find column \"Related Grandchildren\". Did you mean \"Related Children\"?.",`

#### Solution

To resolve this error, you need to place the `Child` table’s `Start` and `End` expressions outside of the table, as shown. With this solution, the `Child` and its `Grandchild` records are included in the same table.

`<<Start: [Related Children]>>`

|                                              |                 |                      |                           |
|----------------------------------------------|-----------------|----------------------|---------------------------|
| **ID**                                       | **Created**     | **ParentID/ChildID** | **Child**                 |
| `<<[ID]>>`                                   | `<<[Created]>>` | `<<[ParentID]>>`     | `<<[Child]>>`             |
| `<<Start: [Related Grandchildren]>><<[ID]>>` | `<<[Created]>>` | `<<[ChildID]>>`      | `<<[Grandchild]>><<End>>` |

`<<End>>` 

Because the first `Start` and `End` expressions are outside of the table, it creates a table for each `Child`, as follows:

|            |                         |                      |                   |
|------------|-------------------------|----------------------|-------------------|
| **ID**     | **Created**             | **ParentID/ChildID** | **Child**         |
| `ff8844ce` | `5/13/2025 12:11:18 PM` | `795954c3`           | `Child A1`        |
| `asdqwe34` | `5/13/2025 12:11:18 PM` | `ff8844ce`           | `Grandchild A1.1` |
| `dfgmnb19` | `5/13/2025 12:11:29 PM` | `ff8844ce`           | `Grandchild A1.2` |
| `jfndkm44` | `5/13/2025 12:11:42 PM` | `ff8844ce`           | `Grandchild A1.3` |

|            |                         |                      |            |
|------------|-------------------------|----------------------|------------|
| **ID**     | **Created**             | **ParentID/ChildID** | **Child**  |
| `0a4f4a3d` | `5/13/2025 12:11:29 PM` | `795954c3`           | `Child A2` |

|            |                         |                      |            |
|------------|-------------------------|----------------------|------------|
| **ID**     | **Created**             | **ParentID/ChildID** | **Child**  |
| `258218bc` | `5/13/2025 12:11:42 PM` | `795954c3`           | `Child A3` |

To add additional space between the tables, add a blank line after the last `End` expression.

#### Example 6: Child record is outside of the table and Grandchild records are inside of the table

#### Template

The `Child` record and its data are outside of the table and only `Grandchild` records are inside of the table.

`<<Start: [Related Children]>> <<[Child]>>`

|                                         |                 |                      |                           |
|-----------------------------------------|-----------------|----------------------|---------------------------|
| **ID**                                  | **Created**     | **ParentID/ChildID** | **Child**                 |
| `<<Start: [Related Children]>><<[ID]>>` | `<<[Created]>>` | `<<[ChildID]>>`      | `<<[Grandchild]>><<End>>` |

`<<End>>`

#### Result

Generates three separate tables, as shown. Two `Child` tables are blank (only the header) because those two `Child` records don’t have any `Grandchild` records.

**Child A1 **

|            |                         |                      |                     |
|------------|-------------------------|----------------------|---------------------|
| **ID**     | **Created**             | **ParentID/ChildID** | **Child**           |
| `asdqwe34` | `5/13/2025 12:11:18 PM` | `ff8844ce`           | `Grandc``hild A1.1` |
| `dfgmnb19` | `5/13/2025 12:11:29 PM` | `ff8844ce`           | `Grandchild A1.2`   |
| `jfndkm44` | `5/13/2025 12:11:42 PM` | `ff8844ce`           | `Grandchild A1.3`   |

**Child A2 **

|        |             |                      |           |
|--------|-------------|----------------------|-----------|
| **ID** | **Created** | **ParentID/ChildID** | **Child** |

**Child A3** 

|        |             |                      |           |
|--------|-------------|----------------------|-----------|
| **ID** | **Created** | **ParentID/ChildID** | **Child** |

 

If you would like to remove the empty `Child` tables, you can write the `Start` expression using `SELECT()` and filter the `Child` records that don’t have any `Grandchild` records. 

`<<Start: SELECT([Related Children][ID],ISNOTBLANK([Related Grandchildren]))>> <<[Child]>>`

|                                         |                 |                      |                           |
|-----------------------------------------|-----------------|----------------------|---------------------------|
| **ID**                                  | **Created**     | **ParentID/ChildID** | **Child**                 |
| `<<Start: [Related Children]>><<[ID]>>` | `<<[Created]>>` | `<<[ChildID]>>`      | `<<[Grandchild]>><<End>>` |

`<<End>>`

Generates the table with `Child` records.

|            |                         |                      |                   |
|------------|-------------------------|----------------------|-------------------|
| **ID**     | **Created**             | **ParentID/ChildID** | **Child**         |
| `asdqwe34` | `5/13/2025 12:11:18 PM` | `ff8844ce`           | `Grandchild A1.1` |
| `dfgmnb19` | `5/13/2025 12:11:29 PM` | `ff8844ce`           | `Grandchild A1.2` |
| `jfndkm44` | `5/13/2025 12:11:42 PM` | `ff8844ce`           | `Grandchild A1.3` |
