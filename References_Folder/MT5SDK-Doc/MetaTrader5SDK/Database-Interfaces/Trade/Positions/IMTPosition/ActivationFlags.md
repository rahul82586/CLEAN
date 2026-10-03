[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Positions](../../Positions.md) / [IMTPosition](../IMTPosition.md) / ActivationFlags

[Previous](ActivationPrice.md) | [Next](ApiDataSet.md)

# IMTPosition::ActivationFlags

Get position activation flags.

C++
    
    
    UINT  IMTPosition::ActivationFlags()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTPosition.ActivationFlags()

### Return Value

A value of the [IMTPosition::EnTradeActivationFlags (#entradeactivationflags)](Enumerations.md#entradeactivationflags) enumeration.

# IMTPosition::ActivationPrice

Sets position activation flags.

C++
    
    
    MTAPIRES  IMTPosition::ActivationFlags(
       const UINT  flags      // Activation flags
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTPosition.ActivationFlags(
       uint        flags      // Activation flags
       )

### Parameters

**flags**  
[in] Position activation flags. The flags are passed using theIMTPosition::EnTradeActivationFlagsenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Flags of orders are inherited from the [orders (#entradeactivationflags)](../../Orders/IMTOrder/Enumerations.md#entradeactivationflags), as a result of which the position is created. However, they can be overridden using the [IMTPosition::ActivationFlags](ActivationFlags.md) method (for example, when synchronizing a position via a gateway to an external trading system).
