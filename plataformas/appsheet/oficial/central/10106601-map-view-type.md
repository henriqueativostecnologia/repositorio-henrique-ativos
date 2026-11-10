---
fonte: https://support.google.com/appsheet/answer/10106601?hl=en
baixado: 2026-11-10
---

# Map view type

The map view allows you to display locations within your app. Depending on the app requirements, you can display location data, drop pins, and provide directions with your app. 

Maps can be displayed in road or aerial view and can be zoomed and panned. By default, the map is zoomed to show all the pins. If your map includes locations in both Australia and Canada, it may be zoomed to show half the world.

The location data points can come from `Address`,`LatLong` (GPS) information, or `XY` (coordinates of a point). You can use either Google maps to display your mapped locations (`Address` and `LatLong`) or a custom image such as the interior map of a manufacturing plant to map `XY` points.

Map view example

The following sections describe how to create, configure, and customize map views:

- [Get started using map views](#get-started)
- [Create a map view](#create-map-view)
- [Configure the map view options](#configure-map-view)
- [Use map pins](#customize-map-pins)
- [Get driving directions](#driving-direction)
- [Use your Google Maps integration](#use-google-maps-integration)
- [Use KML layers to display geographic data](#use-kml-layers)
- [About map view location data points](#about-map-view-types)

## Get started using map views

Get started using map views by viewing the **Active Jobs** map view in the [Field Delivery sample app](https://www.appsheet.com/templates/Track-pending-in-progress-and-completed-deliveries) 

## Create a map view

To create a map view:

1.  Create a view, as described in [Create a view](https://support.google.com/appsheet/answer/10101818#create-view).
2.  Select **map** as the **View type** when configuring the card view details, as described in [View details](https://support.google.com/appsheet/answer/10106688#view-details).
3.  Configure the [map view options](#configure-map-view).
4.  Configure the **Display**, **Behavior**, and **Documentation** settings, as described in [Configure the view](https://support.google.com/appsheet/answer/10106688#configure-view).
5.  Save your app.

##  

## Configure the map view options

Configure the map **View options** by using the settings described in the following table.

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Setting**                                                                   | **Description**                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Map column                                                                    | Select column to use for location data from the drop-down. See also [About    |
|                                                                               | map view location data points](#about-map-view-types).                        |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Secondary data table                                                          | Optional. Select a table that defines a secondary data layer for the map.     |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Map type                                                                      | Select the type of map to show. Options include:                              |
|                                                                               |                                                                               |
|                                                                               | -   **Automatic** - AppSheet selects the map type.                            |
|                                                                               | -   **Road** - Shows transportation infrastructure, including roads, speed    |
|                                                                               |     limits, and so on.                                                        |
|                                                                               | -   **Aerial **- Shows Google Earth satellite images.                         |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Location mode                                                                 | Select how frequently you want to update your current location on the map.    |
|                                                                               |                                                                               |
|                                                                               | -   **None** - Hide the location marker.                                      |
|                                                                               | -   **Normal** - Updates location marker at a medium cadence.                 |
|                                                                               | -   **High** - Updates location marker at a high cadence. **This setting      |
|                                                                               |     might quickly drain the battery of a mobile device.**                     |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Minimum cluster size                                                          | Set the pin cluster size. When the number of pins occur in close proximity,   |
|                                                                               | they will be displayed as a single cluster for improved performance.          |
|                                                                               |                                                                               |
|                                                                               | Set to 0 to disable clustering.                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

## Use map pins

Each location is displayed as a map pin. You can click or tap a map pin to select it. When you select a map pin:

- The map centers on the selected map pin.
- Information about the selected map pin is displayed using one of the following views depending on the screen size:
  - Sidebar view - Detail view of the record; the same view displayed when selecting the row in a table view.
  - Compact view - Single deck view row at the bottom of the screen.

Each view includes a built-in driving directions action (car icon) that will launch Google Navigation from the current location to that destination. (iOS users will need to install Google Maps for this feature to work). The views can be configured using [reference views](https://support.google.com/appsheet/answer/10106516).

You can customize the map pins, as described in the following sections:

- [Control the number of pins displayed](#control-number-of-pins)
- [Customize the pin color and icon style using format rules](#pin-color-style)
- [Show or hide points of interest](#points-of-interest)

### Control the number of pins displayed

For performance reasons, only a limited number of pins can be displayed at once. If the total pins exceed the limit, the map will prioritize showing pins closest to the center of the current view.

You can control the number of pins displayed by using the **Map pin limit** setting when [configuring global map view settings](https://support.google.com/appsheet/answer/10107387#map-view).

Map pin limit in the Map View options

### Customize the pin color and icon style using format rules

Customize the color and icon style of map pins using format rules. You can apply format rules selectively to format a set of map pins one way, and other map pins another way. This allows you to highlight certain map pins or to categorize map pins into groups.

To get started, watch the following video.

Video: https://www.youtube.com/watch?v=kXJIYs-6ZE8

To customize map pins:

1.  Open the app in the editor.
2.  Go to **App ** App icon **\> Format Rules** and click **+** in the Format rules heading to create a new format rule.
     We've made some [improvements to the app editor](https://support.google.com/appsheet/answer/12490168).
    You are **opted in** **to the new editor** by default, but you can [switch back to the legacy editor](https://support.google.com/appsheet/answer/12490168) at any time.

    ## If you are using the legacy editor

    Go to **UX \> Format rules** and click **+New Rule** to create a new format rule.
3.  In the **For this data** drop-down, select the table containing the `Address` or `LatLong` field.
4.  In the **Then format these columns** list, select the name of the `Address` or `LatLong` field.
5.  In the **Highlight color** setting, enter the map pin color you wish by specifying its hex color code. For example, `#FF0000` for red, `#00FF00` for green, `#0000FF` for blue, `#FFFF00` for yellow, `#00FFFF` is cyan, `#FF00FF` is magenta, and so forth. 
6.  In the **Icon** setting, click the preferred icon.
7.  In the **If this condition is true** setting, enter a `Yes/No` expression. The format rule will be applied when the expression is `TRUE`.

Create a format rule for each map pin format you wish. Specify the appropriate **If this condition is true** expression to apply that format rule to the map pins you wish.

### Show or hide points of interest

Show or hide points of interest on the map view by using the **Hide points of interest** setting when [configuring global map view settings](https://support.google.com/appsheet/answer/10107387#map-view).

## Get driving directions

You must install Google Maps on iPhone and iPad devices to get driving directions.

To get driving directions, click the map pin. A small car icon will appear at the bottom of the app. Click the car icon to activate Google Maps driving directions.

## Use your Google Maps integration

Use the Google Maps key from the account settings for geocoding requests by using the **Use my google Maps integration **setting when [configuring global map view settings](https://support.google.com/appsheet/answer/10107387#map-view).

You must turn on this setting if you have more than 1000 geocoded addresses per month.

## Use KML layers to display geographic data

KML (Keyhole Markup Language) is a file format used to display geographic data, most commonly on platforms like Google Earth or Google Maps, that allows for embedding and displaying location points, borders and shapes with different styles. To learn more about KML, review this [Community post.](https://community.appsheet.com/t/kml-map-layer/55)

To enable a KML layer in your map, edit the column definition of any `Address` or `LatLong` column type to add a link to a hosted KML file in the **Optional Url form KML File** setting. 

There are some constraints on the size of KML files that can be displayed:

- Maximum fetched file size (raw or compressed): 3MB
- Maximum uncompressed KML file size: 10MB
- Maximum number of network links: 10
- Maximum number of total document-wide features: 1000
- Maximum number of KML layers: 10 to 20

These constraints are established by Google Maps; AppSheet doesn't have the ability to modify them.

Download an example of a KML file that fits these constraints: [https://code.google.com/apis/kml/documentation/us_states.kml](https://code.google.com/apis/kml/documentation/us_states.kml)

Here are a couple of sites with interesting KML files:

- [Donny's Resources](https://sites.google.com/mrpiercey.com/resources/geo/kml-downloads)
- [South Australian Government Data Directory](https://data.sa.gov.au/data/dataset?res_format=KML)
- [US Census Bureau](https://www.census.gov/geographies/mapping-files/time-series/geo/kml-cartographic-boundary-files.html)

## About map view location data points

Map view location data points can come from an [address](#address), [LatLong](#latlong) (GPS) information, or [XY](#xy) (coordinates of a point).

### Address data

When you enter an address, always specify the complete address including the city, state (if any), and country. This makes it easier for Google Maps to locate the address. A column header called **Address** will help AppSheet identify the column more efficiently.

If an `Address` is not mapped correctly, look up the address on [Google Maps](https://maps.google.com/) to see if there is a problem with the address. If you add many addresses at once to the data source, there may be a delay before you see all the addresses appear on the map within the app because each address must be geocoded before its position can be displayed.

### LatLong data

`LatLong` data is represented as comma-separated decimal values, as in: `44.2456, -122.3348`

`LatLong` data can be captured in a form field when editing or adding rows via the `LatLong` and `ChangeLocation` column types.

The current location button on the `LatLong` input uses high-accuracy GPS location capture on your device, which is potentially time-consuming and battery-intensive. Using a `ChangeLocation` column or an [app formula or initial value](https://support.google.com/appsheet/answer/10106437) expression of [`HERE()`](https://support.google.com/appsheet/answer/10107405) for a `LatLong` column enables passive location capture within the form, but the accuracy may be reduced compared to using the current location button. 

### XY data

The `XY` column type represents a position within an image that you provide. When a map view is configured with an `XY`-type `Map` column, it will display the image in place of the usual map.

To enable an `XY` image map, change the column definition of your location data to `XY` and add a link to your hosted image (as quoted text or an expression) in the **Background image for the XY coordinates** setting.

background image for the XY coordinates

The following video shows how to use custom maps by using the **Background image for the XY coordinates** setting.

Video: https://www.youtube.com/watch?v=IrnSBo_neGg
