[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Data Cache Interfaces](../../Data-Cache-Interfaces.md) / [IMTReportCacheKeySet](../IMTReportCacheKeySet.md) / Swap

[Previous](Clear.md) | [Next](Total.md)

# IMTReportCacheKeySet::Swap

Exchange key sets with the passed object.
    
    
    MTAPIRES  IMTReportCacheKeySet::Swap(
       IMTReportCacheKeySet*  keyset      // Set of keys
       )

### Parameters

**keyset**  
[in] TheIMTReportCacheKeySetobjects, keys from which will replace keys in the current object. Keys from the current object will replace keys in the passed object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
