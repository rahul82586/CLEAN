[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Trade Activity](../../Trade-Activity.md) / [Auxiliary Functions](../Auxiliary-Functions.md) / TradeMarginCheck

[Previous](TradeRateSell.md) | [Next](TradeMarginCheckExt.md)

# IMTManagerAPI::TradeMarginCheck

Checks the availability of the margin required for the execution of this order.

C++
    
    
    MTAPIRES  IMTManagerAPI::TradeMarginCheck(
       const UINT64  login,                    // Login
       LPCWSTR       symbol,                   // Symbol name
       const UINT    type,                     // Type of order
       const UINT64  volume,                   // Volume
       const double  price,                    // Price
       IMTAccount*   account_new=NULL,         // New state of account
       IMTAccount*   account_current=NULL      // Current state of account
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.TradeMarginCheck(
       ulong                  login,               // Login
       string                 symbol,              // Symbol name
       CIMTOrder.EnOrderType  type,                // Type of order
       ulong                  volume,              // Volume
       double                 price,               // Price
       CIMTAccount            account_new=NULL,    // New state of account
       CIMTAccount            account_current=NULL // Current state of account
       )

Python
    
    
    ManagerAPI.TradeMarginCheck(
       login,                 # Login
       symbol,                # Symbol name
       type,                  # Type of order
       volume,                # Volume
       price                  # Price
       )

### Parameters

**login**  
[in] The login of the client for whom the order is executed.

**symbol**  
[in] The name of the trading instrument, for which the order is executed.

**type**  
[in] Type of trade order passed using theIMTOrder::EnOrderTypeenumeration.

**volume**  
[in] The volume of a trade order in the UINT64 format (one unit corresponds to 1/10000 lot, for example, 10500 means 1.05 lots). The final order size is calculated based on the currentcontract sizefor the specified trading instrument.

**price**  
[in] Price of the trade order execution.

**account_new=NULL**  
[out] An object of the trading state of a client account. If account_new is not NULL, it is filled with the state of the client's trading account after the execution of a trade order with the specified parameters. The account_new object must be first created using theIMTManagerAPI::UserCreateAccountmethod.

**account_current=NULL**  
[out] An object of the trading state of a client account. If account_current is not NULL, it is filled with state of the client's trading account before the execution of a trade orders with the specified parameters (i.e., the account state at the time of the call of TradeMarginCheck). The account_current object must be first created using theIMTManagerAPI::UserCreateAccountmethod.

### Return Value

An indication of the availability of the required margin is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The check is performed taking into account the current state of the [client account](../../../../Database-Interfaces/Trade/Accounts/IMTAccount.md) (balance, credit, floating profit, open orders and positions, etc.) and the current market prices for the [group](../../../../Configuration-Interfaces/Groups.md) of the client.

# IMTManagerAPI::TradeMarginCheck

Checks the availability of the margin required for the execution of this order.

C++
    
    
    MTAPIRES  IMTManagerAPI::TradeMarginCheck(
       const IMTOrder*  order,                    // An object of a trade order
       IMTAccount*      account_new=NULL,         // New state of account
       IMTAccount*      account_current=NULL      // Current state of account
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.TradeMarginCheck(
       CIMTOrder        order,                    // An object of a trade order
       CIMTAccount      account_new=NULL,         // New state of account
       CIMTAccount      account_current=NULL      // Current state of account
       )

### Parameters

**order**  
[in] An object of a trading order.

**account_new=NULL**  
[out] An object of the trading state of a client account. If account_new is not NULL, it is filled with the state of the client's trading account after the execution of a trade order with the specified parameters. The account_new object must be first created using theIMTManagerAPI::UserCreateAccountmethod.

**account_current=NULL**  
[out] An object of the trading state of a client account. If account_current is not NULL, it is filled with state of the client's trading account before the execution of a trade orders with the specified parameters (i.e., the account state at the time of the call of TradeMarginCheck). The account_current object must be first created using theIMTManagerAPI::UserCreateAccountmethod.

### Return Value

An indication of the availability of the required margin is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The check is performed taking into account the current state of the [client account](../../../../Database-Interfaces/Trade/Accounts/IMTAccount.md) (balance, credit, floating profit, open orders and positions, etc.) and the current market prices for the group of the client.
