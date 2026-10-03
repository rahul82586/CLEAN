[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Data Cache Interfaces](../../Data-Cache-Interfaces.md) / [IMTReportCacheKeySet](../IMTReportCacheKeySet.md) / Next

[Previous](Array.md) | [Next](Search.md)

# IMTReportCacheKeySet::Next

Get the next key from a sorted key array.
    
    
    const UINT64*  IMTReportCacheKeySet::Next(
       const UINT64*  key      // Key
       )

### Parameters

**key**  
[in] A pointer to a key in the sorted array of keys. To get the pointer to the first key from the set, use theIMTReportCacheKeySet::Arraymethod.

### Return Value

A pointer to the next key or NULL if the array end is reached.
