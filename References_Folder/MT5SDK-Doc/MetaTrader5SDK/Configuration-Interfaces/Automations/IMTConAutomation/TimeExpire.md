[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutomation](../IMTConAutomation.md) / TimeExpire

[Previous](TimeStart.md) | [Next](TimeWeekdays.md)

# IMTConAutomation::TimeExpire

Get the date and time after which the trigger check will be disabled.

C++
    
    
    INT64  IMTConAutomation::TimeExpire()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTConAutomation.TimeExpire()

Python
    
    
    MTConAutomation.TimeExpire

### Return Value

Date and time in seconds elapsed since 01.01.1970.

# IMTConAutomation::TimeExpire

Set the date and time after which the trigger check will be disabled.

C++
    
    
    MTAPIRES  IMTConAutomation::TimeExpire(
       const INT64  time      // End of trigger check
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAutomation.TimeExpire(
       long         time      // End of trigger check
       )

Python
    
    
    MTConAutomation.TimeExpire

### Parameters

**time**  
[in] Date and time in seconds elapsed since 01.01.1970.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
