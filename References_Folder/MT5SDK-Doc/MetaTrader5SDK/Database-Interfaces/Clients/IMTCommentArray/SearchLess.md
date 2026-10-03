[🏠 Document Start](../../../README.md) / [Database Interfaces](../../README.md) / [Clients](../../Clients.md) / [IMTCommentArray](../IMTCommentArray.md) / SearchLess

[Previous](SearchLessOrEq.md) | [Next](SearchLeft.md)

# IMTCommentArray::SearchLess

Search in an array for the first element less than the search key.
    
    
    int  IMTCommentArray::SearchLess(
       const void*        key,               // Sorting key
       MTSortFunctionPtr  sort_function      // A pointer to the search function
       )  const

### Parameters

**key**  
[in] A pointer to the sort key. The search algorithm guarantees that the search key will always be passed to the search function as the first parameter (const void *left).

**sort_function**  
[in] A pointer to thesearch function.

### Return Value

If successful, the method returns the position of a comment object that meets the search criteria. Otherwise, -1 is returned.

### Note

For a successful search, an array must be sorted first by calling the [IMTCommentArray::Sort](Sort.md) method. The sorting function (algorithm) must correspond to the search function (algorithm) used.
