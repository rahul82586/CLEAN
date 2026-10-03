[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Trade](../../Trade.md) / [Orders](../Orders.md) / HistoryDeleteBatch

[Previous](HistoryDelete.md) | [Next](HistoryGet.md)

# IMTServerAPI::HistoryDeleteBatch

Deletes closed orders from a server database in bulk.
    
    
    MTAPIRES  IMTServerAPI::HistoryDeleteBatch(
       const UINT64*   tickets,       // An array of tickets
       const UINT      tickets_total, // The number of tickets in the array
       MTAPIRES*       results        // An array of results
       )

### Parameters

**tickets**  
[in] A pointer to an array of orders which you want to delete.

**tickets_total**  
[in] The number of tickets in the 'tickets' array.

**results**  
[out] An array with the result of the deletion of orders. The size of the 'results' array must be not less than that of 'tickets'.

### Return Value

The [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code means that all specified orders have been deleted. The [MT_RET_ERR_PARTIAL](../../../../Return-Codes/Common-errors.md) response code means that only some of the orders have been deleted. For details, you should analyze the 'results' array. The result of deletion of each order from the 'tickets' array is added to the 'results' array. The index of a result corresponds to the index of a ticket in the source array.

### Note

Deals can be deleted only from the plugins, which run on the same trade server where the deals were created. For all other plugins the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) will be returned. If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) will be returned.
