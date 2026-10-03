[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutomation](../IMTConAutomation.md) / ActionDelete

[Previous](ActionUpdate.md) | [Next](ActionClear.md)

# IMTConAutomation::ActionDelete

Delete an automation task [action](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_action) at the specified position.

C++
    
    
    MTAPIRES  IMTConAutomation::ActionDelete(
       const UINT  pos      // Action position
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAutomation.ActionDelete(
       uint        pos      // Action position
       )

Python
    
    
    MTConAutomation.ActionDelete(
       pos         # Action position
       )

### Parameters

**pos**  
[in] Action position in the list starting at 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
