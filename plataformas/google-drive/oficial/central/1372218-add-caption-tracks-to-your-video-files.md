---
fonte: https://support.google.com/drive/answer/1372218?hl=en
baixado: 2026-11-10
---

# Add caption tracks to your video files

This article has different instructions for each platform/version: Computer, Android phone & tablet, iPhone & iPad. All versions are copied below.

## Version: Computer

You can make your video content available to a larger audience when you add captions. If you want to reach deaf, hard-of-hearing viewers, or speakers of different languages, captions help these groups understand your videos.

To add caption tracks, use a caption file, which contains the text and other information to time your captions with your video.

##### Prepare your caption file

A subtitle or closed caption file contains the text of what's said in the video. It also contains time codes for when each line of text should be displayed. Some files also include position and style info, which is especially useful for deaf or hard of hearing viewers. See what file formats Drive supports below.

##### Basic File Formats

If you’re new to creating caption files, we recommend using one of the following basic file types:

+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **Format name**                                    | **File extension**                                 | **More info**                                      |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| [SubRip](http://en.                                | .srt                                               | -   Only supports basic versions of these files.   |
| wikipedia.org/wiki/SubRip#SubRip_text_file_format) |                                                    | -   No style info or markup is recognized.         |
|                                                    |                                                    | -   The file must be in plain UTF-8.               |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| [                                                  | .sbv or .sub                                       | -   Only supports basic versions of these files.   |
| SubViewer](http://en.wikipedia.org/wiki/SubViewer) |                                                    | -   No style info or markup is recognized.         |
|                                                    |                                                    | -   The file must be in plain UTF-8.               |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| [M                                                 | .mpsub                                             | "FORMAT=" parameter is supported.                  |
| Psub](http://www.mplayerhq.hu/DOCS/tech/mpsub.sub) |                                                    |                                                    |
| (MPlayer subtitle)                                 |                                                    |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| [LR                                                | .lrc                                               | -   No style info or markup is recognized.         |
| C](http://en.wikipedia.org/wiki/LRC_(file_format)) |                                                    | -   Enhanced format is supported.                  |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Videotron Lambda                                   | .cap                                               | This file type is primarily for Japanese           |
|                                                    |                                                    | subtitles.                                         |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+

If you’re new to creating caption files, you may want to use SubRip (.srt) or SubViewer (.sbv). They only require basic timing info, and can be edited using any plain text editing software.

The main difference between SubRip and SubViewer files is the format of the caption start and stop times. Here are examples of both formats:

##### SubRip (.srt) example

`1`

`00:00:00,599 --> 00:00:04,160`

`>> ALICE: Hi, my name is Alice Miller and this is John Brown`

`2`

`00:00:04,160 --> 00:00:06,770`

`>> JOHN: and we're the owners of Miller Bakery.`

`3`

`00:00:06,770 --> 00:00:10,880`

`>> ALICE: Today we'll be teaching you how to make`

`our famous chocolate chip cookies!`

`4`

`00:00:10,880 --> 00:00:16,700`

`[intro music]`

`5`

`00:00:16,700 --> 00:00:21,480`

`Okay, so we have all the ingredients laid out here`

##### SubViewer (.sbv) example

`0:00:00.599,0:00:04.160`

`>> ALICE: Hi, my name is Alice Miller and this is John Brown`

`0:00:04.160,0:00:06.770`

`>> JOHN: and we're the owners of Miller Bakery.`

`0:00:06.770,0:00:10.880`

`>> ALICE: Today we'll be teaching you how to make`

`our famous chocolate chip cookies!`

`0:00:10.880,0:00:16.700`

`[intro music]`

`0:00:16.700,0:00:21.480`

`Okay, so we have all the ingredients laid out here`

##### Advanced file formats

Use these file formats if you want to have more control over the styling (markup) or positioning of your captions. **********************

+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **Format name**                                    | **File extension**                                 | **More info**                                      |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| SAMI (Synchronized Accessible Media Interchange)   | .smi or .sami                                      | Only timecodes, text, and simple markup (\<b\>,    |
|                                                    |                                                    | \<i\>, \<u\>, and the color= attribute within a    |
|                                                    |                                                    | \<font\>) are supported. Positioning isn't         |
|                                                    |                                                    | supported.                                         |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| RealText                                           | .rt                                                | Only timecodes, text, and simple markup (\<b\>,    |
|                                                    |                                                    | \<i\>, \<u\>, and the color= attribute within a    |
|                                                    |                                                    | \<font\>) are supported. Positioning is not        |
|                                                    |                                                    | supported.                                         |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| [WebVTT](https://en.wikipedia.org/wiki/WebVTT)     | .vtt                                               | In initial implementation. Positioning is          |
|                                                    |                                                    | supported, but styling is limited to \<b\>, \<i\>, |
|                                                    |                                                    | \<u\> since CSS class names aren't yet             |
|                                                    |                                                    | standardized.                                      |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| [TTML](http://www.w3.org/TR/ttaf1-dfxp/)           | .ttml                                              | In partial implementation. SMPTE-TT extensions     |
| (Timed-Text Markup Language)                       |                                                    | supported for [CEA-608                             |
|                                                    |                                                    | features](http://en.wikipedia.org/wiki/EIA-608).   |
|                                                    |                                                    | iTunes Timed Text (iTT) file format is supported;  |
|                                                    |                                                    | iTT is a subset of [TTML, Version                  |
|                                                    |                                                    | 1.0](h                                             |
|                                                    |                                                    | ttp://www.w3.org/TR/2010/CR-ttaf1-dfxp-20100223/). |
|                                                    |                                                    | Styling and positioning aresupported.              |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| [DFXP](http://www.w3.org/TR/ttaf1-dfxp/)           | .ttml or .dfxp                                     | These files types are interpreted as TTML files.   |
| (Distribution Format Exchange Profile)             |                                                    |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+

##### Broadcast file formats

These file formats are typically used for closed captions for broadcast content (TV and movies) and support either of these standards:

- [CEA-608](http://en.wikipedia.org/wiki/EIA-608)
- [EBU-STL](https://tech.ebu.ch/docs/tech/tech3264.pdf)

Drive tries to display the captions from these files as if they were on a TV — with the same styling, color, and positioning.

+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| **Format name**                                    | **File extension**                                 | **More info**                                      |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Scenarist Closed Caption                           | .scc                                               | These files have an exact representation of        |
|                                                    |                                                    | [CEA-608                                           |
|                                                    |                                                    | data](http://en.wikipedia.org/wiki/EIA-608).This   |
|                                                    |                                                    | is the preferred format whenever captions are      |
|                                                    |                                                    | based on CEA-608 features.                         |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| [E                                                 | .stl                                               | European Broadcasting Union standard.              |
| BU-STL](http://tech.ebu.ch/docs/tech/tech3264.pdf) |                                                    |                                                    |
| (binary)                                           |                                                    |                                                    |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Caption Center (binary)                            | .tds                                               | Supports                                           |
|                                                    |                                                    | [CEA-608](http://en.wikipedia.org/wiki/EIA-608)    |
|                                                    |                                                    | features.                                          |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Captions Inc. (binary)                             | .cin                                               | Supports                                           |
|                                                    |                                                    | [CEA-608](http://en.wikipedia.org/wiki/EIA-608)    |
|                                                    |                                                    | features.                                          |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Cheetah (ASCII text)                               | .asc                                               | Supports                                           |
|                                                    |                                                    | [CEA-608](http://en.wikipedia.org/wiki/EIA-608)    |
|                                                    |                                                    | features.                                          |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| Cheetah (binary)                                   | .cap                                               | Supports                                           |
|                                                    |                                                    | [CEA-608](http://en.wikipedia.org/wiki/EIA-608)    |
|                                                    |                                                    | features.                                          |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+
| NCI (binary)                                       | .cap                                               | Supports                                           |
|                                                    |                                                    | [CEA-608](http://en.wikipedia.org/wiki/EIA-608)    |
|                                                    |                                                    | features.                                          |
+----------------------------------------------------+----------------------------------------------------+----------------------------------------------------+

##### Upload captions

 

1.  On your computer, sign in to [drive.google.com](https://drive.google.com/).
2.  Right-click the video you want to add captions to, then click **File** **information** and then **Manage** **caption** **tracks**.
    - **Tip:** Alternatively, you can open the video and click **More** and then **File** **information** and then **Manage caption tracks** at the top right.
3.  Click **Add new caption tracks**.
4.  Click **Select file** and choose a caption or transcript file.
5.  Choose the language for the captions and a name for the track.
6.  Click **Upload**.

##### Edit caption tracks

1.  On your computer, sign in to [drive.google.com](https://drive.google.com/).
2.  Right-click the video file with caption tracks you want to edit, then click **File information** and then **Manage caption tracks**.
    - **Tip:** Alternatively, you can open the video and click **More** and then **File** **information** and then **Manage** **caption** **tracks** at the top right.
3.  Click the caption track you want to edit.
4.  Click **Edit**.
5.  You can edit its name and language. You can also turn on or off the track for the video.
6.  Click **Save**.

##### Delete captions

1.  On your computer, sign in to [drive.google.com](https://drive.google.com/).
2.  Right-click the video file with caption tracks you want to delete, then click **File information** and then **Manage caption tracks**.
    - **Tip:** Alternatively, you can open the video and click **More** and then **File information** and then **Manage caption tracks** at the top right.
3.  Next to the caption track you want to delete, click **Delete**.
4.  Click **Delete**.

##### Translate captions

After the caption tracks to your videos are processed, you can translate them.

1.  On your computer, sign in to [drive.google.com](https://drive.google.com/).
2.  Open the video with the caption track you want to translate.
3.  In the bottom right, click Settings Settings .
4.  At the bottom of the language list, click Auto-translate.
5.  Select a language from the list.

##### Sharing settings for captions

The video’s sharing settings also apply to captions. If someone else can edit the video, they can also upload, download, and edit captions for the video. Learn more about [sharing files in Google Drive](https://support.google.com/drive/answer/2494822).

##### Caption error messages

If you get an error while uploading your file, make sure the file is:

- In the correct format. The file types listed under basic, advanced, and broadcast file types on this page are supported.
- Not too large. The caption file must be less than 2 MB.
- Not longer than the video. If the file is longer than the video, the video won’t be able to auto-sync.

##### Automatically generated captions

Available languages:

- Arabic
- Chinese
- Czech
- Dutch
- English
- Filipino
- Finnish
- French
- German
- Greek
- Hebrew
- Hindi
- Hungarian
- Indonesian
- Italian
- Japanese
- Korean
- Malay
- Norwegian
- Polish
- Portuguese
- Romanian
- Russian
- Spanish
- Swedish
- Thai
- Turkish
- Ukrainian
- Vietnamese

You can easily add captions to your videos.

1.  In the Google Drive homepage, right-click on the video you want to add captions to.
2.  Click **Manage caption tracks**.
    - Or, while watching the video, click More More and then **Manage caption tracks**.
3.  Select a language.

Google Workspace Admins can turn on automatic captions for all uploaded videos in your company's Google Workspace.

**Tips:**

- Automatically generated captions will be turned on by default. Captions will generate automatically when you upload a video to Drive.
- Your Google Workspace Admin may require you to request caption generation.
  - Right-clicking the video in your Drive and then Manage Caption tracks and then Generate Automatic Captions.
  - While viewing the video, click More More and then Manage caption tracks and then Generate automatic captions.
- Your Google Workspace Admin may have this feature disabled.

##### File version changes

Captions only apply to the video version they’re uploaded to. If you add a new file version or delete the current one, the captions are removed. You can add new captions to the updated video version.

### Get more help

For more Accessibility help, [contact the Disability Support team](https://support.google.com/accessibility/answer/7641084).

## Version: Android phone & tablet

You can make your video content available to a larger audience when you add captions. If you want to reach deaf, hard-of-hearing viewers, or speakers of different languages, captions help these groups understand your videos.

To add caption tracks, use a caption file, which contains the text and other information to time your captions with your video.

To add caption tracks to your video files, open [Google Drive](https://drive.google.com/) on your computer.

### Get more help

For more Accessibility help, [contact the Disability Support team](https://support.google.com/accessibility/answer/7641084).

## Version: iPhone & iPad

You can make your video content available to a larger audience when you add captions. If you want to reach deaf, hard-of-hearing viewers, or speakers of different languages, captions help these groups understand your videos.

To add caption tracks, use a caption file, which contains the text and other information to time your captions with your video.

To add caption tracks to your video files, open [Google Drive](https://drive.google.com/) on your computer.

### Get more help

For more Accessibility help, [contact the Disability Support team](https://support.google.com/accessibility/answer/7641084).
