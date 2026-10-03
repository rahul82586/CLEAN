[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Main Interface of Reports](../../Main-Interface-of-Reports.md) / [Data cache](../Data-cache.md) / KeySetCreate

[Previous](ReportCacheGetTemporary.md) | [Next](KeySetParamLogins.md)

# IMTReportAPI::KeySetCreate

Create a key set object for working with the cached data.
    
    
    IMTReportCacheKeySet*  IMTReportAPI::KeySetCreate()

### Return Value

Returns a pointer to the created object which implements the [IMTReportCacheKeySet](../../Data-Cache-Interfaces/IMTReportCacheKeySet.md) interface. In case of failure, it returns NULL.

### Note

The created object must be destroyed by calling the [IMTReportCacheKeySet::Release](../../Data-Cache-Interfaces/IMTReportCacheKeySet/Release.md) method of this object.
