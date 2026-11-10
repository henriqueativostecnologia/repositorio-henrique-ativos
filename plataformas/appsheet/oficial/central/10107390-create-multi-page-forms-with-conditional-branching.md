---
fonte: https://support.google.com/appsheet/answer/10107390?hl=en
baixado: 2026-11-10
---

# Create multi-page forms with conditional branching

You might want to break up a long input form into several pages for convenience. In some apps, it makes sense to conditionally show or hide a specific page based on choices made earlier. For example, in a form for a vehicle inspection report, you may have an initial question asking if there is damage. If the answer is Yes, you may want to show a Form page that has specific questions about the damage. If the answer is No, you would want to skip that page.

## Conditional branching in Google Forms

When you are building your app from a Google Form, use **Add Item \> Page break** to split the form into multiple pages

**Note**: You can optionally provide a page header or description. This is helpful to remember where you're directing respondents and helping respondents understand your form's structure.

You can then add **Multiple choice** or **Choose from a list** items with the option **Go to page based on answer** and choose different navigation paths for each option. Often you will also want these conditional branching questions to be marked as required.

At each page break, you can also choose where the form should go next. Keep in mind that the page break navigation will only take effect under certain circumstances:

1.  When the page has no conditional branching questions
2.  When conditional branching questions are not required and no answer is given
3.  When **Continue to next page** is chosen for specific answers to branching questions

After setting up your form, start the [AppSheet add-on](https://workspace.google.com/marketplace/app/appsheet/865237847665) and click **Prepare**. The AppSheet add-on creates page header columns in your response spreadsheet to represent each page break and automatically converts the form's "go-to-page" navigation into AppSheet's `Show_If` expression model. The page header columns appear in AppSheet as [Show](https://support.google.com/appsheet/answer/10106435#show) type columns, meaning they affect the visual presentation of forms. The settings for these columns specifies the **Category** as `Page_Header`. You can examine the [column structure](https://support.google.com/appsheet/answer/10106674#column-structure).

Most forms can now be correctly converted to AppSheet apps automatically, but there are two main limitations:

1.  Reverse navigation is not supported by AppSheet. Try to arrange your form such that all navigation proceeds to higher page numbers.
2.  In Google Forms you can include a special **Other** option for multiple choice questions and assign it specific navigation behavior. However, the navigation associated with this choice is not made available to the AppSheet add-on. We recommend avoiding use of **Other** on questions where **Go to page based on answer** is enabled.

For more information about the conversion from Google Forms to AppSheet, see [Use data from Google Forms](https://support.google.com/appsheet/answer/10106596). 

## Conditional branching in your spreadsheet and the editor

When you are building your form app from a spreadsheet, insert an empty column at each point where you'd like a page break in the form. 

While conditional branching in Google Forms is based on a "go-to-page" navigation model, AppSheet uses a `Show_If` model to describe whether a given page should be shown or hidden. By default, pages are always shown. To make a page appear conditionally:

1.  Open the app in the editor.
2.  Go to **Data**  and select the table you want to edit in the list.
    We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
    You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

     
    ## If you are using the legacy editor

    Go to **Data**, click **Columns**, and expand the table you want to edit.
3.  Find the corresponding Page Header in the table (the empty page-break columns in the spreadsheet are treated within AppSheet as [Show](https://support.google.com/appsheet/answer/10106435#show) type fields with `Page_Header` Category. 
4.  Click **Edit** (pencil icon) associated with the column.
5.  Create an [expression](https://support.google.com/appsheet/answer/10104642) in the **Show If** field that defines when the page should be shown.

**Example:**

Suppose you have an `Enum` (drop-down) on the first page called **Cat or dog person?** with choices **Cat** and **Dog**, and you have page breaks for an About Cats page and an About Dogs page.

The About Cats page can be shown only when Cat is selected by setting the **Show If** field for the page header column to the expression: `[Cat or dog person?]="Cat"`

Likewise the About Dogs page can be shown only when Dog is selected by setting the **Show If** field for the page header column to the expression: `[Cat or dog person?]="Dog"`

## Which should I use?

Auto-generating your app from a Google Form with the [AppSheet add-on](https://workspace.google.com/marketplace/app/appsheet/865237847665) is often easier and more convenient, since the add-on takes care of building the `Show_If` expressions for you. However, if your form requires complex navigation conditions that depend on multiple fields, you may not be able to represent it with Google's "go-to-page" model. 

Creating your own `Show_If` expressions in the editor gives you more freedom to define complex composite or comparison conditions that can't be represented in Google Forms using functions like `AND`, `OR`, `NOT`, and so on.
