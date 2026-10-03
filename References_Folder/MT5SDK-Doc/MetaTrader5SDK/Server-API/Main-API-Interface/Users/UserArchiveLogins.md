[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Users](../Users.md) / UserArchiveLogins

[Previous](UserArchiveGet.md) | [Next](UserRestore.md)

# IMTServerAPI::UserArchiveLogins

Returns an array of logins in an archive database for the specified group.
    
    
    MTAPIRES  IMTServerAPI::UserArchiveLogins(
       LPCWSTR   group,            // Group name
       UINT64*&  logins,           // An array of client logins
       UINT&     logins_total      // The number of logins
       )

### Parameters

**group**  
[in] The name of a group of users. To specify several groups, use the '*' mask (any value) or the '!' symbol (exception). For example: "demo*,!demoforex" - all groups whose names begin with 'demo', except for the group demoforex.

**logins**  
[out] An array of client logins.

**logins_total**  
[out] The number of logins in the logins array.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The UserArchiveLogins function allocates and fills an array of logins that are located in an archive database and belong to the specified group. A pointer to the passed block is placed to the logins parameter. After using, the array placed in the logins variable must be released using the [IMTServerAPI::Free()](../Common-Functions/Free.md) method of the Server API.
