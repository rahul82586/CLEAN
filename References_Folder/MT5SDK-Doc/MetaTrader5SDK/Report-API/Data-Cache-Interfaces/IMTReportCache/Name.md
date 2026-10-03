[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Data Cache Interfaces](../../Data-Cache-Interfaces.md) / [IMTReportCache](../IMTReportCache.md) / Name

[Previous](Release.md) | [Next](TimeLastWrite.md)

# IMTReportCache::Name

Get the name of the data cache.
    
    
    LPCWSTR  IMTReportCache::Name()

### Return Value

The name of the data cache.

### Note

The name is used for accessing the data cache using methods [IMTReportAPI::ReportCacheGet](../../Main-Interface-of-Reports/Data-cache/ReportCacheGet.md) and [IMTReportAPI::ReportCacheGetTemporary](../../Main-Interface-of-Reports/Data-cache/ReportCacheGetTemporary.md).
