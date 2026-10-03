[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTRequestArray](../Requests-IMTRequestArray.md) / Requests Search

[Previous](Requests-Sort.md) | [Next](Requests-SearchGreatOrEq.md)

# IMTRequestArray::Search

Search in an array the array element that matches the search key.
    
    
    int  IMTRequestArray::Search(
       const void         *key,              // Sort key
       MTSortFunctionPtr  sort_function      // Pointer to the search function
       )  const

### Parameters

***key**  
[in] A pointer to the sort key. The search algorithm guarantees that the search key will always be passed to the search function as the first parameter (const void *left).

**sort_function**  
[in] A pointer to theSearch function.

### Return Value

If successful, it returns the position of a trade request object that meets the search criteria. Otherwise, it returns -1.

### Note

For a successful search, an array must be sorted first by calling the [IMTRequestArray::Sort](Requests-Sort.md) method. The sorting function (algorithm) must correspond with the search function (algorithm) used.

### Example
    
    
    //+------------------------------------------------------------------+
    //| Function of comparing requests for sorting                       |
    //+------------------------------------------------------------------+
    int SortReuqests(const void* left,const void* right)
      {
       IMTRequest* lft=*(IMTRequest**)left;
       IMTRequest* rgh=*(IMTRequest**)right;
    //--- Compare by request id
       return CMTStr::Compare(lft->ID(), rgh->ID());
      }
    //+------------------------------------------------------------------+
    //| Function of comparing requests for searching                     |
    //+------------------------------------------------------------------+
    int SearchRequests(const void* left,const void* right)
      {
       UINT        lft=*(UINT*)left;
       IMTRequest* rgh=*(IMTRequest**)right;
    //--- Compare by request id
       return CMTStr::Compare(lft, rgh->ID());
      }
    //+------------------------------------------------------------------+
    //| Example of sorting and searching                                 |
    //+------------------------------------------------------------------+
    int Example()
      {
       IMTRequestArray* array;
       UINT             ID;
       int              index;
       ...
    //--- Initializing and filling the array of requests
       ...
    //--- Sorting
       array->Sort(SortRequests);
    //--- Search
       index=array->Search(12345,SearchRequests);
    //---
       return(0);
      }
