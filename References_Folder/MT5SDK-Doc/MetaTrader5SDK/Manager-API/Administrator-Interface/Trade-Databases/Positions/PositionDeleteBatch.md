[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Positions](../Positions.md) / PositionDeleteBatch

[Previous](PositionDeleteByTicket.md) | [Next](PositionBackupList.md)

# IMTAdminAPI::PositionDeleteBatch

Delete positions from the server database in bulk.

C++
    
    
    MTAPIRES  IMTAdminAPI::PositionDeleteBatch(
       const UINT64*   tickets,       // Array of tickets
       const UINT      tickets_total, // Number of tickets in the array
       MTAPIRES*       results        // Array of results
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.PositionDeleteBatch(
       ulong[]         tickets,       // Array of tickets
       MTRetCode[]     retcodes       // Array of results
       )

Python
    
    
    AdminAPI.PositionDeleteBatch(
       tickets        // Array of tickets
       )

### Parameters

**tickets**  
[in] A pointer to an array of tickets of the position which you want to delete.

**tickets_total**  
[in] The number of tickets in the 'tickets' array.

**results**  
[out] The array with the position deletion results. The size of the 'results' array must not be less than that of 'tickets'.

### Return Value

The [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code indicates that all positions have been deleted. The [MT_RET_ERR_PARTIAL](../../../../Return-Codes/Common-errors.md) response code means that only some of the positions have been deleted. Analyze the 'results' array for more details concerning the execution results. The result of deletion of each position from the 'tickets' array is added to 'results'. The result index corresponds to the ticket index in the source array.

### Note

Positions can only be deleted from the applications connected to the trade server, on which the positions have been created. For all other applications, the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) is returned. If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) is returned.
