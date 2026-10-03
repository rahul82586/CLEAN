[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Geo Services](../../Geo-Services.md) / [IMTGeo](../IMTGeo.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTGeo::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTGeo::Assign(
       const IMTGeo*  obj // source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTGeo.Assign(
       CIMTGeo        obj // source object
       )

### Parameters

**obj**  
[in] Source object.

### Return Value

An indication of a successful performance is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
