[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerAddressRange](../IMTConServerAddressRange.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTConServerAddressRange::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTConServerAddressRange::Assign(
       const IMTConServerAddressRange*  param  // The source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerAddressRange.Assign(
       CIMTConServerAddressRange        param  // The source object
       )

### Parameters

**param**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.
