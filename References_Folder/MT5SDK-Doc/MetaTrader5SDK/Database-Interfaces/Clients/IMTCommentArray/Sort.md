[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTCommentArray](../IMTCommentArray.md) / Sort

[Previous](Next.md) | [Next](Search.md)

# IMTCommentArray::Sort

Sort an array using the passed sort function.
    
    
    MTAPIRES  IMTCommentArray::Sort(
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
    //| Comments comparing function for sorting                          |
    //+------------------------------------------------------------------+
    int SortComments(const void* left,const void* right)
      {
       IMTComment* lft=*(IMTComment**)left;
       IMTComment* rgh=*(IMTComment**)right;
    //--- Compare by comment ID
       return CMTStr::Compare(lft->RecordID(), rgh->RecordID());
      }
    //+------------------------------------------------------------------+
    //| Comments comparing function for search                           |
    //+------------------------------------------------------------------+
    int SearchComments(const void* left,const void* right)
      {
       UINT64     lft=(UINT64)left;
       IMTComment* rgh=*(IMTComment**)right;
    //--- Compare by comment ID
       return CMTStr::Compare(lft, rgh->RecordID());
      }
    //+------------------------------------------------------------------+
    //| Sorting and search method example                                |
    //+------------------------------------------------------------------+
    int Example()
      {
       IMTCommentArray* array;
       UINT64           recordid;
       int              index;
       ...
    //--- initialize and fill the comments array 'array'
       ...
    //--- sorting
       array->Sort(SortComments);
    //--- search
       index=array->Search(12345,SearchComments);
    //---
       return(0);
      }
