[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Additional Parameters](../../Additional-Parameters.md) / [IMTConParamArray](../IMTConParamArray.md) / Add

[Previous](Clear.md) | [Next](AddCopy.md)

# IMTConParamArray::Add

Adds an object of a parameter at the end of an array.

C++
    
    
    MTAPIRES  IMTConParamArray::Add(
       IMTConParam*  param      // An object of the parameter
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConParamArray.Add(
       CIMTConParam  param      // An object of the parameter
       )

### Parameters

**param**  
[in] Parameter object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method places a pointer to a passed object at the end of an array. After a successful call of this method, the control over the life time of the 'param' object is passed to the array object. Thus, when deleting an array object (call of [IMTConParamArray::Release](Release.md)), an earlier inserted object will be automatically removed.

# IMTConParamArray::Add

Adds an object of the array of parameters at the end of an array.

C++
    
    
    MTAPIRES  IMTConParamArray::Add(
       IMTConParamArray*  array      // Added array of parameters
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConParamArray.Add(
       CIMTConParamArray  array      // Added array of parameters
       )

### Parameters

**array**  
[in] The object of the array of parameters.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method places the pointers, which are in the array object, at the end of the current array and clears the array object.
