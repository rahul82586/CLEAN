[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Users](../Users.md) / UserExternalSync

[Previous](UserExternalRequest.md) | [Next](UserBalanceCheck.md)

# IMTManagerAPI::UserExternalSync

Synchronizing client's trading status with an external trading system. When calling this method, [IMTGatewaySink::HookGatewayAccountRequest](../../../Gateway-API/Event-Interface/HookGatewayAccountRequest.md) hook is called in Gateway API. MetaTrader 5 client's trading status will be brought in line with an external trading system when this method is executed in case the gateway developer has provided such a possibility.

C++
    
    
    MTAPIRES  IMTManagerAPI::UserExternalSync(
       const UINT64  login,       // Login
       const UINT64  gateway_id,  // Gateway ID
       LPCWSTR       account_id,  // External system account
       UINT          sync_mode    // Synchronization mode
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.UserExternalSync(
       ulong                               login,       // Login
       ulong                               gateway_id,  // Gateway ID
       string                              account_id,  // External system account
       CIMTManagerAPI.EnExternalSyncModes  sync_mode    // Synchronization mode
       )

Python
    
    
    ManagerAPI.UserExternalSync(
       login,        # Login
       gateway_id,   # Gateway ID
       account_id,   # External system account
       sync_mode     # Synchronization mode
       )

### Parameters

**login**  
[in] Login of the client, for whom synchronization is performed.

**gateway_id**  
[in]Gateway ID. Gateway ID is associated with an account number in an external system.

**account_id**  
[in] Client's account in an external system.

**sync_mode**  
[out] Synchronization mode. Transferred usingIMTManagerAPI::EnExternalSyncModesenumeration.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method works only if trading status synchronization is provided at the gateway used by the client.
