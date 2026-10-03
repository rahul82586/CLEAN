[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Floating Margin](../../Floating-Margin.md) / [IMTConLeverageTier](../IMTConLeverageTier.md) / Clear

[Previous](Assign.md) | [Next](RangeFrom.md)

# IMTConLeverageTier::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTConLeverageTier::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConLeverageTier.Clear()

Python (Manager API)
    
    
    bool  MTConLeverageTier.Clear()

### Return Value

An indication of a successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method cleans all fields ​​and removes embedded objects.
