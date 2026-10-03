[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Floating Margin](../../Floating-Margin.md) / [IMTConLeverageArray](../IMTConLeverageArray.md) / Add

[Previous](Clear.md) | [Next](AddCopy.md)

# IMTConLeverageArray::Add

Add a floating margin configuration object to the end of the array.

C++
    
    
    MTAPIRES  IMTConLeverageArray::Add(
       IMTConLeverage*  record    // Configuration object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConLeverageArray.Add(
       CIMTConLeverage  record    // Configuration object
       )

### Parameters

**record**  
[in]IMTConLeverageconfiguration object.

### Return Value

An indication of a successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, the code of the encountered error is returned.

### Note

This method places a pointer to a passed object at the end of an array. Upon successful method call, the control over the lifetime of the 'record' object is transferred to the array object. Thus, when the array object is deleted (using[IMTClientArray::Release](Release.md)), the earlier added object will be automatically removed.

# IMTConLeverageArray::Add

Add an object of a floating margin configuration array to the end of the array.

C++
    
    
    MTAPIRES  IMTConLeverageArray::Add(
       IMTConLeverageArray*  array      // Array of configurations to be added
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConLeverageArray.Add(
       CIMTConLeverageArray  array      // Array of configurations to be added
       )

### Parameters

**array**  
[in] Configuration array objectIMTConLeverageArray.

### Return Value

An indication of a successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, the code of the encountered error is returned.

### Note

This method appends pointer from the 'array' object to the end of the current array and clears the 'array' object.
