[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSymbol](../IMTConGroupSymbol.md) / PermissionsFlags

[Previous](OrderFlagsDefault.md) | [Next](BookDepthLimit.md)

# IMTConGroupSymbol::PermissionsFlags

Get permission flags for the group symbols.

C++
    
    
    UINT64  IMTConGroupSymbol::PermissionsFlags()  const

.NET (Gateway/Manager API)
    
    
    EnPermissionsFlags  CIMTConGroupSymbol.PermissionsFlags()

Python (Manager API)
    
    
    MTConGroupSymbol.PermissionsFlags

### Return Value

A value from the [IMTConGroup::EnPermissionsFlags (#enpermissionsflags)](Enumerations.md#enpermissionsflags) enumeration.

# IMTConGroupSymbol::PermissionsFlags

Set permission flags for the group symbols.

C++
    
    
    MTAPIRES  IMTConGroupSymbol::PermissionsFlags(
       const UINT64        flags  // Permission flags
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroupSymbol.PermissionsFlags(
       EnPermissionsFlags  flags  // Permission flags
       )

Python (Manager API)
    
    
    MTConGroupSymbol.PermissionsFlags

### Parameters

**flags**  
[in] TheIMTConGroup:EnPermissionsFlagsenumeration is used for passing permission flags..

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
