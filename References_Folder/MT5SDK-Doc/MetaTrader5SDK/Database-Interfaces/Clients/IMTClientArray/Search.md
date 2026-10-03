[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTClientArray](../IMTClientArray.md) / Search

[Previous](Sort.md) | [Next](SearchGreatOrEq.md)

# IMTClientArray::Search

Search in an array for the array element matching the search key.
    
    
    int  IMTClientArray::Search(
       const void*        key,               // Sorting key
       MTSortFunctionPtr  sort_function      // A pointer to the search function
       )  const

### Parameters

**key**  
[in] A pointer to the sorting key. The search algorithm guarantees that the search key will always be passed to the search function as the first parameter (const void *left).

**sort_function**  
[in] A pointer to thesearch function.

### Return Value

If successful, the method returns the position of a client object that meets the search criteria. Otherwise, -1 is returned.

### Note

For a successful search, an array must be sorted first by calling the [IMTClientArray::Sort](Sort.md) method. The sorting function (algorithm) must correspond to the search function (algorithm) used.

### Example
    
    
    //+------------------------------------------------------------------+
    //| Clients comparing function for sorting                           |
    //+------------------------------------------------------------------+
    int SortClients(const void* left,const void* right)
      {
       IMTClient* lft=*(IMTClient**)left;
       IMTClient* rgh=*(IMTClient**)right;
    //--- Compare by client ID
       return CMTStr::Compare(lft->RecordID(), rgh->RecordID());
      }
    //+------------------------------------------------------------------+
    //| Clients comparing function for search                            |
    //+------------------------------------------------------------------+
    int SearchClients(const void* left,const void* right)
      {
       UINT64     lft=(UINT64)left;
       IMTClient* rgh=*(IMTClient**)right;
    //--- Compare by client ID
       return CMTStr::Compare(lft, rgh->RecordID());
      }
    //+------------------------------------------------------------------+
    //| Sorting and search method example                                |
    //+------------------------------------------------------------------+
    int Example()
      {
       IMTClientArray* array;
       UINT64          recordid;
       int             index;
       ...
    //--- initialize and fill the clients array 'array'
       ...
    //--- sorting
       array->Sort(SortClients);
    //--- search
       index=array->Search(12345,SearchClients);
    //---
       return(0);
      }
