[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerTrade](../IMTConServerTrade.md) / OvernightMode

[Previous](DemoPeriod.md) | [Next](OvernightTime.md)

# IMTConServerTrade::OvernightMode

Gets the mode of transition to the next day.

C++
    
    
    UINT  IMTConServerTrade::OvernightMode()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConServerTrade.OvernightMode()

Python (Manager API)
    
    
    MTConServerTrade.OvernightMode

### Return Value

A value of the [IMTConServerTrade::EnOvernightMode (#enovernightmode)](Enumerations.md#enovernightmode) enumeration.

# IMTConServerTrade::OvernightMode

Sets the mode of transition to the next day.

C++
    
    
    MTAPIRES  IMTConServerTrade::OvernightMode(
       const UINT  mode      // The mode of transition to the next day 
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerTrade.OvernightMode(
       uint        mode      // The mode of transition to the next day 
       )

Python (Manager API)
    
    
    MTConServerTrade.OvernightMode

### Parameters

**mode**  
[in] The overnight mode is passed using theIMTConServerTrade::EnOvernightModeenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
