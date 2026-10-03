[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Data Cache Interfaces](../../Data-Cache-Interfaces.md) / [IMTReportCache](../IMTReportCache.md) / ValueCreate

[Previous](TimeLastWrite.md) | [Next](ReadBegin.md)

# IMTReportCache::ValueCreate

Create a cache value object.
    
    
    IMTReportCacheValue*  IMTReportCache::ValueCreate()

### Return Value

Returns a pointer to the created object which implements the [IMTReportCacheValue](../IMTReportCacheValue.md) interface. In case of failure, it returns NULL.

### Note

The created object must be destroyed by calling the [IMTReportCacheValue::Release](../IMTReportCacheValue/Release.md) method of this object.
