[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Data Cache Interfaces](../../Data-Cache-Interfaces.md) / [IMTReportCache](../IMTReportCache.md) / ReadEnd

[Previous](ReadBegin.md) | [Next](ReadParamFrom.md)

# IMTReportCache::ReadEnd

Finish data reading from the cache.
    
    
    MTAPIRES  IMTReportCache::ReadEnd()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

After a successful call of [IMTReportCache::ReadBegin](ReadBegin.md) and before the call of IMTReportCache::ReadEnd, other reports (plugins) cannot write data to this cache.
