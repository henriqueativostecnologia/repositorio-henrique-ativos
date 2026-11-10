---
fonte: https://help.asana.com/s/article/add-movement-to-your-workflow?language=en_US
baixado: 2026-11-10
---

# Add movement to your workflow

Once your foundation is in place, add features that standardize intake, reduce manual updates, and create clear “go/no‑go” moments.

Video: https://fast.wistia.net/embed/iframe/5ixn5tki7j?web_component=true&seo=true&videoFoam=false

## Standardize intake with forms

Use a [form](https://help.asana.com/s/article/forms) to turn submissions into actionable tasks in your project.

**Set up a form**

1.  Open your project and create a form from the customize menu.
2.  Add questions for the details you need (title, description, requester, target date, budget).
3.  [Map form questions to custom fields](https://help.asana.com/s/article/field-mapping-in-forms) so the task is created with key data already filled in.
4.  Use [branching](https://help.asana.com/s/article/forms#gl-branching) so requesters only see relevant follow‑up questions.

## Reduce busywork with Rules

Automate repetitive steps so work moves forward with fewer manual changes.

**Build rules with triggers, conditions, and actions**

- Example: *When a task is added to the project* → **If** `Department = Marketing` → **Then** assign to the Marketing reviewer and set `Status = Assigned`.
- Example: *When* *`Status`* *changes to In review* → add a comment to notify the requester.
- Example: *When* *`Stage`* *moves to Staffing approval* → convert the task to an **Approval** and assign to the staffing team.

**Create rules faster with Asana AI**

Use the [smart rule creator](https://help.asana.com/s/article/smart-rules) to describe what you want in plain language (e.g., “When a request is created from the form", Check if "Department = Marketing", "Then assign to Alex and set Status to Assigned”). Asana will suggest the appropriate trigger, conditions, and actions—you can review and publish.

**Other helpful options**

- Multi‑home key tasks into secondary projects.
- Add [branching/conditions](https://help.asana.com/s/article/conditions-and-branching-in-rules) inside a single rule to handle variations without creating dozens of separate automations.

## Create clarity with approvals

Mark tasks as [**Approvals**](https://help.asana.com/s/article/approvals) when a formal decision is required. Approvers can choose **Approve**, **Request changes**, or **Reject** so everyone knows the status. Use a rule to auto‑convert tasks to approvals at the right stage and to route them to the correct approver.

## Example: Request workflow, end‑to‑end

1.  A requester submits the form. A task is created with fields prefilled.
2.  A rule assigns it to the right reviewer and sets Status.
3.  When Status = **In review**, another rule posts a comment to keep the requester informed.
4.  If the review passes, the task is auto‑converted to an **Approval** and assigned to staffing.
5.  On **Approve**, the event team kicks off the deadline‑bound **event project** (often from a template) and links it back to the original request.
