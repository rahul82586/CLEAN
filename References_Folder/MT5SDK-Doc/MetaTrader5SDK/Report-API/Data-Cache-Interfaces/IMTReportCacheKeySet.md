[🏠 Document Start](../../README.md) / [Report API](../README.md) / [Data Cache Interfaces](../Data-Cache-Interfaces.md) / IMTReportCacheKeySet

[Previous](IMTReportCacheValue/Next.md) | [Next](IMTReportCacheKeySet/Release.md)

# IMTReportCacheKeySet

IMTReportCacheKeySet is an auxiliary interface for describing a set of [data cache](../Main-Interface-of-Reports/Data-cache.md) keys. Use the interface to receive cache information for multiple keys without having to perform routine operations related to request preparation.

Method | Purpose  
---|---  
[Release](IMTReportCacheKeySet/Release.md) | Delete the current object.  
[Assign](IMTReportCacheKeySet/Assign.md) | Assign a passed object to the current one.  
[Clear](IMTReportCacheKeySet/Clear.md) | Clear an object.  
[Swap](IMTReportCacheKeySet/Swap.md) | Exchange key sets with the passed object.  
[Total](IMTReportCacheKeySet/Total.md) | Get the number of keys in the set.  
[Array](IMTReportCacheKeySet/Array.md) | Get keys from the set as a sorted array.  
[Next](IMTReportCacheKeySet/Next.md) | Get the next key from a sorted key array.  
[Search](IMTReportCacheKeySet/Search.md) | Search key in the array.  
[ContainsSet](IMTReportCacheKeySet/ContainsSet.md) | Check if the key set contains all the keys from the passed set.  
[Reserve](IMTReportCacheKeySet/Reserve.md) | Reserve memory for keys in a set.  
[Insert](IMTReportCacheKeySet/Insert.md) | Add a key to the current set.  
[InsertArray](IMTReportCacheKeySet/InsertArray.md) | Add an array of keys to the current set.  
[InsertSet](IMTReportCacheKeySet/InsertSet.md) | Add a key set to the current set.  
[Remove](IMTReportCacheKeySet/Remove.md) | Delete a key from the current set.  
[RemoveArray](IMTReportCacheKeySet/RemoveArray.md) | Delete an array of keys from the current set.  
[RemoveSet](IMTReportCacheKeySet/RemoveSet.md) | Delete a set of keys from the current set.
