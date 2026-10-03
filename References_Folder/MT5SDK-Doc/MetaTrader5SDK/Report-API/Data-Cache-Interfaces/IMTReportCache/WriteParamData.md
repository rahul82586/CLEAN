[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Data Cache Interfaces](../../Data-Cache-Interfaces.md) / [IMTReportCache](../IMTReportCache.md) / WriteParamData

[Previous](WriteParamString.md) | [Next](WriteParamKeySet.md)

# IMTReportCache::WriteParamData

Set the value for the ["Data" parameter (#data)](../../Main-Interface-of-Reports/Data-cache.md#data).
    
    
    MTAPIRES  IMTReportCache::WriteParamData(
       const void*  data,     // Data
       const UINT   size      // Data size
       )

### Parameters

**data**  
[in] A pointer to the data to be written to the "Data" parameter.

**size**  
[in] Size of "data" in bytes.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.
