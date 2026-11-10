---
fonte: https://support.google.com/appsheet/answer/11547502?hl=en
baixado: 2026-11-10
---

# Control the image width in a webhook

`Image` and `Thumbnail` columns included in a webook template are inserted using a URL to the image. For example, if your `Image` column is called `Photo`, you could include an URL to that image as follows:

    Name: <<[Name]>>
    Photo: <<[Photo]>>
    Address: <<[Home Address]>>

 

By default, the image width in the URL is based on the column type, as follows:

- `Thumbnail` column: 200
- `Image` column: 600

You can control the image width in the URL by creating a [format rule](https://support.google.com/appsheet/answer/10106703).

To create a format rule to control how the thumbnail or image is displayed:

1.  Open the AppSheet Editor.
2.  Go to **App \> Format Rules**.
     We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
    You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

    ## If you are using the legacy navigation

    Go to **UX \> Format Rules**.  
3.  Click **+ New Format Rule**.
4.  Choose the table containing the `Thumbnail` or `Image` column in the **For this data** field.
5.  Select the column name in the **Format these columns and actions** field.
6.  Choose one of the following for **Image format** under **Template format**:

    **Large***:* Display as 1000 x 1000 image
    **Medium***:* Display as a 600 x 600 image
    **Small***:* Display as a 200 x 200 image
    **Tiny***:* Display as a 50 x 50 image
    **Text***:* Display as a URL
