[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Users](../Users.md) / UserAccountRequestByLogins

[Previous](UserAccountRequest.md) | [Next](UserAccountRequestArray.md)

# IMTManagerAPI::UserAccountRequestByLogins

Request accounts' trading statuses from the server by a list of logins.

C++
    
    
    virtual MTAPIRES  IMTManagerAPI::UserAccountRequestByLogins(
       const UINT64*     logins,        // list of logins
       const UINT        logins_total,  // number of logins
       IMTAccountArray*  accounts       // trading accounts array object
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.UserAccountRequestByLogins(
       ulong[]            logins,       // logins
       CIMTAccountArray   accounts      // trading accounts array objects
       )

Python
    
    
    ManagerAPI.UserAccountRequestByLogins(
       logins             # logins
       )

### Parameters

**logins**  
[in] Array of client logins.

**logins_total**  
[in] Number of logins in the 'logins' array.

**accounts**  
[out] Array of trading accounts. The 'accounts' object must first be created using theIMTManagerAPI::UserCreateAccountArraymethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method cannot be called from event handlers (any IMT*Sink class methods).
