[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Orders](../Orders.md) / OrderAddBatch

[Previous](OrderAdd.md) | [Next](OrderAddBatchArray.md)

# IMTManagerAPI::OrderAddBatch

Add a batch of open orders to the server database.

C++
    
    
    MTAPIRES  IMTManagerAPI::OrderAddBatch(
       IMTOrderArray*     orders,     // Array of orders
       MTAPIRES*          results     // Array of results
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.OrderAddBatch(
       CIMTOrderArray     orders,     // Array of orders
       MTRetCode[]        res         // Array of results
       )

Python
    
    
    ManagerAPI.OrderAddBatch(
       orders             # Array of orders
       )

### Parameters

**orders**  
[in] A pointer to the array of ordersIMTOrderArray.

**results**  
[out] An array with the order addition results. The size of the 'results' array must not be less than that of 'orders'.

### Return Value

The [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code indicates that all the specified orders have been added. The [MT_RET_ERR_PARTIAL](../../../../Return-Codes/Common-errors.md) response code means that only some of the orders have been added. Analyze the 'results' array for more details on the execution results. The result of adding of each order from the 'orders' array is added to 'results'. The index of a result corresponds to the index of an order in the source array.

### Note

Orders can only be added to the database of the server, to which the application is connected.

The tickets of the orders you are adding ([IMTOrder::OrderSet](../../../../Database-Interfaces/Trade/Orders/IMTOrder/OrderSet.md)) must fall within the orders range on the trading server ([IMTConServerTrade::OrdersRange*](../../../../Configuration-Interfaces/Network/IMTConServerTrade/OrdersRangeAdd.md)), and they must be greater than the last used ticket. 

Note that the server allocates new tickets starting from the last used ticket in the range. For example, if you create an order with a ticket of 5000, the server will allocate for further orders the tickets 5001, 5002, etc. (even if tickets before 5000 are not busy).

If orders are added with a zero ticket, the server will assign the tickets automatically.

Orders being added are checked for integrity. The following fields must be filled:

The [IMTOrder::TimeDone](../../../../Database-Interfaces/Trade/Orders/IMTOrder/TimeDone.md) and [IMTOrder::TimeDoneMsc](../../../../Database-Interfaces/Trade/Orders/IMTOrder/TimeDoneMsc.md) fields must not be filled in the orders.

  * [IMTOrder::Login](../../../../Database-Interfaces/Trade/Orders/IMTOrder/Login.md) (an account with this login must exist on the server)
  * [IMTOrder::Symbol](../../../../Database-Interfaces/Trade/Orders/IMTOrder/Login.md)
  * [IMTOrder::Type](../../../../Database-Interfaces/Trade/Orders/IMTOrder/Type.md)


  * [IMTOrder::Digits](../../../../Database-Interfaces/Trade/Orders/IMTOrder/Digits.md)
  * [IMTOrder::DigitsCurrency](../../../../Database-Interfaces/Trade/Orders/IMTOrder/DigitsCurrency.md)
  * [IMTOrder::ContractSize](../../../../Database-Interfaces/Trade/Orders/IMTOrder/ContractSize.md)


  * [IMTOrder::VolumeInitial](../../../../Database-Interfaces/Trade/Orders/IMTOrder/VolumeInitial.md) (must be less than IMTOrder::VolumeCurrent)
  * [IMTOrder::VolumeCurrent](../../../../Database-Interfaces/Trade/Orders/IMTOrder/VolumeCurrent.md) (cannot be greater than IMTOrder::VolumeInitial)
  * [IMTOrder::PriceOrder](../../../../Database-Interfaces/Trade/Orders/IMTOrder/PriceOrder.md)
  * [IMTOrder::State](../../../../Database-Interfaces/Trade/Orders/IMTOrder/State.md) (the state must correspond to an open order; it cannot be ORDER_STATE_CANCELED, ORDER_STATE_PARTIAL, ORDER_STATE_FILLED, ORDER_STATE_REJECTED, ORDER_STATE_EXPIRED)
  * [IMTOrder::TimeSetupMsc](../../../../Database-Interfaces/Trade/Orders/IMTOrder/TimeSetupMsc.md)


