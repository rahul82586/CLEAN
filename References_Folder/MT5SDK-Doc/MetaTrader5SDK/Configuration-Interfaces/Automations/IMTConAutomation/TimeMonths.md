[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutomation](../IMTConAutomation.md) / TimeMonths

[Previous](TimeWeekdays.md) | [Next](TimeMonthdays.md)

# IMTConAutomation::TimeMonths

Get the months in which the task automation trigger is allowed.

C++
    
    
    UINT  IMTConAutomation::TimeMonths()  const

.NET (Gateway/Manager API)
    
    
    EnTriggerMonths  CIMTConAutomation.TimeMonths()

Python
    
    
    MTConAutomation.TimeMonths

### Return Value

One of the values of the [IMTConAutomation::EnTriggerMonths (#entriggermonths)](Enumerations.md#entriggermonths) enumeration.

# IMTConAutomation::TimeMonths

Set the months in which the task automation trigger is allowed.

C++
    
    
    MTAPIRES  IMTConAutomation::TimeMonths(
       const UINT         months  // Months when the trigger is enabled
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAutomation.TimeMonths(
       EnTriggerMonths    months  // Months when the trigger is enabled
       )

Python
    
    
    MTConAutomation.TimeMonths

### Parameters

**months**  
[in] The schedule is passed using theIMTConAutomation::EnTriggerMonthsenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
