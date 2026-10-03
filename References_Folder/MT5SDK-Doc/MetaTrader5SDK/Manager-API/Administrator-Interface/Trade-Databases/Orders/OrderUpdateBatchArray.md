[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Orders](../Orders.md) / OrderUpdateBatchArray

[Previous](OrderUpdateBatch.md) | [Next](OrderDelete.md)

# IMTManagerAPI::OrderUpdateBatchArray

Update multiple open orders in a server database.

C++
    
    
    MTAPIRES  IMTManagerAPI::OrderUpdateBatchArray(
       IMTOrder**      order,           // Array of orders
       const UINT      orders_total,    // Number of orders in the array
       MTAPIRES*       results          // Array of results
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.OrderUpdateBatchArray(
       CIMTOrder[]     orders,          // Array of orders
       MTRetCode[]     retcodes         // Array of results
       )

### Parameters

**orders**  
[in] A pointer to the array of orders.

**orders_total**  
[in] The number of orders in the 'orders' array.

**results**  
[out] An array with order update results. The size of the 'results' array must not be less than that of 'orders'.

### Return Value

The [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code indicates that all orders have been updated. The [MT_RET_ERR_PARTIAL](../../../../Return-Codes/Common-errors.md) response code means that only some of the orders have been updated. Analyze the 'results' array for more details concerning the execution results. The result of update of each order from the 'orders' array is added to 'results'. The index of a result corresponds to the index of an order in the source array.

### Note

Orders can only be updated from the applications connected to the trade server, on which the orders have been created. For all other applications, the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) is returned. If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) is returned.

  * [IMTOrder::Login](../../../../Database-Interfaces/Trade/Orders/IMTOrder/Login.md)
  * [IMTOrder::Symbol](../../../../Database-Interfaces/Trade/Orders/IMTOrder/Login.md)
  * [IMTOrder::Type](../../../../Database-Interfaces/Trade/Orders/IMTOrder/Type.md)


  * [IMTOrder::Digits](../../../../Database-Interfaces/Trade/Orders/IMTOrder/Digits.md)
  * [IMTOrder::DigitsCurrency](../../../../Database-Interfaces/Trade/Orders/IMTOrder/DigitsCurrency.md)
  * [IMTOrder::ContractSize](../../../../Database-Interfaces/Trade/Orders/IMTOrder/ContractSize.md)


  * [IMTOrder::VolumeInitial](../../../../Database-Interfaces/Trade/Orders/IMTOrder/VolumeInitial.md)
  * [IMTOrder::VolumeCurrent](../../../../Database-Interfaces/Trade/Orders/IMTOrder/VolumeCurrent.md)
  * [IMTOrder::PriceOrder](../../../../Database-Interfaces/Trade/Orders/IMTOrder/PriceOrder.md)
  * [IMTOrder::State](../../../../Database-Interfaces/Trade/Orders/IMTOrder/State.md)
  * [IMTOrder::TimeSetupMsc](../../../../Database-Interfaces/Trade/Orders/IMTOrder/TimeSetupMsc.md)
  * [IMTOrder::TimeDone](../../../../Database-Interfaces/Trade/Orders/IMTOrder/TimeDone.md) or [IMTOrder::TimeDoneMsc](../../../../Database-Interfaces/Trade/Orders/IMTOrder/TimeDoneMsc.md) (for closed orders)


