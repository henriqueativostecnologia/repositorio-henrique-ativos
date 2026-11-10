---
fonte: https://support.google.com/appsheet/answer/11572062?hl=en
baixado: 2026-11-10
---

# Troubleshoot custom fonts in templates

Troubleshoot custom fonts in your Google Docs template file, as described in the following sections:

- [How custom fonts are displayed by AppSheet](#how)
- [Verify all custom fonts are present in the HTML](#verify-all-custom-fonts-present)
- [Remove all custom fonts from your Google Docs template](#remove-all-custom-fonts)

**Note**: Some customers have reported problems when using custom fonts in templates. The PDF service sometimes fails to convert the HTML file to PDF correctly when custom fonts are present. The resulting PDF document may not display the text using the custom font. If you experience this problem, we recommend [remove all custom fonts from your Google Docs template](#remove-all-custom-fonts).

## How custom fonts are displayed by AppSheet

When you use custom fonts like `Libre Barcode 128` and `Libre Barcode 39 Extended Text`, the HTML file that is returned when AppSheet reads the Google Docs template includes an `import url` that refers to these custom fonts.

When your event fires, AppSheet does the following:

1.  Reads the Google Doc file in HTML format.
2.  Creates the attachment from the HTML template file.
3.  Converts the resulting attachment from HTML to PDF by calling the HTML-to-PDF web conversion service.

The HTML-to-PDF web conversion service relies on the HTML file containing the right `import url` value. The `import url` must refer to all of the custom fonts that you are using in your PDF attachment. If the `import url` is missing one or more of your custom fonts, the data values in the PDF attachment file are displayed in the default font rather than in the custom font. See [Verify all custom fonts are present](#verify-all-custom-fonts-present).

## Verify all custom fonts are present in the HTML

To verify that the HTML file returned by Google Doc contains the right custom fonts:

1.  Open your Google Docs template file in Google Docs.
2.  On the Google Docs **File** menu select **Download** \> **Web Page (.html zipped)**.
3.  Google Docs will export your Google Docs template file as a `.zip` file and display the zipped file name in a tab at the bottom of the browser.
4.  Click the **^** symbol to the right of the `.zip` file name in the tab at the bottom of the browser. Select **Show in Finder**.
5.  Unzip the `.zip` file to access your template in HTML format.
6.  Right click on the `.html` file, select **Rename**, and change the file extension from `.html` to `.txt`.
7.  Right click on the renamed template `.txt` file and select **Edit**.
8.  Near the top of the template file, look for `@import url`. It should look something like the following:
    `@import url('`[`https://themes.googleusercontent.com/fonts/css?kit=mJ_rGOyyL62_i4eysdBvxCC0kCcps6hmr3Uub3CurLj6HJltGXvViurXJL6xt9sxwzYVTjVaNNEx2pDT4aBU4J6Nc2zktOcTrnnZfLDyCt73rGVtsTkPsbDajuO5ue`](https://themes.googleusercontent.com/fonts/css?kit=mJ_rGOyyL62_i4eysdBvxCC0kCcps6hmr3Uub3CurLj6HJltGXvViurXJL6xt9sxwzYVTjVaNNEx2pDT4aBU4J6Nc2zktOcTrnnZfLDyCt73rGVtsTkPsbDajuO5ueQw)[Qw](https://themes.googleusercontent.com/fonts/css?kit=mJ_rGOyyL62_i4eysdBvxCC0kCcps6hmr3Uub3CurLj6HJltGXvViurXJL6xt9sxwzYVTjVaNNEx2pDT4aBU4J6Nc2zktOcTrnnZfLDyCt73rGVtsTkPsbDajuO5ueQw)')
9.  Copy the url value starting from `https:` until just before the closing single quote, paste it into the address line of your browser, and press **Enter**.
10. Content similar to the following is displayed.
    Make sure all of the custom fonts you are using are listed.

`/* latin */`
`@font-face {`
`font-family: 'Libre Barcode 128';`
`font-style: normal;`
`font-weight: 400;`
`src: local('Libre Barcode 128 Regular'), local('LibreBarcode128-Regular'), url(`[`https://fonts.gstatic.com/s/librebarcode128/v8/cIfnMbdUsUoiW3O_hVviCwVjuLtXeK_H9AI.woff2`](https://fonts.gstatic.com/s/librebarcode128/v8/cIfnMbdUsUoiW3O_hVviCwVjuLtXeK_H9AI.woff2)`) format('woff2');`
`unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;`
`}`
`/* latin */`
`@font-face {`
`font-family: 'Libre Barcode 39 Extended Text';`
`font-style: normal;`
`font-weight: 400;`
`src: local('Libre Barcode 39 Extended Text'), local('LibreBarcode39ExtendedText-Regular'), url(`[`https://fonts.gstatic.com/s/librebarcode39extendedtext/v7/eLG1P_rwIgOiDA7yrs9LoKaYRVLQ1YldrrOnnL7xPO4jNP6Me7gj.woff2`](https://fonts.gstatic.com/s/librebarcode39extendedtext/v7/eLG1P_rwIgOiDA7yrs9LoKaYRVLQ1YldrrOnnL7xPO4jNP6Me7gj.woff2)`) format('woff2');`
`unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;`
`}`
`/* latin */`
`@font-face {`
`font-family: 'Libre Barcode 39 Text';`
`font-style: normal;`
`font-weight: 400;`
`src: local('Libre Barcode 39 Text Regular'), local('LibreBarcode39Text-Regular'), url(`[`https://fonts.gstatic.com/s/librebarcode39text/v8/sJoa3KhViNKANw_E3LwoDXvs5Un0HQ1vT-0H0h5K.woff2`](https://fonts.gstatic.com/s/librebarcode39text/v8/sJoa3KhViNKANw_E3LwoDXvs5Un0HQ1vT-0H0h5K.woff2)`) format('woff2');`
`unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+`

`2212, U+2215, U+FEFF, U+FFFD;`
`}`

## Remove all custom fonts from your Google Docs template

If you experience issues, you may want to remove all custom fonts from your Google Docs template.

To remove all custom fonts from your Google Docs template:

1.  Open your application in the Editor.
2.  Go to the **Automation \> Tasks** tab in the Editor.
3.  Expand the appropriate task.
4.  Find the template property.
5.  Click **View** adjacent to the template name. This will open the template in Google Docs.
6.  From the Google Docs **Font** menu, uncheck all custom fonts.
7.  Use the procedure described in [Verify all custom fonts are present](#verify-all-custom-fonts-present) to ensure that no custom fonts remain.
