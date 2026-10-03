[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryFillingArray](../IMTHistoryFillingArray.md) / IMTHistoryFillingArray Search

[Previous](IMTHistoryFillingArray-Sort.md) | [Next](IMTHistoryFillingArray-SearchGreatOrEq.md)

# IMTECNHistoryFillingArray::Search

Search in an array for the array element matching the search key.
    
    
    int  IMTECNHistoryFillingArray::Search(
       const void*        key,               // sorting key
       MTSortFunctionPtr  sort_function      // a pointer to the search array
       )  const

### Parameters

**key**  
[in] A pointer to the sorting key. The search algorithm guarantees that the search key will always be passed to the search function as the first parameter (const void *left).

**sort_function**  
[in] A pointer to thesearch function.

### Return Value

If successful, the method returns the position of the order object that meets the search criteria. Otherwise, -1 is returned.

### Note

For a successful search, an array must first be sorted by calling the [IMTECNHistoryFillingArray::Sort](IMTHistoryFillingArray-Sort.md) method. The sorting function (algorithm) must correspond to the search function (algorithm) used.

### Example
    
    
    //+------------------------------------------------------------------+
    //| Function comparing filling orders for sorting                    |
    //+------------------------------------------------------------------+
    int SortOrders(const void* left,const void* right)
      {
       IMTECNHistoryFilling* lft=*(IMTECNHistoryFilling**)left;
       IMTECNHistoryFilling* rgh=*(IMTECNHistoryFilling**)right;
    //--- compare by order identifier
       return CMTStr::Compare(lft->RecordID(), rgh->RecordID());
      }
    //+------------------------------------------------------------------+
    //| Function comparing filling orders for search                     |
    //+------------------------------------------------------------------+
    int SearchOrder(const void* left,const void* right)
      {
       UINT64                 lft=(UINT64)left;
       IMTECNHistoryFilling*  rgh=*(IMTECNHistoryFilling**)right;
    //--- compare by order identifier
       return CMTStr::Compare(lft, rgh->RecordID());
      }
    //+------------------------------------------------------------------+
    //| Sorting and search method example                                |
    //+------------------------------------------------------------------+
    int Example()
      {
       IMTECNHistoryFillingArray*  array;
       UINT64                      recordid;
       int                         index;
       ...
    //--- initializing and filling the array of orders 'array'
       ...
    //--- sort
       array->Sort(SortOrders);
    //--- search
       index=array->Search(12345,SearchOrders);
    //---
       return(0);
      }
