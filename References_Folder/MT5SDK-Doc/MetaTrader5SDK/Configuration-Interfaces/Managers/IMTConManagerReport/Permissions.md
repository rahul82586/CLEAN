[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Managers](../../Managers.md) / [IMTConManagerReport](../IMTConManagerReport.md) / Permissions

[Previous](Report.md) | [Next](LimitDays.md)

# IMTConManagerReport::Permissions

Get report access permissions.

C++
    
    
    UINT64  IMTConManagerReport::Permissions()  const

.NET (Gateway/Manager API)
    
    
    EnPermissionsFlags  CIMTConManagerReport.Permissions()

Python (Manager API)
    
    
    MTConManagerReport.Permissions

### Return Value

A value from the [IMTConManagerReport::EnPermissionsFlags (#enpermissionsflags)](Enumerations.md#enpermissionsflags) enumeration.

# IMTConManagerReport::Permissions

Set report access permissions.

C++
    
    
    MTAPIRES  IMTConManagerReport::Permissions(
       const UINT64        permissions  // Manager permissions
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConManagerReport.Permissions(
       EnPermissionsFlags  permissions  // Manager permissions
       )

Python (Manager API)
    
    
    MTConManagerReport.Permissions

### Parameters

**permissions**  
[in] Report access permissions are passed using theIMTConManagerReport::EnPermissionsFlagsenumeration.

### Return Value

An indication of a successful performance is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error corresponding to the response code occurred.
