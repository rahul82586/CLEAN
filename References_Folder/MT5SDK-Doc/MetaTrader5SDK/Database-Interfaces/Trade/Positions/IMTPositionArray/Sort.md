[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Positions](../../Positions.md) / [IMTPositionArray](../IMTPositionArray.md) / Sort

[Previous](Next.md) | [Next](Search.md)

# IMTPositionArray::Sort

Sort an array using the sort function passed.
    
    
    MTAPIRES  IMTPositionArray::Sort(
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
    //| Function of comparing positions for sorting                      |
    //+------------------------------------------------------------------+
    int SortPositions(const void* left,const void* right)
      {
       IMTPosition* lft=*(IMTPosition**)left;
       IMTPosition* rgh=*(IMTPosition**)right;
    //--- Compare by login
       return CMTStr::Compare(lft->Login(), rgh->Login());
      }
    //+------------------------------------------------------------------+
    //| Function of comparing positions for searching                    |
    //+------------------------------------------------------------------+
    int SearchPositions(const void* left,const void* right)
      {
       UINT64        lft=(UINT64)left;
       IMTPosition*  rgh=*(IMTPosition**)right;
    //--- Compare by login
       return CMTStr::Compare(lft, rgh->Login());
      }
    //+------------------------------------------------------------------+
    //| Example of sorting and searching                                 |
    //+------------------------------------------------------------------+
    int Example()
      {
       IMTPositionArray*  array;
       UINT64             login;
       int                index;
       ...
    //--- Initializing and filling the array of positions
       ...
    //--- Sorting
       array->Sort(SortPositions);
    //--- Search
       index=array->Search(12345,SearchPositions);
    //---
       return(0);
      }
