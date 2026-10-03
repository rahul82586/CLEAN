[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Data Cache Interfaces](../../Data-Cache-Interfaces.md) / [IMTReportCache](../IMTReportCache.md) / WriteParamString

[Previous](WriteParamTo.md) | [Next](WriteParamData.md)

# IMTReportCache::WriteParamString

Set the value for the ["String" parameter (#data)](../../Main-Interface-of-Reports/Data-cache.md#data).
    
    
    MTAPIRES  IMTReportCache::WriteParamString(
       LPCWSTR  param      // Value
       )

### Parameters

**param**  
[in] Value for the "String" parameter.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
