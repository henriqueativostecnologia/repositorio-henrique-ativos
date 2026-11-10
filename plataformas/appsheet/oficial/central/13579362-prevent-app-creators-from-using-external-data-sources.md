---
fonte: https://support.google.com/appsheet/answer/13579362?hl=en
baixado: 2026-11-10
---

# Prevent app creators from using external data sources

Prevent app creators from using external data sources by using the "Restrict external data sources and auth domains" policy, as described below. For more information, see [Define governance policies](https://support.google.com/appsheet/answer/11948767).

To prevent app creators from using external data sources, do the following:

1.  Select **My account \> Policies**.
2.  Click **+ Account Policy** or **+ Team Policy** to add an account or team policy, respectively.
3.  Select **Restrict external data sources and auth domains** from the **Policy Template** drop-down.
4.  Click **Next**.
5.  The policy is preconfigured for you. You can modify any of the field values. See [Add a predefined policy](https://support.google.com/appsheet/answer/11948767#add-predefined-policy) for a description of each field. 
    **Important**: If you modify the **Condition** field, ensure that you retain the functionality defined below: 
    NOT(\[HasExternalAuth\])
6.  Click **Save**.
