[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Floating Margin](../../Floating-Margin.md) / [IMTConLeverageArray](../IMTConLeverageArray.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTConLeverageArray::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTConLeverageArray::Assign(
       const IMTConLeverageArray*  array  // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConLeverageArray.Assign(
       CIMTConLeverageArray        array  // Source object
       )

### Parameters

**array**  
[in] Source object.

### Return Value

An indication of a successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
