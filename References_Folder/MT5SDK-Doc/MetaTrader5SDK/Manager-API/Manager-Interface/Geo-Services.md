[🏠 Document Start](../../README.md) / [Manager API](../README.md) / [Manager Interface](../Manager-Interface.md) / Geo Services

[Previous](ECN/RequestHistoryByTickets.md) | [Next](Geo-Services/GeoCreate.md)

# Geo-services

The methods described in this section provide access to the GeoIP database information on the trading server. These methods enable access to the information about visitors' country, city, coordinates and Internet providers, based on their IP addresses. The database is automatically updated on the server once a week, keeping the relevant information up to date.

By using these methods, you can generate user activity reports and create maps, among others.

Function | Purpose  
---|---  
[GeoCreate](Geo-Services/GeoCreate.md) | Create an IP address description object.  
[GeoResolve](Geo-Services/GeoResolve.md) | Resolve an IPv4 or IPv6 address.  
[GeoResolveBatch](Geo-Services/GeoResolveBatch.md) | Resolve a list of IP addresses of any type: IPv4 or IPv6.
