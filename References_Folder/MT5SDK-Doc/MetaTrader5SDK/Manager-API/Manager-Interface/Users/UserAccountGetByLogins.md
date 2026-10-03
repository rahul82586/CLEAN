[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Users](../Users.md) / UserAccountGetByLogins

[Previous](UserAccountGetByGroup.md) | [Next](UserAccountRequest.md)

# IMTManagerAPI::UserAccountGetByLogins

Get trading accounts for a list of logins.

C++
    
    
    MTAPIRES  IMTManagerAPI::UserAccountGetByLogins(
       const UINT64*    logins,       // Logins
       const UINT       logins_total, // Number of logins
       IMTAccountArray* accounts      // Array of accounts
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.UserAccountGetByLogins(
       ulong[]          logins,       // Logins
       CIMTAccountArray accounts      // Array of accounts
       )

Python
    
    
    ManagerAPI.UserAccountGetByLogins(
       str              logins_list   # Logins
       )

### Parameters

**logins**  
[in] Array of client logins.

**logins_total**  
[in] Number of logins in the 'logins' array.

**accounts**  
[out] Array of trading accounts. The 'accounts' object must first be created using theIMTManagerAPI::UserCreateAccountArraymethod.

### Return Value

An indication of a successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The method only works if the [pumping modes](../Connection-to-the-Server/Pumping-Modes.md) PUMP_MODE_USERS, PUMP_MODE_ORDERS and PUMP_MODE_POSITIONS were specified when connecting.
