[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTClientArray](../IMTClientArray.md) / Sort

[Previous](Next.md) | [Next](Search.md)

# IMTClientArray::Sort

Sort an array using the passed sort function.
    
    
    MTAPIRES  IMTClientArray::Sort(
       MTSortFunctionPtr  sort_function      // Sorting function
       )

### Parameters

**sort_function**  
[in] A pointer to thesort function.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code will be returned.

### Note

Positioning of elements after sorting is determined by sort_function.

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
