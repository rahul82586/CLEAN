[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Floating Margin](../../Floating-Margin.md) / [IMTConLeverageRule](../IMTConLeverageRule.md) / Clear

[Previous](Assign.md) | [Next](Name.md)

# IMTConLeverageRule::Clear

Clear an object.

C++
    
    
    MTAPIRES  IMTConLeverageRule::Clear()

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConLeverageRule.Clear()

Python (Manager API)
    
    
    bool  MTConLeverageRule.Clear()

### Return Value

An indication of a successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

This method cleans all fields ​​and removes embedded objects.
