[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Orders](../Orders.md) / OrderDeleteBatch

[Previous](OrderDelete.md) | [Next](OrderCancel.md)

# IMTManagerAPI::OrderDeleteBatch

Delete orders from the server database in bulk.

C++
    
    
    MTAPIRES  IMTManagerAPI::OrderDeleteBatch(
       const UINT64*   tickets,       // Array of tickets
       const UINT      tickets_total, // Number of tickets in the array
       MTAPIRES*       results        // Array of results
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.OrderDeleteBatch(
       ulong[]         tickets,       // Deal ticket
       MTRetCode[]     retcodes       // Array of results
       )

Python
    
    
    ManagerAPI.OrderDeleteBatch(
       tickets         # Deal ticket
       )

### Parameters

**tickets**  
[in] A pointer to an array of tickets of the orders which you want to delete.

**tickets_total**  
[in] The number of tickets in the 'tickets' array.

**results**  
[out] The array with the order deletion results. The size of the 'results' array must not be less than that of 'tickets'.

### Return Value

The [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code indicates that all orders have been deleted. The [MT_RET_ERR_PARTIAL](../../../../Return-Codes/Common-errors.md) response code means that only some of the orders have been deleted. Analyze the 'results' array for more details concerning the execution results. The result of deletion of each order from the 'tickets' array is added to 'results'. The result index corresponds to the ticket index in the source array.

### Note

Orders can only be deleted from the applications connected to the trade server, on which the orders have been created. For all other applications, the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) is returned. If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) is returned.
