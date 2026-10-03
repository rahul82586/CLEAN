[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Users](../Users.md) / UserRequestArray

[Previous](UserRequest.md) | [Next](UserRequestByLogins.md)

# IMTAdminAPI::UserRequestArray

Request an array of client records by the group name.

C++
    
    
    MTAPIRES  IMTAdminAPI::UserRequestArray(
       LPCWSTR       group,  // Client group
       IMTUserArray* users   // Array of client records
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.UserRequestArray(
       string        group,  // Client group
       CIMTUserArray users   // Array of client records<
       )

Python
    
    
    AdminAPI.UserRequestByGroup(
       str           group   # Client group
       )
    
    
    AdminAPI.UserRequestByGroupCSV(
       str           group,  # Client group
       str           fields  # Comma-separated list of required fields
       )
    
    
    AdminAPI.UserRequestByGroupNumPy(
       str           group,  # Client group
       str           fields  # Comma-separated list of required fields
       )

### Parameters

**group**  
[in] One or more groups, separated by commas, from which accounts are requested. The full group name must be specified, including the path. For example, demo\demoforex. The group name can be obtained using theIMTConGroup::Groupmethod. Groups can also be specified using wildcard characters: "*" (any value) and "!" (exclude). For example: "demo*,!demoforex" - all groups whose names begin with 'demo', except for the group demoforex.

**user**  
[out] An array of objects of users. The object of array of users must first be created using theIMTAdminAPI::UserCreateArraymethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, a corresponding error code will be returned.

### Note

This method copies the data of users with the group to the users array object.
