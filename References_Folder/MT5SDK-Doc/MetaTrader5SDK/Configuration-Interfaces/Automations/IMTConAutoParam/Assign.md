[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Automations](../../Automations.md) / [IMTConAutoParam](../IMTConAutoParam.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTConAutoParam::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTConAutoParam::Assign(
       const IMTConAutoParam*  param  // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConAutoParam.Assign(
       CIMTConAutoParam        param  // Source object
       )

### Parameters

**param**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
