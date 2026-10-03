[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Geo Services](../../Geo-Services.md) / [IMTGeo](../IMTGeo.md) / ASNOrganization

[Previous](ASN.md) | [Next](ISP.md)

# IMTGeo::Province

Get the name of the [autonomous system](https://ru.wikipedia.org/wiki/%D0%90%D0%B2%D1%82%D0%BE%D0%BD%D0%BE%D0%BC%D0%BD%D0%B0%D1%8F_%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0_(%D0%98%D0%BD%D1%82%D0%B5%D1%80%D0%BD%D0%B5%D1%82)) to which an IP address belongs.

C++
    
    
    LPCWSTR  IMTGeo::Province()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTGeo.Province()

### Return Value

The name of the autonomous system to which an IP address belongs.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTGeo](../IMTGeo.md) object.
