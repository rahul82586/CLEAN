[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Data Cache Interfaces](../../Data-Cache-Interfaces.md) / [IMTReportCacheKeySet](../IMTReportCacheKeySet.md) / ContainsSet

[Previous](Search.md) | [Next](Reserve.md)

# IMTReportCacheKeySet::ContainsSet

Check if the key set contains all the keys from the passed set.
    
    
    MTAPIRES  IMTReportCacheKeySet::ContainsSet(
       const IMTReportCacheKeySet  *keyset      // Set of keys
       )

### Parameters

**keyset**  
[in] TheIMTReportCacheKeySetobjects: the presence of its keys will be checked in the current object.

### Return Value

[MT_RET_OK](../../../Return-Codes/Successful-completion.md), if the passed set of keys exists in the current object.
