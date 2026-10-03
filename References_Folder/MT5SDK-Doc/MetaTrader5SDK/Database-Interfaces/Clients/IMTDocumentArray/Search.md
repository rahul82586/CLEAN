[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTDocumentArray](../IMTDocumentArray.md) / Search

[Previous](Sort.md) | [Next](SearchGreatOrEq.md)

# IMTDocumentArray::Search

Search in an array for the array element matching the search key.
    
    
    int  IMTDocumentArray::Search(
       const void*        key,               // Sorting key
       MTSortFunctionPtr  sort_function      // A pointer to the search function
       )  const

### Parameters

**key**  
[in] A pointer to the sort key. The search algorithm guarantees that the search key will always be passed to the search function as the first parameter (const void *left).

**sort_function**  
[in] A pointer to thesearch function.

### Return Value

If successful, the method returns the position of a document object that meets the search criteria. Otherwise, -1 is returned.

### Note

For a successful search, an array must be sorted first by calling the [IMTDocumentArray::Sort](Sort.md) method. The sorting function (algorithm) must correspond to the search function (algorithm) used.

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
