[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Additional Parameters](../../Additional-Parameters.md) / [IMTConParamArray](../IMTConParamArray.md) / Update

[Previous](Detach.md) | [Next](UpdateCopy.md)

# IMTConParamArray::Update

Changes a parameter at the specified position of an array.

C++
    
    
    MTAPIRES  IMTConParamArray::Update(
       const UINT     pos,       // Position
       IMTConParama*  param      // Parameter object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConParamArray.Update(
       uint           pos,       // Position
       CIMTConParama  param      // Parameter object
       )

### Parameters

**pos**  
[in] Position of a daily report in an array, starting with 0.

**param**  
[in] Parameter object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The IMTConParamArray::Update method deletes the previous element (call of [IMTConParam::Release](../IMTConParam/Release.md)) and replaces it with a new one. After that, the lifetime of a new element is controlled by an array object. Thus, when deleting an array object (call of IMTConParamArray::Release), an earlier inserted object will be automatically removed.

In turn, the removal of a previously inserted object will cause the pointer to it, which is stored inside an array object, to be no longer valid. Therefore, call to this pointer (including the case of array object deletion) will cause crash of the application.

Never add a link to one and the same object in an array, because this will lead to a crash during memory release.
