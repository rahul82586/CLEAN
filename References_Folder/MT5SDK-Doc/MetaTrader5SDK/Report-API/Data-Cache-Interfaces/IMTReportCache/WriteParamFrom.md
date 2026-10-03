[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Data Cache Interfaces](../../Data-Cache-Interfaces.md) / [IMTReportCache](../IMTReportCache.md) / WriteParamFrom

[Previous](WriteEnd.md) | [Next](WriteParamTo.md)

# IMTReportCache::WriteParamFrom

Set the value for the ["From" parameter (#data)](../../Main-Interface-of-Reports/Data-cache.md#data).
    
    
    MTAPIRES  IMTReportCache::WriteParamFrom(
       const INT64  from      // Value
       )

### Parameters

**from**  
[in] Value for the "From" parameter.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
