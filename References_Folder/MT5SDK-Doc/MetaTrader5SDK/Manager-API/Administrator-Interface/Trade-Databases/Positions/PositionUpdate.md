[🏠 Document Start](../../../../README.md) / [Manager API](../../../README.md) / [Administrator Interface](../../../Administrator-Interface.md) / [Trade Databases](../../Trade-Databases.md) / [Positions](../Positions.md) / PositionUpdate

[Previous](PositionRequestByTickets.md) | [Next](PositionUpdateBatch.md)

# IMTAdminAPI::PositionUpdate

Update a position.

C++
    
    
    MTAPIRES  IMTAdminAPI::PositionUpdate(
       IMTPosition*  position      // Position object
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.PositionUpdate(
       CIMTPosition  position      // Position object
       )

Python
    
    
    AdminAPI.PositionUpdate(
       position      # Position object
       )

### Parameters

**position**  
[in] An object of a trade position.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

A position can only be updated from the applications connected to the trade server, on which the position has been created. For all other applications the response code [MT_RET_ERR_NOTMAIN](../../../../Return-Codes/API.md) will be returned. If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../../Return-Codes/Common-errors.md) will be returned.
