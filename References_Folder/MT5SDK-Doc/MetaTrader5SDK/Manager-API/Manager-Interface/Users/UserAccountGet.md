[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Users](../Users.md) / UserAccountGet

[Previous](UserAccountUnsubscribe.md) | [Next](UserAccountGetByGroup.md)

# IMTManagerAPI::UserAccountGet

Get client trading account by a login.

C++
    
    
    MTAPIRES  IMTManagerAPI::UserAccountGet(
       const UINT64  login,       // Client login
       IMTAccount*   account      // An object of a trading account
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.UserAccountGet(
       ulong         login,       // Client login
       CIMTAccount   obj          // An object of a trading account
       )

Python
    
    
    ManagerAPI.UserAccountGet(
       login         # Client login
       )

### Parameters

**login**  
[in] The login of a client.

**account**  
[out] An object of a client trading account. The account object must be created using theIMTManagerAPI::UserCreateAccountmethod.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, a corresponding error code will be returned.

### Note

The method is valid only if the PUMP_MODE_USERS, PUMP_MODE_ORDERS and PUMP_MODE_POSITIONS [pumping modes](../Connection-to-the-Server/Pumping-Modes.md) were specified during connection.
