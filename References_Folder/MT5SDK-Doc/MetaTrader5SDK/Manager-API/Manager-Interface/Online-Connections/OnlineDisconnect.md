[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Online Connections](../Online-Connections.md) / OnlineDisconnect

[Previous](OnlineGet.md) | [Next](OnlineDisconnectBatch.md)

# IMTManagerAPI::OnlineDisconnect

Forced disconnection of a client from the server.

C++
    
    
    MTAPIRES  IMTManagerAPI::OnlineDisconnect(
       IMTOnline*     online      // Connection record object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.OnlineDisconnect(
       CIMTOnline     online      // Connection record object
       )

Python
    
    
    ManagerAPI.OnlineDisconnect(
       online         # Connection record object
       )

### Parameters

**online**  
[out] Connection record object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

Forced disconnection is required to ensure that new account settings are activated. For example, after account password change, you can disconnect this account from the server so that the user logs in with the new password.

After the connection is dropped, the client terminals attempt to reconnect to the server automatically.

The method only works if the [pumping modes](../Connection-to-the-Server/Pumping-Modes.md) PUMP_MODE_USERS and PUMP_MODE_ACTIVITY are enabled.
