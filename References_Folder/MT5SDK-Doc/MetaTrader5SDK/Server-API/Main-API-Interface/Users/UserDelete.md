[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Users](../Users.md) / UserDelete

[Previous](UserAdd.md) | [Next](UserUpdate.md)

# IMTServerAPI::UserDelete

Delete a client record.
    
    
    MTAPIRES  IMTServerAPI::UserDelete(
       const UINT64  login      // Login
       )

### Parameters

**login**  
[in] The login of a client record.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

A client record can be deleted only from the plugins that run on the trade server where the record was created. For all other plugins the response code [MT_RET_ERR_NOTMAIN](../../../Return-Codes/API.md) will be returned. If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../Return-Codes/Common-errors.md) will be returned.
