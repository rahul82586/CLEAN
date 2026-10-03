[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Managers](../../Managers.md) / [IMTConManager](../IMTConManager.md) / LimitLogs

[Previous](Server.md) | [Next](LimitReports.md)

# IMTConManager::LimitLogs

Get the time period of system logs available to a manager.

C++
    
    
    UINT  IMTConManager::LimitLogs()  const

.NET (Gateway/Manager API)
    
    
    EnManagerLimit  CIMTConManager.LimitLogs()

Python (Manager API)
    
    
    MTConManager.LimitLogs

### Return Value

A value of the [IMTConManager::EnManagerLimit (#enmanagerlimit)](Enumerations.md#enmanagerlimit) enumeration.

# IMTConManager::LimitLogs

Set the time period of system logs are available to a manager.

C++
    
    
    MTAPIRES  IMTConManager::LimitLogs(
       const UINT      limit  // The limit of log entries
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConManager.LimitLogs(
       EnManagerLimit  limit  // The limit of log entries
       )

Python (Manager API)
    
    
    MTConManager.LimitLogs

### Parameters

**limit**  
[in] The period for which a manager can access logs is passed using theIMTConManager::EnManagerLimitenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
