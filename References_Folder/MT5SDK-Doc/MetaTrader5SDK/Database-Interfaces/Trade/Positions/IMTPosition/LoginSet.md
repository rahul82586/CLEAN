[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Positions](../../Positions.md) / [IMTPosition](../IMTPosition.md) / LoginSet

[Previous](Login.md) | [Next](Symbol.md)

# IMTPosition::LoginSet

Sets the login of the client, to whom the trade position belongs.

C++
    
    
    UINT64  IMTPosition::LoginSet(
       const UINT64  login      // Client login
       )

.NET (Gateway/Manager API)
    
    
    ulong  CIMTPosition.LoginSet(
       ulong         login      // Client login
       )

### Parameters

**login**  
[in] The login of the client to whom the trade position belongs.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.

### Note

The method should only be used for recovering databases of positions using the [IMTAdminAPI::PositionBackupRestore](../../../../Manager-API/Administrator-Interface/Trade-Databases/Positions/PositionBackupRestore.md) method.
