[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerAntiDDoS](../IMTConServerAntiDDoS.md) / AccessMask

[Previous](Priority.md) | [Next](PointsAdd.md)

# IMTConServerAntiDDoS::AccessMask

Get the allowed types of connection to the Anti-DDoS Server.

C++
    
    
    UINT  IMTConServerAntiDDoS::AccessMask()  const

.NET (Gateway/Manager API)
    
    
    EnAccessMask  CIMTConServerAntiDDoS.AccessMask()

Python (Manager API)
    
    
    MTConServerAntiDDoS.AccessMask

### Return Value

A value of the [IMTConServerAntiDDoS::EnAccessMask (#enaccessmask)](Enumerations.md#enaccessmask) enumeration.

# IMTConServerAntiDDoS::AccessMask

Set the allowed types of connection to the Anti-DDoS Server.

C++
    
    
    MTAPIRES  IMTConServerAntiDDoS::AccessMask(
       const UINT    flags    // Types of allowed connections
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerAntiDDoS.AccessMask(
       EnAccessMask  flags    // Types of allowed connections
       )

Python (Manager API)
    
    
    MTConServerAntiDDoS.AccessMask

### Parameters

**flags**  
[in] To pass the types of allowed connections theIMTConServerAntiDDoS::EnAccessMaskenumeration is used.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.
