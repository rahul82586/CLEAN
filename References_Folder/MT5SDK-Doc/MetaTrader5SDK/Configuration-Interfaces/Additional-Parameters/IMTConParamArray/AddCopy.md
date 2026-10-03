[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Additional Parameters](../../Additional-Parameters.md) / [IMTConParamArray](../IMTConParamArray.md) / AddCopy

[Previous](Add.md) | [Next](Delete.md)

# IMTConParamArray::AddCopy

Add a copy of an object of parameters at the end of an array.

C++
    
    
    MTAPIRES  IMTConParamArray::AddCopy(
       const IMTConParam*  param      // Added parameter
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConParamArray.AddCopy(
       CIMTConParam        param      // Added parameter
       )

### Parameters

**param**  
[in] Parameter object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method creates a copy of the 'param' object and places it at the end of the array.

# IMTConParamArray::AddCopy

Adds copies of parameter objects into an array.

C++
    
    
    MTAPIRES  IMTConParamArray::AddCopy(
       const IMTConParamArray*  array      // The added array of parameters
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConParamArray.AddCopy(
       CIMTConParamArray        array      // The added array of parameters
       )

### Parameters

**array**  
[in] The object of the array of parameters.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method creates copies of the objects of parameters belonging to the 'array' object, and inserts them at the end of the current array.
