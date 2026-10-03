[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutomation](../IMTConAutomation.md) / Trigger

[Previous](Name.md) | [Next](Flags.md)

# IMTConAutomation::Trigger

Get a [trigger](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_trigger) — an event in the platform, upon occurrence of which the automation task should be executed.

C++
    
    
    UINT  IMTConAutomation::Trigger()  const

.NET (Gateway/Manager API)
    
    
    EnProviderType  CIMTConAutomation.Trigger()

Python
    
    
    MTConAutomation.Trigger

### Return Value

Automation task trigger. Passed as a value of the [IMTConAutomation::EnTriggers (#entriggers)](Enumerations.md#entriggers) enumeration.

# IMTConAutomation::Trigger

Set a [trigger](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_trigger) — an event in the platform, upon occurrence of which the automation task should be executed.

C++
    
    
    MTAPIRES  IMTConAutomation::Trigger(
       const UINT      trigger  // Trigger
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAutomation.Trigger(
       EnProviderType  trigger  // Trigger
       )

Python
    
    
    MTConAutomation.Trigger

### Parameters

**trigger**  
[in] Automation task trigger. Passed as a value of theIMTConAutomation::EnTriggersenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
