---
fonte: https://help.asana.com/s/article/ai-studio-smart-workflows?language=en_US
baixado: 2026-11-10
---

# Create Smart workflows with AI Studio

AI Studio is available for [Starter](https://asana.com/plan/starter), [Advanced](https://asana.com/plan/advanced), [Enterprise](https://asana.com/enterprise), and [Enterprise+](https://asana.com/enterprise) customers. Visit [asana.com/ai](https://asana.com/ai) to learn more about the launch of Asana AI Studio.

Smart workflows are workflows with AI embedded in them to pass off your teams' busywork. AI Studio provides a user-friendly, no-code interface to set them up in minutes, combining the power of large language models (LLMs) and Asana’s rules engine. This article walks you through how to create Smart workflows using AI Studio — from choosing triggers to configuring AI actions and writing effective instructions. If you’d like to go further, you can also earn the [AI Studio Foundations skill badge](https://academy.asana.com/ai-studio-foundations-skill-badge) in the Asana Academy. You’ll learn how to write effective prompts, plan more advanced workflows, and troubleshoot common issues.

#### Related articles

- [Introduction to Asana AI Studio](https://help.asana.com/s/article/ai-studio)
- [Writing instructions in AI Studio](https://help.asana.com/s/article/writing-ai-studio-instructions)
- [AI Studio FAQ](https://help.asana.com/s/article/ai-studio-faq)
- [AI Studio add-on and pricing](https://help.asana.com/s/article/ai-studio-pricing)
- [Asana AI FAQ](https://help.asana.com/s/article/asana-ai-faq)

## Choose a trigger

Choosing a trigger in AI Studio is no different to choosing a trigger in Asana’s automation builder. Your trigger will be the event that allows the automation to run. See our [automation triggers article](https://help.asana.com/s/article/rule-triggers) for a detailed overview of triggers and how they work.

 

 

Click the **Add trigger **card to choose a trigger for the Smart workflow.

## Add AI conditions

With AI Studio, you can use AI to apply additional analysis or judgment to your rule condition. This is optional. Click **Paths **to add a condition to your Smart workflow.

 

To create a conditional check which uses AI, follow these instructions:

1.  Under **Conditions**, click **Add condition**, and then click **Create conditional check with AI**.

2.  Under **Add condition details **you can write instructions for Asana AI to follow.

 

As with the instructions you wrote in the instructions pane, be sure to use clear and direct language. Read our dedicated article about [writing instructions for AI](https://help.asana.com/s/article/writing-ai-studio-instructions). 

Some example AI conditions might include the following:

- “Check if the task description is in English”
- “Check if there is enough information in the task’s description to create a user story”
- “Check if the task is asking for an approval”

## Add AI actions

Click **Add step** to add an action to your Smart workflow. When creating a smart rule, you can select which action should be performed, but allow AI to decide how to execute that action.

 

 

For example, when selecting the action **Add comment**, instead of commenting with the exact same text, you can allow AI to compose a comment that is tailored to the information in the task, by choosing the variable **Use AI**. This allows the AI to write a comment, draft, report, or any other piece of text based on the instructions provided to it by the creator. 

## The "Use AI" variable

It's crucial to understand that your writing instructions directly impact the **Use AI** variable, which is AI Studio's tool for generating context-aware output.

To learn more, check out [How the Use AI variable works](https://help.asana.com/s/article/ai-studio-use-ai).

## Data and permissions

Click the three dot icon to open the **Settings** section and navigate to the **AI Studio** tab to choose what data can be used, permissions and objects AI can read. Within the **Data and permissions** section, you can configure which data to use from tasks and projects, if you want to include attachments and links added to tasks, and who can be added as a collaborator.

 

Under the **Objects AI can read** section, you can see which Asana objects AI can read.

 

Changing these settings can affect the overall cost and quality of output, as it determines the scope of data that AI should process. A rule has access only to the Asana objects (e.g., tasks, projects, goals, portfolios) that it references. By default, these objects only include (a) information in the task triggering the rule and (b) information and tasks in the project that the rule is housed in.

## Give AI instructions and choose an AI moder

****This is where you will provide simple and direct instructions for Asana AI to follow. Start by describing the overall task that you want the AI to accomplish. You can also include examples and process guidelines to follow, either in text or via attachments, and @mention work objects like tasks and projects in Asana, or include attachments. You can also @mention teams, discussed further in the [AI Studio FAQ](https://help.asana.com/s/article/ai-studio-faq). Read more about how to write instructions for AI [here](https://help.asana.com/s/article/writing-ai-studio-instructions).

AI Studio offers access to various large language models, with different associated costs and capabilities, provided by OpenAI and Anthropic. See our [AI Studio FAQ](https://help.asana.com/s/article/ai-studio-faq) for further details on the models. To choose a mode, click **Instructions** and open the AI model drop-down.

 

Want more AI workflow ideas? [Check our these community posts!](https://forum.asana.com/c/forum-en/ai-studio/ai-studio-tips/212)

[ ](https://forum.asana.com/c/forum-en/tips/6)
