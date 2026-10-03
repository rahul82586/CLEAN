[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Positions](../Positions.md) / PositionDelete

[Previous](PositionUpdateBatchArray.md) | [Next](PositionDeleteByTicket.md)

# IMTAdminAPI::PositionDelete

Deletes a position.

C++
    
    
    MTAPIRES  IMTAdminAPI::PositionDelete(
       IMTPosition*  position      // Position object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.PositionDelete(
       CIMTPosition  position      // Position object
       )

Python
    
    
    AdminAPI.PositionDelete(
       position      # Position object
       )

### Parameters

**position**  
[in] The object of the position that you want to delete.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

A position can only be deleted from the applications connected to the trade server, on which the position has been created. For all other applications the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) will be returned. If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) will be returned.
