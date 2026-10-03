[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Additional Parameters](../../Additional-Parameters.md) / [IMTConParamArray](../IMTConParamArray.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTConParamArray::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTConParamArray::Assign(
       const IMTConParamArray*  array      // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConParamArray.Assign(
       CIMTConParamArray        array      // Source object
       )

### Parameters

**array**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
