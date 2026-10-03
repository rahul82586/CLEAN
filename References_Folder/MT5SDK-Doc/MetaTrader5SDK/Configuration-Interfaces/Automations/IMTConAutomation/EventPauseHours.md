[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutomation](../IMTConAutomation.md) / EventPauseHours

[Previous](EventPauseMinutes.md) | [Next](EventPauseDays.md)

# IMTConAutomation::EventPauseHours

Get the number of hours in the period of time for which the number of repetitions should be checked.>

C++
    
    
    UINT  IMTConAutomation::EventPauseHours()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConAutomation.EventPauseHours()

Python
    
    
    MTConAutomation.EventPauseHours

### Return Value

Number of hours.

# IMTConAutomation::EventPauseHours

Set the number of hours in the period of time for which the number of repetitions should be checked.>

C++
    
    
    MTAPIRES  IMTConAutomation::EventPauseHours(
       const UINT  hours    // Number of hours
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAutomation.EventPauseHours(
       uint        hours    // Number of hours
       )

Python
    
    
    MTConAutomation.EventPauseHours

### Parameters

**hours**  
[in] Number of hours.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
