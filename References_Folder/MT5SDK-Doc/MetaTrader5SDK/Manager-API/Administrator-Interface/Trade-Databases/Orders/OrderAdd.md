[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Orders](../Orders.md) / OrderAdd

[Previous](OrderRequestByTickets.md) | [Next](OrderAddBatch.md)

# IMTAdminAPI::OrderAdd

Add an open order the server database.

C++
    
    
    MTAPIRES  IMTAdminAPI::OrderAdd(
       IMTOrder*  order      // Order object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.OrderAdd(
       CIMTOrder  order      // Order object
       )

Python
    
    
    AdminAPI.OrderAdd(
       order      # Order object
       )

### Parameters

**order**  
[in] Order object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

An order can only be added to the database of the server, to which the application is connected.

  * [IMTOrder::Login](../../../../Database-Interfaces/Trade/Orders/IMTOrder/Login.md) (an account with this login must exist on the server)
  * [IMTOrder::Symbol](../../../../Database-Interfaces/Trade/Orders/IMTOrder/Login.md)
  * [IMTOrder::Type](../../../../Database-Interfaces/Trade/Orders/IMTOrder/Type.md)
  * [IMTOrder::Digits](../../../../Database-Interfaces/Trade/Orders/IMTOrder/Digits.md)
  * [IMTOrder::DigitsCurrency](../../../../Database-Interfaces/Trade/Orders/IMTOrder/DigitsCurrency.md)
  * [IMTOrder::ContractSize](../../../../Database-Interfaces/Trade/Orders/IMTOrder/ContractSize.md)
  * [IMTOrder::VolumeInitial](../../../../Database-Interfaces/Trade/Orders/IMTOrder/VolumeInitial.md) (must be less than IMTOrder::VolumeCurrent)
  * [IMTOrder::VolumeCurrent](../../../../Database-Interfaces/Trade/Orders/IMTOrder/VolumeCurrent.md) (must not be greater than IMTOrder::VolumeInitial)
  * [IMTOrder::PriceOrder](../../../../Database-Interfaces/Trade/Orders/IMTOrder/PriceOrder.md)
  * [IMTOrder::State](../../../../Database-Interfaces/Trade/Orders/IMTOrder/State.md) (the state must correspond to an open order; it cannot be ORDER_STATE_CANCELED, ORDER_STATE_PARTIAL, ORDER_STATE_FILLED, ORDER_STATE_REJECTED, ORDER_STATE_EXPIRED)
  * [IMTOrder::TimeSetupMsc](../../../../Database-Interfaces/Trade/Orders/IMTOrder/TimeSetupMsc.md)


