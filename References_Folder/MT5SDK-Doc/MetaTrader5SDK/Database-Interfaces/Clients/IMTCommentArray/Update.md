[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTCommentArray](../IMTCommentArray.md) / Update

[Previous](Detach.md) | [Next](UpdateCopy.md)

# IMTCommentArray::Update

Change a comment at the specified position of an array.

C++
    
    
    MTAPIRES  IMTCommentArray::Update(
       const UINT   pos,      // Position
       IMTComment*  comment   // Comment object
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTCommentArray.Update(
       uint         pos,      // Position
       CIMTComment  comment   // Comment object
       )

### Parameters

**pos**  
[in] Comment position in an array, starting with 0.

**comment**  
[in]Comment object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The IMTCommentArray::Update method deletes the previous element ([IMTComment::Release](../IMTComment/Release.md) call) and replaces it with a new one. After that, the lifetime of a new element is controlled by an array object. Thus, when deleting an array object (by a call of IMTCommentArray::Release), an earlier inserted object is automatically removed.

### Example
    
    
    //--- example
       IMTCommentArray *array   =api->CommentCreateArray();   
       IMTComment      *comment1=api->CommentCreate();
       IMTComment      *comment2=api->CommentCreate();
    //---
       array->Add(comment1);
       array->Update(0,comment2); // the first element (the comment1 object) is replaced by comment2
       //--- after that the comment1 element will be released via Release, and the comment2 lifetime will be controlled by the array
