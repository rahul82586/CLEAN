[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Users](../Users.md) / UserExternalGet

[Previous](UserAccountRequestArray.md) | [Next](UserExternalRequest.md)

# IMTManagerAPI::UserExternalGet

Get a client record by the [gateway identifier](../../../Configuration-Interfaces/Gateways/IMTConGateway/ID.md) and the [account number in an external trading system](../../../Database-Interfaces/Users/IMTUser/ExternalAccountGet.md).

C++
    
    
    MTAPIRES  IMTManagerAPI::UserExternalGet(
       const UINT64  gateway_id,  // Gateway ID
       LPCWSTR       account,     // Account number in an external system
       IMTUser*      user         // An object of the user record
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.UserExternalGet(
       ulong         gateway_id,  // Gateway ID
       string        account,     // Account number in an external system
       CIMTUser      user         // An object of the user record
       )

Python
    
    
    ManagerAPI.UserExternalGet(
       gateway_id    # Gateway ID
       account       # Account number in an external system
       )

### Parameters

**gateway_id**  
[in] The identifier of a gateway.

**account**  
[in] Client's account in an external system.

**user**  
[out] An object of the client login. The user object must first be created using theIMTManagerAPI::UserCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies the data of a client with the specified gateway identifier and account number. The method is valid only if the [IMTManagerAPI::PUMP_MODE_USERS](../Connection-to-the-Server/Pumping-Modes.md) pumping mode was specified during connection.

# IMTManagerAPI::UserExternalGet

Get a client record by the the [account number in an external trading system](../../../Database-Interfaces/Users/IMTUser/ExternalAccountGet.md) irrespective of a [gateway identifier](../../../Configuration-Interfaces/Gateways/IMTConGateway/ID.md).

C++
    
    
    MTAPIRES  IMTManagerAPI::UserExternalGet(
       LPCWSTR       account,     // Account number in an external system
       IMTUser*      user         // An object of the user record
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.UserExternalGet(
       string        account,     // Account number in an external system
       CIMTUser      user         // An object of the user record
       )

Python
    
    
    ManagerAPI.UserExternalGet(
       account       # Account number in an external system
       )

### Parameters

**account**  
[in] Client's account in an external system.

**user**  
[out] An object of the client login. The user object must first be created using theIMTManagerAPI::UserCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies the data of a client with the specified and account number. The method is valid only if the [IMTManagerAPI::PUMP_MODE_USERS](../Connection-to-the-Server/Pumping-Modes.md) pumping mode was specified during connection.
