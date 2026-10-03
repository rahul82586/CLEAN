[🏠 Document Start](../../README.md) / [Server API](../README.md) / [Main API Interface](../Main-API-Interface.md) / Geo Services

[Previous](Server-Services/ServerUnsubscribe.md) | [Next](Geo-Services/GeoCreate.md)

# Geo-services

The methods described in this section provide access to the GeoIP database information on the trading server. These methods enable access to the information about visitors' country, city, coordinates and Internet providers, based on their IP addresses. The database is automatically updated on the server once a week, keeping the relevant information up to date.

By using these methods, you can generate user activity reports and create maps, among others.

Function | Purpose  
---|---  
[GeoCreate](Geo-Services/GeoCreate.md) | Create an IP address description object.  
[GeoResolve](Geo-Services/GeoResolve.md) | Resolve an IPv4 or IPv6 address.  
[GeoResolveBatch](Geo-Services/GeoResolveBatch.md) | Resolve a list of IP addresses of any type: IPv4 or IPv6.  
[GeoResolveAny](Geo-Services/GeoResolveAny.md) | Resolve a list of IP addresses of any type: IPv4 or IPv6. The method is obsolete and is no longer used.  
[GeoResolveIPv4](Geo-Services/GeoResolveIPv4.md) | Resolve one IPv4 address. The method is obsolete and is no longer used.  
[GeoResolveIPv4Bulk](Geo-Services/GeoResolveIPv4Bulk.md) | Resolve multiple IPv4 addresses. The method is obsolete and is no longer used.  
[GeoResolveIPv6](Geo-Services/GeoResolveIPv6.md) | Resolve one IPv6 address. The method is obsolete and is no longer used.  
[GeoResolveIPv6Bulk](Geo-Services/GeoResolveIPv6Bulk.md) | Resolve multiple IPv6 addresses. The method is obsolete and is no longer used.
