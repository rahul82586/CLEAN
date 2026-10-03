[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Spreads](../../Spreads.md) / [IMTConSpreadLeg](../IMTConSpreadLeg.md) / Clear

[Previous](Assign.md) | [Next](Mode.md)

# IMTConSpreadLeg::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTConSpreadLeg::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSpreadLeg.Clear()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method clears all fields ​​and removes embedded objects.
