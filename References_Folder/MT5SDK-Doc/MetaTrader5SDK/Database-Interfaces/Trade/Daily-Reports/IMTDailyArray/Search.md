[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Daily Reports](../../Daily-Reports.md) / [IMTDailyArray](../IMTDailyArray.md) / Search

[Previous](Sort.md) | [Next](SearchGreatOrEq.md)

# IMTDailyArray::Search

Search in an array the array element that matches the search key.
    
    
    int  IMTDailyArray::Search(
       const void         *key,              // Sort key
       MTSortFunctionPtr  sort_function      // Pointer to the search function
       )  const

### Parameters

***key**  
[in] A pointer to the sort key. The search algorithm guarantees that the search key will always be passed to the search function as the first parameter (const void *left).

**sort_function**  
[in] A pointer to theSearch function.

### Return Value

If successful, it returns the position of a daily report object that meets the search criteria. Otherwise, it returns -1.

### Note

For a successful search, an array must be sorted first by calling the [IMTDailyArray::Sort](Sort.md) method. The sorting function (algorithm) must correspond with the search function (algorithm) used.

### Example
    
    
    //+------------------------------------------------------------------+
    //| Function of comparing reports for sorting                        |
    //+------------------------------------------------------------------+
    int SortDaily(const void* left,const void* right)
      {
       IMTDaily* lft=*(IMTDaily**)left;
       IMTDaily* rgh=*(IMTDaily**)right;
    //--- Compare by login
       return CMTStr::Compare(lft->Login(), rgh->Login());
      }
    //+------------------------------------------------------------------+
    //| Function of comparing report for searching                       |
    //+------------------------------------------------------------------+
    int SearchDaily(const void* left,const void* right)
      {
       UINT64        lft=(UINT64)left;
       IMTDaily*     rgh=*(IMTDaily**)right;
    //--- Compare by login
       return CMTStr::Compare(lft, rgh->Login());
      }
    //+------------------------------------------------------------------+
    //| Example of sorting and searching                                 |
    //+------------------------------------------------------------------+
    int Example()
      {
       IMTDailyArray*     array;
       UINT64             login;
       int                index;
       ...
    //--- Initializing and filling the array of reports
       ...
    //--- Sorting
       array->Sort(SortDaily);
    //--- Search
       index=array->Search(12345,SearchDaily);
    //---
       return(0);
      }
