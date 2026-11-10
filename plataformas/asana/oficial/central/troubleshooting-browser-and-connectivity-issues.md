---
fonte: https://help.asana.com/s/article/troubleshooting-browser-and-connectivity-issues?language=en_US
baixado: 2026-11-10
---

# Troubleshooting browser and connectivity issues

If you experience any of the following issues, please try the suggested troubleshooting steps. If the issue is not resolved, contact [Asana Support](https://help.asana.com/hc/en-us#chat) for assistance.

## Common browser and connectivity issues

#### Asana is stuck on the load screen

#### A popup message indicates you are **disconnected from the server**.

#### A popup message indicates **Asana needs to be reloaded**.

## Unique error phrase

If you see a unique error phrase, be sure to note it down so that you can send it to our support team if the troubleshooting tips below do not resolve your issue.

## Helpful troubleshooting tips

- Disable any browser extensions you have turned on
- Update your browser to the latest version
- Clear your browser’s history/cache/cookies
- Test for the issue in another one of our supported browsers below to see if the issue is isolated to only one browser or across multiple browsers
- Check your ability to establish a WebSocket with the [Asana Connectivity test](https://connectivity-test.asana.com/)
- Check the [Asana Status page](https://status.asana.com/ "Asana Status page") to see the current status of our servers

If you are still experiencing issues after trying the steps above, please contact our [Support team](https://asana.com/support "Support team"). Be sure to indicate exactly which steps you’ve already tried so that we can better assist you.

## Disable browser extensions

To disable browser extensions:

- In [Google Chrome](https://support.google.com/chrome/answer/187443 "Google Chrome")
- In [Safari](https://support.apple.com/en-us/HT203051#:~:text=Uninstall%20or%20turn%20off%20extensions,and%20click%20the%20Uninstall%20button. "Safari")
- In [Mozilla Firefox](https://support.mozilla.org/en-US/kb/disable-or-remove-add-ons "Mozilla Firefox")
- In [Microsoft Edge](https://support.microsoft.com/en-us/microsoft-edge/add-turn-off-or-remove-extensions-in-microsoft-edge-9c0ec68c-2fbc-2f2c-9ff0-bdc76f46b026 "Microsoft Edge")

> If you're using Chrome, [try using an Incognito window](http://support.google.com/chrome/bin/answer.py?hl=en&answer=95464 "try using an Incognito window") (which does not employ your installed extensions) to use Asana.

## Update browsers

Asana only supports the most up-to-date, official browser version. You may run into issues with Asana if you are running an outdated version of a browser. Ensure you have the best possible experience with Asana by updating your browser to the latest version.

To update your browser:

- In [Google Chrome](https://support.google.com/chrome/answer/95414 "Google Chrome")
- In [Safari](http://support.apple.com/en-us/HT6104 "Safari")
- In [Mozilla Firefox](https://support.mozilla.org/en-US/kb/update-firefox-latest-version "Mozilla Firefox")
- In [Microsoft Edge](https://support.microsoft.com/en-us/topic/microsoft-edge-update-settings-af8aaca2-1b69-4870-94fe-18822dbb7ef1 "Microsoft Edge")

## Clear browser history & cache

To clear your history:

- In [Google Chrome](https://support.google.com/chrome/answer/95589 "Google Chrome")
- In [Safari](http://support.apple.com/kb/PH19215 "Safari")
- In [Mozilla Firefox](https://support.mozilla.org/en-US/kb/delete-browsing-search-download-history-firefox "Mozilla Firefox")
- In [Microsoft Edge](https://support.microsoft.com/en-us/microsoft-edge/view-and-delete-browser-history-in-microsoft-edge-00cf7943-a9e1-975a-a33d-ac10ce454ca4 "Microsoft Edge")

> Uncheck the **Passwords** box when clearing your history if you want to retain any passwords you have saved in your browser.

## Compatible browsers

Asana works with the **latest versions** of:

- [Chrome](https://www.google.com/chrome/ "Chrome")
- [Safari for Mac](http://www.apple.com/safari/ "Safari for Mac")
- [Firefox](http://www.mozilla.org/ "Firefox")
- [Microsoft Edge](https://www.microsoft.com/en-ie/windows/microsoft-edge "Microsoft Edge")

If you receive an unsupported browser message, make sure you are using the latest version of the above browsers. More on unsupported browsers below.

## Unsupported browsers

Asana does not work with:

- Internet Explorer
- Opera
- Developer or Beta versions of supported browsers

Asana is a modern web application that uses some of the newest capabilities of HTML5, CSS3, and JavaScript. Different browsers still interpret these in different ways. These differences could potentially cause severe bugs - like data not saving, or data becoming corrupted and overwriting good data.

We test and develop for the list of compatible browsers and block access to Asana from those browsers listed as incompatible above. **This is in order to protect your data.**

> Mobile browser access to Asana is not supported. Instead you will need to utilise the Asana [mobile app](https://asana.com/guide/help/faq/all-asana-features#gl-mobile "mobile app") to use Asana on the go.

## Updating to TLS 1.2

At Asana, security is our top priority. Your web browser may be using an older encryption protocol, TLS 1.1, which has security flaws. To ensure the highest security standards, we are making improvements and retiring older encryption protocols in line with other software providers. This means that we no longer support TLS 1.1, and recommend that you update to version 1.2 or above.

More technical details can be found at our [developers site](https://developers.asana.com/docs "developers site").

Some older versions of browsers support TLS 1.1 by default, but you can manually enable TLS 1.2 by updating your browser to its most current version. If your company's IT team does not allow for browser updating, you will need to enable TLS 1.2 manually to ensure that you can continue to use Asana without any issues. All up-to-date browsers support TLS 1.2.

| Browser:        | No TLS 1.2 support: | TLS 1.2 support but not by default: | TLS 1.2 support by default: |
|-----------------|---------------------|-------------------------------------|-----------------------------|
| Google Chrome   | v1-v21              | v22-37                              | v38+                        |
| Mozilla Firefox | v1-v22              | v23-v26                             | v27+                        |
| Apple Safari    | v1-v6               |                                     | v7+                         |

If you are using any browsers that do not support TLS 1.2 at all, you will have to update your browser to a version that does support TLS 1.2 in order to use Asana.

If you are using any browser that supports TLS 1.2 but not by default, we encourage you to update your browser to a newer version that does support TLS 1.2 by default. If your network IT does not allow you to update your browser, you'll have to enable TLS 1.2 from your browser's settings.

If you believe your browser is up-to-date and you're experiencing issues, you can verify the security of the TLS your browser uses [here](https://howsmyssl.com/ "here").

If the page above shows that you are on TLS 1.1, you'll have to work with your company's IT team to update your connection to TLS 1.2.

## WebSockets

You are required to use WebSockets in order to use Asana and ensure that our latest version of the product works properly. Some Asana users may experience issues connecting over WebSockets when behind strict corporate firewalls or when using aged antivirus software.

If you're having trouble establishing a connection to Asana, we recommend the following steps:

- Test your connectivity [here](https://connectivity-test.asana.com/ "here") - if this site says that you have a successful WebSocket connection, you don't need to do anything further
- Contact your IT department and direct them to this article to diagnose the issue. They can check if your corporate firewall could be interfering with the connection. In this case, allowing \*.asana.com and \*.sync.app.asana.com should be sufficient
- You may need to update your anti-virus or firewall to the latest version to ensure that it's not blocking your connection
- If you're still seeing our top bar announcement or experience issues, contact our [Support team](https://asana.com/support "Support team").
