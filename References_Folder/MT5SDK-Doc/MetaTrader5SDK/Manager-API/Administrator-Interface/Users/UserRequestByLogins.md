[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Users](../Users.md) / UserRequestByLogins

[Previous](UserRequestArray.md) | [Next](UserPasswordCheck.md)

# IMTAdminAPI::UserRequestByLogins

Request accounts from the server by a list of logins.

C++
    
    
    MTAPIRES  IMTAdminAPI::UserRequestByLogins(
       const UINT64* logins,       // logins
       const UINT    logins_total, // number of logins
       IMTUserArray* users         // array of accounts
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.UserRequestByLogins(
       ulong[]       logins,       // logins
       CIMTUserArray users         // array of accounts
       )

Python
    
    
    AdminAPI.UserRequestByLogins(
       login-list    # logins
       )
    
    
    AdminAPI.UserRequestByLoginsCSV(
       login-list,    # logins
       fields         # comma-separated list of required fields
       )
    
    
    AdminAPI.UserRequestByLoginsNumPy(
       login-list,    # logins
       fields         # comma-separated list of required fields
       )

### Parameters

**logins**  
[in] Array of client logins.

**logins_total**  
[in] Number of logins in the 'logins' array.

**users**  
[out] An object of the accounts array. The 'users' object must be previously created using theIMTAdminAPI::UserCreateArraymethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The method cannot be called from event handlers (any IMT*Sink class methods).
