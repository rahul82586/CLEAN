[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTAttachmentArray](../IMTAttachmentArray.md) / Search

[Previous](Sort.md) | [Next](SearchGreatOrEq.md)

# IMTAttachmentArray::Search

Search in an array for the array element matching the search key.
    
    
    int  IMTAttachmentArray::Search(
       const void*        key,               // Sorting key
       MTSortFunctionPtr  sort_function      // A pointer to the search function
       )  const

### Parameters

**key**  
[in] A pointer to the sort key. The search algorithm guarantees that the search key will always be passed to the search function as the first parameter (const void *left).

**sort_function**  
[in] A pointer to theSearch function.

### Return Value

If successful, the method returns the position of a document object that meets the search criteria. Otherwise, it returns -1.

### Note

For a successful search, an array must be sorted first by calling the [IMTAttachmentArray::Sort](Sort.md) method. The sorting function (algorithm) must correspond to the search function (algorithm) used.

### The example
    
    
    //+------------------------------------------------------------------+
    //| Function that compares attachments to sort them                  |
    //+------------------------------------------------------------------+
    int SortAttachments(const void* left,const void* right)
      {
       IMTAttachment* lft=*(IMTAttachment**)left;
       IMTAttachment* rgh=*(IMTAttachment**)right;
    //--- compare by attachment ID
       return CMTStr::Compare(lft->RecordID(), rgh->RecordID());
      }
    //+------------------------------------------------------------------+
    //| Function that compares attachments to search                     |
    //+------------------------------------------------------------------+
    int SearchAttachments(const void* left,const void* right)
      {
       UINT64         lft=(UINT64)left;
       IMTAttachment* rgh=*(IMTAttachment**)right;
    //--- compare by attachment ID
       return CMTStr::Compare(lft, rgh->RecordID());
      }
    //+------------------------------------------------------------------+
    //| Sorting and search method example                                |
    //+------------------------------------------------------------------+
    int Example()
      {
       IMTAttachmentArray* array;
       UINT64            recordid;
       int               index;
       ...
    //--- initialize and fill the 'array' array of attachments
       ...
    //--- sorting
       array->Sort(SortAttachments);
    //--- search
       index=array->Search(12345,SearchAttachments);
    //---
       return(0);
      }
