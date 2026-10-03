[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Geo Services](../../Geo-Services.md) / [IMTGeo](../IMTGeo.md) / Clear

[Previous](Assign.md) | [Next](IPv4From.md)

# IMTGeo::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTGeo::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTGeo.Clear()

### Return Value

An indication of a successful performance is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method cleans all fields ​​and removes embedded objects.
