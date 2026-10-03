[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerAntiDDoS](../IMTConServerAntiDDoS.md) / SourcesAdd

[Previous](ServersNext.md) | [Next](SourcesUpdate.md)

# IMTConServerAntiDDoS::SourcesAdd

Add a range of IP addresses of Anti DDoS provider's proxy servers.

C++
    
    
    MTAPIRES  IMTConServerAntiDDoS::SourcesAdd(
       IMTConServerAddressRange*  range      // The object of the range
       )

.NET
    
    
    MTRetCode  CIMTConServerAntiDDoS.SourcesAdd(
       CIMTConServerAddressRange  range      // The object of the range
       )

Python (Manager API)
    
    
    MTConServerAntiDDoS.SourcesAdd(
       range                      # The object of the range
       )

### Parameters

**range**  
[in] An object of the range.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The ranges of IP addresses of proxy servers should be provide by your Anti DDoS protection service provider. The ranges are used as an additional protection measure: connections forwarded by the Anti-DDoS provider will only be accepted from these addresses.
