[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNMatchingArray](../IMTMatchingArray.md) / IMTMatchingArray Search

[Previous](IMTMatchingArray-Sort.md) | [Next](IMTMatchingArray-SearchGreatOrEq.md)

# IMTECNMatchingArray::Search

Search in an array for the array element matching the search key.
    
    
    int  IMTECNMatchingArray::Search(
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

For a successful search, an array must first be sorted by calling the [IMTECNMatchingArray::Sort](IMTMatchingArray-Sort.md) method. The sorting function (algorithm) must correspond to the search function (algorithm) used.

### Example
    
    
    //+------------------------------------------------------------------+
    //| Matching order comparison function for sorting                   |
    //+------------------------------------------------------------------+
    int SortOrders(const void* left,const void* right)
      {
       IMTECNMatching* lft=*(IMTECNMatching**)left;
       IMTECNMatching* rgh=*(IMTECNMatching**)right;
    //--- compare by order identifier
       return CMTStr::Compare(lft->RecordID(), rgh->RecordID());
      }
    //+------------------------------------------------------------------+
    //| Matching order comparison function for search                    |
    //+------------------------------------------------------------------+
    int SearchOrder(const void* left,const void* right)
      {
       UINT64          lft=(UINT64)left;
       IMTECNMatching* rgh=*(IMTECNMatching**)right;
    //--- compare by order identifier
       return; CMTStr::Compare(lft, rgh->RecordID());
      }
    //+------------------------------------------------------------------+
    //| Sorting and search method example                                |
    //+------------------------------------------------------------------+
    int Example()
      {
       IMTECNMatchingArray* array;
       UINT64               recordid;
       int                  index;
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
