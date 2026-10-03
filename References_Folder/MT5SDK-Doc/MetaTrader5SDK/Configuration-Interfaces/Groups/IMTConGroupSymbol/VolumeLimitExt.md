[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSymbol](../IMTConGroupSymbol.md) / VolumeLimitExt

[Previous](VolumeLimit.md) | [Next](VolumeLimitDefault.md)

# IMTConGroupSymbol::VolumeLimitExt

Gets the maximum aggregate volume (with extended accuracy) of positions and orders for a symbol for this group.

C++
    
    
    UINT64  IMTConGroupSymbol::VolumeLimitExt()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTConGroupSymbol.VolumeLimitExt()

Python (Manager API)
    
    
    MTConGroupSymbol.VolumeLimitExt

### Return Value

The maximum allowed aggregate volume of positions and orders in one direction for a symbol for this group. The volume is specified in the UINT64 format (one unit corresponds to 1/100000000 lot, for example, 105000000 means 1.05 lots).

### Note

For example: if the limit is 5 lots, you may have an open position of 5 lots and place a Sell Limit order of 5 lots as well. But in this case you cannot place a pending Buy Limit order (since the total volume in one direction will exceed the limit) or place a Sell Limit order above 5 lots.

# IMTConGroupSymbol::VolumeLimitExt

Sets the maximum aggregate volume (with extended accuracy) of positions and orders for a symbol for this group.

C++
    
    
    MTAPIRES  IMTConGroupSymbol::VolumeLimitExt(
       const UINT64  volume      // Volume limit
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroupSymbol.VolumeLimitExt(
       ulong         volume      // Volume limit
       )

Python (Manager API)
    
    
    MTConGroupSymbol.VolumeLimitExt

### Program Parameters

**volume**  
[in] The maximum allowed aggregate volume of positions and orders in one direction for a symbol for this group. The volume is specified in the UINT64 format (one unit corresponds to 1/100000000 lot, for example, 105000000 means 1.05 lots).

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

For example: if the limit is 5 lots, you may have an open position of 5 lots and place a Sell Limit order of 5 lots as well. But in this case you cannot place a pending Buy Limit order (since the total volume in one direction will exceed the limit) or place a Sell Limit order above 5 lots.
