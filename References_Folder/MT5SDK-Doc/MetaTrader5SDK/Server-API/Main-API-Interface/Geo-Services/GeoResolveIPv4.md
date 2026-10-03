[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Geo Services](../Geo-Services.md) / GeoResolveIPv4

[Previous](GeoResolveAny.md) | [Next](GeoResolveIPv4Bulk.md)

# IMTServerAPI::GeoResolveIPv4

Resolve one IPv4 address.
    
    
    MTAPIRES  IMTServerAPI::GeoResolveIPv4(
       const ULONG  ip,          // IP address
       LPWSTR       result,      // Result of resolving
       const UINT   result_len,  // Result size
       const UINT   flags        // Flags
       )

### Parameters

**ip**  
[in] IP address.

**result**  
[out] String array with resolving results: source IP address, region, country, city, province, zip code, providers and coordinates.

**result_len**  
[in] The size of the 'result' array in bytes.

**flags**  
[in] Additional resolving parameters in the form of flags. The parameter is currently not used, fill it with zero.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The method is obsolete and is no longer used.
