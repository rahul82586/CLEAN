[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Additional Parameters](../../Additional-Parameters.md) / [IMTConParamArray](../IMTConParamArray.md) / Delete

[Previous](AddCopy.md) | [Next](Detach.md)

# IMTConParamArray::Delete

Deletes an object of a parameter at the specified position.

C++
    
    
    MTAPIRES  IMTConParamArray::Delete(
       const UINT  pos      // Position of the parameter
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConParamArray.Delete(
       uint        pos      // Position of the parameter
       )

### Parameters

**pos**  
[in] The position of a parameter in the array, starting with 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The object to delete will be automatically released by calling the [IMTConParam::Release](../IMTConParam/Release.md) method.
