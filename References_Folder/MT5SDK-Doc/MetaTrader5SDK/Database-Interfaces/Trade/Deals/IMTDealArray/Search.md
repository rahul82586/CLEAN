[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Deals](../../Deals.md) / [IMTDealArray](../IMTDealArray.md) / Search

[Previous](Sort.md) | [Next](SearchGreatOrEq.md)

# IMTDealArray::Search

Search in an array the array element that matches the search key.
    
    
    int  IMTDealArray::Search(
       const void         *key,              // Sort key
       MTSortFunctionPtr  sort_function      // Pointer to the search function
       )  const

### Parameters

***key**  
[in] A pointer to the sort key. The search algorithm guarantees that the search key will always be passed to the search function as the first parameter (const void *left).

**sort_function**  
[in] A pointer to theSearch function.

### Return Value

If successful, it returns the position of a deal object that meets the search criteria. Otherwise, it returns -1.

### Note

For a successful search, an array must be sorted first by calling the [IMTDealArray::Sort](Sort.md) method. The sorting function (algorithm) must correspond with the search function (algorithm) used.

### Example
    
    
    //+------------------------------------------------------------------+
    //| Function of comparing deals for sorting                          |
    //+------------------------------------------------------------------+
    int SortDeals(const void* left,const void* right)
      {
       IMTDeal* lft=*(IMTDeal**)left;
       IMTDeal* rgh=*(IMTDeal**)right;
    //--- Compare by ticket
       return CMTStr::Compare(lft->Deal(), rgh->Deal());
      }
    //+------------------------------------------------------------------+
    //| Function of comparing deals for searching                        |
    //+------------------------------------------------------------------+
    int SearchDeals(const void* left,const void* right)
      {
       UINT64    lft=(UINT64)left;
       IMTDeal*  rgh=*(IMTDeal**)right;
    //--- Compare by ticket
       return CMTStr::Compare(lft, rgh->Deal());
      }
    //+------------------------------------------------------------------+
    //| Example of sorting and searching                                 |
    //+------------------------------------------------------------------+
    int Example()
      {
       IMTDealArray*  array;
       UINT64         ticket;
       int            index;
       ...
    //--- Initializing and sorting the array of deals
       ...
    //--- Sorting
       array->Sort(SortDeals);
    //--- Search
       index=array->Search(12345,SearchDeals);
    //---
       return(0);
      }
