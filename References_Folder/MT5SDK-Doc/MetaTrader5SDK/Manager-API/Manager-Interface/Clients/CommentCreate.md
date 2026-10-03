[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Clients](../Clients.md) / CommentCreate

[Previous](DocumentRequestHistory.md) | [Next](CommentCreateArray.md)

# IMTManagerAPI::CommentCreate

Create a comment object.

C++
    
    
    IMTClient*  IMTManagerAPI::CommentCreate()

.NET
    
    
    CIMTClient  CIMTManagerAPI.CommentCreate()

### Return Value

Returns a pointer to the created object that implements the [IMTComment](../../../Database-Interfaces/Clients/IMTComment.md) interface. NULL is returned in case of failure.

### Note

The created object must be destroyed by calling the [IMTComment::Release](../../../Database-Interfaces/Clients/IMTComment/Release.md) method of this object.
