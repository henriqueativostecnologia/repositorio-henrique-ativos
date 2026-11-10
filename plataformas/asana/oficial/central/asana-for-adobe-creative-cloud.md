---
fonte: https://help.asana.com/s/article/asana-for-adobe-creative-cloud?language=en_US
baixado: 2026-11-10
---

# Asana for Adobe Creative Cloud

**Please note that the Asana for Adobe Creative Cloud integration will be retired on April 15, 2026. Please review our [FAQ article](https://help.asana.com/s/article/deprecation-of-integrations) for further guidance.**

**Available on Asana [*Advanced*](https://asana.com/plan/advanced), [*Enterprise*](https://asana.com/enterprise), and [*Enterprise+*](https://asana.com/enterprise) tiers, as well as [*legacy tiers*](https://asana.com/pricing-legacy) Business and Legacy Enterprise.**

**Visit our [*pricing page*](https://asana.com/pricing) for more information.**

Asana for Adobe Creative Cloud is an integration between Asana and key Adobe Creative Cloud software - Photoshop, Illustrator and InDesign.

The integration is an extension or ‘panel’ inside each of the 3 Adobe applications.

> Asana for Adobe Creative Cloud is built on the [now deprecated CEP framework](https://developer.adobe.com/photoshop/uxp/2022/guides/uxp_for_you/uxp_for_cep_devs/#:~:text=Goodbye%20CEP,juggle%20two%20different%20JavaScript%20environments.) and is not actively being maintained. There are reported compatibility issues with Apple silicon chips and we don't support newer versions of Mac computers out of the box.

## Install Asana for Adobe Creative Cloud

The extension can be installed via the [Adobe Exchange site](https://www.adobeexchange.com/creativecloud.details.101407.asana-for-adobe-creative-cloud.html "Adobe Exchange site"), which is Adobe's extension directory.

> You need to have supported versions of the 3 apps in order to use the extension. Currently we support the 2021 version of Photoshop CC, Illustrator CC and InDesign CC.

Once installed via the Exchange website, the Creative Cloud desktop app will sync the extension to your computer. Please ensure you have installed all updates.

#### Once the extension has been synced and you restart your Adobe Photoshop/Illustrator/InDesign:

1.  Access the **Window** tab
2.  Hover over **Extensions** and select **Asana**

Opening the extension opens a panel in your Adobe software with the Asana extension. From here you can login (if you already have an Asana account) or sign up (if you don’t).

Once you log in, you will be required to authenticate the integration in Asana.

## Access My tasks and task details

After logging in, you will be presented with a view of your **My tasks**.

Clicking on a task takes you into the task details view.

> You can create and view a task's subtasks and approvals once you are in the task details view

#### From the task details view, you can:

1.  Mark the task complete
2.  Attach the file you're working on and choose your file type
3.  Navigate to Asana
4.  View the task's name, due date & description
5.  View/delete existing attachments or attach a new file
6.  Write a new comment or review existing comments

> You can also open a new file to work on by clicking on any compatible attachment. Clicking an incompatible file will yield an error message.

## Search for other tasks and projects

Use the search field to find a task not assigned to you or to find a specific project.

By selecting a project, you will then be brought to that **project view**.

To return to **My tasks**, click on the home icon in the top right hand corner of the plug-in.

## Toggle between organizations and workspaces

From the **My tasks** page, clicking the profile icon on the top left will allow you to toggle between your organizations and workspaces or log out.

## Using the integration with an Apple M1 or M2 chip

Following a recent change to Adobe Creative Cloud, Adobe Photoshop users will run into difficulty using the integration if their Macbook device uses an Apple M1 or M2 chip. We recommend the following workaround which involves running Photoshop in a compatibility mode called **Rosetta**.

First, you will need to download Rosetta. To do this, open the application on your Macbook called **Terminal**. In Terminal, paste the following command and hit enter:

*/usr/sbin/softwareupdate --install-rosetta*

Once Rosetta is installed, you need to open Photoshop in Rosetta by following these steps:

1.  Ensure Photoshop has been fully quit before proceeding
2.  Go to **Finder \> Applications \> Photoshop**
3.  Right-click the Photoshop application
4.  Select **Get Info**
5.  In the infobox, check the box beside **Open using Rosetta**
6.  Close the infobox
7.  Launch Photoshop, and it will open using Rosetta

> There may be some performance degradation in Rosetta compatibility mode. Other Adobe Creative Cloud integrations are unaffected by using M1 and M2 chips.

 

[](https://forum.asana.com/c/forum-en/tips/6)
