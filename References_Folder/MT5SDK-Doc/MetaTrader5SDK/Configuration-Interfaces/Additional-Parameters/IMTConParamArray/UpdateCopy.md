[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Additional Parameters](../../Additional-Parameters.md) / [IMTConParamArray](../IMTConParamArray.md) / UpdateCopy

[Previous](Update.md) | [Next](Shift.md)

# IMTConParamArray::UpdateCopy

Changes a parameter at the specified position of an array by copying the passed parameter object.

C++
    
    
    MTAPIRES  IMTConParamArray::UpdateCopy(
       const UINT          pos,       // Position
       const IMTConParam*  param      // Parameter object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConParamArray.UpdateCopy(
       uint                pos,       // Position
       CIMTConParam        param      // Parameter object
       )

### Parameters

**pos**  
[in] The position of a parameter in the array, starting with 0.

**param**  
[in] Parameter object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The method copies the 'param' object to the parameter object at the specified position of an array.
