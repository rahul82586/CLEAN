[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Managers](../../Managers.md) / [IMTConManager](../IMTConManager.md) / Right

[Previous](LimitReports.md) | [Next](GroupAdd.md)

# IMTConManager::Right

Gets the rights of a manager.

C++
    
    
    UINT  IMTConManager::Right(
       const UINT  right       // Manager's rights
       )  const

.NET (Gateway/Manager API)
    
    
    EnManagerFlags  CIMTConManager.Right(
       EnManagerRights  right  // Manager's rights
       )

Python (Manager API)
    
    
    MTConManager.Right(
       right            # права менеджера
       )
    
    
    MTConManager.RightGet()

### Parameters

**right**  
[out] The manager's rights are passed in the 'right' variable using theIMTConManager::EnManagerRightsenumeration.

### Return Value

A value of the [IMTConManager::EnManagerFlags (#enmanagerrightflags)](Enumerations.md#enmanagerrightflags) enumeration.

# IMTConManager::Right

Sets the rights of a manager.

C++
    
    
    MTAPIRES  IMTConManager::Right(
       const UINT       right,  // Manager's rights
       const UINT       flags   // State of rights
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConManager.Right(
       EnManagerRights  right,  // Manager's rights
       EnManagerFlags   flags   // State of rights
       )

Python (Manager API)
    
    
    MTConManager.Right(
       right            # права менеджера
       )
    
    
    MTConManager.RightGet()

### Parameters

**right**  
[in] Manager's permissions are passed using theIMTConManager::EnManagerRightsenumeration.

**flags**  
[in] The state of permissions (granted or not) is passed using theIMTConManager::EnManagerRightFlagsenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Only one permission at a time can be set. To set multiple permissions, you should call IMTConManager::Right the appropriate number of times, every time passing one permission and its state.
