[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Spreads](../../Spreads.md) / [IMTConSpread](../IMTConSpread.md) / BLegClear

[Previous](BLegDelete.md) | [Next](BLegShift.md)

# IMTConSpread::BLegClear

Clear the list of all spread B legs.

C++
    
    
    MTAPIRES  IMTConSpread::BLegClear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSpread.BLegClear()

Python (Manager API)
    
    
    MTConSpread.BLegClear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
