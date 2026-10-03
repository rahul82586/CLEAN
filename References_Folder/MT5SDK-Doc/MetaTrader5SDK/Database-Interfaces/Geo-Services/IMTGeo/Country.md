[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Geo Services](../../Geo-Services.md) / [IMTGeo](../IMTGeo.md) / Country

[Previous](Continent.md) | [Next](City.md)

# IMTGeo::Country

Get the country where an IP address is located.

C++
    
    
    LPCWSTR  IMTGeo::Country()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTGeo.Country()

### Return Value

The country where an IP address is located.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTGeo](../IMTGeo.md) object.
