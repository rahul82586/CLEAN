[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTAttachment](../IMTAttachment.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTAttachment::Assign

Assign a passed object to the current one.

C++
    
    
    MTAPIRES  IMTAttachment::Assign(
       const IMTAttachment*   document  // Source object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTAttachment.Assign(
       CIMTAttachment         document  // Source object
       )

### Parameters

**attachment**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
