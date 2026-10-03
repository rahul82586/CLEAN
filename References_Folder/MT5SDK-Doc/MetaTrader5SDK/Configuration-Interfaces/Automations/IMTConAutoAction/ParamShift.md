[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutoAction](../IMTConAutoAction.md) / ParamShift

[Previous](ParamClear.md) | [Next](ParamTotal.md)

# IMTConAutoAction::ParamShift

Shift a parameter of an automation task action.

C++
    
    
    MTAPIRES  IMTConAutoAction::ParamShift(
       const UINT  pos,       // Parameter position
       const int   shift      // Shift
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAutoAction.ParamShift(
       uint        pos,       // Parameter position
       int         shift      // Shift
       )

Python
    
    
    MTConAutoAction.ParamShift(
       pos,        # Parameter position
       shift       # Shift
       )

### Parameters

**pos**  
[in] The position of the parameter in the list starting at 0.

**shift**  
[in] Parameter shift relative to its current position. A negative value means shift to the top of the list, a positive value - to its end.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
