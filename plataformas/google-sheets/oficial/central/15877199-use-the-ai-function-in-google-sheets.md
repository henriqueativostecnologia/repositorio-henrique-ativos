---
fonte: https://support.google.com/docs/answer/15877199?hl=en
baixado: 2026-11-10
---

# Use the AI function in Google Sheets

**Feature availability:**

- This feature requires an eligible Google Workspace or Google AI plan. [Learn how to get started with Google Workspace with Gemini](https://support.google.com/docs/answer/13952129).
- This feature is also available through our trusted tester program, [Google Workspace Experiments](https://support.google.com/docs/answer/13447104).
- [Learn about supported languages for Google Workspace with Gemini](https://support.google.com/docs/answer/14925782).

You can use the AI function to:

- Generate text.
- Summarize information.
- Categorize information.
- Analyze sentiment.
- Access real-time information from Google Search.

## Use the AI function in Sheets

You can use the AI function to:

- **Generate text:** To generate text tailored to your data, Google Workspace with Gemini uses relevant information from your sheet.
- **Summarize information:** To help you understand your data, Google Workspace with Gemini analyzes the content of your spreadsheet and extracts important key takeaways.
- **Categorize information:** To help you detect patterns, Google Workspace with Gemini categorizes your data into groups. This includes sentiment analysis.
- **Access real-time information:** To automatically generate accurate and timely answers, Google Workspace with Gemini provides up-to-date information from Google Search.

1.  On your computer, open a spreadsheet from [Google Sheets](https://docs.google.com/spreadsheets/u/0/).
2.  In a cell, enter an AI function. You can use either “=AI()” or “=Gemini()”.
    - For example: `=AI(“Generate slogan for event in 10 words or less”, A2)`
    - Or, at the top of the spreadsheet, click **Insert** and then **Function** and then **AI**.
3.  Select the cell or cells with an AI function.
4.  Click **Generate and Insert**.
5.  **Optional:**
    - To refresh output, click **Refresh and Insert**.
    - To view the web sources used for a response, click into a cell, hover over the content and then click **Sources** .

**Tip:** When you click “Generate and Insert” or “Refresh and Insert,” generated content is inserted and the cell edit is attributed to you in version history.

## Add an AI column to a table

When you add an AI column to a table, its first non-header row automatically shows the AI function. After you enter a specific function in that row, you can autofill the rest of the column with the same function and generate entries.

To add an AI column, at the top right of the last column in the table, click Insert AI column right .

## Fill columns with Gemini

To save time and reduce manual errors, you can use Gemini to extend and complete information in your spreadsheets:

- **Drag-and-drop:** If your column has at least one completed cell, you can use a new drag entry point to fill the column based on the context of the table.
- **Prompt-based filling:** For empty multi-cell selections, you can use a one-click entry point to "Fill" the range. You can either automatically fill cells when a column has at least one completed cell or write a custom prompt to fit your specific needs.

## Check some examples

- **Generate new text**
  - `=AI(“Generate slogan for event in 10 words or less”, A2)`
  - `=AI("Create an email to the reviewer addressing specific items in their reviews.", A2:G2)`
  - `=AI("develop a list of keywords for the job title based on the summary of duties.", A2:C2)`
- **Summarize input cell or range**
  - `=AI("For the customer, write a one sentence summary of their feedback.", A2:D2)`
  - `=AI("You are the owner of a pet sitting business. Write a 2 sentence summary for the customer about their pet’s last stay. Be a little funny.", F2)`
  - `=AI("List in bullet points the main themes of the book summary.", D2)`
- **Categorize inputs based on given definitions or generic categories**
  - `=AI("Classify the preview as either a spam email or not a spam email.", D2)`
  - `=AI("Categorize the customer inquiry as a compliment, exchange request, or return request.",C2)`
  - `=AI("Classify the restaurant by which New York City borough it belongs to. Use the neighborhood to help.", A2:C2)`
- **Analyze sentiment**
  - `=AI("Classify the sentiment of the realtor analysis.”, D2)`
  - `=AI("Perform sentiment analysis on the emails sent by the customers to the barbershop.", C2)`
  - `=AI("Classify the body of the email, as either positive, negative, or neutral.", D2)`
- **Get up-to-date information from the web**
  - `=AI("What is the current capital of Kazakhstan?", A2)`
  - `=AI("What is the population of the list capital city?", A2:B2)`
  - `=AI("What is the birthday of the author who wrote the associated book. Only output the date", A2:B2")`

**Tip:** If you want to refer to two ranges that aren’t contiguous, you can use concatenation in the prompt. However, if there’s a change in the data in ranges that are part of the prompt, you don’t get a prompt to refresh the data.

For example, if you use the function `=AI("Find the major themes in the customer feedback of "&B2&" using the comments: "&D2&"")`, when B2 or D2 change, you need to manually determine when to refresh the data.

## Syntax

`AI(“prompt”,[optional range])`

- **Prompt:** A specific prompt that describes your desired action.
- **Range:** This is optional. It’s the range that the prompt refers to when it generates data.

## Learn about the limitations of the AI functions

- Responses are limited to text.
- The AI function doesn’t have access to your entire spreadsheet or other files in your Google Drive.
  - To provide data or context to your prompt, add the data to your current spreadsheet and use the optional range argument. This is highly recommended to improve output quality.
- You can’t undo or redo your function.
  - You can regenerate your output instead.
- You can’t have more than one function with the same name in Sheets. If you build a custom function with the name “=AI()” or “=Gemini(),” the custom function remaps to the Sheets AI function.
- Embedded AI functions aren’t supported.
  - For example: `=IF(AI(“sentiment analysis”, A2)),”negative”,0)`
- If “AI function not available” shows, it could mean that:
  - You're not a participant in the Workspace Experiments program or you’re not on a Workspace plan with access to AI functions.
  - You don’t have access to the AI function because of your Admin settings or your language setting. [Learn how to change your language setting](https://support.google.com/accounts/answer/32047).
- The AI function has short term and long term generation limits. If you reach a long term limit, you temporarily can’t click “Generate.” You can wait for 24 hours and then try again.
- You can select multiple cells with AI functions and generate outputs; however, only the first 350 selected cells with AI functions will be generated. You can wait for the generation to complete and select more cells to generate outputs.
- You can’t generate content with the AI function if you access Sheets with other cloud storage providers like Box, Dropbox, or Egnyte with Google Drive. [Learn how to use Google Docs, Sheets & Slides with Box, Dropbox, or Egnyte](https://support.google.com/drive/answer/9191990).

## Give feedback on the AI function

- To provide feedback on the generated input of this feature, click , and follow the prompts.
- To provide general feedback on this feature, at the top, go to Help and then Help Docs improve.
- To report a legal issue, [learn how to report content for legal reasons](https://support.google.com/legal/answer/3110420).

## Learn about Gemini feature suggestions

- Gemini feature suggestions don’t represent Google’s views, and should not be attributed to Google.
- Don’t rely on Gemini features as medical, legal, financial or other professional advice.
- Gemini features may suggest inaccurate or inappropriate information. Your feedback makes Gemini more helpful and safe.
- Enterprise end users can submit feedback about their experience using this feature. End users are informed before they submit feedback that the feedback data shouldn’t contain personal, sensitive, or confidential information.
