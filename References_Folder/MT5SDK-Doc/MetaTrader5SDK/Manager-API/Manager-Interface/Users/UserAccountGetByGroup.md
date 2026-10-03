[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Users](../Users.md) / UserAccountGetByGroup

[Previous](UserAccountGet.md) | [Next](UserAccountGetByLogins.md)

# IMTManagerAPI::UserAccountGetByGroup

Get trading accounts for one or several groups.

C++
    
    
    MTAPIRES  IMTManagerAPI::UserAccountGetByGroup(
       LPCWSTR          mask,      // Groups
       IMTAccountArray* accounts   // Array of accounts
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.UserAccountGetByGroup(
       string           mask,      // Groups
       CIMTAccountArray accounts   // Array of accounts
       )

Python
    
    
    ManagerAPI.UserAccountGetByGroup(
       str              mask          # Groups
       )

### Parameters

**mask**  
[in] Groups for which accounts are requested. You can specify one group, several groups (comma separated) or a group mask. The mask is specified using characters "*" (any value) and "!" (exception). For example: "demo*,!demoforex" indicates all groups with the names beginning with 'demo', except for the group demoforex.

**accounts**  
[out] Array of trading accounts. The 'accounts' object must first be created using theIMTManagerAPI::UserCreateAccountArraymethod.

### Return Value

An indication of a successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The method only works if the [pumping modes](../Connection-to-the-Server/Pumping-Modes.md) PUMP_MODE_USERS, PUMP_MODE_ORDERS and PUMP_MODE_POSITIONS were specified when connecting.
