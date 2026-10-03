[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Spreads](../../Spreads.md) / [IMTConSpread](../IMTConSpread.md) / BLegAdd

[Previous](ALegNext.md) | [Next](BLegUpdate.md)

# IMTConSpread::BLegAdd

Add configuration of spread B leg.

C++
    
    
    MTAPIRES  IMTConSpread::BLegAdd(
       IMTConSpreadLeg*  leg      // Spread leg object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSpread.BLegAdd(
       CIMTConSpreadLeg  leg      // Spread leg object
       )

Python (Manager API)
    
    
    MTConSpread.BLegAdd(
       leg               # Spread leg object
       )

### Parameters

**leg**  
[in]Spread legsobject.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The leg type is not connected with some definite position direction (buy or sell). Note that client's positions at all leg's symbols should be either long or short.
