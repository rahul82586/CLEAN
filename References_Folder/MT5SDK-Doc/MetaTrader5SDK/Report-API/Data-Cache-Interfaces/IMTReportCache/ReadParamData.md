[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Data Cache Interfaces](../../Data-Cache-Interfaces.md) / [IMTReportCache](../IMTReportCache.md) / ReadParamData

[Previous](ReadParamString.md) | [Next](ReadParamKeySet.md)

# IMTReportCache::ReadParamData

Get the value of the ["Data" parameter (#data)](../../Main-Interface-of-Reports/Data-cache.md#data).
    
    
    const void*  IMTReportCache::ReadParamData(
       UINT&  size      // data size
       )

### Parameters

**size**  
[out] The size of the received data in bytes.

### Return Value

A pointer to the value of the "Data" parameter.

### 
