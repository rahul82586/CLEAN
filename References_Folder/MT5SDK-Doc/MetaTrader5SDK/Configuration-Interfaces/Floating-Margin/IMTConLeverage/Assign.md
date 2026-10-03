[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Floating Margin](../../Floating-Margin.md) / [IMTConLeverage](../IMTConLeverage.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTConLeverage::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTConLeverage::Assign(
       const IMTConLeverage*  cfg  // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConLeverage.Assign(
       CIMTConLeverage        cfg  // Source object
       )

### Parameters

**cfg**  
[in] Source object.

### Return Value

An indication of a successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
