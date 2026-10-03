[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerAntiDDoS](../IMTConServerAntiDDoS.md) / SourcesNext

[Previous](SourcesTotal.md) | [Next](../IMTConClusterState.md)

# IMTConServerAntiDDoS::SourcesNext

Get the range of IP addresses of Anti DDoS provider's proxy servers at the specified index.

C++
    
    
    MTAPIRES  IMTConServerAntiDDoS::SourcesNext(
       const UINT                 pos,   // The position of the range
       IMTConServerAddressRange*  range  // The object of the range
       )  const

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerAntiDDoS.SourcesNext(
       uint                       pos,   // The position of the range
       CIMTConServerAddressRange  range  // The object of the range
       )

Python (Manager API)
    
    
    MTConServerAntiDDoS.SourcesNext(
       pos,                       # The position of the range
       range                      # The object of the range
       )

### Parameters

**pos**  
[in] Position of the range, starting with 0.

**range**  
[out] An object of the range. The 'range' object must first be created using theIMTAdminAPI::NetServerAddressRangeCreateorIMTServerAPI::NetServerAddressRangeCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

This method copies the range of IP addresses with a specified index to the 'range' object.
