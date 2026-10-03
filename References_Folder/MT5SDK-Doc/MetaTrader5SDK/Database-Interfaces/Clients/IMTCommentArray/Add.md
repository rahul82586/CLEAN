[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTCommentArray](../IMTCommentArray.md) / Add

[Previous](Clear.md) | [Next](AddCopy.md)

# IMTCommentArray::Add

Add a comment object to the end of an array.

C++
    
    
    MTAPIRES  IMTCommentArray::Add(
       IMTComment*  comment   // Comment to be added
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTCommentArray.Add(
       CIMTComment  comment   // Comment to be added
       )

### Parameters

**comment**  
[in]Comment object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method places a pointer to a passed object at the end of an array. After a successful call of this method, the control over the lifetime of the 'comment' object is passed to the array object. Thus, when deleting an array object (by a call of [IMTCommentArray::Release](Release.md)), an earlier inserted object is automatically removed.

# IMTCommentArray::Add

Add a comment array object to the end of an array.

C++
    
    
    MTAPIRES  IMTCommentArray::Add(
       IMTCommentArray*  array     // Array of comments to be added
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTCommentArray.Add(
       CIMTCommentArray  array     // Array of comments to be added
       )

### Parameters

**array**  
[in] Object of the comments array.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method places the pointers, which are in the 'array' object, at the end of the current array and clears the 'array' object.

### Example
    
    
    //--- example
       IMTCommentArray *array  =api->CommentCreateArray();   
       IMTComment      *comment=api->CommentCreate();
    //---
       array->Add(comment);  // after that the lifetime is controlled by the array
       array->Delete(0);     // delete the first element, after that a pointer in 'comment' becomes invalid ('Release' was called)
     
    //--- Incorrect use example
       IMTCommentArray *array  =api->CommentCreateArray();   
       IMTComment      *comment=api->CommentCreate();
    //---
       array->Add(comment);
       array->Add(comment); // in this case the array will contain two pointers to one and the same object!
       //--- an attempt to clear the array will lead to crash, because this will be an attempt to delete the object twice
