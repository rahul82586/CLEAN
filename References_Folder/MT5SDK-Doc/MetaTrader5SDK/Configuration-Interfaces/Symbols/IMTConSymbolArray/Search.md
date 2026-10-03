[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Symbols](../../Symbols.md) / [IMTConSymbolArray](../IMTConSymbolArray.md) / Search

[Previous](Sort.md) | [Next](SearchGreatOrEq.md)

# IMTConSymbolArray::Search

Search an array for an element that matches the search key.
    
    
    int  IMTConSymbolArray::Search(
       const void         *key,              // Sort key
       MTSortFunctionPtr  sort_function      // Pointer to search function
       )  const

### Parameters

***key**  
[in] A pointer to the sort key. The search algorithm guarantees that the search key will always be passed to the search function as the first parameter (const void *left).

**sort_function**  
[in] A pointer to thesearch function.

### Return Value

If successful, the method returns the position of the object that meets the search criteria. Otherwise, -1 is returned.

### Note

For a successful search, the array must be previously sorted by calling the [IMTConSymbolArray::Sort](Sort.md) method. The sorting function (algorithm) must correspond to the search function (algorithm) used.

### Example
    
    
    //+------------------------------------------------------------------+
    //| Function comparing elements for sorting                          |
    //+------------------------------------------------------------------+
    int SortParams(const void* left,const void* right)
      {
       IMTConSymbol* lft=*(IMTConSymol**)left;
       IMTConSymbol* rgh=*(IMTConSymbol**)right;
    //--- compare by value
       return CMTStr::Compare(lft->Symbol(), rgh->Symbol());
      }
    //+------------------------------------------------------------------+
    //| Parameter comparing function for search                          |
    //+------------------------------------------------------------------+
    int SearchParams(const void* left,const void* right)
      {
       LPCWSTR          lft=(LPCWSTR)left;
       IMTConSymbol*    rgh=*(IMTConSymbol**)right;
    //--- compare by value
       return (CMTStr::Compare(lft, rgh->Symbol());
      }
    //+------------------------------------------------------------------+
    //| Sort and search method example                                   |
    //+------------------------------------------------------------------+
    int Example()
      {
       IMTConSymbolArray*  array;
       LPCWSTR             symbol;
       int                 index;
       ...
    //--- initialize and fill the the 'array' array of parameters
       ...
    //--- sort
       array->Sort(SortParams);
    //--- search
       index=array->Search(L"EURUSD",SearchParams);
    //---
       return(0);
      }
