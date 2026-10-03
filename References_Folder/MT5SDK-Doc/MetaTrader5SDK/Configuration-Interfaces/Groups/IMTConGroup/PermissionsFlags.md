[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroup](../IMTConGroup.md) / PermissionsFlags

[Previous](Server.md) | [Next](AuthMode.md)

# IMTConGroup::PermissionsFlags

Get permission flags for the group.

C++
    
    
    UINT64  IMTConGroup::PermissionsFlags()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTConGroup.PermissionsFlags()

Python (Manager API)
    
    
    MTConGroup.PermissionsFlags

### Return Value

A value from the [IMTConGroup::EnPermissionsFlags (#enpermissionsflags)](Enumerations.md#enpermissionsflags) enumeration.

# IMTConGroup::PermissionsFlags

Set permission flags for the group.

C++
    
    
    MTAPIRES  IMTConGroup::PermissionsFlags(
       const UINT64  flags      // Permission flags
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroup.PermissionsFlags(
       ulong         flags      // Permission flags
       )

Python (Manager API)
    
    
    MTConGroup.PermissionsFlags

### Parameters

**flags**  
[in] TheIMTConGroup:EnPermissionsFlagsenumeration is used for passing permission flags..

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
