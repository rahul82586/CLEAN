[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Floating Margin](../../Floating-Margin.md) / [IMTConLeverageArray](../IMTConLeverageArray.md) / Delete

[Previous](AddCopy.md) | [Next](Detach.md)

# IMTConLeverageArray::Delete

Delete a floating margin configuration object by position.

C++
    
    
    MTAPIRES  IMTConLeverageArray::Delete(
       const UINT  pos      // Configuration position
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConLeverageArray.Delete(
       uint        pos      // Configuration position
       )

### Parameters

**pos**  
[in] Position of the configuration in the array, starting from 0.

### Return Value

An indication of a successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, the code of the encountered error is returned.

### Note

The object being deleted will be automatically released by calling [IMTConLeverage::Release](../IMTConLeverage/Release.md).
