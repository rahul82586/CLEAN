[🏠 Document Start](../../../README.md) / [Configuration Interfaces](../../README.md) / [Groups](../../Groups.md) / [IMTConGroupArray](../IMTConGroupArray.md) / Search

[Previous](Sort.md) | [Next](SearchGreatOrEq.md)

# IMTConGroupArray::Search

Search an array for an element that matches the search key.
    
    
    int  IMTConGroupArray::Search(
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

For a successful search, the array must be previously sorted by calling the [IMTConGroupArray::Sort](Sort.md) method. The sorting function (algorithm) must correspond to the search function (algorithm) used.

### Example
    
    
    //+------------------------------------------------------------------+
    //| Function comparing elements for sorting                          |
    //+------------------------------------------------------------------+
    int SortParams(const void* left,const void* right)
      {
       IMTConGroup* lft=*(IMTConGroup**)left;
       IMTConGroup* rgh=*(IMTConGroup**)right;
    //--- compare by value
       return CMTStr::Compare(lft->Group(), rgh->Group());
      }
    //+------------------------------------------------------------------+
    //| Parameter comparing function for search                          |
    //+------------------------------------------------------------------+
    int SearchParams(const void* left,const void* right)
      {
       LPCWSTR          lft=(LPCWSTR)left;
       IMTConGroup*     rgh=*(IMTConGroup**)right;
    //--- compare by value
       return CMTStr::Compare(lft, rgh->Group());
      }
    //+------------------------------------------------------------------+
    //| Sort and search method example                                   |
    //+------------------------------------------------------------------+
    int Example()
      {
       IMTConGroupArray*   array;
       LPCWSTR             group;
       int                 index;
       ...
    //--- initialize and fill the the 'array' array of parameters
       ...
    //--- sort
       array->Sort(SortParams);
    //--- search
       index=array->Search(L"demo",SearchParams);
    //---
       return(0);
      }
