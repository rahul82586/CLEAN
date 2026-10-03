[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTDocument](../IMTDocument.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTDocument::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTDocument::Assign(
       const IMTDocument*     document  // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTDocument.Assign(
       CIMTDocument           document  // Source object
       )

### Parameters

**document**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
