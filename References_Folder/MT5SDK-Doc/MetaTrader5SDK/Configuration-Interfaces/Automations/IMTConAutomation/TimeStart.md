[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutomation](../IMTConAutomation.md) / TimeStart

[Previous](Flags.md) | [Next](TimeExpire.md)

# IMTConAutomation::TimeStart

Get the date and time on which the trigger check will be activated.

C++
    
    
    INT64  IMTConAutomation::TimeStart()  const

.NET (Gateway/Manager API)
    
    
    long  CIMTConAutomation.TimeStart()

Python
    
    
    MTConAutomation.TimeStart

### Return Value

Date and time in seconds elapsed since 01.01.1970.

# IMTConAutomation::TimeStart

Set the date and time on which the trigger check will be activated.

C++
    
    
    MTAPIRES  IMTConAutomation::TimeStart(
       const INT64  start     // Start of trigger check
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAutomation.TimeStart(
       long         start     // Start of trigger check
       )

Python
    
    
    MTConAutomation.TimeStart

### Parameters

**start**  
[in] Date and time in seconds elapsed since 01.01.1970.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
