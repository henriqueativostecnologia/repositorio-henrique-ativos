---
fonte: https://help.asana.com/s/article/zoom-transcripts-for-automation-and-ai-studio?language=en_US
baixado: 2026-11-10
---

# Zoom transcripts for automation and AI Studio

**Zoom automation is available within Asana automation. Available on Asana** [ **Advanced**](https://asana.com/plan/advanced)**,** [ **Enterprise**](https://asana.com/enterprise)**, and** [ **Enterprise+**](https://asana.com/enterprise) **tiers, as well as** [ **legacy tiers**](https://asana.com/pricing-legacy) **Business, and Legacy Enterprise.**

Zoom transcript automation enables you to automatically generate meeting summaries and action items from your Zoom meeting recordings. This feature helps track meeting outcomes and increase accountability by automating post-meeting summaries, providing clearer tracking of decisions, and capturing next steps. 

Instead of asking participants to read notes or watch recordings, AI Studio can analyze the transcript to generate summaries and automatically create actionable tasks in Asana.

#### Related Articles

- [How to create a Zoom call notes workflow with AI Studio](https://help.asana.com/s/article/how-to-create-a-zoom-call-notes-workflow-with-ai-studio)
- [AI Studio](https://help.asana.com/hc/en-us/articles/14076905203483-Approvals)
- [Zoom meetings and Asana](https://help.asana.com/hc/en-us/articles/14138545317659-Zoom-and-Asana-integration)
- [Rules](https://help.asana.com/hc/en-us/articles/17974450400283-IT-help-desk)

## Setting up Zoom transcript automation

Zoom transcript automation for AI Studio connects your Zoom meetings to create Asana tasks through rules. When a Zoom meeting recording is completed and a transcript becomes available, rules can automatically create tasks containing the meeting transcript and recording link and passcode. AI Studio rules can take this even further - AI can analyze the transcript to automate creation of tasks for action items discussed during the meeting. 

To set it up:

1.  Ensure you have the Zoom integration installed in your Asana workspace
2.  Create a rule in AI Studio that uses the **Transcript is ready** trigger and create task action. Add variables to the action like transcript text or Use AI
3.  If using AI to create tasks for action items, ensure “Let AI decide the number of tasks to create” is selected on the create task action
4.  Configure the AI guidance to extract the information you need from the transcript.

## Types of triggers available

There are two main trigger options for Zoom transcript automation:

1.  **Transcript is ready for all recorded meetings**: This trigger activates whenever any Zoom meeting recording with a transcript becomes available
2.  **Transcript is ready for specific meeting ID series**: This trigger activates only for a specific meeting series that you designate

## Configuring AI to process transcripts

When setting up your rule, you can configure AI Studio to:

1.  Generate a summary of the meeting discussion
2.  Identify key decisions made during the meeting
3.  Extract action items and create tasks or subtasks for each one
4.  Assign tasks to the appropriate team members based on the transcript content

See an example of how to set this up in [How to create a Zoom call notes workflow with AI Studio](https://help.asana.com/s/article/how-to-create-a-zoom-call-notes-workflow-with-ai-studio).

## Frequently asked questions

### Do I need a paid Zoom account to use this feature?

Yes, you need a Zoom account with recording and transcription capabilities enabled.

### Can I customize how the AI interprets the transcript?

Yes, you can customize the AI guidance in your rule to focus on specific types of information or formatting preferences.

### Will this work for all languages?

The feature works best with English transcripts. Support for other languages may vary based on Zoom's transcription capabilities.

### How long does it take for the automation to run?

Typically 5-15 minutes after your meeting ends, depending on transcript processing time and meeting length.

### Can I edit the AI-generated summaries?

Yes, all generated tasks and comments can be edited.

### What if I don't want automation for certain meetings?

Use the "specific meeting" trigger option and only configure rules for meetings you want automated, or manually disable recording for meetings you want to keep private.

### Does this work with breakout rooms?

The automation captures the main meeting transcript. Breakout room discussions are typically included if the main session is being recorded.

### Can I see the raw transcript?

Yes, you can configure the rule to also attach the raw transcript file to tasks for reference.

### Is there a limit on meeting length?

While there's no strict limit, very long meetings (2+ hours) may result in less accurate summaries. Consider breaking these into shorter segments or manually reviewing results.
