[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Managers](../../Managers.md) / [IMTConManager](../IMTConManager.md) / LimitReports

[Previous](LimitLogs.md) | [Next](Right.md)

# IMTConManager::LimitReports

Get the time period of reports available to a manager.

C++
    
    
    UINT  IMTConManager::LimitReports()  const

.NET (Gateway/Manager API)
    
    
    EnManagerLimit  CIMTConManager.LimitReports()

Python (Manager API)
    
    
    MTConManager.LimitReports

### Return Value

A value of the [IMTConManager::EnManagerLimit (#enmanagerlimit)](Enumerations.md#enmanagerlimit) enumeration.

# IMTConManager::LimitReports

Set the time period of reports available to a manager.

C++
    
    
    MTAPIRES  IMTConManager::LimitReports(
       const UINT      limit  // The limit of reports
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConManager.LimitReports(
       EnManagerLimit  limit  // The limit of reports
       )

Python (Manager API)
    
    
    MTConManager.LimitReports

### Parameters

**limit**  
[in] The period for which a manager can access reports, is passed using theIMTConManager::EnManagerLimitenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
