[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Data Cache Interfaces](../../Data-Cache-Interfaces.md) / [IMTReportCache](../IMTReportCache.md) / ReadBegin

[Previous](ValueCreate.md) | [Next](ReadEnd.md)

# IMTReportCache::ReadBegin

Start data reading from the cache.
    
    
    MTAPIRES  IMTReportCache::ReadBegin()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

During the IMTReportCache::ReadBegin call, a verification is performed that no other report (plugin) is currently writing data to the cache. If data is currently being written by another report (plugin) the method waits for 10 seconds for recording to finish. If writing is finished by that time, the method returns [MT_RET_OK](../../../Return-Codes/Successful-completion.md) and thus you can start reading. Otherwise, the method returns an error.
