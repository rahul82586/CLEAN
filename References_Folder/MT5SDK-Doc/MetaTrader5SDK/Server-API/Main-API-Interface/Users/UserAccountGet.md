[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Users](../Users.md) / UserAccountGet

[Previous](NotificationsSend.md) | [Next](../Online-Connections.md)

# IMTServerAPI::UserAccountGet

Get client trading account by a login.
    
    
    MTAPIRES  IMTServerAPI::UserAccountGet(
       const UINT64  login,       // Client login
       IMTAccount*   account      // An object of a trading account
       )

### Parameters

**login**  
[in] The login of a client.

**account**  
[out] An object of a client trading account. The account object must be created using theIMTServerAPI::UserCreateAccountmethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, a corresponding error code will be returned.

### Note

The state of a trade account can be received only in case it has open orders or positions or a trade activity has been detected at the account after the last server restart.
