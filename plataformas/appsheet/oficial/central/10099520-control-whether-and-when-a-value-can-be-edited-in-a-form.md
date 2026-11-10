---
fonte: https://support.google.com/appsheet/answer/10099520?hl=en
baixado: 2026-11-10
---

# Control whether and when a value can be edited in a form

To control whether and when a value can be edited in a form, use the [Editable_If expression](https://support.google.com/appsheet/answer/10107954), which is part of the [column definition](https://support.google.com/appsheet/answer/10106674). `Editable_If` is a [column constraint](https://support.google.com/appsheet/answer/10107948) that you define by using the [**Columns**](https://support.google.com/appsheet/answer/10106674) pane of the app editor. It tells the system if a particular value of a particular row can be edited.

Some examples are provided below based on specific scenarios.

**Scenario 1**: I have a building assessment app with 10 questions. I want the fields to be editable until the user presses save.  Once saved, I want the fields to no longer be editable.

**Resolution**: Set the [Editable_If expression](https://support.google.com/appsheet/answer/10107954) to `ISBLANK([_THIS])`. This means you can edit the value only if it is blank. After the users presses save, the fields are not blank and therefore not editable.

**Scenario 2**: I have a building assessment app with 10 questions. I want the fields to be editable until the assessment is marked Complete.  Once saved, I want the fields to no longer be editable.

**Resolution**: Set the [Editable_If expression](https://support.google.com/appsheet/answer/10107954) to `NOT ([Status] = "Complete")`. 

Scenario 3: I have a building assessment app with 10 questions.  I want the fields to be editable until the assessment is marked Complete.  Once saved, I want the fields to no longer be editable by anyone other than Bob.

**Resolution**: Set the [Editable_If expression](https://support.google.com/appsheet/answer/10107954) to `OR ( NOT([Status] = "Complete"), USEREMAIL() = "bob@mydomain.com")`
