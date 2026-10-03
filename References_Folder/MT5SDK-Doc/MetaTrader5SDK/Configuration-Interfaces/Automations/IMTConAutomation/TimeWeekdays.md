[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutomation](../IMTConAutomation.md) / TimeWeekdays

[Previous](TimeExpire.md) | [Next](TimeMonths.md)

# IMTConAutomation::TimeWeekdays

Get the days on which the task automation trigger is allowed.

C++
    
    
    UINT  IMTConAutomation::TimeWeekdays()  const

.NET (Gateway/Manager API)
    
    
    EnTriggerWeekdays  CIMTConAutomation.TimeWeekdays()

Python
    
    
    MTConAutomation.TimeWeekdays

### Return Value

One of the values of the [IMTConAutomation::EnTriggerWeekdays (#entriggerweekdays)](Enumerations.md#entriggerweekdays) enumeration.

# IMTConAutomation::TimeWeekdays

Set the days on which the task automation trigger is allowed.

C++
    
    
    MTAPIRES  IMTConAutomation::TimeWeekdays(
       const UINT         weekdays  // Days when the trigger is enabled
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAutomation.TimeWeekdays(
       EnTriggerWeekdays  weekdays  // Days when the trigger is enabled
       )

Python
    
    
    MTConAutomation.TimeWeekdays

### Parameters

**weekdays**  
[in] The schedule is passed using theIMTConAutomation::EnTriggerWeekdaysenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
