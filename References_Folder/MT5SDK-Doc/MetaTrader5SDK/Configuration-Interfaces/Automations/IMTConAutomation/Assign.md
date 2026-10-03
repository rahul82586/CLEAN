[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutomation](../IMTConAutomation.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTConAutomation::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTConAutomation::Assign(
       const IMTConAutomation*  automation  // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAutomation.Assign(
       CIMTConAutomation        automation  // Source object
       )

### Parameters

**automation**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
