[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Positions](../Positions.md) / PositionRequest

[Previous](PositionGetBySymbol.md) | [Next](PositionRequestByGroup.md)

# IMTManagerAPI::PositionRequest

Request from the server open positions by login.

C++
    
    
    MTAPIRES  IMTManagerAPI::PositionRequest(
       const UINT64       login,         // User's login
       IMTPositionArray*  positions      // An object of the array of positions
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.PositionRequest(
       ulong              login,         // User's login
       CIMTPositionArray  positions      // An object of the array of positions
       )

Python
    
    
    ManagerAPI.PositionRequest(
       int                login          # User's login
       )

### Parameters

**login**  
[in] The login of a user.

**positions**  
[out] An object of the array of trade positions. The position object must be first created using theIMTManagerAPI::PositionCreateArraymethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies the array of positions of a client with the specified login to the position object.
