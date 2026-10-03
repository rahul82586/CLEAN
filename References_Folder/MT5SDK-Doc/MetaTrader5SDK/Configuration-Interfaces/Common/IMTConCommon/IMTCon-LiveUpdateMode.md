[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Common](../../Common.md) / [IMTConCommon](../IMTCon.md) / IMTCon LiveUpdateMode

[Previous](IMTCon-LimitSymbols.md) | [Next](IMTCon-TotalUsers.md)

# IMTConCommon::LiveUpdateMode

Get the update mode of the components of the trading platform.

C++
    
    
    UINT  IMTConCommon::LiveUpdateMode()  const

.NET (Gateway/Manager API)
    
    
    EnUpdateMode  CIMTConCommon.LiveUpdateMode()

Python (Manager API)
    
    
    MTConCommon.LiveUpdateMode

### Return Value

If successful, returns one of the values of [IMTConCommon::EnUpdateMode](IMTCon-Enumerations.md). Otherwise, it returns NULL.

# IMTConCommon::LiveUpdateMode

Set the mode of update of the trading platform.

C++
    
    
    MTAPIRES  IMTConCommon::LiveUpdateMode(
       const UINT   mode     // Update mode
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConCommon.LiveUpdateMode(
       EnUpdateMode mode     // Update mode
       )

Python (Manager API)
    
    
    MTConCommon.LiveUpdateMode

### Parameters

**mode**  
[in] TheIMTConCommon::EnUpdateModeenumeration is used to pass the mode.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
