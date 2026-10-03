[🏠 Document Start](../../../README.md) / [Manager API](../../README.md) / [Administrator Interface](../../Administrator-Interface.md) / [Geo Services](../Geo-Services.md) / GeoResolve

[Previous](GeoCreate.md) | [Next](GeoResolveBatch.md)

# IMTAdminAPI::GeoResolve

Resolve an IPv4 or IPv6 address.

C++
    
    
    MTAPIRES  IMTAdminAPI::GeoResolve(
       LPCWSTR      address,      // IP address
       const UINT   flags,        // flags
       IMTGeo       record        // IP address description
       )

.NET
    
    
    MTRetCode  CIMTAdminAPI.GeoResolve(
       string                     address, // IP address
       CIMTGeo.EnGeoRequestFlags  flags,   // flags
       CIMTGeo                    record   // IP address description
       )

Python
    
    
    AdminAPI.GeoResolve(
       address,                   # IP address
       flags                      # flags
       )

### Parameters

**address**  
[in] IPv4 or IPv6 address.

**flags**  
[in] Additional resolution parameters in the form of flags from theIMTGeo::EnGeoRequestFlagsenumeration.

**record**  
[out] IP address description as anIMTGeoobject. The object must be first created by theIMTAdminAPI::GeoCreatemethod.

### Return Value

An indication of a successful performance is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
