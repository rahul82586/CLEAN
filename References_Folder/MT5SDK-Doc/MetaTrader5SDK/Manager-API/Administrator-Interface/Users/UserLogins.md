[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Users](../Users.md) / UserLogins

[Previous](UserExternalSync.md) | [Next](NotificationsSend.md)

# IMTAdminAPI::UserLogins

Returns an array of logins of the clients who are included in the specified group.

C++
    
    
    MTAPIRES  IMTAdminAPI::UserLogins(
       LPCWSTR   group,            // Group name
       UINT64*&  logins,           // An array of client logins
       UINT&     logins_total      // The number of logins
       )

.NET
    
    
    ulong[]  CIMTAdminAPI.UserLogins(
       string         group,       // Group name
       out MTRetCode  res          // Response code
       )

Python
    
    
    AdminAPI.UserLogins(
       group          # Group name
       )

### Parameters

**group**  
[in] The name of a group of users. The entire name of the group must be specified including the path. For example, demo\demoforex. To get the name of a group, use theIMTConGroup::Groupmethod.

**logins**  
[out] An array of client logins.

**logins_total**  
[out] The number of logins in the logins array.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The UserLogins method allocates and fills an array of logins that belong to the passed group, a pointer to the passed block is placed to the logins parameter After using, the array placed in the logins variable must be released using the [IMTAdminAPI::Free()](UserCreateArray.md) method of the Manager API.
