[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTCommentArray](../IMTCommentArray.md) / AddCopy

[Previous](Add.md) | [Next](Delete.md)

# IMTCommentArray::AddCopy

Add a copy of a comment object to the end of an array.

C++
    
    
    MTAPIRES  IMTCommentArray::AddCopy(
       const IMTComment*  comment  // Comment to be added
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTCommentArray.AddCopy(
       CIMTComment        comment  // Comment to be added
       )

### Parameters

**comment**  
[in]Comment object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method creates a copy of the 'comment' object and places it at the end of the array.

# IMTCommentArray::AddCopy

Add copies of client objects into an array.

C++
    
    
    MTAPIRES  IMTCommentArray::AddCopy(
       const IMTCommentArray*  array     // Array of comments to be added
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTCommentArray.AddCopy(
       CIMTCommentArray       array      // Array of comments to be added
       )

### Parameters

**array**  
[in] Object of the comments array.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method creates copies of comment objects belonging to the 'array' object and inserts them at the end of the current array.
