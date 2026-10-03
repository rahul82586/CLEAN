[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Trade](../../Trade.md) / [Orders](../Orders.md) / HistoryAdd

[Previous](HistoryUnsubscribe.md) | [Next](HistoryAddBatch.md)

# IMTServerAPI::HistoryAdd

Adds a closed order to the server database.
    
    
    MTAPIRES  IMTServerAPI::HistoryAdd(
       IMTOrder*  order    // The order object
       )

### Parameters

**order**  
[in] Order object.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an appropriate error code is returned.

### Note

An order can only be added to the database of the server, on which the plugin is running.

The ticket of the order being added ([IMTDeal::OrderSet](../../../../Database-Interfaces/Trade/Orders/IMTOrder/OrderSet.md)) must fall into the range of orders of the trading server ([IMTConServerTrade::OrdersRange*](../../../../Configuration-Interfaces/Network/IMTConServerTrade/OrdersRangeAdd.md)), and must be greater than the last used ticket. 

  * [IMTOrder::Login](../../../../Database-Interfaces/Trade/Orders/IMTOrder/Login.md) (an account with this login must exist on the server)
  * [IMTOrder::Symbol](../../../../Database-Interfaces/Trade/Orders/IMTOrder/Login.md)
  * [IMTOrder::Type](../../../../Database-Interfaces/Trade/Orders/IMTOrder/Type.md)


  * [IMTOrder::Digits](../../../../Database-Interfaces/Trade/Orders/IMTOrder/Digits.md)
  * [IMTOrder::DigitsCurrency](../../../../Database-Interfaces/Trade/Orders/IMTOrder/DigitsCurrency.md)
  * [IMTOrder::ContractSize](../../../../Database-Interfaces/Trade/Orders/IMTOrder/ContractSize.md)


  * [IMTOrder::VolumeInitial](../../../../Database-Interfaces/Trade/Orders/IMTOrder/VolumeInitial.md) (must be >= IMTOrder::VolumeCurrent)
  * [IMTOrder::VolumeCurrent](../../../../Database-Interfaces/Trade/Orders/IMTOrder/VolumeCurrent.md)
  * [IMTOrder::PriceOrder](../../../../Database-Interfaces/Trade/Orders/IMTOrder/PriceOrder.md)
  * [IMTOrder::State](../../../../Database-Interfaces/Trade/Orders/IMTOrder/State.md) (the state must correspond to a closed order: IMTOrder::ORDER_STATE_CANCELED, IMTOrder::ORDER_STATE_FILLED, IMTOrder::ORDER_STATE_EXPIRED or IMTOrder::ORDER_STATE_RECJECTED))


  * [IMTOrder::TimeSetup](../../../../Database-Interfaces/Trade/Orders/IMTOrder/TimeSetup.md) or [IMTOrder::TimeSetupMsc](../../../../Database-Interfaces/Trade/Orders/IMTOrder/TimeSetupMsc.md)
  * [IMTOrder::TimeDone](../../../../Database-Interfaces/Trade/Orders/IMTOrder/TimeDoneMsc.md) or [IMTOrder::TimeDoneMsc](../../../../Database-Interfaces/Trade/Orders/IMTOrder/TimeDoneMsc.md) (cannot be less than IMTOrder::TimeSetup/IMTOrder::TimeSetupMsc)


