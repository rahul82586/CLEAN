[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Main Interface of Reports](../../Main-Interface-of-Reports.md) / [Data cache](../Data-cache.md) / ReportCacheGetTemporary

[Previous](ReportCacheGet.md) | [Next](KeySetCreate.md)

# IMTReportAPI::ReportCacheGetTemporary

Call the [temporary data cache (#temporary)](../Data-cache.md#temporary) by name and version.
    
    
    MTAPIRES  IMTReportAPI::ReportCacheGetTemporary(
       LPCWSTR          name,              // Name
       const UINT       version,           // Version
       const UINT64     key_time_to_live,  // Time-to-live
       IMTReportCache*  report_cache       // Cache description
       )

### Parameters

**name**  
[in] The name of the data cache. Corresponds toIMTReportCache::Name.

**version**  
[in] The version of the data cache. Corresponds toIMTReportCache::Version. It is recommended to update the cache version whenever its data structure is changed.

**key_time_to_live**  
[in] The TTL (time-to-live) of keys in the data cache in seconds. After that time (since the time of addition), the key is deleted from the cache. The zero value means that the TTL is not limited.

**report_cache**  
[out] TheIMTReportCacheobject which describes the data cache.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

Temporary cache is identified by name, version and TTL. Caches having the same name and version but different TTL are considered to be two different independent caches.
