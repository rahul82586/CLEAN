[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerAccess](../IMTConServerAccess.md) / AccessMask

[Previous](AccessFlags.md) | [Next](NewsMax.md)

# IMTConServerAccess::AccessMask

Get the allowed types of connection to the Access Server.

C++
    
    
    UINT  IMTConServerAccess::AccessMask()  const

.NET (Gateway/Manager API)
    
    
    EnAccessMask  CIMTConServerAccess.AccessMask()

Python (Manager API)
    
    
    MTConServerAccess.AccessMask

### Return Value

A value from the [IMTConServerAccess::EnAccessMask (#enaccessmask)](Enumerations.md#enaccessmask) enumeration.

# IMTConServerAccess::AccessMask

Set the allowed types of connection to the Access Server.

C++
    
    
    MTAPIRES  IMTConServerAccess::AccessMask(
       const UINT    flags    // Types of allowed connections
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerAccess.AccessMask(
       EnAccessMask  flags    // Types of allowed connections
       )

Python (Manager API)
    
    
    MTConServerAccess.AccessMask

### Parameters

**flags**  
[in] The allowed types of connection are passed using theIMTConServerAccess::EnAccessMaskenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
