[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Clients](../Clients.md) / CommentCreateArray

[Previous](CommentCreate.md) | [Next](CommentAdd.md)

# IMTAdminAPI::CommentCreateArray

Create an object of the array of comments.

C++
    
    
    IMTClientArray*  IMTAdminAPI::CommentCreateArray()

.NET
    
    
    CIMTClientArray  CIMTAdminAPI.CommentCreateArray()

### Return Value

Returns a pointer to the created object that implements the [IMTCommentArray](../../../Database-Interfaces/Clients/IMTCommentArray.md) interface. NULL is returned in case of failure.

### Note

The created object must be destroyed by calling the [IMTCommentArray::Release](../../../Database-Interfaces/Clients/IMTCommentArray/Release.md) method of this object.
