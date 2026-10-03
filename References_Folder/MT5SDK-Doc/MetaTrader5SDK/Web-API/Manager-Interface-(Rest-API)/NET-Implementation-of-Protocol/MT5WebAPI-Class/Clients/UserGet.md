[🏠 Document Start](../../../../../README.md) / [Web API](../../../../README.md) / [Manager Interface (Rest API)](../../../../Manager-Interface-(Rest-API).md) / [.NET Implementation of Protocol](../../../NET-Implementation-of-Protocol.md) / [MT5WebAPI Class](../../MT5WebAPI-Class.md) / [Clients](../Clients.md) / UserGet

[Previous](UserDelete.md) | [Next](UserPasswordCheck.md)

# MT5WebAPI.UserGet

Get information about a client by the login.
    
    
    MTAPIRES  MT5WebAPI.UserGet(
       ulong       login,    // Login
       out MTUser  user      // Client account
       )

### Parameters

**login**  
[in] The login of a client.

**user**  
[out] An object of a client account MTUser. The parameters of the client account are described in the"Data Structure"section.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

Information about a client that can be obtained depends on access permissions of a manager account that is used for connection of the Web client. If the "Access to personal data of accounts" permission is absent", [some of the fields are not filled (#private-info)](../../../../Getting-Started.md#private-info) in the server response.
