[🏠 Document Start](../../../README.md) / [Server API](../../README.md) / [Main API Interface](../../Main-API-Interface.md) / [Geo Services](../Geo-Services.md) / GeoResolveIPv6Bulk

[Previous](GeoResolveIPv6.md) | [Next](../Dataset.md)

# IMTServerAPI::GeoResolveIPv6Bulk

Resolve multiple IPv6 addresses.
    
    
    MTAPIRES  IMTServerAPI::GeoResolveIPv6Bulk(
       const IN6_ADDR* ip_list,     // Array of IP addresses
       const UINT      ip_list_len, // Array size
       LPWSTR          result,      // Result of resolving
       const UINT      result_len,  // Result size
       const UINT      flags        // Flags
       )

### Parameters

**ip_list**  
[in] Array of IP addresses.

**ip_list_len**  
[in] The ip_list array size in bytes.

**result**  
[out] String array with resolving results: source IP address, region, country, city, province, zip code, providers and coordinates.

**result_len**  
[in] The size of the 'result' array in bytes.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.

### Note

The method is obsolete and is no longer used.
