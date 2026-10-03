[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Geo Services](../Geo-Services.md) / GeoResolveBatch

[Previous](GeoResolve.md) | [Next](GeoResolveAny.md)

# IMTServerAPI::GeoResolveAny

Resolve a list of IP addresses of any type: IPv4 or IPv6.
    
    
    MTAPIRES  IMTServerAPI::GeoResolveAny(
       LPCWSTR*     addresses,       // array of IP addresses
       const UINT   addresses_total, // number of addresses
       const UINT   flags,           // flags
       IMTGeo**     records,         // description of IP addresses
       MTAPIRES*    results          // array of results
       )

### Parameters

**addresses**  
[in] Array of addresses of any type: IPv4 or IPv6.

**addresses_total**  
[in] Number of addresses in the 'addresses' array.

**flags**  
[in] Additional resolution parameters in the form of flags from theIMTGeo::EnGeoRequestFlagsenumeration.

**records**  
[out] Description of IP addresses as an array ofIMTGeoobjects. The objects must be first created by theIMTServerAPI::GeoCreatemethod.

**results**  
[out] Array with the address resolution results. The size of the 'results' array must not be less than that of 'addresses'.

### Return Value

The [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code indicates that all specified addresses have been processed. The [MT_RET_ERR_PARTIAL](../../../Return-Codes/Common-errors.md) response code indicates that resolution results are only available for some of the addresses. Analyze the 'results' array for more details on the execution results. It contains the result of processing of each address from the 'addresses' array. The result index corresponds to the address index in the source array.

### Note

In 'addresses' you can simultaneously transfer IP addresses of both types.
