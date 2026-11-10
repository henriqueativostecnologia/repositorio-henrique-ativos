---
fonte: https://support.google.com/appsheet/answer/10106762?hl=en
baixado: 2026-11-10
---

# Use an Apigee data source

App creators can build apps in AppSheet using the data exposed by APIs managed by Apigee with the Apigee data source type.

**Note**: Both Apigee X and Apigee Edge are supported.

At this time, there are primarily two options to connect AppSheet apps to Apigee APIs: 

- Manual
- OpenAPI Spec

This article covers the detailed steps and the prerequisites for the API necessary to set up the connection from the AppSheet apps to Apigee managed APIs.

- [Quick start video](#video)
- [Set up the Apigee data source for AppSheet](#set-up-data-source)
- [Configure an OpenAPI Spec Apigee connection](#openapi)
- [Configure a Manual Apigee connection](#manual)
- [Prerequisites for your API proxy](#prerequisites)
- [Enable pagination](#pagination) (OpenAPI Spec Apigee connection only)
- [Specify filter parameters](#filter-params) (OpenAPI Spec Apigee connection only)
- [Support multiple parameters in an API path](#multiple-parameters) (OpenAPI Spec Apigee connection only)
- [Limitations and known issues](#limitation)
- [Troubleshoot](#troubleshoot)

##  Quick start video

Watch a video to learn how to use an Apigee data source in AppSheet.

**Note**: The concepts in this video are still valid, though the AppSheet UI has changed since this video was recorded.

Video: https://www.youtube.com/watch?v=2FVfPruDil4

## ****Set up the Apigee data source for AppSheet

To set up the Apigee data source for AppSheet, perform the following steps:

1.  [Set up authentication in Apigee](#set-up-authentication-Apigee)
2.  [Create the Apigee data source in AppSheet](#create-apigee-data-source)

### Set up authentication in Apigee 

To authenticate with an Apigee data source, you can choose one of the options described in the following table

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Authentication**                                                            | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| OAuth                                                                         | Set up OAuth validation in Apigee to provide an authorized way to access your |
|                                                                               | API. For more information, see:                                               |
|                                                                               |                                                                               |
|                                                                               | -   Apigee X: [Secure an API with                                             |
|                                                                               |     OAuth](https://cloud.google.com/apigee/docs/api-                          |
|                                                                               | platform/tutorials/secure-calls-your-api-through-oauth-20-client-credentials) |
|                                                                               | -   Apigee Edge: [Secure an API with                                          |
|                                                                               |     OAuth](https://docs.apigee.com/api-                                       |
|                                                                               | platform/tutorials/secure-calls-your-api-through-oauth-20-client-credentials) |
|                                                                               |                                                                               |
|                                                                               | **Note**: Currently the Apigee data source in AppSheet only supports the      |
|                                                                               | client credentials grant type. For more information, see:                     |
|                                                                               |                                                                               |
|                                                                               | -   Apigee X: [Implementing the client credentials grant                      |
|                                                                               |     type](https://cloud.google.com/ap                                         |
|                                                                               | igee/docs/api-platform/security/oauth/oauth-20-client-credentials-grant-type) |
|                                                                               | -   Apigee Edge: [Implementing the client credentials grant                   |
|                                                                               |     type](https://docs.ap                                                     |
|                                                                               | igee.com/api-platform/security/oauth/oauth-20-client-credentials-grant-type)  |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| API key                                                                       | Set up API key validation in Apigee to provide an authorized way to access    |
|                                                                               | your API. For more information, see:                                          |
|                                                                               |                                                                               |
|                                                                               | -   Apigee X: [Secure an API by requiring API                                 |
|                                                                               |     keys](https://cloud.google.com/apigee/                                    |
|                                                                               | docs/api-platform/tutorials/secure-calls-your-api-through-api-key-validation) |
|                                                                               | -   Apigee Edge: [Secure an API by requiring API                              |
|                                                                               |     keys](https://docs.apigee                                                 |
|                                                                               | .com/api-platform/tutorials/secure-calls-your-api-through-api-key-validation) |
|                                                                               |                                                                               |
|                                                                               | **Note**: The API key is passed back in the `x-apikey` header of each request |
|                                                                               | from AppSheet.                                                                |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| No authentication                                                             | Select API key and put any non-empty value (such as, `ABC`) into the API key  |
|                                                                               | field.                                                                        |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

### Create the Apigee data source in AppSheet

**Before you begin**: After you have configured authentication for your API and before you create the Apigee data source, review the [Prerequisites for your Apigee API proxy](#prerequisites) to ensure the API can be consumed by AppSheet.

To create the Apigee data source in AppSheet to create a connection to Apigee:

1.  Sign in to [appsheet.com](http://www.appsheet.com).
2.  Click **My account** in the top navigation bar.
3.  Select the **Sources** tab.
4.  Click **+ New Data Source**.
5.  Name your new Data Source and select **Apigee**.
    Add Apigee API connection information dialog

Configure an [OpenAPI Spec](#openapi) or [Manual](#manual) Apigee connection, as described in the following sections.

## ****Configure an OpenAPI Spec Apigee connection

If you have an OpenAPI Specification for your API proxy, you can configure an OpenAPI Spec Apigee connection. 

To configure an **OpenAPI Spec** Apigee connection:

1.  In the Add Apigee API connection information dialog, click **OpenAPI Spec**.
2.  To use OAuth authentication, select **OAuth** as the **Authentication Type** and configure the following settings.
    +-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Setting**                                                                   | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Apigee Client Id                                                              | Client ID generated by Apigee.                                                |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Apigee Client Secret                                                          | Client secret generated by Apigee.                                            |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| OpenAPI Spec URL                                                              | URL pointing to the OpenAPI 3.0 Spec. AppSheet will accept either JSON or     |
|                                                                               | YAML format. The URL must be publicly accessible as a REST endpoint.          |
|                                                                               |                                                                               |
|                                                                               | Appsheet will send a `GET` call to the URL to get the OpenAPI Spec.           |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
3.  To use API key authentication, select **ApiKey** as the **Authentication Type** and configure the following settings.
    +-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Setting**                                                                   | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Apigee API Key                                                                | API key generated by Apigee.                                                  |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| OpenAPI Spec URL                                                              | URL to the OpenAPI Spec.                                                      |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Custom Headers                                                                | Custom headers to send with all requests to Apigee. Click **Add** and specify |
|                                                                               | the header name and value. Repeat to add additional custom headers.           |
|                                                                               |                                                                               |
|                                                                               | **Note**: You can add up to 20 custom headers. Custom header names and values |
|                                                                               | cannot exceed 1000 characters each.                                           |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
4.  To validate the connection, click **Validate**.
    AppSheet makes a `GET` call to the OpenAPI Spec URL and parses the OpenAPI Spec. Then, AppSheet makes `GET` calls to each table resource after they are inferred from the OpenAPI Spec.
5.  Click **Authorize Access** to add the data source.

## ****Configure a Manual Apigee connection

If you don't have an OpenAPI Specification available for your API, configure a Manual Apigee connection. 

To configure a **Manual** Apigee connection:

1.  In the Add Apigee API connection information dialog, click **Manual**.
2.  To use OAuth authentication, select **OAuth** as the **Authentication Type** and configure the following settings.
     
    |                                 |                                                                                               |
|---------------------------------|-----------------------------------------------------------------------------------------------|
| **Setting**                     | **Description**                                                                               |
| Apigee Authorization Token URL  | URL of your API proxy that handles the Access token generation.                               |
| Apigee Client Id                | Client ID generated by Apigee.                                                                |
| Apigee Client Secret            | Client secret generated by Apigee.                                                            |
| Authorization Scopes (Optional) | Scopes of your authorization if defined in your policy.                                       |
| Apigee API Base Path            | Base path of your Apigee proxy.                                                               |
| API Resource Paths              | Comma-separated list of API proxy endpoints. The paths correspond to table names in Appsheet. |
3.  To use API key authentication, select **ApiKey** as the **Authentication Type** and configure the following settings.
    +-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Setting**                                                                   | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Apigee API Key                                                                | API key generated by Apigee.                                                  |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Apigee API Base Path                                                          | Base path of your Apigee proxy.                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| API Resource Paths                                                            | Comma-separated list of API proxy endpoints. The paths correspond to table    |
|                                                                               | names in AppSheet.                                                            |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Custom Headers                                                                | Custom headers to send with all requests to Apigee. Click **Add** and specify |
|                                                                               | the header name and value. Repeat to add additional custom headers.           |
|                                                                               |                                                                               |
|                                                                               | **Note**: You can add up to 20 custom headers. Custom header names and values |
|                                                                               | cannot exceed 1000 characters each.                                           |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
4.  To test the connection, click **Test Connection**.
    - **For OAuth authentication**: AppSheet makes a `POST` call with Apigee Client Id and Apigee Client Secret to the Apigee Authorization Token URL and gets the access token. Then, using the access token AppSheet makes a `GET` call to all of the `{Apigee API Base Path}/{API Resource Path}` paths to verify access.
    - **For API key authentication**: AppSheet makes a `GET` call to all of the `{Apigee API Base Path}/{API Resource Path}` paths to verify access.
5.  Click **Authorize Access** to add the data source.

## ****Prerequisites for your API proxy

Depending on the type of Apigee data source setup (Manual or OpenAPI Spec), there are some additional requirements for the underlying Apigee API proxy APIs to ensure compatibility with AppSheet.

### OpenAPI Spec Apigee connection

When you configure an OpenAPI Spec Apigee connection, ensure that the Apigee API proxy supports the required API operations described in [Required operations for the API proxy](#required-operations). 

In addition, the OpenAPI Spec must conform to the following guidelines:

- Servers must have exactly one entry as a base path

- For the OAuth authentication type:

  - Must include `components:securitySchemes` section
  - When the `components:securitySchemes` type is `oauth2`, flows must be specified as `clientCredentials`
  - `tokenUrl` must be provided
  - `scopes` is optional

  Example `components` snippet in OpenAPI Spec: 

  `components:`
  `securitySchemes:`
  `  oAuth2ClientCredentials:`
  `    type: oauth2`
  `    Description:  Experimental Apigee APIs`
  `    Flows:`
  `      clientCredentials:`
  `        tokenUrl: https://appsheet-test.apigee.net/oauth2/token/`
  `        scopes:  #Can be empty {}`
  `          read: Grant read-only access`

- If you provide the schema of the response body for `GET /tableName/{id}`, AppSheet will infer the column type from it. Otherwise, AppSheet will directly try to infer the column type from the actual response.

The OpenAPI Spec endpoint can be hosted within or outside Apigee. For example (SwaggerHub): [Sample OpenAPI Specification](https://api.swaggerhub.com/apis/kurtkanaskie/persons-v1/1.0.0) 

Replace the `app.swaggerhub.com` with `api.swaggerhub.com` to get the correct API-based URL.

**Note:** The API Key provided will be passed in the header as `x-apikey` when making a request to fetch the OpenAPI Spec.

### Manual Apigee connection

When you configure a Manual Apigee connection, ensure that the Apigee API proxy supports the required API operations described in [Required operations for the API proxy](#required-operations). 

### Required operations for the API proxy

For each table, the following operations are required: 

- [Get all entries in a table](#get-all-entries)
- [Get an entry in a table](#get-an-entry) (required for write operations)

The following API operations are optional:

- [Create an entry in a table](#create-entry)
- [Update an entry in a table](#update-entry)
- [Delete an entry in a table](#delete-entry)

#### Get all entries in a table (Required)

To get all entries in a table, the Apigee API proxy must support the following API operation:

`GET /{tableName} ` 

Where:

- `{tableName}` - Name of the table.

The response body consists of a JSON payload with the table name, for example `"orders"`, as the key that includes the details for all rows in the table. For example:

`{`
`  "orders": [`
`  {`
`    "ID": 1,`
`    "TextValue": "Order1",`
`    "DecimalValue": 1.10,`
`    "DateTime": "1/1/2016 1:01:01 AM",`
`    "PhoneValue": "111 111 1111",`
`    "EmailValue": "email1@appsheet.com"`
`  },`
`  {`
`    "ID": 2,`
`    "TextValue": "Order2",`
`    "DecimalValue": 1.11,`
`    "DateTime": "2/1/2016 1:01:01 AM",`
`    "PhoneValue": "111 112 1111",`
`    "EmailValue": "email2@appsheet.com"`
`  }`
`  ]`
`}`

#### Get an entry in a table (Required for write operations)

**Note**: This API operation is required to support **write** operations.

To get an entry in a table, the Apigee API proxy must support the following API operation: 

`GET /{tableName}/{id}` 

Where:

- `{tableName}` - Name of the table.
- `{id}` - Unique ID for the table entry. This ID is mapped to the key column by the app creator in the editor, as described in [Set the key and editable columns in AppSheet](#set-key-editable-column).

The response body consists of a JSON payload that includes the details for the selected row. 

#### Create an entry in a table (Optional)

To support creating an entry in a table, the Apigee API proxy must support the following API operation:

`POST /{tableName}`

Where:

- `{tableName}` - Name of the table.
- `{id}` - Unique ID for the table entry. This ID is mapped to the key column by the app creator in the editor, as described in [Set the key and editable columns in AppSheet](#set-key-editable-column).

  The request body contains the details for the row to be created. The columns specified in the payload must be marked as **Editable** by the app creator in the editor, as described in [Set the key and editable columns in AppSheet](#set-key-editable-column).

#### Update an entry in a table (Optional)

To update an entry in a table, the Apigee API proxy must support the following API operation:

`PUT /{tableName}/{id}` 

Where:

- `{tableName}` - Name of the table.
- `{id}` - Unique ID for the table entry. This ID is mapped to the key column by the app creator in the editor, as described in [Set the key and editable columns in AppSheet](#set-key-editable-column).

The request body contains the details for the row to be updated. The updated columns must be marked as **Editable** by the app creator in the editor, as described in [Set the key and editable columns in AppSheet](#set-key-editable-column).

#### Delete an entry in a table (Optional)

To delete an entry in a table, the Apigee API proxy must support the following API operation:

`DELETE /{tableName}/{id}`

Where:

- `{tableName}` - Name of the table.
- `{id}` - Unique ID for the table entry. This ID is mapped to the key column by the app creator in the editor, as described in [Set the key and editable columns in AppSheet](#set-key-editable-column).

### Set the key and editable columns in AppSheet

To support write operations on table entries, you must enable the following settings in the table columns:

- **Key?** - Uniquely identifies a table entry. See [What is a key?](https://support.google.com/appsheet/answer/10106672)
- **Editable?** Enables you to perform write operations on the column.

 When calling write operations, AppSheet will send APIs to `/{tableName}/{id}` with the request body. In the above example, `id` is the key column. See [Best practices for the id field](#best-practices-id). The fields in the request body will include the columns marked as **Editable**, such as `id`, `age`, and `name` in the above example.

### Best practices for the ID field

The preferred solution is to have one ID field generated by AppSheet using expressions like [`UNIQUEID()`](https://support.google.com/appsheet/answer/10108209). If the generation of the id field occurs in the backend:

- We recommend using two fields in your API payload that can act as the primary key for that entry. One generated and sent by AppSheet in the `POST` request body and the other one generated by the backend.
- For the AppSheet-generated ID, you can use the expression [*`UNIQUEID()`*](https://help.appsheet.com/en/articles/2357317-uniqueid) as the initial value.
- The backend-generated ID field will be left empty in the `POST` request body and will be populated on the next Sync after the creation of a new row.

The API should operate with the `{id}` parameter input with either the AppSheet ID or the backend-generated ID. In other words, the ID matching needs to work with either of the column values. AppSheet will always use the AppSheet-generated ID for its API calls.

If your API can only support one ID field that is generated by the backend, then:

- AppSheet will need to generate a temporary unique ID in the API’s `{id}` field (use expression `UNIQUEID()` in the **Initial Value** setting for the API ID column).
- When the `POST` operation is called, the backend will generate its own key for the entry, which will overwrite the value that AppSheet generated and passed in the `POST` body.
- On the next Sync after the create (`POST`) operation is finished, AppSheet will retrieve the ID generated by the backend, and the temporary ID generated by AppSheet will be overwritten.
- This can cause issues in cases where a row is created and updated (or deleted) before a Sync operation occurs. Since the operations are queued, id used for the update operation will be the temporary id generated by AppSheet and this will not exist in the backend.

## ****Enable pagination

**Note**: Pagination can be enabled for OpenAPI Spec Apigee connections only.

To enable pagination for your API, the OpenAPI Spec must specify an `x-pagination` extension for the `GET ALL` operation as an [OpenAPI extension](https://swagger.io/docs/specification/openapi-extensions/). The Apigee data source supports offset-based and cursor-based pagination directives.

General parameters：

- **Type (required)**: `offset` \| `cursor`
- **limitParam (required)**: The param key in parameters object. Example: `limit`
- **defaultLimit**: Default value of limit; if not specified, it will be set as 50

Offset-based parameters:

- **offsetParam (required):** The offset param key in parameters object
- **defaultOffset**: Default value of offset, if not specified, it will be set as 0

Cursor-based parameters:

- **cursorParam (required)**: The cursor param key in parameters object

**Example: Offset-based parameters in OpenAPI Spec YAML**

`/users:`
`    get:`
`      tags:`
`      - person`
`      parameters:`
`      - name: limit`
`        in: query`
`        required: false`
`        schema:`
`          type: integer`
`          format: int64`
`      - name: offset`
`        in: query`
`        required: false`
`        schema:`
`          type: integer`
`          format: int64`
`      responses:`
`        '200':`
`          description: Array of all person in the system with filter and pagination`
`          content:`
`            application/json:`
`              schema:`
`                type: array`
`                items:`
`                  $ref: '#/components/schemas/Person'`
`      x-pagination:`
`        type: offset`
`        limitParam: limit`
`        defaulLimit: 30`
`        offsetParam: offset`
`        defaultOffset: 0`

**URL**：

    api/users?limit=30&offset=0

 

**Example: Cursor-based parameters in OpenAPI Spec YAML**

    /users:

    get:
          tags:
          - person
          parameters:
          - name: page_size
            in: query
            required: false
            schema:
              type: integer
              format: int64
          - name: page_token
            in: query
            required: false
            schema:
              type: integer
              format: int64
          responses:
            '200':
              description: Array of all person in the system with filter and pagination
              content:
                application/json:
                  schema:
                    type: array
                    items:
                      $ref: '#/components/schemas/Person'
          x-pagination:
            type: cursor
            limitParam: page_size
            defaulLimit: 30
            cursorParam: page_token

**URL**：

    api/users?page_size=30&page_token=GIYDAOBNGEYS2MBWKQYDAO

## ****Specify filter parameters (query parameters/security filters)

**Note**: Filter parameters can be used for OpenAPI Spec Apigee connections only.

To specify a filter for a table, the OpenAPI Spec must specify an `x-filter` extension for `GET ALL` operation as an [OpenAPI extension](https://swagger.io/docs/specification/openapi-extensions/) and must specify a type of filter.  Apigee data source only supports `RHS-Colon` and `LHS-Brackets`.

**Example: RHS-Colon**

    /users:
        get:
          tags:
          - publisher
          summary: Get all person
          responses:
            '200':
              description: Array of all person in the system with filter and pagination
              content:
                application/json:
                  schema:
                    type: array
                    items:
                      $ref: '#/components/schemas/Person'
            '500':
              description: Internal server error.
          x-filter:
            type: RHS-Colon

 

Make sure that you put a space in between the type: and the `RHS-Colon` or `LHS-Brackets`.

For example, the following syntax won’t work: `type:RHS-Colon`

Correct syntax with a space: `type: RHS-Colon`

The `x-filter` directive only supports the operators in the table below. The table also shows the mapping between security filter resources and URL request (using age in the users table as example).

AppSheet’s security filter for the Apigee data source will be passed down to the API via these query parameters using the scheme (`RHS-Colon` or `LHS-Brackets`) as specified in the OpenAPI Spec. The operators supported are shown in the following table.

|                                       |                                      |                     |                       |                          |
|---------------------------------------|--------------------------------------|---------------------|-----------------------|--------------------------|
| **AppSheet Security Filter Operator** | **AppSheet Security Filter example** | **Filter operator** | **RHS-Colon example** | **LHS-Brackets example** |
| =                                     | \[age\]=25                           | eq                  | api/users?age=eq:25   | api/users?age\[eq\]=25   |
| \<\>                                  | \[age\]\<\>25                        | neq                 | api/users?age=neq:25  | api/users?age\[neq\]=25  |
| \>                                    | \[age\]\>25                          | gt                  | api/users?age=gt:25   | api/users?age\[gt\]=25   |
| \>=                                   | \[age\]\>=25                         | gte                 | api/users?age=gte:25  | api/users?age\[gte\]=25  |
| \<                                    | \[age\]\<25                          | lt                  | api/users?age=lt:25   | api/users?age\[lt\]=25   |
| \<=                                   | \[age\]\<=25                         | lte                 | api/users?age=lte:25  | api/users?age\[lte\]=25  |

## Support multiple parameters in an API path

**Note**: Multiple path parameters can be used for OpenAPI Spec Apigee connections only.

The OpenAPI Spec Apigee connection supports multiple parameters in API paths that are defined in an OpenAPI Spec.  For example:

`/parentName/{parent}/tableName/{id}:`
`    get:`
`      parameters:`
`      - name: parent`
`        in: path`
`        required: true`
`        schema:`
`          type: integer`
`          format: int64`
`      - name: id`
`        in: path`
`        required: true`
`        schema:`
`          type: integer`
`          format: int64`

`...`

The path parameters `{parent}` and `{id}` should map to valid columns in the [`GET /myTable`](#get-all-entries) response: 

- The primary key for `tableName` is inferred as `{id}`.
- The parent table key for `tableName` is inferred as the `{parent}`.
- The parent table must be defined in the same OpenAPI Spec. For example, both `/publishers/{id}` and `/publishers/{publisher}/books/{id}` must be defined.

If you use a child table to create an app using an OpenAPI Spec with two path parameters, the Apigee data source will generate two tables (one for the parent and one for the child table) and automatically set up a reference column between the tables. In this case, the parent table must be defined in the same OpenAPI Spec. For example, both `/publishers/{id}` and `/publishers/{publisher}/books/{id}` must be defined in the spec.

**Notes**:

- Currently, the Apigee data source only supports **two** path parameters in an OpenAPI spec.

- Each OpenAPI Spec path must adhere to the [OpenAPI Spec 3.0 requirements](https://swagger.io/specification/) for the Apigee data source in AppSheet.

## ****Limitations and known issues

The following lists the limitations and known issues:

- Row limits are not currently supported. Use [filter params](#filter-params) to limit the data returned.
- Response types of all APIs are expected to be `application/json`.
- During [create an entry in a table](#create-entry) operation, ID values should be generated inside AppSheet as a best practice. See [Best practices for the ID field](#best-practices-id).
- The path parameters should always be at the end of the path string.
- Only the REST operations defined in [Required operations for the API proxy](#required-operations) are supported.
- The fields in the responses should not be nested, the fields should be of simple types like int, string, or list that can be converted into [AppSheet data column types](https://support.google.com/appsheet/answer/10106435).

The OpenAPI Spec-based Apigee connection doesn’t strictly adhere to OpenAPI:

- Doesn’t use resource definition in OpenAPI Spec, uses superset of responses from `GET /resources` to build columns.
- AppSheet assigns emails and phone number data types as required during initial data source creation. The App creator can adjust data after the table is created in the app.
- Doesn’t recognize the security schemes for API Key. AppSheet sends the API Key as `x-apikey` header only.

## Troubleshoot

You may encounter the following exceptions when creating and testing your app. Examples and possible solutions are provided.

`Your client credentials are invalid. Please ensure your Apigee client credentials and token url are correct.`

Ensure your credentials are correct. For the OAuth type, you can verify your credentials by calling the following curl command. (curl is available on Linux-based systems. For MS DOS, you may need to install a third-party curl program). If you need assistance, contact an Apigee administrator, developer,  or IT staff.

`curl -X POST -H "Content-Type: application/x-www-form-urlencoded" \`
`“tokenUrl” \`
`-d "client_id={key}&client_secret={secret}"`

You should get a `200` response with `access_token` in the response body. For example:
`{`
`   ...`
`   "token_type" : "BearerToken",`
`   "client_id" : "xNnREu1DNGfiwzQZ5HUN8IAUwZSW1GZW",`
`   "access_token" : "GTPY9VUHCqKVMRB0cHxnmAp0RXc0",`
`   "refresh_token_expires_in" : "30000", //--in seconds`
`   ...`
`}`

Then, call the API with the access token:

`curl https://{org-name}-test.apigee.net/tablename \`
`-H "Authorization: Bearer {access-token}"`

Parsing of OpenAPI Spec failed. Error: The Apigee data source requires both the \`GET /tableName\` and 'GET /tableName/id'

Make sure every table in the spec includes both `GET tableName` and `GET /tableName/id` operations. For more details, see [Prerequisites for your API proxy](#prerequisites).

`Error: Table 'table' is no longer connected to its schema/column structure.` 

If the Apigee data source successfully passes the test step and is authorized, but shows this error while creating the app, check the response format of the `GET tableName`. This API is expected to return a list of rows with the key for this list as the table name/proxy endpoint. For more details, see [Prerequisites for your API proxy](#prerequisites).
