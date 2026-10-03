[🏠 Document Start](../../README.md) / [Database Interfaces](../README.md) / [Geo Services](../Geo-Services.md) / IMTGeo

[Previous](../Geo-Services.md) | [Next](IMTGeo/Enumerations.md)

# IMTGeo

This interface provides access to information about the IP address, including the owner, geographic location, and other details.

Method | Purpose  
---|---  
[Release](IMTGeo/Release.md) | Delete the current object.  
[Assign](IMTGeo/Assign.md) | Assign a passed object to the current one.  
[Clear](IMTGeo/Clear.md) | Clear an object.  
[IPv4From](IMTGeo/IPv4From.md) | Get the beginning of the range of IPv4 addresses.  
[IPv4To](IMTGeo/IPv4To.md) | Get the end of the range of IPv4 addresses.  
[IPv6From](IMTGeo/IPv6From.md) | Get the beginning of the range of IPv6 addresses.  
[IPv6To](IMTGeo/IPv6To.md) | Get the end of the range of IPv6 addresses.  
[Continent](IMTGeo/Continent.md) | Get the continent where an IP address is located.  
[Country](IMTGeo/Country.md) | Get the country where an IP address is located.  
[City](IMTGeo/City.md) | Get the city where an IP address is located.  
[Region](IMTGeo/Region.md) | Get the region where an IP address is located.  
[Province](IMTGeo/Province.md) | Get the province/state where an IP address is located.  
[ASN](IMTGeo/ASN.md) | Get the Autonomous System Number (ASN) to which an IP address belongs.  
[ASNOrganization](IMTGeo/ASNOrganization.md) | Get the name of the autonomous system to which an IP address belongs.  
[ISP](IMTGeo/ISP.md) | Get the name of the internet service provider that owns an IP address.  
[ISPOrganization](IMTGeo/ISPOrganization.md) | Get the organization that owns an IP address.  
[Latitude](IMTGeo/Latitude.md) | Get the latitude for an IP address.  
[Longitude](IMTGeo/Longitude.md) | Getting longitude for an IP address.  
[Details](IMTGeo/Details.md) | Get more information about an IP address.  
  
The IMTGeo class contains the following enumerations:

Enumeration | Description  
---|---  
[EnGeoRequestFlags (#engeorequestflags)](IMTGeo/Enumerations.md#engeorequestflags) | Types of data requested about an IP address.  
[EnGeoRecordDetails (#engeorecorddetails)](IMTGeo/Enumerations.md#engeorecorddetails) | Flags for transmitting additional information about an IP address.
