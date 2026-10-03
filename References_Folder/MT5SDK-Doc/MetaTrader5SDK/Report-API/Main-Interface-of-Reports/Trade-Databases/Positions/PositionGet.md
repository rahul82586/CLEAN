[🏠 Document Start](../../../../README.md) / [Report API](../../../README.md) / [Main Interface of Reports](../../../Main-Interface-of-Reports.md) / [Trade Databases](../../Trade-Databases.md) / [Positions](../Positions.md) / PositionGet

[Previous](PositionCreateArray.md) | [Next](PositionGetByTicket.md)

# IMTReportAPI::PositionGet

Get a trade position.
    
    
    MTAPIRES  IMTReportAPI::PositionGet(
       const UINT64  login,        // User's login
       LPCWSTR       symbol,       // Symbol
       IMTPosition*  position      // Position object
       )

### Parameters

**login**  
[in] The login of a user whose position should be deleted.

**symbol**  
[in] The symbol, for which you need to get a position.

**position**  
[out] An object of a trade position. The position object must be first created using theIMTReportAPI::PositionCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies the data of a position of specified client and the specified symbol to the position object.

To get a position when using the hedging accounting system ([EnMarginMode::MARGIN_MODE_RETAIL_HEDGED (#enmarginmode)](../../../../Configuration-Interfaces/Groups/IMTConGroup/Enumerations.md#enmarginmode)), use the [IMTReportAPI::PositionGetByTicket](PositionGetByTicket.md) method as a position in that case is identified by the ticket, not by the login and symbol.

# IMTReportAPI::PositionGet

Get an array of positions by the login.
    
    
    MTAPIRES  IMTReportAPI::PositionGet(
       const UINT64       login,        // User's login
       IMTPositionArray*  position      // An object of the array of positions
       )

### Parameters

**login**  
[in] The login of a user.

**position**  
[out] An object of the array of trade positions. The position object must be first created using theIMTReportAPI::PositionArrayCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies the array of positions of a client with the specified login to the position object.
