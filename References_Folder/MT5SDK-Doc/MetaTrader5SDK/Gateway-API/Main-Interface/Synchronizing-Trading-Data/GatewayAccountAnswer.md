[🏠 Document Start](../../../README.md) / [Gateway API](../../README.md) / [Main Interface](../../Main-Interface.md) / [Synchronizing Trading Data](../Synchronizing-Trading-Data.md) / GatewayAccountAnswer

[Previous](../Synchronizing-Trading-Data.md) | [Next](GatewayAccountRequest.md)

# IMTGatewayAPI::GatewayAccountAnswer

The method is used to match client's MetaTrader 5 trading data (current pending orders, positions and balance) with an external trading system. After calling [IMTGatewaySink:HookGatewayAccountRequest](../../Event-Interface/HookGatewayAccountRequest.md) hook, a developer can transfer the state of positions, orders and client balance to MetaTrader 5 platform using this method. As a result of executing the method, the current pending orders, positions and client balance will match the passed data.

C++
    
    
    MTAPIRES  IMTGatewayAPI::GatewayAccountAnswer(
       const MTAPIRES          result,           // Result
       const INT64             accounts_time,    // State fixing time
       const IMTUser*          user             // An object of a client record
       const IMTAccount*       account          // An object of a trading account
       const IMTOrderArray*    orders           // Array of orders
       const IMTPositionArray* positions        // Positions array
       )

.NET
    
    
    MTRetCode  CIMTGatewayAPI.GatewayAccountAnswer(
       MTRetCode               result,           // Result
       long                    accounts_time,    // State fixing time
       CIMTUser                user              // An object of a client record
       CIMTAccount             account           // An object of a trading account
       CIMTOrderArray          orders            // Array of orders
       CIMTPositionArray       positions         // Positions array
       )

### Parameters

**result**  
[in] Code of the result of handling the client data request. MT_RET_OK response code is used if data has been successfully received. Otherwise, the appropriateerror codeis to be returned.

**accounts_time**  
[in] Time period, during which passed client trading status is actual. The date is specified in seconds since January 1, 1970.

**user**  
[in]An object of the client record.Loginfield is used in IMTUser object for identifying a user, for whom data synchronization is performed. The client external system's account number corresponding to the gateway can also be used for identification. Account in an external system can be defined usingIMTUser::ExternalAccountAddmethod.

**account**  
[in]Trading account object. OnlyBalancefield is used in IMTAccount object for passing the actual balance value.

**orders**  
[in]An object of the array of ordersplaced for the specified account. To avoid order synchronization, pass the NULL value.

**positions**  
[in]An object of the array of positionsplaced for the specified account. For a correct operation, the following fields ofIMTPositionobjects inside the array must be filled:

  * Symbol
  * Volume
  * ContractSize
  * Action
  * PriceOpen



### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

Correcting operations are created as a result of trading data synchronization. These operations are displayed in the client's trading history.

  * Balance: identification is based on the number of the client account in the external trading system, which corresponds to this gateway (it is set via [IMTUser::ExternalAccountAdd](../../../Database-Interfaces/Users/IMTUser/ExternalAccountAdd.md)). If the passed balance (the 'account' parameter) and the client's balance on the trade server do not match, a corrective balance deal is formed on the trade server. If the client's balance on the trade server is zero (when balance should be added), the deal type will be [IMTDeal::DEAL_BALANCE (#endealaction)](../../../Database-Interfaces/Trade/Deals/IMTDeal/Enumerations.md#endealaction). Otherwise the deal type is [IMTDeal::DEAL_CORRECTION (#endealaction)](../../../Database-Interfaces/Trade/Deals/IMTDeal/Enumerations.md#endealaction).
  * Orders: when the method is called, the equality of the list of passed orders (the 'orders' parameter) and the client's list of orders on the trade server is checked. The following details are checked: the order ID in an external trading system ([IMTOrder::ExternalID](../../../Database-Interfaces/Trade/Orders/IMTOrder/ExternalID.md)), the trading symbol ([IMTOrder::Symbol](../../../Database-Interfaces/Trade/Orders/IMTOrder/Symbol.md)), the order type ([IMTOrder::Type](../../../Database-Interfaces/Trade/Orders/IMTOrder/Type.md)), the current volume ([IMTOrder::VolumeCurrent](../../../Database-Interfaces/Trade/Orders/IMTOrder/VolumeCurrent.md)) and the order price ([IMTOrder::PriceOrder](../../../Database-Interfaces/Trade/Orders/IMTOrder/PriceOrder.md)). If the lists are equal, synchronization of orders is considered completed. If the lists do not match, orders existing on the trade server are canceled and an appropriate log is added to the server journal. After that new orders passed by the gateway are placed. The server tries to preserve the SL\TP values, if the external ID, trading symbol, direction and price of the order have not changed.
  * Positions: when the method is called, the equality of the list of passed positions (the 'positions' parameter) and the client's list of positions on the trade server is checked. The following details are checked: the position ID in an external trading system ([IMTPosition::ExternalID](../../../Database-Interfaces/Trade/Positions/IMTPosition/ExternalID.md)), the trading symbol ([IMTPosition::Symbol](../../../Database-Interfaces/Trade/Positions/IMTPosition/Symbol.md)), position direction ([IMTPosition::Action](../../../Database-Interfaces/Trade/Positions/IMTPosition/Action.md)), volume ([IMTPosition::VolumeCurrent](../../../Database-Interfaces/Trade/Positions/IMTPosition/Volume.md)), open price ([IMTPosition::PriceOpen](../../../Database-Interfaces/Trade/Positions/IMTPosition/PriceOpen.md)) and contract size ([IMTPosition::ContractSize](../../../Database-Interfaces/Trade/Positions/IMTPosition/ContractSize.md)). If the lists are equal, synchronization of positions is considered completed. If the lists do not match:


  * Positions, which exist on the trade server but are not found in the passed list, are closed with zero profit.
  * Positions, which do not exist on the trade server but are included in the passed list, are added to the client's account.
  * Positions with matching trading symbols existing in both lists are compared. If the direction, open price or contract size of a position has changed, the position on the trade server is closed and a new one received via the gateway is opened. If only the volume of a position has changed, the position on the trade server is corrected via an appropriate deal.


