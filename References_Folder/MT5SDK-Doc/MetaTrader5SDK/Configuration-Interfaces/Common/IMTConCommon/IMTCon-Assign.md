[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Common](../../Common.md) / [IMTConCommon](../IMTCon.md) / IMTCon Assign

[Previous](IMTCon-Release.md) | [Next](IMTCon-Clear.md)

# IMTConCommon::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTConCommon::Assign(
       const IMTConCommon*  param      // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConCommon.Assign(
       CIMTConCommon        obj        // Source object
       )

### Parameters

**param**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
