[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTAttachmentArray](../IMTAttachmentArray.md) / SearchRight

[Previous](SearchLeft.md) | [Next](../../Users.md)

# IMTAttachmentArray::SearchRight

Search in an array for the last element equal to the search key.
    
    
    int  IMTAttachmentArray::SearchRight(
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
