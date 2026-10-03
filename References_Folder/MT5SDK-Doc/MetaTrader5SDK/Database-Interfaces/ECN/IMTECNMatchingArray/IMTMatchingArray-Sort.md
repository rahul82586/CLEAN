[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNMatchingArray](../IMTMatchingArray.md) / IMTMatchingArray Sort

[Previous](IMTMatchingArray-Next.md) | [Next](IMTMatchingArray-Search.md)

# IMTECNMatchingArray::Sort

Sort an array using the passed sort function.
    
    
    MTAPIRES  IMTECNMatchingArray::Sort(
       MTSortFunctionPtr  sort_function      // sort function
       )

### Parameters

**sort_function**  
[in] A pointer to thesort function.

### Return Value

An indication of a successful execution is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

Positioning of elements after sorting is determined by sort_function.

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
