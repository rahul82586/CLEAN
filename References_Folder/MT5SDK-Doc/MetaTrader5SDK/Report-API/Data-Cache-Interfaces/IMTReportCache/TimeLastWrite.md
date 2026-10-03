[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Data Cache Interfaces](../../Data-Cache-Interfaces.md) / [IMTReportCache](../IMTReportCache.md) / TimeLastWrite

[Previous](Name.md) | [Next](ValueCreate.md)

# IMTReportCache::TimeLastWrite

Get the time of the last data cache change.
    
    
    INT64  IMTReportCache::TimeLastWrite()

### Return Value

The time of the last modification of the data cache, in seconds elapsed since 01.01.1970.

### Note

Use this method to determine if data in the cache needs to be updated.
