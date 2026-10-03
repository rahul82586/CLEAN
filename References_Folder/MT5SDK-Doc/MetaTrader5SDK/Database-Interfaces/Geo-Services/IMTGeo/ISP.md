[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Geo Services](../../Geo-Services.md) / [IMTGeo](../IMTGeo.md) / ISP

[Previous](ASNOrganization.md) | [Next](ISPOrganization.md)

# IMTGeo::ISP

Get the name of the internet service provider that owns an IP address.

C++
    
    
    LPCWSTR  IMTGeo::ISP()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTGeo.ISP()

### Return Value

The name of the internet service provider that owns an IP address.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTGeo](../IMTGeo.md) object.
