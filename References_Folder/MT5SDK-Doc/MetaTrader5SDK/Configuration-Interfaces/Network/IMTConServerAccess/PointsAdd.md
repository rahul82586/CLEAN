[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Network](../../Network.md) / [IMTConServerAccess](../IMTConServerAccess.md) / PointsAdd

[Previous](AntifloodErrors.md) | [Next](PointsUpdate.md)

# IMTConServerAccess::PointsAdd

Add an access point (public address).

C++
    
    
    MTAPIRES  IMTConServerAccess::PointsAdd(
       LPCWSTR  path      // Address and port of the access point
       )

.NET (Gateway/Manager API)
    
    
    MTRetCode  CIMTConServerAccess.PointsAdd(
       string   path      // Address and port of the access point
       )

Python (Manager API)
    
    
    MTConServerAccess.PointsAdd(
       path     # Address and port of the access point
       )

### Parameters

**path**  
[in] Address and port of the access point, separated by a colon.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

An access point is specified in the format address:port.
