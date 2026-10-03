[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServer](../IMTConServer.md) / ClusterStateNext

[Previous](ClusterStateTotal.md) | [Next](ClusterStateGet.md)

# IMTConServer::ClusterStateNext

Get the network connection status with a cluster component having the specified index.

C++
    
    
    MTAPIRES  IMTConServer::ClusterStateNext(
       const UINT          pos,   // Component position
       IMTConServerRange*  state  // Connection status object
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServer.ClusterStateNext(
       uint                pos,   // Component position
       CIMTConServerRange  state  // Connection status object
       )

Python (Manager API)
    
    
    MTConServer.ClusterStateNext(
       pos                 # Component position
       )

### Parameters

**pos**  
[in] The position of the cluster component in the list, starting with 0.

**state**  
[out] Thenetwork connection statusobject. The 'state' object must be previously created using theIMTServerAPI::NetServerClusterStateCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The enables the obtaining of the network connection status between the current server ([IMTConServer::Id](Id.md)) and another server within the cluster, which is specified as a position in the list of components.
