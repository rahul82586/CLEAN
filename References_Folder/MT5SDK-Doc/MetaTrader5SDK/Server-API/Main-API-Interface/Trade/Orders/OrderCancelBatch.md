[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Trade](../../Trade.md) / [Orders](../Orders.md) / OrderCancelBatch

[Previous](OrderCancel.md) | [Next](OrderGet.md)

# IMTServerAPI::OrderCancelBatch

Move multiple open order to history.
    
    
    MTAPIRES  IMTServerAPI::OrderCancelBatch(
       const UINT64*   tickets,       // array of tickets
       const UINT      tickets_total, // number of tickets in the array
       MTAPIRES*       results        // array of results
       )

### Parameters

**tickets**  
[in] A pointer to an array of order tickets which you want to move to history.

**tickets_total**  
[in] The number of tickets in the 'tickets' array.

**results**  
[out] An array with the order transferring result. The size of the 'results' array must not be less than that of 'tickets'.

### Return Value

The [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code indicates that all specified accounts have been moved to history. The [MT_RET_ERR_PARTIAL](../../../../Return-Codes/Common-errors.md) response code means that only some of the orders have been moved. Analyze the 'results' array for a detailed information on execution results. The result of transfer of each order from the 'tickets' array is added to 'results'. The result index corresponds to the ticket index in the source array.

### Note

When an order is transferred, its state changes to [IMTOrder::ORDER_STATE_CANCELED (#enorderstate)](../../../../Database-Interfaces/Trade/Orders/IMTOrder/Enumerations.md#enorderstate). Such orders are not executed or triggered, and no margin is charged for them.
