[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerAccess](../IMTConServerAccess.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTConServerAccess::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTConServerAccess::Assign(
       const IMTConServerAccess*  param  // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerAccess.Assign(
       CIMTConServerAccess        param  // Source object
       )

### Parameters

**param**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
