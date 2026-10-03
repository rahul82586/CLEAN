[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Online Connections](../Online-Connections.md) / OnlineDisconnect

[Previous](OnlineGet.md) | [Next](OnlineDisconnectBatch.md)

# IMTServerAPI::OnlineDisconnect

Forced disconnection of a client from the server.
    
    
    MTAPIRES  IMTServerAPI::OnlineDisconnect(
       IMTOnline*     online      // Connection record object
       )

### Parameters

**online**  
[out] Connection record object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

Forced disconnection is required to ensure that new account settings are activated. For example, after account password change, you can disconnect this account from the server so that the user logs in with the new password.
