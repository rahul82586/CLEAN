[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Assets](../../Assets.md) / [IMTExposureArray](../IMTExposureArray.md) / Search

[Previous](Sort.md) | [Next](SearchGreatOrEq.md)

# IMTExposureArray::Search

Search in an array the array element that matches the search key.
    
    
    int  IMTExposureArray::Search(
       const void         *key,              // Sort key
       MTSortFunctionPtr  sort_function      // Sort function
       )  const

### Parameters

***key**  
[in] A pointer to the sort key. The search algorithm guarantees that the search key will always be passed to the search function as the first parameter (const void *left).

**sort_function**  
[in] A pointer to thesort function.

### Return Value

If successful, it returns the position of an asset record object that meets the search criteria. Otherwise, it returns -1.

### Note

For a successful search, an array must be sorted first by calling the [IMTExposureArray::Sort](Sort.md) method. The sorting function (algorithm) must correspond with the search function (algorithm) used.

### Example
    
    
    //+------------------------------------------------------------------+
    //| Function of comparing exposure for sorting                       |
    //+------------------------------------------------------------------+
    int SortExposure(const void* left,const void* right)
      {
       IMTExposure* lft=*(IMTExposure**)left;
       IMTExposure* rgh=*(IMTExposure**)right;
    //--- Compare by client volume
       return CMTStr::Compare(lft->VolumeClients(), rgh->VolumeClients());
      }
    //+------------------------------------------------------------------+
    //| Function of comparing exposure for searching                     |
    //+------------------------------------------------------------------+
    int SearchExposure(const void* left,const void* right)
      {
       double       lft=(double)left;
       IMTExposure* rgh=*(IMTExposure**)right;
    //--- Compare by client volume
       retrun CMTStr::Compare(lft, rgh->VolumeClients());
      }
    //+------------------------------------------------------------------+
    //| Example of sorting and searching                                 |
    //+------------------------------------------------------------------+
    int Example()
      {
       IMTExposureArray* array;
       double            VolumeClients;
       int               index;
       ...
    //--- Initializing and filling the array of exposures
       ...
    //--- Sorting
       array->Sort(SortExposure);
    //--- Search
       index=array->Search(345,SearchExposure);
    //---
       return(0);
      }
