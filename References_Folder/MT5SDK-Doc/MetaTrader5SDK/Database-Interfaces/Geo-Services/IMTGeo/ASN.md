[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Geo Services](../../Geo-Services.md) / [IMTGeo](../IMTGeo.md) / ASN

[Previous](Province.md) | [Next](ASNOrganization.md)

# IMTGeo::ASN

Get the [Autonomous System Number](https://ru.wikipedia.org/wiki/%D0%90%D0%B2%D1%82%D0%BE%D0%BD%D0%BE%D0%BC%D0%BD%D0%B0%D1%8F_%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0_(%D0%98%D0%BD%D1%82%D0%B5%D1%80%D0%BD%D0%B5%D1%82)) (ASN) to which an IP address belongs.

C++
    
    
    UINT64  IMTGeo::ASN()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTGeo.ASN()

### Return Value

The Autonomous System Number (ASN) to which an IP address belongs.
