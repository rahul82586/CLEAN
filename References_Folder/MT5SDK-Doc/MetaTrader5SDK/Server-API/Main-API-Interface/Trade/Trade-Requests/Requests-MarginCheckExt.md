[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Trade](../../Trade.md) / [Trade Requests](../Requests.md) / Requests MarginCheckExt

[Previous](Requests-MarginCheck.md) | [Next](Requests-BalanceCheck.md)

# IMTServerAPI::TradeMarginCheckExt

Checks the availability of the margin required for the execution of this order with the indication of increased accuracy volume.
    
    
    MTAPIRES  IMTServerAPI::TradeMarginCheckExt(
       const UINT64  login,                    // Login
       LPCWSTR       symbol,                   // Symbol name
       const UINT    type,                     // Order type
       const UINT64  volume,                   // Volume
       const double  price,                    // Price
       IMTAccount*   account_new=NULL,         // New account state
       IMTAccount*   account_current=NULL      // Current account state
       )

### Program Parameters

**login**  
[in] The login of the client for whom the order is executed.

**symbol**  
[in] The name of the trading instrument, for which the order is executed.

**type**  
[in] Type of trade order passed using theIMTOrder::EnOrderTypeenumeration.

**volume**  
[in] Trading order volume in the UINT64 format (one unit corresponds to 1/100000000 lot, for example, 105000000 means 1.05 lots). The final order size is calculated based on the currentcontract sizefor the specified trading instrument.

**price**  
[in] Price of the trade order execution.

**account_new=NULL**  
[out] An object of the trading state of a client account. If account_new is not NULL, it is filled with the state of the client's trading account after the execution of a trade order with the specified parameters. The account_new object must be created in advance using theIMTServerAPI::UserCreateAccountmethod.

**account_current=NULL**  
[out] An object of the trading state of a client account. If account_current is not NULL, it is filled with state of the client's trading account before the execution of a trade orders with the specified parameters (i.e., the account state at the time of the call of TradeMarginCheck). The account_current object must be created in advanceIMTServerAPI::UserCreateAccount.

### Return Value

An indication of the availability of the required margin is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The check is performed taking into account the current state of the [client account](../../../../Database-Interfaces/Trade/Accounts/IMTAccount.md) (balance, credit, floating profit, open orders and positions, etc.) and using the current market prices for the [group](../../../../Configuration-Interfaces/Groups.md) of the client.
