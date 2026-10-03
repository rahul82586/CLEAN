[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Users](../Users.md) / UserUpdate

[Previous](UserDelete.md) | [Next](UserTotal.md)

# IMTServerAPI::UserUpdate

Update a client record.
    
    
    MTAPIRES  IMTServerAPI::UserUpdate(
       IMTUser*  user      // An object of the client record
       )

### Parameters

**user**  
[in] An object of the client record.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

A client record can be updated only from the plugins that run on the trade server where the record was created. For all other plugins the response code [MT_RET_ERR_NOTMAIN](../../../Return-Codes/API.md) will be returned. If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../Return-Codes/Common-errors.md) will be returned.
