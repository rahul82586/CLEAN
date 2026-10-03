[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Trade](../../Trade.md) / [Positions](../Positions.md) / PositionGet

[Previous](PositionUpdate.md) | [Next](PositionGetByTicket.md)

# IMTServerAPI::PositionGet

Get a trade position.
    
    
    MTAPIRES  IMTServerAPI::PositionGet(
       const UINT64  login,        // User's login
       LPCWSTR       symbol,       // Symbol
       IMTPosition*  position      // Position object
       )

### Parameters

**login**  
[in] The login of a user whose position should be obtained.

**symbol**  
[in] The symbol, for which you need to get a position.

**position**  
[out] An object of a trade position. The position object must be first created using theIMTServerAPI::PositionCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies the data of a position of specified client and the specified symbol to the position object.

# IMTServerAPI::PositionGet

Get an array of positions by the login.
    
    
    MTAPIRES  IMTServerAPI::PositionGet(
       const UINT64       login,        // User's login
       IMTPositionArray*  position      // An object of the array of positions
       )

### Parameters

**login**  
[in] The login of a user.

**position**  
[out] An object of the array of trade positions. The position object must be first created using theIMTServerAPI::PositionCreateArraymethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies the array of positions of a client with the specified login to the position object.
