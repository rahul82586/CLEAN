[🏠 Document Start](../../../README.md) / [Report API](../../README.md) / [Data Cache Interfaces](../../Data-Cache-Interfaces.md) / [IMTReportCache](../IMTReportCache.md) / ReadDictionaryString

[Previous](ReadDictionaryPos.md) | [Next](WriteBegin.md)

# IMTReportCache::ReadDictionaryString

Get the string (value) from a dictionary based on the position.
    
    
    MTAPIRES  IMTReportCache::ReadDictionaryString(
       const UINT  dictionary_id,     // Dictionary identifier
       const UINT  pos,               // Position
       LPCWSTR&    string             // String
       )

### Parameters

**dictionary_id**  
[in] Dictionary identifier.

**pos**  
[in] The position of the string in the dictionary.

**string**  
[in] String.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### 
