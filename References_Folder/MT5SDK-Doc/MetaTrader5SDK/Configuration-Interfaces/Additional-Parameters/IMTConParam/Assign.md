[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Additional Parameters](../../Additional-Parameters.md) / [IMTConParam](../IMTConParam.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTConParam::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTConParam::Assign(
       const IMTConParam*  param      // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConParam.Assign(
       CIMTConParam        param      // Source object
       )

### Parameters

**param**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
