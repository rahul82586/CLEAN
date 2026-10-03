[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutomation](../IMTConAutomation.md) / TimeMonthdays

[Previous](TimeMonths.md) | [Next](EventPauseMinutes.md)

# IMTConAutomation::TimeMonthdays

Get the days of the month on which the task automation trigger is allowed.

C++
    
    
    UINT  IMTConAutomation::TimeMonthdays()  const

.NET (Gateway/Manager API)
    
    
    EnTriggerWeekdays  CIMTConAutomation.TimeMonthdays()

Python
    
    
    MTConAutomation.TimeMonthdays

### Return Value

One of the values of the [IMTConAutomation::EnTriggerMonthDays (#entriggermonthdays)](Enumerations.md#entriggermonthdays) enumeration.

# IMTConAutomation::TimeMonthdays

Set the days of the month on which the task automation trigger is allowed.

C++
    
    
    MTAPIRES  IMTConAutomation::TimeMonthdays(
       const UINT         monthdays  // Days of the month when the trigger is enabled
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAutomation.TimeMonthdays(
       EnTriggerWeekdays  monthdays  // Days of the month when the trigger is enabled
       )

Python
    
    
    MTConAutomation.TimeMonthdays

### Parameters

**monthdays**  
[in] The schedule is passed using theIMTConAutomation::EnTriggerMonthDaysenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
