[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Positions](../Positions.md) / PositionDeleteByTicket

[Previous](PositionDelete.md) | [Next](PositionDeleteBatch.md)

# IMTAdminAPI::PositionDeleteByTicket

Delete a position by ticket.

C++
    
    
    MTAPIRES  IMTAdminAPI::PositionDeleteByTicket(
       UINT64        ticket        // Position object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.PositionDeleteByTicket(
       ulong         ticket        // Position object
       )

Python
    
    
    AdminAPI.PositionDeleteByTicket(
       ticket        # Position object
       )

### Parameters

**ticket**  
[in] The ticket of the position you want to delete.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

A position can only be deleted from the applications connected to the trade server, on which the position has been created. For all other applications, the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) is returned. If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) is returned.
