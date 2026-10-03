[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTComment](../IMTComment.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTComment::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTComment::Assign(
       const IMTComment*      comment   // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  IMTComment.Assign(
       CIMTComment            comment   // Source object
       )

### Parameters

**comment**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
