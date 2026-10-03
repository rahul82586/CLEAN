[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Data Cache Interfaces](../../Data-Cache-Interfaces.md) / [IMTReportCacheKeySet](../IMTReportCacheKeySet.md) / Search

[Previous](Next.md) | [Next](ContainsSet.md)

# IMTReportCacheKeySet::Search

Search key in the array.
    
    
    const UINT64*  IMTReportCacheKeySet::Search(
       const UINT64  key      // Key
       )

### Parameters

**key**  
[in] The key which you want to find.

### Return Value

Pointer to the found key or NULL if nothing is found.
