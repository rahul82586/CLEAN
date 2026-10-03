[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutoAction](../IMTConAutoAction.md) / Action

[Previous](Clear.md) | [Next](Name.md)

# IMTConAutoAction::Action

Get the [action](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_action) performed upon the triggering of an automation task.

C++
    
    
    UINT  IMTConAutoAction::Action()  const

.NET (Gateway/Manager API)
    
    
    EnActions  CIMTConAutoAction.Action()

Python
    
    
    MTConAutoAction.Action

### Return Value

[IMTConAutoAction::EnActions (#enactions)](Enumerations.md#enactions) enumeration value.

# IMTConAutoAction::Action

Set the [action](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_action) performed upon the triggering of an automation task.

C++
    
    
    MTAPIRES  IMTConAutoAction::Action(
       const UINT     action   // Action type
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAutoAction.Action(
       EnActions      action   // Action type
       )

Python
    
    
    MTConAutoAction.Action

### Parameters

**action**  
[in] The action performed upon the triggering of an automation task. The value is passed using theIMTConAutoAction::EnActionsenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
