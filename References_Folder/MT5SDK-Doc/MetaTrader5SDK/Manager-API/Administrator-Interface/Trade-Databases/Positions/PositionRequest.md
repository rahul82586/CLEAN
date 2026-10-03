[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Positions](../Positions.md) / PositionRequest

[Previous](PositionCreateArray.md) | [Next](PositionRequestByGroup.md)

# IMTAdminAPI::PositionRequest

Request from the server open positions by login.

C++
    
    
    MTAPIRES  IMTAdminAPI::PositionRequest(
       const UINT64       login,        // User's login
       IMTPositionArray*  positions     // An object of the array of positions
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.PositionRequest(
       ulong              login,        // User's login
       CIMTPositionArray  positions     // An object of the array of positions
       )

Python
    
    
    AdminAPI.PositionRequest(
       int                login         # User's login
       )

### Parameters

**login**  
[in] The login of a user.

**positions**  
[out] An object of the array of trade positions. The position object must be first created using theIMTAdminAPI::PositionCreateArraymethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies the array of positions of a client with the specified login to the position object.
