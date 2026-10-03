[🏠 Document Start](../../../../README.md) / [Server API](../../../README.md) / [Main API Interface](../../../Main-API-Interface.md) / [Trade](../../Trade.md) / [Orders](../Orders.md) / HistoryDelete

[Previous](HistoryUpdateBatchArray.md) | [Next](HistoryDeleteBatch.md)

# IMTServerAPI::HistoryDelete

Delete a closed trade order from the server data base.
    
    
    MTAPIRES  IMTServerAPI::HistoryDelete(
       const UINT64  ticket      // The ticket of an order
       )

### Parameters

**ticket**  
[in] The number (ticket) of an order.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

An order can be deleted only from the plugins that run on the same trade server where the order was created. For all other plugins the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) will be returned. If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) will be returned.
