[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Positions](../../Positions.md) / [IMTPosition](../IMTPosition.md) / Action

[Previous](Symbol.md) | [Next](Digits.md)

# IMTPosition::Action

Get the position type.

C++
    
    
    UINT  IMTPosition::Action()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTPosition.Action()

### Return Value

A value of the [IMTPosition::EnPositionAction (#enpositionaction)](Enumerations.md#enpositionaction) enumeration.

# IMTPosition::Action

Set the position type.

C++
    
    
    MTAPIRES  IMTPosition::Action(
       const UINT  action      // Position type
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTPosition.Action(
       uint        action      // Position type
       )

### Parameters

**action**  
[in] Position type. TheIMTPosition::EnPositionActionenumeration is used to set the type..

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
