[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Floating Margin](../../Floating-Margin.md) / [IMTConLeverageArray](../IMTConLeverageArray.md) / AddCopy

[Previous](Add.md) | [Next](Delete.md)

# IMTConLeverageArray::AddCopy

Add a copy of a floating margin configuration object to the end of the array.

C++
    
    
    MTAPIRES  IMTConLeverageArray::AddCopy(
       const IMTConLeverage*  record    // Configuration to be added
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConLeverageArray.AddCopy(
       CIMTConLeverage        record    // Configuration to be added
       )

### Parameters

**record**  
[in]IMTConLeverageconfiguration object.

### Return Value

An indication of a successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, the code of the encountered error is returned.

### Note

This method creates a copy of the 'record' object and appends it to the end of the array.

# IMTConLeverageArray::AddCopy

Add copies of floating margin configuration objects to an array.

C++
    
    
    MTAPIRES  IMTConLeverageArray::AddCopy(
       const IMTConLeverageArray*  array      // Array with configurations to be added
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConLeverageArray.AddCopy(
       CIMTConLeverageArray        array      // Array of configurations to be added
       )

### Parameters

**array**  
[in] Configuration array objectIMTConSymbolArray.

### Return Value

An indication of a successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, the code of the encountered error is returned.

### Note

This method creates copies of the objects belonging to the 'array' object and appends them to the end of the current array.
