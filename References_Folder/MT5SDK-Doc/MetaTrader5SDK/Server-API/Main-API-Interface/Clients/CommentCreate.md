[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Clients](../Clients.md) / CommentCreate

[Previous](DocumentGetHistory.md) | [Next](CommentCreateArray.md)

# IMTServerAPI::CommentCreate

Create a comment object.
    
    
    IMTClient*  IMTServerAPI::CommentCreate()

### Return Value

Returns a pointer to the created object that implements the [IMTComment](../../../Database-Interfaces/Clients/IMTComment.md) interface. NULL is returned in case of failure.

### Note

The created object must be destroyed by calling the [IMTComment::Release](../../../Database-Interfaces/Clients/IMTComment/Release.md) method of this object.
