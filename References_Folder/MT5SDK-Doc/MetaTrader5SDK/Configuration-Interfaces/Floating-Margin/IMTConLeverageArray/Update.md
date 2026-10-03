[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Floating Margin](../../Floating-Margin.md) / [IMTConLeverageArray](../IMTConLeverageArray.md) / Update

[Previous](Detach.md) | [Next](UpdateCopy.md)

# IMTConLeverageArray::Update

Update the floating margin configuration at the specified array position.

C++
    
    
    MTAPIRES  IMTConLeverageArray::Update(
       const UINT     pos,       // Position
       IMTConSymbol*  record     // Configuration object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConLeverageArray.Update(
       uint           pos,       // Position
       CIMTConSymbol  record     // Configuration object
       )

### Parameters

**pos**  
[in] Position of the configuration in the array, starting from 0.

**record**  
[in]IMTConLeverageconfiguration object.

### Return Value

An indication of a successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

IMTConLeverageArray::Update deletes the previous element (by calling [IMTConLeverage::Release](../IMTConLeverage/Release.md)) and replaces it with a new one. After that, the lifetime of the new element is controlled by the array object. Thus, when the array object is deleted (using IMTConLeverageArray::Release), the earlier added object will be automatically deleted.
