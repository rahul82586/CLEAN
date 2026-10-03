[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutomation](../IMTConAutomation.md) / EventPauseDays

[Previous](EventPauseHours.md) | [Next](EventRepeats.md)

# IMTConAutomation::EventPauseDays

Get the number of days in the period of time for which the number of repetitions should be checked.>

C++
    
    
    UINT  IMTConAutomation::EventPauseDays()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTConAutomation.EventPauseDays()

Python
    
    
    MTConAutomation.EventPauseDays

### Return Value

Number of days.

# IMTConAutomation::EventPauseDays

Set the number of days in the period of time for which the number of repetitions should be checked.>

C++
    
    
    MTAPIRES  IMTConAutomation::EventPauseDays(
       const UINT  days     // Number of days
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAutomation.EventPauseDays(
       uint        days     // Number of days
       )

Python
    
    
    MTConAutomation.EventPauseDays

### Parameters

**hours**  
[in] Number of days.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
