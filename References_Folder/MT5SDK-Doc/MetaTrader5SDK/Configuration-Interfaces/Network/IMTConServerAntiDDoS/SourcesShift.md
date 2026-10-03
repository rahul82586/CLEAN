[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerAntiDDoS](../IMTConServerAntiDDoS.md) / SourcesShift

[Previous](SourcesDelete.md) | [Next](SourcesTotal.md)

# IMTConServerAntiDDoS::SourcesShift

Change the position of the range of IP addresses of Anti DDoS provider's proxy servers in the list.

C++
    
    
    MTAPIRES  IMTConServerAntiDDoS::SourcesShift(
       const UINT  pos,      // The position of the range
       const int   shift      // Shift
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerAntiDDoS.SourcesShift(
       uint        pos,       // The position of the range
       int         shift      // Shift
       )

Python (Manager API)
    
    
    MTConServerAntiDDoS.SourcesShift(
       pos,        # The position of the range
       shift       # Shift
       )

### Parameters

**pos**  
[in] Position of the range, starting with 0.

**shift**  
[in] Shift from its current position. A negative value means shift towards the top of the list, a positive value shifts towards the end.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

The ranges of IP addresses of proxy servers should be provide by your Anti DDoS protection service provider. The ranges are used as an additional protection measure: connections forwarded by the Anti-DDoS provider will only be accepted from these addresses.
