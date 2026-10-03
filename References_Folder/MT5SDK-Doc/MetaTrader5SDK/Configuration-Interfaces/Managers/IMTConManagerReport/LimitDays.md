[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Managers](../../Managers.md) / [IMTConManagerReport](../IMTConManagerReport.md) / LimitDays

[Previous](Permissions.md) | [Next](../IMTConManagerSink.md)

# IMTConManager::LimitDays

Get the depth to which a manager can query data in a report.

C++
    
    
    UINT  IMTConManager::LimitDays()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConManager.LimitDays()

Python (Manager API)
    
    
    MTConManager.LimitDays

### Return Value

Depth of available data in number of days.

# IMTConManager::LimitDays

Set the depth to which a manager can query data in a report.

C++
    
    
    MTAPIRES  IMTConManager::LimitDays(
       const UINT      limit  // Data limit
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConManager.LimitDays(
       uint            limit  // Data limit
       )

Python (Manager API)
    
    
    MTConManager.LimitDays

### Parameters

**limit**  
[in] Depth of available data in number of days.

### Return Value

An indication of a successful performance is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error corresponding to the response code occurred.
