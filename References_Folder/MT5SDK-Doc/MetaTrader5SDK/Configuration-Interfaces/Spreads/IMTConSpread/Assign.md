[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Spreads](../../Spreads.md) / [IMTConSpread](../IMTConSpread.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTConSpread::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTConSpread::Assign(
       const IMTConSpread*  spread      // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConSpread.Assign(
       CIMTConSpread        spread      // Source object
       )

### Parameters

**spread**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
