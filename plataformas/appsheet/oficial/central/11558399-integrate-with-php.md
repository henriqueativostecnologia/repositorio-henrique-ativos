---
fonte: https://support.google.com/appsheet/answer/11558399?hl=en
baixado: 2026-11-10
---

# Integrate with PHP

You can create a bot in your AppSheet app that will post a JSON payload to a PHP service that you created.

To do this:

1.  [Call a webhook from a bot](https://support.google.com/appsheet/answer/11511244) in your AppSheet app.
2.  Add a JSON **Body Template**.
3.  The template controls the format of the JSON data sent in the body of the webhook post.
4.  Your PHP code that is invoked by the webhook post can retrieve the post body data by specifying:
    `$postdata = `*`json_decode`*`(`*`file_get_contents`*`("php://input"));`
5.  After successfully processing the webhook request, your PHP code should return a JSON object containing: `{"Status":"Success"}`
