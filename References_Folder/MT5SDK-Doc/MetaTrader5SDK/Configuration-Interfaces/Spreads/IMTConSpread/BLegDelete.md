[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Spreads](../../Spreads.md) / [IMTConSpread](../IMTConSpread.md) / BLegDelete

[Previous](BLegUpdate.md) | [Next](BLegClear.md)

# IMTConSpread::BLegDelete

Delete spread A leg by the index.

C++
    
    
    MTAPIRES  IMTConSpread::BLegDelete(
       const UINT  pos       // Spread leg position
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSpread.BLegDelete(
       uint        pos       // Spread leg position
       )

Python (Manager API)
    
    
    MTConSpread.BLegDelete(
       pos         # Spread leg position
       )

### Parameters

**pos**  
[in] Spread leg position starting from 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Several symbols can be configured for each leg (several spread leg configurations can be created).
