[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Data Cache Interfaces](../../Data-Cache-Interfaces.md) / [IMTReportCacheKeySet](../IMTReportCacheKeySet.md) / Reserve

[Previous](ContainsSet.md) | [Next](Insert.md)

# IMTReportCacheKeySet::Reserve

Reserve memory for keys in a set.
    
    
    MTAPIRES  IMTReportCacheKeySet::Reserve(
       const UINT  total      // Number of keys
       )

### Parameters

**total**  
[in] The number of keys, for which you want to reserve memory.

### Return Value

[MT_RET_OK](../../../Return-Codes/Successful-completion.md), if the passed set of keys exists in the current object.

### Note

Use this method before adding a set of keys to a set. By allocating memory in advance, you will save server time on allocating memory for each key separately.
