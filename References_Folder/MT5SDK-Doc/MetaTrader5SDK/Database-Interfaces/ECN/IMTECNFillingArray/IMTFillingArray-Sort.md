[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [ECN](../../ECN.md) / [IMTECNFillingArray](../IMTFillingArray.md) / IMTFillingArray Sort

[Previous](IMTFillingArray-Next.md) | [Next](IMTFillingArray-Search.md)

# IMTECNFillingArray::Sort

Sort an array using the passed sort function.
    
    
    MTAPIRES  IMTECNFillingArray::Sort(
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
    //| Function comparing filling orders for sorting                    |
    //+------------------------------------------------------------------+
    int SortOrders(const void* left,const void* right)
      {
       IMTECNFilling* lft=*(IMTECNFilling**)left;
       IMTECNFilling* rgh=*(IMTECNFilling**)right;
    //--- compare by order identifier
       return CMTStr::Compare(lft->RecordID(), rgh->RecordID());
      }
    //+------------------------------------------------------------------+
    //| Function comparing filling orders for search                     |
    //+------------------------------------------------------------------+
    int SearchOrder(const void* left,const void* right)
      {
       UINT64          lft=(UINT64)left;
       IMTECNFilling*  rgh=*(IMTECNFilling**)right;
    //--- compare by order identifier
       return CMTStr::Compare(lft, rgh->RecordID());
      }
    //+------------------------------------------------------------------+
    //| Sorting and search method example                                |
    //+------------------------------------------------------------------+
    int Example()
      {
       IMTECNFillingArray*  array;
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
