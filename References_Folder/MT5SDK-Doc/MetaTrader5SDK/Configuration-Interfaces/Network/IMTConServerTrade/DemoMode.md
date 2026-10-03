[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerTrade](../IMTConServerTrade.md) / DemoMode

[Previous](Clear.md) | [Next](DemoPeriod.md)

# IMTConServerTrade::DemoMode

Get the mode of demo account allocation.

C++
    
    
    UINT  IMTConServerTrade::DemoMode()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConServerTrade.DemoMode()

Python (Manager API)
    
    
    MTConServerTrade.DemoMode

### Return Value

A value of the [IMTConServerTrade::EnDemoMode (#endemomode)](Enumerations.md#endemomode) enumeration.

# IMTConServerTrade::DemoMode

Set the mode of demo account allocation.

C++
    
    
    MTAPIRES  IMTConServerTrade::DemoMode(
       const UINT  mode      // Demo account allocation mode
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerTrade.DemoMode(
       uint        mode      // Demo account allocation mode
       )

Python (Manager API)
    
    
    MTConServerTrade.DemoMode

### Parameters

**mode**  
[in] The demo account allocation mode is passed using theIMTConServerTrade::EnDemoModeenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
