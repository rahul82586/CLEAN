[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Time](../../Time.md) / [IMTConTime](../IMTCon.md) / IMTCon Daylight

[Previous](IMTCon-TableSet.md) | [Next](IMTCon-DaylightState.md)

# IMTConTime::Daylight

Get the mode of switching to the daylight saving time.

C++
    
    
    bool  IMTConTime::Daylight()  const

.NET (Gateway/Manager API)
    
    
    bool  CIMTConTime.Daylight()

Python (Manager API)
    
    
    MTConTime.Daylight

### Return Value

false - DST is disabled, true - enabled.

# IMTConTime::Daylight

Get the mode of switching to the daylight saving time.

C++
    
    
    MTAPIRES  IMTConTime::Daylight(
       const bool  enable      // DST mode
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConTime.Daylight(
       bool        enable      // DST mode
       )

Python (Manager API)
    
    
    MTConTime.Daylight

### Parameters

**enable**  
[in] Dsaylight saving time mode: false - disabled, true - enabled.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
