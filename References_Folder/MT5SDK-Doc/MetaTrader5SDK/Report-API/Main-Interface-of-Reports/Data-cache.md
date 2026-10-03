[🏠 Document Start](../../README.md) / [Report API](../README.md) / [Main Interface of Reports](../Main-Interface-of-Reports.md) / Data cache

[Previous](Dataset/RequestCreate.md) | [Next](Data-cache/ReportCacheCreate.md)

<a id="data-cache"></a>
# Data cache (#data-cache)

Data cache is used to store data requested from the trading platform database, between report generation times. Use of data cache saves resources when creating reports: there is no need to re-retrieve data from databases and perform related calculations, while the ready data is available in the cache.

Caches are stored on the trade server:

  * In memory, for quick access to frequently used data. The cache is automatically unloaded from the memory if it is not accessed within 2 days.
  * On a hard disk, for long-term access. The cache is automatically deleted from the disk if it is not accessed within 30 days.



<a id="type"></a>
## Cache types (#type)

There are two types of caches:

  * Permanent: data can only be added but cannot be deleted. It is permanently stored on the server and it is impossible to set time-to-live (TTL) for the data.
  * Temporary: temporary data can be added to this cache, with the explicit specification of the TTL for key-value pairs. After that time data is deleted from the cache.



<a id="data"></a>
## Cached data types (#data)

The cache allows storing data of three types: key-value pairs, dictionaries and parameters.

Key-value pairs are the main data in the cache. Methods [IMTReportCache::ReadValue*](../Data-Cache-Interfaces/IMTReportCache/ReadValue.md) and [IMTReportCache::WriteValue*](../Data-Cache-Interfaces/IMTReportCache/WriteValue.md) are used for working with them.

Dictionaries enable efficient operation with various listings, such as countries, cities, etc. Data in dictionaries is stored as an array of strings. Use methods [IMTReportCache::ReadDictionary*](../Data-Cache-Interfaces/IMTReportCache/ReadDictionaryPos.md) and [IMTReportCache::WriteDictionaryString](../Data-Cache-Interfaces/IMTReportCache/WriteDictionaryString.md) to work with the dictionary.

In addition, the cache has five optional parameters which the programmer can use for different purposes, for example, to describe the cache contents.

  * From — the beginning of data in the cache. To work with this parameter, use methods [IMTReportCache::ReadParamFrom](../Data-Cache-Interfaces/IMTReportCache/ReadParamFrom.md) and [IMTReportCache::WriteParamFrom](../Data-Cache-Interfaces/IMTReportCache/WriteParamFrom.md).
  * To — describes the end of data in the cache. To work with this parameter, use methods [IMTReportCache::ReadParamTo](../Data-Cache-Interfaces/IMTReportCache/ReadParamTo.md) and [IMTReportCache::WriteParamTo](../Data-Cache-Interfaces/IMTReportCache/WriteParamTo.md).
  * String — parameter for storing string data. To work with the parameter use methods [IMTReportCache::ReadParamString](../Data-Cache-Interfaces/IMTReportCache/ReadParamString.md) and [IMTReportCache::WriteParamString](../Data-Cache-Interfaces/IMTReportCache/WriteParamString.md).
  * Data — parameter for storing binary data. To work with the parameter use methods [IMTReportCache::ReadParamData](../Data-Cache-Interfaces/IMTReportCache/ReadParamData.md) and [IMTReportCache::WriteParamData](../Data-Cache-Interfaces/IMTReportCache/WriteParamData.md).
  * KeySet — parameter for storing a [set of keys](../Data-Cache-Interfaces/IMTReportCacheKeySet.md). To work with the parameter, use methods [IMTReportCache::ReadParamKeySet](../Data-Cache-Interfaces/IMTReportCache/ReadParamKeySet.md) and [IMTReportCache::WriteParamKeySet](../Data-Cache-Interfaces/IMTReportCache/WriteParamKeySet.md).



<a id="the-general-scheme-for-operations-with-the-cache"></a>
## The general scheme for operations with the cache (#the-general-scheme-for-operations-with-the-cache)

  * Create a cache object using the [ReportCacheCreate](Data-cache/ReportCacheCreate.md) method
  * Receive cache to it using the [ReportCacheGet](Data-cache/ReportCacheGet.md) or [ReportCacheGetTemporary](Data-cache/ReportCacheGetTemporary.md) method
  * Call [IMTReportCache::ReadBegin](../Data-Cache-Interfaces/IMTReportCache/ReadBegin.md) to start reading data. Then use [IMTReportCache::Read*](../Data-Cache-Interfaces/IMTReportCache/ReadParamFrom.md) methods. After finishing data reading call [IMTReportCache::ReadEnd](../Data-Cache-Interfaces/IMTReportCache/ReadEnd.md).
  * Call [IMTReportCache::WriteBegin](../Data-Cache-Interfaces/IMTReportCache/WriteBegin.md) to start writing data. Then use [IMTReportCache::Write*](../Data-Cache-Interfaces/IMTReportCache/WriteParamFrom.md) methods. After finishing data writing call [IMTReportCache::WriteEnd](../Data-Cache-Interfaces/IMTReportCache/WriteEnd.md). Note that only one report instance can be writing data to cache at a time.



Examples of operations with the data cache are provided in the source code of the Capital report, which is available in "[Report API installation directory]\Report\Examples\Capital.Standard.Reports".

<a id="list-functions"></a>
## List Functions (#list-functions)

The following functions are available for working with the data cache:

Function | Purpose  
---|---  
[ReportCacheCreate](Data-cache/ReportCacheCreate.md) | Create a data cache object.  
[ReportCacheGet](Data-cache/ReportCacheGet.md) | Call the permanent data cache by name and version.  
[ReportCacheGetTemporary](Data-cache/ReportCacheGetTemporary.md) | Call the temporary data cache by name and version.  
[KeySetCreate](Data-cache/KeySetCreate.md) | Create a key set object for working with the cached data.  
[KeySetParamLogins](Data-cache/KeySetParamLogins.md) | Fill the key set with the logins of trading accounts for which the report is generated.
