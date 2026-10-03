[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerAntiDDoS](../IMTConServerAntiDDoS.md) / SourcesUpdate

[Previous](SourcesAdd.md) | [Next](SourcesDelete.md)

# IMTConServerAntiDDoS::SourcesUpdate

Update the range of IP addresses of Anti DDoS provider's proxy servers.

C++
    
    
    MTAPIRES  IMTConServerAntiDDoS::SourcesUpdate(
       const UINT                 pos,    // The position of the range
       IMTConServerAddressRange*  range   // The object of the range
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerAntiDDoS.SourcesUpdate(
       uint                       pos,   // The position of the range
       CIMTConServerAddressRange  range  // The object of the range
       )

Python (Manager API)
    
    
    MTConServerAntiDDoS.SourcesUpdate(
       pos,                       # The position of the range
       range                      # The object of the range
       )

### Parameters

**pos**  
[in] Position of the range of logins in the list, starting with 0.

**range**  
[in] An object of the range.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The ranges of IP addresses of proxy servers should be provide by your Anti DDoS protection service provider. The ranges are used as an additional protection measure: connections forwarded by the Anti-DDoS provider will only be accepted from these addresses.
