[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Main Interface of Reports](../../Main-Interface-of-Reports.md) / [Users](../Users.md) / UserLogins

[Previous](UserGetLight.md) | [Next](UserAccountGet.md)

# IMTReportAPI::UserLogins

Returns an array of logins of the clients who are included in the specified group.
    
    
    MTAPIRES  IMTReportAPI::UserLogins(
       LPCWSTR   group,            // Group name
       UINT64*&  logins,           // An array of client logins
       UINT&     logins_total      // The number of logins
       )

### Parameters

**group**  
[in] The name of a group of users. The entire name of the group must be specified including the path. For example, demo\demoforex. To get the name of a group, use theIMTConGorup::Group.

**logins**  
[out] An array of client logins.

**logins_total**  
[out] The number of logins in the logins array.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The UserLogins function allocates and fills an array of logins that belong to the passed group, a pointer to the passed block is placed to the logins parameter. After using, the array placed in the logins variable must be released using the [IMTReportAPI::Free](../Common-Functions/Free.md) method.
