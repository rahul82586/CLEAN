[🏠 Document Start](../../../../../README.md) / [Web API](../../../../README.md) / [Manager Interface (Rest API)](../../../../Manager-Interface-(Rest-API).md) / [PHP Implementation of Protocol](../../../PHP-Implementation-of-Protocol.md) / [MTWebAPI Class](../../MTWebAPI-Class.md) / [Clients](../Clients.md) / UserDelete

[Previous](UserUpdate.md) | [Next](UserGet.md)

# MTWebAPI::UserDelete

Delete a client account on the server.
    
    
    MTAPIRES  MTWebAPI::UserDelete(
       int  $login      // Login
       )

### Parameters

**$login**  
[in] The login of an account to be deleted.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

  * A user account can be deleted only when connecting to the same trade server where the account is located. If an account with the specified login is not found, code [MT_RET_ERR_NOTFOUND](../../../../../Return-Codes/Common-errors.md) is returned.
  * Accounts that belong to manager and administrator groups cannot be deleted.


