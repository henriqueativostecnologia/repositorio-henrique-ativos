---
fonte: https://help.asana.com/s/article/writing-ai-studio-instructions?language=en_US
baixado: 2026-11-10
---

# Writing instructions in AI Studio

AI Studio is available for customers on [Starter](https://asana.com/plan/starter), [Advanced](https://asana.com/plan/advanced), [Enterprise](https://asana.com/enterprise), and [Enterprise+](https://asana.com/enterprise) plans. Visit [asana.com/ai](https://asana.com/ai) to learn more about the launch of Asana AI Studio.

This article will walk you through best practices for writing effective instructions in AI Studio. If you’d like to go further, you can also earn the [AI Studio Foundations skill badge](https://academy.asana.com/ai-studio-foundations-skill-badge) in the Asana Academy. You’ll learn how to write effective prompts, plan Smart workflows, and troubleshoot common issues.

**

Video: https://fast.wistia.net/embed/iframe/qpil1n1n4u?web_component=true&seo=true

#### Related articles

- [Introduction to Asana AI Studio](https://help.asana.com/s/article/ai-studio)
- [Create Smart workflows with AI Studio](https://help.asana.com/s/article/ai-studio-smart-workflows)
- [AI Studio FAQ](https://help.asana.com/s/article/ai-studio-faq)
- [AI Studio add-on and pricing](https://help.asana.com/s/article/ai-studio-pricing)
- [Asana AI FAQ](https://help.asana.com/s/article/asana-ai-faq)

## General principles for AI instructions

Well-written instructions are critical to a successful Smart workflow. Below are some best practices and things to avoid when writing instructions in AI Studio. These tips will help ensure your instructions are interpreted correctly by Asana AI, so it delivers the expected outcomes.

**AI models know an incredible amount, but they may not have good intuition about your problem domain, and may approach the problem naively. **If AI is not doing what you want, it’s likely because it is not seeing something you think it can, or because you’re not describing what you want clearly enough for it.

Reading the AI’s reasoning is usually a good way to understand what’s happening. If the rule cannot run for a specific reason, the AI will include this detail in the task history under **All activity**. **It will follow directions very well, especially if they are well organized and well formatted. It structures its understanding hierarchically — punctuation and structure are extremely important to its understanding.**

## The "Use AI" variable

It's crucial to understand that your writing instructions directly impact the **Use AI** variable, which is AI Studio's tool for generating context-aware output.

To learn more, check out [How the Use AI variable works](https://help.asana.com/s/article/ai-studio-use-ai).

## Be clear and precise

Use clear, direct language and avoid ambiguity. Specify exact actions, inputs, and outputs. Instructions should be direct commands, such as "Check if the task has a due date" or "Generate a list of top 3 project risks".

Tell AI where it is, and what it is doing. For example, “you are working in the Asana of Acme Corporation and your job is to triage incoming design requests.” It will benefit from this context.

**Tell AI everything it needs to know in order to complete the task, and what to do. For example: “If the request is functionally the duplicate of any of the tasks in @design-project, then write a comment on the task explaining why it is a duplicate of a pre-existing task, and link to the duplicate task.” **Don't assume the AI has access to information or context that isn't explicitly provided in the task or attachments. 

**With all of this in mind, it’s fine to start out with a minimal set of instructions and only add more details later if you encounter issues with the output. Not every workflow requires an exhaustive explanation.

## Include examples of the desired output

Beyond simply describing the output you expect, it can be helpful in some instances to include concrete examples of desired outputs or actions to guide the AI.

For instance, "Summarize the key points from the attached project brief, like this: **Project goals: X, Y, Z.** **Target audience: A, B, C**". If you can provide multiple examples of the desired output in the instructions, the AI’s output is more likely to match your expectations in cases where a simple description is not sufficient.

## Provide context with structure and labels

When working with multi-step processes or intricate conditions, it's helpful to break down instructions into clear, actionable parts.

Use numbered lists, bullet points, or headings to clearly separate each step or condition, ensuring the AI understands the flow and context. In addition to giving a clear structure of the context in tasks and instructions, provide any necessary resources, constraints, or goals upfront.

Attach files or resources directly on tasks or in instructions that will give the AI the full picture, avoiding assumptions about what it knows beforehand. This will help the AI make more accurate decisions and respond effectively. Asana AI can read data from files attached to tasks, or those attached to the AI Studio instructions. 

Simply labeling information with headings in your instructions will make it easier for the AI to understand the context. Labeling specific parts of a prompt lets the AI know what’s an instruction, a question, or any other piece of context. You can refer to the specific part of the prompt in other areas of your instructions, too. This improves how the AI processes the input, ensuring the right focus on each part. See the image below for a simple example of how to use headings to organize information within the AI instructions.

 

 

In this example, the instructions specify that the AI should refer to the style guide while drafting the email. The style guide is included in the instructions and is clearly labeled, meaning the AI has the context it needs to match the style guide. It would also be possible to attach a style guide document directly to the instructions.Consider various situations that may arise and provide instructions for handling each case. Use conditional logic ("if this, then that") where appropriate.

## Iterate and refine

Testing your workflow and observing its outcomes is one of the best ways to learn how and where to improve your instructions. Check the AI reasoning in each task’s history to understand how AI is interpreting your instructions. 

For example, imagine you have a use case around work intake triaging. Your instructions to Asana AI to move new tasks to a specific section if they have “enough information” for a human reviewer to make a decision. You notice that there are a lot of false positives, and tasks without much detail are moving to that section. An iteration you might try is describing what a task with enough detail, and what a task *without* enough detail looks like. This can help Asana AI to make the right call and avoid false positives.

Give the AI a way to tell you if it has enough information or not, or tell it what to do when something isn’t right. For example, "If the task description is empty, add a comment to the task to prompt the user to provide more information before proceeding”.

## Choose the right AI model

Keep in mind that you will likely observe different outputs depending on the model you choose and its capabilities. See [AI Studio FAQ](https://help.asana.com/s/article/ai-studio-faq) for more detail on the available models.

## Earn the AI Studio Foundations skill badge

Earn the [AI Studio Foundations skill badge](https://academy.asana.com/ai-studio-foundations-skill-badge) in the Asana Academy. You’ll learn how to write effective prompts, plan Smart workflows, and troubleshoot common issues.

[](https://forum.asana.com/c/forum-en/tips/6)
