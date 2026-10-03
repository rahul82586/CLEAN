[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Floating Margin](../../Floating-Margin.md) / [IMTConLeverageArray](../IMTConLeverageArray.md) / Search

[Previous](Sort.md) | [Next](SearchGreatOrEq.md)

# IMTConLeverageArray::Search

Search an array for an element that matches the search key.
    
    
    int  IMTConLeverageArray::Search(
       const void         *key,              // Sort key
       MTSortFunctionPtr  sort_function      // Pointer to the search function
       )  const

### Parameters

***key**  
[in] Pointer to the sort key. The search algorithm guarantees that the search key will always be passed to the search function as the first parameter (const void *left).

**sort_function**  
[in] Pointer to thesearch function.

### Return Value

In case of success, the method returns the position of the configuration object that satisfies the search condition. Otherwise, -1 is returned.

### Note

For successful searching, the array must be pre-sorted by calling the [IMTConLeverageArray::Sort](Sort.md) method. The sorting function (algorithm) must correspond to the search function (algorithm) used.

### Example
    
    
    //+------------------------------------------------------------------+
    //| Function comparing elements for sorting                          |
    //+------------------------------------------------------------------+
    int SortParams(const void* left,const void* right)
      {
       IMTConLeverage* lft=*(IMTConLeverage**)left;
       IMTConLeverage* rgh=*(IMTConLeverage**)right;
    //--- compare by value
       return CMTStr::Name(lft->Symbol(), rgh->Name());
      }
    //+------------------------------------------------------------------+
    //| Parameter comparing function for search                          |
    //+------------------------------------------------------------------+
    int SearchParams(const void* left,const void* right)
      {
       LPCWSTR          lft=(LPCWSTR)left;
       IMTConLeverage*  rgh=*(IMTConLeverage**)right;
    //--- compare by value
       return CMTStr::Compare(lft, rgh->Name());
      }
    //+------------------------------------------------------------------+
    //| Sorting and search method example                                |
    //+------------------------------------------------------------------+
    int Example()
      {
       IMTConLeverageArray*  array;
       LPCWSTR               name;
       int                   index;
       ...
    //--- initialize and fill the the 'array' array of parameters
       ...
    //--- sorting
       array->Sort(SortParams);
    //--- Search
       index=array->Search(L"Night Rule",SearchParams);
    //---
       return(0);
      }
