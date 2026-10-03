[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Positions](../../Positions.md) / [IMTPositionArray](../IMTPositionArray.md) / Search

[Previous](Sort.md) | [Next](SearchGreatOrEq.md)

# IMTPositionArray::Search

Search in an array the array element that matches the search key.
    
    
    int  IMTPositionArray::Search(
       const void         *key,              // Sort key
       MTSortFunctionPtr  sort_function      // Pointer to the search function
       )  const

### Parameters

***key**  
[in] A pointer to the sort key. The search algorithm guarantees that the search key will always be passed to the search function as the first parameter (const void *left).

**sort_function**  
[in] A pointer to theSearch function.

### Return Value

If successful, it returns the place of a position object that meets the search criteria. Otherwise, it returns -1.

### Note

For a successful search, an array must be sorted first by calling the [IMTPositionArray::Sort](Sort.md) method. The sorting function (algorithm) must correspond with the search function (algorithm) used.

### Example
    
    
    //+------------------------------------------------------------------+
    //| Function of comparing positions for sorting                      |
    //+------------------------------------------------------------------+
    int SortPositions(const void* left,const void* right)
      {
       IMTPosition* lft=*(IMTPosition**)left;
       IMTPosition* rgh=*(IMTPosition**)right;
    //--- Compare by login
       return CMTStr::Compare(lft->Login(), rgh->Login());
      }
    //+------------------------------------------------------------------+
    //| Function of comparing positions for searching                    |
    //+------------------------------------------------------------------+
    int SearchPositions(const void* left,const void* right)
      {
       UINT64        lft=(UINT64)left;
       IMTPosition*  rgh=*(IMTPosition**)right;
    //--- Compare by login
       return CMTStr::Compare(lft, rgh->Login());
      }
    //+------------------------------------------------------------------+
    //| Example of sorting and searching                                 |
    //+------------------------------------------------------------------+
    int Example()
      {
       IMTPositionArray*  array;
       UINT64             login;
       int                index;
       ...
    //--- Initializing and filling the array of positions
       ...
    //--- Sorting
       array->Sort(SortPositions);
    //--- Search
       index=array->Search(12345,SearchPositions);
    //---
       return(0);
      }
