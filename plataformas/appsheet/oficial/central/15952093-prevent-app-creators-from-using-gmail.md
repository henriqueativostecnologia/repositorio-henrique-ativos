---
fonte: https://support.google.com/appsheet/answer/15952093?hl=en
baixado: 2026-11-10
---

# Prevent app creators from using Gmail

Prevent app creators from using Gmail by defining a governance policy. For more information, see [Define governance policies](https://support.google.com/appsheet/answer/11948767).

To prevent app creators from building automations using Gmail:

1.  Select **My account \> Policies**.

2.  Click **+ Organization Policy** or **+ Team Policy** to add an account or team policy, respectively.

3.  Select **Custom Policy** from the **Policy Template** drop-down.

4.  Click **Next**.

5.  Configure the policy as follows:
     

    |                 |                                                   |
|-----------------|---------------------------------------------------|
| **Setting**     | **Value**                                         |
| Name            | **Disable Gmail event **or other descriptive name |
| Component       | **Events**                                        |
| Condition       | `NOT([EventType]='Gmail')`                        |
| Severity        | **Error**                                         |
| Target          | **All Apps**                                      |
| Stage           | **Enforce always**                                |
| Description     | **Apps must disable Gmail event functionality**   |
| Success Message | Success                                           |
| Failure Message | This app can't use Gmail events                   |

6.  Click **Save**.
