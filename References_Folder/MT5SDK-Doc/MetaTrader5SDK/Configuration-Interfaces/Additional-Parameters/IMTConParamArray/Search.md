[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Additional Parameters](../../Additional-Parameters.md) / [IMTConParamArray](../IMTConParamArray.md) / Search

[Previous](Sort.md) | [Next](SearchGreatOrEq.md)

# IMTConParamArray::Search

Search in an array the array element that matches the search key.
    
    
    int  IMTConParamArray::Search(
       const void         *key,              // Sort key
       MTSortFunctionPtr  sort_function      // Pointer to the search function
       )  const

### Parameters

***key**  
[in] A pointer to the sort key. The search algorithm guarantees that the search key will always be passed to the search function as the first parameter (const void *left).

**sort_function**  
[in] A pointer to theSearch function.

### Return Value

If successful, it returns the position of the parameter object that meets the search criteria. Otherwise, it returns -1.

### Note

For a successful search, an array must be sorted first by calling the [IMTConParamArray::Sort](Sort.md) method. The sorting function (algorithm) must correspond with the search function (algorithm) used.

### Example
    
    
    //+------------------------------------------------------------------+
    //| Function of comparing parameters for sorting                     |
    //+------------------------------------------------------------------+
    int SortParams(const void* left,const void* right)
      {
       IMTConParam* lft=*(IMTConParam**)left;
       IMTConParam* rgh=*(IMTConParam**)right;
    //--- Compare by value
       return CMTStr::Compare(lft->ValueInt(), rgh->ValueInt());
      }
    //+------------------------------------------------------------------+
    //| Function of comparing parameters for searching                   |
    //+------------------------------------------------------------------+
    int SearchParams(const void* left,const void* right)
      {
       INT64         lft=(INT64)left;
       IMTConParam*  rgh=*(IMTConParam**)right;
    //--- Compare by value
       return CMTStr::Compare(lft, rgh->ValueInt());
      }
    //+------------------------------------------------------------------+
    //| Example of sorting and searching                                 |
    //+------------------------------------------------------------------+
    int Example()
      {
       IMTConParamArray*  array;
       INT64              ValueInt;
       int                index;
       ...
    //--- Initializing and filling of the array of parameters
       ...
    //--- Sorting
       array->Sort(SortParams);
    //--- Search
       index=array->Search(12345,SearchParams);
    //---
       return(0);
      }
