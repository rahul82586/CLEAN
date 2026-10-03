[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Floating Margin](../../Floating-Margin.md) / [IMTConLeverageArray](../IMTConLeverageArray.md) / Next

[Previous](Total.md) | [Next](Sort.md)

# IMTConLeverageArray::Next

Get a floating margin configuration object by position.

C++
    
    
    IMTConLeverage*  IMTConLeverageArray::Next(
       const UINT  index      // Configuration position
       )  const

.NET (Gateway/Manager API)
    
    
    CIMTConLeverage  CIMTConLeverageArray.Next(
       uint        index      // Configuration position
       )

### Parameters

**index**  
[in] Position of the configuration in the array, starting from 0.

### Return Value

If successful, the method returns a pointer to the [IMTConLeverage](../IMTConLeverage.md) configuration object located at the corresponding position in the array. Otherwise, it returns NULL.

### Note

The lifetime of the returned object is controlled by the current array object. Consequently, when the array object is deleted, the returned pointer will become invalid.
