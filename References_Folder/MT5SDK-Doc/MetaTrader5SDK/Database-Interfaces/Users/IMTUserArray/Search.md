[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Users](../../Users.md) / [IMTUserArray](../IMTUserArray.md) / Search

[Previous](Sort.md) | [Next](SearchGreatOrEq.md)

# IMTUserArray::Search

Search in an array the array element that matches the search key.
    
    
    int  IMTUserArray::Search(
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

For a successful search, an array must be sorted first by calling the [IMTUserArray::Sort](Sort.md) method. The sorting function (algorithm) must correspond with the search function (algorithm) used.

### Example
    
    
    //+------------------------------------------------------------------+
    //| Function of comparing users for sorting                          |
    //+------------------------------------------------------------------+
    int SortUsers(const void* left,const void* right)
      {
       IMTUser* lft=*(IMTUser**)left;
       IMTUser* rgh=*(IMTUser**)right;
    //--- Compare by login
       return CMTStr::Compare(lft->Login(), rgh->Login());
      }
    //+------------------------------------------------------------------+
    //| Function of comparing users for searching                        |
    //+------------------------------------------------------------------+
    int SearchUsers(const void* left,const void* right)
      {
       UINT64        lft=(UINT64)left;
       IMTUser*      rgh=*(IMTUser**)right;
    //--- Compare by login
       return CMTStr::Compare(lft, rgh->Login());
      }
    //+------------------------------------------------------------------+
    //| Example of sorting and searching                                 |
    //+------------------------------------------------------------------+
    int Example()
      {
       IMTUserArray*      array;
       UINT64             login;
       int                index;
       ...
    //--- Initialization and filling of the array of users
       ...
    //--- Sorting
       array->Sort(SortUsers);
    //--- Search
       index=array->Search(12345,SearchUsers);
    //---
       return(0);
      }
