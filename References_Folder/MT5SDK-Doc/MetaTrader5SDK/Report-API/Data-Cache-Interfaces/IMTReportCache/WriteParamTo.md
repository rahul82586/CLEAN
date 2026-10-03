[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Data Cache Interfaces](../../Data-Cache-Interfaces.md) / [IMTReportCache](../IMTReportCache.md) / WriteParamTo

[Previous](WriteParamFrom.md) | [Next](WriteParamString.md)

# IMTReportCache::WriteParamTo

Set the value for the ["To" parameter (#data)](../../Main-Interface-of-Reports/Data-cache.md#data).
    
    
    MTAPIRES  IMTReportCache::WriteParamTo(
       const INT64  to      // Value
       )

### Parameters

**to**  
[in] Value for the "To" parameter

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
