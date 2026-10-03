[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Clients](../Clients.md) / CommentCreateArray

[Previous](CommentCreate.md) | [Next](CommentSubscribe.md)

# IMTServerAPI::CommentCreateArray

Create an object of the array of comments.
    
    
    IMTClientArray*  IMTServerAPI::CommentCreateArray()

### Return Value

Returns a pointer to the created object that implements the [IMTCommentArray](../../../Database-Interfaces/Clients/IMTCommentArray.md) interface. NULL is returned in case of failure.

### Note

The created object must be destroyed by calling the [IMTCommentArray::Release](../../../Database-Interfaces/Clients/IMTCommentArray/Release.md) method of this object.
