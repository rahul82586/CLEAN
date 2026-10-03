[🏠 Document Start](../../../../../README.md) / [Web API](../../../../README.md) / [Manager Interface (Rest API)](../../../../Manager-Interface-(Rest-API).md) / [PHP Implementation of Protocol](../../../PHP-Implementation-of-Protocol.md) / [MTWebAPI Class](../../MTWebAPI-Class.md) / [Clients](../Clients.md) / UserLogins

[Previous](UserAccountGet.md) | [Next](../Orders.md)

# MTWebAPI::UserLogins

Returns an array of logins of the clients who are included in the specified group.
    
    
    MTAPIRES  MTWebAPI::UserLogins(
       string        $group,       // Group name
       array(int)    &$logins      // An array of client logins
       )

### Parameters

**group**  
[in] The name of a group of users. The entire name of the group must be specified including the path. For example, demo\demoforex.

**logins**  
[out] An array of client logins.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### 
