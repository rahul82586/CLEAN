[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Orders](../../Orders.md) / [IMTOrderArray](../IMTOrderArray.md) / Search

[Previous](Sort.md) | [Next](SearchGreatOrEq.md)

# IMTOrderArray::Search

Search in an array the array element that matches the search key.
    
    
    int  IMTOrderArray::Search(
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

For a successful search, an array must be sorted first by calling the [IMTOrderArray::Sort](Sort.md) method. The sorting function (algorithm) must correspond with the search function (algorithm) used.

### Example
    
    
    //+------------------------------------------------------------------+
    //| Function of comparing orders for sorting                         |
    //+------------------------------------------------------------------+
    int SortOrders(const void* left,const void* right)
      {
       IMTOrder* lft=*(IMTOrder**)left;
       IMTOrder* rgh=*(IMTOrder**)right;
    //--- Compare by ticket
       return CMTStr::Compare(lft->Order(), rgh->Order());
      }
    //+------------------------------------------------------------------+
    //| Function of comparing orders for sorting                         |
    //+------------------------------------------------------------------+
    int SearchOrders(const void* left,const void* right)
      {
       UINT64    lft=(UINT64)left;
       IMTOrder* rgh=*(IMTOrder**)right;
    //--- Compare by ticket
       return CMTStr::Compare(lft, rgh->Order());
      }
    //+------------------------------------------------------------------+
    //| Example of sorting and searching                                 |
    //+------------------------------------------------------------------+
    int Example()
      {
       IMTOrderArray* array;
       UINT64         ticket;
       int            index;
       ...
    //--- Initializing and filling the array of orders
       ...
    //--- Sorting
       array->Sort(SortOrders);
    //--- Search
       index=array->Search(12345,SearchOrders);
    //---
       return(0);
      }
