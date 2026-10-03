[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Main Interface of Reports](../../Main-Interface-of-Reports.md) / [Data cache](../Data-cache.md) / ReportCacheCreate

[Previous](../Data-cache.md) | [Next](ReportCacheGet.md)

# IMTReportAPI::ReportCacheCreate

Create a data cache object.
    
    
    IMTReportCache*  IMTReportAPI::UserCreate()

### Return Value

Returns a pointer to the created object which implements the [IMTReportCache](../../Data-Cache-Interfaces/IMTReportCache.md) interface. In case of failure, it returns NULL.

### Note

The created object must be destroyed by calling the [IMTReportCache::Release](../../Data-Cache-Interfaces/IMTReportCache/Release.md) method of this object.
