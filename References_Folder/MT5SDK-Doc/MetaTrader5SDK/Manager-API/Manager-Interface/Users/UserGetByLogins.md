[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Users](../Users.md) / UserGetByLogins

[Previous](UserGetByGroup.md) | [Next](UserRequest.md)

# IMTManagerAPI::UserGetByLogins

Get accounts by the list of logins.

C++
    
    
    MTAPIRES  IMTManagerAPI::UserGetByLogins(
       const UINT64* logins,       // Logins
       const UINT    logins_total, // Number of logins
       IMTUserArray* users         // Array of accounts
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.UserGetByLogins(
       ulong[]       logins,       // Logins
       CIMTUserArray users         // Array of accounts
       )

Python
    
    
    ManagerAPI.UserGetByLogins(
       logins        # Logins
       )
    
    
    ManagerAPI.UserGetByLoginsCSV(
       logins,       # Logins
       fields        # Comma-separated list of required fields
       )
    
    
    ManagerAPI.UserGetByLoginsNumPy(
       logins,       # Logins
       fields        # Comma-separated list of required fields
       )

### Parameters

**logins**  
[in] Array of client logins.

**logins_total**  
[in] Number of logins in the 'logins' array.

**users**  
[out] An object of the accounts array. The 'users' object must be previously created using theIMTManagerAPI::UserCreateArraymethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The method only works if the [IMTManagerAPI::PUMP_MODE_USERS](../Connection-to-the-Server/Pumping-Modes.md) pumping mode was specified during connection.
