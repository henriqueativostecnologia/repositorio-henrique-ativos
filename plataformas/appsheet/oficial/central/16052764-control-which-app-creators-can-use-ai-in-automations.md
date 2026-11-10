---
fonte: https://support.google.com/appsheet/answer/16052764?hl=en
baixado: 2026-11-10
---

# Control which app creators can use AI in automations

You can control which app creators can use AI in automations in their apps by using the Disable Gemini in AppSheet Solutions (AI Tasks) policy, as described below. For more information, see [Define governance policies](https://support.google.com/appsheet/answer/11948767).

To prevent app creators from using AI in automations:

1.  Select **My account \> Policies**.
2.  Click **+ Organization Policy** or **+ Team Policy** to add an organization or team policy, respectively.
3.  Select **Disable Gemini in AppSheet Solutions (AI Tasks)** from the **Policy Template** drop-down.
4.  Click **Next**.
5.  The policy is preconfigured for you. You can modify any of the field values. See [Add a predefined policy](https://support.google.com/appsheet/answer/11948767#add-predefined-policy) for a description of each field. 
    **Important**: If you modify the **Condition** field, ensure that you retain the functionality defined below:
    `NOT([IsAiTask])`
6.  Click **Save**.
