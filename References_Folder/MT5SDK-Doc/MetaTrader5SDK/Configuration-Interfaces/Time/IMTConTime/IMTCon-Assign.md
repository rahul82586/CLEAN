[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Time](../../Time.md) / [IMTConTime](../IMTCon.md) / IMTCon Assign

[Previous](IMTCon-Release.md) | [Next](IMTCon-Clear.md)

# IMTConTime::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTConTime::Assign(
       const IMTConTime*  param      // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConTime.Assign(
       CIMTConTime  param      // Source object
       )

### Parameters

**param**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
