[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTAttachment](../IMTAttachment.md) / FileFlags

[Previous](FileSize.md) | [Next](../IMTAttachmentArray.md)

# IMTAttachment::FileFlags

Get the file flags.

C++
    
    
    UINT  IMTAttachment::FileFlags()  const

.NET (Gateway/Manager API)
    
    
    uint  CIMTAttachment.FileFlags()

### Return Value

A value of the [IMTAttachment::EnFileFlags (#enfileflags)](Enumerations.md#enfileflags) enumeration.

# IMTAttachment::FileFlags

Set the file flags.

C++
    
    
    MTAPIRES  IMTAttachment::FileFlags(
       const UINT  type        // File flags
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTAttachment.FileFlags(
       uint        type        // File flags
       )

### Parameters

**type**  
[in] File flags. The flags are passed using theIMTAttachment::EnFileFlagsenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
