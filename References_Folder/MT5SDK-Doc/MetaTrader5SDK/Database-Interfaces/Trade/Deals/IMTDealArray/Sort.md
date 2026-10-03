[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Deals](../../Deals.md) / [IMTDealArray](../IMTDealArray.md) / Sort

[Previous](Next.md) | [Next](Search.md)

# IMTDealArray::Sort

Sort an array using the sort function passed.
    
    
    MTAPIRES  IMTDealArray::Sort(
       MTSortFunctionPtr  sort_function      // Sort function
       )

### Parameters

**sort_function**  
[in] A pointer to thesort function.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

Positioning of elements after sorting is determined by the sort function sort_function.

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
