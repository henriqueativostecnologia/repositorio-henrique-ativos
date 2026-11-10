---
fonte: https://support.google.com/appsheet/answer/10106705?hl=en
baixado: 2026-11-10
---

# Geocode addresses

Each time you enter a new address or change an existing address, AppSheet must send the address to the Google mapping service to convert the address to its corresponding latitude and longitude. This is referred to as *geocoding* the address. Since `LatLong` fields already contain a latitude and longitude, they do not need to be geocoded.

AppSheet sends geocoding requests to Google as quickly as possible. Google imposes limits on geocoding to prevent overloading their mapping servers. After AppSheet makes a number of geocoding calls, the Google server may respond with a rate-limiting error. When Google responds with this error, AppSheet uses *exponential back off* between successive calls to the geocoding service. For example, AppSheet might first impose no delay between calls to the geocoding service. AppSheet makes as many geocoding calls as possible, using no delay. Then:

- If Google responds with a rate-limiting error, AppSheet imposes a one-second delay between calls.
- If Google responds with a second rate-limiting error, AppSheet imposes a two-second delay between calls.
- If Google responds with a third rate-limiting error, AppSheet imposes a four-second delay between calls.
- If Google responds with a fourth rate-limiting error, AppSheet imposes an eight-second delay between calls.

And so on. As the delay increases each time Google returns a rate-limiting error, it can take minutes, hours, or days to geocode your addresses if you have hundreds or thousands of new or changed addresses.

Once your addresses are geocoded, AppSheet caches the results on our servers to avoid the cost of geocoding the addresses again.
