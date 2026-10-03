[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Data Cache Interfaces](../../Data-Cache-Interfaces.md) / [IMTReportCache](../IMTReportCache.md) / WriteDictionaryString

[Previous](WriteMissingKeys.md) | [Next](../IMTReportCacheValue.md)

# IMTReportCache::WriteDictionaryString

Add a string (value) to the dictionary and return its position.
    
    
    MTAPIRES  IMTReportCache::WriteDictionaryString(
       const UINT  dictionary_id,     // Dictionary identifier
       LPCWSTR     string,            // String
       UINT&       pos                // Position
       )

### Parameters

**dictionary_id**  
[in] Dictionary identifier. If the dictionary with the specified ID does not exist, it will be created.

**string**  
[in] The string to add.

**pos**  
[out] The position in the dictionary, at which the string was added.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### 
