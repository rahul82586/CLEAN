[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNHistoryDealArray](../IMTHistoryDealArray.md) / IMTHistoryDealArray Search

[Previous](IMTHistoryDealArray-Sort.md) | [Next](IMTHistoryDealArray-SearchGreatOrEq.md)

# IMTECNHistoryDealArray::Search

Search in an array for the array element matching the search key.
    
    
    int  IMTECNHistoryDealArray::Search(
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

For a successful search, an array must first be sorted by calling the [IMTECNHistoryDealArray::Sort](IMTHistoryDealArray-Sort.md) method. The sorting function (algorithm) must correspond to the search function (algorithm) used.

### Example
    
    
    //+------------------------------------------------------------------+
    //| The function compares deals for sorting                          |
    //+------------------------------------------------------------------+
    int SortDeals(const void* left,const void* right)
      {
       IMTECNHistoryDeal* lft=*(IMTECNHistoryDeal**)left;
       IMTECNHistoryDeal* rgh=*(IMTECNHistoryDeal**)right;
    //--- compare by deal identifier
       if(lft->RecordID()<rgh->RecordID()) return(-1);
       if(lft->RecordID()>rgh->RecordID()) return(1);
    //---
       return(0);
      }
    //+------------------------------------------------------------------+
    //| The function compares deals for search                           |
    //+------------------------------------------------------------------+
    int SearchDeal(const void* left,const void* right)
      {
       UINT64             lft=(UINT64)left;
       IMTECNHistoryDeal* rgh=*(IMTECNHistoryDeal**)right;
    //--- compare by deal identifier
       if(lft<rgh->RecordID()) return(-1);
       if(lft>rgh->RecordID()) return(1);
    //---
       return(0);
      }
    //+------------------------------------------------------------------+
    //| Sorting and search method example                                |
    //+------------------------------------------------------------------+
    int Example()
      {
       IMTECNHistoryMatchingDeal* array;
       UINT64                     recordid;
       int                        index;
       ...
    //--- initializing and filling the array of deals 'array'
       ...
    //--- sort
       array->Sort(SortDeals);
    //--- search
       recordid=12345;
       index=array->Search(&recordid,SearchDeal);
    //---
       return(0);
      }
