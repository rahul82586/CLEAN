[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUser](../IMTUser.md) / ExternalAccountNext

[Previous](ExternalAccountTotal.md) | [Next](ExternalAccountGet.md)

# IMTUser::ExternalAccountNext

Gets the number of a client's trading account in the external system and the ID of the gateway, through which the platform interacts with the system.

C++
    
    
    MTAPIRES  IMTUser::ExternalAccountNext(
       const UINT  pos,            // Position
       UINT64&     gateway_id,     // Gateway ID
       MTAPISTR&   account         // Account
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTUser.ExternalAccountNext(
       uint        pos,            // Position
       out ulong   gateway_id,     // Gateway ID
       out string  account         // Account
       )

### Parameters

**pos**  
[in] Account position starting with 0.

**gateway_id**  
[out] The identifier of the gateway with which the account in an external system is associated.

**account**  
[out] An account in the external trading system.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### 
