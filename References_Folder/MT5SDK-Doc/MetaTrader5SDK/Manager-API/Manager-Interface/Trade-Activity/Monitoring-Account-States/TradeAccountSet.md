[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Trade Activity](../../Trade-Activity.md) / [Monitoring Account States](../Monitoring-Account-States.md) / TradeAccountSet

[Previous](../Monitoring-Account-States.md) | [Next](../../Market-Depth.md)

# IMTManagerAPI::TradeAccountSet

The method is used to match client's MetaTrader 5 trading data (current pending orders, positions and balance) with an external trading system. Using this method, a developer can transfer the state of positions, orders and client balance to MetaTrader 5 platform. As a result of executing the method, the current pending orders, positions and client balance will match the passed data.

C++
    
    
    MTAPIRES  IMTManagerAPI::TradeAccountSet(
       const INT64             request_id,      // Request ID
       const IMTUser*          user,            // An object of a client record
       const IMTAccount*       account,         // An object of a trading account
       const IMTOrderArray*    orders,          // Orders array
       const IMTPositionArray* positions        // Positions array
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.TradeAccountSet(
       long                    request_id,       // Request ID
       CIMTUser                user,             // An object of a client record
       CIMTAccount             account,          // An object of a trading account
       CIMTOrderArray          orders,           // Orders array
       CIMTPositionArray       positions         // Positions array
       )

Python
    
    
    ManagerAPI.TradeAccountSet(
       request_id,             # Request ID
       user,                   # An object of a client record
       account,                # An object of a trading account
       orders,                 # Orders array
       positions               # Positions array
       )

### Parameters

**request_id**  
[in] Arbitrary request ID. It is used for binding the requests executed by this method and the answers received viaIMTManagerSink::OnTradeAccountSet.

**user**  
[in]An object of the client record. The Login field is used for identification of the user, for whom data synchronization is performed. If that feild is not filled, the client's account number in an external system is used. Account in an external system can be defined usingIMTUser::ExternalAccountAddmethod.

**account**  
[in]Trading account object. OnlyBalancefield is used in IMTAccount object for passing the actual balance value.

**orders**  
[in]An object of the array of ordersplaced for the specified account. To avoid order synchronization, pass the NULL value.

**positions**  
[in]An object of the array of positionsplaced for the specified account. To avoid position synchronization, pass the NULL value.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

Correcting operations are created as a result of trading data synchronization. These operations are displayed in the client's trading history.

If this condition is not met for any of the passed orders, synchronization stops with an error.

After that the system copies the orders which are not available in the current list (which were not found by ticket or ID).

  * [IMTOrder::Symbol](../../../../Database-Interfaces/Trade/Orders/IMTOrder/Symbol.md)
  * [IMTOrder::VolumeInitial](../../../../Database-Interfaces/Trade/Orders/IMTOrder/VolumeInitial.md)
  * [IMTOrder::VolumeCurrent](../../../../Database-Interfaces/Trade/Orders/IMTOrder/VolumeCurrent.md) (must be less than or equal to [IMTOrder::VolumeInitial](../../../../Database-Interfaces/Trade/Orders/IMTOrder/VolumeInitial.md))
  * [IMTOrder::PriceOrder](../../../../Database-Interfaces/Trade/Orders/IMTOrder/PriceOrder.md) (must be non-zero)
  * [IMTOrder::State](../../../../Database-Interfaces/Trade/Orders/IMTOrder/State.md) (must be ORDER_STATE_STARTED, ORDER_STATE_PLACED, ORDER_STATE_PARTIAL or ORDER_STATE_REQUEST_*)


  * [IMTOrder::Order](../../../../Database-Interfaces/Trade/Orders/IMTOrder/Order.md)
  * [IMTOrder::ExternalID](../../../../Database-Interfaces/Trade/Orders/IMTOrder/ExternalID.md)
  * [IMTOrder::Symbol](../../../../Database-Interfaces/Trade/Orders/IMTOrder/Symbol.md)
  * [IMTOrder::Type](../../../../Database-Interfaces/Trade/Orders/IMTOrder/Type.md)
  * [IMTOrder::VolumeCurrent](../../../../Database-Interfaces/Trade/Orders/IMTOrder/VolumeCurrent.md)
  * [IMTOrder::PriceOrder](../../../../Database-Interfaces/Trade/Orders/IMTOrder/PriceOrder.md)
  * [IMTOrder::State](../../../../Database-Interfaces/Trade/Orders/IMTOrder/State.md) (if this field in the incoming order is different from ORDER_STATE_STARTED)


  * [IMTOrder::Order](../../../../Database-Interfaces/Trade/Orders/IMTOrder/Order.md)
  * [IMTOrder::PriceTP](../../../../Database-Interfaces/Trade/Orders/IMTOrder/PriceTP.md)
  * [IMTOrder::PriceSL](../../../../Database-Interfaces/Trade/Orders/IMTOrder/PriceSL.md)
  * [IMTOrder::State](../../../../Database-Interfaces/Trade/Orders/IMTOrder/State.md) (if this field in the incoming order is ORDER_STATE_STARTED)
  * [IMTOrder::ContractSize](../../../../Database-Interfaces/Trade/Orders/IMTOrder/ContractSize.md)
  * [IMTOrder::Digits](../../../../Database-Interfaces/Trade/Orders/IMTOrder/Digits.md)
  * [IMTOrder::DigitsCurrency](../../../../Database-Interfaces/Trade/Orders/IMTOrder/DigitsCurrency.md)


  * Positions which exist on the trade server but are not found in the passed list, are closed with zero profit.
  * Positions which do not exist on the trade server but are included in the passed list, are added to the client's account.
  * Positions with matching trading symbols existing in both lists are compared. If the direction, open price or contract size of a position has changed, the position on the trade server is closed and a new one received via the gateway is opened. If only the volume of a position has changed, the position on the trade server is corrected via an appropriate deal.


