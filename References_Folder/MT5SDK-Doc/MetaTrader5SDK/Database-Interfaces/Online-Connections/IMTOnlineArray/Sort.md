[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Online Connections](../../Online-Connections.md) / [IMTOnlineArray](../IMTOnlineArray.md) / Sort

[Previous](Next.md) | [Next](Search.md)

# IMTOnlineArray::Sort

Sort an array using the sort function passed.
    
    
    MTAPIRES  IMTOnlineArray::Sort(
       MTSortFunctionPtr  sort_function      // Sort function
       )

### Parameters

**sort_function**  
[in] A pointer to thesort function.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

Positioning of elements after sorting is determined by the sort function sort_function.

### Example
    
    
    //+------------------------------------------------------------------+
    //| The function compares connection records for sorting             |
    //+------------------------------------------------------------------+
    int SortOnline(const void* left,const void* right)
      {
       IMTOnline* lft=*(IMTOnline**)left;
       IMTOnline* rgh=*(IMTOnline**)right;
    //--- Comparing by login
       return CMTStr::Compare(lft->Login(), rgh->Login());
      }
    //+------------------------------------------------------------------+
    //| The function compares connection records for search              |
    //+------------------------------------------------------------------+
    int SearchOnline(const void* left,const void* right)
      {
       UINT64        lft=(UINT64)left;
       IMTOnline*    rgh=*(IMTOnline**)right;
    //--- Comparing by login
       return CMTStr::Compare(lft, rgh->Login());
      }
    //+------------------------------------------------------------------+
    //| Example of sort and search method                                |
    //+------------------------------------------------------------------+
    int Example()
      {
       IMTOnlineArray*    array;
       UINT64             login;
       int                index;
       ...
    //--- Initializing and filling the array of records 'array'
       ...
    //--- Sorting
       array->Sort(SortOnline);
    //--- Search
       index=array->Search(12345,SearchOnline);
    //---
       return(0);
      }
