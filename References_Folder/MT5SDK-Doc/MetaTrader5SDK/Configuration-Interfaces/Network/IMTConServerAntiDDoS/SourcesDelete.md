[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerAntiDDoS](../IMTConServerAntiDDoS.md) / SourcesDelete

[Previous](SourcesUpdate.md) | [Next](SourcesShift.md)

# IMTConServerAntiDDoS::SourcesDelete

Delete the range of IP addresses of Anti DDoS provider's proxy servers.

C++
    
    
    MTAPIRES  IMTConServerAntiDDoS::SourcesDelete(
       const UINT  pos      // The position of the range
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerAntiDDoS.SourcesDelete(
       uint        pos      // The position of the range
       )

Python (Manager API)
    
    
    MTConServerAntiDDoS.SourcesDelete(
       pos         # The position of the range
       )

### Parameters

**pos**  
[in] Position of the range, starting with 0.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

If the object is not found, the response code [MT_RET_ERR_NOTFOUND](../../../Return-Codes/Common-errors.md) is returned.
