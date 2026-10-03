[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Manager Interface](../../../Manager-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Deals](../Deals.md) / DealDeleteBatch

[Previous](DealDelete.md) | [Next](DealPerform.md)

# IMTManagerAPI::DealDeleteBatch

Delete deals from the server database in bulk.

C++
    
    
    MTAPIRES  IMTManagerAPI::DealDeleteBatch(
       const UINT64*   tickets,       // Array of tickets
       const UINT      tickets_total, // Number of tickets in the array
       MTAPIRES*       results        // Array of results
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.DealDeleteBatch(
       ulong[]         tickets,       // Deal ticket
       MTRetCode[]     res            // Array of results
       )

Python
    
    
    ManagerAPI.DealDeleteBatch(
       tickets         # Deal ticket
       )

### Parameters

**tickets**  
[in] A pointer to an array of tickets of the deal which you want to delete.

**tickets_total**  
[in] The number of tickets in the 'tickets' array.

**results**  
[out] The array with the deal deletion results. The size of the 'results' array must not be less than that of 'tickets'.

### Return Value

The [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code means that all the specified deals were deleted. The [MT_RET_ERR_PARTIAL](../../../../Return-Codes/Common-errors.md) response code means that only some of the deals have been deleted. Analyze the 'results' array for more details concerning the execution results. The result of deletion of each deal from the 'tickets' array is added to 'results'. The result index corresponds to the ticket index in the source array.

### Note

A deal can only be deleted from the applications connected to the trade server, on which the deals have been created. For all other applications, the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) is returned. If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) is returned.
