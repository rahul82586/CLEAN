[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Geo Services](../../Geo-Services.md) / [IMTGeo](../IMTGeo.md) / Region

[Previous](City.md) | [Next](Province.md)

# IMTGeo::Region

Get the region where an IP address is located.

C++
    
    
    LPCWSTR  IMTGeo::Region()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTGeo.Region()

### Return Value

The region where an IP address is located.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTGeo](../IMTGeo.md) object.
