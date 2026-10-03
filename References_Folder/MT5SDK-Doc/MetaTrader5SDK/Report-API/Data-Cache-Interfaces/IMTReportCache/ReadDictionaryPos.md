[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Data Cache Interfaces](../../Data-Cache-Interfaces.md) / [IMTReportCache](../IMTReportCache.md) / ReadDictionaryPos

[Previous](ReadMissingKeys.md) | [Next](ReadDictionaryString.md)

# IMTReportCache::ReadDictionaryPos

Get the position of a string (value) in the dictionary.
    
    
    MTAPIRES  IMTReportCache::ReadDictionaryPos(
       const UINT  dictionary_id,     // Dictionary identifier
       LPCWSTR     string,            // String
       UINT&       pos                // Position
       )

### Parameters

**dictionary_id**  
[in] Dictionary identifier.

**string**  
[in] The string the position of which is to be retrieved.

**pos**  
[in] The position of the string in the dictionary.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### 
