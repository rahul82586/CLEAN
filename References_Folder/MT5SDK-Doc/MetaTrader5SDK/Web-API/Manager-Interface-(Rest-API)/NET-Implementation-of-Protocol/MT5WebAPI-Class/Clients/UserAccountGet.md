[🏠 Document Start](../../../../../README.md) / [Web API](../../../../README.md) / [Manager Interface (Rest API)](../../../../Manager-Interface-(Rest-API).md) / [.NET Implementation of Protocol](../../../NET-Implementation-of-Protocol.md) / [MT5WebAPI Class](../../MT5WebAPI-Class.md) / [Clients](../Clients.md) / UserAccountGet

[Previous](UserPasswordChange.md) | [Next](UserLogins.md)

# MT5WebAPI.UserAccountGet

Get the status of a client's trade account.
    
    
    MTRetCode  MT5WebAPI.UserAccountGet(
       ulong          login,       // Login
       out MTAccount  account      // Trade account status
       )

### Parameters

**login**  
[in] The login of a client.

**account**  
[out] The MTAccount structure that describes the state of a trading account. The structure parameters are described in the"Trade Account Parameters"section.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The state of a trade account can be received only in case it has open orders or positions or a trade activity has been detected at the account after the last server restart.
