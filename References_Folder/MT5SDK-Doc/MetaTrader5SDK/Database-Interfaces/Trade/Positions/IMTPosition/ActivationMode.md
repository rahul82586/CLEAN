[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Positions](../../Positions.md) / [IMTPosition](../IMTPosition.md) / ActivationMode

[Previous](APIDataUpdate.md) | [Next](ActivationTime.md)

# IMTPosition::ActivationMode

Get position activation type.

C++
    
    
    UINT  IMTPosition::ActivationMode()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTPosition.ActivationMode()

### Return Value

A value of the [IMTPosition::EnActivation (#enactivation)](Enumerations.md#enactivation) enumeration.

### Note

A position can be in one of three states - the Margin Call level reached, the Stop Out level reached, none of the levels reached.

# IMTPosition::ActivationMode

Sets position activation type.

C++
    
    
    MTAPIRES  IMTPosition::ActivationMode(
       const UINT  mode      // Activation type
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTPosition.ActivationMode(
       uint        mode      // Activation type
       )

### Parameters

**mode**  
[in] Position activation type. The type is passed using theIMTPosition::EnActivationenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

A position can be in one of three states - the Margin Call level reached, the Stop Out level reached, none of the levels reached.
