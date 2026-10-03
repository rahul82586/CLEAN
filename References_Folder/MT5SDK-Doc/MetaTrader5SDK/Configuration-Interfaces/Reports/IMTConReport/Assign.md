[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Reports](../../Reports.md) / [IMTConReport](../IMTConReport.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTConReport::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTConReport::Assign(
       const IMTConReport*  param      // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConReport.Assign(
       CIMTConReport        param      // Source object
       )

### Parameters

**param**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
