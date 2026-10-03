[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Users](../Users.md) / UserExternalRequest

[Previous](UserBalanceCheckBatch.md) | [Next](UserExternalSync.md)

# IMTAdminAPI::UserExternalRequest

Request a client record from a server by the [gateway identifier](../../../Configuration-Interfaces/Gateways/IMTConGateway/ID.md) and the [account number in an external trading system](../../../Database-Interfaces/Users/IMTUser/ExternalAccountGet.md).

C++
    
    
    MTAPIRES  IMTAdminAPI::UserExternalRequest(
       const UINT64  gateway_id,  // Gateway ID
       LPCWSTR       account,     // Account number in an external system
       IMTUser*      user         // An object of the user record
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.UserExternalRequest(
       ulong         gateway_id,  // Gateway ID
       string        account,     // Account number in an external system
       CIMTUser      user         // An object of the user record
       )

Python
    
    
    AdminAPI.UserExternalRequest(
       gateway_id    # Gateway ID
       account       # Account number in an external system
       )

### Parameters

**gateway_id**  
[in] The identifier of a gateway. The account number of a client in an external system.

**account**  
[in] Client's account in an external system.

**user**  
[out] An object of the client login. The user object must first be created using theIMTAdminAPI::UserCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies the data of a client with the specified gateway identifier and account number.

# IMTAdminAPI::UserExternalRequest

Request a client record from a server by the [account number in an external trading system](../../../Database-Interfaces/Users/IMTUser/ExternalAccountGet.md) irrespective of a [gateway identifier](../../../Configuration-Interfaces/Gateways/IMTConGateway/ID.md).

C++
    
    
    MTAPIRES  IMTAdminAPI::UserExternalRequest(
       LPCWSTR       account,     // Account number in an external system
       IMTUser*      user         // An object of the user record
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.UserExternalRequest(
       string        account,     // Account number in an external system
       CIMTUser      user         // An object of the user record
       )

Python
    
    
    AdminAPI.UserExternalRequest(
       account       # Account number in an external system
       )

### Parameters

**account**  
[in] Client's account in an external system.

**user**  
[out] An object of the client login. The user object must first be created using theIMTAdminAPI::UserCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies the data of a client with the specified gateway identifier and account number.
