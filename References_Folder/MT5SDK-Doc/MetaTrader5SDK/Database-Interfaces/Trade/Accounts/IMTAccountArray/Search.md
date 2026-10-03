[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Accounts](../../Accounts.md) / [IMTAccountArray](../IMTAccountArray.md) / Search

[Previous](Sort.md) | [Next](SearchGreatOrEq.md)

# IMTAccountArray::Search

Search in an array the array element that matches the search key.
    
    
    int  IMTAccountArray::Search(
       const void         *key,              // Sort key
       MTSortFunctionPtr  sort_function      // Pointer to the search function
       )  const

### Parameters

***key**  
[in] A pointer to the sort key. The search algorithm guarantees that the search key will always be passed to the search function as the first parameter (const void *left).

**sort_function**  
[in] A pointer to theSearch function.

### Return Value

If successful, it returns the position of a trade order object that meets the search criteria. Otherwise, it returns -1.

### Note

For a successful search, an array must be sorted first by calling the [IMTAccountArray::Sort](Sort.md) method. The sorting function (algorithm) must correspond with the search function (algorithm) used.

### Example
    
    
    //+------------------------------------------------------------------+
    //| Function of comparing accounts for sorting                       |
    //+------------------------------------------------------------------+
    int SortAccounts(const void* left,const void* right)
      {
       IMTAccount* lft=*(IMTAccount**)left;
       IMTAccount* rgh=*(IMTAccount**)right;
    //--- Compare by login
       return CMTStr::Compare(lft->Login(), rgh->Login());
      }
    //+------------------------------------------------------------------+
    //| Function of comparing accounts for searching                     |
    //+------------------------------------------------------------------+
    int SearchAccounts(const void* left,const void* right)
      {
       UINT64        lft=(UINT64)left;
       IMTAccount*   rgh=*(IMTAccount**)right;
    //--- Compare by login
       return CMTStr::Compare(lft, rgh->Login());
      }
    //+------------------------------------------------------------------+
    //| Example of sorting and searching                                 |
    //+------------------------------------------------------------------+
    int Example()
      {
       IMTAccountArray*   array;
       UINT64             login;
       int                index;
       ...
    //--- Initializing and filling the array of accounts
       ...
    //--- Sorting
       array->Sort(SortAccounts);
    //--- Search
       index=array->Search(12345,SearchAccounts);
    //---
       return(0);
      }
