[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Geo Services](../../Geo-Services.md) / [IMTGeo](../IMTGeo.md) / ISPOrganization

[Previous](ISP.md) | [Next](Latitude.md)

# IMTGeo::ISPOrganization

Get the organization that owns an IP address.

C++
    
    
    LPCWSTR  IMTGeo::ISPOrganization()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTGeo.ISPOrganization()

### Return Value

The organization that owns an IP address.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTGeo](../IMTGeo.md) object.
