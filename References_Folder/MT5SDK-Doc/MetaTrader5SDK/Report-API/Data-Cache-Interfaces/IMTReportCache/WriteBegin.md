[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Data Cache Interfaces](../../Data-Cache-Interfaces.md) / [IMTReportCache](../IMTReportCache.md) / WriteBegin

[Previous](ReadDictionaryString.md) | [Next](WriteEnd.md)

# IMTReportCache::WriteBegin

Start writing data to the cache.
    
    
    MTAPIRES  IMTReportCache::WriteBegin()

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

Only one report instance can be reading/writing data to cache at a time. If an attempt is made to access the cache from which the data is currently being read or written, the method waits for 20 seconds. If reading/writing is not finished by that time, the method returns an error.
