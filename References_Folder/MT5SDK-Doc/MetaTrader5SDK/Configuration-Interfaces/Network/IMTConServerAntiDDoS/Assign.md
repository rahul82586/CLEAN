[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerAntiDDoS](../IMTConServerAntiDDoS.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTConServerAntiDDoS::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTConServerAntiDDoS::Assign(
       const IMTConServerAntiDDoS*  param  // The source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerAccess.Assign(
       CIMTConServerAntiDDoS        param  // The source object
       )

### Parameters

**param**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.
