[🏠 Document Start](../../../../../README.md) / [Web API](../../../../README.md) / [Manager Interface (Rest API)](../../../../Manager-Interface-(Rest-API).md) / [.NET Implementation of Protocol](../../../NET-Implementation-of-Protocol.md) / [MT5WebAPI Class](../../MT5WebAPI-Class.md) / [Clients](../Clients.md) / UserLogins

[Previous](UserAccountGet.md) | [Next](../Orders.md)

# MT5WebAPI.UserLogins

Returns a list of logins of the clients who are included in the specified group.
    
    
    MTRetCode  MT5WebAPI.UserLogins(
       string         group,       // Group name
       out List<int>  logins       // A list of client logins
       )

### Parameters

**group**  
[in] The name of a group of users. The entire name of the group must be specified including the path. For example, demo\demoforex.

**logins**  
[out] A list of client logins.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### 
