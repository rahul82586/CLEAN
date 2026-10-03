[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Trade](../../Trade.md) / [Orders](../Orders.md) / HistoryAddBatchArray

[Previous](HistoryAddBatch.md) | [Next](HistoryUpdate.md)

# IMTServerAPI::HistoryAddBatchArray

Adds closed orders to a server database in bulk.
    
    
    MTAPIRES  IMTServerAPI::HistoryAddBatchArray(
       IMTOrder**      orders,        // An array of orders
       const UINT      orders_total,  // The number of orders in the array
       MTAPIRES*       results        // An array of results
       )

### Parameters

**orders**  
[in] A pointer to the array of orders.

**ordes_total**  
[in] The number of orders in the 'orders' array.

**results**  
[out] An array with the results of adding of orders. The size of the 'results' array must be not less than that of 'orders'.

### Return value

The [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code indicates that all orders have been added. The [MT_RET_ERR_PARTIAL](../../../../Return-Codes/Common-errors.md) response code means that only some of orders have been added. Analyze the 'results' array for a detailed information on execution results. The result of adding of each order from the 'orders' array is added to 'results'. The index of a result corresponds to the index of an order in the source array.

### Note

Orders can only be added to the database of the server, on which the plugin is running.

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


