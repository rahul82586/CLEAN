[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerTrade](../IMTConServerTrade.md) / OvermonthMode

[Previous](OvernightDays.md) | [Next](OvermonthTimeLast.md)

# IMTConServerTrade::OvermonthMode

Get the mode of transition to the next month.

C++
    
    
    UINT  IMTConServerTrade::OvermonthMode()  const

.NET (Gateway/Manager API)
    
    
    EnOvermonthMode  CIMTConServerTrade.OvermonthMode()

Python (Manager API)
    
    
    MTConServerTrade.OvermonthMode

### Return Value

A value of the [IMTConServerTrade::EnOvermonthMode (#enovermonthmode)](Enumerations.md#enovermonthmode) enumeration.

# IMTConServerTrade::OvermonthMode

Set the mode of transition to the next month.

C++
    
    
    MTAPIRES  IMTConServerTrade::OvermonthMode(
       const UINT      mode      // The mode of transition to the next month
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerTrade.OvermonthMode(
       EnOvermonthMode mode      // The mode of transition to the next month
       )

Python (Manager API)
    
    
    MTConServerTrade.OvermonthMode

### Parameters

**mode**  
[in] The overmonth mode is passed using theIMTConServerTrade::EnOvermonthModeenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
