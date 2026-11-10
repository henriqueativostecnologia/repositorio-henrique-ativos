---
fonte: https://support.google.com/docs/answer/62754?hl=en
baixado: 2026-11-10
---

# Search and use find and replace

This article has different instructions for each platform/version: Computer, Android phone & tablet, iPhone & iPad. All versions are copied below.

## Version: Computer

You can find and replace words in a document, spreadsheet, or presentation with Google Docs, Sheets, and Slides. You can also search within a file using the keyboard shortcut **Ctrl + f** (**⌘ + f** on a Mac).

### Use find and replace in a document or presentation

1.  On your computer, open a document or presentation in [Google Docs](https://docs.google.com) or [Google Slides](https://slides.google.com).
2.  Click **Edit** and then **Find and replace**.
3.  Next to "Find," type the word you want to find. If you want to replace the word, enter the new word next to "Replace with."
4.  To see the next time the word is used, click **Next**. To go back to the previous word, click **Prev**.
5.  Optional: Narrow your search by using an option below.
    - **Match case**: Matches only words with the same capitalization.
    - **Match using regular expressions**: In Google Docs, matches words based on regular expressions.
6.  To replace the highlighted word, click **Replace**. To replace the word every time it’s used, click **Replace all**.

### Use find and replace in a spreadsheet

1.  On your computer, open a spreadsheet in [Google Sheets](http://google.com/sheets).
2.  Click **Edit** and then **Find and replace**.
3.  Next to "Find," type the word you want to find, If you want to replace the word, enter the new word next to "Replace with."
4.  To search for the word, click **Find**. To see the next time the word is used, click **Find** again.
5.  Optional: Narrow your search by using an option below.
    - **Match case**: Makes your search case-sensitive.
    - **Match entire cell contents**: Searches for cells that are an exact match.
    - **Search using regular expressions**: Searches for cells that match a pattern.
    - **Also search within formulas**: Searches include formulas.
6.  To replace the highlighted word, click **Replace**. To replace the word every time it’s used, click **Replace all**.

### Find and replace items using regular expressions

You can find and replace strings of text, including characters, numbers, words, or patterns with regular expressions in [Google Docs](https://docs.google.com) and [Sheets](http://google.com/sheets).

#### Find words using regular expressions

1.  On your computer, open a document or spreadsheet in [Google Docs](https://docs.google.com) or [Google Sheets](http://google.com/sheets)
2.  Click **Edit** and then **Find and replace**.
3.  Next to "Find," type the expression and click **Search using regular expressions** or **Match using regular expressions**.
4.  Click **Find**.

When you use Find and replace, your results may change based on which boxes are checked. The examples below are with "Match case" checked and "Match entire cell contents" (for spreadsheets) unchecked.

##### See an example

##### Search for dollar amounts

**Note:** This example only works with Google Sheets.

- Enter into "Find": ^\\(\[0-9,\]+)?\[.\]\[0-9\]+
- This string means a dollar amount where the first number is any number 0-9 or comma occurring zero or more times, followed by \[.\], followed by any number 0-9 repeated one or more times. This search could find numbers like: \$4.666, \$17.86, \$7.76, \$.54, \$900,001.00, \$523,877,231.56.

##### Search for U.S. zip codes

- Enter into "Find": \[0-9\]{5}(-\[0-9\]{4})?
- This string represents a U.S. zip code consisting of five numbers with an optional hyphen and four-digit add-on.

##### Search for names that start with a lowercase letter

**Note:** This example only works with Google Sheets.

- Enter into "Find": ^\[a-z\].\*
- This string represents a cell with a lowercase letter followed by another character 0 or more times. This search would find: bob, jim, gEORGE, marTin.

#### Replace with regular expressions

You can replace parts of a regular expression with capture groups. You reference these capture groups in the "Replace" string using the format "\$."

**Tip:** Regular expression replacements (including capture groups and special characters like \n for newlines) only work with Google Sheets. In Google Docs, any regex formatting entered into the "Replace with" field will be inserted as literal text.

##### See an example

The expression (\d\*)/\d\*/(\d{4}) matches dates such as 3/8/2015. This expression has two capture groups.

1.  (\d\*) - Matches the month
2.  (\d{4}) - Matches the year

To replace each date matched with the above regular expression to the first date of the month, you would use the string "\$1/1/\$2." The date 3/8/2015 would be replaced with 3/1/2015.

#### Regular expressions

Google products use [RE2](https://en.wikipedia.org/wiki/RE2_(software)) for regular expressions. You can see all of the [RE2 expressions](https://github.com/google/re2/blob/master/doc/syntax.txt) on GitHub.

If you want to search for a character that has a meaning in regular expressions, such as \$, put a backslash in front of it. For example, to search for the \$ character, you'd write \\.

##### Common regular expressions

+-------------------------------+-------------------------------+-------------------------------+-------------------------------+-------------------------------+
| Expression                    | Description                   | Example                       | Matches                       | Does not match                |
+===============================+===============================+===============================+===============================+===============================+
| .                             | A period represents any       | d\.                           | do, dog, dg, ads              | fog, jog                      |
|                               | character in the given        |                               |                               |                               |
|                               | position.                     |                               |                               |                               |
+-------------------------------+-------------------------------+-------------------------------+-------------------------------+-------------------------------+
| \*                            | An asterisk after a character | do\*g                         | dog, dg, dooog                | dOg, doug                     |
|                               | represents a search for that  |                               |                               |                               |
|                               | preceding character repeated  |                               |                               |                               |
|                               | 0 or more times.              |                               |                               |                               |
+-------------------------------+-------------------------------+-------------------------------+-------------------------------+-------------------------------+
| \+                            | A plus after a character      | do+g                          | dog, dooog                    | dg, dOg, doug                 |
|                               | represents a search for that  |                               |                               |                               |
|                               | character displayed 1 or more |                               |                               |                               |
|                               | times.                        |                               |                               |                               |
+-------------------------------+-------------------------------+-------------------------------+-------------------------------+-------------------------------+
| ?                             | The previous expression is    | do?g                          | dg, dog                       | dOg, doug                     |
|                               | optional.                     |                               |                               |                               |
+-------------------------------+-------------------------------+-------------------------------+-------------------------------+-------------------------------+
| \^                            | A caret must be placed at the | \^\[dh\]og                    | dog, hog                      | A dog, his hog                |
|                               | beginning of a regular        |                               |                               |                               |
|                               | expression. It signifies the  |                               |                               |                               |
|                               | string starts with the        |                               |                               |                               |
|                               | character(s) or sequence      |                               |                               |                               |
|                               | placed after the caret.       |                               |                               |                               |
|                               |                               |                               |                               |                               |
|                               | **Note:** This regular        |                               |                               |                               |
|                               | expression only works with    |                               |                               |                               |
|                               | Google Sheets.                |                               |                               |                               |
+-------------------------------+-------------------------------+-------------------------------+-------------------------------+-------------------------------+
| \$                            | A dollar sign must be placed  | \[dh\]og\$                    | dog, hog, hot dog             | dogs, hogs, doggy             |
|                               | at the end of a regular       |                               |                               |                               |
|                               | expression and signifies that |                               |                               |                               |
|                               | the string ends with the      |                               |                               |                               |
|                               | character(s) or sequence      |                               |                               |                               |
|                               | placed before the dollar      |                               |                               |                               |
|                               | sign.                         |                               |                               |                               |
|                               |                               |                               |                               |                               |
|                               | **Note:** This regular        |                               |                               |                               |
|                               | expression only works with    |                               |                               |                               |
|                               | Google Sheets.                |                               |                               |                               |
+-------------------------------+-------------------------------+-------------------------------+-------------------------------+-------------------------------+
| {A, B}                        | The previous expression is    | d(o{1,2})g                    | dog, doog                     | dg, dooog, dOg                |
|                               | repeated between A and B      |                               |                               |                               |
|                               | times, where A and B are      |                               |                               |                               |
|                               | numbers.                      |                               |                               |                               |
+-------------------------------+-------------------------------+-------------------------------+-------------------------------+-------------------------------+
| \[x\], \[xa\], \[xa5\]        | A character set indicates     | d\[ou\]g                      | dog, dug                      | dg, dOg, dooog                |
|                               | that just one of the given    |                               |                               |                               |
|                               | character(s) should occur in  |                               |                               |                               |
|                               | the current position.         |                               |                               |                               |
|                               | Usually, any characters are   |                               |                               |                               |
|                               | valid within brackets,        |                               |                               |                               |
|                               | including characters          |                               |                               |                               |
|                               | mentioned previously in       |                               |                               |                               |
|                               | expressions: \[xa,\$5Gg.\]    |                               |                               |                               |
+-------------------------------+-------------------------------+-------------------------------+-------------------------------+-------------------------------+
| \[a-z\]                       | A character set range         | d\[o-u\]g                     | dog, dug, dpg, drg            | dg, dOg, dag                  |
|                               | signifies a search for a      |                               |                               |                               |
|                               | character within the given    |                               |                               |                               |
|                               | range of characters. Common   |                               |                               |                               |
|                               | ranges include a-z, A-Z, and  |                               |                               |                               |
|                               | 0-9. Ranges can be combined   |                               |                               |                               |
|                               | into a single range:          |                               |                               |                               |
|                               | \[a-zA-Z0-9\]. Ranges can     |                               |                               |                               |
|                               | also be combined with         |                               |                               |                               |
|                               | character sets (mentioned     |                               |                               |                               |
|                               | previously): \[a-zA-Z,&\*\].  |                               |                               |                               |
+-------------------------------+-------------------------------+-------------------------------+-------------------------------+-------------------------------+
| \[\^a-fDEF\]                  | A character set beginning     | d\[\^aeu\]g                   | dog, dOg, dig, d\$g           | dg, dag, deg, dug             |
|                               | with a \^ signifies a search  |                               |                               |                               |
|                               | for a character that is not   |                               |                               |                               |
|                               | within the given set.         |                               |                               |                               |
+-------------------------------+-------------------------------+-------------------------------+-------------------------------+-------------------------------+
| \\s                           | Any white-space character.    | d\\sg                         | d g, d\[TAB\]g                | dg, dog,                      |
+-------------------------------+-------------------------------+-------------------------------+-------------------------------+-------------------------------+

## Version: Android phone & tablet

You can find and replace words in a document, spreadsheet, or presentation with Google Docs, Sheets, and Slides. You can also search within a file using the keyboard shortcut **Ctrl + f** (**⌘ + f** on a Mac).

### Use find and replace in a document

1.  On your Android phone or tablet, open a document in the [Google Docs app](https://play.google.com/store/apps/details?id=com.google.android.apps.docs.editors.docs).
2.  Tap More More   and then **Find and replace**.
3.  Type the word you want to find.
4.  Tap Search Search .
5.  To see every time the word is used, in the top right, tap the arrows.
    - **Replace a single word:** Tap More More and then  **Replace**. Then type the replacement and tap **Replace**.
    - **Replace a word every time it's used:** Tap More More and then ** Replace all**. Then type the replacement and tap **Replace all**.
6.  To return to the document, tap Done Done .

### Use find and replace in a spreadsheet

1.  On your Android phone or tablet, open a spreadsheet in the [Google Sheets app](https://play.google.com/store/apps/details?id=com.google.android.apps.docs.editors.sheets).
2.  Tap More More   and then **Find and replace**.
3.  Type the word you want to find.
4.  Tap Search Search .
5.  To see every time the word is used, in the top right, tap the arrows.
6.  To replace the word, tap **Replace with**.
7.  Type the replacement and tap **Replace** or **Replace all**.
8.  To return to the spreadsheet, tap Done Done .

## Version: iPhone & iPad

You can find and replace words in a document, spreadsheet, or presentation with Google Docs, Sheets, and Slides. You can also search within a file using the keyboard shortcut **Ctrl + f** (**⌘ + f** on a Mac).

### Use find and replace in a document

1.  On your iPhone or iPad, open a document in the [Google Docs app](https://itunes.apple.com/app/google-docs/id842842640?mt%3D8).
2.  Tap More   and then **Find and replace**.
3.  Type the word you want to find.
4.  Tap **Search**.
5.  To see and scroll through every time the word is used, use the arrows at the top of the screen.
6.  To replace the word, tap **Replace with**.
    - To replace a single word, tap **Replace**.
    - To replace every time the word is used, tap **All**.
7.  To return to the document, tap Close  Close .

### Use find and replace in a spreadsheet

1.  On your iPhone or iPad, open a spreadsheet in the [Google Sheets app](https://itunes.apple.com/app/apple-store/id842849113?pt=9008&ct=sheets_hc&mt=8).
2.  Tap More   and then **Find and replace**.
3.  Type the word you want to find.
4.  Tap **Search**.
5.  To see every time the word is used, in the top right, tap the arrows.
6.  To replace the word, tap **Replace with**.
    - To replace a single word, tap **Replace**.
    - To replace every time the word is used, tap **All**.
7.  To return to the spreadsheet, tap Close  Close .
