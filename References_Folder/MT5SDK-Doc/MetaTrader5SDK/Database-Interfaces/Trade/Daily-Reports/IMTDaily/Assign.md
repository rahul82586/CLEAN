[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Daily Reports](../../Daily-Reports.md) / [IMTDaily](../IMTDaily.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTDaily::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTDaily::Assign(
       const IMTDaily*  exec      // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDaily.Assign(
       CIMTDaily        exec      // Source object
       )

### Parameters

**exec**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
