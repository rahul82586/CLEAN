[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTDocumentArray](../IMTDocumentArray.md) / Sort

[Previous](Next.md) | [Next](Search.md)

# IMTDocumentArray::Sort

Sort an array using the passed sort function.
    
    
    MTAPIRES  IMTDocumentArray::Sort(
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
    //| Documents comparing function for sorting                         |
    //+------------------------------------------------------------------+
    int SortDocuments(const void* left,const void* right)
      {
       IMTDocument* lft=*(IMTDocument**)left;
       IMTDocument* rgh=*(IMTDocument**)right;
    //--- Compare by comment ID
       return CMTStr::Compare(lft->RecordID(), rgh->RecordID());
      }
    //+------------------------------------------------------------------+
    //| Documents comparing function for search                          |
    //+------------------------------------------------------------------+
    int SearchDocuments(const void* left,const void* right)
      {
       UINT64       lft=(UINT64)left;
       IMTDocument* rgh=*(IMTDocument**)right;
    //--- Compare by document ID
       return CMTStr::Compare(lft, rgh->RecordID());
      }
    //+------------------------------------------------------------------+
    //| Sorting and search method example                                |
    //+------------------------------------------------------------------+
    int Example()
      {
       IMTDocumentArray* array;
       UINT64            recordid;
       int               index;
       ...
    //--- initialize and fill the documents array 'array'
       ...
    //--- sorting
       array->Sort(SortDocuments);
    //--- search
       index=array->Search(12345,SearchDocuments);
    //---
       return(0);
      }
