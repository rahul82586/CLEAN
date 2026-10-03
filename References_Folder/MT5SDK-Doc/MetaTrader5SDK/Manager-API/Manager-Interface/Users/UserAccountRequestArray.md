[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Users](../Users.md) / UserAccountRequestArray

[Previous](UserAccountRequestByLogins.md) | [Next](UserExternalGet.md)

# IMTManagerAPI::UserAccountRequestArray

Request an array of trade accounts from a server by the group name.

C++
    
    
    virtual MTAPIRES  IMTManagerAPI::UserAccountRequestArray(
       LPCWSTR            group,    // Client group
       IMTAccountArray*   accounts  // An array of trading accounts
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.UserAccountRequestArray(
       string             group,    // Client group
       CIMTAccountArray   accounts  // An array of trading accounts
       )

Python
    
    
    ManagerAPI.UserAccountRequestArray(
       group              # Client group
       )

### Parameters

**group**  
[in]The name of a client group.

**accounts**  
[out] An object of an array of trading accounts. The object of array of trading accounts must be created using theIMTManagerAPI::UserCreateAccountArraymethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
