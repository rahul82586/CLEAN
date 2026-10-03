[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServer](../IMTConServer.md) / FailoverMode

[Previous](BindingsNext.md) | [Next](FailoverTimeout.md)

# IMTConServer::FailoverMode

Getting the [automated failover mode](https://support.metaquotes.net/en/docs/mt5/platform/components/backup_server/backup_server_switch).

C++
    
    
    UINT  IMTConServer::FailoverMode()  const

.NET (Gateway/Manager API)
    
    
    EnFailoverModes  CIMTConServer.FailoverMode()

Python (Manager API)
    
    
    MTConServer.FailoverMode

### Return Value

Obe of the values of the [IMTConServer::EnFailoverModes (#enfailovermodes)](Enumerations.md#enfailovermodes) enumeration.

# IMTConServer::FailoverMode

Setting the [automated failover mode](https://support.metaquotes.net/en/docs/mt5/platform/components/backup_server/backup_server_switch).

C++
    
    
    MTAPIRES  IMTConServer::FailoverMode(
       const UINT       type  // Failover mode
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServer.FailoverMode(
       EnFailoverModes  type  // Failover mode
       )

Python (Manager API)
    
    
    MTConServer.FailoverMode

### You should use these inputs;

**type**  
[in] TheIMTConServer::EnFailoverModesenumeration is used to pass the failover mode.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.
