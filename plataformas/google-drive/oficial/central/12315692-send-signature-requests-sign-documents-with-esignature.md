---
fonte: https://support.google.com/drive/answer/12315692?hl=en
baixado: 2026-11-10
---

# Send signature requests & sign documents with eSignature

With eSignature, you can create documents for signatures and send signature requests in Google Docs and Google Drive. To complete eSignature requests, signers can easily fill in requested information.

## Eligibility

The eSignature feature for Google Docs and PDFs is available to:

- Workspace Individual accounts.
- These Workspace plans when your administrator enables the feature:
  - Business Standard and Plus
  - Enterprise Starter, Standard, and Plus
  - Enterprise Essentials and Enterprise Essentials Plus
  - Education Plus users
  - Microsoft Word files opened in Google Docs

If you don’t have a Workspace subscription plan, you can gain access to this feature today. [Sign up for a Workspace Individual plan](https://workspace.google.com/individual/).

**Tip:** If you upgraded your account to access the eSignature feature, it can take a few minutes for the feature to become fully available. Wait a few minutes and refresh your page to try again.

## Create & send a document for eSignature

#### Prepare an eSignature document

**Important:** This is available to certain [eligible users](https://support.google.com/docs/answer/12315692#eligible_users).

1.  Open the eSignature side panel.
    - If you start from PDF files in Google Drive:
      1.  On your computer, go to [drive.google.com](http://drive.google.com).
      2.  Upload a new PDF file or find an existing one that you want to use.
      3.  Open the PDF file in viewing mode.
      4.  At the top right, click Menu More and then **eSignature**.
    - If you start from Google Docs:
      1.  On your computer, go to [drive.google.com](https://drive.google.com/).
      2.  Create a new Google Doc or open an existing one.
      3.  At the top, click **Tools** and then **eSignature**.
2.  If you have multiple signers, under “Insert fields for,” select the specific signer you want to insert an eSignature field for.
    - To update the list of available signers in the dropdown, select **Manage signers**. It’ll open the **Manage signers** dialog.
    - In the **Manage signers** dialog, you can add up to 10 signers and assign labels for each signer to identify the signers in the document.
3.  Drag one or more of the following fields to add to your document:
    - Signature
    - Initials
    - Name
    - Text field
    - Date signed
4.  To find who the field is assigned to, click the field.
    - To update signer assignment for the field, use the **Assigned to** dropdown in the popup.
    - To update the list of signers in the Google Doc and open the same dialog as above, in the dropdown, click **Manage signers**.
    - When you select a ”Text Field,” you can add a description and select the font size in the popup.
      - The description informs signers what you expect in this field, like “Job title” or “Email address.”
      - The font size you set becomes the font size of the value the signer enters for this text field.
5.  To add all signers and eSignature fields for signers in the document, repeat the steps.

**Tips:**

- You can add a maximum of 200 fields of any type per document.
- You can add up to 10 signers to an eSignature request.
- For a signer in the document, the signer label is just a placeholder identifier and isn't part of the signing PDF that’s generated later.
- There's no requirement to use signer's email addresses as signer labels at this point since no emails are sent yet. That happens later in the "Send an eSignature request” section below where the placeholder labels for signers are mapped to actual email addresses.
- To differentiate fields assigned to different signers easily, each signer in the document is assigned a unique color. All fields assigned to the same signer are displayed in the same color.

#### Send an eSignature request

1.  After you add all appropriate fields, on the right, click **Request signature**.
    - Collaborators that own or have edit access to the document can find this button. Otherwise, this button won't be available.
2.  Enter a title for the generated PDF file.
3.  Enter the email address for each signer.
    - You can also add a message that'll be sent to the signers in the eSignature request email.
4.  To send periodic reminders to signers, turn on **Automatic reminders**.
    - When this is enabled, signers who haven't completed the request will receive a reminder email 3 days (72 hours) after the initial request is sent.
    - Additional reminders are sent every 3 days after that, for up to 9 days, or until the document is signed.
5.  You can select the audit trail locale in the request dialog. This value determines the locale in which the audit trail generates at the end.
6.  Review and accept Terms of Service if shown in the request dialog.
7.  Click **Request signature**.
    - After your request is successfully created:
      - A PDF is made from your document and shared with the signers. They can sign the form, but won’t be able to make any other edits or change who has access to the file.
      - An email notification with a link to the document is sent to the signers.
8.  You can find a PDF copy of the sent file in the same folder as your original document.
    - **Important**: The PDF copy will be saved in your **My Drive** instead of the original folder in two cases:
      - If you are not an Editor of the folder where it is stored.
      - If the original folder's [*sharing rules*](https://support.google.com/a/answer/60781) would prevent the signers from having access to the file. Saving to My Drive makes sure all signers can see the document.

**Tips:**

- After you click **Request signature**, the PDF file locks to avoid any changes before the signers can fulfill the eSignature request. The file used to create the signature request remains unlocked and isn't automatically shared with the signers as part of the eSignature request.
- To check the progress of an eSignature request:
  - Open the respective PDF file in Drive or through the link in the email notification.
  - To open the right side panel and view eSignature details, at the top right of the PDF, click **View details**.

#### Save a contract template

To save a PDF file with eSignature fields as a template, at the top right, click **Save changes**. For future use, Google Docs saves the eSignature fields automatically.

#### Add changes to a document after you send it

You can't update the PDF file once an eSignature request starts on it because the PDF file is locked. You can still organize it in your Drive, for instance: change its location.

To change or cancel the eSignature request after a request is sent, select **Cancel**. You can send a new request after you add changes to the source Google Doc or PDF file in Google Drive and send a new PDF file for signature. Follow the steps in [Create and send a document for eSignature](https://support.google.com/docs/answer/12315692#create&senddoc).

If the eSignature request is active, you can't unlock the PDF file. You can still add changes to the Google Doc at any time because it isn't locked as part of the eSignature request.

#### Cancel a pending eSignature request

If the eSignature request is still pending, to cancel the request:

1.  Open the PDF file for that request.
2.  Click Menu More   and then **Cancel**.

**Tip:** If you want to delete the PDF copy of your canceled request, navigate to the file’s folder and delete that copy. The default location is My Drive.

#### Check the status of eSignature request

1.  Open the PDF file for that request.
2.  Select an action:
    - Click Menu More and then **eSignature**.
    - Click **View details**.
3.  On the side panel, you’ll find the details of the eSignature request and its status.

## Sign, reject, or view details for an eSignature request

#### Sign an eSignature request

1.  Open the email account that the eSignature request was sent to.
2.  Open the email notification.
3.  Click the embedded link.
    - If you open the PDF file directly from Drive, to sign the document, click **Sign**.
4.  Your document may contain text fields for you to fill out, such as “Job Title” or “Email”. If so, click and complete these fields.
5.  Click on any colored fields, which indicate that those fields are yours to sign.
    - A dialog box will appear for your signature. You'll have two options to create your electronic signature:
      - **Type**: Enter your full name. The system will automatically create a signature for you in a standard style. You can also enter your initials.
      - **Draw**: Use your mouse, trackpad, or touchscreen to draw your actual signature. You can also draw your initials.
    - After you have created your signature, click **Adopt and sign**.
    - **Tip:**
      - If there are multiple signature or initial fields, you can reuse this same signature throughout the document.
      -  If signature drawing is unavailable, try updating your web browser..
    - Fields assigned to other signers who haven’t signed yet will appear grayed out.
    - Signature values provided by other signers who have already signed will be visible in the PDF.
6.  After you complete all required signature fields, at the top of the page, click **Mark Complete**.
    - After you click "Mark Complete," you get a notice in the dialog that shows:
      - The exact email value being recorded for you that is viewable by others with access to the eSignature PDFs after you click to proceed.
      - In the case where you have multiple emails on your Google Account, the email that the requester had entered for you in the request dialog is used.
7.  Review and accept the [Terms of Service](https://workspace.google.com/terms/google-workspace-individual-terms/esignature-signer/).
8.  Click **Agree & Continue**.

**Tips:**

- **If you're the only signer:** You and the requester get an email that the request is complete.
- **If the request has multiple signers:** The request isn’t complete until all signers sign, at which point all signers and the requester get an email that the request is complete.

#### Reject an eSignature request

1.  On a computer, open the email account that the eSignature request was sent to.
2.  Open the email notification.
3.  Click the embedded link.
4.  Click **Reject**.
    - The requester receives an email that the request was rejected.

#### View details of an eSignature request

1.  On a computer, open the email account that the eSignature request was sent to.
2.  Open the email notification.
3.  Click the embedded link.
4.  Click **View details.**

## Complete eSignature requests

#### Find the finalized document

After the eSignature request is complete, all parties can find copies of the final document.

- **For signers:** You can find a personal copy of the signed PDF document in your My Drive folder. You can also find a link to your copy in the email you received upon completion of the document.
- **For requesters:** You can find the final PDF copy in the same folder where the original document was saved. You can also find a link in the email you received upon completion of the document.
  - **Important**: The PDF copy will be saved in your **My Drive** instead of the original folder in two cases:

    - If you are not an Editor of the folder where it is stored.

    - If the original folder's [*sharing rules*](https://support.google.com/a/answer/60781) would prevent the signers from having access to the file. Saving to My Drive makes sure all signers can see the document.

If you can't find the final document:

- Search in your My Drive folder.
- Use Advanced search
  - In the search bar, click Advanced search .
  - In the "Approvals and eSignatures" section, select an option:
    - **Awaiting my approval**
    - **Requested by me**
- Check your spam folder.
- Reach out to other parties involved in the eSignature request to obtain a copy.
- [Send feedback about Gmail](https://support.google.com/mail/answer/9212652) or [Contact Google Drive support](https://support.google.com/drive/answer/4431192).
- To make sure you can receive future eSignature documents:
  - If you have a Google Drive account, check your Drive settings so that you can store new content.
- Check your email settings so that you can receive emails from <esignature-noreply@google.com>.

#### Find audit trail

You can select the audit trail locale in the request dialog. This value determines the locale in which the audit trail generates at the end.

**Tip:** After all signers sign the document, a final .pdf is generated. The end of the .pdf contains an audit trail page. The page is generated in the locale the requester selected when they start the eSignature request. This page contains a log of various events that occurred during the eSignature request lifecycle with timestamps, such as:

- eSignature requested
- eSignature signed
- eSignature completion
- Identifying information for the requester and signers such as their email and name

## Send feedback

To provide feedback to Google:

1.  Open the PDF file for the signature request you want to provide feedback for.
2.  Click **View details ** and then  Menu  More   and then  **Send feature feedback**.

You can also send feedback through the product:

- [Send feedback about Gmail](https://support.google.com/mail/answer/9212652)
- [Contact Google Workspace support](https://support.google.com/a/answer/1047213)
