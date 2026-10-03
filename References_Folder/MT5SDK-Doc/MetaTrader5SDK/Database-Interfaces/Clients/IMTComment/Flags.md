[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTComment](../IMTComment.md) / Flags

[Previous](RelatedDocument.md) | [Next](Extra.md)

# IMTComment::Flags

Get comment flags.

C++
    
    
    UINT64  IMTComment::Flags()  const

.NET (Gateway/Manager API)
    
    
    ulong  CIMTComment.Flags()

### Return Value

Comment flags. The flags are passed using the [IMTComment::EnCommentFlags (#encommentflags)](Enumerations.md#encommentflags) enumeration.

### Note

This method is reserved for future use.

# IMTComment::Flags

Set comment flags.

C++
    
    
    MTAPIRES  IMTComment::Flags(
       const UINT64  flags      // Comment flags
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTComment.Flags(
       ulong         flags      // Comment flags
       )

### Parameters

**flags**  
[in] Comment flags. The flags are passed using theIMTComment::EnCommentFlagsenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### 
