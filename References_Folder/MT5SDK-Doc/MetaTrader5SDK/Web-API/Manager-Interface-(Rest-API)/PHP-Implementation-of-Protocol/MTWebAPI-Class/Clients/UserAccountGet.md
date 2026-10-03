[🏠 Document Start](../../../../../README.md) / [Web API](../../../../README.md) / [Manager Interface (Rest API)](../../../../Manager-Interface-(Rest-API).md) / [PHP Implementation of Protocol](../../../PHP-Implementation-of-Protocol.md) / [MTWebAPI Class](../../MTWebAPI-Class.md) / [Clients](../Clients.md) / UserAccountGet

[Previous](UserPasswordChange.md) | [Next](UserLogins.md)

# MTWebAPI::UserAccountGet

Get the status of a client's trade account.
    
    
    MTAPIRES  MTWebAPI::UserAccountGet(
       int        $login,        // Login
       MTAccount  &$account      // Trade account state
       )

### Parameters

**$login**  
[in] The login of a client.

**& $account**  
[out] The MTAccount structure that describes the state of a trading account. The structure parameters are described in section"Data Structure".

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The state of a trade account can be received only in case it has open orders or positions or a trade activity has been detected at the account after the last server restart.
