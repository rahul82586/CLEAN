[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Daily Reports](../../Daily-Reports.md) / [IMTDailyArray](../IMTDailyArray.md) / Sort

[Previous](Next.md) | [Next](Search.md)

# IMTDailyArray::Sort

Sort an array using the sort function passed.
    
    
    MTAPIRES  IMTDailyArray::Sort(
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
    //| Function of comparing reports for sorting                        |
    //+------------------------------------------------------------------+
    int SortDaily(const void* left,const void* right)
      {
       IMTDaily* lft=*(IMTDaily**)left;
       IMTDaily* rgh=*(IMTDaily**)right;
    //--- Compare by login
       return CMTStr::Compare(lft->Login(), rgh->Login());
      }
    //+------------------------------------------------------------------+
    //| Function of comparing report for searching                       |
    //+------------------------------------------------------------------+
    int SearchDaily(const void* left,const void* right)
      {
       UINT64        lft=(UINT64)left;
       IMTDaily*     rgh=*(IMTDaily**)right;
    //--- Compare by login
       return CMTStr::Compare(lft, rgh->Login());
      }
    //+------------------------------------------------------------------+
    //| Example of sorting and searching                                 |
    //+------------------------------------------------------------------+
    int Example()
      {
       IMTDailyArray*     array;
       UINT64             login;
       int                index;
       ...
    //--- Initializing and filling the array of reports
       ...
    //--- Sorting
       array->Sort(SortDaily);
    //--- Search
       index=array->Search(12345,SearchDaily);
    //---
       return(0);
      }
