[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupSymbol](../IMTConGroupSymbol.md) / VolumeLimit

[Previous](VolumeStepExtDefault.md) | [Next](VolumeLimitExt.md)

# IMTConGroupSymbol::VolumeLimit

Gets the maximum allowable aggregate volume of positions and orders on a symbol in one direction for this group.

C++
    
    
    UINT64  IMTConGroupSymbol::VolumeLimit()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTConGroupSymbol.VolumeLimit()

Python (Manager API)
    
    
    MTConGroupSymbol.VolumeLimit

### Return Value

The maximum allowable aggregate volume of positions and orders on a symbol in one direction for this group. The volume is specified in the UINT64 format (one unit corresponds to 1/10000 lot, for example, 10500 means 1.05 lots).

### Note

Example: if the limit is 5 lots, you may have an open position of 5 lots and place a Sell Limit order of 5 lots as well. But in this case, you cannot place a pending Buy Limit order (since the total volume in one direction will exceed the limit) or place a Sell Limit order above 5 lots.

# IMTConGroupSymbol::VolumeLimit

Sets the maximum allowable aggregate volume of positions and orders on a symbol in one direction for this group.

C++
    
    
    MTAPIRES  IMTConGroupSymbol::VolumeLimit(
       const UINT64  volume      // Volume limit
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConGroupSymbol.VolumeLimit(
       ulong         volume      // Volume limit
       )

Python (Manager API)
    
    
    MTConGroupSymbol.VolumeLimit

### Parameters

**volume**  
[in] The maximum allowable aggregate volume of positions and orders on a symbol in one direction for this group. The volume is specified in the UINT64 format (one unit corresponds to 1/10000 lot, for example, 10500 means 1.05 lots).

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

Example: if the limit is 5 lots, you may have an open position of 5 lots and place a Sell Limit order of 5 lots as well. But in this case, you cannot place a pending Buy Limit order (since the total volume in one direction will exceed the limit) or place a Sell Limit order above 5 lots.
