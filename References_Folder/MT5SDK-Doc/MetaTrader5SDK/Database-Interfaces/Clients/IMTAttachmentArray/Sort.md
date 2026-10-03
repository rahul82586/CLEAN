[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTAttachmentArray](../IMTAttachmentArray.md) / Sort

[Previous](Next.md) | [Next](Search.md)

# IMTAttachmentArray::Sort

Sort an array using the passed sort function.
    
    
    MTAPIRES  IMTAttachmentArray::Sort(
       MTSortFunctionPtr  sort_function      // sort function
       )

### Parameters

**sort_function**  
[in] A pointer to thesort function.

### Return Value

An indication of successful completion is the [MT_RET_OK](../../../Return-Codes/Successful-completion.md) response code. Otherwise, an error code is returned.

### Note

Positioning of elements after sorting is determined by the sort function sort_function.

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
