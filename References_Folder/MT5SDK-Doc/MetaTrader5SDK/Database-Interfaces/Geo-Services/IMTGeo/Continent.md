[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Geo Services](../../Geo-Services.md) / [IMTGeo](../IMTGeo.md) / Continent

[Previous](IPv6To.md) | [Next](Country.md)

# IMTGeo::Continent

Get the continent where an IP address is located.

C++
    
    
    LPCWSTR  IMTGeo::Continent()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTGeo.Continent()

### Return Value

The continent where an IP address is located.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTGeo](../IMTGeo.md) object.
