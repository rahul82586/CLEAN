[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerAccess](../IMTConServerAccess.md) / AccessFlags

[Previous](PriorityCurrent.md) | [Next](AccessMask.md)

# IMTConServerAccess::AccessFlags

Getting additional parameters of the Access Server.

C++
    
    
    UINT  IMTConServerAccess::AccessFlags()  const

.NET (Gateway/Manager API)
    
    
    EnAccessFlags  CIMTConServerAccess.AccessFlags()

Python (Manager API)
    
    
    MTConServerAccess.AccessFlags

### Return Value

A value of the [IMTConServerAccess::EnAccessFlags (#enaccessflags)](Enumerations.md#enaccessflags) enumeration.

# IMTConServerAccess::AccessFlags

Setting additional parameters of the Access Server.

C++
    
    
    MTAPIRES  IMTConServerAccess::AccessFlags(
       const UINT    flags    // Flags of parameters
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerAccess.AccessFlags(
       EnAccessFlags flags    // Flags of parameters
       )

Python (Manager API)
    
    
    MTConServerAccess.AccessFlags

### Settings

**flags**  
[in] Settings of the access server are passed using flags from theIMTConServerAccess::EnAccessFlagsenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.
