---
fonte: https://support.google.com/appsheet/answer/10107397?hl=en
baixado: 2026-11-10
---

# Configure suggested values for a column

Every column input in a form can prompt the user with a list of suggested values. For example, a column `Industry` of type `Text` could have `Tech`, `Media` and `Construction` as suggested values. 

The list of suggested values is optionally defined by an expression in the column definition. The expression could be a constant (such as, `LIST("Tech", "Media")`) or a dynamic expression (such as, `SELECT(LookupTable[Option], [Category] = [_THISROW].[Category]`).

**Note**: The suggested values constraint is a "soft" constraint: the list is not meant to be exhaustive or constraining. The user will be able to enter any other value that conforms to the column type (and the [Valid_If](https://support.google.com/appsheet/answer/10107949) constraint if one has been defined).
