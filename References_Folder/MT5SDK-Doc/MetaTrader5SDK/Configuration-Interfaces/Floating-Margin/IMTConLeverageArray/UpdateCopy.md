[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Floating Margin](../../Floating-Margin.md) / [IMTConLeverageArray](../IMTConLeverageArray.md) / UpdateCopy

[Previous](Update.md) | [Next](Shift.md)

# IMTConLeverageArray::UpdateCopy

Update the floating margin configuration at the specified array position by copying the passed configuration object.

C++
    
    
    MTAPIRES  IMTConLeverageArray::UpdateCopy(
       const UINT             pos,    // Position
       const IMTConLeverage*  record  // Configuration object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConLeverageArray.UpdateCopy(
       uint                   pos,    // Position
       CIMTConLeverage        record  // Configuration object
       )

### Parameters

**pos**  
[in] Position of the configuration in the array, starting from 0.

**record**  
[in]IMTConLeverageconfiguration object.

### Return Value

An indication of a successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The method copies the 'record' object to the configuration object located at the specified position of the array.
