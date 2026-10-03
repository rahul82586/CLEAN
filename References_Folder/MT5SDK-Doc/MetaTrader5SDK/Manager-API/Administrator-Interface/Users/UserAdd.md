[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Users](../Users.md) / UserAdd

[Previous](UserCreateArray.md) | [Next](UserDelete.md)

# IMTAdminAPI::UserAdd

Add a client record.

C++
    
    
    MTAPIRES  IMTAdminAPI::UserAdd(
       IMTUser*  user,              // An object of the client record
       LPCWSTR   master_pass,       // The master password
       LPCWSTR   investor_pass      // The investor password
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.UserAdd(
       CIMTUser  user,              // An object of the client record
       string    master_pass,       // The master password
       string    investor_pass      // The investor password
       )

Python
    
    
    AdminAPI.UserAdd(
       user,          # An object of the client record
       master_pass,   # The master password
       investor_pass  # The investor password
       )

### Parameters

**user**  
[in][out] An object of the client record.

**master_pass**  
[in] The master password of an account. The password must contain four character types: lowercase letters, uppercase letters, numbers, andspecial characters(#, @, ! etc.). For example, 1Ar#pqkj. The minimum password length is determined by group settings (IMTConGroup::AuthPasswordMin), while the lowest possible value is 8 characters. The maximum length is 16 characters.

**investor_pass**  
[in] The investor password of an account. The password must contain four character types: lowercase letters, uppercase letters, numbers, andspecial characters(#, @, ! etc.). For example, 1Ar#pqkj. The minimum password length is determined by group settings (IMTConGroup::AuthPasswordMin), while the lowest possible value is 8 characters. The maximum length is 16 characters.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, a corresponding error code will be returned.

### Note

In case no login is specified for a record (is equal to 0), the server will automatically allocate a login from the available range and will assign it to the user record. In case there are no more available ranges of logins, the [MT_RET_USR_LOGIN_EXHAUSTED](../../../Return-Codes/User-management.md) error is returned.
