[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUser](../IMTUser.md) / Group

[Previous](Login.md) | [Next](CertSerialNumber.md)

# IMTUser::Group

Get the group to which the user is included.

C++
    
    
    LPCWSTR  IMTUser::Group()  const

.NET (Gateway/Manager API)
    
    
    string  CIMTUser.Group()

### Return Value

If successful, it returns a pointer to a string with the group of a user. Otherwise, it returns NULL.

### Note

The pointer to the resulting string is valid for the lifetime of the [IMTUser](../IMTUser.md) object.

# IMTUser::Group

Set the group of a user.

C++
    
    
    MTAPIRES  IMTUser::Group(
       LPCWSTR  group      // Group of accounts
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTUser.Group(
       string   group      // Group of accounts
       )

### Parameters

**group**  
[in] A group of accounts in accordance with the hierarchy of groups in the trading platform.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

A group is specified in accordance with the hierarchy of groups in the trading platform. You can specify only a group that belongs to the same server where the plugin is running.
