[🏠 Document Start](../../README.md) / [Report API](../README.md) / [Data Cache Interfaces](../Data-Cache-Interfaces.md) / IMTReportCache

[Previous](../Data-Cache-Interfaces.md) | [Next](IMTReportCache/Release.md)

# IMTReportCache

IMTReportCache is the [data cache](../Main-Interface-of-Reports/Data-cache.md) description interface. It enables the receiving and writing of data to cache as the key — value pairs, parameters and dictionaries.

Method | Purpose  
---|---  
[Release](IMTReportCache/Release.md) | Delete the current object.  
[Name](IMTReportCache/Name.md) | Get the name of the data cache.  
[TimeLastWrite](IMTReportCache/TimeLastWrite.md) | Get the time of the last data cache change.  
[ValueCreate](IMTReportCache/ValueCreate.md) | Create a cache value object.  
[ReadBegin](IMTReportCache/ReadBegin.md) | Start data reading from the cache.  
[ReadEnd](IMTReportCache/ReadEnd.md) | Finish data reading from the cache.  
[ReadParamFrom](IMTReportCache/ReadParamFrom.md) | Get the value of the "From" parameter.  
[ReadParamTo](IMTReportCache/ReadParamTo.md) | Get the value of the "To" parameter.  
[ReadParamString](IMTReportCache/ReadParamString.md) | Get the value of the "String" parameter.  
[ReadParamData](IMTReportCache/ReadParamData.md) | Get the value of the "Data" parameter.  
[ReadParamKeySet](IMTReportCache/ReadParamKeySet.md) | Get the value of the "KeySet" parameter.  
[ReadValue](IMTReportCache/ReadValue.md) | Get the cache value with the specified key.  
[ReadValues](IMTReportCache/ReadValues.md) | Get multiple values from cache using a set of keys.  
[ReadMissingKeys](IMTReportCache/ReadMissingKeys.md) | Get the list of missing keys in cache.  
[ReadDictionaryPos](IMTReportCache/ReadDictionaryPos.md) | Get the position of a string (value) in the dictionary.  
[ReadDictionaryString](IMTReportCache/ReadDictionaryString.md) | Get the string (value) from a dictionary based on the position.  
[WriteBegin](IMTReportCache/WriteBegin.md) | Start writing data to the cache.  
[WriteEnd](IMTReportCache/WriteEnd.md) | Finish writing data to the cache.  
[WriteParamFrom](IMTReportCache/WriteParamFrom.md) | Set the value for the "From" parameter.  
[WriteParamTo](IMTReportCache/WriteParamTo.md) | Set the value for the "To" parameter.  
[WriteParamString](IMTReportCache/WriteParamString.md) | Set the value for the "String" parameter.  
[WriteParamData](IMTReportCache/WriteParamData.md) | Set the value for the "Data" parameter.  
[WriteParamKeySet](IMTReportCache/WriteParamKeySet.md) | Set the value for the "KeySet" parameter.  
[WriteValue](IMTReportCache/WriteValue.md) | Write the value for a key in the cache.  
[WriteMissingKeys](IMTReportCache/WriteMissingKeys.md) | Add missing keys to the cache.  
[WriteDictionaryString](IMTReportCache/WriteDictionaryString.md) | Add a string (value) to the dictionary and return its position.
