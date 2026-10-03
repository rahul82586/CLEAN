[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [VPS](../../VPS.md) / [IMTConVPSGroup](../IMTConGroup.md) / IMTConGroup InactiveDays

[Previous](IMTConGroup-MinBalance.md) | [Next](../IMTConSink.md)

# IMTConVPSGroup::InactiveDays

Get a trader inactivity period, after which the sponsored hosting is automatically canceled.

C++
    
    
    UINT  IMTConVPSGroup::InactiveDays()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConVPSGroup.InactiveDays()

Python
    
    
    MTConVPSGroup.InactiveDays

### Return Value

Inactivity period in the number of days. 0 means the hosting is not disabled.

### Note

An account is considered inactive if no trading operation takes place on it during a specified period.

# IMTConVPSGroup::InactiveDays

Set a trader inactivity period, after which the sponsored hosting is automatically canceled.

C++
    
    
    MTAPIRES  IMTConVPSGroup::InactiveDays(
       const UINT  days        // inactivity period
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConVPSGroup.InactiveDays(
       uint        days        // inactivity period
       )

Python
    
    
    MTConVPSGroup.InactiveDays

### Parameters

**days**  
[in] Inactivity period in the number of days. Set 0 in order not to disable the hosting.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

An account is considered inactive if no trading operation takes place on it during a specified period.
