[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Manager Interface](../../Manager-Interface.md) / [Geo Services](../Geo-Services.md) / GeoResolve

[Previous](GeoCreate.md) | [Next](GeoResolveBatch.md)

# IMTManagerAPI::GeoResolve

Resolve an IPv4 or IPv6 address.

C++
    
    
    MTAPIRES  IMTManagerAPI::GeoResolve(
       LPCWSTR      address,      // IP address
       const UINT   flags,        // flags
       IMTGeo       record        // IP address description
       )

.NET
    
    
    MTRetCode  CIMTManagerAPI.GeoResolve(
       string                     address, // IP address
       CIMTGeo.EnGeoRequestFlags  flags,   // flags
       CIMTGeo                    record   // IP address description
       )

Python
    
    
    ManagerAPI.GeoResolve(
       address,                   # IP address
       flags                      # flags
       )

### Parameters

**address**  
[in] IPv4 or IPv6 address.

**flags**  
[in] Additional resolution parameters in the form of flags from theIMTGeo::EnGeoRequestFlagsenumeration.

**record**  
[out] IP address description as anIMTGeoobject. The object must be first created by theIMTManagerAPI::GeoCreatemethod.

### Return Value

An indication of a successful performance is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
