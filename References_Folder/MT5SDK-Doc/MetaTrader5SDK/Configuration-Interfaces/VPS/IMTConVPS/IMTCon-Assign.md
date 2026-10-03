[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [VPS](../../VPS.md) / [IMTConVPS](../IMTCon.md) / IMTCon Assign

[Previous](IMTCon-Release.md) | [Next](IMTCon-Clear.md)

# IMTConVPS::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTConVPS::Assign(
       const IMTConVPS*  param  // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConVPS.Assign(
       CIMTConVPS        param  // Source object
       )

### Parameters

**param**  
[in] Source object.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
