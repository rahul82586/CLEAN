[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Data Cache Interfaces](../../Data-Cache-Interfaces.md) / [IMTReportCacheKeySet](../IMTReportCacheKeySet.md) / Assign

[Previous](Release.md) | [Next](Clear.md)

# IMTReportCacheKeySet::Assign

Assign a passed object to the current one.
    
    
    MTAPIRES  IMTReportCacheKeySet::Assign(
       const IMTReportCacheKeySet*  keyset      // Source object
       )

### Parameters

**keyset**  
[in] Source object.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error has occurred, which corresponds to the response code.
