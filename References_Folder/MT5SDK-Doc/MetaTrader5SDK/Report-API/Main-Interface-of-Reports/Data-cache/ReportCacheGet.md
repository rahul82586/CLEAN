[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Main Interface of Reports](../../Main-Interface-of-Reports.md) / [Data cache](../Data-cache.md) / ReportCacheGet

[Previous](ReportCacheCreate.md) | [Next](ReportCacheGetTemporary.md)

# IMTReportAPI::ReportCacheGet

Call the [permanent data cache (#continuous)](../Data-cache.md#continuous) by name and version.
    
    
    MTAPIRES  IMTReportAPI::ReportCacheGet(
       LPCWSTR          name,         // Name
       const UINT       version,      // Version
       IMTReportCache*  report_cache  // Cache description
       )

### Parameters

**name**  
[in] The name of the data cache. Corresponds toIMTReportCache::Name.

**version**  
[in] The version of the data cache. Corresponds toIMTReportCache::Version. It is recommended to update the cache version whenever its data structure is changed.

**report_cache**  
[out] TheIMTReportCacheobject which describes the data cache. The object must be previously created using theIMTReportAPI::ReportCacheCreatemethod.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

Permanent cache is identified by name and version. Caches having the same name but different versions, are considered to be two different independent caches.
