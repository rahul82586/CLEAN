[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Floating Margin](../../Floating-Margin.md) / [IMTConLeverageArray](../IMTConLeverageArray.md) / Detach

[Previous](Delete.md) | [Next](Update.md)

# IMTConLeverageArray::Detach

Detach a floating margin configuration object from the array.

C++
    
    
    IMTConLeverage*  IMTConLeverageArray::Detach(
       const UINT  pos      // Configuration position
       )

.NET (Gateway/Manager API)
    
    
    CIMTConLeverage  CIMTConLeverageArray.Detach(
       uint        pos      // Configuration position
       )

### Parameters

**pos**  
[in] Position of the configuration in the array, starting from 0.

### Return Value

Returns a pointer to the detached configuration object [IMTConLeverage](../IMTConLeverage.md).

### Note

This method removes the pointer to the object at the given position of the array and returns it. The size of the array is decreased by one, while the deleted object is not freed.
