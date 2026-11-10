---
fonte: https://help.asana.com/s/article/migrating-time-tracking-data-from-everhour-to-asana?language=en_US
baixado: 2026-11-10
---

# Migrating time tracking data from Everhour to Asana

This article explains how to move historical time tracking data from Everhour into Asana’s native Timesheets and Budgets add-on. By following these steps, you can consolidate your team’s time data, ensuring accurate project reporting and budget tracking within a single platform.

### Related articles

- [Time tracking in Asana](https://help.asana.com/s/article/time-tracking-in-asana)
- [Timesheets and Budgets add-on](https://help.asana.com/s/article/timesheets-and-budgets-add-on)

## Step 1: Export time entries from Everhour

The migration begins by retrieving your existing data. To ensure you have all historical logs for your team, follow these steps:

1.  Log in to your Everhour account as an **Owner** or **Admin**.
2.  Navigate to the **Team Settings** page by visiting [https://app.everhour.com/#/account/team](https://app.everhour.com/#/account/team).
3.  Locate the export section and download the **ZIP file** containing your team's complete time logs.
4.  Extract the ZIP file. You will typically use the **JSON** export for the migration script.

## Step 2: Make sure it is possible to map task and project identifiers

To successfully attribute time to the correct records in Asana, your data must map to existing Asana GIDs (Global Identifiers). In an Everhour export, Asana-synced tasks often include a prefix.

 

|                |                                     |                                          |
|----------------|-------------------------------------|------------------------------------------|
| **Data Field** | **Everhour Export Label (Sample)**  | **Required Asana Target**                |
| **Task ID**    | task.id (e.g., as:1212815283326608) | The numeric GID (e.g., 1212815283326608) |
| **Project ID** | task.projects                       | Asana Project GID                        |
| **Time Spent** | time (Seconds)                      | Asana duration_minutes                   |

> When processing the export, ensure you strip any as: prefixes from IDs to match Asana's internal GID format.

Step 3: Implement the migration script (Python)

The script below uses the [Asana Create Time Tracking Entry API](https://developers.asana.com/reference/createtimetrackingentry) to recreate logs. The logic utilizes email addresses to match users between systems, ensuring that time is attributed to the correct team member.

### Python

```
import asana

import json

# Initialize Asana Client

client = asana.Client.access_token('YOUR_PERSONAL_ACCESS_TOKEN')

workspace_gid = "YOUR_WORKSPACE_GID"

def migrate_everhour_to_asana(json_file_path, user_mapping_file_path):

    with open(json_file_path) as f:

        entries = json.load(f)

    # 1. Fetch Asana users to map emails to GIDs

    asana_users = {u['email']: u['gid'] for u in client.users.get_users_for_workspace(workspace_gid, opt_fields=['email', 'gid'])}

    

    # 2. Load a mapping of Everhour User IDs to Emails

    # (e.g., from Everhour's Team Member export)

    with open(user_mapping_file_path) as f:

        everhour_user_emails = {user['id']: user['email'] for user in json.load(f)}

    for entry in entries:

        everhour_user_id = entry['user']

        user_email = everhour_user_emails.get(everhour_user_id)

        

        # Match user by email

        asana_user_gid = asana_users.get(user_email)

        if not asana_user_gid:

            continue

        # Clean Task ID (remove 'as:' prefix)

        task_gid = entry['task']['id'].replace("as:", "")

        

        # Convert seconds to minutes for Asana API

        duration_mins = entry['time'] // 60 

        # 3. Create entry in Asana

        try:

            client.time_tracking_entries.create_time_tracking_entry(task_gid, {

                'created_by': asana_user_gid,

                'duration_minutes': duration_mins,

                'entered_on': entry['date'],

                'description': entry.get('comment', '')

            })

            print(f"Successfully migrated {duration_mins}m for Task {task_gid}")

        except Exception as e:

            print(f"Error for entry {entry['id']}: {e}")

migrate_everhour_to_asana('time_2026_01.json', 'users.json')
```

 

Why Migrate to Native Asana Time Tracking?

Moving your data into Asana allows you to leverage the full power of the **Timesheets and Budgets** addon:

- **Integrated Reporting:** View estimated vs. actual time directly in Asana Dashboards.
- **Automated Budgeting:** Set project budgets that update in real-time as team members log time.
- **Centralized Workflow:** Reduce tool-switching by keeping time logs where the work happens.
- Learn more about [Asana API](https://developers.asana.com/reference/time-tracking-entries)
- Learn more about [timesheets and budgets](https://help.asana.com/s/article/timesheets-and-budgets-add-on).
