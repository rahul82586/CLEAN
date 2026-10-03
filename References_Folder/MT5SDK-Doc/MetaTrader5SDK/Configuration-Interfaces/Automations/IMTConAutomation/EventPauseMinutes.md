[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutomation](../IMTConAutomation.md) / EventPauseMinutes

[Previous](TimeMonthdays.md) | [Next](EventPauseHours.md)

# IMTConAutomation::EventPauseMinutes

Get the number of minutes in the period of time for which the number of repetitions should be checked.>

C++
    
    
    UINT  IMTConAutomation::EventPauseMinutes()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConAutomation.EventPauseMinutes()

Python
    
    
    MTConAutomation.EventPauseMinutes

### Return Value

Number of minutes.

# IMTConAutomation::EventPauseMinutes

Set the number of minutes in the period of time for which the number of repetitions should be checked.>

C++
    
    
    MTAPIRES  IMTConAutomation::EventPauseMinutes(
       const UINT  minutes  // Number of minutes
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAutomation.EventPauseMinutes(
       uint        minutes  // Number of minutes
       )

Python
    
    
    MTConAutomation.EventPauseMinutes

### Parameters

**minutes**  
[in] Number of minutes.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
