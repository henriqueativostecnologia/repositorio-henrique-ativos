---
fonte: https://support.google.com/docs/answer/6282736?hl=en
baixado: 2026-11-10
---

# Use Google Docs Editors with a screen reader

The Google Docs Editors (Docs, Sheets, Vids, Slides, and Pics) are designed to work with screen readers using speech or braille output. For best results, use the latest screen reader with the latest Chrome web browser.

## Topics

This article is divided into sections with headings. To jump to a specific section of the article, use the links below:

- [Topics](#Topics)
- [Open a blank doc](#Open_a_blank_doc)
- [Turn on screen reader support](#Turn_on_screen_reader_support)
  - [Menu bar](#Menu_bar)
  - [Keyboard shortcut](#Keyboard_shortcut)
- [Configure your screen reader](#Configure_your_screen_reader)
  - [ChromeVox](#ChromeVox)
  - [NVDA](#NVDA)
  - [JAWS](#JAWS)
  - [VoiceOver](#VoiceOver)
  - [Turn on Braille Support](#Turn_on_Braille_Support)
- [Common UI elements](#Common_UI_elements)
  - [Landmarks](#Landmarks)
  - [Menu bar and menus](#Menu_bar_&_menus)
  - [Top level buttons](#Top_level_buttons)
  - [Toolbar](#Toolbar)
  - [Context Menu](#Context_Menu)
- [Use keyboard shortcuts](https://support.google.com/docs/answer/6282736#Use_keyboard_shortcuts)
  - [Use popup list of keyboard shortcuts](#Use_popup_list_of_keyboard_shortcuts)
  - [Windows keyboard shortcut considerations](#Windows_keyboard_shortcut_considerations)
  - [Keyboard shortcut webpage](#Keyboard_shortcut_webpage)
- [Start editing](#Start_editing)
  - [Video tutorials](#Video_tutorials)

## Open a blank doc

1.  On the URL bar of the Chrome web browser, type: `docs.new`, `deck.new`, `sheet.new`, `vids.new`, or `pics.new`.

2.  Press **Enter**.

3.  As the page opens, listen for “Screen reader support enabled.”

**Tip:** You can use a screen reader with .pdf files that you export from Google Docs. [Learn how to download a file](https://support.google.com/drive/answer/2423534?co=GENIE.Platform%3DDesktop).

## Turn on screen reader support

To turn on or verify screen reader support, you can use either of these methods in any editor.

### Menu bar

1.  To open the Tools menu:
    - **On Windows and ChromeOS:** Press **Alt** **+** **Shift** **+** **t**.
    - **On MacOS:** Press **Control + Option + t**.
2.  In the Tools menu, select **Accessibility settings**.
3.  Tab to and check **Turn on screen reader support**.
4.  To close the dialog, press **Enter**.

**Tip:** Once any menu option is open, press the **Right arrow** or **Left arrow** to navigate to the other menus.

### Keyboard shortcut

- **On ChromeOS:** Screen reader support is automatically turned on when ChromeVox is on.
- **On Windows:** Press **Ctrl + Alt + z**.
- **On MacOS:** Press **Command** **+** **Option** **+** **z**.

## Configure your screen reader

The Google Docs Editors should be used as a web application instead of a web page. For guidance on how to configure your screen reader, follow these instructions:

### ChromeVox

Ensure sticky mode is turned off. To turn off, press the **Search** key twice until you hear “Sticky mode disabled.”

### JAWS

For editing content, ensure that JAWS Virtual PC cursor is off. To turn off, press **JAWS + z** until you hear "Use virtual PC cursor off."

Depending on your Forms mode configuration, this can be required more than once.

### NVDA

Focus mode generally provides a better experience for editing content than browse mode.

- **To switch between focus and browse modes:** Press **NVDA + space**.
- The **Ctrl + Alt + n** keyboard shortcut is used for efficient navigation in these editors, so make sure it isn’t used for the NVDA desktop shortcut.
  - **To verify or change your NVDA keyboard shortcut:** From the context menu on the NVDA desktop shortcut, open **Properties**.
  - On the Shortcut tab, edit the Shortcut key so it doesn't conflict with the Google Docs Editors, for example, **Ctrl + Alt + slash**.

### VoiceOver

- **Ensure Quick Nav is turned off:** Press the **Left arrow** and **Right arrow** keys at the same time until you hear “Quick Nav off.”
- **If VoiceOver doesn't automatically focus on the correct part of the page, like if a dialog window appears:** Press **Escape** to return your focus to the editing area.
- **To return to the editing area:** Press **VoiceOver + Shift + Down arrow**.

#### Keyboard shortcuts VoiceOver

The default VoiceOver keyboard shortcut, **Control + Option**, conflicts with Google Docs Editors menu shortcuts. There are 2 ways to avoid this conflict:

Change the VoiceOver modifier to use only the Caps Lock key:

1.  To open the VoiceOver Utility, press **VoiceOver + F8**.
2.  Tab to “Keys to use as the VoiceOver modifier.”
3.  Down arrow to the Caps Lock option (or any that omits **Control + Option**).
4.  To close the Utility: press **Command + q**.

If you don’t expect to use the menus frequently, you can:

- **Use the VoiceOver pass-through command:**
  1.  Press **VoiceOver + Tab.**
  2.  Type the menu shortcut, like for the Tools menu, **Control + Option + t**.
- **To search the menus:**
  1.  Press **Option + slash**.
  2.  Search for a term, like: `accessibility`.

### Turn on Braille Support

Docs, Sheets, and Slides have a Braille mode that’s needed when using a Braille display but can also be used when using spoken feedback. If you turn on braille support, you can notice the following improvements:

- Your braille display starts showing content.
- You can use the cursor routing buttons on your braille display to move the cursor.
- Faster screen reader typing echo.
- Faster screen reader navigation handling when you navigate by character.
- Better screen reader announcements of punctuation and whitespace.
- While you type, your screen reader uses its settings for character echo and word echo instead of always echoing characters.

If you aren’t using a braille display, or notice poor responsiveness in Sheets or Slides, turning off braille support can help. To turn off:

1.  Open the Tools menu.
2.  To open the Accessibility settings dialog, select **Accessibility**.
3.  Tab to the ”Turn on braille support” checkbox, then press **Space** to toggle.
4.  To accept the change and close the dialog. press **Enter**.

You can also use this shortcut:

- **On Windows and ChromeOS:** Press **Ctrl** **+** **Alt** **+** **h**.
- **On MacOS:** Press **Command** **+ Option + h**.

## Common UI elements

### Landmarks

In Docs, Sheets, and Slides you can quickly navigate between the Menu bar, Side panel, and the Main landmarks with the following shortcuts:

- **On Windows:** Press **Ctrl + Alt + period**.
- **On ChromeOS:** Press **Alt + Shift + period**.
- **On MacOS:** Press **Command** **+** **Option + period**.

**Tips:**

- Replacing period with comma will navigate in the reverse direction.
- These are landmarks that can be announced by your screen reader, but using the screen reader landmark navigation can be unreliable due to performance optimizations.

### Menu bar & menus

The editors have a menu bar with menus for File, Tools, and Accessibility:

- **To open the File menu:**
  - **On Windows and ChromeOS:** Press **Alt + Shift + f**.
  - **On MacOS:** Press **Control + Option + f**.
- **To explore that menu:** Use **Up arrow** and **Down arrow**.
- **To open other menus, like Tools or Accessibility:** Use the **Right arrow** or **Left arrow**.
- **To open each menu directly:** You can usually use the first letter, like:
  - **For Tools on Windows and ChromeOS:** Press **Alt + Shift + t**.
  - **For Accessibility on MacOS:** Press **Control + Option + a**.

To learn all menu bar shortcuts, refer to [Use keyboard shortcuts](https://support.google.com/docs/answer/6282736#Use_keyboard_shortcuts).

**Tips:**

- If the menu shortcut doesn’t move focus, it is likely because the menus have been hidden. Turn on menu visibility (and function) with the keyboard shortcut: **Ctrl + Shift + f**.
- To quickly find a menu option, press **Alt + slash** (on MacOS, press **Option + slash**). After pressing the shortcut, type part of the name and the matching items can be found with a **Down arrow**. This shortcut is available even when the menus are hidden.

### Top level buttons

There are top level buttons for document level actions like renaming, sharing, or moving to a different folder, between the Menu bar landmark and the menu bar.

- **To navigate to the last button:**
  1.  Open the File menu.
  2.  To navigate to the “Google account” button, press **Shift + Tab**.
- **To navigate to the first button:**
  1.  Navigate to the Menu bar landmark.
  2.  To navigate to the “Home” and the other top level buttons, press **Tab**.
- **To explore other top level buttons:** Press **Shift + Tab** or **Tab**.
- **To return to the main content:** Press **Escape**.

### Toolbar

A toolbar is a horizontal row of common action buttons that usually duplicate menu actions.

- **To get to the main toolbar:** From the menu bar or menus, press **Tab**.
- **To navigate to each of these toolbar actions for the application:** Press the **Right arrow**.

**Tip:** Many of the keyboard shortcuts are presented along with the name for quick usage later without navigating to the toolbar.

### Context Menu

A context menu is provided that has actions that are related to the current context, like editing or keyboard focus.

To open the context menu, press **Shift + F10**.

## Use keyboard shortcuts

The editors include many keyboard shortcuts for navigation and editing.

To open a popup list of keyboard shortcuts while you're editing:

- **On Windows and ChromeOS:** Press **Ctrl + slash**.
- **On MacOS:** Press Command **+ slash**.

Use these Help Center resources to learn more about Google Docs Editors keyboard shortcuts:

- [Keyboard shortcuts for Google Docs](https://support.google.com/docs/answer/179738)
- [Keyboard shortcuts for Google Sheets](https://support.google.com/docs/answer/181110)
- [Keyboard shortcuts for Google Slides](https://support.google.com/docs/answer/1696717)
- [Keyboard shortcuts for Google Vids](https://support.google.com/docs/answer/14950498)

### Use popup list of keyboard shortcuts

This UI is most helpful when you know that a shortcut exists because you can search.

When the “Keyboard shortcuts” dialog is displayed, tab once to the “Search keyboard shortcuts” combo box and type part of the function name like, “menu” and press **Enter**. The results will be presented in one or more tables that include that term. From there:

1.  Switch your screen reader to Virtual, Browse, Sticky, or QuickNav mode.
2.  If focus isn’t already on the table, navigate to the next table.
3.  Navigate down the column to hear the function names (matching your search).
4.  Navigate to the next column to hear the shortcut.
5.  If needed, navigate back to the first column and continue, or navigate to the next table to explore matches in another category of functions.
6.  When you find the desired shortcut, turn off your screen reader Virtual, Browse, Sticky, or QuickNav mode. To return to the content, press **Escape**.

**Tip:** These steps also work to browse all presented shortcuts even without performing a search.

### Windows keyboard shortcut considerations

If you aren’t using the default US English keyboard layout, many shortcuts that include the **Ctrl + Alt** modifier won't work as expected. They'll act as if the **AltGr** key was pressed instead. If you would like to use these shortcuts, consult the Windows documentation on installing and temporarily switching to the US English keyboard layout.

## Start editing

Learn more about using Google Docs Editors with a screen reader in the following help pages and videos.

- [Use Google Docs with a screen reader](https://support.google.com/docs/answer/1632201)
- [Use Google Sheets with a screen reader](https://support.google.com/docs/answer/1632199)
- [Use Google Slides with a screen reader](https://support.google.com/docs/answer/1634140)
- [Collaborate comment with a screen reader](https://support.google.com/docs/answer/6239410)

**Tip:** In Docs, Sheets, and Slides, you can turn off the screen reader announcements about other people entering, editing, or leaving the file. [Learn how to turn off collaborator announcements](https://support.google.com/docs/answer/6239410#announcements).

### Video tutorials

Screen reader videos for Docs, Sheets, and Slides

[Get started with Google Docs (18.9 minutes)](https://www.youtube.com/watch?v=LPzSAqhHqQk)

In this video, you’ll learn how to get started with Google Docs using NVDA.

[Get started with Google Sheets (26.3 minutes)](https://www.youtube.com/watch?v=oCYT63b_m88)

In this video, you’ll learn how to get started with Google Sheets using NVDA.

[Get started with Google Slides (16 minutes)](https://www.youtube.com/watch?v=IWZVQ-vldEk)

In this video, you’ll learn how to get started with Google Slides using NVDA.

## Get more help

For more Accessibility help, [contact the Disability Support team](https://support.google.com/accessibility/answer/7641084).

## Related resources

- [Use Google Docs with a screen reader](https://support.google.com/docs/answer/1632201)
- [Collaborate comment with a screen reader](https://support.google.com/docs/answer/6239410)
- [Change how paragraphs fonts look](https://support.google.com/docs/answer/145737)
