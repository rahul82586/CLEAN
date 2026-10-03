[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Geo Services](../../Geo-Services.md) / [IMTGeo](../IMTGeo.md) / City

[Previous](Country.md) | [Next](Region.md)

# IMTGeo::City

Get the city where an IP address is located.

C++
    
    
    LPCWSTR  IMTGeo::City()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTGeo.City()

### Return Value

The city where an IP address is located.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTGeo](../IMTGeo.md) object.
