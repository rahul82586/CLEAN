[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Trade](../../Trade.md) / [Orders](../Orders.md) / OrderAdd

[Previous](OrderUnsubscribe.md) | [Next](OrderAddBatch.md)

# IMTServerAPI::OrderAdd

Adds an open order to the server database.
    
    
    MTAPIRES  IMTServerAPI::OrderAdd(
       IMTOrder*  order    // The order object
       )

### Parameters

**order**  
[in] Order object.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an appropriate error code is returned.

### Note

An order can only be added to the database of the server, on which the plugin is running.

  * [IMTOrder::Login](../../../../Database-Interfaces/Trade/Orders/IMTOrder/Login.md) (an account with this login must exist on the server)
  * [IMTOrder::Symbol](../../../../Database-Interfaces/Trade/Orders/IMTOrder/Login.md)
  * [IMTOrder::Type](../../../../Database-Interfaces/Trade/Orders/IMTOrder/Type.md)


  * [IMTOrder::Digits](../../../../Database-Interfaces/Trade/Orders/IMTOrder/Digits.md)
  * [IMTOrder::DigitsCurrency](../../../../Database-Interfaces/Trade/Orders/IMTOrder/DigitsCurrency.md)
  * [IMTOrder::ContractSize](../../../../Database-Interfaces/Trade/Orders/IMTOrder/ContractSize.md)


  * [IMTOrder::VolumeInitial](../../../../Database-Interfaces/Trade/Orders/IMTOrder/VolumeInitial.md) (must be less than IMTOrder::VolumeCurrent)
  * [IMTOrder::VolumeCurrent](../../../../Database-Interfaces/Trade/Orders/IMTOrder/VolumeCurrent.md) (cannot be greater than IMTOrder::VolumeInitial)
  * [IMTOrder::PriceOrder](../../../../Database-Interfaces/Trade/Orders/IMTOrder/PriceOrder.md)
  * [IMTOrder::State](../../../../Database-Interfaces/Trade/Orders/IMTOrder/State.md) (the state must correspond to an open order, it cannot be equal to ORDER_STATE_CANCELED, ORDER_STATE_PARTIAL, ORDER_STATE_FILLED, ORDER_STATE_REJECTED, ORDER_STATE_EXPIRED)
  * [IMTOrder::TimeSetupMsc](../../../../Database-Interfaces/Trade/Orders/IMTOrder/TimeSetupMsc.md)


