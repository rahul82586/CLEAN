[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutomation](../IMTConAutomation.md) / Flags

[Previous](Trigger.md) | [Next](TimeStart.md)

# IMTConAutomation::Flags

Get additional automation task settings.

C++
    
    
    UINT64  IMTConAutomation::Flags()  const

.NET (Gateway/Manager API)
    
    
    EnFlags  CIMTConAutomation.Flags()

Python
    
    
    MTConAutomation.Flags

### Return Value

Additional settings as the values of the [IMTConAutomation::EnFlags (#enflags)](Enumerations.md#enflags) enumeration.

# IMTConAutomation::Flags

Set additional automation task settings.

C++
    
    
    MTAPIRES  IMTConAutomation::Flags(
       const UINT64  flags   // Automation task settings
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAutomation.Flags(
       EnFlags       flags   // Automation task settings
       )

Python
    
    
    MTConAutomation.Flags

### Parameters

**flags**  
[in] Additional settings as the values of theIMTConAutomation::EnFlagsenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
