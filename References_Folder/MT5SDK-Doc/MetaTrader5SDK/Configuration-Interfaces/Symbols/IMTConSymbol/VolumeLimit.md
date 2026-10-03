[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbol](../IMTConSymbol.md) / VolumeLimit

[Previous](VolumeStepExt.md) | [Next](VolumeLimitExt.md)

# IMTConSymbol::VolumeLimit

Gets the maximum aggregate volume of positions and orders for a symbol in one direction.

C++
    
    
    UINT64  IMTConSymbol::VolumeLimit()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTConSymbol.VolumeLimit()

Python (Manager API)
    
    
    MTConSymbol.VolumeLimit

### Return Value

The maximum allowed aggregate volume of positions and orders for a symbol in one direction. Volume is specified in the UINT64 format (one unit corresponds to 1/10000 lot, for example, 10500 means 1.05 lots).

### Note

Example: if the limit is 5 lots, you may have an open position of 5 lots and place a Sell Limit order of 5 lots as well. But in this case, you cannot place a pending Buy Limit order (since the total volume in one direction will exceed the limit) or place a Sell Limit order above 5 lots.

# IMTConSymbol::VolumeLimit

Sets the maximum aggregate volume of positions and orders for a symbol in one direction.

C++
    
    
    MTAPIRES  IMTConSymbol::VolumeLimit(
       const UINT64  volume      // Maximum aggregate volume
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSymbol.VolumeLimit(
       luong         volume      // Maximum aggregate volume
       )

Python (Manager API)
    
    
    MTConSymbol.VolumeLimit

### Parameters

**volume**  
[in] The maximum allowed aggregate volume of positions and orders for a symbol in one direction. Volume is specified in the UINT64 format (one unit corresponds to 1/10000 lot, for example, 10500 means 1.05 lots).

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

Example: if the limit is 5 lots, you may have an open position of 5 lots and place a Sell Limit order of 5 lots as well. But in this case, you cannot place a pending Buy Limit order (since the total volume in one direction will exceed the limit) or place a Sell Limit order above 5 lots.
