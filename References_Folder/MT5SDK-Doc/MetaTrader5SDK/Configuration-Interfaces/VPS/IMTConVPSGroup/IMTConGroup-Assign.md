[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [VPS](../../VPS.md) / [IMTConVPSGroup](../IMTConGroup.md) / IMTConGroup Assign

[Previous](IMTConGroup-Release.md) | [Next](IMTConGroup-Clear.md)

# IMTConVPSGroup::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTConVPSGroup::Assign(
       const IMTConVPSGroup*  param  // source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConVPSGroup.Assign(
       CIMTConVPSGroup        param  // source object
       )

### Parameters

**param**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
