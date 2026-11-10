---
fonte: https://help.asana.com/s/article/ai-studio-credit-optimization?language=en_US
baixado: 2026-11-10
---

# AI Studio credit optimization

## How credit works

Asana AI Studio uses a credit-based system to power smart workflows and AI-driven automations. Every time a rule executes, it consumes credits based on the volume of input data, the AI model selected, and how frequently the rule runs.

> **Tip:** The cost of a rule is primarily driven by the data going in. Optimizing your inputs is the single most impactful way to reduce credit consumption.

Four factors determine how many credits a rule uses:

- **Input volume —** The amount of data processed, including task details, attachments, web links, and referenced projects.
- **Output volume —** The amount of content the AI generates, such as comments, summaries, or field updates. Longer outputs cost more.
- **AI model —** Different models have different per-token costs. Premium models cost more but handle complex tasks better.
- **Frequency —** How often the rule triggers directly multiplies total consumption.

Approximately 100 tokens equal 1 credit. Each AI model has its own cost multiplier, so the same input processed by different models will consume different amounts.

### Credit plans at a glance

| **Plan**  | **Allocation**       | **Details**                                                                      |
|-----------|----------------------|----------------------------------------------------------------------------------|
| **Basic** | 50K–200K / month     | Included with Starter, Advanced, and Enterprise plans. Stacks with paid credits. |
| **Plus**  | 100K credits / month | Credits expire monthly with no rollover.                                         |
| **Pro**   | 5M credits / quarter | Credits expire at quarter’s end. Workflows pause at approx. 130% usage.          |
| **Max**   | Unlimited            | No credit limits. Scale AI workflows without usage constraints.                  |

Mid-period add-ons provide full credits immediately, with fees prorated for the remaining period.

### AI model cost reference

Use this reference to estimate how switching models affects your credit costs. By default, Asana recommends **GPT-4o** and automatically selects a model based on the rule content.

| **Model**             | **Input Multiplier** | **Output Multiplier** | **Best For**                                           |
|-----------------------|----------------------|-----------------------|--------------------------------------------------------|
| **Claude 3.5 Sonnet** | 5x                   | 25x                   | Great at writing documents and handling most tasks.    |
| **Claude 3 Opus**     | 25x                  | 125x                  | Best at following complex guidance and deep reasoning. |
| **GPT-4o \***         | 2.5x                 | 20x                   | High-performance default for complex logic.            |
| **GPT-4o mini**       | 0.5x                 | 5x                    | Handles most routine tasks extremely efficiently.      |
| **Claude 3.5 Haiku**  | 3x                   | 15x                   | Good at summarizing and rapid classification.          |

\* **Recommended default.** Asana auto-selects a model based on rule content when this option is chosen.

**Credit cost formula:**
`((Input Tokens × Input Multiplier) + (Output Tokens × Output Multiplier)) / 100 = Total Credits`

> **Model selection tip:** GPT-4o mini (0.5x input) costs significantly less than Claude 3 Opus (25x input) for the same data. Start with the lightest model that produces acceptable results.

## Checking your credit usage

Monitor credit consumption directly in the Asana Admin Console:

1.  **Navigate to Admin Console** and select your billing account.
2.  **Locate AI Studio** under Paid Products.
3.  **Open the Usage tab** to view detailed consumption data.

From the Usage tab, you can identify your top-consuming builders and rules—both are automatically sorted by credit usage. Click into any individual rule to view its configuration and find optimization opportunities.

## Optimizing credit consumption

The following optimization levers are listed in priority order. Start at the top for the biggest impact.

### 1. Highest impact: Review referenced projects

If your rule guidance includes @mentioned projects, each one pulls its content into the input—multiplying costs. Only @mention strictly necessary projects.

### 2. High impact: Manage attachments and web links

Uncheck “Include attachments and links added to tasks” in rule settings if not essential for the AI to perform the task.

### 3. Medium impact: Choose the right AI model

**GPT-4o mini** and **Claude 3.5 Haiku** are low cost and great for summarizing or classifying. Reserve higher-cost models for long-form document generation.

## Managing credit limits

### Approaching or exceeding your limit

1.  **Optimize first.** Apply the levers in the optimization section above.
2.  **Right-size your plan.** Assess whether Basic, Plus, Pro, or Max matches your actual usage.
3.  **Add credits mid-period.** Mid-period purchases provide full credits immediately with prorated fees.

### Overage policies

| **Plan**       | **What happens at the limit**                                                    |
|----------------|----------------------------------------------------------------------------------|
| **Plus / Pro** | Workflows continue up to 130% of purchased credits within the cycle, then pause. |
| **Max**        | Unlimited credits — no overage limits apply.                                     |
| **Basic**      | You may qualify for a one-time extension. Contact your Asana representative.     |

## When to reach out

Contact your Asana account team if:

- A single rule execution consumes an unexpectedly large number of credits.
- Your usage has jumped dramatically without a clear cause.
- You need a temporary credit increase to maintain business continuity.

**Questions? Your Asana account team is here to help.**
