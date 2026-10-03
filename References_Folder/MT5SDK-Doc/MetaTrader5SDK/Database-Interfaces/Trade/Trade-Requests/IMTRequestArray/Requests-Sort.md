[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Trade Requests](../../Requests.md) / [IMTRequestArray](../Requests-IMTRequestArray.md) / Requests Sort

[Previous](Requests-Next.md) | [Next](Requests-Search.md)

# IMTRequestArray::Sort

Sort an array using the sort function passed.
    
    
    MTAPIRES  IMTRequestArray::Sort(
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
       UINT        lft=(UINT)left;
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
