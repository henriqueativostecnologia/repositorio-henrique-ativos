---
fonte: https://support.google.com/appsheet/answer/11547760?hl=en
baixado: 2026-11-10
---

# Display images, thumbnails, drawings, and signatures in templates

Display images, thumbnails, drawings, and signatures in templates as described in the following sections:

- [Include image, thumbnail, drawing, and signature columns in templates](#include)
- [Control the display of images, thumbnails, drawings, and signatures](#control-display)
- [Link to an image](#link)

## Include image, thumbnail, drawing, and signature columns in templates

You can include image, thumbnail, drawing, and signature columns in templates.

For example, if your `Image` column is called `MyPhoto`, you could include it as follows:

    Name: <<[Name]>>
    Photo: <<[MyPhoto]>>
    Address: <<[Home Address]>>

## Control the display of images, thumbnails, drawings, and signatures

By default, the image, thumbnail, drawing, and signature columns are displayed as images. The display image size depends on the column type, as follows:

|                 |                          |
|-----------------|--------------------------|
| **Column type** | **Default display size** |
| Drawing         | 600x600                  |
| Image           | 600x600                  |
| Signature       | 600x600                  |
| Thumbnail       | 200x200                  |

You can create a [format rule](https://support.google.com/appsheet/answer/10106703) to control how the image, thumbnail, drawing, and signature values are displayed, including:

- Whether each value is displayed as an image or a URL

- The size of each displayed value

To create a format rule to control the display of the columns:

1.  Open the AppSheet Editor.
2.  Go to **App \> Format Rules**.
     We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
    You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

    ## If you are using the legacy navigation

    Go to **UX \> Format Rules**.  
3.  Click **+ New Format Rule**.
4.  Choose the table containing the Drawing, Image, Signature, or Thumbnail column in the **For this data** field.
5.  Select one or more columns to format in the **Format these columns and actions** field.
6.  Choose one of the following for **Image format** under **Template format**:
    **Large***:* Display as 1000 x 1000 image
    **Medium***:* Display as a 600 x 600 image
    **Small***:* Display as a 200 x 200 image
    **Tiny***:* Display as a 50 x 50 image
    **Text***:* Display as a URL

## Link to an image

To link to an image, use a [hyperlink expression](https://support.google.com/appsheet/answer/10107911).
