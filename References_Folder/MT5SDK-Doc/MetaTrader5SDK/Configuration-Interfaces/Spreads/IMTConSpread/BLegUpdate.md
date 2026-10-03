[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Spreads](../../Spreads.md) / [IMTConSpread](../IMTConSpread.md) / BLegUpdate

[Previous](BLegAdd.md) | [Next](BLegDelete.md)

# IMTConSpread::BLegUpdate

Update spread B leg by the index.

C++
    
    
    MTAPIRES  IMTConSpread::BLegUpdate(
       const UINT        pos,     // Spread leg position
       IMTConSpreadLeg*  leg      // Spread leg object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSpread.BLegUpdate(
       uint              pos,     // Spread leg position
       CIMTConSpreadLeg  leg      // Spread leg object
       )

Python (Manager API)
    
    
    MTConSpread.BLegUpdate(
       pos,              # Spread leg position
       leg               # Spread leg object
       )
    
    
    MTConSpread.BLegSet(
       leg_list          # A list of spread leg objects
       )

### Parameters

**pos**  
[in] Spread leg position in the list starting with 0.

**leg**  
[in]Spread legsobject.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
