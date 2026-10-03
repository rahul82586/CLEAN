[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Users](../Users.md) / UserArchiveRequestArray

[Previous](UserArchiveRequest.md) | [Next](UserArchiveRequestByLogins.md)

# IMTAdminAPI::UserArchiveRequestArray

Request accounts from an archive databased, filtered by groups.

C++
    
    
    MTAPIRES  IMTAdminAPI.UserArchiveRequestArray(
       LPCWSTR       groups,     // Groups
       IMTUserArray* users       // Array of accounts
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.UserArchiveRequestArray(
       string        groups,     // Groups
       CIMTUserArray users       // Array of accounts
       )

Python
    
    
    AdminAPI.UserArchiveRequestArray(
       groups        # Groups
       )

### Parameters

**groups**  
[in] One or more groups, separated by commas, from which accounts are requested. The full group name must be specified, including the path. For example, demo\demoforex. The group name can be obtained using theIMTConGroup::Groupmethod.

**user**  
[out] An object of the accounts array. The 'users' object must be previously created using theIMTAdminAPI::UserCreateArraymethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method cannot be called from event handlers (any IMT*Sink class methods).
