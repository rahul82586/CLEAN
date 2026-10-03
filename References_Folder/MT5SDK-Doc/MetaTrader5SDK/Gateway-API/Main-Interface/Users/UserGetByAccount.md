[🏠 Document Start](../../../README.md) / [Gateway API](../../README.md) / [Main Interface](../../Main-Interface.md) / [Users](../Users.md) / UserGetByAccount

[Previous](UserGet.md) | [Next](UserGroup.md)

# IMTGatewayAPI::UserGetByAccount

Get a client record, which corresponds to the account number in the external trading system.

C++
    
    
    MTAPIRES  IMTGatewayAPI::UserGetByAccount(
       LPCWSTR       account,   // Account number
       IMTUser*      user       // Client record object
       )

.NET
    
    
    MTRetCode  CIMTGatewayAPI.UserGetByAccount(
       ulong         account,   // Account number
       CIMTUser      user       // Client record object
       )

### Parameters

**account**  
[in] The number of the account in an external trading system.

**user**  
[out] An object of the client record. The user object must first be created using theIMTGatewayAPI::UserCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note
