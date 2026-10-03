[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Managers](../../Managers.md) / [IMTConManagerReport](../IMTConManagerReport.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTConManagerReport::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTConManagerReport::Assign(
       const IMTConManagerReport*  access      // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConManagerReport.Assign(
       CIMTConManagerReport        access      // Source object
       )

### Parameters

**access**  
[in] Source object.

### Return Value

An indication of a successful performance is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error corresponding to the response code occurred.
