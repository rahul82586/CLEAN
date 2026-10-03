[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutomation](../IMTConAutomation.md) / ActionShift

[Previous](ActionClear.md) | [Next](ActionTotal.md)

# IMTConAutomation::ActionShift

Move an automation task [action](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_action) in the list.

C++
    
    
    MTAPIRES  IMTConAutomation::ActionShift(
       const UINT  pos,       // Action position
       const int   shift      // Shift
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAutomation.ActionShift(
       uint        pos,       // Action position
       int         shift      // Shift
       )

Python
    
    
    MTConAutomation.ActionShift(
       pos,        # Action position
       shift       # Shift
       )

### Parameters

**pos**  
[in] Action position in the list starting at 0.

**shift**  
[in] The shift of the action relative to its current position. A negative value means shift to the top of the list, a positive value - to its end.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
