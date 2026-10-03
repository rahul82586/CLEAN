[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Managers](../../Managers.md) / [IMTConManagerAccess](../IMTConManagerAccess.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTConManagerAccess::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTConManagerAccess::Assign(
       const IMTConManagerAccess*  access      // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConManagerAccess.Assign(
       CIMTConManagerAccess        access      // Source object
       )

### Parameters

**access**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
