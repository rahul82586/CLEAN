[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Geo Services](../Geo-Services.md) / GeoResolve

[Previous](GeoCreate.md) | [Next](GeoResolveBatch.md)

# IMTServerAPI::GeoResolve

Resolve an IPv4 or IPv6 address.
    
    
    MTAPIRES  IMTServerAPI::GeoResolve(
       LPCWSTR      address,     // IP address
       const UINT   flags,       // flags
       IMTGeo       record       // IP address description
       )

### Parameters

**address**  
[in] IPv4 or IPv6 address.

**flags**  
[in] Additional resolution parameters in the form of flags from theIMTGeo::EnGeoRequestFlagsenumeration.

**record**  
[out] IP address description as anIMTGeoobject. The object must be first created by theIMTReportAPI::GeoCreatemethod.

### Return Value

An indication of a successful performance is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred that corresponds to the response code.
