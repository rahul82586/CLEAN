[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroup](../IMTConGroup.md) / DemoInactivityPeriod

[Previous](DemoDeposit.md) | [Next](LimitHistory.md)

# IMTConGroup::DemoInactivityPeriod

Get demo account inactivity period, after which open orders and positions from these accounts will be deleted from the platform databases.

C++
    
    
    UINT  IMTConGroup::DemoInactivityPeriod()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConGroup.DemoInactivityPeriod()

Python (Manager API)
    
    
    MTConGroup.DemoInactivityPeriod

### Return Value

Inactivity period in the number of days. 0 means that deletion of operations is disabled.

### Note

The method is only applicable to demo groups.

# IMTConGroup::DemoInactivityPeriod

Set demo account inactivity period, after which open orders and positions from these accounts will be deleted from the platform databases.

C++
    
    
    MTAPIRES  IMTConGroup::DemoInactivityPeriod(
       const UINT  period        // Inactivity period
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroup.DemoInactivityPeriod(
       uint        period        // Inactivity period
       )

Python (Manager API)
    
    
    MTConGroup.DemoInactivityPeriod

### Program Parameters

**period**  
[in] Inactivity period in the number of days. To disable the deletion of operations, set the value to 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The method is only applicable to demo groups.
