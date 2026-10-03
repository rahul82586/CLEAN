[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServer](../IMTConServer.md) / ClusterStateGet

[Previous](ClusterStateNext.md) | [Next](../IMTConServerTrade.md)

# IMTConServer::ClusterStateGet

Get the network connection status with a cluster component having the specified identifier.

C++
    
    
    MTAPIRES  IMTConServer::ClusterStateGet(
       const UINT64        id,     // Identifier
       IMTConServerRange*  state   // Connection status object
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServer.ClusterStateGet(
       ulong               id,     // Identifier
       CIMTConServerRange  state   // Connection status object
       )

Python (Manager API)
    
    
    MTConServer.ClusterStateGet(
       id                  # Identifier
       )

### Parameters

**id**  
[in] The network identifier of the component, the status of connection with which you ant to get. Corresponds toRequestInfo::idof this server (not of the current object).

**state**  
[out] Thenetwork connection statusobject. The 'state' object must be previously created using theIMTServerAPI::NetServerClusterStateCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The method enables the obtaining of the network connection status between the current server ([IMTConServer::Id](Id.md)) and another server within the cluster, which is specified as a network identifier.
