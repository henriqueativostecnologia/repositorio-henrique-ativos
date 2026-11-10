---
fonte: https://support.google.com/docs/answer/10519333?hl=en
baixado: 2026-11-10
---

# Get started with encrypted files in Drive, Docs, Sheets & Slides

This article has different instructions for each platform/version: Android phone & tablet, Computer, iPhone & iPad. All versions are copied below.

## Version: Android phone & tablet

All files uploaded to Drive or created in Docs, Sheets, and Slides are encrypted in transit and at rest with [AES256 bit encryption](https://support.google.com/drive/answer/141702). For additional confidentiality, your organization can allow you to encrypt Drive, Docs, Sheets, and Slides files with Workspace Client-side encryption. Encrypted files have some limitations from standard files. You can also upload any Drive file types like PDFs and Office as encrypted Drive files.

**Important:**

- **For administrators:** You can use Drive API to perform bulk imports of encrypted files for your organization. For more information, refer to the [Migrating Client-Side Encrypted Data to Drive guide](https://knowledge.workspace.google.com/admin/security/about-client-side-encryption?) in the Admin Knowledge Base.
- To encrypt Drive, Docs, Sheets, and Slides files with Workspace Client-side encryption:
  - You must have a Workspace account.
  - Your administrator must enable client-side encryption.
  - You must verify your identity.

You can download or preview an encrypted file on your Android Device if your admin has turned on the setting. Learn more about how to [download a file](https://support.google.com/drive/answer/2423534) from Google Drive.

To make, copy, or upload an encrypted file, go to [drive.google.com](https://drive.google.com) on your computer.

**Tips:**

- This feature is available for file types supported by Google Drive, including Microsoft Office and PDF files.
- To look at or preview client-side encrypted files, you need a compatible reader on your device.
- Google Docs, Sheets, and Slides are not yet supported.

#### Related articles

- [Collaborate on encrypted files in Docs, Sheets & Slides](https://support.google.com/docs/answer/10519035)
- [Connect to your identity provider for client-side encryption](https://support.google.com/a/answer/10743588)

## Version: Computer

All files uploaded to Drive or created in Docs, Sheets, and Slides are encrypted in transit and at rest with [AES256 bit encryption](https://support.google.com/drive/answer/141702). For additional confidentiality, your organization can allow you to encrypt Drive, Docs, Sheets, and Slides files with Workspace Client-side encryption. Encrypted files have some limitations from standard files. You can also upload any Drive file types like PDFs and Office as encrypted Drive files.

**Important:**

- **For administrators:** You can use Drive API to perform bulk imports of encrypted files for your organization. For more information, refer to the [Migrating Client-Side Encrypted Data to Drive guide](https://knowledge.workspace.google.com/admin/security/about-client-side-encryption?) in the Admin Knowledge Base.
- To encrypt Drive, Docs, Sheets, and Slides files with Workspace Client-side encryption:
  - You must have a Workspace account.
  - Your administrator must enable client-side encryption.
  - You must verify your identity.

### Learn about encryption

Encryption is the process of encoding information to protect your data. Only users who have Workspace Client-side encryption enabled by their admin and have verified their identity can make or copy encrypted files. On an encrypted file, any user with whom the file has been shared can access it using an encryption key unique to that file. Normally Google encrypts your content in transit and at rest, but with client-side encryption your domain has chosen to add an extra layer of protection.

##### Things to know about encryption

- Your domain administrator has control over which groups and individuals can use encryption. If you would like to move files to locations with encryption turned off or to turn on this feature for new locations, [contact your administrator](https://support.google.com/a/answer/6208960).
- Your administrator also has the option to recommend that new files in Drive, Docs, Sheets, and Slides are created using Client-side Encryption via in-app prompts. Please consult with your admin as needed to ensure that expectations for your organization are understood.
- Client-side Encryption provides an extra layer of protection for your organization. Your files are encrypted from end-to-end and between clients. Google cannot decrypt your files. Keep in mind:
  - Applications on your computer with sufficient permissions granted, such as Chrome extensions, may be able to view and exfiltrate encrypted files.
  - Encryption does not protect your files from someone who can view your screen.
- How often you’re required to resign in to open client-side encrypted files, is up to your admin. If you have to sign in often, contact your admin.

##### Find what’s different about encrypted files

- A lock appears next to an encrypted file.
- Only one person can edit an encrypted file at a time. [Learn how to collaborate on encrypted files](https://support.google.com/docs/answer/10519035).
- In encrypted files, autosave starts every 30 seconds, unless your device is idle or you perform another action, like share a file or attempt to exit a file.
  - If you attempt to exit an unsaved file, you get a warning. To avoid the loss of your unsaved changes, click **Cancel**.
- Autosave has 3 statuses:
  - **Waiting to save:** Waits for an autosave trigger or the 30-second timer.
  - **Saving:** A save is in progress. You can continue to edit your file.
  - **Saved to Drive:** You haven’t made any changes. Your version is current.
- There are different steps to create encrypted files. [Learn how to make or copy encrypted files](#section2).
- In order to access encrypted files, your admin may require you to sign into an additional SSO service twice, once for your organization's IDP and once with Google for Drive, Docs, Sheets, and Slides.
- You can print from Docs or Sheets, but not from Slides.
- Spellcheck for encrypted Docs and Slides is available in American English, British English, French, German, Italian, and Spanish.
- Spellcheck isn't available in Sheets.
- You can export a Sheets file into an Excel file. Go to **File** and then **Download**.
- Version History for encrypted files retains up to 100 versions. After you exceed 100 versions, less significant versions are removed automatically. Named versions aren't yet available.
- Encrypted Docs, Sheets, and Slides have a maximum size of 100 MB. Encrypted Drive files have no limit.
- The maximum number of images in a document is 3,000.
- A single image size is 1 MB.
- Downloading a folder doesn't affect client-side encrypted files.
- You can preview encrypted PDF documents and image files directly in Google Drive on the web without a file download. Other encrypted non-native files such as .txt and .md do not have preview support.

##### Find what’s not available for encrypted files

- Open [Microsoft Office in Edit mode for Docs or Slides](https://support.google.com/drive/answer/9276408)
- Comment on Drive files
- Use the mobile app to edit Docs, Sheets, or Slides
- Use functions in Sheets that make external calls
- Import Microsoft Office files into Docs or Slides
- Use certain tools, which includes:
  - Grammar check
  - Translate and compare documents
  - Voice typing
  - Add-ons
- Download Docs or Slides
- Container-bound Apps Script automations

### Make or copy encrypted files

**Important:** To make or copy encrypted files, you need to:

- Sign into a work or school account
- Have client-side encryption enabled by your admin
- Verify that your account can create files

##### Create a new encrypted file

To create an encrypted document, spreadsheet, or presentation, choose an option:

From Google Drive:

1.  Go to [drive.google.com](https://drive.google.com/).
2.  At the top left, click New .
3.  Point to the arrow next to Docs, Sheets, or Slides and then click **Blank encrypted document/spreadsheet/presentation**.
4.  In the “New encrypted document” window, click **Create**.

From Google Docs, Sheets, or Slides:

1.  Open a Google Docs, Sheet, or Slide.
2.  At the top, click **File**.
3.  Point to New and then click **New encrypted document/spreadsheet/presentation**.
4.  In the “New encrypted document” window, click **Create**.

**Tips:**

- If your admin enables CSE by Default, "New/Blank encrypted document/spreadsheet/presentation" appears as the recommended option under File and then New menu.
- If you create an encrypted file in a Shared folder, the encrypted file has the same access as the folder.
- If the options for **Blank encrypted document/spreadsheet/presentation** or **New encrypted document/spreadsheet/presentation** aren't available:
  - Confirm you’re logged into your work or school account.
  - Check if your admin has enabled client-side encryption.
  - Ensure you verify your identity. [Learn more about encryption with your identity provider.](https://support.google.com/a/answer/10743588)

##### Upload a new encrypted file

1.  Go to [drive.google.com](https://drive.google.com/).
2.  At the top left, click New .
3.  Point to the arrow next to File upload and then click **Encrypt and upload file**.

**Tips:**

- If your admin enables CSE by Default, "Encrypt and upload" appears as the recommended option in the New+ menu.
- If you upload an encrypted file in a Shared folder, the encrypted file has the same access as the folder.
- If the option for **Encrypt and upload file** isn't available:
  - Confirm you’re logged into your Workspace account.
  - Check if your admin has enabled client-side encryption.
  - Ensure you verify your identity. [Learn more about encryption with your identity provider.](https://support.google.com/a/answer/10743588)

##### Copy an encrypted file

**From Google Docs, Sheets, or Slides:**

1.  Open an encrypted Google Docs, Sheets, or Slides file.
2.  At the top left, click **File and then Make a copy**.

**From Google Drive:**

1.  Right-click on the encrypted file.
2.  If the encrypted file is:
    - **A Google Docs, Sheets, or Slides file:** Select **Make a copy**.
    - **Not a Google Docs, Sheets, or Slides file:** Select **Make a copy** and then **Make a copy**.

**Tip:** If you want to make a copy without additional encryption, [remove additional encryption from a document](https://support.google.com/docs/answer/10519333#zippy=%2Cremove-encryption-from-a-document).

##### Add encryption to a document

**From Google Docs, Sheets, or Slides:**

1.  Open a Google Docs, Sheets, or Slides file.
2.  At the top, click **File** and then **Make a copy**.
    - If it’s a Google Slides file, click **Entire presentation**.
3.  Select **Add additional encryption**.

**From Google Drive:**

**Important:** You can’t add additional encryption for Google Workspace editor files.

1.  Right-click on the file.
2.  Select **Make a copy** and then **Make an encrypted copy**.

**Tip:**

- If you can’t find the “Add additional encryption” checkbox in Google Docs, Sheets, or Slides, or the “Make an encrypted copy” menu item in Drive:
  - Confirm you're logged into your work or school account.
  - Check if your admin allows client-side encryption.
  - Confirm that you are the owner of the document in My Drive or the Manager of the shared drive.
  - Verify your identity. [Learn how to connect with your identity provider](https://support.google.com/a/answer/10743588).

**Important:** Features that additional encryption doesn't support are made static or removed.

- Features made static:
  - Checklists
  - Embedded drawings, charts, and tables
  - Linked forms
  - External data functions like GOOGLEFINANCE
  - Connected Sheets
  - WordArt
- Features removed from the document:
  - E-signature fields
  - Protected ranges
  - Apps Script and Add-ons

##### Remove additional encryption from a document

**From Google Docs, Sheets, or Slides:**

1.  Open a Google Docs, Sheets, or Slide file.
2.  At the top, click **File** and then **Make a copy**.
    - If it’s a Google Slides file, click **Entire presentation**.
3.  Select **Remove additional encryption**.

**From Google Drive:**

**Important:** You can’t remove additional encryption for Google Workspace editor files.

1.  Right-click on the encrypted file.
2.  Select **Make a copy** and then **Make a decrypted copy**.

**Tip:**

- If you can’t find the “Remove additional encryption” option in Google Docs, Sheets, or Slides, or the “Make a decrypted copy” menu option in Drive:
  - Confirm you're logged into your work or school account.
  - Check if your admin allows client-side encryption.
  - Confirm that you are the owner of the document in My Drive or the Manager of the shared drive.
  - Verify your identity. [Learn how to connect with your identity provider](https://support.google.com/a/answer/10743588).

### Learn how to work with encrypted Excel files in Drive

There are different ways to work with encrypted Excel files. You can:

- Edit Excel files in Sheets.
- Import Excel data into Sheets.
- Convert Excel files to Sheets.
- Download a copy of a Sheets file in Excel format.

##### Edit Excel files in Sheets

- In Drive, double-click an encrypted Excel file.
- The spreadsheet opens in a new tab.
- You can now edit, share, find version history, and more. All changes you make are saved to the original encrypted Excel file.

**Tips:**

- You can only open encrypted Excel files with the .xlsx extension.
- File size can be up to 100 MB.
- Image memory limit can be up to 90 MB.
- You can have a maximum of up to:
  - 10 million cells
  - 3000 images

##### Learn how to import Excel data into Sheets

You can import data from an Excel file to an available encrypted Sheets file. Your Excel file won’t be changed, even as you change the encrypted Sheets file.

1.  In Sheets, create a new or open an available encrypted Excel file.
2.  At the top left, click **File and then Import**.
3.  Choose the Excel file.
4.  Click **Select**.
5.  Choose an import option:
    - Create new spreadsheet
    - Insert new sheet(s)
6.  Click **Import data**.

**Tips:**

- You can only import Excel files with the .xlsx extension.
- While you import, unsupported Excel features in Sheets are ignored.
- **Maximum file size:** 100MB
- **Maximum number of cells:** 10M
- **Maximum number of images:** 3000

##### Convert Excel files to Sheets

Instead of importing data, you can convert an encrypted Excel file to Sheets while you continue to work on it. The encrypted file won’t change.

1.  In Drive, double-click an encrypted Excel file.
    - The spreadsheet opens in a new tab.
2.  Click **File** and then **Save as Google Sheets**.

You can find the encrypted Excel file and the new encrypted Sheets in Drive. You can keep or delete the Excel file. If you keep the Excel file, to avoid confusion, rename it to {ARCHIVE}...xlsx.

##### Learn how to download a Sheets file into an Excel file

You can download a copy of an encrypted Sheets file in Excel format.

1.  In Sheets, at the top left, click **File and then Download and decrypt**.
2.  Click **Microsoft Excel (.xlsx)**.

#### Related articles

- [Collaborate on encrypted files in Docs, Sheets & Slides](https://support.google.com/docs/answer/10519035)
- [Connect to your identity provider for client-side encryption](https://support.google.com/a/answer/10743588)

## Version: iPhone & iPad

All files uploaded to Drive or created in Docs, Sheets, and Slides are encrypted in transit and at rest with [AES256 bit encryption](https://support.google.com/drive/answer/141702). For additional confidentiality, your organization can allow you to encrypt Drive, Docs, Sheets, and Slides files with Workspace Client-side encryption. Encrypted files have some limitations from standard files. You can also upload any Drive file types like PDFs and Office as encrypted Drive files.

**Important:**

- **For administrators:** You can use Drive API to perform bulk imports of encrypted files for your organization. For more information, refer to the [Migrating Client-Side Encrypted Data to Drive guide](https://knowledge.workspace.google.com/admin/security/about-client-side-encryption?) in the Admin Knowledge Base.
- To encrypt Drive, Docs, Sheets, and Slides files with Workspace Client-side encryption:
  - You must have a Workspace account.
  - Your administrator must enable client-side encryption.
  - You must verify your identity.

You can download or preview an encrypted file on your iPhone or iPad if your admin has turned on the setting. Learn more about how to [download a file](https://support.google.com/drive/answer/2423534) from Google Drive.

To make, copy, or upload an encrypted file, go to [drive.google.com](https://drive.google.com) on your computer.

**Tips:**

- This feature is available for file types supported by Google Drive, including Microsoft Office and PDF files.
- To look at or preview client-side encrypted files, you need a compatible reader on your device. 
- To protect your data, you can’t record your screen while viewing encrypted files. A visual mask hides the content if you record. Encrypted audio and video playback pauses automatically until you stop recording.
- Google Docs, Sheets, and Slides are not yet supported.

#### Related articles

- [Collaborate on encrypted files in Docs, Sheets & Slides](https://support.google.com/docs/answer/10519035)
- [Connect to your identity provider for client-side encryption](https://support.google.com/a/answer/10743588)
