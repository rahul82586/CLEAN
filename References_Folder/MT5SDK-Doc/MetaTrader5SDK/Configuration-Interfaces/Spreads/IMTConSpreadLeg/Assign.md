[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Spreads](../../Spreads.md) / [IMTConSpreadLeg](../IMTConSpreadLeg.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTConSpreadLeg::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTConSpreadLeg::Assign(
       const IMTConSpreadLeg*  leg      // source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSpreadLeg.Assign(
       CIMTConSpreadLeg        leg      // source object
       )

### Parameters

**leg**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
