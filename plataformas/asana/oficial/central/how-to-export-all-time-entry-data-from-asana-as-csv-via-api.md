---
fonte: https://help.asana.com/s/article/how-to-export-all-time-entry-data-from-asana-as-csv-via-api?language=en_US
baixado: 2026-11-10
---

# How to export all time entry data from Asana as CSV via API

For organizations using Asana’s [**Timesheets and Budgets**](https://help.asana.com/s/article/timesheets-and-budgets-add-on), periodic reporting is essential for accurate accounting and payroll. While Asana provides robust in-app views, you may occasionally need a comprehensive CSV export of all time entries across your entire domain for external auditing or custom processing at the end of a month or quarter.

This article explains how to use the Asana API to aggregate time entries from across your workspace and format them into a clean, accounting-ready CSV that matches your internal requirements.

> While this guide is tailored for users of the [Timesheets and Budgets add-on](https://help.asana.com/s/article/timesheets-and-budgets-add-on), this API-based export method is also available for non-addon users who log time via standard Asana task fields.

## Why export via API?

While the Asana UI offers powerful dashboards, exporting via API allows you to:

- **Automate reporting:** Schedule monthly or quarterly exports for your finance team without manual clicks.
- **Audit granularity:** Access specific metadata, such as Task Status, Priority, and Entry GIDs, that are crucial for record-keeping.
- **System integration:** Easily pipe your Asana time data into ERP or payroll software.

## The target export format

To ensure compatibility with standard accounting practices, your export script should produce a CSV containing the following fields as seen in your reviewer view exports:

|                  |                                                         |
|------------------|---------------------------------------------------------|
| **Column**       | **Description**                                         |
| **Task name**    | The title of the task where time was logged.            |
| **Time (hours)** | Total duration converted from minutes to decimal hours. |
| **Date**         | The specific day the work was performed.                |
| **Submitter**    | The name of the team member who logged the time.        |
| **Task GID**     | The unique identifier for the Asana task.               |
| **Project GID**  | The unique identifier for the parent project.           |
| **Task Status**  | Whether the task is currently "Open" or "Completed".    |
| **Entry GID**    | The unique identifier for the specific time log.        |

## Implementation: Exporting via Python

To export "all" time, your script must iterate through your projects to find tasks, then fetch time entries for those tasks using the [Get time tracking entries for a task](https://developers.asana.com/reference/gettimetrackingentriesfortask) endpoint.

### Prerequisites

- An [**Asana Personal Access Token (PAT)**](https://help.asana.com/s/article/app-management-and-integrations#h_01HQ14QVHB7HY1V9BDPA3GEM0T).
- Your **Workspace GID**.
- Python installed with the asana and pandas libraries.

### The export script

    Python
    import asana
    import pandas as pd

    # Initialize Client
    client = asana.Client.access_token('YOUR_PERSONAL_ACCESS_TOKEN')
    workspace_gid = 'YOUR_WORKSPACE_GID'

    def export_domain_time():
        all_time_data = []

        # 1. Iterate through all projects in the workspace
        projects = client.projects.get_projects({'workspace': workspace_gid})
       
        for project in projects:
            # 2. Get all tasks for the project
            tasks = client.tasks.get_tasks_for_project(project['gid'], opt_fields=[
                'name', 'gid', 'completed', 'completed_at', 'priority'
            ])

            for task in tasks:
                # 3. Fetch time entries for each task
                time_entries = client.time_tracking_entries.get_time_tracking_entries_for_task(
                    task['gid'],
                    opt_fields=['created_by.name', 'duration_minutes', 'entered_on', 'gid']
                )

                for entry in time_entries:
                    # Calculate hours in decimal format
                    hours = round(entry['duration_minutes'] / 60, 2)
                   
                    # Build the row to match the CSV template
                    all_time_data.append({
                        "Task name": task['name'],
                        "Time (hours)": hours,
                        "Date": entry['entered_on'],
                        "Submitter": entry['created_by']['name'],
                        "Task GID": task['gid'],
                        "Project GID": project['gid'],
                        "Task Status": "Completed" if task['completed'] else "Open",
                        "Task Completion Date": task.get('completed_at', ''),
                        "Task Priority": task.get('priority', ''),
                        "Entry GID": entry['gid']
                    })

        # 4. Save to CSV
        df = pd.DataFrame(all_time_data)
        df.to_csv('asana_time_export_accounting.csv', index=False)
        print("Export complete: asana_time_export_accounting.csv")

    export_domain_time()

## Critical considerations for large domains

When running this export for an entire organization, keep the following best practices in mind:

- **API Rate Limits:** Asana has limits on how many requests you can make per minute. For massive domains, consider adding time.sleep() or using the Asana library's built-in retry logic.
- **Date Filtering:** For monthly accounting, use the entered_on field within your script to filter only for the relevant period (e.g., the previous month).
- **Permissions:** Ensure the Personal Access Token belongs to a **Service Account** or an **Admin** who has access to all relevant projects, so no entries are skipped.

## Export time entries from the Timesheets page

You can export time entries from the **Timesheets** page for the timeframe you select. From **Timesheets**, click the dropdown arrow next to the page title, then select the export option that matches the time entries you need.

 

- **Export my time entries CSV** exports your own time entries for the selected timeframe.
- **Export submitters’ time entries CSV** exports time entries for the people whose time entries you review.
- **Export everyone’s time entries CSV** exports all time entries across the organization for the selected timeframe. This option is available to super admins.

Use the Timesheets export when you need a CSV file without setting up an API workflow. For automated reporting, custom processing, or access to the API response fields described later in this article, use the API method.

[](https://forum.asana.com/c/forum-en/tips/6)
