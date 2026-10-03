[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUser](../IMTUser.md) / ExternalAccountGet

[Previous](ExternalAccountNext.md) | [Next](../IMTUserArray.md)

# IMTUser::ExternalAccountGet

Gets the number of a client's trading account in the external system by the ID of the gateway, through which the platform interacts with the system.

C++
    
    
    MTAPIRES  IMTUser::ExternalAccountGet(
       UINT64&     gateway_id,     // Gateway ID
       MTAPISTR&   account         // Account
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTUser.ExternalAccountGet(
       ulong       gateway_id,     // Gateway ID
       out string  account         // Account
       )

### Parameters

**gateway_id**  
[in] The identifier of the gateway with which the account in an external system is associated.

**account**  
[out] An account in the external trading system.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### 
