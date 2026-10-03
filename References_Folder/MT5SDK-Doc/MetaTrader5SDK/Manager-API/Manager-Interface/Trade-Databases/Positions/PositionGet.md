[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Positions](../Positions.md) / PositionGet

[Previous](PositionUnsubscribe.md) | [Next](PositionGetByGroup.md)

# IMTManagerAPI::PositionGet

Get an open trade position.

C++
    
    
    MTAPIRES  IMTManagerAPI::PositionGet(
       const UINT64  login,        // User's login
       LPCWSTR       symbol,       // Symbol
       IMTPosition*  position      // Position object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.PositionGet(
       ulong         login,        // User's login
       string        symbol,       // Symbol
       CIMTPosition  position      // Position object
       )

Python
    
    
    ManagerAPI.PositionGet(
       int           login,        # User's login
       str           symbol        # Symbol
       )

### Parameters

**login**  
[in] The login of a user whose position should be deleted.

**symbol**  
[in] The symbol, for which you need to get a position.

**position**  
[out] An object of a trade position. The 'position' object must be first created using theIMTManagerAPI::PositionCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies the data of a position of specified client and the specified symbol to the position object. The method is valid only if the [IMTManagerAPI::PUMP_MODE_POSITIONS](../../Connection-to-the-Server/Pumping-Modes.md) pumping mode was specified during connection.

# IMTManagerAPI::PositionGet

Get an array of open positions of all symbols for the specified login.

C++
    
    
    MTAPIRES  IMTManagerAPI::PositionGet(
       const UINT64       login,        // User's login
       IMTPositionArray*  position      // An object of the array of positions
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.PositionGet(
       ulong              login,        // User's login
       CIMTPositionArray  position      // An object of the array of positions
       )

Python
    
    
    ManagerAPI.PositionGet(
       int                login         # User's login
       )

### Parameters

**login**  
[in] The login of a user.

**position**  
[out] An object of the array of trade positions. The position object must be first created using theIMTManagerAPI::PositionArrayCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies the array of positions of a client with the specified login to the position object. The method is valid only if the [IMTManagerAPI::PUMP_MODE_POSITIONS](../../Connection-to-the-Server/Pumping-Modes.md) pumping mode was specified during connection.
