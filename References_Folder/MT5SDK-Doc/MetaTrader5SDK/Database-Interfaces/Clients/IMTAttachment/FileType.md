[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTAttachment](../IMTAttachment.md) / FileType

[Previous](RelatedClient.md) | [Next](FileName.md)

# IMTAttachment::FileType

Get the file type.

C++
    
    
    UINT  IMTAttachment::FileType()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTAttachment.FileType()

### Return Value

A value of the [IMTAttachment::EnFileType (#enfiletype)](Enumerations.md#enfiletype) enumeration.

# IMTAttachment::FileType

Set the file type.

C++
    
    
    MTAPIRES  IMTAttachment::FileType(
       const UINT  type        // File type
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTAttachment.FileType(
       uint        type        // File type
       )

### Parameters

**type**  
[in] File type. The type is passed using theIMTAttachment::EnFileTypeenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
