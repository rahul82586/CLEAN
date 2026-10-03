[🏠 Document Start](../../../README.md) / [Gateway API](../../README.md) / [Main Interface](../../Main-Interface.md) / [Synchronizing Trading Data](../Synchronizing-Trading-Data.md) / GatewayAccountSet

[Previous](GatewayAccountRequest.md) | [Next](../Mail-Database.md)

# IMTGatewayAPI::GatewayAccountSet

The method is used to match client's MetaTrader 5 trading data (current pending orders, positions and balance) with an external trading system. Using this method, a developer can transfer the state of positions, orders and client balance to MetaTrader 5 platform. As a result of executing the method, the current pending orders, positions and client balance will match the passed data.

C++
    
    
    MTAPIRES  IMTGatewayAPI::GatewayAccountSet(
       const INT64             request_id        // Request ID
       const IMTUser*          user              // An object of a client record
       const IMTAccount*       account           // An object of a trading account
       const IMTOrderArray*    orders            // Array of orders
       const IMTPositionArray* positions         // Positions array
       )

.NET
    
    
    MTRetCode  CIMTGatewayAPI.GatewayAccountSet(
       long                    request_id        // Request ID
       CIMTUser                user              // An object of a client record
       CIMTAccount             account           // An object of a trading account
       CIMTOrderArray          orders            // Positions array
       CIMTPositionArray       positions         // Positions array
       )

### Parameters

**request_id**  
[in] Arbitrary request ID. It is used for binding the requests executed by this method and the answers received viaIMTGatewayAPI::OnGatewayAccountSet.

**user**  
[in]An object of the client record. The client external system's account number corresponding to the gateway is used for identification of the user, for whom data synchronization is performed. Account in an external system can be defined usingIMTUser::ExternalAccountAddmethod.

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

Execution result, as well as the final status of a client entry are passed to [IMTGatewaySink::OnGatewayAccountSet](../../Event-Interface/OnGatewayAccountSet.md) handler.

If this condition is not met for any of the passed orders, synchronization stops with an error.

After that the system copies the orders which are not available in the current list (which were not found by ticket or ID).

  * [IMTOrder::Symbol](../../../Database-Interfaces/Trade/Orders/IMTOrder/Symbol.md)
  * [IMTOrder::VolumeInitial](../../../Database-Interfaces/Trade/Orders/IMTOrder/VolumeInitial.md)
  * [IMTOrder::VolumeCurrent](../../../Database-Interfaces/Trade/Orders/IMTOrder/VolumeCurrent.md) (must be less than or equal to [IMTOrder::VolumeInitial](../../../Database-Interfaces/Trade/Orders/IMTOrder/VolumeInitial.md))
  * [IMTOrder::PriceOrder](../../../Database-Interfaces/Trade/Orders/IMTOrder/PriceOrder.md) (must be non-zero)
  * [IMTOrder::State](../../../Database-Interfaces/Trade/Orders/IMTOrder/State.md) (must be ORDER_STATE_STARTED, ORDER_STATE_PLACED, ORDER_STATE_PARTIAL or ORDER_STATE_REQUEST_*)


  * [IMTOrder::Order](../../../Database-Interfaces/Trade/Orders/IMTOrder/Order.md)
  * [IMTOrder::ExternalID](../../../Database-Interfaces/Trade/Orders/IMTOrder/ExternalID.md)
  * [IMTOrder::Symbol](../../../Database-Interfaces/Trade/Orders/IMTOrder/Symbol.md)
  * [IMTOrder::Type](../../../Database-Interfaces/Trade/Orders/IMTOrder/Type.md)
  * [IMTOrder::VolumeCurrent](../../../Database-Interfaces/Trade/Orders/IMTOrder/VolumeCurrent.md)
  * [IMTOrder::PriceOrder](../../../Database-Interfaces/Trade/Orders/IMTOrder/PriceOrder.md)
  * [IMTOrder::State](../../../Database-Interfaces/Trade/Orders/IMTOrder/State.md) (if this field in the incoming order is different from ORDER_STATE_STARTED)


  * [IMTOrder::Order](../../../Database-Interfaces/Trade/Orders/IMTOrder/Order.md)
  * [IMTOrder::PriceTP](../../../Database-Interfaces/Trade/Orders/IMTOrder/PriceTP.md)
  * [IMTOrder::PriceSL](../../../Database-Interfaces/Trade/Orders/IMTOrder/PriceSL.md)
  * [IMTOrder::State](../../../Database-Interfaces/Trade/Orders/IMTOrder/State.md) (if this field in the incoming order is ORDER_STATE_STARTED)
  * [IMTOrder::ContractSize](../../../Database-Interfaces/Trade/Orders/IMTOrder/ContractSize.md)
  * [IMTOrder::Digits](../../../Database-Interfaces/Trade/Orders/IMTOrder/Digits.md)
  * [IMTOrder::DigitsCurrency](../../../Database-Interfaces/Trade/Orders/IMTOrder/DigitsCurrency.md)


  * Positions which exist on the trade server but are not found in the passed list, are closed with zero profit.
  * Positions which do not exist on the trade server but are included in the passed list, are added to the client's account.
  * Positions with matching trading symbols existing in both lists are compared. If the direction, open price or contract size of a position has changed, the position on the trade server is closed and a new one received via the gateway is opened. If only the volume of a position has changed, the position on the trade server is corrected via an appropriate deal.


