[🏠 Document Start](../../../../README.md) / [Database Interfaces](../../../README.md) / [Trade](../../../Trade.md) / [Accounts](../../Accounts.md) / [IMTAccountArray](../IMTAccountArray.md) / Sort

[Previous](Next.md) | [Next](Search.md)

# IMTAccountArray::Sort

Sort an array using the sort function passed.
    
    
    MTAPIRES  IMTAccountArray::Sort(
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
    //| Function of comparing accounts for sorting                       |
    //+------------------------------------------------------------------+
    int SortAccounts(const void* left,const void* right)
      {
       IMTAccount* lft=*(IMTAccount**)left;
       IMTAccount* rgh=*(IMTAccount**)right;
    //--- Compare by login
       return CMTStr::Compare(lft->Login(), rgh->Login());
      }
    //+------------------------------------------------------------------+
    //| Function of comparing accounts for searching                     |
    //+------------------------------------------------------------------+
    int SearchAccounts(const void* left,const void* right)
      {
       UINT64        lft=(UINT64)left;
       IMTAccount*   rgh=*(IMTAccount**)right;
    //--- Compare by login
       return CMTStr::Compare(lft, rgh->Login());
      }
    //+------------------------------------------------------------------+
    //| Example of sorting and searching                                 |
    //+------------------------------------------------------------------+
    int Example()
      {
       IMTAccountArray*   array;
       UINT64             login;
       int                index;
       ...
    //--- Initializing and filling the array of accounts
       ...
    //--- Sorting
       array->Sort(SortAccounts);
    //--- Search
       index=array->Search(12345,SearchAccounts);
    //---
       return(0);
      }
