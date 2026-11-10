---
fonte: https://support.google.com/appsheet/answer/10107947?hl=en
baixado: 2026-11-10
---

# Other expressions

Modify text, create unique IDs, and work with location

Expressions may be used in various AppSheet features - [app formulas](https://support.google.com/appsheet/answer/10106437), [column constraints](https://support.google.com/appsheet/answer/10107948) (`Valid_If`, `Show_If`, `Required_If`) - to customize app behavior and provide advanced functionality.

The expressions described here cover a range of needs and don't fit into any of the other [expression types](https://support.google.com/appsheet/topic/10104376).

**New to expressions?** See also [Expressions: The Essentials](https://support.google.com/appsheet/answer/10104642).

## Functions

### Conditional

- [`IF()`](https://support.google.com/appsheet/answer/10108198) - Either/or conditional evaluation
- [`IFS()`](https://support.google.com/appsheet/answer/10107912) - First-match conditional evaluation
- [`SWITCH()`](https://support.google.com/appsheet/answer/10107700) - Choose-one conditional evaluation

### Hyperlinks & URLs

- [`HYPERLINK()`](https://support.google.com/appsheet/answer/10107911) - New hyperlink

- [`LINKTEXT()`](https://support.google.com/appsheet/answer/10107913) - text component of hyperlink

- [`LINKURL()`](https://support.google.com/appsheet/answer/10107967)` `- URL component of hyperlink

### Informational

- [`CONTEXT()`](https://support.google.com/appsheet/answer/10107885) - Information about the running app
- [`USEREMAIL()`](https://support.google.com/appsheet/answer/10108210) - User's email address
- [`USERLOCALE()`](https://support.google.com/appsheet/answer/10108289) - User's locale
- [`USERNAME()`](https://support.google.com/appsheet/answer/10108211) - User's name
- [`USERROLE()`](https://support.google.com/appsheet/answer/10108128) - Assigned role of approved user
- [`USERSETTINGS()`](https://support.google.com/appsheet/answer/10108291) - Specified user-setting value

### LatLong & XY

- [`DISTANCE()`](https://support.google.com/appsheet/answer/11587699) - Distance between two locations
- `GETX()` - X component of `XY` value
- `GETY()`- Y component of `XY` value
- [`HERE()`](https://support.google.com/appsheet/answer/10107405) - Current location
- [`LAT()`](https://support.google.com/appsheet/answer/10107682) - Latitude component of `LatLong` value
- [`LATLONG()`](https://support.google.com/appsheet/answer/10107965) - `LatLong` from components
- [`LONG()`](https://support.google.com/appsheet/answer/10108108) - Longitude component of `LatLong` value

### Utility

- [`TEXT_ICON()`](https://support.google.com/appsheet/answer/11622091) - Icon from text
- [`UNIQUEID()`](https://support.google.com/appsheet/answer/10108209) - Pseudo-unique ID
