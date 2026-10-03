[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Geo Services](../../Geo-Services.md) / [IMTGeo](../IMTGeo.md) / Province

[Previous](Region.md) | [Next](ASN.md)

# IMTGeo::Province

Get the province/state where an IP address is located.

C++
    
    
    LPCWSTR  IMTGeo::Province()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTGeo.Province()

### Return Value

The province/state where an IP address is located.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTGeo](../IMTGeo.md) object.
